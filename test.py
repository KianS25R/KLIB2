import machineLearning


a = machineLearning.RNNLM_HYBRID(5, dictionary="vocab.mem", veclength=16, neurons=64, load_vocab="test")

a.warmup("cat sat duck fuck suckie_suckie")

a.run(1)