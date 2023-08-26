Group by account_id, each document will have only account_id, which is grouped
```
[
  {
    $group: {
      _id: "$account_id",
    },
  },
]
```
---
Groups by multiple fields 
```[
  {
    $group: {
      _id: {
        limit: "$limit",
        account_id: "$account_id",
      },
    },
  },
]
```
---
Group by Nested Fields
//sample_mflix.movies
```
[
  {
    $group:
      {
        _id: "$imdb.rating",
      },
  },
]
```
---
Match and group
```
[
  {
    $match:
      {
        limit: {
          $gte: 2000,
        },
      },
  },
  {
    $group:
      {
        _id: "$account_id"
      },
  },
]
```
Match, unwind array, group and add fields
```
[
  {
    $match: {
      limit: {
        $gte: 5000,
      },
    },
  },
  {
    $unwind:
      {
        path: "$products",
      },
  },
  {
    $group: {
      _id: "$account_id",
      products: {
        $push: "$products",
      },
    },
  },
]
```