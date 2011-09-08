Introduction
============

This product provides a group based lookup recipient source for 
`collective.megaphone`.

To register a group, configure it through zcml::

    <configure xmlns:grouplookup="http://namespaces.inigo-tech.com/megaphonegrouplookup">
        <grouplookup:group 
            name="mygroup_lookup"
            json_source="path_to_group_data.json"
            />
    </configure>


JSON Data Format
------------------

The json source expects this format::

    {
        'Group1 Title': [
            {
                'honorific': 'honorific',
                'first': 'firstname',
                'last': 'lastname',
                'email': 'user@server.com',
                'description': 'description'        
            }, ...
        ],
        'Group2 Title': [
            {
                'honorific': 'honorific',
                'first': 'firstname',
                'last': 'lastname',
                'email': 'user@server.com',
                'description': 'description'        
            }, ...
        ]
    }

Extra options
--------------

site
  Site ID. Provide this if you only want this recipient list available for a particular site

title
  Title of the group

description
  Description of the group

select_label
  Label for the group selection field

select_description
  Description for the group selection field
