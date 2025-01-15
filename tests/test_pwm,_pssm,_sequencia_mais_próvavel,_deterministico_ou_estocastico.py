# -*- coding: utf-8 -*-
"""test_PWM, PSSM, Sequencia mais próvavel, deterministico ou estocastico

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K-cpxdHn0wdaNhwgDzIQbsE8w2y1uaJb
"""

import unittest
from math import log2, prod, isclose
from re import findall
from math import isclose

class TestPWMPSSMSequencia(unittest.TestCase):
    def setUp(self):
        self.seqs = ["ACGT", "ACGA", "ACGG", "ACGC"]
        self.seq = "ACGTACGGACGC"
        self.pseudocontagem = 1
        self.bg_freq = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
        self.casas_decimais = 2

    def test_sequencias_tamanho_diferente(self):
        with self.assertRaises(ValueError):
            pwm_pssm_e_sequencia_mais_provavel(["ACGT", "ACGA", "ACG"], "ACGTACGGACGC")

    def test_sequencia_menor_que_motivo(self):
        with self.assertRaises(ValueError):
            pwm_pssm_e_sequencia_mais_provavel(["ACGT", "ACGA", "ACGG", "ACGC"], "ACG")

    def test_tipo_invalido(self):
        with self.assertRaises(ValueError):
            pwm_pssm_e_sequencia_mais_provavel(["ACGT", "ACGA", "ACGG", "ACGC"], "ACGTACGGACGC", tipo="RNA")

    def test_pwm_calculation(self):
        pwm, _, _, _ = pwm_pssm_e_sequencia_mais_provavel(
            self.seqs, self.seq, pseudocontagem=self.pseudocontagem,
            casas_decimais=self.casas_decimais, bg_freq=self.bg_freq
        )

        N = len(self.seqs)
        A = 4
        pc = self.pseudocontagem

        self.assertTrue(isclose(pwm[0]['A'], (4 + pc)/(N + A*pc), rel_tol=1e-2))
        self.assertTrue(isclose(pwm[0]['C'], (0 + pc)/(N + A*pc), rel_tol=1e-2))
        self.assertTrue(isclose(pwm[0]['G'], (0 + pc)/(N + A*pc), rel_tol=1e-2))
        self.assertTrue(isclose(pwm[0]['T'], (0 + pc)/(N + A*pc), rel_tol=1e-2))

        for pos in range(len(pwm)):
            prob_sum = sum(pwm[pos].values())
            self.assertTrue(isclose(prob_sum, 1.0, rel_tol=1e-2))

    def test_pssm_calculation(self):
        _, pssm, _, _ = pwm_pssm_e_sequencia_mais_provavel(
            self.seqs, self.seq, pseudocontagem=self.pseudocontagem,
            casas_decimais=self.casas_decimais, bg_freq=self.bg_freq
        )

        for pos in range(len(pssm)):
            for base in 'ACGT':
                self.assertTrue(isinstance(pssm[pos][base], float))
                if pssm[pos][base] != float('-inf'):
                    self.assertTrue(-10 <= pssm[pos][base] <= 10)

    def test_sequencia_mais_provavel(self):
        _, _, _, (seqs_provaveis, prob) = pwm_pssm_e_sequencia_mais_provavel(
            self.seqs, self.seq, pseudocontagem=self.pseudocontagem,
            casas_decimais=self.casas_decimais, bg_freq=self.bg_freq
        )

        self.assertTrue(len(seqs_provaveis) > 0)
        self.assertTrue(0 <= prob <= 1)
        for seq in seqs_provaveis:
            self.assertEqual(len(seq), len(self.seqs[0]))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPWMPSSMSequencia)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")

class TestPWM_PSSM(unittest.TestCase):

    def test_pwm_pssm_calculation_valid_input(self):
        seqs = ["ATGCATGC", "ATGCATGC", "ATGCATGC"]
        seq = "ATGCATGC"
        pwm, pssm, prob_seq, seqs_mais_probaveis = pwm_pssm_e_sequencia_mais_provavel(seqs, seq)

        self.assertIsInstance(pwm, list)
        self.assertIsInstance(pwm[0], dict)

        self.assertIsInstance(pssm, list)
        self.assertIsInstance(pssm[0], dict)

    def test_invalid_sequences_length(self):
        seqs = ["ATGCATGC", "ATGCATGC"]
        seq = "ATGC"
        with self.assertRaises(ValueError):
            pwm_pssm_e_sequencia_mais_provavel(seqs, seq)

    def test_invalid_characters_in_sequences(self):
        seqs = ["ATGCATGC", "ATGXATGC"]
        seq = "ATGCATGC"
        with self.assertRaises(ValueError):
            pwm_pssm_e_sequencia_mais_provavel(seqs, seq)

    def test_invalid_alphabet_type(self):
        seqs = ["ATGCATGC", "ATGCATGC"]
        seq = "ATGCATGC"
        with self.assertRaises(ValueError):
            pwm_pssm_e_sequencia_mais_provavel(seqs, seq, tipo="RNA")

    def test_background_frequency_check(self):
        seqs = ["ATGCATGC", "ATGCATGC"]
        seq = "ATGCATGC"
        bg_freq = {'A': 0.25, 'C': 0.25, 'G': 0.25}
        with self.assertRaises(ValueError):
            pwm_pssm_e_sequencia_mais_provavel(seqs, seq, bg_freq=bg_freq)

    def test_empty_sequences(self):
        seqs = []
        seq = "ATGCATGC"
        with self.assertRaises(ValueError):
            pwm_pssm_e_sequencia_mais_provavel(seqs, seq)

    def test_probabilidade_com_zeros(self):
        seqs = ["ATGCATGC", "ATGCATGC", "ATGCATGC"]
        seq = "AAAAAAA"
        pwm, pssm, prob_seq, seqs_mais_probaveis = pwm_pssm_e_sequencia_mais_provavel(seqs, seq)
        self.assertEqual(prob_seq, 0.0)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPWMPSSMSequencia)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")