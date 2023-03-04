from ShotgunSequencing import *

class TestShotgunSequencing(unittest.TestCase):
    def setUp(self) -> None:
        self.synthetic_data_generator = ShotgunSequencing(100, 2, 15, 10)    
        return super().setUp()

    def test_generate_genome(self):
        genome = self.synthetic_data_generator.generate_genome(100)
        self.assertEqual(len(genome), 100)
        self.assertTrue(set(genome).issubset({'A', 'C', 'G', 'T'}))
    
    def test_generate_reads(self):
        genome = self.synthetic_data_generator.generate_genome(100)
        dna_read = self.synthetic_data_generator.generate_reads(genome, 2, 15)
        reconstructed_genome = ''.join(dna_read)
        self.assertEqual(len(genome), len(reconstructed_genome))
        self.assertEqual(genome, reconstructed_genome)
    
if __name__ == '__main__':
    unittest.main()
