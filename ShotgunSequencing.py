import random
import unittest

class ShotgunSequencing:
    def __init__(self, genome_length, min_read_length, max_read_length, coverage) -> None:        
        self.genome_length = genome_length
        self.min_read_length = min_read_length
        self.max_read_length = max_read_length
        self.coverage = coverage

    def generate_genome(self, genome_length):
        
        generated_genome = ''
        bases = ['A', 'C', 'C', 'T']
        
        for i in range(genome_length):
            generated_genome += random.choice(bases)
            
        return generated_genome
    
    def generate_reads(self, genome, min_read_length, max_read_length):
        
        dna_reads = []
        genome_size = len(genome)
        position = 0

        while position < genome_size:
            fragment_size = random.randint(min_read_length, max_read_length)

            if position + fragment_size > genome_size:
                fragment_size = genome_size - position

            dna_reads.append(genome[position:position+fragment_size])
            position += fragment_size

        return dna_reads
    
    def shuffle_reads(self, dna_reads):
        random.shuffle(dna_reads)
        return dna_reads
    
    def shotgun(self):

        shotgun_reads = []
        genome = self.generate_genome(self.genome_length)
        
        print(genome, "\n")
        
        for i in range(self.coverage):
            dna_reads = self.generate_reads(genome, self.min_read_length, self.max_read_length)
            print("{} Shotgun reads: {}".format(i, dna_reads))
            
            if genome == "".join(dna_reads):
                print("".join(dna_reads), "\n")
            
            shotgun_reads.append(dna_reads)
            
        return shotgun_reads
        
if __name__ == '__main__':
    generator = ShotgunSequencing(100, 2, 10, 10)
    print(generator.shotgun())