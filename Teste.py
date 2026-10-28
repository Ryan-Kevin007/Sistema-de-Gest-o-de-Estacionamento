opcao = 5
total_veiculos = 0
carros = 0
motos = 0
vans = 0
clientes_conveniados = 0
atendimentos_fim_de_semana = 0
tickets_perdidos = 0
pagamento_dinheiro = 0
pagamento_cartao = 0
pagamento_pix = 0
valor_total = 0
total_atendimentos = 0
valor_da_maior_venda = 45
valor_da_menor_venda = 45
desconto_total = 0
taxa_total = 0
atendimentos_20 = 0
atendimentos_50 = 0
atendimentos_maior_50 = 0
#====================INÍCIO DO MENU===========================
while opcao!=0:
  print("\n========= ESTACIONAMENTO =========\n\n")
  print("1 - Registrar saída de veículo")
  print("2 - Consultar relatório")
  print("3 - Simular valor de estacionamento")
  print("0 - Encerrar sistema")
  print("\nEscolha uma opção:")
  opcao = int(input(""))
  if opcao==1:
    total_atendimentos+=1
    valor = 0
    tarida_estacionamento = 0
    estacionamento_taxa = 0
    desconto = 0.20
    valor_desconto = 0
    desconto_pix = 0.05
    fim_de_semana = 5
    cartao = 1.03
    taxa_ticket = 0
    ajuste_pagamento = 0
  #====================MENU DOS VEÍCULOS===========================
    print("====TIPO DE VEÍCULO====")
    print("\n1-CARRO")
    print("2-MOTO")
    print("3-VAN\n")

  #====================DADOS DO CLIENTE===========================

    tipo_veiculo = str(input("Tipo de veículo:"))
    while tipo_veiculo !="CARRO" and tipo_veiculo !="VAN" and tipo_veiculo!="MOTO":
     tipo_veiculo = str(input("Tipo de veículo:"))
    qtd_horas_estacionados = int(input("Quantidades de horas estacionadas:"))
    while qtd_horas_estacionados <=0 or qtd_horas_estacionados >24:
      qtd_horas_estacionados = int(input("Quantidades de horas estacionadas:"))
    cliente_conveniado = str(input("Cliente conveniado: S/N"))
    while cliente_conveniado !="S" and cliente_conveniado !="N":
      cliente_conveniado = str(input("Cliente conveniado: S/N"))
    estacionamento_fim_de_semana = str(input("Estacionamento realizado no fim de semana: S/N"))
    while estacionamento_fim_de_semana !="S" and estacionamento_fim_de_semana !="N":
      estacionamento_fim_de_semana = str(input("Estacionamento realizado no fim de semana: S/N"))
    ticket_perdido = str(input("Ticket perdido: S/N"))
    while ticket_perdido !="S" and ticket_perdido !="N":
      ticket_perdido = str(input("Ticket perdido: S/N"))
    forma_de_pagamento = str(input("Forma de pagamento:"))
    while forma_de_pagamento !="PIX" and forma_de_pagamento !="DINHEIRO" and forma_de_pagamento !="CARTAO":
      forma_de_pagamento = str(input("Forma de pagamento:"))

#====================TARIFA DE ESTACIONAMENTO===========================
    if tipo_veiculo == "CARRO":
        carros = carros+1
        total_veiculos = total_veiculos+1
        if qtd_horas_estacionados <= 2:
            valor = 12
            tarida_estacionamento = tarida_estacionamento + 12
        elif qtd_horas_estacionados <= 5:
            valor = 20
            tarida_estacionamento = tarida_estacionamento + 20
        elif qtd_horas_estacionados <= 10:
            valor = 30
            tarida_estacionamento = tarida_estacionamento + 30
        else:
            valor = 45
            tarida_estacionamento = tarida_estacionamento + 45


    elif tipo_veiculo == "MOTO":
        motos+=1
        total_veiculos+=1
        if qtd_horas_estacionados <= 2:
            valor = 6
            tarida_estacionamento = tarida_estacionamento + 6
        elif qtd_horas_estacionados <= 5:
            valor = 10
            tarida_estacionamento = tarida_estacionamento + 10
        elif qtd_horas_estacionados <= 10:
            valor = 15
            tarida_estacionamento = tarida_estacionamento + 15
        else:
            valor = 25
            tarida_estacionamento = tarida_estacionamento + 25

    elif tipo_veiculo == "VAN":
        vans+=1
        total_veiculos+=1
        if qtd_horas_estacionados <= 2:
            valor = 18
            tarida_estacionamento = tarida_estacionamento + 18
        elif qtd_horas_estacionados <= 5:
            valor = 30
            tarida_estacionamento = tarida_estacionamento + 30
        elif qtd_horas_estacionados <= 10:
            valor = 45
            tarida_estacionamento = tarida_estacionamento + 45
        else:
            valor = 65
            tarida_estacionamento = tarida_estacionamento + 65

