from flask import Flask, redirect,render_template,request

app=Flask(__name__)

results = []

@app.route('/', methods=['GET','POST'])
def input(): #main.html의 정보를 전송
    if request.method == 'POST':
        results = []
    return render_template('main.html')

@app.route('/home', methods=["POST"])
def home(): #홈버튼 기능
    if request.form.get('action') == "Home": # 홈버튼을 누르면 저장된 데이터 초기화
        results.clear()
        return render_template('main.html') # main.html로 이동


@app.route('/delete-result', methods=["POST"]) #선택된 row 삭제하는 기능
def delete_result():
    selected = request.form.getlist('selected')
    print("selected:", selected, flush=True)

    for index in sorted(selected, reverse=True):
        del results[int(index)]

    return render_template("result.html", results=results, enumerate=enumerate)


@app.route('/result',methods=['GET','POST']) 
def result(): #result 
    if request.method=='POST':
        name = request.form["name"]
        student_number = request.form["StudentNumber"]
        major = request.form["major"]
        email_id = request.form["email_id"]
        email_addr = request.form["email_addr"]
        gender = request.form.getlist("Gender")
        programming_languages = request.form.getlist("ProgrammingLanguages")
    
        result = { #결과 데이터 딕셔너리로 저장
            "이름": name,
            "학번": student_number,
            "전공": major,
            "이메일": email_id + "@" + email_addr,
            "성별": "".join(gender),
            "프로그래밍 언어": ", ".join(programming_languages)
        }

        results.append(result) #결과 데이터 리스트에 저장
        results.sort(key=lambda x: x["학번"]) # key 파라미터로 들어간 람다함수를 각 원소에 적용한 결과값을 기반으로 정렬
    
        return render_template("result.html", results=results, enumerate=enumerate)

if __name__=='__main__':
    app.run(debug=True,port=8000)