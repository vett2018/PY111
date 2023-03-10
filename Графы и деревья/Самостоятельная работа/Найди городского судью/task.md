В городе есть люди, помеченные от 1 до n. Ходят слухи, что один из этих людей тайно является городским судьей.

Если городской судья существует, то:

* Городской судья никому не доверяет.
* Все (за исключением городского судьи) доверяют городскому судье.

Существует ровно один человек, который удовлетворяет свойствам 1 и 2.

Вам дается массив `trust`, где trust[i] = [ai, bi], представляющий, что человек с пометкой ai доверяет человеку с пометкой bi. 
Если доверительная связь не существует в массиве trust, то такая доверительная связь не существует.

Верните метку городского судьи, если городской судья существует и может быть идентифицирован, или верните -1 в противном случае.

Пример 1:

Input: n = 2, trust = [[1,2]]

Output: 2

Пример 2:

Input: n = 3, trust = [[1,3],[2,3]]

Output: 3

Пример 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]

Output: -1

[leetcode](https://leetcode.com/problems/find-the-town-judge/)