import sqlite3
conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id
#   (inteiro), nome (texto), idade (inteiro) e curso (texto).
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

#cursor.execute('DROP TABLE gerentes')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario ')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')
# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no
#   exercício anterior.
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Isadora",18,"letras")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"João",20,"matemática")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Sofia",17,"ciência da computação")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Lucas",17,"farmácia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Luisa",19,"medicina")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6,"Ana",23,"Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(7,"Matheus",20,"Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(8,"Carlos",17,"ciência da computação")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(9,"Luis",24,"Engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(10,"Joana",19,"Engenharia")')

#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
 #   print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#dados = cursor.execute('SELECT nome, idade FROM alunos  WHERE idade>20')
#for alunos in dados:
 #   print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
#dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
#for alunos in dados:
#    print(alunos)

#d) Contar o número total de alunos na tabela
#dados = cursor.execute('SELECT id FROM alunos ORDER BY id DESC')
#for alunos in dados:
#    print(alunos)


#4. Atualização e Remoção
#   a) Atualize a idade de um aluno específico na tabela
#cursor.execute('UPDATE alunos SET idade="22" WHERE nome="João"')

#b) Remova um aluno pelo seu ID.
#cursor.execute('DELETE FROM alunos where id=3')


#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), 
#idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

#cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), idade INT, saldo REAL)')
'''cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Joana",31,3200.00)')
cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Gustavo",18,915.00)')
cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Emili",30,3250.00)')
cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Pedro",40,1000.00)')
cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Manoela",20,2500.00)')
cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Thiago",32,800.00)')
cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Larissa",22,980.00)')
cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("José",51,2500.00)')
cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Marcia",44,3800.00)')
cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Carlos",33,1100.00)')
cursor.execute('INSERT INTO clientes(nome,idade,saldo) VALUES("Joana",28,5000.00)')
'''


#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
#for clientes in dados:
#    print(clientes)

#b) Calcule o saldo médio dos clientes.
#cursor.execute('SELECT AVG(saldo) FROM clientes')
#saldo_medio = cursor.fetchone()[0]
#print(f"Saldo médio:{saldo_medio:.2f}")

#c) Encontre o cliente com o saldo máximo.
#cursor.execute('SELECT MAX(saldo) FROM clientes')
#saldo_max = cursor.fetchone()[0]
#print(f"Saldo máximo:{saldo_max:.2f}")

#d) Conte quantos clientes têm saldo acima de 1000.
#cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
#contagem = cursor.fetchone()[0]
#print(f"Clientes com saldo maior que 1000: {contagem}")


#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
#cursor.execute('UPDATE clientes SET saldo=1000.20 WHERE nome="Gustavo"')

#b) Remova um cliente pelo seu ID.
#cursor.execute('DELETE FROM clientes where id=3')


#8. Junção de Tabelas
'''Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real). Insira algumas
compras associadas a clientes existentes na tabela "clientes".
Escreva uma consulta para exibir o nome do cliente, o produto e o
valor de cada compra.'''

#cursor.execute('CREATE TABLE compras(id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INTEGER NOT NULL, PRODUTO VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

'''
cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(1,"Notebook",3500.00)')
cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(2,"Ipad",4000.00)')
cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(5,"Geladeira",7000.00)')
cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(9,"Celular",2200.00)')
cursor.execute('INSERT INTO compras(cliente_id,produto,valor) VALUES(11,"Sofá",4500.00)')
'''
dados = cursor.execute('SELECT clientes.id, clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id')
for compra in dados:
    print(compra)

conexao.commit()
conexao.close()