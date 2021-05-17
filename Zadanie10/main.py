import random

class CantSPLA(Exception):
    pass

def predict_learn(row, w):
	activation = w[0]
	for i in range(len(row)-1):
		activation += w[i + 1] * row[i]
	return 1.0 if activation >= 0.0 else 0.0

def spla(train, l_rate):
    w = [random.random() / 5 for i in range(len(train[0]))]
    retries = 0
    while True:
        retries += 1
        if retries > 1000:
            raise CantSPLA()
        sum_error = 0.0
        
        for row in train:
            prediction = predict_learn(row, w)
            error = row[-1] - prediction
            sum_error += error**2
            if abs(error) < 0.01:
                continue
            w[0] = w[0] + l_rate * error
            for i in range(len(row)-1):
                    w[i + 1] = w[i + 1] + l_rate * error * row[i]
        #print('>lrate=%.3f, error=%.3f' % (l_rate, sum_error))
        if sum_error < 0.01:
            break
    return w
 
OR_DATASET = [
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1)
]

AND_DATASET = [
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 0)
]

XOR_DATASET = [
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 0)
]

l_rate = 0.0001

and_weights = spla(AND_DATASET, l_rate)
print("-----AND-----")
print("Weights:", and_weights)
print("(0, 0)", predict_learn((0, 0, 0), and_weights))
print("(1, 0)", predict_learn((1, 0, 0), and_weights))
print("(0, 1)", predict_learn((0, 1, 0), and_weights))
print("(1, 1)", predict_learn((1, 1, 0), and_weights))

or_weights = spla(AND_DATASET, l_rate)
print("-----OR-----")
print("Weights:", or_weights)
print("(0, 0)", predict_learn((0, 0, 0), or_weights))
print("(1, 0)", predict_learn((1, 0, 0), or_weights))
print("(0, 1)", predict_learn((0, 1, 0), or_weights))
print("(1, 1)", predict_learn((1, 1, 0), or_weights))

print("-----XOR-----")
try:
    spla(XOR_DATASET, l_rate)
except CantSPLA:
    print("Maximum number of epoch exceeded (1000)")