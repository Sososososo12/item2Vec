#train_file=$1
../bin/word2vec -train ../based_data/combineout_userf_train.txt -output ../data/race_vec.txt -size 128 -window 3 -sample 1e-3-negative 5 -hs 0 -binary 1 -cbow 1 -iter 50 -save-vocab ../data/vocab.txt
