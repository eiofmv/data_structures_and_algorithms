#include <iostream>
#include <vector>

using namespace std;

long long MaxPairwiseProduct(const vector<int>& v) {
	int max1 = -1, max2 = -1;
	for (const auto& i : v) {
		if (i > max1) {
			max2 = max1;
			max1 = i;
		}
		else if (i > max2) {
			max2 = i;
		}
	}
	return (long long)max1 * (long long)max2;
}

int main() {
	int n;
	cin >> n;
	vector<int> v(n);
	for (auto& i : v) {
		cin >> i;
	}
	cout << MaxPairwiseProduct(v) << endl;
	return 0;
}
