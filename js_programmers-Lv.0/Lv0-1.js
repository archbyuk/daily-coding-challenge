function solution(n, slicer, num_list) {
    let answer = [];
    
    const [a, b, c] = [slicer[0], slicer[1], slicer[2]];
    // cons [a, b, c] = [...slicer] or slicer
    
    // if > switch문도 가능
    if (n === 1) {
        answer = num_list.slice(0, b + 1);
    }
    
    else if (n === 2) {
        answer = num_list.slice(a)   
    }
    
    else if (n === 3){
        answer = num_list.slice(a, b + 1)
    }
    
    else {
        for (let i = a; i <= b; i += c) {
            answer.push(num_list[i]);
        }
    }
        
    
    return answer;
}