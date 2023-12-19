# esp32_micropython_4x4keypad
```python

```
![Матричная клавиатура 4х4](/files/image1.png)
## Инициализация
```python
kp = ClassKeypad(PCF8574(SoftI2C(sda=Pin(4), scl=Pin(5))))
```
### Получение нажатой клавиши
```python
key = kp.process()
```
