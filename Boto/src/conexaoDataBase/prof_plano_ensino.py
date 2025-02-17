from mysql.connector import ProgrammingError
from Boto.src.conexaoDataBase.databaseBOTO import nova_con

"""Função que recebe o link do plano de ensino e a coloca na tabela do banco de dados"""

async def colocar_plano(link, matricula_professor) -> int:

    SQL = "UPDATE professor SET plano_de_ensino = %s WHERE matricula= %s "
    val = (str(link), str(matricula_professor))

    with nova_con() as con:
        try:
            cursor = con.cursor()
            cursor.execute(SQL,val)
            con.commit()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
