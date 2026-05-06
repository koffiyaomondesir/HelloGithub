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
                "UPDATE accounts SET email = %s, balance = %s WHERE id = %s",
                (email, balance or 0, account_id)
            )
            conn.commit()