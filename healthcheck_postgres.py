 # pip install psycopg2-binary or for the newer version: pip install psycopg
import psycopg2 # or import psycopg for the newer version

def postgresql_health_check(dbname, user, password, host='localhost', port='5432'):
    try:
        # Establish a connection
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        # Create a cursor object
        cursor = conn.cursor()
        # Execute a simple query to check connectivity
        cursor.execute("SELECT 1")
        # If no exception occurs, the connection is successful
        print(f"PostgreSQL health check successful for database '{dbname}' on {host}:{port}")
        return True
    except psycopg2.OperationalError as e:
        # Handle connection errors
        print(f"PostgreSQL health check failed for database '{dbname}' on {host}:{port}. Error: {e}")
        return False
    finally:
        # Close the connection if it was established
        if 'conn' in locals() and conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    # Replace with your actual database credentials
    db_name = "your_database_name"
    db_user = "your_username"
    db_password = "your_password"
    db_host = "localhost" # or your remote host
    db_port = "5432"

    postgresql_health_check(db_name, db_user, db_password, db_host, db_port)
