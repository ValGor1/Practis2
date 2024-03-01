gektar = int(input('Сколько гектаров участка?'))
M = gektar * 10000
sm = float(input('Сколько сантиметров осадков?'))
mm = 100 * sm
osadki = M * mm
print(int(osadki))