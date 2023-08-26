$sum, $avg, $max, $min



sample_analytics.transactions

```
[
  {
    $limit:
      1,
  },
  {
    $unwind:
      {
        path: "$transactions",
      },
  },
  {
    $project:
      {
        sum: {
          $sum: "$transactions.amount",
        },
        transactions: 1,
      },
  },
  {
    $group:
      {
        _id: "$_id",
        sum: {
          $sum: "$sum",
        },
        max: {
          $max: "$sum",
        },
        avg: {
          $avg: "$sum",
        },
        count: {
          $sum:1
        }
      },
  },
]
```