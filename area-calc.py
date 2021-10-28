def conv2float(input_number):
    return float(input_number)

area = 0
with open('data.txt') as file:
    data = file.readlines()
    for line in data:
        lf, li, bf, bi = map(conv2float, line.strip().split())
        length = lf * 12 + li
        breadth = bf * 12 + bi

        area_in = length * breadth
        area += area_in / 144
        
        print('Area Progress : {:.2f}'.format(area))

print('Calculated area: {:.2f}'.format(area))




# for i in range(n):
    # print('Compartment {}'.format(i+1))
    # print('Length:')
    # l1 = float(input('feet: '))
    # l2 = float(input('inches: '))
    # l = l1 * 12 + l2

    # print('Breadth:')
    # b1 = float(input('feet: '))
    # b2 = float(input('inches: '))
    # b = b1 * 12 + b2

    # area_in += l * b

area_f = area_in / 144

print('Area of the house is {} sq. feet'.format(area_f))
    
