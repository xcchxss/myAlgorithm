while True:
    try:
        s = input()
        # input()：读入一行，并将其转换为字符串

        if s == "":
            break
        # 当输入为空行时，终止程序

    except EOFError:
        break
    # EoFError：End of File Error
    # 表示输入结束

    ans = s.split()
    # 将字符串 s 分割为字符串列表 ans[]
    
    index = -1
    flag = " "
    
    for i in range(len(ans[0])):
        if ans[0][i] > flag:
            flag = ans[0][i]
            index = i
    
    for i in range(len(ans[0])):
        print(ans[0][i], end = "")
        if i == index:
            print(ans[1], end = "")
    print()