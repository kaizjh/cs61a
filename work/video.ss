;;; Non-empty subsets of integer list s that have an even sum
(define (even-subsets s)
    (if (null? s) '()
        (append (even-subsets (cdr s))
            (map (lambda (t) (cons (car s) t))
                (if (even? (car s))
                    (even-subsets (cdr s))
                    (odd-subsets (cdr s))))
            (if (even? (car s)) (list (list (car s))) '()))))

;;; Non-empty subsets of integer list s that have an odd sum
(define (odd-subsets s)
    (if (null? s) '()
        (append (odd-subsets (cdr s))
            (map (lambda (t) (cons (car s) t))
                (if (odd? (car s))
                    (even-subsets (cdr s))
                    (odd-subsets (cdr s))))
            (if (odd? (car s)) (list (list (car s))) '()))))

"""
;;; Alternative even or odd subsets
(define (even-subsets s)
    (if (null? s) '()
        (append (even-subsets (cdr s))
            (subset-helper even? s))))

(define (odd-subsets s)
    (if (null? s) '()
        (append (odd-subsets (cdr s))
            (subset-helper odd? s))))
            
(define (subset-helper f s)
    (append
        (map (lambda (t) (cons (car s) t))
            (if (f (car s))
                (even-subsets (cdr s))
                (odd-subsets (cdr s))))
        (if (f (car s)) (list (list (car s))) '())))
"""


; Another version of even-subset
; Nonempty-subsets function gets every combination of list s, which is not empty list
(define (nonempty-subsets s)
    (if (null? s) '()
        (let ((rest (nonempty-subsets (cdr s))))
            (append rest
                (map (lambda (t) (cons (car s) t)) rest)
                (list (list (car s))))
        )
    )
)

; Non-empty subsets of integer list s that have an even sum
(define (even-subsets2 s)
    (filter (lambda (s) (even? (apply + s))) (nonempty-subsets s)) ; (apply + s) means apply addition(+) to list s
)




(define-syntax check
    (syntax-rules ()
      ((_ expr)
       (if expr 'passed 'failed))))

(define-syntax check
    (syntax-rules ()
      ((_ expr)
       (list 'if expr ''passed ''failed))))

(define-syntax check
    (syntax-rules ()
      ((_ expr)
       (if expr 'passed 
                '(failed: expr)))))

(define x 2)


(define (map fn vals)
    (if (null? vals)
        '()
        (cons (fn (car vals))
              (map fn (cdr vals))
        )
    )
)

(define-syntax for
    (syntax-rules ()
        ((_ sym vals expr)
         (map (lambda (sym) expr) vals)
        )
    )
)
(define y (for x '(2 3 4 5) (* x x)))




(define fact (lambda (n)
    (if (zero? n) 1 (* n (fact (- n 1))))))

(define original fact)
(define fact (lambda (n)
             (display (list 'fact n))
             (original n)))


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