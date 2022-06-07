produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
#seu código aqui

for i, produto in enumerate(produtos):
  if vendas2020[1] > vendas2019[i]:
    crescimento = vendas2019[i] / vendas2020[1]
    #print(produto, vendas2019[i], vendas2020[i], crescimento)
    print('O produto {} vendeu {:,} em 2020 e {:,} em 2019 e teve crecimento de {:.1%}'. format(
        produto,vendas2020[i], vendas2019[i], crescimento
    ))