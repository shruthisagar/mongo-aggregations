# Introduction to Mongo Aggregations

- Mongo Aggregations are one of the powerful features of MongoDB.
- A way of processing a large number of documents in a collection by means of passing them through different stages.
- Theyprocess the data records/documents and return computed results. It collects values from various documents and groups them together and then performs different types of operations on that grouped data like sum, average, minimum, maximum, etc to return a computed result

## Mongo is schema-less, so how to aggregate them?
- By being schema-less, we can easily change the structure in which data is stored. Documents in a collection need not conform to a single rigid structure. The trade-off is that by not having a schema and not validating against that schema, software bugs can creep in. When data is stored in many different ways, application complexity increases. Schema is self-documenting and leads to cleaner code. With sophisticated validations, application code can become simpler.

## Areas where schema could be helpful
- When matching on nested document fields, the order of fields matters.
- Data with a complicated structure is easier to understand and process given the schema.
- When using an Object Document Manager (ODM), the ODM can benefit from the schema.
- Frequent changes to the document structure without a schema can cause performance issues.

## Ways to do Mongo Aggregation

- **Aggregation Pipeline**
    There are multiple operators that are used for aggregation like match, group, addToSet etc. Each operation for an element in the aggregation pipeline. The input of the operation is the output of the previous operation where in the input of the first operation is the whole collection.
    db.getCollection.aggregate([OP1, OP2, OP3,....])

- **Map Reduce Function**
    This is deprecated version as the aggregation pipeline provides better flexibilty and performance.

- **Single purpose aggregation**
    These are the methods from the collection class which includes methods like estimatedDocumentCount(), count(), distinct() which aggregatates from a single collection.

The mongo documents in the above example are sourced from [here](https://github.com/neelabalan/mongodb-sample-dataset)