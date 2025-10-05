with open("m1.txt", "r") as file:
    content = file.read()
    print(content)

    m1 = content.split(',')
    print(len(m1))

with open("m2.txt", "r") as file:
    content = file.read()
    print(content)

    m2 = content.split(',')
    print(len(m2))

m_double = []

for i in range(len(m1)):
    for j in range(len(m2)):
        if (m1[i] == m2[j]):
            m_double.append(m1[i])

m_double = set(m_double)

print(m_double)
