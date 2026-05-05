from database_logic import load_accounts_db

def test_load_accounts_db(mocker):
    """
    Vérifie que load_accounts_db retourne bien les données
    que la base de données (simulée) lui envoie.
    """
    # 1. Préparation
    mock_connect = mocker.patch('database_logic.psycopg2.connect')

    fake_data = [
        (1, 'Alice', 'alice@email.com', 1000),
        (2, 'Bob', 'bob@email.com', 2000)
    ]
    mock_cursor = mock_connect().__enter__().cursor().__enter__()
    mock_cursor.fetchall.return_value = fake_data

    # 2. Appel
    result = load_accounts_db()

    # 3. Assertions
    mock_cursor.execute.assert_called_once_with(
        "SELECT id, name, email, balance FROM accounts ORDER BY id"
    )
    assert result == fake_data