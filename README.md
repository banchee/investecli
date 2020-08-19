# investecli
A Simple Python CLI tool for viewing your Investec Bank account details on the terminal

# Getting started

> Make sure you have python3.7 or higher install on your machine.

1. Clone the repo to your machine

```
$ git clone git@github.com:banchee/investecli.git
```

2. Open your terminal, and navigate to directory of the project

```
$ cd investecli
```

3. Next build the project locally

```
$ pip install -e .
```

4. Create a investecli credentials file that will be needed to access your account information

```
$ echo '{"client_id": "xxxxxxxx", "client_secret": "xxxxxx"}' > ~/.investecli/credentials

```

# Using the CLI

## Login

To use the CLI, you will first need to login and retrieve a token with an expiry date. This will append to the `~/.investecli/credentials` file the token returned and the token type.

```
$ investecli login
```

## Accounts

Once you have logged in, you are now able to query your accounts to get the ID needed to view balances and transactions.

```
$ investecli accounts


                 accountId |   accountNumber | accountName   | referenceName   | productName
---------------------------+-----------------+---------------+-----------------+-------------------------
 XXXXXXXXXXXXXXXXXXXXXXXX1 |     xxxxxxxxxxx | Mr E Xample   | Mr E Xample     | Private Bank Account
 XXXXXXXXXXXXXXXXXXXXXXXX2 |   xxxxxxxxxxxxx | Mr E Xample   | Mr E Xample     | Cash Management Account

```

## Balances

You can now use the `accountId` to find out the balance in your account

```
$ investecli balance --account_id=XXXXXXXXXXXXXXXXXXXXXXXX1

                 accountId |   currentBalance |   availableBalance | currency
---------------------------+------------------+--------------------+------------
 XXXXXXXXXXXXXXXXXXXXXXXX1 |          10000.0 |            10000.0 | ZAR
```

## Transactions

You can now use the `accountId` to see the transcation on your account

```
$ investecli transactions --account_id=XXXXXXXXXXXXXXXXXXXXXXXX1

                 accountId | type   | status   | description                            | cardNumber       | postingDate   | valueDate   | actionDate   | transactionDate   |   amount
---------------------------+--------+----------+----------------------------------------+------------------+---------------+-------------+--------------+-------------------+----------
 XXXXXXXXXXXXXXXXXXXXXXXX1 | DEBIT  | POSTED   | WOOLWORTHS COBBLE WALK DURBANVILLE ZA  | xxxxxxxxxxxxxxxx | 2020-08-10    | 2020-08-31  | 2020-08-19   | 2020-08-08        |   600
 XXXXXXXXXXXXXXXXXXXXXXXX1 | DEBIT  | POSTED   | WOOLWORTHS COBBLE WALK DURBANVILLE ZA  | xxxxxxxxxxxxxxxx | 2020-08-08    | 2020-08-07  | 2020-08-19   | 2020-08-07        |   600
 XXXXXXXXXXXXXXXXXXXXXXXX1 | DEBIT  | POSTED   | WOOLWORTHS COBBLE WALK DURBANVILLE ZA  |                  | 2020-08-06    | 2020-08-06  | 2020-08-19   | 2020-08-06        |   600
 XXXXXXXXXXXXXXXXXXXXXXXX1 | DEBIT  | POSTED   | WOOLWORTHS COBBLE WALK DURBANVILLE ZA  |                  | 2020-08-05    | 2020-08-05  | 2020-08-19   | 2020-08-05        |   600
 XXXXXXXXXXXXXXXXXXXXXXXX1 | DEBIT  | POSTED   | WOOLWORTHS COBBLE WALK DURBANVILLE ZA  | xxxxxxxxxxxxxxxx | 2020-08-04    | 2020-08-31  | 2020-08-19   | 2020-08-02        |   600
 XXXXXXXXXXXXXXXXXXXXXXXX1 | DEBIT  | POSTED   | WOOLWORTHS COBBLE WALK DURBANVILLE ZA  |                  | 2020-08-03    | 2020-08-03  | 2020-08-19   | 2020-08-03        |   600
 ...
 ...
```
