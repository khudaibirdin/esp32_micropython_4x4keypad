# micropython_esp32_4x4keypad
## Внешний матричной клавиатуры:

![Матричная клавиатура 4х4](/files/image2.png)

## Подключение
### Подключение клавиатуры 4x4 к расширителю PCF8574
|Клавиатура|PCF8574|
|---|---|
|1|P0|
|2|P1|
|3|P2|
|4|P3|
|5|P4|
|6|P5|
|7|P6|
|8|P7|
### Подключение расширителя к PCF8574 к ESP32-S2 mini
|PCF8574|ESP32-S2 mini|
|---|---|
|VCC|3.3V|
|GND|GND|
|SDA|3|
|SCL|5|

При желании, можно назначить другие SDA и SCL пины на ESP32-S2 mini.
## Работа с ПО
### Инициализация
```python
kp = ClassKeypad(PCF8574(SoftI2C(sda=Pin(3), scl=Pin(5))))
```
### Получение нажатой клавиши
```python
key = kp.process()
```
### Проверка, нажата ли сейчас кнопка
```python
kp.is_pressed
```
### Предыдущая кнопка
```python
kp.previous
```
