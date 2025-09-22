#71. Simplify Path

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        curr = ""
        
        for p in path + "/":
            if p == "/":
                if curr == "..":
                    if stack: stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += p
        return "/" + "/".join(stack)

if __name__ == "__main__":
    sol = Solution()
    path = "/home//foo/"
    print("Output is : ", sol.simplifyPath(path))
    
    path2 = "/.../a/../b/c/../d/./"
    print("Output is : ", sol.simplifyPath(path2))
