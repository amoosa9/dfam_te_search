#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

"""A CGI script that searches a transposable element database to autocomplete
element name searches in an HTML form. Limits results to five to prevent
long search suggestion lists"""

def main():

    print("Content-Type: application/json\n\n")

    #gets form data
    form = cgi.FieldStorage()
    term = form.getvalue('search_term')

    #checks for blank term and formats them for SQL query
    term = process_term(term)

    #queries database for matching TEs
    results = query_db(term)

    #prints the matches in JSON format
    print(json.dumps(results))

#formats search terms for SQL query
def process_term(term):

	#checks for blank inputs 
	if term is None:
		term = "" 

	#formats inputs for SQL query
	term = "%" + term + "%"

	return term

#queries TE database for elements that match the searched type or family
def query_db(term):
        
    #creates connection to mySQL database
    conn = mysql.connector.connect(user='amoosa1',
	 			   password='IHaveTwelveSeals!',
				   host='localhost', database='amoosa1_te')

    #cursors for checking types and families
    curs = conn.cursor()
    
    #results of the queries
    results = { 'match_count': 0, 'matches': list() }

    #queries the database for element types that match term
    qry = """
	SELECT e.type AS type, e.type LIKE term AS type_found,
	       e.fam AS family, e.fam LIKE term AS fam_found
	FROM elements e
	WHERE e.type LIKE %s OR e.fam LIKE %s
    """
    curs.execute(qry, (term, term))

    #adds matches to results
    for (type, family, type_found, fam_found) in curs:

	#if the match was to an element type
	if type_found == 1:
        	results['matches'].append({'label': type, 'value': type})

	#if the match was to a family of elements
	elif fam_found == 1:
		results['matches'].append({'label': family, 'value': family})

	#increment count of matches found
        results['match_count'] += 1

	#terminates when five matches are added
	if results['match_count'] == 5:
		break

    #closes cursors
    curs.close()

    #closes connection to the mySQL database
    conn.close()

    return results


if __name__ == '__main__':
    main()
