#train_file=$1
../bin/word2vec -train ../based_data/paticipant_train/combineout_userf_train.txt -output ../data/race_partake_vec_2.txt -size 100 -window 2 -sample 1e-3-negative 5 -hs 0 -binary 0 -cbow 1 -iter 100 -save-vocab ../data/race_partake_vocab_2.txt
