#include <bits/stdc++.h>
using namespace std;

class DisjointSet {
 private:
  vector<long long> parent;
  vector<long long> size;

 public:
  DisjointSet(long long n) {
    parent.resize(n + 1);
    size.resize(n + 1);
    for (int i = 0; i <= n; i++) parent[i] = i;
    for (int i = 0; i <= n; i++) size[i] = 1;
  }
  long long find(long long v) {
    if (v == parent[v]) return v;
    return parent[v] = find(parent[v]);
  }
  void uni(long long a, long long b) {
    a = find(a);
    b = find(b);
    if (a != b) {
      if (size[a] < size[b]) {
        swap(a, b);
      }
      parent[b] = a;
      size[a] += size[b];
    }
  }
};