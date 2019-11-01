from flask import Flask,request,jsonify
import json
import urllib.request as urllib

app=Flask(__name__)


# Path for URL will be localhost:5000/repos and payload will be in json { "org":"github-org-id" }
@app.route('/repos',methods=['POST'])
def highRatedRepo():

    try:

        if not request.json or 'org' not in request.json:
            return 'Request Body is not right!'

        # Calling github api with constraints of org-id and sorting in descending order according to stars with limit 3
        url='https://api.github.com/search/repositories?q=org:'+request.json.get('org')+'&sort=stars&order=desc&per_page=3'

        # Reading response of url and reading and loading it as json
        data=json.loads(urllib.urlopen(url).read())

        # Returning { "results": [ "name":"repo_name", "stars":number_of_stars ] } for top 3 repos in given org-id
        return jsonify({'results':[{'name':result['name'] , 'stars':result['stargazers_count']} for result in data['items']]})

    except Exception as e:

        return 'Exception Occured: '+str(e)+' \n**ERROR THROWN BY GITHUB API** \n <a href="http://developer.github.com/v3/search">DOC LINK</a>'

if __name__=='__main__':
    app.run(debug=True)