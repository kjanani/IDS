# IDS
A recommender for hashtags on Twitter

- Step 1:
	Copy files from ML-MACHINE.
	``for file in `ssh ipaddress ls | tail -n 15`; do scp user@ipaddress:~/$file . ; done``

- Step 2: ``createDB.py``
	There's a separate collection for each round.
	Change ``full_collection_name`` and ``hashtag_collection_name``
	Can run ``createDB.py`` with both ``fulldb()`` and ``create\_collection\_hashtag()`` intact

- Step 3: ``text\_processing.py`` 
	Change collection name at the top.
	change ``run_number``
	``get_vocab()`` - After this, one needs to manually look at the vocab file for deciding the vocabulary.
	``convert_to_btm_input_training()``

- Step 4: ``model_scripts.py``
	Change ``run_number``; change ``no_topics``
	can run ``run_btm_learning()`` and ``run_btm_inference()`` intact

	Next, run change the collection name inside ``getHashtags()`` and run it!

	

