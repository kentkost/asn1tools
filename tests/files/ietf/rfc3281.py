EXPECTED = {'PKIXAttributeCertificate': {'extensibility-implied': False,
                              'imports': {'PKIX1Explicit88': ['Attribute',
                                                              'AlgorithmIdentifier',
                                                              'CertificateSerialNumber',
                                                              'Extensions',
                                                              'UniqueIdentifier',
                                                              'id-pkix',
                                                              'id-pe',
                                                              'id-kp',
                                                              'id-ad',
                                                              'id-at'],
                                          'PKIX1Implicit88': ['GeneralName',
                                                              'GeneralNames',
                                                              'id-ce']},
                              'object-classes': {},
                              'object-sets': {},
                              'tags': 'IMPLICIT',
                              'types': {'AAControls': {'members': [{'name': 'pathLenConstraint',
                                                                    'optional': True,
                                                                    'restricted-to': [(0,
                                                                                       'MAX')],
                                                                    'type': 'INTEGER'},
                                                                   {'name': 'permittedAttrs',
                                                                    'optional': True,
                                                                    'tag': {'number': 0},
                                                                    'type': 'AttrSpec'},
                                                                   {'name': 'excludedAttrs',
                                                                    'optional': True,
                                                                    'tag': {'number': 1},
                                                                    'type': 'AttrSpec'},
                                                                   {'default': 'TRUE',
                                                                    'name': 'permitUnSpecified',
                                                                    'type': 'BOOLEAN'}],
                                                       'type': 'SEQUENCE'},
                                        'ACClearAttrs': {'members': [{'name': 'acIssuer',
                                                                      'type': 'GeneralName'},
                                                                     {'name': 'acSerial',
                                                                      'type': 'INTEGER'},
                                                                     {'element': {'type': 'Attribute'},
                                                                      'name': 'attrs',
                                                                      'type': 'SEQUENCE '
                                                                              'OF'}],
                                                         'type': 'SEQUENCE'},
                                        'AttCertIssuer': {'members': [{'name': 'v1Form',
                                                                       'type': 'GeneralNames'},
                                                                      {'name': 'v2Form',
                                                                       'tag': {'number': 0},
                                                                       'type': 'V2Form'}],
                                                          'type': 'CHOICE'},
                                        'AttCertValidityPeriod': {'members': [{'name': 'notBeforeTime',
                                                                               'type': 'GeneralizedTime'},
                                                                              {'name': 'notAfterTime',
                                                                               'type': 'GeneralizedTime'}],
                                                                  'type': 'SEQUENCE'},
                                        'AttCertVersion': {'type': 'INTEGER'},
                                        'AttrSpec': {'element': {'type': 'OBJECT '
                                                                         'IDENTIFIER'},
                                                     'type': 'SEQUENCE OF'},
                                        'AttributeCertificate': {'members': [{'name': 'acinfo',
                                                                              'type': 'AttributeCertificateInfo'},
                                                                             {'name': 'signatureAlgorithm',
                                                                              'type': 'AlgorithmIdentifier'},
                                                                             {'name': 'signatureValue',
                                                                              'type': 'BIT '
                                                                                      'STRING'}],
                                                                 'type': 'SEQUENCE'},
                                        'AttributeCertificateInfo': {'members': [{'name': 'version',
                                                                                  'type': 'AttCertVersion'},
                                                                                 {'name': 'holder',
                                                                                  'type': 'Holder'},
                                                                                 {'name': 'issuer',
                                                                                  'type': 'AttCertIssuer'},
                                                                                 {'name': 'signature',
                                                                                  'type': 'AlgorithmIdentifier'},
                                                                                 {'name': 'serialNumber',
                                                                                  'type': 'CertificateSerialNumber'},
                                                                                 {'name': 'attrCertValidityPeriod',
                                                                                  'type': 'AttCertValidityPeriod'},
                                                                                 {'element': {'type': 'Attribute'},
                                                                                  'name': 'attributes',
                                                                                  'type': 'SEQUENCE '
                                                                                          'OF'},
                                                                                 {'name': 'issuerUniqueID',
                                                                                  'optional': True,
                                                                                  'type': 'UniqueIdentifier'},
                                                                                 {'name': 'extensions',
                                                                                  'optional': True,
                                                                                  'type': 'Extensions'}],
                                                                     'type': 'SEQUENCE'},
                                        'ClassList': {'type': 'BIT STRING'},
                                        'Clearance': {'members': [{'name': 'policyId',
                                                                   'tag': {'number': 0},
                                                                   'type': 'OBJECT '
                                                                           'IDENTIFIER'},
                                                                  {'default': ['unclassified'],
                                                                   'name': 'classList',
                                                                   'tag': {'number': 1},
                                                                   'type': 'ClassList'},
                                                                  {'element': {'type': 'SecurityCategory'},
                                                                   'name': 'securityCategories',
                                                                   'optional': True,
                                                                   'tag': {'number': 2},
                                                                   'type': 'SET '
                                                                           'OF'}],
                                                      'type': 'SEQUENCE'},
                                        'Holder': {'members': [{'name': 'baseCertificateID',
                                                                'optional': True,
                                                                'tag': {'number': 0},
                                                                'type': 'IssuerSerial'},
                                                               {'name': 'entityName',
                                                                'optional': True,
                                                                'tag': {'number': 1},
                                                                'type': 'GeneralNames'},
                                                               {'name': 'objectDigestInfo',
                                                                'optional': True,
                                                                'tag': {'number': 2},
                                                                'type': 'ObjectDigestInfo'}],
                                                   'type': 'SEQUENCE'},
                                        'IetfAttrSyntax': {'members': [{'name': 'policyAuthority',
                                                                        'optional': True,
                                                                        'tag': {'number': 0},
                                                                        'type': 'GeneralNames'},
                                                                       {'element': {'members': [{'name': 'octets',
                                                                                                 'type': 'OCTET '
                                                                                                         'STRING'},
                                                                                                {'name': 'oid',
                                                                                                 'type': 'OBJECT '
                                                                                                         'IDENTIFIER'},
                                                                                                {'name': 'string',
                                                                                                 'type': 'UTF8String'}],
                                                                                    'type': 'CHOICE'},
                                                                        'name': 'values',
                                                                        'type': 'SEQUENCE '
                                                                                'OF'}],
                                                           'type': 'SEQUENCE'},
                                        'IssuerSerial': {'members': [{'name': 'issuer',
                                                                      'type': 'GeneralNames'},
                                                                     {'name': 'serial',
                                                                      'type': 'CertificateSerialNumber'},
                                                                     {'name': 'issuerUID',
                                                                      'optional': True,
                                                                      'type': 'UniqueIdentifier'}],
                                                         'type': 'SEQUENCE'},
                                        'ObjectDigestInfo': {'members': [{'name': 'digestedObjectType',
                                                                          'type': 'ENUMERATED',
                                                                          'values': [('publicKey',
                                                                                      0),
                                                                                     ('publicKeyCert',
                                                                                      1),
                                                                                     ('otherObjectTypes',
                                                                                      2)]},
                                                                         {'name': 'otherObjectTypeID',
                                                                          'optional': True,
                                                                          'type': 'OBJECT '
                                                                                  'IDENTIFIER'},
                                                                         {'name': 'digestAlgorithm',
                                                                          'type': 'AlgorithmIdentifier'},
                                                                         {'name': 'objectDigest',
                                                                          'type': 'BIT '
                                                                                  'STRING'}],
                                                             'type': 'SEQUENCE'},
                                        'ProxyInfo': {'element': {'type': 'Targets'},
                                                      'type': 'SEQUENCE OF'},
                                        'RoleSyntax': {'members': [{'name': 'roleAuthority',
                                                                    'optional': True,
                                                                    'tag': {'number': 0},
                                                                    'type': 'GeneralNames'},
                                                                   {'name': 'roleName',
                                                                    'tag': {'number': 1},
                                                                    'type': 'GeneralName'}],
                                                       'type': 'SEQUENCE'},
                                        'SecurityCategory': {'members': [{'name': 'type',
                                                                          'tag': {'kind': 'IMPLICIT',
                                                                                  'number': 0},
                                                                          'type': 'OBJECT '
                                                                                  'IDENTIFIER'},
                                                                         {'choices': {},
                                                                          'name': 'value',
                                                                          'tag': {'number': 1},
                                                                          'type': 'ANY '
                                                                                  'DEFINED '
                                                                                  'BY',
                                                                          'value': 'type'}],
                                                             'type': 'SEQUENCE'},
                                        'SvceAuthInfo': {'members': [{'name': 'service',
                                                                      'type': 'GeneralName'},
                                                                     {'name': 'ident',
                                                                      'type': 'GeneralName'},
                                                                     {'name': 'authInfo',
                                                                      'optional': True,
                                                                      'type': 'OCTET '
                                                                              'STRING'}],
                                                         'type': 'SEQUENCE'},
                                        'Target': {'members': [{'name': 'targetName',
                                                                'tag': {'number': 0},
                                                                'type': 'GeneralName'},
                                                               {'name': 'targetGroup',
                                                                'tag': {'number': 1},
                                                                'type': 'GeneralName'},
                                                               {'name': 'targetCert',
                                                                'tag': {'number': 2},
                                                                'type': 'TargetCert'}],
                                                   'type': 'CHOICE'},
                                        'TargetCert': {'members': [{'name': 'targetCertificate',
                                                                    'type': 'IssuerSerial'},
                                                                   {'name': 'targetName',
                                                                    'optional': True,
                                                                    'type': 'GeneralName'},
                                                                   {'name': 'certDigestInfo',
                                                                    'optional': True,
                                                                    'type': 'ObjectDigestInfo'}],
                                                       'type': 'SEQUENCE'},
                                        'Targets': {'element': {'type': 'Target'},
                                                    'type': 'SEQUENCE OF'},
                                        'V2Form': {'members': [{'name': 'issuerName',
                                                                'optional': True,
                                                                'type': 'GeneralNames'},
                                                               {'name': 'baseCertificateID',
                                                                'optional': True,
                                                                'tag': {'number': 0},
                                                                'type': 'IssuerSerial'},
                                                               {'name': 'objectDigestInfo',
                                                                'optional': True,
                                                                'tag': {'number': 1},
                                                                'type': 'ObjectDigestInfo'}],
                                                   'type': 'SEQUENCE'}},
                              'values': {'id-aca': {'type': 'OBJECT IDENTIFIER',
                                                    'value': ['id-pkix', 10]},
                                         'id-aca-accessIdentity': {'type': 'OBJECT '
                                                                           'IDENTIFIER',
                                                                   'value': ['id-aca',
                                                                             2]},
                                         'id-aca-authenticationInfo': {'type': 'OBJECT '
                                                                               'IDENTIFIER',
                                                                       'value': ['id-aca',
                                                                                 1]},
                                         'id-aca-chargingIdentity': {'type': 'OBJECT '
                                                                             'IDENTIFIER',
                                                                     'value': ['id-aca',
                                                                               3]},
                                         'id-aca-encAttrs': {'type': 'OBJECT '
                                                                     'IDENTIFIER',
                                                             'value': ['id-aca',
                                                                       6]},
                                         'id-aca-group': {'type': 'OBJECT '
                                                                  'IDENTIFIER',
                                                          'value': ['id-aca',
                                                                    4]},
                                         'id-at-clearance': {'type': 'OBJECT '
                                                                     'IDENTIFIER',
                                                             'value': [('joint-iso-ccitt',
                                                                        2),
                                                                       ('ds',
                                                                        5),
                                                                       ('module',
                                                                        1),
                                                                       ('selected-attribute-types',
                                                                        5),
                                                                       ('clearance',
                                                                        55)]},
                                         'id-at-role': {'type': 'OBJECT '
                                                                'IDENTIFIER',
                                                        'value': ['id-at', 72]},
                                         'id-ce-targetInformation': {'type': 'OBJECT '
                                                                             'IDENTIFIER',
                                                                     'value': ['id-ce',
                                                                               55]},
                                         'id-pe-aaControls': {'type': 'OBJECT '
                                                                      'IDENTIFIER',
                                                              'value': ['id-pe',
                                                                        6]},
                                         'id-pe-ac-auditIdentity': {'type': 'OBJECT '
                                                                            'IDENTIFIER',
                                                                    'value': ['id-pe',
                                                                              4]},
                                         'id-pe-ac-proxying': {'type': 'OBJECT '
                                                                       'IDENTIFIER',
                                                               'value': ['id-pe',
                                                                         10]}}}}