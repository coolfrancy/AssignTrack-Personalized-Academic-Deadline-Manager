#edits phone_number for user
def edit_phone_number(user_id, new_phone_number):
    try:
        from backend.db_conn import connect_to_db


        conn=connect_to_db()
        cursor=conn.cursor()

        #query to edit the users info into the reminders table
        cursor.execute("""
            UPDATE users SET phone_number = %s WHERE id = %s
            """,(new_phone_number, user_id))
        
        conn.commit()

        return 'success'

    except sqlite3.IntegrityError as e:
        if 'reminders.user_id' in str(e):
            return 'Invalid, user have yet to add a phone_number to edit'

    except Exception as e:
        return f"Unexpected error occured when editting reminder {e}"

    finally:
        if conn:
            conn.close()

#edits email for user
def edit_user_email(user_id, new_email_address):
    try:
        from backend.db_conn import connect_to_db


        conn=connect_to_db()
        cursor=conn.cursor()

        #query to edit the users info into the reminders table
        cursor.execute("""
            UPDATE users SET email_address = %s WHERE id = %s
            """,(new_email_address, user_id))
        
        conn.commit()

        return 'success'

    except sqlite3.IntegrityError as e:
        if 'reminders.user_id' in str(e):
            return 'Invalid, user have yet to add a email_address to edit'

    except Exception as e:
        return f"Unexpected error occured when editting reminder {e}"

    finally:
        if conn:
            conn.close()
