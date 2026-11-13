class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i, j = 0, n-1
        cnt = 0
        while i <= j:
           rem = limit - people[j]
           j -= 1
           cnt += 1
           if i <= j and rem >= people[i]:
            i += 1
        return cnt
                