#====================TICKET PERDIDO===========================
    if ticket_perdido == "S":
      desconto = 0
      valor = valor + 25
      taxa_ticket = taxa_ticket + 25
      tickets_perdidos+=1
#====================FIM DE SEMANA===========================
    if estacionamento_fim_de_semana == "S":
      estacionamento_taxa = estacionamento_taxa + 5
      valor = valor + 5
      atendimentos_fim_de_semana+=1
#====================CONTAGEM DE CLIENTES CONVENIADOS===========================
    if cliente_conveniado == "S":
      clientes_conveniados+=1

#====================DESCONTO DE CLIENTE CONVENIADO===========================
    if tipo_veiculo == "CARRO" and qtd_horas_estacionados <= 2 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto
    elif tipo_veiculo == "CARRO" and qtd_horas_estacionados <= 5 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto
    elif tipo_veiculo == "CARRO" and qtd_horas_estacionados <=10 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto
    elif tipo_veiculo == "CARRO" and qtd_horas_estacionados <=24 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto

    if tipo_veiculo == "MOTO" and qtd_horas_estacionados <= 2 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto
    elif tipo_veiculo == "MOTO" and qtd_horas_estacionados <= 5 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto
    elif tipo_veiculo == "MOTO" and qtd_horas_estacionados <=10 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto
    elif tipo_veiculo == "MOTO" and qtd_horas_estacionados <=24 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto

    if tipo_veiculo == "VAN" and qtd_horas_estacionados <= 2 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto
    elif tipo_veiculo == "VAN" and qtd_horas_estacionados <= 5 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto
    elif tipo_veiculo == "VAN" and qtd_horas_estacionados <=10 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto
    elif tipo_veiculo == "VAN" and qtd_horas_estacionados <=24 and cliente_conveniado == "S":
       valor_desconto = valor * desconto
       valor = valor - valor_desconto

#====================FORMAS DE PAGAMENTOS===========================
    if forma_de_pagamento == "PIX" and ticket_perdido == "N":
      pagamento_pix+=1
      ajuste_pagamento = valor * desconto_pix
      valor = valor - ajuste_pagamento


    if forma_de_pagamento == "CARTAO":
      pagamento_cartao+=1
      ajuste_pagamento = valor * 0.03
      valor = valor + ajuste_pagamento


    if forma_de_pagamento == "DINHEIRO":
      pagamento_dinheiro+=1
#======================VALOR TOTAL===================================
    valor_total = valor_total + valor
#====================MEDIA POR ATENDIMENTOS===========================
    if total_atendimentos > 0:
     media = valor_total / total_atendimentos
    else:
     media = 0
#====================MAIOR VENDA E MENOR VENDA===========================
    if total_atendimentos == 1:
     valor_da_maior_venda = valor
     valor_da_menor_venda = valor
    else:
     if valor > valor_da_maior_venda:
        valor_da_maior_venda = valor

    if valor < valor_da_menor_venda:
        valor_da_menor_venda = valor
#==========================================================================
    desconto_total = desconto_total + valor_desconto
    taxa_total = taxa_total + estacionamento_taxa + taxa_ticket + ajuste_pagamento

#====================CONTAGEM DE VALORES===========================
    if valor <=20:
      atendimentos_20+=1
    elif valor <=50:
      atendimentos_50+=1
    else:
      atendimentos_maior_50+=1



