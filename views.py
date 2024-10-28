import sys
import csv
def add(i):
    with open('data.csv', '+a',newline='')as file:
        writer=csv.writer(file)
        writer.writerows(i)

    # add(['anonymous', 'M', '54321', 'data@gamil.com'])
    # add(['demo', 'M', '123', 'demo@gmail.com'])    

def view():
    data = []
    with open('data.csv')as file:
        reader= csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return(data)

view()

def remove(i):
    def save(i):
        with open('data.csv', 'W',newline='')as file:
            writer=csv.writer(file)
            writer.writerows(i)





    new_list =[]
    telephone = i

    with open('data.csv','')as file:
        reader=csv.reader(file)
        for row in reader:
            new_list.append(row)


            for elements in row:
                if elements == telephone:
                    new_list.remove(row)

#view()

def update(i):
    def update_new_list(j):
        with open('data.csv', 'w', newline='')as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone =i[0]
    # ['54321','anonymous','M','54321','data@gamil.com']

    with open('data.csv', 'r')as file:
        reader=csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element== telephone:
                  name = i [1]
                  gender = i[2]
                  telephone = i[3]
                  gmail = i[4]

                  data = [name, gender, telephone, gmail]
                  index = new_list.index(row)
                  new_list[index] = data

    update_new_list(new_list)            
          

# sample = ['54321','boycode', 'F', '54321', 'boy54321@gmail.com']
# update(sample)

def search(i):
    data = []
    telephone = i
    with open('data.csv', 'r')as file:
        reader= csv.reader(file)
        for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)
    print(data)                
    return data
search('123')
