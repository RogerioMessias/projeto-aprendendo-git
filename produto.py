precoProduto = float(input('Digite o valor do Produto: '))
percentualDesconto = float(input('Qual o percentual de desconto? '))

valorDesconto = (precoProduto * percentualDesconto)/100
totalApagar = precoProduto - valorDesconto

print('Um desconto de %5.2f %% em uma mercadoria de  R$ %7.2f' % (valorDesconto, precoProduto))
print('vale R$ %7.2f' % valorDesconto)
print('O valor a pagar é de %7.2f' % totalApagar)
