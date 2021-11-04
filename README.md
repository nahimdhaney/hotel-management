
# Booking API

El proyecto siguiente está desarrollado con Django y Django rest Framework.

Básicamente es una API donde yo puedo gestionar reservas de habitaciones de un hotel.

A continuación los diferentes EndPoints:


![Logo](https://4.imimg.com/data4/VC/PG/MY-28015217/hotel-api-integration-250x250.png)


## API Reference

#### Post Client
Servicio simple donde el cliente pueda hacer login.

```http
  POST v1/api/bookings/clients

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | - |

Body Example

```
{
    "nit":"12345439",
    "comercial_name":"José Osinaga",
    "invoice_name":"Monterrey",
    "email"="jose@hotmail.com"
}
```


#### Get Client
Obtiene los clientes registrados

```http
  GET v1/api/bookings/clients
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | - |



#### Post Room
Registro de habitaciones.

```http
  POST v1/api/bookings/rooms

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | - |

Body Example

```
{
    "number":"A3",
    "price":65
}
```

#### Get Rooms
Obtiene las habitaciones registrados

```http
  GET v1/api/bookings/rooms
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | - |




#### Post Booking
Registro de reserva por parte del cliente.

*IMPORTANTE*

Un cliente puede reservar varias habitaciones desde una fecha determinada a otra fecha determinada.
cada reserva puede tener su propia fecha.

```http
  POST v1/api/bookings/bookings
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | - |

Body Example

```
{
    "client":1,
    "rooms":[
        {
            "room":3,
            "inicial_date":"2021-11-08",
            "final_date":"2021-11-08"
        },
        {
            "room":2,
            "inicial_date":"2021-11-10",
            "final_date":"2021-11-15"
        }    
    ]
}
```

#### Get Bookings
Obtiene las habitaciones registrados.

Opcionalmente se puede digitar el nro para buscarlo en el path.

```http
  GET v1/api/bookings/bookings/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Not Required**. Id de la reserva |



#### Patch Bookings
Modifica el status de la reserva.

```http
  PATCH v1/api/bookings/bookings/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id de la reserva |

Body Example

```
{
    "status":2
}
```

#### Get Availables Rooms
Obtiene las habitaciones que el usuario puede registrar según la fecha dada.
Identifica cuales y cuantas habitaciones puedo reservar.
```http
  GET v1/api/bookings/bookings/
```

| QueryParam | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `inicial_date`| `date` | **Required**. fecha inicial de consulta |
| `final_date`| `date` | **Required**. fecha final de consulta |



#### Post Payments
Registro de pagos.

```http
  POST v1/api/bookings/payments

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | - |

Body Example

```
{
    "number":"1",
    "booking":2,
    "status":1,
    "method":1,
    "date":"2021-11-03",
    "amount":50.05
}
```

#### Get Payments
Obtiene los pagos registradas

```http
  GET v1/api/bookings/payments
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | - |


#### Post Invoices
Registro de facturas.

```http
  POST v1/api/bookings/invoices

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | - |

Body Example

```
{
    "nit":"12345439",
    "booking":2,
    "status":1,
    "name":"Nahim Terrazas",
    "number":"1",
    "auth_number":"213431342304030",
    "code_control":"2K-5F-D2-5F",
    "discount":0,
    "total":50.05,
    "date":"2021-11-03"
}
```

#### Get Invoices
Obtiene los pagos invoices

```http
  GET v1/api/bookings/payments
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | - | - |



## Installation

Install python

Install pip

Install hotel-management with pip

```bash
  pip install requirements.txt
```


## Running Tests

To run tests, run the following command

```bash
  py manage.py test
```



## Run Locally

Clone the project

```bash
  git clone https://github.com/nahimdhaney/hotel-management.git
```

Go to the project directory

```bash
  cd hotel-management
```

Install packages

```bash
  pip install requirements.txt
```

Migrations and migrate

```bash
  py manage.py makemigrations
  py manage.py migrate
```


Start the server

```bash
  py manage.py runserver
```

## Authors

- [@nahimdhaney](https://www.github.com/nahimdhaney)

