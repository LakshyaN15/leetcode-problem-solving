# Problem - https://leetcode.com/problems/rank-scores/
# Approach - 
# Topic - Database
# Difficulty - Medium
SELECT S.score ,COUNT(S2.SCORE) as `rank` FROM SCORES S,
(SELECT DISTINCT SCORE FROM SCORES)  S2
WHERE S.SCORE<=S2.SCORE 
GROUP BY S.ID 
ORDER BY S.SCORE DESC;