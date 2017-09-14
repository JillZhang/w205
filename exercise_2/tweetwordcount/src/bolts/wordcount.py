from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to the database
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        cur = conn.cursor()
        uWord = word
        cur.execute( "SELECT * FROM tweetwordcount WHERE word = %s", (uWord,))
        
        if cur.rowcount == 0:
            cur.execute("INSERT INTO tweetwordcount (word,count) \
                        VALUES (%s, 1)",(uWord,))
            conn.commit()
        else:
            records = cur.fetchall()
            uCount=records[0][1] + 1
            cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (uCount, uWord))
            conn.commit()
        
        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
