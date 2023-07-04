from sentencepiece import SentencePieceTrainer

data = "datasets/dataset.txt"
max_words = 31000
model_type = "bpe"
model_prefix = "bpe_model"
pad_id = 0
unk_id = 1
bos_id = 2
eos_id = 3

sentencepiece_params = ' '.join([
    "--input={}".format(data),
    "--model_type={}".format(model_type),
    "--model_prefix={}".format(model_prefix),
    "--vocab_size={}".format(max_words),
    "--pad_id={}".format(pad_id),
    "--unk_id={}".format(unk_id),
    "--bos_id={}".format(bos_id),
    "--eos_id={}".format(eos_id)
])

SentencePieceTrainer.train(sentencepiece_params)




