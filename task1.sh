

## downloaded assembly here: https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.26/#
## brew install samtools
## brew install bowtie2

# convert .bam to .sam to see file content
samtools view -h -o miniMNM00065.sam miniMNM00065.bam

# check if there are reads mapping to chromosome 1
samtools view -F 4 miniMNM00065.sam | cut -f1,3  | awk -F '\t' '{ if ($2 == 1) print $1 }'  > reads_mapped_to_chr_1

# get selected read and dump it into folder
samtools view -F 4 miniMNM00065.sam | cut -f1,3,10  | awk -F '\t' '{ if ($2 == 1) print $1,$3 }'   |  sed 's/^/>/' | sed 's/\t/\n/'  > reads_mapped_to_chr_1.fasta

# download chromossome 38 and unzip it
gunzip GCF_000001405.26_GRCh38_genomic.fna.gz

# bowtie indexing # (starting at 17:18 and running for over an hour)
bowtie2-build --threads 4 GCF_000001405.26_GRCh38_genomic.fna GCF_000001405.26_GRCh38_genomic 

# mapping reads (process was not run)
bowtie -f reads_mapped_to_chr_1.fasta -X GCF_000001405.26_GRCh38_genomic.fna -s mapped_reads.sam

# conversion from .sam to .bam (process was not run)
samtools view -Sb  mapped_reads.sam  >  mapped_reads.bam