#====================COMPROVANTE DA OPÇÃO 1===========================
    print("\n-----COMPROVANTE-----\n")
    print("Tipo de veículo:",tipo_veiculo)
    print("Horas estacionadas:",qtd_horas_estacionados)
    print("Tarifa de estacionamento:R$",tarida_estacionamento)
    print("\nDesconto de convênio:R$",valor_desconto)
    print("Taxa de fim de semana:R$",estacionamento_taxa)
    print("Taxa de ticket perdido:R$",taxa_ticket)
    print("Ajuste de pagamento:R$",ajuste_pagamento)
    print("\nValor final:R$",valor)

#====================SIMULAÇÃO DE ESTACIONAMENTO===========================
  elif opcao==3:
    valor2 = 0
    tarida_estacionamento2 = 0
    estacionamento_taxa2 = 0
    desconto2 = 0.20
    valor_desconto2 = 0
    desconto_pix2 = 0.05
    fim_de_semana2 = 5
    cartao2 = 1.03
    taxa_ticket2 = 0
    ajuste_pagamento2 = 0

#====================MENU DE VEÍCULOS===========================
    print("====TIPO DE VEÍCULO====")
    print("\n1-CARRO")
    print("2-MOTO")
    print("3-VAN\n")
#====================DADOS DO CLIENTE===========================
    tipo_veiculo2 = str(input("Tipo de veículo:"))
    while tipo_veiculo2 !="CARRO" and tipo_veiculo2 !="VAN" and tipo_veiculo2!="MOTO":
     tipo_veiculo2 = str(input("Tipo de veículo:"))
    qtd_horas_estacionados2 = int(input("Quantidades de horas estacionadas:"))
    while qtd_horas_estacionados2 <=0 or qtd_horas_estacionados2 >24:
      qtd_horas_estacionados2 = int(input("Quantidades de horas estacionadas:"))
    cliente_conveniado2 = str(input("Cliente conveniado: S/N"))
    while cliente_conveniado2 !="S" and cliente_conveniado2 !="N":
      cliente_conveniado2 = str(input("Cliente conveniado: S/N"))
    estacionamento_fim_de_semana2 = str(input("Estacionamento realizado no fim de semana: S/N"))
    while estacionamento_fim_de_semana2 !="S" and estacionamento_fim_de_semana2 !="N":
      estacionamento_fim_de_semana2 = str(input("Estacionamento realizado no fim de semana: S/N"))
    ticket_perdido2 = str(input("Ticket perdido: S/N"))
    while ticket_perdido2 !="S" and ticket_perdido2 !="N":
      ticket_perdido2 = str(input("Ticket perdido: S/N"))
    forma_de_pagamento2 = str(input("Forma de pagamento:"))
    while forma_de_pagamento2 !="PIX" and forma_de_pagamento2 !="DINHEIRO" and forma_de_pagamento2 !="CARTAO":
      forma_de_pagamento2 = str(input("Forma de pagamento:"))

#====================TARIFA DE ESTACIONAMENTO===========================
    if tipo_veiculo2 == "CARRO":
        if qtd_horas_estacionados2 <= 2:
            valor2 = 12
            tarida_estacionamento2 = tarida_estacionamento2 + 12
        elif qtd_horas_estacionados2 <= 5:
            valor2 = 20
            tarida_estacionamento2 = tarida_estacionamento2 + 20
        elif qtd_horas_estacionados2 <= 10:
            valor2 = 30
            tarida_estacionamento2 = tarida_estacionamento2 + 30
        else:
            valor2 = 45
            tarida_estacionamento2 = tarida_estacionamento2 + 45

    elif tipo_veiculo2 == "MOTO":
        if qtd_horas_estacionados2 <= 2:
            valor2 = 6
            tarida_estacionamento2 = tarida_estacionamento2 + 6
        elif qtd_horas_estacionados2 <= 5:
            valor2 = 10
            tarida_estacionamento2 = tarida_estacionamento2 + 10
        elif qtd_horas_estacionados2 <= 10:
            valor2 = 15
            tarida_estacionamento2 = tarida_estacionamento2 + 15
        else:
            valor2 = 25
            tarida_estacionamento2 = tarida_estacionamento2 + 25

    elif tipo_veiculo2 == "VAN":
        if qtd_horas_estacionados2 <= 2:
            valor2 = 18
            tarida_estacionamento2 = tarida_estacionamento2 + 18
        elif qtd_horas_estacionados2 <= 5:
            valor2 = 30
            tarida_estacionamento2 = tarida_estacionamento2 + 30
        elif qtd_horas_estacionados2 <= 10:
            valor2 = 45
            tarida_estacionamento2 = tarida_estacionamento2 + 45
        else:
            valor2 = 65
            tarida_estacionamento2 = tarida_estacionamento2 + 65

