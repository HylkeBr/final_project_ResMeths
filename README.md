# final project #
Final project for introduction to research methods

__Use of ’jou’ and ’jouw’ in Dutch tweets__


## twitter_jou_jouw.py ##
The code is used to find the tweets with 'jou' or 'jouw' in them.
Prints the the query words 'jou'/'jouw' with a context of three words on each side.
'jou'/'jouw' are highlighted when printing in to the screen.

### Argument: ###
Argument is the compressed file that contains all the information of the tweets.

Usage: 

	$ python3 twitter_jou_jouw.py <twitterdata-file.gz>

### How the code works: ###
First imports the necessary libraries.

Opens the compressed file with gzip library, reads it's contents and puts it in the variable 'infile'.

After that it sets certein variables to zero. Those variables count the amount of tweets that meet their requirements.

Next, a for-loop is used to loop through the file tweet by tweet. Every tweet's data is given on a single line, therefore a for-loop can be used to loop through them.

Then it finds the contents of the tweet by searching by the key 'text'. The value that belongs to this key is the content of the tweet.

When the contents are found, some if-statements are presented to filter out the tweets that have the words 'jou' or 'jouw' in their contents. The if-statements search for ' jou ' or ' jouw '. The spaces around the words are there to make certein it are single words that are found and not parts of words.

Inside the if-statements every word of the tweet's content gets put in a list. Also the index of the word 'jou'/'jouw' is saved in a variable to later get the right word and context.

The counting variables are updated with a '+= 1', so they keep track of how many items there have been passed through.

Almost at the end a new list is made that only concludes the word 'jou' or 'jouw' in the middle and have a pre-defined length of words around them. Both before and after the words. This is done by slicing in the first list.

Then there's another for-loop. This one is only used for printing the right things to the screen, with colored 'jou'/'jouw' for the ease of use when manually annotating the tweets.

All the way at the end there are some print statements to show the counting variables that kept track of the amount of items it ran through. They are printed with a context to keep them apart easily.


## find_random_files.sh ##
The script is used to find two random files in a directory.

### Argument: ###
This script does not take any arguments.

Only if file permission to run the script isn't added:

	$ chmod +x find_random_files.sh

Usage: 

	$ ./find_random_files.sh

### How the script works: ###
The file has to be in the directory from which you want to extract two random files from.

The script first lists all items with the 'ls' command. 
Then it takes the output of that and shuffels it in a random order with the 'shuf' command.
To only get two random files, the argument '-n 2' is added to the 'shuf' command. This causes it to only output two files.
