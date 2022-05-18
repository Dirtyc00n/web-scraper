* Simple web escraper que almacenara caracteristicas y precio de los teclados con un 30 % de descuento como si fuera un usuario 

** Las variables By.CSS_SELECTOR Y 'input.nav-search-input' seran usadas para hacer click en un objeto en este caso el buscador de mercado libre, 'input.nav-search-input' y .send_keys('') se usara para mandar lo que buscaremos que seria 'teclado' luego para clickear en busqueda (EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.nav-icon-search'))).click() y filanlmente copiamos el full href de 30 % de descuento (EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/aside/section/div[12]/ul/li[6]/a')))

** Estas tres variables se pueden modificar para navegar por la pagina web
** WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.nav-search-input'))).send_keys('teclado')
** WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.nav-icon-search'))).click()
**WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/aside/section/div[12]/ul/li[6]/a')))

** La siguiente variable almacena el link y lo lanza a la siguiente url

** url = driver.find_element_by_xpath('/html/body/main/div/div/aside/section/div[12]/ul/li[6]/a').get_attribute("href")

** Y lo proximo es seleccionar la seccion donde se muestran los teclados((By.XPATH, '/html/body/main/div/div/section/ol'))) y dentro de esto almacenamos los elementos selecionados por etiqueta css
