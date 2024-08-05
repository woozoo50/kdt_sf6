#과제 1
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
"""
while True:
    print("====================RESTART")
    sel = input("마시고 싶은 음료?")

    for i in vending_machine:
       if sel == str(vending_machine[i]):
          print(f'{sel} 드릴게요')
          vending_machine.remove(sel)
       else:
          print(f'{sel}는 지금 없네요')
"""
while True:
    print("====================RESTART")
    sel = input("마시고 싶은 음료?")
    
    if sel in vending_machine:
        vending_machine.remove(sel)
        print(sel, "드릴게요")
        print("남은 음료는", vending_machine)
    else:
        print(f'{sel}는 지금 없네요')