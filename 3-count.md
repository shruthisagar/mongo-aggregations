All documents count
```
[
  {
    $count: 'allDocuments'
  }
]
```
---
Group and count
gives distinct count of unique accounts
```
[
  {
    $group:
      {
        _id: "$account_id",
      },
  },
  {
    $count:
      "total",
  },
]
```
---
Match group and count
```
[
  {
    $match:
      {
        limit: {
          $gte: 9000,
        },
      },
  },
  {
    $group:
      {
        _id: "$account_id"
      },
  },
  {
    $count: 'count'
  }
]
```