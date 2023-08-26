Limit to 1 document
```
[
  {
    $limit:1
  }
]
```
---
Can be used in pagination along with skip. Here we are using skip, regex match, along with skip  and limit
```
[
  {
    $skip:
      100,
  },
  {
    $limit:
      100,
  },
  {
    $match:
      {
        email: {
          $regex: "gmail.com",
          $options: "i",
        },
      },
  },
  {
    $sort:
      {
        _id: 1,
      },
  },
]
```
