_BANKOMAT = ['сбер', 'открытие', 'россельхоз']


class Card:

    def choice_card(self):
        dict_card = {'сбер': 1515, 'открытие': 1278, 'россельхоз': 6751}
        input_card = input('Введите название банка, картой которого хотите воспользоваться (сбер, открытие или россельхоз) : ')

        for key, value in dict_card.items():
            if key == input_card.lower():
                pin = int(input('Введите pin код : '))
                while True:
                    if pin == value:
                        print(f'Пин код карты {key} введен верно')
                        return True
                    else:
                        print('Пин код не верный')




class Bankomat:
    many = 1000
    def choise_bank(self):
        bank = input('Каким банкоматом хотите воспользоваться? (сбер, открытие или россельхоз) : ')
        if bank.lower() in _BANKOMAT:
            pass

    def operation(self):

        while True:
            input_oper = input('Введите тип операции (снять, положить, перевести, выйти)')
            # input_summ_operation = int(input('Введите сумму операции'))

            if input_oper.lower() == 'снять':
                oper = self._out(self.many)
                # return oper
            if input_oper.lower() == 'положить':
                oper = self._in()
                # return oper
            if input_oper.lower() == 'перевести':
                oper = self._trans()

            if input_oper.lower() == 'выйти':

                break
        return oper

    def _out(self, many):
        self.many = many
        input_summ_operation = int(input('Введите сумму операции'))
        # self.input_summ_operation = input_summ_operation
        many -= input_summ_operation
        print(many)
        return many

    def _in(self):
        pass

    def _trans(self):
        pass


def main():


    pin_cod_1 = Card()
    print(pin_cod_1.choice_card())

    bankomat1 = Bankomat()
    # print(bankomat1.operation())
    Bankomat.many = bankomat1.operation()

if __name__ == '__main__':
    main()

