+++
title = "Blog post"
author = ["daniel"]
draft = false
+++

## Introduction {#introduction}

In my experience, scientific programming typically falls into one of three camps.
The first camp consists of quick one-off scripts -- usually written in less than a day -- that are used a handful of times and quickly discarded.
For example, a scientist may write a quick analysis script to examine means in several different conditions of their data, realize the analysis is not fruitful, and discard the script.

In the second camp, one finds code with a slightly longer development history (several days to several weeks) and slightly more life to live (perhaps used in the context of a single paper and somewhat intended for consumption).
Code that underlies a single project or paper may live in this camp.
For example, a scientist may write a set of plotting scripts that generate the figures for a single paper.
This sort of code is probably developed over several weeks to several months, is intensely used for a short period of time, and then rarely reused or reviewed once the paper is published.

Finally, in the third camp, the necessary glue that holds modern science together is found.
That is, we find bodies of code that are used for long periods of time, used by one or more groups, and supported or actively devleoped for long periods of time.
Large open-source projects that support modern scientific programming are found here, as are smaller toolboxes or packages that link several research groups or small fields.


## Unit tests {#unit-tests}

Unit testing has a lot to offer when it comes to assisting in the design of software for scientific uses, particulary those that fall into the first two camps!
Unit testing is a common part of modern software design but is rarely practiced in scientific programming.

Test-driven development.

However, can be a little tricky to initially get into.

Basic ideas

Let's say we write a function to determine if a number is prime.

```python
def is_prime(num):
    flag = False
    for divisor in range(2, num):
      if (num % divisor) == 0:
	  flag = True
	  break
    return not flag
```

It is easy enough to work through this code in your head and observe that this code will successfully discriminate between prime numbers and non-prime numbers.
However, suppose we want to make this code faster, or add additional features.
Normally, this would entail making changes to the code and then manually testing the new code to make sure it works the same as before.
Such a manual testing process is a major failure point in software development.
I suspect that any scientific programmer has had the experience of making seeminlgy innocent changes to their code only to find out, perhaps several weeks or months later, that the changes had unintended consequences or introduced new bugs.

To take the human factor out of the equation, we can develop a set of automated unit tests for this code.
A unit test is simple --- just a short chunk of code that runs our \`is\_prime\` function and verifies that it satisifes some test.
For example, one key test for an prime-checking function would be to make sure that it correclty reports prime numbers as primes and non-prime numbesr as non-primes.

```python
def test_is_prime_small_numbers():
    primes = [1, 2, 3, 5, 7, 11, 13]
    non_primes = [2, 4, 6, 8, 9, 10, 12]
    for prime in primes:
      assert is_prime(prime)
    for non_prime in non_primes:
	assert not is_prime(prime)
```

Here is an example of a short unit test that tests whether \`is\_prime\` correctly handles integers less than or equal to 13.
Your initial reaction may be one of surprise --- the testing code is as long as the code itself!
Line counts don't matter...
Increasingly useful...


## Test-driven development {#test-driven-development}


## Closing remarks {#closing-remarks}