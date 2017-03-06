#API Docs

If you want to make a cron job to automate sandwich ordering, this API will help.
It will also let you view some information I haven't exposed on the main site yet.

##[/items/](http://hoagie.club/items/)

###Get a list of items

Send a `GET` to receive a JSON containing a list of item objects.

**NOTE:** items that can't be halved (*Middle Finger* and items from *FROM THE GRILL*) will have equal `price` and `price_half` properties.
Don't worry about sending in a "wrong" order since the server is smart enough to know when something can't be halved!

##[/api/order](http://hoagie.club/api/order)

###Creates a new order

Send a `POST` request with a JSON that looks like this:
```
{
    "email": "example@princeton.edu",
    "order": [
        {
            "id": 43,
            "in_half": true,
            "notes": "oil and mustard"
        },
        {
            "id": 2
        }
    ]
}
```
**NOTES:** 
* `order` must be an array, and the `notes` and `in_half` properties are optional.
* `content-type` must be `application/json`. The Python `requests` module can do this automatically if you call
`requests.post("http://hoagie.club/api/order", json={...})`. If you use cURL, you can set this with `-H "Content-Type: application/json"`

It will give you back JSON that looks like this:
```
{
    "success": true | false
}
```
Make sure to check your email to confirm the order!
