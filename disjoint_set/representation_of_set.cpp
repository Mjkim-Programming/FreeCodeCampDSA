#include <bits/stdc++.h>
#define FASTIO      \
  cin.tie(nullptr); \
  ios::sync_with_stdio(false)
#define END return 0
using namespace std;

// Solving BOJ 1717 집합의 표현

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

int main() {
  FASTIO;
  long long n, m;
  cin >> n >> m;
  DisjointSet set(n);
  while (m--) {
    int q;
    long long a, b;
    cin >> q >> a >> b;
    if (q == 0) {
      set.uni(a, b);
    } else if (q == 1) {
      if (set.find(a) == set.find(b))
        cout << "YES\n";
      else
        cout << "NO\n";
    }
  }
  END;
}