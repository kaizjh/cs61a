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