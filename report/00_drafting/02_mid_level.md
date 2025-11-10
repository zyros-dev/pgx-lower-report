pgx-lower: Bridging Modern Database Compiler Advances With Battle-Tested Database Systems
# Notes (not in thesis)
> The thesis is the destination, not dragging the user through the journey

# Abstract
* pgx-lower is a PostgreSQL extension that proves the architectural feasibility of integrating a modern, MLIR-based compiler execution engine into a battle-tested system.

# Introduction

## 1-2 paragraphs on the field
* Databases are heavily used...
* Modern hardware advances...
* This has resulted in significant research into compilers within databases...
* A problem is that adoption is hard, and a lot of these systems create their databases from scratch. This means they need to concern themselves with MVCC, ACID, and other requirements.
## 1-2 paragraphs on the project
* Postgres's execution engine was replaced with a compiler to show a feasible way for research projects to productionize their research without requiring a new database as well as evidence that it has the potential to be faster than PostgreSQL. Furthermore, we introduce methods to take advantage of PostgreSQL's memory context system to simplify runtime functions within this.
> pgx-lower is a PostgreSQL extension that proves the architectural feasibility of integrating a modern, MLIR-based compiler execution engine into a battle-tested system.
## 1 paragraph on challenge: PostgreSQL is a massive system
* A major potential issue with this is PostgreSQL
## 1 paragraph on the layout of the writing
* In chapter xyz we ...

# Background

## Fundamentals

### Database background

#### What is a typical database structure (system + execution system) (1 paragraph)
* Majority of databases are structured like this figure, SQL is parsed, turned into RA, optimized, executed, then materialized into a table. 
* This execution engine runs using the volcano model, where the plan tree is traversed by calling produce() on the root node, which calls the children, until it calls a leaf which calls consume() on itself, and this calls the parent's consume function, carrying the result up. When it arrives at the root again, it can be materialized.
#### Introduce the problem with this (1 paragraph)
* The issue with this is that this model moves one tuple at a time, severely underutilising the CPU cache. Broadly speaking, the two solutions proposed for this is vectorising the results or compiling the queries. Vectorised results is when groups of tuples are carried up, but it encounters challenges when a node can make the result large (such as a join). Alternatively, a compiler can be introduced which can take advantage of classical optimisations for this problem.
#### CPU vs on-disk measurements (1 pg)
* In the previous work, this CPU time was found to take between 34% - 75% of the runtime. This shows the potential for optimisation; if the system is perfectly optimised, we would see that drop to 0%.
#### Briefly mention ACID (1 paragraph)
* Databases are also heavily reliant on ACID, MVCC and OLTP vs OLAP...

### JIT in Databasing

#### What is a compiler/JIT compiler (1 pg)
* A just in time compiler functions by having multiple layers of compilation and are mostly used by interpreted languages to... (this is already written)
#### Why use JIT (1 pg)
* JIT compiles fast...
* JIT uses branch-prediction which can make it faster than traditional compilers...
#### Types of compilers in databases (1 pg)
* QEP vs EXP...
* This is usually fast in OLAP-style database and queries that heavily use expressions in their queries.
#### Introduce common compiler infrastructures (2 pg)
* LLVM and MLIR
* TODO: Introduce other popular compiler toolchains...
#### Most of these compilers are in-memory, which limits the benchmarking options compared to production databases.
* The choice to exclude majority of other compiler things was because majority of them are in-memory, and as a result their latency is significantly better. This was illustrated in xyz, where it was found that PostgreSQL runs abc times slower... This means that it isn't a fair comparison to compare these compilers to our system.

### PostgreSQL implementation details

#### What are memory contexts
* An arena allocator allows you to create an object used to make allocations, and when the arena allocator is freed, all of the objects inside are freed. An extension of this is the memory context model in PostgreSQL, where there is a root memory context, you can spawn child contexts, and if a context is freed, all of its children are also freed. 
#### What are the types of nodes
* Typically these plan trees can be defined by two types of nodes, plans and expressions. Plans consist of routines such as sequential scan, index scan, aggregations, while expressions define operations with a clear single output, such as addition, subtraction, and more. This is important to understand as a number of these optimisations are applied to specific types, and it affects the pattern of the AST parser.

