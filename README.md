Robotistan Web Kazıma Projesi

Bu proje, Robotistan e-ticaret sitesinden ürünlerin adı, fiyatı ve stok durumu bilgilerini çekmek için yazılmış bir Python web kazıma uygulamasıdır. 
`robotistan_scraper.py` dosyası web kazıma işlemini gerçekleştirmekte, `main.py` dosyası ise bu işlemi çalıştırarak kullanıcıya ürün bilgilerini sunmaktadır.

Özellikler

- Robotistan sitesindeki ürünlerin isimlerini, fiyatlarını ve stok durumlarını çeker.
- Python ve web kazıma kütüphaneleri (`requests`, `BeautifulSoup`) kullanılarak geliştirilmiştir.
- Çekilen veriler, kullanıcıya anlaşılır bir formatta sunulur.

Gereksinimler

Projenin çalışabilmesi için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:
- `requests`
- `BeautifulSoup4`

Bu kütüphaneleri yüklemek için şu komutu kullanabilirsiniz:
```bash
pip install requests beautifulsoup4
```

Kullanım

1. GitHub deposunu bilgisayarınıza klonlayın:
   ```bash
   git clone https://github.com/kullaniciAdi/robotistan_scraper.git
   ```
2. İlgili dizine gidin:
   ```bash
   cd robotistan_scraper
   ```
3. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
4. `main.py` dosyasını çalıştırarak Robotistan'dan ürün bilgilerini çekin:
   ```bash
   python main.py
   ```
   Bu komut, Robotistan sitesinden ürünlerin adlarını, fiyatlarını ve stok durumlarını ekranda gösterecektir.

Dosya Yapısı

- `robotistan_scraper.py`: Web kazıma işlemini gerçekleştiren dosya.
- `main.py`: Projeyi çalıştıran ve veriyi kullanıcıya sunan dosya.

Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, aşağıdaki adımları takip edebilirsiniz:
1. Repo'yu forklayın.
2. Yeni bir dal (branch) oluşturun.
3. Değişikliklerinizi yapın ve yeni bir pull request gönderin.

Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.
