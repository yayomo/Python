import pyodbc

# Configura los parámetros de conexión
conn_params = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=tu_servidor;'
    'DATABASE=msdb;'  # La base de datos 'msdb' es donde se guardan los trabajos del Agente SQL Server
    'UID=tu_usuario;'
    'PWD=tu_contraseña'
)

try:
    # Conectar a la base de datos
    conn = pyodbc.connect(conn_params)
    cursor = conn.cursor()

    # Definir y ejecutar el plan de mantenimiento
    # Suponiendo que el plan de mantenimiento está definido como un trabajo del Agente SQL Server
    job_name = 'NombreDelPlanDeMantenimiento'
    query = f"""
    DECLARE @job_id UNIQUEIDENTIFIER;
    SELECT @job_id = job_id FROM msdb.dbo.sysjobs WHERE name = '{job_name}';
    EXEC msdb.dbo.sp_start_job @job_id = @job_id;
    """

    # Ejecutar la consulta
    cursor.execute(query)
    conn.commit()

    print(f"El plan de mantenimiento '{job_name}' se ha iniciado exitosamente.")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    # Cerrar la conexión
    if cursor:
        cursor.close()
    if conn:
        conn.close()
