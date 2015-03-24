$Author : Ashrith Jalagam

1) First, Create a primary index from a wiki dump file.
Command : "python assignment_index.py 100.xml"
Output : Creates a Primary Index inside a folder "Index" and also a file "index.txt" which contains metadata about the created files.
Also, the entire index is split into multiple files because of buffer size limitation

2) Next, Create a Secondary index from the Primary Index by using the events.
Command : "python assignment_sindex.py ./Index/index.txt"
Output : The Secondary index "S_index.txt" is created inside the folder "Index".

3) Finally, to give the results on the query file "queryfile.txt",
Command : "python search.py queryfile.txt Index/S_index.txt"

This gives top 10 results on each query based on the ranking function that I used.
