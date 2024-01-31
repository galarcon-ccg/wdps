from flask import Flask, request, render_template, make_response, send_from_directory
from wdps.web_services.queries.GenesResult import WSGenes 

def gene_list():
    template = ":)"
    if request.method == 'POST':
        if request.form.get('search') == 'search':
            return template
    else:
        ws = WSGenes()
        list = ws.getAll_genes()
        print(list)
        return "list"
        
    
'''
def collection_list():
    template = "no collection support"
    if request.method == 'POST':
        if request.form.get('search') == 'search':
            keyword = request.form['keyword']
            collection = Gene_collection(gql_service,browser_url)
            results = collection.search(keyword)
            template =render_template('/ecoli/gene/index.html', data=results["data"], pagination=results["pagination"], search_result=keyword)
        elif request.form.get('nextPage') == 'nextPage':
            page_current = int(request.form['current_page'])
            page_last = int(request.form['last_page'])
            if page_current<page_last:
                page_current = page_current+1
            collection = Gene_collection(gql_service,browser_url)
            results = collection.search("RDBECOLI",page_current)
            template =render_template('/ecoli/gene/index.html', data=results["data"], pagination=results["pagination"], search_result="")
        elif request.form.get('prevPage') == 'prevPage':
            page_current = int(request.form['current_page'])
            if page_current > 0:
                page_current = page_current-1
            collection = Gene_collection(gql_service,browser_url)
            results = collection.search("RDBECOLI",page_current)
            template =render_template('/ecoli/gene/index.html', data=results["data"], pagination=results["pagination"], search_result="")
        else:
            template = "invalid access"
    else:
        collection = Gene_collection(gql_service,browser_url)
        results = collection.search("RDBECOLI")
        print(results)
        template =render_template('/ecoli/gene/index.html', data=results["data"], pagination=results["pagination"], search_result="")
    return template
    '''