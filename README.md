TR:
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

EN:
The code aims to automatically create a new account on the website https://playvalorant.com/tr-tr/. During this process, it generates a random email, username (nickname), and password, and then saves these details to a file.

Functions

generate_random_email()
Generates a random email address. The email address consists of 10 random lowercase letters followed by @gmail.com.

generate_random_nickname()
Generates a random username (nickname). The username consists of 12 random lowercase letters.

generate_random_password()
Generates a random password. The password is a 10-character string composed of letters and digits.

save_email_and_nickname_to_file(email, nickname, password, filename="accounts.txt")
Saves the generated email, username, and password to the specified file.

click_element()
Uses Selenium WebDriver to navigate to the website and perform the account creation steps automatically.

The steps are as follows:

Click the login button.
Click the "Join Your Team" button.
Enter the randomly generated email address in the email field.
Fill in the birth date, month, and year fields with random values.
Enter the randomly generated username in the username field.
Enter the randomly generated password in the password fields.
Finally, check the "Terms of Service" checkbox and proceed.

Selenium Operations

WebDriverWait: Waits for elements to load and performs click operations.
ActionChains: Automates clicks and other interactions.
JavaScript: Used to remove the 'disabled' attribute from the checkbox.

Error Handling

If any error occurs, it prints the error message and closes the browser.
Usage

The script runs by calling the click_element() function within the if __name__ == "__main__": block and performs the specified steps automatically.

This code provides an example automation scenario for those who need to automate account creation processes. For the script to work successfully, the necessary Selenium and WebDriver dependencies must be installed.
