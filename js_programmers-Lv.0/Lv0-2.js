function solution(ineq, eq, n, m) {
    
    const lambdafunc = {
        '>=': (n, m) => n >= m,
        '<=': (n, m) => n <= m,
        '>!': (n, m) => n > m,
        '<!': (n, m) => n < m
    };
    
    const func_key = ineq + eq;
    return +lambdafunc[func_key](n, m);
}

// 자바스크립트에서 +true는 1로 +false는 0으로 자동 변환

/*
    파이썬은 bool이 int의 하위형이어서 자동으로 True → 1, False → 0이 된다.
    하지만 JavaScript의 true, false는 boolean 타입이고,
    
    그 자체로는 숫자형이 아니다.
*/

function solution_2(ineq, eq, n, m) {

    const func_key = ineq + eq;
    let result = false;

    switch (func_key) {
        case '>=':
            result = n >= m;
            break;
        case '<=':
            result = n <= m;
            break;
        case '>!':
            result = n > m;
            break;
        case '<!':
            result = n < m;
            break;
    }

    return +result; // or result ? 1 : 0;
}

/* TYPESCRIPT */

/*
    function solution(ineq: string, eq: string, n: number, m: number): number {
        
        const lambdafunc = {
            '>=': (n: number, m: number) => n >= m,
            '<=': (n: number, m: number) => n <= m,
            '>!': (n: number, m: number) => n > m,
            '<!': (n: number, m: number) => n < m
        };
        
        const func_key = ineq + eq;
        return +lambdafunc[func_key](n, m);
}
*/