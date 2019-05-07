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
{
    "PaymentsRecords": [
        {
            "boleto": [],
            "card": [
                {
                    "cvc": 1213,
                    "month": 7,
                    "number": "4444333322221111",
                    "year": 2042
                }
            ],
            "cpf": "11555134609",
            "email": "renato@email.com",
            "name": "Renato Almeida",
            "payment": [
                {
                    "amount": 90.5,
                    "type": "credit_card",
                    "u_id": "f49d656b-710d-11e9-ad10-685b357c6685"
                }
            ]
        },
        {
            "boleto": [
                {
                    "number": "514063144412920996301392351456658136409509526996"
                }
            ],
            "card": [],
            "cpf": "33723404855",
            "email": "dustydrums@strokes.com",
            "name": "Julian Casablancas",
            "payment": [
                {
                    "amount": 254.37,
                    "type": "boleto",
                    "u_id": "e6356526-7110-11e9-877e-685b357c6685"
                }
            ]
        }
    ]
}       
}...
```


## Registering a new Payment

**Definition**

`POST /payments`

**Arguments:**

- `"amount:float` the payment amount
- `"type:string`   payment that can be either boleto or credit card.
- `"status:string` the payment can approved, pending or declined.
- `"client":string` a globally unique identifier for the client
- `"buyer": ` nesting buyer information
  - `"name":string` buyer name
  - `"email": string` buyer email address
  - `"cpf": string` buyer social security number (CPF)
- `"card"`: nesting credit card information
  - `"card_holderName": string` Cardholder's name
  - `"card_number": string` Credit Card number
  - `"card_expDate": string` Credit Card Expiry date
  - `"card_cvv": string` Credit Card Verification Value

### Request for Credit Card Payment
**Request**
```json
{
    "client": {
        "id": 1
    },
    "buyer": {
        "name": "Julian Casablancas",
        "email": "dustydrums@strokes.com",
        "cpf": 33723404855
    },
    "payment": {
        "amount": 254.37,
        "type": "boleto",
        "card": {
            "cardNumber": "",
            "holderName": "",
            "month": "",
            "year": "",
            "cvv": ""
        }
    }
}
```


### Response for Credit Card Payment

**Response:**

- `201 Created` on success

```json
{
    "response": "Payment added successfuly!",
    "status": "Approved"
}
```

### Response for Boleto Payment

**Response:**

- `201 Created` on success

```json
{   "boleto":
        {
        "boleto_number":"288881905123923272040005888782304971646982007844"
        }
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
    "PaymentsRecords": [
        {
            "boleto": [
                {
                    "number": "514063144412920996301392351456658136409509526996"
                }
            ],
            "card": [],
            "cpf": "33723404855",
            "email": "dustydrums@strokes.com",
            "name": "Julian Casablancas",
            "payment": [
                {
                    "amount": 254.37,
                    "type": "boleto",
                    "u_id": "e6356526-7110-11e9-877e-685b357c6685"
                }
            ]
        }
    ]
}
```

### Response for Credit Card Payment

- `200 OK` on success

```json
{
"PaymentsRecords": [
    {   
        "boleto": [],
        "card": [
            {
                "cvc": 1213,
                "month": 7,
                "number": "4444333322221111",
                "year": 2042
            }
        ],
        "cpf": "11555134609",
        "email": "renato@email.com",
        "name": "Renato Almeida",
        "payment": [
            {
                "amount": 90.5,
                "type": "credit_card",
                "u_id": "f49d656b-710d-11e9-ad10-685b357c6685"
            }
        ]
    }
    ]
}
```


[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/860385e4cdf21b126101)
