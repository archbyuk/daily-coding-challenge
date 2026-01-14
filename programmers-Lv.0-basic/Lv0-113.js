function solution(arr) {
    const stk = [];
    let i = 0;
    
    while(i < arr.length) {
        
        if (stk.length < 1) {
            stk.push(arr[i]);
        }
        
        else {
            stk.at(-1) === arr[i] 
                ? stk.pop() 
                : stk.push(arr[i]);
        }
        
        i++;
    }
    
    return stk.length < 1 ? [-1] : stk
}