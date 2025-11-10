Seems about 11 pages of overhead... Seems I'm aiming for a ballpark of
10k - 20k words.

core sentence: "pgx-lower is a PostgreSQL extension that proves the
architectural feasibility of integrating a modern, MLIR-based execution
engine into a battle-tested system."

# Introduction

* 1-2 paragraphs on the field
* 1-2 paragraphs on the project
* 1 paragraph on challenge: PostgreSQL is a massive 
database, and this is a way to integrate bleeding edge systems into it.
* 1 paragraph on the layout of the writing

# Background

## Fundamentals

### Database background

* What is a typical database structure (system + execution system) (1 paragraph)
* Introduce the problem with this (1 paragraph)
* Briefly mention ACID (1 paragraph)
* CPU vs on-disk measurements (1 pg)

### JIT in Databasing

* What is a compiler/JIT compiler (1 pg)
* Why use JIT (1 pg)
* Types of compilers in databases (1 pg)
* Introduce common compiler infrastructures (2 pg)

### PostgreSQL implementation details

* What are memory contexts
* What are the types of nodes

## Related Works

This is an abridged version of the literature review

* System-R (1 pg)
* HyPer + Umbra (2-3 pg)
* Mutable (1 pg)
* LingoDB (1 pg)
* PostgreSQL's implementation of expressions - the idea, 
the review comments, what went wrong, and the impact of 
this (2-3 pg)

## Aims

* Writing a JIT compiler... hmm... I wonder if this should move to the start 
of methods, but in the marking criteria its in the background so...
* Criticism is that PostgreSQL can be bad for testing an idea because 
there is so much going on in the system (e.g. genetic optimisations)
that how do you standardise your testing? This is a big concern, and should be 
discussed either here or in the discussion. Maybe at least mention it here.

# Method

## Sytem Design

* Discuss tradeoffs: which compiler to use, which database to use, how to implement
the compiler, where to implement the compiler. (2 pgs)
* Make sure to mention that LingoDB uses pg_query, so it's the most applicable
to our usecase (0 pgs, last section)
* Here is where I should slap that diagram of how the system is connected, and 
what will be the focus areas of our implementation. (2 pgs)

## Implementation
> The thesis should be the destination, not the journey!
* LingoDB codebase integration - wrangling the LLVM version up
* Memory boundary 
* Logging infrastructure
* Implementing AST translation pattern. Maybe walk through a couple
of the AST implementations? (5-8 pgs)
* Implementing Runtime defintiions patterns (4 pgs)
* Make sure to mention the viability of passing information through the arena
allocator to simplify parsing. 
* Mention data type challenges (strings, decimals, dates) and nullability (3 pgs)
* Configuring the LLVM JIT compilation settings (1pg)
* Profiling to improve the latency by finding obvious challenges (3 pgs)
* Maybe I should include the dialect, or the dialect changes I made? (2 pgs)

## Launching website

* Worth mentioning so that its easy to demonstrate the project (1pg)

## Benchmarking

* How to ensure the environment is fair... (2pgs)
* Show benchmarks (1pg)
* Say rough conclusion (1pg)
* I'll have to go do multiple runs and include a standard deviation. Probably
just the test sets I made. I don't think its actually that long, but it
kinda crashes sometimes lol. Maybe I can disable some of them then run it like
100x and include a deviation.

## Discussion of results

* Sometimes PostgreSQL wins, sometimes we win (1 pg)
* Its hard to make a fair conclusion here without implementing indexes or
fully doing the implementation (1 pg)

## Future work

* Adding indexes (0.5pg)
* Swapping to wasm; make sure to justify that LingoDB was chosen because
they used pg_query so their structure was at least related already. (0.5pg)
* Doing evaluation with pg_bench or the official postgres tests.

# Conclusion

* Final conclusion
