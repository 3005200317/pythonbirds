from unittest import \
    def TestCase(self):

from oo.carro import Motor

class CarroTestCase(testCase) :
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

