
// See "sample_jsonc" for the .JSON version of this .js file

// this object is an array, notice the square brackets
myObj = [
    {
        "Id": 1,
        "FirstName": "Jane",
        "LastName": "Doe",
        "Email": "j.doe@names.com"
    },

    {
        "Id": 2,
        "FirstName": "John",
        "LastName": "Smith",
        "Email": "j.smith@names.com"
    },

    {
        "Id": 3,
        "FirstName": "Diamond",
        "LastName": "Jim",
        "Email": "d.jim@names.com"
    }

]

// Therefore, when we log to the terminal we can call "0" for the first element
console.log(myObj[0]);

// Specific key values can also be output
console.log("")
console.log(myObj[2].Email);

// Or we might instead make an object with an array inside
myObj2 = { "People":

    [
        {
            "Id": 1,
            "FirstName": "Jane",
            "LastName": "Doe",
            "Email": "j.doe@names.com",
            "Active": true            
        },

        {
            "Id": 2,
            "FirstName": "John",
            "LastName": "Smith",
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

// Let's log the last item from the array within the "People" object
console.log("");
console.log(myObj2.People[2]);

// How about the LastName value for the second item in the array,km 
console.log("");
console.log(myObj2.People[1].LastName);

// The "typeof" operator returns the variable type
console.log("");
console.log(typeof myObj2.People[1].Active);