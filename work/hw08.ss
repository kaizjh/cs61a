(define (ascending? s)
    'YOUR-CODE-HERE
    (if (or (null? s) (null? (cdr s)))
        #t
        (if (> (car s) (car (cdr s)))
            #f
            (ascending? (cdr s))
        )    
    )
)


(define (my-filter pred s)
    'YOUR-CODE-HERE
    (if (null? s)
        s
        (if (pred (car s))
            (cons (car s) (my-filter pred (cdr s)))
            (my-filter pred (cdr s))
        )
    )
)

(define (pred x)
    (if (= x 1)
        #t
        #f
    )
)

(define s (list 1 2 1 3 4))