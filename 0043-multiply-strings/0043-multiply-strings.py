class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Array to hold the product digits
        res = [0] * (len(num1) + len(num2))
        
        # Multiply from right to left
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Calculate the product of two single digits
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Determine positions in the result array
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]
                
                # Update positions with values and carries
                res[p2] = total % 10
                res[p1] += total // 10
                
        # Skip any leading zeros
        ans = []
        for digit in res:
            if not (len(ans) == 0 and digit == 0):
                ans.append(str(digit))
                
        return "".join(ans)
