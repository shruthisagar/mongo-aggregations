Sorts documents by certain fields
```
[
  {
    $sort: {
      account_id: -1
    }
  }
]
```
---
Sort multiple fields
```
[
  {
    $sort: {
      account_id: 1,
      limit:1
    }
  }
]
```
---
Sort by array length
```
[
  {
    $addFields: {
      productsLength: {
        $size: "$products",
      },
    },
  },
  {
    $sort:
      {
        productsLength: -1,
      },
  },
]
```
---
Group and sort
```
[
  {
    $group: {
      _id: "$account_id",
    },
  },
  {
    $sort: {
      _id: -1,
    },
  },
]
```