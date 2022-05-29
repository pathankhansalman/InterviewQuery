def replace_words(roots, sentence):
  sorted_roots = list(sorted(roots, key=lambda x: len(x)))
  words = sentence.strip().split(' ')
  stemmed_words = []
  for word in words:
    root_found = False
    for root in sorted_roots:
      if word.startswith(root):
        stemmed_words.append(root)
        root_found = True
        break
    if not root_found:
      stemmed_words.append(word)
  print(stemmed_words)
  return ' '.join(stemmed_words)