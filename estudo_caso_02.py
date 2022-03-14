"""
Bioinformática: comparando genomas

Realizar a comparação entre duas sequências de DNA: (1) ser humano, (2) bactéria
DNA: A, T, C ou G.
Avaliar a quantidade de pares de nucleotídeos, para verificar as diferenças entre organismos
diferentes.

"""

entrada = open('bd/human.fasta').read()
saida = open('html/human.html', 'w')

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i + j] = 0

entrada = entrada.replace('\n', '')

for k in range(len(entrada) - 1):
    cont[entrada[k] + entrada[k + 1]] += 1

i = 1
for k in cont:
    transparencia = cont[k] / max(cont.values())
    saida.write(
        "<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float: left; background-color: rgba(0, 0, 0, " + str(
            transparencia) + "')>" + k + "</div>")
    if i % 4 == 0:
        saida.write("<div style='clear:both'></div>")
    i += 1

saida.close()
