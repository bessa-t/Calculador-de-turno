
def main():
    print("Digite os horários no formato HH:MM!")
    print("Digite uma carga horária de 4 a 12 horas diárias.")

    def adquirir_h(frase):
        horario = input(frase)
        try:
            horas,minutos = map(int,horario.split(":"))
            if 0 <= horas < 24 and 0 <= minutos < 60:
                return horario
            else:
                print("Digite um horário válido!")
        except:
            print("Digite um horário no formato HH:MM!")
        return adquirir_h(frase)

    def adquirir_t(frase):
        try:
            turno = int(input(frase))
            if 4 <= turno <= 12:
                return turno
            else:
                print("Digite uma carga válida!")
        except ValueError:
            print("Digite a sua carga horária diária em horas!")
        return adquirir_t(frase)

    def format_min(horario):
        return  int(horario[:2])*60 + int(horario[3:])

    def obter_entradas():
        entrada = adquirir_h(f"Digite o horário de entrada: ")
        saida_alm = adquirir_h(f"Digite o horário de saída para o almoço: ")
        volta_alm = adquirir_h(f"Digite o horário de volta do almoço: ")
        turno = adquirir_t((f"Digite qual é a sua carga horária (em horas): "))

        if format_min(entrada) < format_min(saida_alm) <= format_min(volta_alm):
            return entrada, saida_alm , volta_alm, turno
        else:
            print("digite horarios válidos!")
        obter_entradas()

    entrada , saida_alm , volta_alm , turno = obter_entradas()
    saida = turno *60 + format_min(entrada) + format_min(volta_alm) - format_min(saida_alm)

    def format_horario(tempo):  
        if tempo < 10:
            return "0" + str(tempo)
        else:
            return str(tempo)
        
    print(f"Seu horário de saída é às {format_horario(saida//60)}:{format_horario(saida%60)}.")

main()