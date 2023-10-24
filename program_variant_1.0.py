
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Укажите путь к драйверу Chrome

driver = webdriver.Chrome()

# Откройте веб-сайт
url = 'http://publicbg.mjs.bg/Bginfo'  # Замените на адрес искомого сайта
driver.get(url)

# Найдите элементы для ввода логина и пароля
wait = WebDriverWait(driver, 10)
login_field = wait.until(EC.presence_of_element_located((By.ID, 'reqNun')))
  # Замените 'login_id' на реальный идентификатор поля
password_field = wait.until(EC.presence_of_element_located((By.ID,'pin')))

# Введите логин и пароль
login = '19988/2023'
password = '962227'
login_field.send_keys(login)
password_field.send_keys(password)

# Найдите и нажмите кнопку входа
login_button = driver.find_element(By.XPATH,"//button[@class='btn btn-success']")
login_button.click()

# Дождитесь загрузки страницы
wait = WebDriverWait(driver, 2)
status_field = driver.find_element(By.XPATH, "//*[@class='container body-content']"
                                              "/div[@class='container'][1]/div"
                                              "[@class='validation-summary-errors text-danger']/ul/li")

# Получите текст статуса
status_text = status_field.text


print("Статус:", status_text)

# Закройте браузер после завершения операций
driver.quit()