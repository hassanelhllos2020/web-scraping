## initialize

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
```

## open browser and get url and navigation

```python
browser = webdriver.Chrome()
browser.get("https://elzero.org/")

driver.forward()
driver.back()
```

## selectors

### find_element, find_elements

```python
browser.find_elements(By.CSS_SELECTOR,"#id") 
browser.find_elements(By.CSS_SELECTOR,".class") 
#multiple classes
money = browser.find_elements(By.CSS_SELECTOR,".bn-flex.items-baseline.flex-row") 
print(money[0].text)
-----------------------
find_elements(By.CLASS_NAME,"bn-flex.items-baseline.flex-row") #multiple classes
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.LINK_TEXT, "link text") #using with <a> elemet
continue_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
#xpath
**browser.find_element(By.XPATH, "/html/body/form[1]")**
#https://microsoftedge.microsoft.com/addons/detail/ruto-xpath-finder/kfnnofoddnpcpbeopfeaecieihgnfnla
```

## select

```python
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.NAME, 'name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.deselect_all()

https://selenium-python.readthedocs.io/navigating.html#filling-in-forms
```

## **Interacting with the page**

```python
element.send_keys("some text")
element.send_keys(" and some", Keys.ARROW_DOWN)
element.clear()
element.submit()
element.click()
```

### **Drag and drop**

```python
element = driver.find_element(By.NAME, "source")
target = driver.find_element(By.NAME, "target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(browser)
action_chains.drag_and_drop(element, target).perform()

```

### attripute

```python
element.get_attribute("class") 
element.get_attribute("value") 
element.text
```

## waits

[5. Waits — Selenium Python Bindings 2 documentation (selenium-python.readthedocs.io)](https://selenium-python.readthedocs.io/waits.html)
