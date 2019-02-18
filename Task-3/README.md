# Task-2

### Made by David Carl & Tjalfe Møller
### www.dcarl.me


## Last weeks Task

[See the answer here!](Task-2.md)

## This weeks Task
Model | Atomicity | Sharding |Indexes |Large Number of Collections | Collection Contains Large Number of Small Documents
----|:----:|:----:|:----:|:----:|:----:
| Arrays of Ancestors  |X|   | X  | X  |   |
|  Materialized paths |   |  X |   | X  |  X |
|  Nested sets |  X | X  | X  |   |   |


### Arguments

#### - Arrays of Ancestors
- Atomicity
    - When you insert into the collection only a single document is changed or created.
- Indexes
    - Its possible to index parents on the document. 
- Large Number of Collections
    - You need to refer each document to their parent (_all_ ancestor), so you that way around get a large collection.

See for more info https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-ancestors-array/

#### - Materialized paths
- Sharding
    - Since you can get partial path to the desired document.
- Large Number of Collections
    - The path is still stored in each document that is created.
- Collection Contains Large Number of Small Documents
    - Since there are multiple smaller ones instead of one big document you get many small documents.

see for more info https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-materialized-paths

#### - Nested sets
- Atomicity
    - Since, when you are adding to the collection only the current document is crated or changed.
- Sharding
    - Still possible to shard the different categories.
- Indexes
    - Its still possible to add indexes to the different categories.
    
See for more info https://docs.mongodb.com/manual/tutorial/model-tree-structures-with-nested-sets/
