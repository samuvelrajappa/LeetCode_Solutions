class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: the first sequence is always "1"
        current_seq = "1"
        
        # Iteratively build up to the nth sequence
        for _ in range(n - 1):
            next_seq = []
            i = 0
            # Scan through the current sequence to compute Run-Length Encoding (RLE)
            while i < len(current_seq):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(current_seq) and current_seq[i] == current_seq[i + 1]:
                    count += 1
                    i += 1
                
                # Append the count followed by the character itself
                next_seq.append(str(count))
                next_seq.append(current_seq[i])
                i += 1
            
            # Update the sequence for the next iteration
            current_seq = "".join(next_seq)
            
        return current_seq
