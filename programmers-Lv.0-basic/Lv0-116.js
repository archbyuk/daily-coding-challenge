/*
정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

단, arr에 2가 없는 경우 [-1]을 return 합니다.
*/

function solution(arr) {
    let idx = [];
    
    arr.forEach((v, i) => { if (v === 2) idx.push(i) })
    
    if (idx.length === 0 ) return [-1]
    
    const start = Math.min(...idx);
    const end = Math.max(...idx);
    
    return arr.slice(start, end + 1)
}

// forEach는 (값, 인덱스, 배열) 세 가지 인자를 받는다 순서를 반드시 지켜야 한다

function solution(arr) {
    let idx = [];
    
    idx = arr.map(
        (v, i) => v === 2 ? i : -1
    ).filter(i => i !== -1);
    
    return idx.length ? arr.slice(Math.min(...idx), Math.max(...idx) + 1) : [-1]
}

// map과 filter 조합으로 인덱스 뽑아내기

// 다른 사람 풀이 중 가장 인상깊었떤
function solution(arr) {
    const from = arr.indexOf(2);      // 첫 번째 2의 위치
    const end = arr.lastIndexOf(2);   // 마지막 2의 위치

    return from === -1 ? [-1] : arr.slice(from, end+1);
}