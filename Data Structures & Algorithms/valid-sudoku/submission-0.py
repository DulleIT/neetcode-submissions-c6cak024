class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)
        for r in range(9):
            besuchte = set()
            for c in range(9):
                wert = board[r][c]
                if wert == ".":
                    continue
                
                block_id = (r // 3), (c // 3)
                if (wert in rows[r] or 
                    wert in cols[c] or 
                    wert in blocks[block_id]):
                    return False
            
                rows[r].add(wert)
                cols[c].add(wert)
                blocks[block_id].add(wert)

        return True
                

