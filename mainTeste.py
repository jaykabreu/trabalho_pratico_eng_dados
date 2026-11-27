import psycopg2

def create(table, values):
    try:
        match table:
            case "usuario":
                insert_script = "INSERT INTO universidade.usuario (cpf, nome, data_nascimento, email, telefone, login, senha) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                curs.execute(insert_script, values)
                conn.commit()

            case "professor":
                insert_script = "INSERT INTO universidade.professor (mat_professor, departamento, cpf, formacao, data_admissao, tipo_jornada_trabalho, salario) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                curs.execute(insert_script, values)
                conn.commit()

            case "leciona":
                insert_script = "INSERT INTO universidade.leciona (id_turma, mat_professor) VALUES (%s,%s)"
                curs.execute(insert_script, values)
                conn.commit()

            case "turma":
                insert_script = "INSERT INTO universidade.turma (cod_disc, id_turma, ano, semestre, numero) VALUES (%s,%s,%s,%s,%s)"
                curs.execute(insert_script, values)
                conn.commit()

            case _:
                raise ValueError("Tabela não disponível.")

        print("Usuario cadastrado.")
    except:
        print("Não foi possível cadastrar o usuário.")

def read(table):
    try:
        match table:
            case "usuario":
                curs.execute("SELECT * FROM universidade.usuario;")

            case "professor":
                curs.execute("SELECT * FROM universidade.professor;")

            case "leciona":
                curs.execute("SELECT * FROM universidade.leciona;")

            case "turma":
                curs.execute("SELECT * FROM universidade.turma;")
        
            case _:
                raise ValueError("Tabela não disponível.")
            
        for data in curs.fetchall():
            print(data)

    except:
        print("Ocorreu um erro.")

def update(sql):
    try:
        curs.execute(sql)
        conn.commit()

        print("Alteração bem-sucedida.")
    except:
        print("Não foi possível executar a alteração.")

def delete(sql):
    try:
        curs.execute(sql)
        conn.commit()

        print("Deletado com sucesso.")
    except:
        print("Não foi possível deletar.")

### ===================================================== ###

conn = None
curs = None
try:
    #conexão feita com db hospedado na aws
    conn = psycopg2.connect(host="",
                                    port="",
                                    dbname="",
                                    user="",
                                    password="")

    #abre um cursor para executar as operações no db
    curs= conn.cursor()

    #aqui estão os scripts para o CREATE, READ, UPDATE e DELETE (chama a função definida acima do codigo)

    #iserir dados na tabela
    insert_table = "usuario"
    insert_values = (40028922,"Jayk","2007-09-12",["jayk@gmail.man"],["7922982004"],"Jaykeulogin","essaeasenha")
    create(insert_table, insert_values)

    #ler dados de alguma tabela
    read_table = "professor"
    read(read_table) 

    #atualizar algo na tabela
    update_sql = "UPDATE universidade.usuario SET nome='jorge' WHERE nome='Prof E'"
    update(update_sql)

    #deletar algo na tabela
    delete_sql = "DELETE FROM universidade.usuario WHERE nome='jorge'"
    delete(delete_sql)

except:
    print("[ERRO] Não foi possível efetuar a conexão com o banco de dados")
finally:
    if conn is not None:
        conn.close()
    if curs is not None:
        curs.close()



