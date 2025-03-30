from robotistan_scraper import RobotistanScraper

def display_products(products):
    if not products:
        print("\n❌ Hiç ürün bulunamadı.")
        return

    print("\n📦 Bulunan Ürünler:")
    print("-" * 80)
    for i, product in enumerate(products, 1):
        print(f"{i}. Ürün:")
        print(f"   Başlık: {product['title']}")
        print(f"   Fiyat: {product['price']}")
        print(f"   Stok Durumu: {'✅ Stokta' if product['stock_status'] == 'In Stock' else '❌ Stokta Yok'}")
        print("-" * 80)

def main():
    scraper = RobotistanScraper()
    keyword = input("Aramak istediğiniz ürünü girin: ").strip()

    try:
        products = scraper.fetch_products(keyword)
        display_products(products)
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()
