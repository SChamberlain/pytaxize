import sys
from lxml import etree
import pandas as pd
import requests
from pytaxize.refactor import Refactor

def ubio_search(searchName = None, searchAuth = None, searchYear = None,
    order = None, sci = None, vern = None, keyCode = None):
    '''
    ubio_search returns NameBankIDs that match search terms

    :param searchName: (string) - term to search within name string
    :param searchAuth: (string) - term to search within name authorship
    :param searchYear: (string) - term to search within name year
    :param order: (string) - (name or namebankID) field by which the results will
    be sorted (default is namebankID)
    :param sci: (int) - (sci, vern, or all) type of results to be returned
    (default is all)
    :param vern: (int) - (limit 1000) maximum number of results to be returned
    (default is 1000)
    :param keyCode: Your uBio API key; loads from .Rprofile. If you don't have
       one, obtain one at http://www.ubio.org/index.php?pagename=form.
    :param callopts: Parameters passed on to httr::GET call.

    Usage
    # A basic example
    >>> import pytaxize
    >>>
    >>> pytaxize.ubio_search(searchName = 'elephant', sci = 1, vern = 0)
    >>> pytaxize.ubio_search(searchName = 'Astragalus aduncus', sci = 1, vern = 0)
    '''
    url = "http://www.ubio.org/webservices/service.php"
    ubioApiKey = "b052625da5f330e334471f8efe725c07bf4630a6"
    payload = {'function': 'namebank_search', 'searchName': searchName,
               'searchAuth': searchAuth, 'searchYear': searchYear, 'order': order,
               'sci': sci, 'vern': vern, 'keyCode': ubioApiKey}
    tt = Refactor(url, payload, request='get').xml()
    nodes = tt.xpath('//value')

    if (len(nodes) == 0):
        sys.exit('Please enter a valid searchName')
    outlist = []
    for i in range(len(nodes)):
        tt_ = nodes[i].getchildren()
        outlist.append([x.text for x in tt_[:8]])
    df = pd.DataFrame(outlist, columns=['namebankID','nameString','fullNameString','packageID','packageName','basionymunit','rankID','rankName'])
    return df
    # tt = content(tmp)
    # toget = c("namebankID", "nameString", "fullNameString", "packageID",
    #                    "packageName", "basionymUnit", "rankID", "rankName")
    # temp2 = lapply(toget, function(x) sapply(xpathApply(tt, paste("//", x, sep="")), xmlValue))
    # temp2[2:3] = sapply(temp2[2:3], base64Decode)
    # out = data.frame(do.call(cbind, temp2))
    # names(out) = c("namebankid", "namestring", "fullnamestring", "packageid",
    #                               "packagename", "basionymunit", "rankid", "rankname")


# searchAuth = None
# searchYear = None
# order = None
# sci = None
# vern = None
# keyCode = None
