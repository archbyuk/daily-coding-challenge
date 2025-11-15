/*
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.

각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.

위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.
*/
function solution(arr, queries) {

    for (const [i, j] of queries) {
        [ arr[i], arr[j] ] = [arr[j], arr[i] ]
    }
    
    return arr
}

// for of문으로 2차원 배열을 구조분해할당 해주고,
// arr[i], arr[j]의 값을 서로 바꿔서 배치시는 것또한 구조 분해 할당으로 깔끔하게 해봄.