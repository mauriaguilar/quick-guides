import os
import json
from time import sleep

# get issues json from gitlab
project_id = "6550869"
out_file = "issues"
token = "ryP5_rYncef4ZL93hiWF"
page = "1"

def getApi(page,issue_iid=""):
    issue_path = ""
    if issue_iid != "":
        issue_path = "/" + issue_iid + "/notes"
    params = "?per_page=100\&page="+page
    cmd = 'curl --header "PRIVATE-TOKEN: '+token+'" https://gitlab.com/api/v4/projects/'+project_id+'/issues'+issue_path+params+' >> '+out_file+page+issue_iid+".json"
    print("COMANDO: "+cmd)
    os.system("rm "+out_file+page+issue_iid+".json")
    os.system(cmd)

def readJson(page):
    f = open(out_file+page+".json")
    data = json.load(f)

    cant = 0
    for d in data:
        print("--------------------------------------------------------")
        id = str(d['id'])
        title = str(d['title'])
        description = str(d['description'])
        links = str(d['_links']['notes'])
        iid = str(d['iid'])
        text = "<div style='background: #9AB9D9'>" + iid + " - " + title + "</div>" + "\n\n<br><br>"
        md_text = "issue> " + iid + " - " + title + "  \n"

        getApi(page,iid)
        n = open(out_file+page+iid+".json")
        n_data = json.load(n)
        for nd in n_data:
            ndata = str(nd['body'])
            if "changed" in ndata or "assigned" in ndata or "closed" in ndata:
                continue
            text += ndata
            text += "\n<br>---------------------------------------------------------\n<br>"
            md_text += (ndata + "  \n")
            md_text += "---------------------------------------------------------  \n  \n"

        cant += 1

        fi = open("issue_"+iid+".html","w")
        text = "<html><head></head><body>" + text + "</body></html>"
        fi.write(text)
        fi.close()

        mdf = open("issue_"+iid+".md","w")
        mdf.write(md_text)
        mdf.close()

        cmd = "pandoc issue_"+iid+".md -o iss/issue_"+iid+".html"
        os.system(cmd)

    print("Cant Issues: ",cant)

getApi("1")
getApi("2")

sleep(3)

# get info issues
readJson("1")
readJson("2")

def move_files(type):
    cmd = "rm -r " + type
    os.system(cmd)
    cmd = "mkdir " + type
    os.system(cmd)
    cmd = "mv *." + type + " " + type
    os.system(cmd)

move_files("pdf")
move_files("md")
move_files("html")
move_files("json")