## Related Works

This is an abridged version of the literature review

### System-R (1 pg)
* System R is an interesting case because it was the paper that... (this can basically
be copied from the literature review...)
### HyPer + Umbra (2-3 pg)
* Same as lit, but shorter
### Mutable (1 pg)
* Same as lit, but shorter
### LingoDB (1 pg)
* Same as lit, but shorter
* Make sure to mention its structure: AST translation, relalg, db dialect, etc
### PostgreSQL's implementation of expressions - the idea, the review comments, what went wrong, and the impact of this (2-3 pg)
* Same as lit, but shorter
### Benchmark summary
* Make sure to mention that most of these research systems seem to skip index implementation, which will impact comparing them to our systems...
* Include my literature review's benchmarks here to compare these systems... do a comparison of their performance...

## Aims

## Writing a JIT compiler... hmm... I wonder if this should move to the start of methods, but in the marking criteria its in the background so...
## Criticism is that PostgreSQL can be bad for testing an idea because there is so much going on in the system (e.g. genetic optimisations) that how do you standardise your testing? This is a big concern, and should be discussed either here or in the discussion. Maybe at least mention it here.
* Tying this together, this piece aims to integrate a research compiler within an established database system. This shows that rather than requiring to recreate a database and redefine specifics (query optimisation, ACID, ...), these new execution models can be applied within a battle-tested system. 
* This means these papers that implement compilers can productionize and make their systems broadly available to existing databases.
> TODO: This part is kind of a mess. I'm talking about how it "might" overtake postgres, maybe I just need to mention that these compiled engines are faster, but improvements are required for it to properly overtake postgres. And the benchmarks validate that this is possible.
* Furthermore, a key output is proving that a system can be within the same order of magnitude as the target system. This validates optimisations can be done to the point that it becomes faster than PostgreSQL, directly. To do this, TPC-H benchmarks will be used as majority of the reviewed papers utilised them to show their benchmarks...
* One concern is that these databases are a large system, so it might be unfair for benchmarking and it's very challenging as a result. This will be combatted by running larger queries... Also, a primary goal of this type of research should be to improve production systems.
* Furthermore, an appeal is if the high level dialect is standardised then it could be easier to do research on the compiler alone. For instance, if you make a compiler on your own and target the same high level language, you would be able to integrate it with this plugin very easily.
* It would be ideal if we show the database can function end-to-end to maintain its ACID properties, even if the extension fails. This encourages adoption of the extension, as it is something that might improve the performance, but will not cause failures.

# Method
* Small intro - mention the core message of the thesis again...
> pgx-lower is a PostgreSQL extension that proves the architectural feasibility of integrating a modern, MLIR-based compiler execution engine into a battle-tested system.

## Design

### Discuss tradeoffs: which compiler to use, which database to use, how to implement the compiler, where to implement the compiler. (2 pgs)
* The first decision to make is which database and which compiler to use. We require something has a strong extension support, has wide-spread usage, is already high performance, and has a volcano execution model. For the compiler, it would be nice if their interface already closely matches our target database and displays promising results in performance. 
* As a result, PostgreSQL and LingoDB were chosen. PostgreSQL offers strong support for extensions, and it has support for overriding its execution engine using its hooks. An example of this is Tiger Data, who created a full time-series database (maybe need citation, or move this to intro?). LingoDB uses `pg_query` during its initial parsing, is new, and has promising results. The primary challenge with it is that its a columnar and in-memory database, so it will require adjustments. Furthermore, LingoDB does not support indexes...
### Make sure to mention that LingoDB uses pg_query, so it's the most applicable to our usecase (0 pgs, last section)
### Here is where I should slap that diagram of how the system is connected, and what will be the focus areas of our implementation. (2 pgs)
* The design that was chosen looks like X. We use the PostgreSQL runtime hooks at Y to integrate, then we can have a module. This is where the LingoDB compiler will sit. We will have to make adjustments to the compiler itself because of some architectural and type differences, but this is expected to be much lower than other databases.
* The other challenge that was encountered was `pg_query` hands the query tree to LingoDB, not the plan tree. This query tree is harder to parse, but also allows us to rely more on the database's existing optimisations.
* We also need a testing framework, which `pg_regress` can provide. With this, we can create a set of tests to support the progressive implementation of nodes with the final target being all of the TPC-H queries. This requires 18/40 of the plan nodes to be implemented, and x/y of the execution nodes...   

