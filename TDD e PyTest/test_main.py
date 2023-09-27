#Testa cada caso da função exemplo criada

from main_code import fun_teste

def test_reposta_padrão():
    n = 1
    assert fun_teste(n) == "0"

def test_multiplos_de_tres_v1():
    n = 3 #entrada
    esperado = "Auto" #valor esperado
    resultado = fun_teste(n) #valor recebido
    assert resultado == esperado 

def test_multiplos_de_tres_v2():
    n = 3
    assert fun_teste(n) == 'Auto'

def test_multiplos_de_cinco():
    n = 5
    assert fun_teste(n) == "Trac"

def test_multiplos_de_quinze():
    n = 15
    assert fun_teste(n) == "Autotrac"

def test_entrada_igual_zero():
    n = 0
    assert fun_teste(n) == 0