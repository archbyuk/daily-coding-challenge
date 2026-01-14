/*
문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. 
str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
"l"이나 "r"이 없다면 빈 리스트를 return합니다.
*/

function solution(str_list) {
    const l_first = str_list.indexOf('l');
    const r_first = str_list.indexOf('r')
    
    if (l_first === -1 || r_first === -1) return []
    
    const result = [];
    
    if (l_first > r_first) {
        return str_list.slice(r_first)
    } 
    
    else if (l_first < r_first) {
        return str_list.slice(0, l_first)
    }
}

// '이나'면 OR이 맞는 거 같은데, 왜 AND로 해야 통과되는지 모르겠네..
function solution(str_list) {
    const l_first = str_list.indexOf('l');
    const r_first = str_list.indexOf('r');

    // 둘 다 없으면 []: '이나'인데 왜 OR가 아니고 AND임? 내가 빡데가리라 이해를 못하는 건가?
    if (l_first === -1 && r_first === -1) return [];

    // r이 먼저 나옴
    if (r_first !== -1 && (l_first === -1 || r_first < l_first)) {
        return str_list.slice(r_first + 1);
    }

    // l이 먼저 나옴
    if (l_first !== -1 && (r_first === -1 || l_first < r_first)) {
        return str_list.slice(0, l_first);
    }

    return [];
}