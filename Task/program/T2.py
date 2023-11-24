n = int(input('Enter the number of details you given:'))

print('Enter name, age, score with comma sepration')

s1 = []

for i in range(n):
    s1.append(input().split(','))


if(len(s1[0]) == 3 and len(s1[1]) == 3 and len(s1[2]) == 3):
    choice = int(input('press 1 for this order (name> age> score)\npress 2 for this order (age> score> name)\npress 3 for this order (score> name > age)\nenter number: '))

    
    if(choice == 1):

        for i in range(0, len(s1)):
            for j in range(i+1, len(s1)):
                if(s1[i][2] > s1[j][2]):
                    temp = s1[i]
                    s1[i] = s1[j]
                    s1[j] = temp

        for i in range(0, len(s1)):
            for j in range(i+1, len(s1)):
                if(s1[i][1] > s1[j][1]):
                    temp = s1[i]
                    s1[i] = s1[j]
                    s1[j] = temp

        for i in range(0, len(s1)):
            for j in range(i+1, len(s1)):
                if(s1[i][0] > s1[j][0]):
                    temp = s1[i]
                    s1[i] = s1[j]
                    s1[j] = temp


    elif(choice == 2):
        for i in range(0, len(s1)):
            for j in range(i+1, len(s1)):
                if(s1[i][0] > s1[j][0]):
                    temp = s1[i]
                    s1[i] = s1[j]
                    s1[j] = temp

        for i in range(0, len(s1)):
            for j in range(i+1, len(s1)):
                if(s1[i][2] > s1[j][2]):
                    temp = s1[i]
                    s1[i] = s1[j]
                    s1[j] = temp

        for i in range(0, len(s1)):
            for j in range(i+1, len(s1)):
                if(s1[i][1] > s1[j][1]):
                    temp = s1[i]
                    s1[i] = s1[j]
                    s1[j] = temp

                
    elif(choice == 3):
        for i in range(0, len(s1)):
            for j in range(i+1, len(s1)):
                if(s1[i][1] > s1[j][1]):
                    temp = s1[i]
                    s1[i] = s1[j]
                    s1[j] = temp

        for i in range(0, len(s1)):
            for j in range(i+1, len(s1)):
                if(s1[i][0] > s1[j][0]):
                    temp = s1[i]
                    s1[i] = s1[j]
                    s1[j] = temp

        for i in range(0, len(s1)):
            for j in range(i+1, len(s1)):
                if(s1[i][2] > s1[j][2]):
                    temp = s1[i]
                    s1[i] = s1[j]
                    s1[j] = temp

                    
    else:
        print('Please enter valid input')
    print([tuple(i) for i in s1])


else:
    print('Please enter details like name,age ,score')
