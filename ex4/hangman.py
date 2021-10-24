from hangman_helper import *

def update_word_pattern(word,pattern,letter):
    pattern = list(pattern)
    for i in range(len(word)):
        if letter == word[i]:
            pattern[i] = letter
    patternToStr = ''.join([str(p) for p in pattern])
    return patternToStr

#print(update_word_pattern("worddd","______","d"))

# word = hangman_helper.get_random_word(["i","love","you"])




def run_single_game (words_list,score):
    word = str(get_random_word(words_list))
    #print(word)
    #print(len(word))
    pattern= "_" * len(word)
    wrong_guess_lst = []
    msg= "wellcome to The game"

    while score > 0 and pattern != word:
        display_state(pattern, wrong_guess_lst, int(score), msg)
        user_answer =  get_input()
        user_input = user_answer[1]
        score -= 1
        if user_answer[0] == LETTER:
            if not user_input.islower() or len(user_answer[1]) != 1:
                msg = "the letter you entered is invalid"
                score += 1
            elif user_input in wrong_guess_lst or user_input in pattern :
                msg= "The letter you entered was already chosen"
                score += 1
            else:
                msg = "good for u! try one more guess"
                if user_input in word and not user_input in pattern:
                    times_in_word = word.count(user_input)
                    score += times_in_word * (times_in_word+1)/2
                    pattern = update_word_pattern(word, pattern, user_input)
                else:
                    wrong_guess_lst.append(user_input)
        elif user_answer[0] == WORD:
            msg = "good for u! try one more guess"
            if user_input == word: 
                times_in_word = pattern.count("_")
                score += times_in_word * (times_in_word + 1) / 2
                pattern = word
        elif user_answer[0] == HINT:
            msg = "good for u! try one more guess"
            a = filter_word_list(words_list, pattern, wrong_guess_lst)
            b = find_hint(a)
            show_suggestions(b)
    if pattern == word:
        msg = "you win!"
        display_state(pattern, wrong_guess_lst, int(score), msg)
    else:
        msg = "you lose! the right word is " + word
        display_state(pattern, wrong_guess_lst, int(score), msg)
    return score

def find_hint(lst):
    if HINT_LENGTH < len(lst):

        return [lst[i*len(lst)//HINT_LENGTH] for i in range(HINT_LENGTH)]
    return lst


#run_single_game (["rtgfd","sdfg"],10)

def main():
    word_list = load_words()
    score = POINTS_INITIAL
    playing_times = 1
    score =run_single_game(word_list,score)

    while score > 0:
        msg="u play until now "+ str(playing_times) + " times, and ur score is " + str(score)+" do you want to play again?"
        user_choice =  play_again(msg)
        if user_choice == True:
            playing_times += 1
            run_single_game(word_list, score)
        elif user_choice == False:
            score = -1
    if score == 0:
        msg = "u play " + str(playing_times) + " times until now, do you want to play again?"
        user_choice_after_loss = play_again(msg)
        if user_choice_after_loss == True:
            main()



#word_list = load_words()
#print(len(word_list[0]))
#words = ['aaa','zzzz','qqq']
#pat=  '_ab'

def filter_word(word,pattern,wrong_guess_lst):
    if len(word) != len(pattern):
        return False
    else:
        for i in range(len(pattern)):
            if word[i] in wrong_guess_lst or (pattern[i] != "_" and (word.count(word[i]) != pattern.count(word[i]) or word[i] != pattern[i])):
                return False
    return True

def filter_words_list(words,pattern,wrong_guess_lst):

    wordToruturn = []
    for word in words:
        if filter_word(word, pattern, wrong_guess_lst):
            wordToruturn.append(word)
    return wordToruturn

if __name__=="__main__":
    main()
