import urllib, urllib.request, requests

# install a custom handler to prevent following of redirects automatically.
class SmartRedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        return headers
opener = urllib.request.build_opener(SmartRedirectHandler())
urllib.request.install_opener(opener)

parameters = {
    'seqdb':'pdb',
    'seq':'>Seq\nKLRVLGYHNGEWCEAQTKNGQGWVPSNYITPVNSLENSIDKHSWYHGPVSRNAAEY'
}
enc_params = urllib.parse.urlencode(parameters)
print(enc_params)

#post the seqrch request to the server
request = urllib.request.Request('https://www.ebi.ac.uk/Tools/hmmer/search/phmmer',enc_params)

#get the url where the results can be fetched from
with urllib.request.urlopen(request) as f:
    resp = f.read()
    results_url = requests.get('https://www.ebi.ac.uk/Tools/hmmer/results/7690E2DE-5C51-11EC-A638-6AE9DBC3747A/score')

# modify the range, format and presence of alignments in your results here
res_params = {
    'output': 'json',
    'range': '1,10'
}

# add the parameters to your request for the results
enc_res_params = urllib.parse.urlencode(res_params)
modified_res_url = results_url + '?' + enc_res_params

# send a GET request to the server
results_request = urllib.request.Request(modified_res_url)
data = urllib.request.urlopen(results_request)

# print out the results
dat = open('hmm.txt')
dat.write(data.read())
dat.close()