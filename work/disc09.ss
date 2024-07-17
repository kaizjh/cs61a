(define (square x) (* x x))
;(display (square -3))

(define (average a b)
  (/ (+ a b) 2))

(define (sqrt x)
    (define (update guess)
      (define (good-enough? guess)
        (< (abs (- (square guess) x)) 0.001))
      (if (good-enough? guess)
          (round guess)  ; Convert to float when returning the result
          (update (average guess (/ x guess)))))
    (update 1))


;;; Return whether there are n perfect squares with no repeats that sum to total
(define (fit total n)
    (define (f total n k)
        (cond
            ((and (= n 0) (= total 0)) #t)
            ((< total (* k k)) #f)
            (else (or (f total n (+ k 1)) (f (- total (* k k)) (- n 1) (+ k 1)))))
    )
    (f total n 1)
    )
   
"""
(expect (fit 10 2) #t)  ; 1*1 + 3*3
(expect (fit 9 1)  #t)  ; 3*3
(expect (fit 9 2)  #f)  ;
(expect (fit 9 3)  #f)  ; 1*1 + 2*2 + 2*2 doesn't count because of repeated 2*2
(expect (fit 25 1)  #t) ; 5*5
(expect (fit 25 2)  #t) ; 3*3 + 4*4
"""


(define li
    (list (list 'a 'b) 'c 'd (list 'e))
)

(define qu
    (quote ((a b) c d (e)))
)

; Actually, (cons . .) is used for creating a pair, so it takes only two prameters a time
; So, it is not a good idea to use (cons) to create a list
(define co
    (cons (cons 'a (cons 'b '())) (cons'c (cons 'd (cons (cons 'e '()) '()))))
)




;;; scm> (pair-up '(3 4 5 6 7 8))
;;; ((3 4) (5 6) (7 8))
;;; scm> (pair-up '(3 4 5 6 7 8 9))
;;; ((3 4) (5 6) (7 8 9))
(define (pair-up s)
    (if (<= (length s) 3)
        (list s)
        (list (list (car s) (car (cdr s))) (pair-up (cdr (cdr s))))
    )
)

