# Objetivo e passar as configs para criar um pool (regiao) de DIMMs para o optane pmem
# este e so o calculo teorico e precisa dos valores para efetuar o calculo
#
#Por exemplo:
#Para DDR4 2933, a memória compatível com algumas séries Core-x é (1466,67 X 2) X 8 (n º de bytes de largura) X 4 (n º de canais) = largura de banda de 93866,88 MB/s ou 94 GB/s.

"""

Objetivo e efetuar um calculo teoria para configurar um pool (regiao) de DIMMs para configurar o optane pmen

A ideia basicamente esta em aplicacoes que requerem maior desempenho de largura de banda

Por exemplo:
Para DDR4 2933, a memória compatível com algumas séries Core-x é (1466,67 X 2) X 8 (n º de bytes de largura) X 4 (n º de canais) = largura de banda de 93866,88 MB/s ou 94 GB/s.

dmidecode -t memory


Memory Device
	Array Handle: 0x0007
	Error Information Handle: Not Provided
	Total Width: 64 bits
	Data Width: 64 bits
	Size: 8192 MB
	Form Factor: SODIMM
	Set: None
	Locator: ChannelB-DIMM0
	Bank Locator: BANK 2
	Type: DDR3
	Type Detail: Synchronous
	Speed: 1600 MT/s
	Manufacturer: 859B
	Serial Number: 00000000
	Asset Tag: None
	Part Number: CT8G3S160BM.M16FED
	Rank: Unknown
	Configured Memory Speed: 1600 MT/s

        ouvido:
            ceruminolitico
            otodem plus

        pulgas: 
            simparic 10 a 20 kg
"""

try:
    subprocess.run(
            ['dmidecode', '-t', 'memory'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    print(f"Erro para gerar o dmidecode")
    exit(1)

for line in result.stdout.splitlines():
    if "Speed:" in str(line):
        freq = line

    if "Total Width:" in str(line):
        width = line
    if "
