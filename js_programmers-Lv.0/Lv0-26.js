/**
 * 양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
 */

/**
[ (0, 0), (0, 1), (0, 2), (0, 3), (0, 4) ],
[ (1, 0), (1, 1), (1, 2), (1, 3), (1, 4) ],
[ (2, 0), (2, 1), (2, 2), (2, 3), (2, 4) ],
[ (3, 0), (3, 1), (3, 2), (3, 3), (3, 4) ],
[ (4, 0), (4, 1), (4, 2), (4, 3), (4, 4) ]
*/
function solution(n) {
    
    // 초기 n * n 배열
    const init_Arr = Array.from( {length: n}, () => new Array(n).fill(0));
    console.log(init_Arr)
    
    // 초기 좌표
    let x = 0;
    let y = 0;
    
    // (0, 1): 오른쪽 || (1, 0): 아래 || (0, -1): 왼쪽 || (-1, 0): 위쪽
    const direction = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    
    // 초기 방향 인덱스
    let dir_idx = 0
    
    for (let i = 1; i <= n * n; i++) {
        
        // 현재 좌표에 숫자 넣기
        init_Arr[x][y] = i;
        
        // 구조 분해 할당
        let [dx, dy] = direction[dir_idx]
        
        // 현재 좌표에 방향 수식 덧셈
        let pre_x = x + dx
        let pre_y = y + dy
        
        // 1. pre_x = 4 >= n
        // 2. pre_y = 4 >= n
        // 3. pre_x = 0 >= n
        // 4. init_Arr[pre_x][pre_y] !== 0
        // 5. init_Arr[pre_x][pre_y] !== 0
        // 6. init_Arr[pre_x][pre_y] !== 0
        if (pre_x < 0 || pre_x >= n || pre_y < 0 || pre_y >= n || init_Arr[pre_x][pre_y] !== 0) {
            
            // + 1을 하는 이유는 방향이 전환됨에 따라 방향 배열의 인덱스가 변경되어야 하기 때문.
            // 1. 현재 0일 때: 0 + 1이후, 1/4의 나머지는 1
            // 2. 현재 1일 때: 1 + 1이후, 2/4의 나머지는 2
            // 3. 현재 2일 때: 2 + 1이후, 3/4의 나머지는 3
            // 4. 현재 3일 때: 3 + 1이후, 4/4의 나머지는 4
            dir_idx = (dir_idx + 1) % 4;
            
            [dx, dy] = direction[dir_idx];
        }
        
        x += dx;
        y += dy;
    }
    
    return init_Arr
}

// 게임이 이렇게 만들어 지는구나...