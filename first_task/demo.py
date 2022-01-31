from letter_number_gen import id_value_generator

if __name__ == "__main__":
    with open('./data/f1.txt', 'r') as f:
        with open('./data/f2.txt', 'r') as f_:
            data = f.readlines()
            data_ = f_.readlines()
            for i in id_value_generator(data, data_):
                print(i)
