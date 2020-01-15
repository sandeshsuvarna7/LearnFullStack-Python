import psycopg2

con = None
try:
    con = psycopg2.connect(database="dvdrental", user="postgres", password="Colgate@123", host="127.0.0.1", port="5432")
    print("Database opened successfully...")
    
    cur = con.cursor()
    query = "SELECT * FROM public.actor where first_name Like '{0}' and last_name Like '{1}'".format("S%", "%r%")
    cur.execute(query)
    result = cur.fetchall()
    for r in result:
        print("Actor ID: ", r[0])
        print("Actor First Name: ", r[1])
        print("Actor Last Name: ", r[2])
        print("Last time record updated: ", r[3], "\n")

except:
    print("Error in connection...")
    
finally:
    if con != None:
        con.close()
        print("Database connection closed...")
        

