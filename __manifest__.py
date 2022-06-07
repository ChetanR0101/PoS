{
    "name": "Pos",
    "version":"1.0",
    "author":"Prisms - PoS",
    "description":"This App for PoS invoice",
    "sequence":-100,
    "depends":["base"],
    "data":[
            "views/pos_checkin_views.xml",
            "views/pos_checkout_views.xml",
            "views/pos_products_views.xml",
            "security/ir.model.access.csv"
            ],
    "installable":True,
    "application":True
}