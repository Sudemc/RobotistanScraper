from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class RobotistanScraper:
    def __init__(self, base_url="https://www.robotistan.com"):
        self.base_url = base_url

    def fetch_products(self, keyword):
        products = []
        page = 1
        max_pages = 5

        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=service, options=options)

        while True:
            url = f"{self.base_url}/search?q={keyword}&page={page}"
            driver.get(url)

            try:
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'product-item'))
                )
                
                WebDriverWait(driver, 20).until(
                    lambda driver: driver.execute_script('return document.readyState') == 'complete'
                )
                
                page_source = driver.page_source
                soup = BeautifulSoup(page_source, 'html.parser')

            except Exception as e:
                print(f"Hata oluştu: {e}")
                driver.quit()
                return []

            product_elements = soup.find_all('div', class_='product-item')

            if not product_elements or page > max_pages:
                break

            for product in product_elements:
                # Başlık Bilgisi
                title_element = product.find('a', class_='product-title')
                title = title_element.get_text(strip=True) if title_element else "N/A"

                # Fiyat Bilgisi
                price = "N/A"
                price_elements = product.find_all(['div', 'span', 'p'])
                for element in price_elements:
                    text = element.get_text(strip=True)
                    if any(char.isdigit() for char in text) and ('TL' in text or '₺' in text):
                        price_text = text
                        price_text = price_text.replace(title, '').strip()
                        price_text = price_text.replace('SEPETE EKLE', '').strip()
                        if 'TL' in price_text:
                            price = price_text.split('TL')[0].strip() + ' TL'
                        elif '₺' in price_text:
                            price = price_text.split('₺')[0].strip() + ' ₺'
                        if price != "N/A":
                            break

                # Stok Durumu
                stock_status = "Out of Stock"
                add_to_cart_btn = product.find('a', class_='add-to-cart-btn')
                if add_to_cart_btn and not add_to_cart_btn.get('disabled'):
                    stock_status = "In Stock"

                products.append({
                    'title': title,
                    'price': price,
                    'stock_status': stock_status
                })

            page += 1

        driver.quit()
        return products

def main():
    base_url = "https://www.robotistan.com"
    fetcher = RobotistanScraper(base_url)

    keyword = input("Aramak istediğiniz ürünü girin: ").strip()

    try:
        products = fetcher.fetch_products(keyword)
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return

    if not products:
        print("\n❌ Hiç ürün bulunamadı.")
    else:
        print("\n📦 Bulunan Ürünler:")
        print("-" * 80)
        for i, product in enumerate(products, 1):
            print(f"{i}. Ürün:")
            print(f"   Başlık: {product['title']}")
            print(f"   Fiyat: {product['price']}")
            print(f"   Stok Durumu: {'✅ Stokta' if product['stock_status'] == 'In Stock' else '❌ Stokta Yok'}")
            print("-" * 80)

if __name__ == "__main__":
    main()
