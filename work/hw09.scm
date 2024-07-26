(define (curry-cook formals body)
    (if (null? formals)
        body
        `(lambda (,(car formals)) ,(curry-cook (cdr formals) body))
    ))

(define-macro (trace expr) ; (trace (fact 5))
    (define operator (car expr)) ; fact
    `(begin
        (define original ,operator)
        (define ,operator (lambda (n)
                            (print (list ',operator n))
                            (original n)))
        (define result ,expr)
        (define ,operator original)
        result
    )
)

(define fact (lambda (n)
                (if (zero? n) 1 (* n (fact (- n 1))))))

(fact 5)
(trace (fact 5))
(fact 5)