## DIFFICULTY:

Medium-hard

## PREREQUISITES:

Binary search, Data structures, Two pointer.

## PROBLEM STATEMENT:

An array $c$ is a subarray of an array $b$ if $c$ can be obtained from $b$ by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

Let's call a nonempty array good if for every nonempty subarray of this array, sum of the elements of this subarray is nonzero. For example, array $[−1,2,−3]$ is good, as all arrays $[−1], [−1,2], [−1,2,−3], [2], [2,−3], [−3]$ have nonzero sums of elements. However, array $[−1,2,−1,−3]$ isn't good, as his subarray $[−1,2,−1]$ has sum of elements equal to $0$.

Calculate the number of nonempty good subarrays of a given array $a$.

## EXPLANATION

If the subarray $[a_{i},...,a_{j}]$ is good, then the subarray $[a_{i},...,a_{j−1}]$ is also good, and if the subset $[a_{i},...,a_{j}]$ is not good, then the subarray $[a_{i},...,a_{j+1}]$ is not good either. Then for each left border $a_{i}$ we want to find the rightmost border $a_{j}$ such that $[ai,...,aj]$ is good and add to the answer $j−i+1$ (subarrays $[ai,...,aj],$ $[ai,...,aj−1],...,[ai]$) $[1]$. Let's denote the rightmost border $j$ for border $i$ as $R(i)$.

Let's calculate the prefix-sum of the array $P$.

$P_{0}=0,$ $P_{i}=a_{1}+..+a_{i},$ $ 1≤i≤n.$

Note that a subset of $[a_{i},...,a_{j}]$ has a zero sum if $P_{i−1}=P_{j}$. Then the subset $[a_{i},...,a_{j}$] is a good if sum of prefixes $[P_{i}−1,...,P_{j}]$ has no duplicates $[2]$.

Using $[1]$ and $[2]$, we can simply iterate over $i$ from $0$ to $n$ and over $j$ from $ i$ to $n$ and count the set of prefix sums $[P_{i},...,P_{j}]$. The first moment $j_{0}$ when this set contains duplicates gives us the rightmost border $j_{0}−1$, and we add $(j_{0}−1)−i$ (no $+1$, because it is an array of prefix sums) to answer.

To improve this solution to $O(n×log(n))$, we need to note that $R(i)$ is monotonous over $i$. Now we can iterate over $i$ from $0$ to $n$ and over $j$ from $R(i−1)$ to $n$ uses a set of prefix sums from the previous iteration. Thus we have a solution $O(n×log(n))$, because $j$ points to each element of the array exactly once.

**C++ Code (solution)**

    #include <bits/stdc++.h>
    using namespace std;

    int main() {
        int t;
        cin >> t;
        while(t--){
            int n;
            cin >> n;
            vector<long long> prefix(n + 1, 0);
            for (int i = 0; i < n; ++i) {
                int x;
                cin >> x;
                prefix[i + 1] = prefix[i] + x;
            }
            int begin = 0, end = 0;
            long long ans = 0;
            set<long long> s = {0};
            while(begin < n) {
                while(end < n && !s.count(prefix[end + 1])) {
                    ++end;
                    s.insert(prefix[end]);
                }
                ans += end - begin;
                s.erase(prefix[begin]);
                ++begin;
            }
            cout << ans << endl;
        }
    }

## TIME COMPLEXITY:

$O(n×log(n))$
