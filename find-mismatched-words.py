def mismatched_words(string1, string2):
   return [x for x in list(set(string1.strip().lower().split(' ')).symmetric_difference(set(string2.strip().lower().split(' ')))) if len(x) > 0]