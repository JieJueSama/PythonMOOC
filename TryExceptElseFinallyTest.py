try:
    print('try...')
    r = 10 / 0
    r = 10 / 'xyz'
    print('result:', r)
    print('Test................')
except TypeError as e:
    print('TypeError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')