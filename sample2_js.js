
// Remember that unlike the .JSON format...
// A .js file must have a "parent" variable object that holds the object with our data
MyObj = { "People":

    [
        
        {
            "Id": 1,
            "Name": {"FN": "Jane", "LN": "Doe"},
            "Email": "j.doe@names.com",
            "Active": true
        },

        {
            "Id": 2,
            "Name": ["John", "Smith"],
            "Email": "j.smith@names.com",
            "Active": true
        },

        {
            "Id": 3,
            "FirstName": "Diamond",
            "LastName": "Jim",
            "Email": "d.jim@names.com",
            "Active": false
        }

    ]
}
// Let's query our objects for their "Name" keys
console.log(MyObj.People[0].Name);
console.log("");
console.log(MyObj.People[1].Name);