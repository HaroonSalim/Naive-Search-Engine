# Big-Data-Assignment
Haroon Salim 21i-1663
Immad Shahid Qureshi 21i-1664
Ahmad Luqman 22i-2018

# Language to be used: 
Why Python? 
Because we are familiar with the language and have some practice and grip over it.

Based on the given instructions and dataset description, here's how we approach developing the Naïve Search Engine utilising MapReduce, focusing on the ARTICLE_ID and SECTION_TEXT columns and following the basic principles of the vector space model for information retrieval: 

**Data Preprocessing:** Extract the necessary columns (ARTICLE_ID and SECTION_TEXT) from the provided dataset. Perform basic text cleaning operations such as removing punctuation, converting text to lowercase, and tokenisation. Optionally, perform additional preprocessing steps like stopword removal and stemming. 

**Indexing Phase: **

Mapper: Tokenize SECTION_TEXT and emit (word, 1) pairs. 
Reducer: Aggregate word frequencies to generate a set of unique words and assign unique IDs to each word. 

 
Mapper: Tokenize SECTION_TEXT and emit (word, ARTICLE_ID) pairs. 
Reducer: Count the number of unique ARTICLE_IDs for each word to calculate IDF values. 
Indexer Phase: 

Mapper: Tokenize SECTION_TEXT, calculate TF/IDF weights for each word, and emit (ARTICLE_ID, word_id: TF/IDF) pairs. 
Reducer: Aggregate TF/IDF values for each ARTICLE_ID to generate the vector representation of each document. 

Query Processing Phase: Implement the Query Vectorizer function to generate the vector representation of a query using TF/IDF weights. Implement the Relevance Analyzer task using MapReduce.

Mapper: Receive the query vector and document vector pairs, calculate the inner product, and emit (ARTICLE_ID, relevance_score) pairs. 

Reducer: Aggregate relevance scores and sort the documents based on relevance. 

Testing: Conduct local testing on a smaller dataset to validate the correctness and performance of your MapReduce jobs. Use unit tests to ensure the individual components work as expected. 

Deployment: Package the MapReduce jobs into a JAR file. Deploy the JAR file to the Hadoop cluster and run the indexing and query processing tasks using Hadoop Streaming. 

Integration and User Interface: Integrate the MapReduce jobs into a cohesive search engine application. Provide a user interface for users to input queries and display the relevant documents. 

Version Control and Collaboration: Set up a public GitHub repository to track the project's progress and collaborate with the team. Use incremental commits to document changes and facilitate collaboration. 

