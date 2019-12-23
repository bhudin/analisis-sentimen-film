import tkinter

main_window = tkinter.Tk()
main_window.title("Sentimen Analisis")

resultt = [0,0,0,0,0,0,0,0,0,0,0]
result = "Hasil akan muncul disini\n"

def showResult():
    calculate()
    result = ""
    for i in range(len(resultt)):
        result += str(resultt[i])
    resultText.config(text=result)

inputText = tkinter.Label(main_window, text="Masukkan kalimat yang ingin di analisis :\n")
inputField = tkinter.Entry(main_window)
resultText = tkinter.Label(main_window, text=result)
submitBtn = tkinter.Button(main_window, text="Submit", command=showResult)

def calculate():
    new_kalimat = inputField.get()
    new_index = []
    new_word = new_kalimat.split()
    merge_text = ""
    dataset = [["the movie today and thought it was a good effort, good messages for kids", "very slow-moving, aimless movie about a distressed, drifting young man",
                "movie showed a lot of Florida at it best, made it look very appealing", "It had some average acting from the main person, and it was a low budget as you clearly can see",
                "The structure of this film is easily the most tightly constructed in the history of cinema", "The plot simply rumbles on like a machine, desperately depending on the addition of new scenes",
                "I must say I have taped most of the episodes and i find myself watching them over and over again", "Even if you love bad movies, do not watch this movie",
                "I would give this television series a 10 plus if i could", "Lucy Bell is so much higher than this crap and for her to sink this low is quite depressing"],
            [True, False, True, False, True, False, True, False, True, False]]

    for i in range(len(dataset[0])):
        dataset[0][i] = dataset[0][i].replace(",","")
        if dataset[0][i] not in merge_text:
            merge_text += dataset[0][i].lower() + " "
            
    preprocess = []
    stopwords = ["i", "the", "it", "was", "a", "in", "of", "on", "if", "and", "you", "at", "them", "would", "is"]
    def split_line(text):
        words = text.split()
        for word in range(len(words)):
            if words[word] not in preprocess:
                preprocess.append(words[word])
                
    split_line(merge_text)
    preprocess = list(set(preprocess)-set(stopwords))
    binary_data = dataset
    for i in range(len(dataset[0])):
        tmp = dataset[0][i].lower().split()
        tmp2 = []
        for j in preprocess:
            if j in tmp:
                tmp2.append(1)
            elif j not in tmp:
                tmp2.append(0)
        binary_data[0][i] = tmp2
        
    count = 0
    p = 0
    count_f = 0
    for i in range(len(binary_data[0])):
        if binary_data[1][i] == True:
            count += 1
        prob_pos = count/len(binary_data[0])
        if binary_data[1][i] == False:
            count_f += 1
        prob_neg = count_f/len(binary_data[0])


    post_khus = []
    for k in range(len(preprocess)):
        pk = 0
        for i in range(len(binary_data[0])):
            if binary_data[1][i] == True:
                pk += binary_data[0][i][k]
        post_khus.append(pk)
        
    post_khus_f = []
    for l in range(len(preprocess)):
        pk_f = 0
        for i in range(len(binary_data[0])):
            if binary_data[1][i] == False:
                pk_f += binary_data[0][i][l]
        post_khus_f.append(pk_f)

    res_prob_word = []    
    for a in range(len(preprocess)):
        rpw = (post_khus[a]+1)/(p+len(preprocess))
        res_prob_word.append(round(rpw,3))
        
    res_prob_word_f = []    
    for a in range(len(preprocess)):
        rpw = (post_khus_f[a]+1)/(p+len(preprocess))
        res_prob_word_f.append(round(rpw,3))

    def multiplyList(myList) : 
        result = 1
        for x in myList: 
            result = result * x  
        return result

    tmp3 = []
    for j in preprocess:
        if j in new_word:
            tmp3.append(1)
        elif j not in new_word:
            tmp3.append(0)
    new_index = tmp3

    def prod(a,b):
        p=[]
        for i in range(len(a)):
            if a[i] != 0:
                p.append(a[i]*b[i])
        return p
    hasil = prod(new_index,res_prob_word)
    hasil_f = prod(new_index,res_prob_word_f)

    global result
    print("-"*35)
    print("No", " Words         +", "-" )
    for i in range(len(preprocess)):
        if i < 9:
            print(i+1," ", preprocess[i]," "*(12-len(preprocess[i])), post_khus[i], post_khus_f[i])
        else:
            print(i+1,"", preprocess[i]," "*(12-len(preprocess[i])), post_khus[i], post_khus_f[i])
    resultt[0] = hasil
    resultt[1] = "\n"
    u = prob_pos * round(multiplyList(hasil), 18)
    resultt[2] = "Posterior Positif dikali semua Prob. kata latih = " + str(u)
    resultt[3] = "\n"
    resultt[4] = hasil_f
    resultt[5] = "\n"
    o = prob_neg * round(multiplyList(hasil_f), 18)
    resultt[6] = "Posterior Negatif dikali semua Prob. kata latih = " + str(o)
    resultt[7] = "\n"
    if u >= o:
        resultt[8] = "Kalimat -" + new_kalimat + "- memiliki sentimen positif"
        resultt[9] = "\n"
        resultt[10] = "\n"
    else:
        resultt[8] = "Kalimat -" + new_kalimat + "- memiliki sentimen negatif"
        resultt[9] = "\n"
        resultt[10] = "\n"

def split_line(text,preprocess):
    words = text.split()
    for word in range(len(words)):
        if words[word] not in preprocess:
            preprocess.append(words[word])

def multiplyList(myList) : 
    result = 1
    for x in myList: 
         result = result * x  
    return result

def prod(a,b):
    p=[]
    for i in range(len(a)):
        if a[i] != 0:
            p.append(a[i]*b[i])
    return p

inputText.pack()
inputField.pack()
inputField.focus_set()

submitBtn.pack()
resultText.pack()

main_window.mainloop()
