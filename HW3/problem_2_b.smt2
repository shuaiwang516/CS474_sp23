(declare-const l1 Real)
(declare-const u1 Real)
(declare-const l2 Real)
(declare-const u2 Real)
(declare-const l3 Real)
(declare-const u3 Real)
(declare-const l4 Real)
(declare-const u4 Real)

(define-fun intersect ((la Real) (ua Real) (lb Real) (ub Real)) Bool
    (exists ((z Real)) 
    (and 
        (< la z) (< z ua) (< lb z) (< z ub))))

(define-fun alphaG () Bool
    (and 
        (< l1 u1) (< l2 u2) (< l3 u3) (< l4 u4)
        (intersect l1 u1 l2 u2) (intersect l1 u1 l4 u4)
        (intersect l2 u2 l3 u3) (intersect l3 u3 l4 u4)))
        (not (intersect l2 u2 l4 u4)) (not (intersect l1 u1 l3 u3))

(assert alphaG)
(check-sat)