# matchmaker
Matchmaker is a document that allows you to create matches of documents by their first column.

# Concept
Take a base or main file, then it takes a second file which will try to match all their ids into the base, same concept as a LEFT JOIN in SQL. Take a full table on right and join anything you can find from left table.

# Limitations
- You can only do this with two files.
- Files must be .CSV extension file only.
- Place files on same folder.
- Each .CSV only works with unique key_id on the first column just like a primary-key on DB's table.
- If you don't have unique keys on each file it will not work. The idea is to take a unique id on file A and it can be found on file B (matching)
- You can fabricate a unique value if you don't have officially one by joining columns with numbers on each spreadsheet and place them as first column. Per example: a school_id + a current grade + a next grade will create a unique primary key to work, just remember, if there are duplicates in your file you will have incorrect matching, so file must be duplicate free on both files.
- I haven't check if a file with headers my not work, so use headers always.
- The intended use is for non duplicate keys only, can be use on massive amounts of date but duplicate free.

# Execution
> python3 main.py
