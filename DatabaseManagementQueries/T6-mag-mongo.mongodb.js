// *****PLEASE ENTER YOUR DETAILS BELOW*****
// T6-mag-mongo.mongodb.js

// Student ID: 34269193
// Student Name: Robiatul Adawiyah Al-Qosh

//Comments for your marker:
// In 6d --> The no_of_artworks was not updated after i add the contents in artworks. So, I updated it manually using $set.

// ===================================================================================
// Do not modify or remove any of the comments below (items marked with //)
// ===================================================================================

//Use (connect to) your database - you MUST update xyz001
//with your authcate username

use("ralq0003")

//(b)
// PLEASE PLACE REQUIRED MONGODB COMMAND TO CREATE THE COLLECTION HERE
// YOU MAY PICK ANY COLLECTION NAME
// ENSURE that your query is formatted and has a semicolon
// (;) at the end of this answer

//Drop collection 

use("ralq0003");
db.getCollectionNames();
db.monashart.drop();


//Create collection and insert documents

use("ralq0003");
db.monashart.insertMany([
    {
        "_id": 1,
        "name": "Ajimat Januar",
        "address": {
            "street": "Jl. Panglima Sudirman No. 33",
            "city": "Cimahi",
            "region": "West Java"
        },
        "phone": "0225300384",
        "no_of_artworks": 3,
        "artworks": [
            {
                "no": 1,
                "title": "The Creation of Adam",
                "minimum_price": 30000
            },
            {
                "no": 3,
                "title": "Serpihan Kaca",
                "minimum_price": 25000
            },
            {
                "no": 2,
                "title": "Pesta Perahu",
                "minimum_price": 14500
            }
        ]
    },
    {
        "_id": 2,
        "name": "Nilam Pratiwi",
        "address": {
            "street": "Jl. Moch. Toha No. 200",
            "city": "Surabaya",
            "region": "East Java"
        },
        "phone": "0318858093",
        "no_of_artworks": 1,
        "artworks": [
            {
                "no": 1,
                "title": "The Starry Night",
                "minimum_price": 55400
            }
        ]
    },
    {
        "_id": 3,
        "name": "Bagong ",
        "address": {
            "street": "Jl. Raden Intan No. 161",
            "city": "Sleman",
            "region": "DI Yogyakarta"
        },
        "phone": "0818843662",
        "no_of_artworks": 1,
        "artworks": [
            {
                "no": 1,
                "title": "Saint Francis of Assisi",
                "minimum_price": 24500
            }
        ]
    },
    {
        "_id": 4,
        "name": "Gatot Prabowo",
        "address": {
            "street": "Jl. Gajah Mada No. 14",
            "city": "Lombok",
            "region": "West Nusa Tenggara (NTB)"
        },
        "phone": null,
        "no_of_artworks": 1,
        "artworks": [
            {
                "no": 1,
                "title": "The Last Supper",
                "minimum_price": 17900
            }
        ]
    },
    {
        "_id": 5,
        "name": " Pakpahan",
        "address": {
            "street": "Jl. Pahlawan Trip No. 32",
            "city": "Medan",
            "region": "North Sumatra"
        },
        "phone": "0819562816",
        "no_of_artworks": 2,
        "artworks": [
            {
                "no": 1,
                "title": "Padang Belukar",
                "minimum_price": 45000
            },
            {
                "no": 2,
                "title": "The Sojourn",
                "minimum_price": 46700.45
            }
        ]
    },
    {
        "_id": 7,
        "name": "Septi Hartati",
        "address": {
            "street": "Jl. Manggarai Raya Gg. Kepompong No. 34",
            "city": "Jakarta Selatan",
            "region": "DKI Jakarta"
        },
        "phone": null,
        "no_of_artworks": 2,
        "artworks": [
            {
                "no": 1,
                "title": "Gadis Berkerudung Jingga",
                "minimum_price": 12900
            },
            {
                "no": 2,
                "title": "Saint Francis of Assisi",
                "minimum_price": 34536.9
            }
        ]
    },
    {
        "_id": 8,
        "name": "Iman Sulaiman",
        "address": {
            "street": "Jl. K.H. Wahid Hasyim (Kopo) No. 805",
            "city": "Bandung",
            "region": "West Java"
        },
        "phone": "0813427245",
        "no_of_artworks": 2,
        "artworks": [
            {
                "no": 2,
                "title": "Cafe Terrace at Night",
                "minimum_price": 45600.35
            },
            {
                "no": 1,
                "title": "Anting Mutiara",
                "minimum_price": 23100
            }
        ]
    },
    {
        "_id": 9,
        "name": "Alisa Kusudiarjo",
        "address": {
            "street": "Jl. Semeru No. 3",
            "city": "Palembang",
            "region": "South Sumatra"
        },
        "phone": "0817832032",
        "no_of_artworks": 1,
        "artworks": [
            {
                "no": 1,
                "title": "The Mystic",
                "minimum_price": 34000
            }
        ]
    },
    {
        "_id": 10,
        "name": "Restu Ningrum",
        "address": {
            "street": "Jl. Sosrowidjayan Gg. 4 No. 17",
            "city": "Yogyakarta",
            "region": "DI Yogyakarta"
        },
        "phone": "0817345845",
        "no_of_artworks": 1,
        "artworks": [
            {
                "no": 1,
                "title": "The Scientist",
                "minimum_price": 24000
            }
        ]
    }
]);


// List all documents you added

use("ralq0003");
db.monashart.find();


//(c)
// PLEASE PLACE REQUIRED MONGODB COMMAND/S FOR THIS PART HERE
// ENSURE that your query is formatted and has a semicolon
// (;) at the end of this answer

use("ralq0003");
db.monashart.find({
    $or:    [
            {"no_of_artworks": 2},
            {$and:  [
                    {"no_of_artworks": 1},
                    {"artworks.minimum_price": {$gte: 40000}}
            ]}
    ]
});


//(d)
// PLEASE PLACE REQUIRED MONGODB COMMAND/S FOR THIS PART HERE
// ENSURE that your query is formatted and has a semicolon
// (;) at the end of this answer

use("ralq0003");
db.monashart.updateOne(
    { "_id": 5 },
    { $push: {
        "artworks": {
            "no": 3,
            "title": "Biru Senja",
            "minimum_price": 25000
            }
        }
    }
);

use("ralq0003");
db.monashart.updateOne(
    { "_id": 5 },
    { $set: {
        "no_of_artworks": 3
        }
    }
);


// Illustrate/confirm changes made

use("ralq0003");
db.monashart.find();

