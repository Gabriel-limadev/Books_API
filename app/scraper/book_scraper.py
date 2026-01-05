import re  # Regex para extração de dados a partir de texto
from urllib.parse import urljoin  # Utilizado para montar URLs absolutas

# Bibliotecas do Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookScraper:
    """
    Classe responsável por realizar o scraping dos livros
    disponíveis no site books.toscrape.com
    """

    BASE_URL = "https://books.toscrape.com/index.html"

    def __init__(self, headless=True):
        """
        Inicializa e configura o WebDriver do Selenium
        """

        options = Options()

        # Configurações do navegador
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        # Inicialização do driver e do WebDriverWait
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def get_all_book_links(self):
        """
        Navega por todas as páginas do site e coleta os links individuais de cada livro.

        Retorna:
            list[str]: Lista com as URLs de todos os livros
        """

        self.driver.get(self.BASE_URL)

        # Garante que a página foi carregada
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        links = []

        while True:
            # Aguarda os containers dos livros estarem disponíveis
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.image_container a"))
            )

            books = self.driver.find_elements(By.CSS_SELECTOR, "div.image_container a")

            # Extrai os links dos livros
            links.extend(b.get_attribute("href") for b in books)

            try:
                # Verifica se existe botão de próxima página
                next_btn = self.driver.find_element(
                    By.CSS_SELECTOR, "ul.pager li.next a"
                )

                # Navega para a próxima página
                self.driver.get(next_btn.get_attribute("href"))

            except:
                # Se não existir botão de próxima página, encerra o loop
                break

        return links

    def parse_book_page(self, book_link):
        """
        Acessa a página individual de um livro e extrai todas as informações relevantes.

        Args:
            book_link (str): URL da página do livro

        Retorna:
            dict: Dicionário contendo os dados do livro
        """

        self.driver.get(book_link)

        # Aguarda o título do livro estar visível
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        # Extrai o ID do livro a partir da URL
        book_id = int(re.search(r"_(\d+)/index\.html", book_link).group(1))

        title = self.driver.find_element(By.TAG_NAME, "h1").text

        # Captura o preço e remove o símbolo da moeda
        price = self.driver.find_element(By.CSS_SELECTOR, "p.price_color").text
        price = price.replace("£", "").strip()

        # Captura a classificação por estrelas em texto
        rating_word = (
            self.driver.find_element(By.CSS_SELECTOR, "p.star-rating")
            .get_attribute("class")
            .split()[1]
        )

        # Mapeia o texto da classificação para valor numérico
        rating_map = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
        }
        rating = rating_map[rating_word]

        # Captura a disponibilidade em estoque
        availability_text = self.driver.find_element(
            By.CSS_SELECTOR, "p.instock.availability"
        ).text

        availability = int(re.search(r"\d+", availability_text).group())

        # Captura a categoria do livro
        category = self.driver.find_element(
            By.CSS_SELECTOR, "ul.breadcrumb li:nth-child(3) a"
        ).text

        # Captura a URL da imagem do livro
        image_src = self.driver.find_element(
            By.CSS_SELECTOR, "div.item.active img"
        ).get_attribute("src")

        image_url = urljoin(self.driver.current_url, image_src)

        return {
            "id": book_id,
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability,
            "category": category,
            "image": image_url,
        }

    def scrape_all_books(self):
        """
        Executa o processo completo de scraping:
        - Coleta os links de todos os livros
        - Extrai os dados individuais de cada livro

        Retorna:
            list[dict]: Lista com os dados de todos os livros
        """

        links = self.get_all_book_links()
        return [self.parse_book_page(link) for link in links]

    def close(self):
        """
        Encerra o WebDriver e libera os recursos
        """

        self.driver.quit()