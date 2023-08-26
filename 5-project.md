1: add, 0 don't project:
newField:{
    `<expression>`
}
```
[
  {
    $project: {
      account_id: 1,
      _id: 0,
      products: 1,
      totalProducts: {
        $size: "$products",
      },
    },
  },
  
]
```
---

Adding Embedded fields
// sample_mflix.movies
```
[
  {
    $project:
      {
        title: 1,
        year: 1,
        tomatoes_critic_rating:
          "$tomatoes.critic.rating",
      },
  },
]
```
---

Also can be used to rename fields
```
[
  {
    $project: {
      account_id: 1,
      _id: 0,
      obj_id: "$_id",
      products: 1,
      totalProducts: {
        $size: "$products",
      },
    },
  },
  
]
```