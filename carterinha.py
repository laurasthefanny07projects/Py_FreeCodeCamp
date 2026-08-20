from datetime import date

first_name = 'Laura'
last_name = 'Santos' 
full_name = first_name + ' ' + last_name
print(full_name)

address_facul = 'Curso Técnico Inovação, CEP 14105-425'
address_facul += ', n° 123, Jardim Primavera - SP '
print(address_facul)

RA_id = '123456789-0'
full_RA = 'RA: ' + RA_id
print(full_RA)

tec_name = "Técnico em Desenvolvimento Web"
carteirinha = 'Nome: ' + full_name + ' | ' + full_RA + ' | Curso/Técnico: ' + tec_name + ' | ' + 'Endereço: ' + address_facul
print(carteirinha)

emissao_c = date(2026, 8, 19)
emissao_carteirinha = emissao_c.strftime('%d/%m/%Y')
print(emissao_carteirinha)

first_name = 'Laura'
last_name = 'Santos' 
full_name = first_name + ' ' + last_name
print(full_name)

address_facul = 'Curso Técnico Inovação, CEP 14105-425'
address_facul += ', n° 123, Jardim Primavera - SP '
print(address_facul)

RA_id = '123456789-0'
full_RA = 'RA: ' + RA_id
print(full_RA)

emissao_c = date(2026, 8, 19)
emissao_carteirinha = emissao_c.strftime('%d/%m/%Y')
print(emissao_carteirinha)

validade_c = date(2028,8,19)
validade_carteirinha = validade_c.strftime('%d/%m/%Y')
print(validade_carteirinha)


carteirinha =f'{carteirinha} | Data de emissão: {emissao_carteirinha} | Data de validade: {validade_carteirinha}'
print(carteirinha)