def create_account_db(name, email, balance):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO accounts (name, email, balance) VALUES (%s, %s, %s)",
                (name, email, balance)
            )
            conn.commit()
def update_account_db(account_id, name, email, balance):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE accounts SET balance = %s, name = %s, email = %s WHERE id = %s",
                (balance or 0, name, email, account_id)
            )
            conn.commit()