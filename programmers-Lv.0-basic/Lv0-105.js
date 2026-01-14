/*
    문자열 배열 strArr이 주어집니다. 
    strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.
*/

/*
    [순서도 만들어보기]

    1. strArr에 담긴 문자열들을 길이 배열로 치환한다.
    2. 길이 배열을 돌면서 가장 많이 나온 수를 반환해야 한다. > '빈도'를 측정해야 함.
    3. 그럼 빈도 측정을 어떻게 할까? 배열을 한 번씩 순회하면서 각 숫자의 등장 횟수를 세야 한다.
    4. 그 중에서 가장 많이 나온 수를 찾아내서 반환하면 되는데,
    5. 우선 숫자와 빈도 수를 저장할 공간이 필요하다. 1: 2, 2:9 이런식으로 key:value 형태로 저장하면 좋을 거 같다. 이럼 어떤 숫자가 빈도를 얼마 가지고 있는지 알 수 있다.
    6. JS에서는 {} 객체나 map 객체로 key-value값을 저장한다.
    
    3. 가장 빈도가 높은 수를 return 한다.
 */

function solution(strArr) {
    
    // 처음부터 key: value 형태로 숫자: 빈도수를 만들어야 함.
    const dict = new Map();
    
    for (const str of strArr) {
        const len = str.length;
        dict.set(len, (dict.get(len) || 0) + 1);
    }
    
    const max = Math.max(...dict.values());
    
    return max
    
}