def sort_on(dict):
    return dict["num"]

def get_num_words(booktext):
    wc=booktext.split()
    #print(f"{len(wc)} words found in the document")
    print(f"Found {len(wc)} total words")

def count_characters(booktext):
    result=[]
    booktext_lower=booktext.lower()
    for key in booktext_lower:
        if key.isalpha():
            #if not any(d.get('char', default_value) == key for d in result):
            if not any(d["char"] == key for d in result):
                d={"char":"","num":0}
                d["char"]= key
                d["num"]=0
                result.append(d)
            
            a=[d for d in result if d["char"] == key]
            #car[0].update({"year": (car[0].get("year")+1)})
            a[0].update({"num": a[0].get("num")+1})
            #print(a)
            #break
        
            
    #print(result)
    #result_sorted=sort_on(result)
    result_sorted=result
    result_sorted.sort(reverse=True, key=sort_on)
    #print(result_sorted)
    return(result_sorted)