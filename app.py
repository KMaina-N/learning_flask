from flask import Flask, render_template,request
import requests, json
app=Flask(__name__)

@app.route('/', methods=['GET','POST'])

def calculate():
    oib=''
    #name=''
    if request.method=='POST' and 'oib' in request.form:
        OIB=(request.form.get('oib'))

        oib=int(OIB)


        # 76860791838
        identifikator = oib
        url = f'https://sudreg-api.pravosudje.hr/javni/subjekt_detalji?tipIdentifikatora=oib&identifikator={identifikator}&expand_relations=True'
        newheaders = {"Accept": "application/json", 'Ocp-Apim-Subscription-Key': '67748797ee8c4ad2ba050a079e0b39f5'}

        response = requests.get(url,
                                data={"tipIdentifikatora": 'oib', "identifikator": identifikator,
                                      "expand_relations": True},
                                headers=newheaders)
        package_json = response.json()
        package_str = json.dumps(package_json, indent=2)
        #print(package_str)
        oib=package_json['oib']
        print('OIB:',oib)
        for tvtrke in package_json['tvrtke']:
            name = tvtrke['ime']

    return render_template('index.html', oib=oib,name=name)


if __name__=='__main__':
    app.run()