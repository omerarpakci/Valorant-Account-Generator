Kod, https://playvalorant.com/tr-tr/ adresindeki web sitesinde otomatik olarak yeni bir hesap oluşturmayı amaçlar. Bu işlem sırasında rastgele bir e-posta, kullanıcı adı (nickname) ve şifre oluşturur, ardından bu bilgileri bir dosyaya kaydeder.

Fonksiyonlar
generate_random_email()
Rastgele bir e-posta adresi oluşturur. E-posta adresi, 10 karakter uzunluğunda rastgele harflerden ve @gmail.com domaininden oluşur.
generate_random_nickname()
Rastgele bir kullanıcı adı (nickname) oluşturur. Kullanıcı adı, 12 karakter uzunluğunda rastgele küçük harflerden oluşur.
generate_random_password()
Rastgele bir şifre oluşturur. Şifre, harfler ve rakamlardan oluşan 10 karakter uzunluğunda bir dizidir.
save_email_and_nickname_to_file(email, nickname, password, filename="accounts.txt")
Oluşturulan e-posta, kullanıcı adı ve şifreyi belirtilen dosyaya kaydeder.
click_element()
Selenium WebDriver kullanarak web sitesine otomatik olarak gider ve hesap oluşturma adımlarını gerçekleştirir.
Adımlar şunlardır:
Giriş butonuna tıklama.
"Takımına Katıl" butonuna tıklama.
E-posta alanına rastgele oluşturulan e-posta adresini girme.
Doğum günü, ayı ve yılını rastgele değerlerle doldurma.
Kullanıcı adı alanına rastgele oluşturulan kullanıcı adını girme.
Şifre alanlarına rastgele oluşturulan şifreyi girme.
Son olarak, "Kullanım Şartları" checkbox'ını işaretleyip devam etme.
Selenium İşlemleri
WebDriverWait: Elementlerin yüklenmesini bekler ve tıklama işlemlerini gerçekleştirir.
ActionChains: Tıklama ve diğer etkileşimleri otomatikleştirir.
JavaScript: Checkbox'ın 'disabled' niteliğini kaldırmak için kullanılır.
Hata Yönetimi
Herhangi bir hata oluştuğunda, hata mesajını yazdırır ve tarayıcıyı kapatır.
Kullanım
Kod, if __name__ == "__main__": bloğu içerisinde click_element() fonksiyonunu çağırarak çalışır ve belirtilen adımları otomatik olarak gerçekleştirir.

Bu kod, otomatik hesap oluşturma süreçlerini gerçekleştirmek isteyenler için örnek bir otomasyon senaryosu sunar. Kodun başarılı bir şekilde çalışabilmesi için gerekli Selenium ve WebDriver bağımlılıklarının kurulmuş olması gerekmektedir.
