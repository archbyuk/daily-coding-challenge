/*
정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.

각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.
*/
function solution(arr, queries) {

    const final = [];       // 최종적으로 각 반복에서 뽑아낸 최소 arr[i]를 담는 배열

    for (const [s, e, k] of queries) {
        const middle = [];      // 중간에 k보다 큰 i들에 대한 arr[i]를 담는 배열

        for (let i = e; s <= i; i--) {   
            // k보다 큰 arr[i]이 있을 때,
            if (arr[i] > k) {
                middle.push(arr[i])
            }
        }

        if (middle.length === 0) {
            final.push(-1)
        }
        else {
            final.push(Math.min(...middle));   
        }
    }

    return final
}

// 문제는 맞췄는데
/*

    •	문제는 단순히 “범위 내의 값들을 검사”하는 것이 목적
	•	i가 어디서부터 시작하든(정방향/역방향), 반복 범위가 올바르면 결과는 같아야 함
	•	그런데 현재 코드의 반복 범위 조건이 s ≤ i ≤ e를 만족하지 않음

라는...
*/

// map 사용하기

function solution2 (arr, queries) {

    return queries.map(
        ([s, e, k]) => 
            arr.slice(s, e + 1)
                .filter( (slice_element) => slice_element > k)
                    .sort( (x, y) => x - y )[0] || -1
    )
}