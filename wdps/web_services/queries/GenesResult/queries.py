query_GetAllGenes = '''
query GetAllGenes{
  getObjectList(datamartType:"gene") {
    _id
    name
    productsName
  }
}
'''
#query_Get