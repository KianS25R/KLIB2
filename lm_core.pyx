# lm_core.pyx

from KLIB2.kmath import FixSoftmax, Argmax, ReLu, LeakyReLu, log

cdef double hybrid(double z):
    if z <= 0:
        return LeakyReLu(z)
    else:
        return ReLu(z)

cdef double hybrid_prime(double z):
    if z <= 0:
        return 0.01
    else:
        return 1.0

cpdef activate_step(obj, int indexa, int target):
    """
    obj = your RNNLM_HYBRID instance
    This function directly reads/writes obj.embedings, obj.lweights, etc.
    """

    cdef int neurons = obj.neurons
    cdef int vocabL = obj.vocabL
    cdef int vecL = obj.vecL
    cdef double lr = obj.lr

    cdef int H, i, k
    cdef double val

    # local references for speed
    embed = obj.embedings
    lw = obj.lweights
    lhw = obj.lhweights
    bias = obj.bias
    who = obj.who
    bo = obj.bo
    ht = obj.ht

    # allocate local buffers
    ut = [0.0] * neurons
    ot = [0.0] * vocabL
    d_ot = [0.0] * vocabL
    d_bo = [0.0] * vocabL
    d_ht = [0.0] * neurons
    d_ut = [0.0] * neurons
    d_bias = [0.0] * neurons
    d_embed = [0.0] * vecL

    d_who = [[0.0 for _ in range(neurons)] for _ in range(vocabL)]
    d_lweights = [[0.0 for _ in range(vecL)] for _ in range(neurons)]
    d_lhweights = [[0.0 for _ in range(neurons)] for _ in range(neurons)]

    # -----------------------------
    # Forward pass
    # -----------------------------
    for H in range(neurons):
        val = 0.0
        for i in range(vecL):
            val += lw[H][i] * embed[indexa][i]
        for i in range(neurons):
            val += lhw[H][i] * ht[i]
        val += bias[H]
        ut[H] = val

    for i in range(neurons):
        ht[i] = hybrid(ut[i])

    for k in range(vocabL):
        val = 0.0
        for i in range(neurons):
            val += who[k][i] * ht[i]
        val += bo[k]
        ot[k] = val

    pt = FixSoftmax(ot)
    obj.nexttoken = Argmax(pt)
    obj.loss = -log(pt[target])

    # -----------------------------
    # Backprop
    # -----------------------------
    for i in range(vocabL):
        if i == target:
            d_ot[i] = pt[i] - 1.0
        else:
            d_ot[i] = pt[i]

    for k in range(vocabL):
        for i in range(neurons):
            d_who[k][i] = d_ot[k] * ht[i]

    for k in range(vocabL):
        d_bo[k] = d_ot[k]

    for i in range(neurons):
        val = 0.0
        for k in range(vocabL):
            val += d_ot[k] * who[k][i]
        d_ht[i] = val

    for i in range(neurons):
        d_ut[i] = d_ht[i] * hybrid_prime(ut[i])

    for H in range(neurons):
        for i in range(vecL):
            d_lweights[H][i] = d_ut[H] * embed[indexa][i]

    for H in range(neurons):
        for i in range(neurons):
            d_lhweights[H][i] = d_ut[H] * ht[i]

    for H in range(neurons):
        d_bias[H] = d_ut[H]

    for i in range(vecL):
        val = 0.0
        for H in range(neurons):
            val += d_ut[H] * lw[H][i]
        d_embed[i] = val

    # -----------------------------
    # Apply gradients
    # -----------------------------
    for k in range(vocabL):
        for i in range(neurons):
            who[k][i] -= lr * d_who[k][i]

    for k in range(vocabL):
        bo[k] -= lr * d_bo[k]

    for H in range(neurons):
        for i in range(vecL):
            lw[H][i] -= lr * d_lweights[H][i]

    for H in range(neurons):
        for i in range(neurons):
            lhw[H][i] -= lr * d_lhweights[H][i]

    for H in range(neurons):
        bias[H] -= lr * d_bias[H]

    for i in range(vecL):
        embed[indexa][i] -= lr * d_embed[i]

    obj.reply.append(obj.dictionary[obj.nexttoken])
