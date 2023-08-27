Joining of two collections - time consuming.
Also added new operator `$arrayElemAt` in `$project` field.
Collection: sample_analytics.transactions
```
[
  {
    $lookup:
      {
        from: "accounts",
        localField: "account_id",
        foreignField: "account_id",
        as: "account_details",
      },
  },
  {
    $project:
      {
        account_id: 1,
        transaction_count: 1,
        account_details: {
          $arrayElemAt: ["$account_details", 0],
        },
      },
  },
]
```
The above lookup is similar to the following psuedocode in SQL
```
SELECT tr.account_id, ac.*, tr.transaction_count from transaction tr
join accounts ac on tr.account_id=ac.account_id
```
