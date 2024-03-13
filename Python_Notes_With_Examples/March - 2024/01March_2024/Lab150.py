try:
    c = 10/0
except Exception as e:
    print("Zero division error")
finally:
    print("The code should be displayed")