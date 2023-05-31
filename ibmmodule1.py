def initialize_translation_prob(sent_pairs):
    translation_prob = {}
    for (e, f) in sent_pairs:
        for e_word in set(e):
            for f_word in set(f):
                if (e_word, f_word) not in translation_prob:
                    translation_prob[(e_word, f_word)] = 1.0 / len(set(f))
    return translation_prob

from collections import defaultdict

def ibm_model_1(sent_pairs, num_iterations):
    # Preprocess the sentences by tokenizing them and converting them to 
lowercase
    sent_pairs = [tuple(map(str.lower, sent_pair)) for sent_pair in 
sent_pairs]
    sent_pairs = [tuple(map(str.split, sent_pair)) for sent_pair in 
sent_pairs]

    # Create a set of all English and Turkish words
    e_vocab = set()
    f_vocab = set()
    for (e_sent, f_sent) in sent_pairs:
        e_vocab.update(e_sent)
        f_vocab.update(f_sent)

    # Initialize translation probabilities uniformly
    t = defaultdict(lambda: 1.0 / len(f_vocab))
    t_prev = None

    # Run EM algorithm for a fixed number of iterations
    for iteration in range(num_iterations):
        print(f"Iteration {iteration+1}:")
        count = defaultdict(float)
        total = defaultdict(float)
        for (e_sent, f_sent) in sent_pairs:
            # Compute the normalization factor for this sentence pair
            s_total = defaultdict(float)
            for e_word in e_sent:
                for f_word in f_sent:
                    s_total[e_word] += t[(e_word, f_word)]

            # Print s-total values
            print(f"s-total(e) for sentence pair ({e_sent}, {f_sent}):")
            for e_word in e_sent:
                print(f"\t{s_total[e_word]:.4f} (e_word: {e_word})")

            # Collect counts
            for e_word in e_sent:
                for f_word in f_sent:
                    count[(e_word, f_word)] += t[(e_word, f_word)] / 
s_total[e_word]
                    total[f_word] += t[(e_word, f_word)] / s_total[e_word]

        # Print expected counts and total(f)
        print("Expected counts (count(e|f)):")
        for (e_word, f_word) in count:
            print(f"\tcount({e_word}|{f_word}) = {count[(e_word, 
f_word)]:.4f}")
        print("Total(f):")
        for f_word in f_vocab:
            print(f"\ttotal({f_word}) = {total[f_word]:.4f}")

        # Estimate probabilities
        for (e_word, f_word) in count:
            t[(e_word, f_word)] = count[(e_word, f_word)] / total[f_word]

        # Print estimate probabilities
        print("Estimated probabilities (t(e|f)):")
        for (e_word, f_word) in t:
            print(f"\tt({e_word}|{f_word}) = {t[(e_word, f_word)]:.4f}")

        # Check for convergence
        if t == t_prev:
            break
        t_prev = t.copy()

    return t

sent_pairs = [("merhaba dünya", "hello world"), ("bugün hava güzel", "the 
weather is nice today"),
              ("ben bir kitap okuyorum", "I am reading a book"), ("seni 
seviyorum", "I love you"),
              ("ne yapıyorsun", "what are you doing")]

t = ibm_model_1(sent_pairs, 10)

# Print the translation probabilities for each Turkish-English word pair
for (turkish_word, english_word), probability in t.items():
    if turkish_word in ["merhaba", "dünya", "bugün", "hava", "güzel", 
"ben", "bir", "kitap", "okuyorum", "seni", "seviyorum", "ne", 
"yapıyorsun"]:
        print(f"t({turkish_word}|{english_word}) = {probability:.4f}")
