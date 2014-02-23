#! /usr/bin/python

import re
import urllib

url = 'http://www.cciehof.com/'

def get_all_data():
    print 'Requesting data from server...'
    u = urllib.urlopen(url)
    page = u.read()
    mo_l = re.findall(r'CCIE #([0-9]+)\s+-\s+([\s\w]+)(\(.*\))', page)
    ccie_dict_all = {}
    for mo_tuple in mo_l:
        '''
        >>> mo_l[23]
        ('1069', 'KENT SCHWARTZ ', '(1,Routing and Switching)')
        >>> mo_l[6]
        ('1034', 'PHILLIP REMAKER ', '(2,Routing and Switching, ISP Dial)')
        '''
        ccie_num = int(mo_tuple[0])
        name = mo_tuple[1].strip().lower()
        cert_detail = mo_tuple[2].strip('()')
        cert_l = cert_detail.split(',')
        try:
            num_of_ccie = int(cert_l[0].strip())
        except ValueError as e:
            #print e
            continue
        cert_l.pop(0)

        ccie_dict_all[name] = {'ccie_num'    : ccie_num,
                           'num_of_ccie' : num_of_ccie,
                           'cert_l'      : cert_l
                          }
    print '... Received all data'
    return ccie_dict_all

def find_by_name(name, ccie_dict_all):
    if name not in ccie_dict_all:
        print name.title(), " was either not found or was not verifiable"
        return None
    #print 'Found ', name, ' in database'
    return ccie_dict_all[name]

def print_record(ccie_dict, name):
    print name.title()
    print '\tCCIE number: ', ccie_dict['ccie_num']
    print '\tNumber of CCIE certifications: ', ccie_dict['num_of_ccie']
    print '\tCertificate list'
    for i in range(len(ccie_dict['cert_l'])):
        print '\t\t', ccie_dict['cert_l'][i].strip()

if __name__ == '__main__':
    name_l = ['Phillip Remaker', 'ANDREW YOUrtcHENKO', 'ALOK WADHWA',
              'MIKE CRANE', 'NEIL MOORE', 'JAVED TUFAIL',
              'Stephen Lee', 'Srinivas Vegesna', 'Jose Liste']
    ccie_dict_all = get_all_data()
    for name in name_l:
        ccie_dict = find_by_name(name.lower(), ccie_dict_all)
        if ccie_dict is not None:
            print_record(ccie_dict, name)
        print '*' * 50
    
    

