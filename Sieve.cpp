const int N = 10000000;
vector<int> lp(N+1);
vector<int> pr;
void sieve(int N){ // compute prime factors till N in O(N) 
    for (int i=2; i <= N; ++i) {
        if (lp[i] == 0) {
            lp[i] = i;
            pr.push_back(i);
        }
        for (int j = 0; i * pr[j] <= N; ++j) {
            lp[i * pr[j]] = pr[j];
            if (pr[j] == lp[i]) break;
        }
    }
}
vector<int> getFactorization(int x){ // gives prime factors of x in O(log(x)) by pre computing sieve
    vector<int> ret;
    while (x != 1){
        ret.push_back(lp[x]);
        x = x / lp[x];
    }
    return ret;
}
