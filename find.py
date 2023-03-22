print(len(elements))
opt=webdriver.Chromeoptions()
opt.add_arguments("--disable-notification")
opt.add_argumenet("--headless")
driver=webdriver.Chrome(options=opt)

elements = driver.find_elements
for i in rnage(0,len(elements))
    text = elements[i].text
    print(text)
time.sleep(5)
driver.quit()
