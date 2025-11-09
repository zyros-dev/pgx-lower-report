Seems about 11 pages of overhead... Seems I'm aiming for a ballpark of
10k - 20k words.

core sentence: "pgx-lower is a PostgreSQL extension that proves the
architectural feasibility of integrating a modern, MLIR-based execution
engine into a battle-tested system."

# Introduction

1-2 pages of an overview - this seems very standard across different theses.

* 1-2 paragraphs on the field
* 1-2 paragraphs on the project
* 1 paragraph on the layout of the writing

# Background

## Fundamental knowledge and definitions

### Database background

* What is a typical database structure (system + execution system)
* Introduce the problem with this
* Briefly mention ACID
* CPU vs on-disk measurements

### JIT in Databasing

* What is a compiler/JIT compiler
* Why use JIT
* Types of compilers in databases
* Introduce common compiler infrastructures

## Existing research

This is an abridged version of the literature review

* System-R
* HyPer + Umbra
* Mutable
* LingoDB
* PostgreSQL's implementation of expressions

## Goals

* Writing a JIT compiler...

# Method

## Design

* Discuss tradeoffs
* Make sure to mention that LingoDB uses pg_query, so it's the most applicable
to our usecase
* Here is where I should slap that diagram of how the system is connected
* Make sure to mention the viability of passing information through the arena
allocator to simplify parsing.

## Implementation

* LingoDB codebase integration - wrangling the LLVM version up
* Implementing AST translation pattern. Maybe walk through a couple
of the AST implementations?
* Implementing Runtime defintiions patterns
* Mention data type challenges and nullability
* Configuring the LLVM JIT compilation settings
* Profiling to improve the latency by finding obvious challenges
* Maybe I should include the dialect, or the dialect changes I made?

## Benchmarking

* How to ensure the environment is fair...
* Show benchmarks
* Say rough conclusion
* I'll have to go do multiple runs and include a standard deviation. Probably
just the test sets I made. I don't think its actually that long, but it
kinda crashes sometimes lol. Maybe I can disable some of them then run it like
100x and include a deviation.

## Discussion of results

* Sometimes PostgreSQL wins, sometimes we win
* Its hard to make a fair conclusion here without implementing indexes or
fully doing the implementation

## Future work

* Adding indexes
* Swapping to wasm; make sure to justify that LingoDB was chosen because
they used pg_query so their structure was at least related already.

# Conclusion

* Final conclusion
