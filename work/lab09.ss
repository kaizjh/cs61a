(define (over-or-under num1 num2)
    (if (< num1 num2) -1
        (if (= num1 num2) 0 1)))

(define (over-or-under2 n1 n2)
    (cond
        ((< n1 n2) -1)
        ((= n1 n2) 0)
        (else 1)))


(define (make-adder num)
    (define (add inc)
        (+ num inc))
    add)

(define (make-adder2 num)
    (lambda (inc) (+ inc num)))


(define (square x) (* x x))

(define (composed f g)
    (lambda (x) (f (g x))))

; Using recursion
(define (repeat f n)
  (if (< n 1)
    (lambda (x) x)  ; Base case
    (composed f (repeat f (- n 1)))))


(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))

(define (gcd a b)
    ;YOUR-CODE-HERE
    (define ma (max a b))
    (define mi (min a b))
  
    (define (helper d ma mi)
        (if (and (zero? (modulo mi d)) (zero? (modulo ma d))) 
            d 
            (helper (- d 1) ma mi))
    )
    (helper mi ma mi)
)
