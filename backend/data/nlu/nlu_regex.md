## regex:date slash
- [0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}

## regex:date point
- [0-3]?[0-9]\.[0-3]?[0-9]\.(?:[0-9]{2})?[0-9]{2}

## regex:date dash
- [0-3]?[0-9]-[0-3]?[0-9]-(?:[0-9]{2})?[0-9]{2}

## regex:time 24h
- ([0-1]?[0-9]|[2][0-3]):([0-5][0-9])

## regex:time am/pm
- (1[0-2]|[1-9]):[0-5][0-9]\s?(a|p|A|P)(m|M)

## regex:date MMM dd, yyyy
- (?:(((Jan(uary)?|Ma(r(ch)?|y)|Jul(y)?|Aug(ust)?|Oct(ober)?|Dec(ember)?)\ 31)|((Jan(uary)?|Ma(r(ch)?|y)|Apr(il)?|Ju((ly?)|(ne?))|Aug(ust)?|Oct(ober)?|(Sept|Nov|Dec)(ember)?)\ (0?[1-9]|([12]\d)|30))|(Feb(ruary)?\ (0?[1-9]|1\d|2[0-8]|(29(?=,\ ((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00)))))))\,\ ((1[6-9]|[2-9]\d)\d{2}))

## regex:date dd MMM yyyy
- ((31(?!\ (Feb(ruary)?|Apr(il)?|June?|(Sep(?=\b|t)t?|Nov)(ember)?)))|((30|29)(?!\ Feb(ruary)?))|(29(?=\ Feb(ruary)?\ (((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00)))))|(0?[1-9])|1\d|2[0-8])\ (Jan(uary)?|Feb(ruary)?|Ma(r(ch)?|y)|Apr(il)?|Ju((ly?)|(ne?))|Aug(ust)?|Oct(ober)?|(Sep(?=\b|t)t?|Nov|Dec)(ember)?)\ ((1[6-9]|[2-9]\d)\d{2})

## regex:nr of people 10 - 599
- [^\D]?[1-9]{1}[0-9]{1,3}[^\D]?\b|people|persons|employees|guests

## regex:budget 600 - 99999
- (\$|€|GBP|CAN\$|£|CHF|USD|US\$|Fr\.|^\D)?([6-9]\d\d|[1-9]['|,]?\d{3,4})([^\D]|Fr\.?|)?