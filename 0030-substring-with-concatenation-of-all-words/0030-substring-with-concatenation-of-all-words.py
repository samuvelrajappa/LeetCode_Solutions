from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        # Count frequency of each word required
        word_counts = Counter(words)
        result = []
        
        # Iterate over all possible remainder alignments up to word_len
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            count = 0
            
            # Slide window across s in steps of word_len
            while right + word_len <= s_len:
                # Extract the next word segment
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_counts:
                    current_counts[word] += 1
                    count += 1
                    
                    # If word frequency exceeds what's required, shrink window from left
                    while current_counts[word] > word_counts[word]:
                        left_word = s[left:left + word_len]
                        current_counts[left_word] -= 1
                        count -= 1
                        left += word_len
                        
                    # If window matches total words required, add to results
                    if count == num_words:
                        result.append(left)
                else:
                    # Reset window if an unknown word is encountered
                    current_counts.clear()
                    count = 0
                    left = right
                    
        return result
