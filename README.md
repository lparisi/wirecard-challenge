# Wirecard Challenge Payment Registry Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

## List All Payments

**Definition:**

`GET /payments`

**Response:**

- `200 OK` on success

```json
{   {   "id":82,
        "amount":1.00,
        "type":"BOLETO",
        "status":"APPROVED",
        "client":{"id":1},
        "buyer":{   "name":"Miguel",
                    "email":"email@email.com",
                    "cpf":"32014080003"},
        "card":null,
        "boleto":{"id":83,
        "number":"34191790010104355872392553590008878710000100"
        }
    },
    {
        "id":86,
        "amount":1000.58,
        "type":"CREDIT_CARD",
        "status":"APPROVED",
        "client":{"id":1},
        "buyer":{"name":"Miguel",
        "email":"email@gmail.com",
        "cpf":"82613833009"},
        "card":{"id":85,
        "holderName":"Welligton Miguel",
        "number":"5477239667148925",
        "expiryDate":"2020-12-28",
        "cvv":"793"},
        "boleto":null
    },
    {
        "id":89,
        "amount":100.00,
        "type":"CREDIT_CARD",
        "status":"APPROVED",
        "client":{"id":1},
        "buyer":{"name":"Name Buyer",
        "email":"email@email.com",
        "cpf":"51170898041"},
        "card":{"id":88,
        "holderName":"Welligton Miguel",
        "number":"4929340466625068",
        "expiryDate":"2019-05-25",
        "cvv":"12"},
        "boleto":null
    },
}...
```


## Registering a new Payment

**Definition**

`POST /payments`

**Arguments:**

- `"id:string`     a globally unique identifier for this payment.
- `"amount:float` the payment amount
- `"type:string`   payment that can be either boleto or credit card.
- `"status:string` the payment can approved, pending or declined.
- `"client":string` a globally unique identifier for the client
- `"buyer": ` nesting buyer information
  - `"name":string` buyer name
  - `"email": string` buyer email address
  - `"cpf": string` buyer social security number (CPF)
- `"card"`: nesting credit card information
  - `"card_id": string`: an identifier for the credit card BIN (Bank Identification Number)
  - `"card_holderName": string` Cardholder's name
  - `"card_number": string` Credit Card number
  - `"card_expDate": string` Credit Card Expiry date
  - `"card_cvv": string` Credit Card Verification Value
- `"boleto": string` unique identifier for boleto payment

### Response for Credit Card Payment

**Response:**

- `201 Created` on success

```json
{
    {
        "id":42,
        "status":"Approved"}
}
```

### Response for Boleto Payment

**Response:**

- `201 Created` on success

```json
{   "boleto":                       {"number":"34191790010104351004791020150008178710026000"}
}
```

**Definition:**

`GET /payments/<int:id>`

## Lookup payment details

- `404 Not Found` if the payment does not exist

### Response for Boleto Payment

- `200 OK` on success

```json
{
    {"id":86,
    "amount":260.00,
    "type":"BOLETO",
    "status":"APPROVED",
    "client":{"id":1},
    "buyer":{   "name":"Miguel",
                "email":"email@email.com",
                "cpf":"32014080003"},
    "card":null,
    "boleto":{"id":83,
    "number":"34191790010104351004791020150008178710026000",
    }
}
```

### Response for Credit Card Payment

- `200 OK` on success

```json
[
    {   "id":82,
        "amount":1.00,
        "type":"BOLETO",
        "status":"APPROVED",
        "client":{"id":1},
        "buyer":{   "name":"Miguel",
                    "email":"email@email.com",
                    "cpf":"32014080003"},
        "card":null,
        "boleto":{"id":83,
        "number":"34191790010104355872392553590008878710000100"
        }
    },
]
```


[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/860385e4cdf21b126101)
