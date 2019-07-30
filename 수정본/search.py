def search(keyword):
    
    s_line = []
    List_A = []
    f = open("data.txt", 'r')

    while True:
        line = f.readline()
        s_line.append(line)
        if '#' in line:
            List_A.append(s_line)
            s_line = []
        if not line: break
    f.close()
    #print(List_A)

    result = []
    #전체 저장된 데이터의 개수만큼 for문
    for i in List_A:
        lenth = len(i)

        #각각의 데이터 안에서 태그의 개수만큼 for문
        for j in range(1,lenth):
            if keyword in i[j]:
                result.append(i)


    return result

#쓰는 방법
#함수안에 키워드를 전달해 주면 됨
#keyword = "천재"
#search(keyword)