## Implementation
> The thesis should be the destination, not the journey!
### Integrating Systems
* To connect LingoDB through PostgreSQL requires request to pass from PostgreSQL's bindings, through to C++, then through the LingoDB to parse the data, and back to PostgreSQL for display. A template repository for integrating PostgreSQL with C++ was used, cppgres (citation), and the extension hook (here) was used. This extension also enabled pg_regress to be used to provide rails for implementation by doing integration test driven development.
### LingoDB codebase integration - wrangling the LLVM version up
* In implementation, several adjustments had to be made to LingoDB. Firstly, a simplified version of LingoDB was used, xyz version, because the later versions contain unrequired features that would make implementation more challenging. Secondly, the LLVM version was upgraded to 20.1.5, which was the newest at the time. This required going through LingoDB and upgrading the syntax.
* This also required changes to the dialects... (include table of dialects)
### Logging infrastructure
* With the compiler running through multiple phases, a custom logger was created to support this. PGX_LOG is a two layer logging macro, where the first argument is the level (INFO, WARN, ERROR), and the second is the layer it is in (AST, RELALG_LOWER, ...). This enables debugging to target and isolate specific layers, and reduces log noise when running large queries. 
### Ensuring safety
* A PG_TRY and PG_CATCH pattern was used so that any runtime errors will cause the system to roll back to Postgres, but more ideally the query analyzer rejects it early... However, extensive testing was not done on this so it is possible for this to segfault and still fail at this stage...
### Implementing AST translation pattern. Maybe walk through a couple of the AST implementations? (5-8 pgs)
* The majority of the work is in the plan tree translation to relational algebra...
* Our proposed design is a recursive descent parser, and our goal is to encourage  type-safety and performance. As a result, each implementation typically uses the pattern of pushing context downwards, then returning results upwards in translation results...
* Each function typically follows the pattern of translating the children of the node, then defining what the node means within our own context, writing the relalg into the op builder, then creating a translation result.
* To do this, a query context and translation result were made. The context typically contains... 
* To pass parameters the context...
* An example plan node translation is...
* An example execution node translation is...
* The list of implemented nodes are:
### Implementing Runtime defintiions patterns (4 pgs)
* The other side of this is the runtime definitions which are used to support complex algorithms and add support for a link back to postgresql...
* The core one for this is the link to pass tuples through to the MLIR... this needs to support translating the data types when its requested...
* We also implemented the sort and hash map APIs, which was required due to disk spillage. The sort API looks like... the hash API looks like...
* For the sort API...
### Make sure to mention the viability of passing information through the arena allocator to simplify parsing. 
* A key component that was taken advantage of here was the memory contexts. Within a runtime definition, if we need to allocate objects we can create a memory context at the start of the object creation (e.g. iterator creation), then at the end free it. These compilers are unique because they are not running standalone, they're running inside of another system. As such, you can take advantage of things the outer system provides.
* Furthermore, LingoDB tended to put JSON objects directly in the compiled code, however, with memory contexts you can allocate specifications on the TransactionContext and put the pointer into your code instead. This means less time is spent on parsing, the code that needs to be optimised is lighter, ...
### Mention data type challenges (strings, decimals, dates) and nullability (3 pgs)
* Several challenges were caused with data types because PostgreSQL and LingoDB use fundamentally different data type systems. This is bounded to its representations of dates, strings, decimals, and its nullability.
* For dates, the core challenge is the months field. Ideally the representation for this would be a struct with a dedicated field, but the majority of LingoDB has assumed that date types are simply integers. A compromise was made here to use the average microseconds in a month... Furthermore, PostgreSQL supports a large number of different date systems...
* With decimals and strings, a core challenge is that these are dynamic structures in PostgreSQL. Strings in PostgreSQL were consolidated to only one data type and that was fine, but with decimals they were represented as i128. As a result, the maximum precision in practice is <32, 6>.
* When it comes to nullability, PostgreSQL and LingoDB have a different method of packing their tuples, so this required a number of adjustments...
### Configuring the LLVM JIT compilation settings (1pg)
* Majority of online advice around the LLVM compiler recommends not digging through compiler flags and simply using the O2 adjustment. However, we want to use the JIT compiler so then we...
### Profiling to find the characteristics of performance
* To support profiling, magic trace was used to isolate obvious performance issues. Magic trace is... (todo: this should move to background)...
* Figure xyz is an example of a chart from magic trace before optimisation... 
* We found that tuples columns data types were beingg read too often resulting in too many table open/closes, and LingoDB's optimiser was overriding PostgreSQL's choices resulting in a NestLoop. Both of these were delt with.

