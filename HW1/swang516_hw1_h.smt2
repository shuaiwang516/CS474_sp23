; Author: Shuai Wang
; NID: swang516

; Lines beginning with semicolons are comments.
; Fix colors 0, 1, 2
; The following line declares a propositional atom
; representing whether node 0 has the color 0

(declare-const p00 Bool)
(declare-const p01 Bool)
(declare-const p02 Bool)
(declare-const p10 Bool)
(declare-const p11 Bool)
(declare-const p12 Bool)
(declare-const p20 Bool)
(declare-const p21 Bool)
(declare-const p22 Bool)
(declare-const p30 Bool)
(declare-const p31 Bool)
(declare-const p32 Bool)
(declare-const p40 Bool)
(declare-const p41 Bool)
(declare-const p42 Bool)

; At least one color per node
(assert (or p00 p01 p02))
(assert (or p10 p11 p12))
(assert (or p20 p21 p22))
(assert (or p30 p31 p32))
(assert (or p40 p41 p42))

; At most one color per node
(assert (not (and p00 p01)))
(assert (not (and p00 p02)))
(assert (not (and p01 p02)))
(assert (not (and p10 p11)))
(assert (not (and p10 p12)))
(assert (not (and p11 p12)))
(assert (not (and p20 p21)))
(assert (not (and p20 p22)))
(assert (not (and p21 p22)))
(assert (not (and p30 p31)))
(assert (not (and p30 p32)))
(assert (not (and p31 p32)))
(assert (not (and p40 p41)))
(assert (not (and p40 p42)))
(assert (not (and p41 p42)))

; Nodes connected by an edge have different colors
(assert (not (and p00 p10)))
(assert (not (and p00 p20)))
(assert (not (and p01 p11)))
(assert (not (and p01 p21)))
(assert (not (and p02 p12)))
(assert (not (and p02 p22)))
(assert (not (and p10 p20)))
(assert (not (and p10 p30)))
(assert (not (and p10 p40)))
(assert (not (and p11 p21)))
(assert (not (and p11 p31)))
(assert (not (and p11 p41)))
(assert (not (and p12 p32)))
(assert (not (and p12 p42)))
(assert (not (and p20 p30)))
(assert (not (and p20 p40)))
(assert (not (and p21 p31)))
(assert (not (and p21 p41)))
(assert (not (and p22 p32)))
(assert (not (and p22 p42)))
(assert (not (and p30 p40)))
(assert (not (and p31 p41)))
(assert (not (and p32 p42)))

(check-sat)