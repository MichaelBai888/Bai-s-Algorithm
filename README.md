By excluding integers ending in 0, 2, 4, 6, 8, and 5 from the set of potential factors, the algorithm reduces the search space to integers ending in 1, 3, 7, or 9. This fundamental optimization rests on the premise that any integer ending in the excluded digits must contain prime factors of 2 or 5, an established mathematical certainty. 

The cornerstone of the proposed method is the exploitation of number-ending characteristics. A number's final digit dramatically influences its divisibility properties. For example, any integer ending in an even number is divisible by 2, and any ending in 5 is divisible by 5. Recognizing these patterns, one can effectively filter out a significant proportion of non-prime candidates when factoring a given integer. 
The algorithm, therefore, focuses solely on integers ending with 1, 3, 7, and 9, which represent potential prime factors that are not immediately obvious. Further analysis illuminates a discernible pattern concerning these digits. When two such integers are multiplied, the product will retain an ending digit within this set. 
For instance, any two numbers ending in 1, when multiplied, will yield a product ending in 1. This property holds true across all combinations within the set, producing a product ending in 1, 3, 7, or 9. Further analysis reveals a pattern: the product of two integers, each ending in 1, 3, 7, or 9, will result in an integer also terminating with one of these digits. 
For example, a public key ending in 1 can only be the product of two such integers (e.g., 11×11=121, 3×7=21, 9×9=81), regardless of the number of preceding digits. This principle holds true for integers ending in 3, 7, and 9, with potential factor combinations also ending in these digits.
This insight suggests a refined factorization algorithm that iterates only through integers ending in 1, 3, 7, and 9, thereby potentially increasing computational efficiency by an order of magnitude compared to traditional algorithms that test all integers up to the square root of the target number.

Building upon the foundational knowledge of number-ending characteristics, the algorithm is meticulously designed to exploit these patterns. It selectively iterates through integers ending in 1, 3, 7, or 9, thereby potentially expediting the factorization process by avoiding numbers that are categorically composite due to their terminal digits. This approach introduces efficiency by reducing the search space to only 40% of the integers below the square root of the target number, assuming a uniform distribution of terminal digits.
The algorithm's workflow is as follows:
•	Initially, it excludes all numbers ending in 0, 2, 4, 6, 8, and 5.
•	It then creates a sequence of candidate factors that terminate with 1, 3, 7, or 9, starting from the lowest primes.
•	The algorithm employs a modulo operation to test for divisibility among these candidates, leveraging computational shortcuts where applicable.
•	Concurrently, the digit sum analysis is invoked to swiftly eliminate candidates divisible by 3, which constitutes roughly one-third of the remaining numbers, further narrowing the search field.
This method does not simply offer a linear improvement but can be viewed as geometric progression in terms of efficiency. The digit sum rule serves as an overlay to the number-ending characteristics, providing an additional filter for the candidate factors. If the sum of the digits of the integer is divisible by 3, the algorithm bypasses the divisibility check for 3, streamlining the process.

