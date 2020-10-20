dist = float(input('Ditância em metros: '))
print('A mediade de {:.1f}m corresponde a'.format(dist))

km = dist / 1000
hm = dist / 100
dam = dist / 10
dm = dist * 10
cm = dist * 100
mm = dist * 1000

print('\n{:.3f}Km\n{:.2f}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(km, hm, dam, dm, cm, mm))
