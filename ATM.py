WithdrawAmt,InitialBalence = input().split()
InitialBalence = float(InitialBalence)
WithdrawAmt = int(WithdrawAmt)

if WithdrawAmt % 5 == 0 and WithdrawAmt < (InitialBalence - 0.50):
    InitialBalence = InitialBalence - (WithdrawAmt + 0.50)
print("%0.2f"%InitialBalence)
