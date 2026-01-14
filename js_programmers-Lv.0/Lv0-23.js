/**
    이차원 정수 배열 arr이 매개변수로 주어집니다. 
    arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
 */

function solution(arr) {
    const col = arr.length
    const row = arr[0].length
    
    let condition = { type: '', gap: 0 };
    
    col > row
        ? condition = { type: 'col', gap: col - row }
        : row > col
            ? condition = { type: 'row', gap: row - col }
            : condition = { type: 'equal', gap: 0 }
 
    if (condition.type === 'col') {
        arr.forEach((a) => {
            a.push(...new Array(condition.gap).fill(0))
        })
    }
    
    else if (condition.type === 'row') {
        const newRow = Array.from( {length: condition.gap}, () => new Array(row).fill(0))
        
        arr.push(...newRow)
    }
    
    return arr
}