#====================TICKET PERDIDO===========================
    if ticket_perdido2 == "S":
      desconto2 = 0
      valor2 = valor2 + 25
      taxa_ticket2 = taxa_ticket2 + 25
#====================FIM DE SEMANA===========================
    if estacionamento_fim_de_semana2 == "S":
      estacionamento_taxa2 = estacionamento_taxa2 + 5
      valor2 = valor2 + 5




#====================DESCONTO DE CLIENTE CONVENIADO=============================

    if tipo_veiculo2 == "CARRO" and qtd_horas_estacionados2 <= 2 and cliente_conveniado2 == "S":
       valor_desconto2 = valor2 * desconto2
       valor2 = valor2 - valor_desconto2
    elif tipo_veiculo == "CARRO" and qtd_horas_estacionados <= 5 and cliente_conveniado2 == "S":
       valor_desconto2 = valor2 * desconto2
       valor2 = valor2 - valor_desconto2
    elif tipo_veiculo2 == "CARRO" and qtd_horas_estacionados2 <=10 and cliente_conveniado2 == "S":
       valor_desconto2 = valor2 * desconto2
       valor2 = valor2 - valor_desconto2
    elif tipo_veiculo2 == "CARRO" and qtd_horas_estacionados2 <=24 and cliente_conveniado2 == "S":
       valor_desconto2 = valor2 * desconto2
       valor2 = valor2 - valor_desconto2

    if tipo_veiculo2 == "MOTO" and qtd_horas_estacionados2 <= 2 and cliente_conveniado2 == "S":
       valor_desconto2 = valor2 * desconto2
       valor2 = valor2 - valor_desconto2
    elif tipo_veiculo2 == "MOTO" and qtd_horas_estacionados2 <= 5 and cliente_conveniado2 == "S":
       valor_desconto2 = valor2 * desconto2
       valor2 = valor2 - valor_desconto2
    elif tipo_veiculo2 == "MOTO" and qtd_horas_estacionados2 <= 10 and cliente_conveniado2 == "S":
       valor_desconto2 = valor2 * desconto2
       valor2 = valor2 - valor_desconto2
    elif tipo_veiculo2 == "MOTO" and qtd_horas_estacionados2 <= 24 and cliente_conveniado2 == "S":
       valor_desconto2 = valor2 * desconto2
       valor2 = valor2 - valor_desconto2

    if tipo_veiculo2 == "VAN" and qtd_horas_estacionados2 <= 2 and cliente_conveniado2 == "S":
      valor_desconto2 = valor2 * desconto2
      valor2 = valor2 - valor_desconto2
    elif tipo_veiculo2 == "VAN" and qtd_horas_estacionados2 <= 5 and cliente_conveniado2 == "S":
      valor_desconto2 = valor2 * desconto2
      valor2 = valor2 - valor_desconto2
    elif tipo_veiculo2 == "VAN" and qtd_horas_estacionados2 <= 10 and cliente_conveniado2 == "S":
      valor_desconto2 = valor2 * desconto2
      valor2 = valor2 - valor_desconto2
    elif tipo_veiculo2 == "VAN" and qtd_horas_estacionados2 <= 24 and cliente_conveniado2 == "S":
      valor_desconto2 = valor2 * desconto2
      valor2 = valor2 - valor_desconto2

#====================FORMA DE PAGAMENTOS===========================
    if forma_de_pagamento2 == "PIX" and ticket_perdido2 == "N":
      ajuste_pagamento2 = valor2 * desconto_pix2
      valor2 = valor2 - ajuste_pagamento2

    if forma_de_pagamento2 == "CARTAO":
      ajuste_pagamento2 = valor2 * 0.03
      valor2 = valor2 + ajuste_pagamento2


