#setup
votes: list = []
invalid_voters: set = set()
s_uniq = set()
counter = 0
invalid_votes = 0

vote = None
print("to stop, press   -999   ")

#voting
while True:
    vote = int(input("please enter your id: "))
    if vote == -999:
        break
    if vote > 100 or vote < 0:
        vote = int(input("invalid number, please enter your id: "))
        counter += 1
        votes.append(vote)
        s_uniq.add(vote)
        continue
    else:
        votes.append(vote)
        s_uniq.add(vote)
    counter += 1


for vote in s_uniq:
    if votes.count(vote) > 1:
        invalid_votes += 1
        invalid_voters.add(vote)
        votes.remove(vote)


#printing
print (f'you got {counter} voters')
print(f"Those are your valid voters: {s_uniq} over all: {counter - invalid_votes}")
print(f'you have {invalid_votes} amount of invalid voters')
