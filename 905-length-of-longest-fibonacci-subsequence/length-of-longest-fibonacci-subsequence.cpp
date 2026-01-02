class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        unordered_set<int> numSet(arr.begin(), arr.end());
        int max_len = 0;
        for(int start = 0; start<arr.size(); start++){
            for(int next = start+1; next<arr.size(); next++){
                int prev = arr[next];
                int curr = arr[start] + arr[next];
                int curr_len = 2;
                while(numSet.find(curr) != numSet.end()){
                    int temp = curr;
                    curr = prev + curr;
                    prev = temp;
                    max_len = max(max_len, ++curr_len);
                }
        
            }
        }
    if (max_len>2){
        return max_len;}
    else{return 0;}
    }
};