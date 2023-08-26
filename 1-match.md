Matches the documents and returns count
```
[
    { 
        $match: { 
            'limit': { 
                    $lte: 5000
                }
            }
    },
    { $count: 'account_id'
    }
]
```
---
Match and project
```
[
  {
    $match:
      {
        limit: {
          $lte: 5000,
        },
      },
  },
  {
    $project:
      {
        account_id: 1,
        _id: 0,
        products: 1,
      },
  },
]
```
---
Match products whose array length is 2
```
[
  {
    $match: {
      products: {
        $size: 2,
      },
    },
  },
  {
    $project: {
      account_id: 1,
      _id: 0,
      products: 1,
    },
  },
]
```
---
Project new field called `productsLength` and match all the documents with products length gt 2
```
[
  {
    $project: {
      account_id: 1,
      _id: 0,
      products: 1,
      productsLength: {
        /* 
            adding new field
        */
        $size: "$products",
      },
    },
  },
  {
    $match: {
      productsLength: {
        $gt: 2,
      },
    },
  },
]
```
---
