from contas import Conta
from clientes import Cliente
import sqlite3

class Banco:
    def __init__(self, db_name="banco.db"):
        self.conn = sqlite3.connect(db_name)
        self.criar_Tabelas()

    def criar_Tabelas(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            cpf TEXT PRIMARY KEY,
            nome TEXT,
            endereco TEXT
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas (
            numero INTEGER PRIMARY KEY,
            cpf_cliente TEXT,
            saldo REAL,
            FOREIGN KEY (cpf_cliente) REFERENCES clientes (cpf)
        )
        ''')
        self.conn.commit()

    def criar_Conta(self, numero, cliente, saldo):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO contas (numero, cpf_cliente, saldo) VALUES (?, ?, ?)
        ''', (numero, cliente.cpf, saldo))
        self.conn.commit()

    def cliente_ja_cadastrado(self, cpf):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT COUNT(1) FROM clientes WHERE cpf = ?
        ''', (cpf,))
        return cursor.fetchone()[0] > 0

    def adicionar_Cliente(self, novoCliente):
        if not self.cliente_ja_cadastrado(novoCliente.cpf):
            cursor = self.conn.cursor()
            cursor.execute('''
            INSERT INTO clientes (cpf, nome, endereco) VALUES (?, ?, ?)
            ''', (novoCliente.cpf, novoCliente.nome, novoCliente.endereco))
            self.conn.commit()
            print(f"Cliente {novoCliente.nome} foi adicionado!")
        else:
            print(f"Cliente {novoCliente.nome} ja possui cadastro.")
