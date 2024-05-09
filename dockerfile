# Menggunakan base image yang sudah termasuk Selenium dan Chrome WebDriver
FROM selenium/standalone-chrome:latest

WORKDIR /home/aditya/saucedemo-test-cases

# Copy kode Python Anda ke dalam kontainer
COPY . /home/aditya/saucedemo-test-cases