## Launching website

### Worth mentioning so that its easy to demonstrate the project (1pg)
* Due to installing the extension being challenging, a website was launched at... The code is published at... This was done with a docker container...

## Benchmarking

### How to ensure the environment is fair... (2pgs)
* In the introduction, it was defined that the target benchmark will be TPC-H. A core concern is that PostgreSQL is a large database system, so there are a lot of variables that can cause poor measurements. To address this, XYZ runs were done in total, and graphs were produced. Furthermore, both were hosted inside of a docker container, and ran on xyz hardware...
* One other consideration is the LingoDB did not have support for index scans, so this...
### Show benchmarks (1pg)

## Discussion of results

### Sometimes PostgreSQL wins, sometimes we win (1 pg)
* If you look at query xyz... however... If these queries were enabled, they'd run on the magnitude of hours... This means across the queries, xyz% are slower, abc% are faster, and the difference is on average ijk%
* We measure genuine speedups in the heavy analytical queries, validating the research direction, however, the overhead and smaller optimisations dominates on the smaller queries.
### however, we can look at the profiling
* We can find the root cause of this by looking at profiling graphs... (show some profiling flame charts of the most expensive queries)
* We can see there is still work to be done with reading the tuples, and most of the runtime sits inside of C++, not the LLVM... however, the compiler still adds abc milliseconds of overhead...
* Furthermore, JIT lowering do not seem to trigger... This may be because...
### Its hard to make a fair conclusion here without implementing indexes or fully doing the implementation (1 pg)
* A fair benchmark across these queries require implementing indexes.

## Future work

### Adding indexes (0.5pg)
* First and foremost, the main improvement to improve benchmarks is indexes. LingoDB's implementation of nest loop joins precalculates the inner table into a vector first, then uses it for the join which means a new type of join needs to be introduced. Furthermore, the way these parameters flow through requires an abnormal pattern where the consume() function from the outer child needs to invoke the consume() function of the inner child, and pass parameters through. This is significant implementation effort. 
* However, it is appealing to target a different architecture. LingoDB's target was to make the optimisations transparent and do them within the compiler using MLIR layers, but in our case PostgreSQL does the optimisations for us. As stated in chapter xyz, LingoDB was appealing because of their usage of pg_query. An appealing compiler to target for this is a WebAssembly one, because it has the fastest JIT startup time, and using a stricter language such as Rust or Ocaml would promote correctness. However, it's important to still advocate for an easy to target high level language. If there is a standard interface for the compiler, it means it will be easy to reuse the runtime specifications and that initial plan tree parsing for future research.
* Another further work is improving the correctness with more testing and tuning the performance. PostgreSQL provides pg_bench and a large integration suite of tests. If these are used then it can be shown to be safe and ACID properties are maintained. Furthermore, there is work to be done in the query analyzer. Methods such as gradient descent could be utilised to optimise when to use the compiler based on the cost metrics PostgreSQL gives... Other performance improvements can be found with the runtime functions and JIT tuning.
* The system can also be extended further to more general PostgreSQL nodes, like the WINDOW node, ... this will enable a complete comparison...

# Conclusion

### Final conclusion
> pgx-lower is a PostgreSQL extension that proves the architectural feasibility of integrating a modern, MLIR-based compiler execution engine into a battle-tested system.
* In this thesis... this showed... blah blah
