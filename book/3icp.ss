(define (abs x)
    (if (< x 0)
        (- x)
        x))
;(display (abs -3))

(define (square x) (* x x))
;(display (square -3))

(define (average a b)
  (/ (+ a b) 2))

(define (sqrt x)
    (define (update guess)
      (define (good-enough? guess)
        (< (abs (- (square guess) x)) 0.001))
      (if (good-enough? guess)
          (exact->inexact guess)  ; Convert to float when returning the result
          (update (average guess (/ x guess)))))
    (update 1))

(define (size x)
    (cond ((> x 10) (display 'big))
          ((> x 5) (display 'medium))
          (else    (display 'small))))

(define c (let ((a 3)
                (b ( + 2 2)))
                (sqrt (+ (* a a) (* b b)))))


(define (length items)
  (if (null? items)
    0
    (+ 1 (length (cdr items)))))
  
(define (getitem items n)
  (if (= n 0)
    (car items)
    (getitem (cdr items) (- n 1))))

(define squares (list 1 4 9 16 25))




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