#====================COMPROVANTE DE SIMULAÇÃO===========================

    print("\n-----COMPROVANTE DE SIMULAÇÃO-----\n")
    print("Tipo de veículo:",tipo_veiculo2)
    print("Horas estacionadas:",qtd_horas_estacionados2)
    print("Tarifa de estacionamento:R$",tarida_estacionamento2)
    print("\nDesconto de convênio:R$",valor_desconto2)
    print("Taxa de fim de semana:R$",estacionamento_taxa2)
    print("Taxa de ticket perdido:R$",taxa_ticket2)
    print("Ajuste de pagamento:R$",ajuste_pagamento2)
    print("\nValor final:R$",valor2)

#===========================================================================

#====================NENHUM ATENDIMENTO REGISTRADO===========================
  if total_atendimentos == 0:
    print("Nenhum atendimento registrado.")

#====================RELATÓRIO OPÇÃO2===========================
  elif opcao==2:

    print("\n====RELATÓRIO====\n")
#====================MOVIMENTO===========================
    print("\n---MOVIMENTO---")
    print("Total de veículos atendidos:",total_veiculos)
    print("Carros:",carros)
    print("Motos:",motos)
    print("Vans:",vans)

#====================FORMAS DE PAGAMENTO===========================
    print("\n---FORMAS DE PAGAMENTOS---")
    print("Dinheiro:",pagamento_dinheiro)
    print("Cartão:",pagamento_cartao)
    print("Pix:",pagamento_pix)

#====================PERFIL DOS ATENDIMENTOS===========================
    print("\n---PERFIL DOS ATENDIMENTOS---")
    print("Cliente conveniados:",clientes_conveniados)
    print("Atendimentos do fim de semana:",atendimentos_fim_de_semana)
    print("Ticket Perdidos::",tickets_perdidos)

#====================FINANCEIRO===========================
    print("\n---FINANCEIRO---")
    print("Total arrecadado:R$",valor_total)
    print("Média de valor por atendimento:R$",media)
    print("Valor da maior venda:R$",valor_da_maior_venda)
    print("Valor da menor venda:R$",valor_da_menor_venda)
    print("Total concedido em descontos:R$",desconto_total)
    print("Total cobrado em taxas:R$",taxa_total)

#====================CLASSIFICAÇÃO FINANCEIRA===========================
    print("\n--- CLASSIFICAÇÃO FINANCEIRA---")
    print("Até 20R$:",atendimentos_20)
    print("Acima de R$20 até 50R$:",atendimentos_50)
    print("Acima de R$50:",atendimentos_maior_50)

#====================TIPO DE VEÍCULO MAIS ATENDIDO===========================
    print("\n--- TIPO DE VEÍCULO MAIS ATENDIDO---")
    maior = max(carros, motos, vans)
    if (carros == motos == maior) or (carros == vans == maior) or (motos == vans == maior):
     print("Tipo de veículo mais atendido: EMPATE")
    elif carros == maior:
     print("Tipo de veículo mais atendido: CARRO")
    elif motos == maior:
     print("Tipo de veículo mais atendido: MOTO")
    else:
     print("Tipo de veículo mais atendido: VAN")

#====================PAGAMENTO MAIS UTILIZADO===========================
    print("\n--- TIPO DE PAGAMENTO MAIS UTILIZADO---")
    maior_pagamento = max(pagamento_pix, pagamento_cartao, pagamento_dinheiro)
    if (pagamento_dinheiro == maior_pagamento and pagamento_pix == maior_pagamento) or (pagamento_dinheiro == maior_pagamento and pagamento_cartao == maior_pagamento) or (pagamento_pix == maior_pagamento and pagamento_cartao == maior_pagamento):
     print("Forma de pagamento mais utilizada: EMPATE")
    elif pagamento_pix == maior:
     print("Forma de pagamento mais atendida: PIX")
    elif pagamento_cartao == maior:
     print("Forma de pagamento mais atendida: CARTÃO")
    else:
     print("Forma de pagamento mais atendida: DINHEIRO")
    if total_atendimentos > 0:
     percentual = (clientes_conveniados / total_atendimentos) * 100
    else:
     percentual = 0
#====================PERCENTUAL DE CLIENTES CONVENIADOS,===========================
    print("\n===PERCENTUAL DE CLIENTES CONVENIADOS===")
    print("Percentual de clientes conveniados:", round(percentual, 1), "%")