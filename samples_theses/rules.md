https://gernot-heiser.org/style-guide.html
https://gernot-heiser.org/benchmarking-crimes.html


Tips and Guidance for Students and ECRs Writing Papers and Reports
Gernot Heiser
Contents
Introduction
General Advice on Technical Writing
About (Honours) Thesis Writing
General Advice
Structure and Coherence
About Paper Writing
Paper vs thesis
General rules
Expectations on systems papers
Structure
Formatting
Some Things People Frequently Get Wrong
Microsoft Word
Some TeXniques
Auxiliary Material
My talk on paper writing
On evaluation and benchmarking
A nice example
Introduction
This document originally grew out of frustration of having to fight my way through poorly written thesis and paper drafts, and was targeted at my own students. It developed (mostly grew) over time as I found new issues to address.

In the meantime, externals seem to use it too. I have consequently started to make it less specific to my own students, in the hope that more people benefit from the (accumulated over time) significant effort that went into this. Please send me feedback if you find any errors or have suggestions for improvements.

I get to read a fair amount of student prose, and the quality is highly variable, and some of it everything but a pleasure to read. In fact, some of it is very poorly written. Sometimes it's an early draft (where somehow the author thinks things will magically improve later), sometimes it is even a final (submitted) version of an undergraduate thesis.

I also do a lot of reviewing, mostly as a member of program committees of conferences. And sadly, some of those papers submitted for publication are not much better than drafts my students give me to read.

Such poor writing is annoying and counter-productive:

I'm wasting my time correcting stuff students should be doing themselves. My time would be better used commenting about the technical contents. But they are often hard to get to in a poor manuscript.
Maybe I read the thing carefully even if it's poorly written, maybe not. Most wouldn't. I certainly wouldn't if it came from somewhere else.
If a paper submitted to a conference is poorly written, this will reduce its chance of acceptance, like it or not. But it's also costing me (as your supervisor, or as a reviewer) extra time and effort, so I'd be much happier if all submissions were written well.
Poor written communication skills will most likely impede your career, whether you'll be working in industry or academia. Hence it's important to do something about it while there is still time:
Maybe you're just too lazy to do a proper job. In this case you're really saying that you consider your time more valuable than mine. I don't agree, and it'll cost you.
Maybe you have a real communication problem. In this case it is important that you realise this, and that you do something about it. Get professional help, communication skills are important for your future! There are places on your campus which can help you.
I've written up some general hints on technical writing, followed by more specific guidelines aimed at students writing their thesis. (This is mostly aimed at undergraduate thesis students, although I've assessed PhD theses which got a lot of the same things wrong, so PhD students may find this useful too.) I separately discuss writing conference papers.

Finally there is a section listing style and grammar issues I encounter most frequently in student prose, and some guidelines on how to do better. However, there is much more to get wrong, and I recommend getting a good style book. I generally follow:

Pam Peters. The Cambridge Australian English Style Guide. Cambridge University Press, 1995.
This describes the “official” rules in place in Australia (as far as there is such a thing). It often isn't specific enough for the purposes of technical prose. The following is an excellent book, geared towards folks like us. The author knows computing jargon, and knows her nerds:

Lyn Dupré. Bugs in writing: A Guide to Debugging Your Prose. Addison-Wesley, 1995
This book's main drawback is that it uses American rules, which are some times conflicting with Australian/British rules. She follows the official American rules to the dot, including where no-one else does, and occasionally produces bizarre results. The book is nevertheless very useful.

It is acceptable to use American rules (for papers), but only if you use them consistently. That means using all American spelling as well as grammar and style rules. Don't mix!

An interesting case is program vs. programme. The former is American while the latter used to be the British (and Australian) spelling. However, the Macquarie Dictionary since at least the beginning of the century considers program the correct spelling for all cases (not only computer programs), while the OED treats both equally. Facit: use program.

Another good (although highly incomplete) reference are the Notes for Authors editor Peter Salus wrote for the (long-defunct) Usenix Computing Systems journal. You can tell from the examples that this was written in the '80s, but the advice (except as it relates to the troff typesetting program) is still current.

The below hints are generally consistent with British/Australian rules, but sometimes narrower, particularly if this makes them consistent with American rules as well.

General Advice on Technical Writing
One of the most crucial aspects of writing a good technical paper is what I call maintaining user state. Like a good operating system, the writer should ensure that the (mental) state of the user (i.e. reader) is kept coherent. A good writer is fully aware of the relevant state in the mind of the reader at any point of the paper/report.

What do I mean with this? Basically it means that the paper systematically builds up the reader's understanding and knowledge of the work, starting from a reasonable initial state. This means you need to put yourself into the reader's shoes (or, rather, brain) and ensure that they can follow at each instance. One of the characteristics of good writers is that they do this well. Here is what this means:

Make reasonable assumptions about the initial state (i.e. prior knowledge). A common fault of theses and papers is too much assumed knowledge. You're breathing this stuff daily, and somehow assume everyone else does. They don't.

I frequently encounter the opposite problem in paper manuscripts: too much information is given that is considered general knowledge of the discipline. This is understandable in the case of junior students, who do not yet have a good understanding of what is considered the “general knowledge” of the discipline.

It is important to understand that what is “reasonable” assumed knowledge depends on the kind of report or paper you're writing. For an undergraduate thesis the initial state is the knowledge of the field you can expect from one of your peers: students at the same stage, but who haven't done their thesis in your area. You can assume them to have passed the basic operating-systems course (with no more than a credit) but know nothing about the area beyond that.

For papers it can be anything between an informed and intelligent generalist to a subject expert, depending on the publication venue. In particular, reviewers are experts in the discipline area of the conference, but they may not be the top experts in the (potentially) narrow problem your paper addresses. This becomes more pronounced as you progress through your PhD: in the end (when you're finished) you'll be the expert, and there may only be a handfull others at a comparable level of expertise. And not all of them will be your reviewers, so you can expect most reviewers to have a somewhat lesser degree of expertise (but you can also assume them to be very smart!)

Make sure the paper/report is self-contained. While it is important to reference prior work (yours as well as others), don't expect the reader to have read all those papers! In fact, a person of the right target group can in general not be expected to have read any but the most seminal papers, and even if they read them, they can't be expected to remember every detail (relevant as it may be to you). For example, if your work is about system virtual machines, you can expect the reader to be familiar with the Xen work, especially the Cambridge SOSP paper. But don't expect them to remember every trick described there!

Also, don't assume that the reviewers don't know some work intimately, there's always a likelihood that someone will. So don't think you can hide anything!

Ensure that at any point in the paper, you don't expect more knowledge from the reader than the union of the initial state and what you've told them so far. This seems obvious, but is violated frequently. Remember, the reader normally reads the work sequentially. It doesn't help them if a term you're using right now is explained ten pages later. Define-before-use isn't just important in programming, it's important in writing just the same.

Occasionally it is necessary to leave a detailed explanation for later. In this case you must provide a forward reference at the place where it is first used. However, this is only acceptable if an approximate understanding suffices at the point of the forward reference, and you can reasonably expect that approximate understanding to exist in the reader's mind. Examples are concepts that are widely used (and you use them consistently with the reader's expectation), or you have given at least a brief (potentially informal or anecdotal) explanation.

Small, strategic doses of redundancy help (but don't go overboard, as unnecessary redundancy annoys the reader as it wastes their time and detracts from the essentials). Use this to establish context. A good approach is for each section:

Say what you're going to say,
say it,
say what you just said.
This may look silly, but if done right significantly improves readability. You (1) start the section with a brief (1–3 sentence) overview what the section is about. Then (2) you provide the material. Finally (3) you summarise (in 1–3 sentences) the main take-aways, so the reader knows what they are expected to remember.

Use this in the main sections of a paper (not the intro, related work section or conclusion), but be really concise. In a thesis you're well advised to use it not only on the main chapters, but also the top-level sections of the chapters (and maybe even long secondary sections).

Occasionally you have circular dependencies: Explaining A requires understanding B, and explaining B requires understanding A. What do you do here? The usual way out of this is to first give a brief, informal explanation of all terms, and follow it up with a rigorous definition/explanation later. Particularly when the definitions are highly formal or tricky, this is a good idea anyway.

Remember, human memories aren't perfect, and therefore the user state is lossy. Like with DRAM, you need to refresh it. If a term has been explained early on, and then not used for many pages, chances are that the reader has forgotten. (Remember, a 50–100-page report is unlikely to be read in one go, the reader may have read that section a week ago. Even a conference submission may not be read in one go, reviewers get interruptions too!) So, give them a little refresher. Examples:

In Section 2 we had defined gizmo to be something every cool kid wants. Now we will... [Gently re-hashes definition]
The concept of a trusted computing base has been introduced in Chapter 3. We will now have a closer look at the components of the TCB in our system. [Unintrusively reminds readers of the definition of TCB without seeming repetitive]
This is another example of strategic use of redundancy to improve readability.

Be consistent in your own terminology. This again sounds too obvious to mention, but is violated all the time. For example, don't use two different terms interchangeably, unless they really have the same meaning, and you have made that point explicitly. For example:

Hypervisor and virtual-machine monitor are traditionally interchangeable, but don't use them interchangeably, as you're likely to confuse the reader. It's ok (in fact good) to mention interchangeable names, but then stick to one for the rest of the document! Also, note that these two terms are starting to take on different meanings, “hypervisor” is increasingly used only for the part of the virtual-machine monitor which executes in the most privileged mode, while there may be less privileged parts (such as the usermode virtualization support in L4, or Dom0 in Xen).
In a capability system you invoke operations by supplying a capability. You may talk of using a capability to invoke an object, or invoking a capability. Both are reasonable terminology, but they can't co-exist, as a capability is different from the object that gets invoked through it. Decide which terminology you want to use, and stick to it. Don't confuse the reader with loose language!
There are probably more rules of this sort, I'll add them as I think of them (and feel free to suggest some to me). In summary, the more you worry about maintaining user state, the more readable people will find your work.

About Thesis Writing
This section focuses on honours (undergraduate) theses, as they tend to be the ones needing advice. However, there are late-stage PhD students who are also well advised to read this (I've seen examples both when reading drafts from internal students as well as when assessing theses from other unis).
General advice
First rule is think before you write. Have an outline, know what you want to write about in each part, and how to approach it. If you start off with a brain dump, the final thesis will probably look like a brain dump. Not a good position from which to get a high mark... The section on structure tries to help you with this.

Also, be careful how you write. Ensure that the thesis is well-readable. This implies following the general style and grammar rules, violating those detracts the reader and makes the text harder to follow. These rules have developed for a reason. Also, check below for the proper use of “we”.

You may think I'm petty for insisting on proper prose. The reason I do it is because a report that ignores these rules is hard to read and annoys the reader. Making it hard to read wastes my time, and I don't feel I've got time to waste.

Many students have the attitude of “I'll write it down quickly and worry about the details later.” That's fine, as long as you worry about the “details” before you present a draft for feedback. Experience is you don't, and sloppy remains sloppy. In about thirty years as an academic, I am yet to experience a case where I got to read a sloppily/carelessly written draft which ended up being a well-written thesis. These cases may exist, I just haven't seen them. Avoid starting off in the wrong direction! The section on typical mistakes tries to help you with this. Read it before you start, and read it again before you hand out a draft for feedback!

Also, take feedback on your draft seriously. This means not only blindly fixing marked-up issues, but think about the comments. Particularly if the same mistake gets highlighted repeatedly, think about why you make this mistake, and how you can avoid making it again. How else do you want to learn good writing? Writing your thesis is your job, not mine. I only provide feedback so you can learn!

Please do not expect that I keep marking up the same mistake repeatedly, usually I only mark it up once. So when correcting a mistake, think about whether it might be part of a pattern.

Obviously, having a close look at a number of good thesis reports is a good idea, such as the samples we provide on our publications page. But keep in mind that some have been put up there because the work was good or interesting even though the presentation might be far from perfect. After all, those are real rather than ideal theses.

There are no firm rules on how to write a thesis, and there is certainly a lot of advice available. I'll try to concentrate on a few main points (which tend to apply to a lot of technical writing, not only to theses but also to conference papers).

Structure and coherence
Make sure your thesis is well structured, that each major section does what it is supposed to do, and that the whole thing hangs together. The basic structure is often as follows (but other structures are possible).

In particular, don't think you need to have exactly as many major sections or chapters as there below list implies; sometimes it makes sense to merge things, sometimes it makes sense to move things (e.g. the literature review is in many papers deferred until after the results), sometimes it makes sense to split a logical part into several individual sections. Also, PhD theses often integrate multiple broad issues which are covered in separate chapters, each with its own background and related work. Use common sense!

Title
Use a descriptive title for your work. Don't use a title that promises more than you'll deliver, don't use a title that implies something different from what you've done. (The focus of a thesis often shifts in the course of a year, don't be afraid to adjust the title, in consultation with your supervisor.)
Abstract
A short (1–3 paragraph) summary of the work. Should state the problem, major assumptions, basic idea of solution, results. Avoid non-standard terms and acronyms. The abstract must be able to be read completely on its own, detached from any other work (e.g. in collections of paper abstracts). Don't use references in an abstract.
Introduction
Introduce the problem (gently!) Try to give the reader an appreciation of the difficulty, and an idea of how you will go about it. It's like the overture of an opera: it plays on all the relevant themes.

Make sure you clearly state the vision/aims of your work, what problem you are trying to solve, and why it is important. Especially, make clear you highlight the challenges you need to overcome. Having made it through the intro, the reader should have a clear idea of what to expect in the remainder of the work. This applies to the problem, the author's hypothesis, and (at a very high level) the approach taken. Leave out any of these at your peril!

While the introduction is the part that is read first (ignoring title and abstract), and it is generally a good idea to write it first, in order to define the roadmap for the thesis, it is important that you revise (and more often than not, re-write) the intro after the document is essentially finished, and all the results are in and understood. This is essential to ensure consistency.

Remember, the intro is the first thing that is being read, and will have a major influence on the how the reader approaches your work. If you bore them now, you've most likely lost them already. On the other hand, if you make outrageous claims, pretend to solve the world's problems, etc, you're likely fighting an uphill battle later on.

Make sure you pick up any threads spun in the introduction later on, to ensure that the reader thinks they get what they have been promised. Don't create an expectation that you'll deliver more than you actually do. That is called bait and switch, and tends to leave the reader highly dissatisfied. Remember, the reader may be your marker (of a thesis) or referee (of a paper), and you don't want to piss them off.

It's also important that you provide enough context and indication the limitations/assumptions of your work to avoid uprising (and disappointing) your reader.

Exposition of problem
The basic problem should have been stated in the intro, here is the place to go into detail.

Make it clear you know what you are talking about (and this includes being complete, don't jump right into things, give the reader a chance to follow). Give a thorough and complete discussion of the problem, enough so an educated reader whose speciality is outside yours can appreciate that you're trying to attack an interesting problem, and also appreciates what's interesting about it. (Remember to maintain user state!)

Btw, don't call this section “exposition of the problem”, or you'll be immediately outed as someone who can only follow recipes. Same applies to the next bit.

Literature review (often called “related work”)
This is really important. If you cannot demonstrate that you know, and understand, what others have done, you only demonstrate that you're clueless. For an undergraduate thesis this, together with a thorough understanding of the problem, should be the result of the first session's work. It is an unfortunate fact that many students do very little work during the first session of their thesis. It usually shows here (and is usually reflected in their mark). Don't think you can fool your thesis supervisor/assessor. And don't even dream about fooling the referee of a paper. If you haven't done your homework here, it's probably not worth going any further.

In this part you demonstrate that you are aware of what's going on in the field, and how it relates to your particular problem. In an undergraduate thesis (unlike a conference paper) it may be ok to repeat work that has already been done elsewhere (usually in somewhat different circumstances). Be open, and explain why what you're doing is still worthwhile. In the more normal case that you're doing something that hasn't already been done, convince the reader that this is actually the case. One of the less convincing arguments goes along the line “a Google search on `frying giblets on StrongARM-driven toasters' didn't turn up anything”. You might as well pack up here. The way to convince the reader that your work hasn't been done before is to explain what has been done, what's different about what has been done, and, if you're good, why it hasn't been done already. There is always related work, and the more vague you are about it, the more obvious it is that you haven't done your homework. (And, no, looking at all the Google hits isn't enough.)

Sometimes some relevant background work is quite old; the discipline goes in cycles and it isn't all that infrequent that people rediscover things that have been done 30 years ago (virtual machines are an example). In such case please note that the language has changed a fair bit in the meantime. You're not doing your reader a favour of reporting an old paper's findings in that paper's language (and in the informed reader's mind you'll raise the suspicion that you don't understand what's going on). Talk about the work of the paper in contemporary systems language. This makes it easier to compare to other work, including yours.

Design of your solution
Having explained the problem, and what others have done in similar situations, now explain your approach. Again, give a general overview of your design first, and then go into detail (i.e. use a top-down approach). Make sure that the document (particularly a thesis) is self-contained: It should be possible for a reader familiar with the general area (that means operating systems, not methods for implementing free-block lists) to understand your design. (Remember to maintain user state!)

Discuss design tradeoffs before you present the design you have settled on, don't use the backward approach of “I'm doing it this way. I could have done it that way, but...” This smells of having been added as an afterthought. Show that you have thought things through, and convincingly show how and why you have arrived at the best solution.

Note that this may be an inversion of the approach you have taken in reality: You might have tried something, run into problems and then changed the design. Remember: your thesis isn't an activity report, it is the presentation of research. Which detours you took to arrive at the destination is primarily irrelevant (and in many cases just an admission of not having thought things through before you started). Focus on the destination, not the journey!

It's not necessarily wrong to point out what traps you fell into, but present that in the context of a discussion of design tradeoffs. Sometimes the correct design may be impossible to determine a priori, making some early experiments essential. But that doesn't mean it should be presented as a history lesson. Discuss the alternatives, say what you did to investigate the implications, and then present your design decision.

Importantly, be forthright about the limitations and assumptions of your design. Also, make sure you justify any shortcuts/limitations convincingly

Implementation
In many (not all cases) there is a clear difference between the general approach (design) and its implementation in your particular circumstances. The design may be more general than what you can do given time and resources. Or you have developed a general design, and are now implementing a prototype on particular hardware. Or the design is relatively high-level but leaves open a lot of implementation questions. Avoid mixing up discussions of design and implementation! Design is first, implementation later.

Give all required details. It should be possible to understand all this without referring to the source code. (I generally refer to the source code to check whether the code is consistent with the report, I shouldn't have to do this in order to understand the report.)

This will, in general, include extracts of actual source code (or pseudo-code), basic algorithms, function prototypes etc. Don't list pages of C code, an electronic copy of the source should accompany the submission and should be available to the marker, so there's no point in killing extra trees to put it into the report.

Make sure you describe your implementation in enough detail. (Maintain user state!) Someone who has nothing else but your thesis report to go by should be able to repeat your work, and arrive at essentially the same implementation. Reproducibility is an important component of scientific work. Also, clearly state the limitations of your implementation, and justify them.

Experiments
A thesis almost always has an experimental part, typically some benchmarking. This is usually its weakest part. Many students debug their code less than a week prior to the submission deadline (typical indication of having started too late) which makes it hopeless to do any real benchmarking. Benchmarking takes time, for running the experiments, but also for thinking them up in the first place, and for analysing the results (and, inevitably, decide you'll have to do more benchmarks to clear things up).

Probably the majority of theses I mark is really deficient in this part, typically for lack of attention (often resulting from a late start). Think about what makes sense to measure, what you want to learn from your measurements. Think about what is really the relevant contribution of your thesis, and how you can prove that you have achieved your goals. Think about what you can measure in order to get a good insight into the performance of various aspects of your design, how you can distinguish between systematic and accidental effects, how you can convince yourself that your results are right. Most of this should have been done during Part A of your thesis, together with your project plan you should have decided what your success criteria are, and how to establish that you have met them.

If you get surprising results, don't just say "surprise, surprise, performance isn't as good as hoped". Find out why. Surprises without explanation indicate either that you are clueless about what's going on, or that you have made a mistake (most likely both). Unconvincing results tend to imply unconvincing marks. (Of course, this could be avoided if the results were available more than a couple of days prior to the thesis deadline.)

It is amazing how few students have even the faintest clue of the most basic statistics and their use. Measurements always have statistical (sampling) errors. Owing to the deterministic nature of computers these are sometimes very small in our area, particularly in the case of micro-benchmarks, where disturbing factors can be minimised. However, the reader should be given an indication of how statistically significant the results are. This is done by providing at least a standard deviation in addition to averages. Whenever the results of several runs are averaged, a standard deviation can (and must) be supplied. After all, you average to reduce statistical errors.

The reproducibility argument applies here just as much as for the implementation. Give enough detail on what you measure, and how you measure it, so that someone who has your implementation (but not your test code) or has re-done your implementation independently, should be able to repeat your measurements and arrive at essentially the same results. I read many theses which contain results which seem outright wrong. In most cases not enough detail is provided to allow me to pinpoint the likely source of the error. In many cases the cause is systematic errors resulting from an incorrect measurement technique. If it seems wrong, and the text doesn't convince me that it isn't wrong, I will assume that it is wrong.

Discussion
Discuss and explain your results. Show how they support your thesis (or, if they don't, come up with a damned good reason real quick). It is important to separate objective facts clearly from their discussion (which is bound to contain subjective opinion). If the reader doesn't understand your results, you probably do neither. And this will be reflected in the assessment.

Conclusions
Don't leave it at the discussion: discuss what you/we can learn from the results. Draw some real conclusions. Separate discussion/interpretation of the results clearly from the conclusions you draw from them. (So-called “conclusion creep” tends to upset reviewers. It means surrendering your scientific objectivity.)

Identify all shortcomings/limitations of your work, and discuss how they could be fixed (“future work”).

I repeat: don't stick slavishly to this structure. Also, remember that the thesis must be:
honest, stating clearly all limitations;
self-contained—don't write just for the locals, don't assume that the reader has read the same literature as you, don't let the reader work out the details for themselves.
Also, a thesis isn't called “thesis” by accident: It is supposed to present a thesis (hypothesis) you are making about some system, and your justification and confirmation of that hypothesis. This means that a thesis is not an experience report. You may have taken a few detours and explored a few blind alleys. Some of that might be valuable to document, but only for what general truths can be learned from it, e.g. what the pros and cons of particular design decisions are.

So, explain the facts (and what's behind them) but don't bother the reader with the details of you got to the end. I repeat, focus on the destination, not on the journey!

My colleague Kevin Elphinstone has written an excellent guide on how to write a thesis, which also contains further references. My physics colleague Joe Wolfe has written a PhD thesis guide from a somewhat different angle.

By the way, if you found reading this page helped you write a better thesis, it would be nice to say so in the acknowledgments section.

About Paper Writing
Paper vs thesis
Thesis and paper writing are related, they both are technical presentations of work done. The main differences between a paper and a thesis are:

A paper is obviously much more concise. You don't have as much space to explain things. On the other hand, a paper is more directed at the experts, and can assume much more background knowledge. However, it is still (if not even more) important that relevant background information is cited. Part of the space limitation is that you generally need to put much more work into presentation of results, as you have very little space for them, yet need to show as many as you can!
A conference paper is pass/fail (with a very high failure rate, > 80% in most systems conferences!) And you typically only get a single shot, if you fail, you'll have to wait for the next conference. As such, a paper tends to be much more critically assessed, and you'll end up investing much more time per page than for a thesis (including your PhD). Remember, you're competing with the best minds in the field, and it is up to you to prove that you're playing on the same level!
General rules
As far as general writing style is concerned, I find it useful to think in the below Two Cs. Most papers I find poorly written (as opposed to technically deficient) fall down on one or both of them, or on structure (which is separately addressed below). Here are the Two Cs:

Be clear.
This should go without saying, but too many don't get it. Clarity applies at several levels, from individual words, to sentences, to paragraphs, to sections, to the whole paper. Make sure that at every level, what you are writing conveys a clear and unambiguous message.

For example, make sure that each sentence is unambiguous in its meaning. Make sure your formulation is precise.

Make sure every paragraph has a clear and unique purpose. Make sure a paragraph is homogeneous in its message (talks about one thing only) and paragraph breaks correspond to changes of points. When there is a point that requires a lot of text, so you want to break it into several paragraphs, make sure you break at a point that doesn't tear your argument apart. (Try to keep paragraphs to 2–4 sentences.)

Make sure each section (at any level) has a clear and coherent purpose and message. (Yet avoid sections getting too long, preferably not more than a single column, if at all possible not longer than a page, else break it up or sub-structure it.)

Most importantly, make sure the whole paper has a clear and consistent message. Make sure you understand what this message is! You should be able to state this message in one short sentence. Then stick to it, in the abstract, in the intro, in the body, in the conclusion.

It happens not infrequently that I read a paper, don't find any major faults (but typically not much excitement either) and at the end ask myself what I've learnt, or what the paper was trying to tell me. If I'm a reviewer, I'll argue for rejection in this case.

Summary: clarity at all levels!

Be concise.
In a thesis you can afford to be waffly (although it won't endear you to the reader), in a paper you can't. Reviewers expect a fair amount of meat in the 12 or so pages you've got, and if you waffle, you won't fit enough meat in. Furthermore, bloated prose tends to be harder to read. If something can be said in a sentence or in a paragraph, say it in a sentence.

Obviously, conciseness must not come at the expense of clarity, if shortening means loss of clarity, don't. Also, keep in mind what I said above about maintaining user state, However, experience shows that in most cases the more concise formulation is also the clearer one.

A common experience is that I edit a student's paper draft and in the process shorten it by 20–25%. In most cases the student will agree that clarity has improved at the same time (I call this “gainful compression”). A good method is “Jay's Rule of Thumb“, named after Jay Nievergelt, one of my early supervisors (I was pretty careless in my early postgrad days and lost a few of them ;-). It means you cover up parts of the text with your thumb. If it doesn't change the meaning, you know where you should cut.

Summary: Be brief but complete.

Besides that, it is important that the paper is readable. This means that reading it should be an enjoyable experience, not hard work! If it's hard to read, you're already in an uphill battle, irrespective of the content. Try to write in a lucid, engaging style. Explain things top-down, not bottom up.

While good writing is a bit of an art, paper writing also is lot of engineering. And, like in engineering, if the product looks like it's sloppy and thrown together quickly, the reader becomes automatically suspicious that it may not hold up. And experience shows that sloppy presentation frequently goes with content that isn't very solid, keep that in mind while writing!

Make reasonable assumptions on the background and experience of the reader. Not every reviewer will be a complete expert on your area, but you need to convince them anyway! On the other hand, don't think you can hide something from reviewers, at least one is likely to be a real expert and perfectly able to spot any holes!

Also, make sure your paper is properly spell-checked and proof-read. If you're not a native English speaker, get someone who is to help with proof-reading. Sloppiness annoys reviewers!

It's a good idea to get a non-author to sceptically read it (as a reviewer would), this can help spotting holes before it is too late.

Excellent advice is also contained in a set of slides by Simon Peyton Jones from Microsoft Research Cambridge.

Expectations on systems papers
How papers are expected to be written depends a bit on the discipline. What characterises systems is that ideas are considered cheap, and may get you a workshop paper, but nothing more. For a real paper you need a system, and evaluate it.

The classical How (and How Not) to Write a Good Systems Paper, written by the PC co-chairs of SOSP'83, spells it out quite clearly, and with about 35 years of age is still highly relevant. In the end, it comes down to making a convincing case of solving a real problem.

Note that the emphasised words are all relevant: “solving”, “problem” and “real”. You need to identify a problem, offer a solution, and show that you actually solve the problem. Solutions looking for problems find very little interest in this community! And coming up with a cool idea may get you some brownie points, but it isn't good enough.

Structure
Technical papers tend to have a certain structure. In the systems community, there is a fairly clear consensus on what the structure should be. It is outlined below, with recommendations on what to put into the various sections.

Title
The title is the primary hook for grabbing the potential reader's attention. For the final paper this is a form of marketing. For the submission to a conference, it is part of attracting the right reviewers.

Most conference PCs have a bidding process, where PC members express preferences for papers they want to review. These preferences are generally made on the basis of looking at the title and then the abstract. In fact, these conferences have 300 or more submissions, so the bidding itself takes a fair amount of time, and it's definitely a form of overhead on the reviewers, so they want to minimise it. The title is the first piece of information that tells the reviewer whether the paper is likely inside their sphere of interest and expertise, and most PC members will only look at the abstracts of papers where the title tells them that it might be of interest.

Therefore, make sure the title is informative! It should tell me whether this is about distribution or inside the node, whether it is about security or performance, whether it's about abstractions or implementation issues, whether it's theory-heavy or purely practical.

For the same reason, don't use a cute title for the submission, focus on being informative. You can get cute once the paper is accepted.

Abstract
The abstract serves multiple purposes. In any case, it is supposed to give the potential reader a good idea of what to expect in the paper. If I come across a paper with a title that sounds like it might be relevant, I'll next look at the abstract, and then decide whether I'll look further.

For a paper which is submitted to a conference for review, the abstract serves a single purpose: to attract the right reviewers (and many others don't seem to understand this). Having found the title potentially intersted, the PC member then checks the abstract for a bit more detail.

The critical importance here is to attract the right reviewers, those who really understand (and appreciate) what you're up to. It's bad news to end up with reviewers who are only marginally qualified/interested. Your paper has the best chances if it is reviewed by the PC members with the most relevant expertise. (That is, if the paper is good. If it's not, then you shouldn't have submitted it in the first place!)

This means that you need to word the abstract carefully so it correctly sets the expectations on the content of the paper. Make sure that it allows the reader to judge whether your paper is more theoretical or practical, whether it is in their area of interest and expertise. For example, a paper dealing with OS security issues might at one end deal with formal security models, or on the other end with design and implementation techniques which decrease the attack surface. Both are important and relevant, but the best reviewers (from a given PC) are likely to be different people!

BTW, it's always a good idea to look at who actually is on the PC, and think about whom you prefer as reviewer of your paper. Then write the abstract to get them interested!

Once your paper is accepted, the abstract has a different purpose: it should contain the right keywords to direct searches, and give people an idea of whether it contains something of interest for them. That's similar, but different from the purpose of the submission version (you're now trying to appeal to a wider audience) so you might want to re-write. In these days of search machines and word clouds, this classical function of the abstract is of much less relevance than it used to be, and a good reason to keep it short.

A core rule for the abstract is keep it short! A long abstract not only wastes valuable real estate, it actually makes it harder to quickly assess what the paper is about. This is especially important in the bidding process: when reading 100s of abstracts I'm not likely to carefully read one that is half a page. But it is also when just browsing for papers that are potentially relevant to my work.

A good rule of thumb is that an abstract should be like a good elevator pitch, address the following, each in one (at most two) sentences:

What is the problem you're trying to address?
Why is it a problem (aka who cares)?
How are you solving it?
Which results did you get (aka what did you achieve)?
Anyone who wants more detail should read (skim) the introduction (which itself should be brief).

Introduction
This is the most important part of the paper, certainly as far as writing is concerned. Here you need to convince the reader that you have identified a real problem (which includes motivating why it is relevant!) and outline your approach to solving it. And make it clear that you have actually solved it!

It is often a good idea to write the intro in two steps. Write it before you write anything else, this will define where the paper is heading. Then, at the very end, go over it very carefully to ensure that it is still consistent with the rest of the paper. In particular, ensure that the intro doesn't promise more than what the paper holds. Reviewers get very angry with bait-and-switch papers (see below)!

Make sure that the intro is concise, yet interesting, highly readable, and complete. It should not be longer than about a page, if it does, you're probably putting too much detail in, leave that for later. Use the intro to whet the reader's appetite: make them want to know more (but don't let them guessing whether the paper is in their domain of interest).

Also, try to put a diagram/figure on the first page. This immediately makes the paper look more appealing. Obviously, the figure must be related to what you are presenting and help understanding, else it's a useless filler. Good examples are diagrams (eg from measurements) which highlight the problem you're trying to solve, or an indication of your results. And it should be referenced on the first page, else it belongs to where it is referenced.

Avoid buzzwords, over-the-top statements and outrageous claims. This applies to the whole paper, but the introduction section is particularly prone to over-selling. This makes the reader suspect and frequently annoyed. Examples of buzzwords are “new”, “novel”, “innovative”, etc. These are useless fillers and should be avoided! If your work isn't novel, you wouldn't be trying to publish it, right?

One particular kind of over-selling is called “bait and switch”: promising (or appearing to promise) in the intro great things but then deliver only a subset or something completely different. This happens a lot, and is an excellent way to bias reviewers against you!

Then cut to the chase! After getting an idea what you're trying to sell me, I want to know how it works. At least a general idea of how you solve the problem should be presented in the intro. I want to see that what you are saying makes sense. It is extremely annoying having to read through lots of cruft to find out how it's supposed to work (especially if you fail to convince the reader that your approach will work). That's typically a death sentence for your paper!

Then I want to get an idea of the outcomes of the work. That means a brief, high-level description of your results. But the outcome is more than the experimental results, it's the general contribution the paper makes. List your contributions explicitly, best done in a bullet list, with forward references to the sections in the paper where I can find them.

In summary, the intro must convey that you meet the general criteria for a systems paper: identified a real problem (motivate that it is real and interesting), come up with a solution (give a rough idea what the solution looks like) and actually solved the problem (high-level summary of results).

An utterly useless (despite its popularity) part of the intro is the paragraph starting “the rest of the paper is structured as follows”, and frequently ends “and we conclude in Section 5.” What a pointless waste of real estate! There is no useful info in such a paragraph, particularly if you followed my advice of having a bulleted list of contributions with forward references.

Background
This is where you go into details about the motivation for your work, and any other background required to understand it. The length of this is very dependent on your paper, it's hard to give a general guideline here.

This section will contain a lot of references to related work. Some people will therefore have a related-work section right after the intro (I have done that sometimes too). However, in most cases that's not a good idea. Focus on providing the background needed for the rest of the paper and get to the interesting bits as quickly as possible, and having to cover and discuss everything that's related only distracts from that mission. So, it's generally better to put the related work section at the end. However, make sure you properly cite every bit of background you introduce!

What you've actually done
Of course, you won't use that as a section title, but this is what the middle part of your paper is all about. It's typically broken into two sections, eg concepts/design and implementation, but it can be more or fewer sections.

The best general advise here is to be concise, precise and easy to follow. This sounds like motherhood and apple pie (and is to a degree) but you won't believe how many submissions can't get this right. Remember, a PC member might read 20–30 papers. Keep them interested. If a paper is boring, or hard to follow, it's got an uphill battle to be accepted.

Use diagrams where possible to explain things. Good diagrams help the reviewer getting though your paper quickly, without missing important content. If it can be explained with the help of a diagram, it should.

In the PC meeting, where the fate of papers is decided, papers without a “champion” (someone who really likes a paper and wants it published) stand a poor chance to survive. Do your best to ensure that there is at least one PC member who'll champion your paper!

Evaluation
This is where the rubber hits the road: You now have to prove that you've actually done it (solved your problem) and done so in a convincing way. This means finding the right evaluation criteria—meaningful benchmarks which demonstrate that you have something useful. It also means looking good on those benchmarks.

I intentionally said “prove”: The evaluation isn't about just going through motions of showing some numbers, it must instill confidence in the reader that your solution really is what you claim it is. If you are not doing your best to show that your solution is up to scratch in every respect, the reviewer will suspect that you're trying to hide something. So, your evaluation needs to be pro-active in a sense that it needs to anticipate what problems the reader might suspect, and deal with them head-on.

Select your evaluation scenarios carefully and convincingly. Don't artificially construct best cases, they will be discounted if they don't present a convincing scenario.

Also, keep in mind that any improvement must satisfy a progressive as well as a conservative criterion (and your evaluation must show this). The progressive criterion requires that you demonstrate significant improvement with respect to the problem you have identified. The conservative criterion requires that you demonstrate that you have not worsened the situation in all the other circumstances people may care about. For example, if your work speeds up certain system calls, I want to be convinced that this is not at the expense of other system calls (or a strong argument why this doesn't matter).

This means that you need to think carefully about worst-case scenarios for your approach, and show that they aren't too bad. Go out of your way to be fair, and think of scenarios an adversary (who wants you to look bad) might come up with. Reviewers appreciate thoroughness here.

Above all, be honest, and be seen as such. I maintain my list of benchmarking crimes separately, make sure you stay away from those!

Related work
The most important role of the related-work section is to show that you know the field, and are familiar with all the relevant contributions made by others. Take specific care not to omit any work by likely reviewers! It's a good idea to go through the list of PC members and think about what they worked on in the past, and whether any of that work might be worth citing. Reviewers get pissed off if they think that you're re-inventing something they did before.

But stay clear of anything that might look like an attempt to bribe reviewers with citations. If it looks like you only cited my paper because I'm on the PC, and the paper isn't really relevant, I won't think highly of you. Good judgement is important!

Don't fall into the trap of trying to make prior work look bad in order to justify your own. While it is true that some bad work gets published, and occasionally some badness provides the motivation for your work, be very careful there. State, as neutrally as possible, what the prior work has achieved, and, where relevant, its limitations.


For example, saying “Doe investigates core temperature but fails to account for load fluctuations” implies that Doe stuffed up. You really only want to say that if you (a) think they stuffed up and (b) really want to make that point (“a courageous decision“ as Sir Humphrey would say!) Else a better formulation might be “Doe investigates core temperature under the implied assumption of constant load”.

The normal assumption is that the prior work is good, and you're taking it further. It's OK to admit you're standing on the shoulders of giants! Also, remember that the author of the work you cite might be your reviewer. Little infuriates a reviewer more than the feeling you misrepresent their work, or you don't understand it. Biasing reviewers against you isn't a smart strategy.

An important aspect of this last advice is that you must have carefully read and understood the work you are citing. Don't cite a paper just because it's the standard reference and everyone cites it. Read. It. Carefully. Failure to follow this rule increases the likelihood of misrepresenting the paper and annoying your reviewer (even if they aren't the author of that paper, if it's the standard work you can safely assume that they have read it and understand it!)

Conclusions and Future Work
This is where you summarise what you've achieved. This is a bit like some of the later parts of the intro, but different. Now the reader knows everything, and this is your last chance to press what you think are your main achievements. Don't over-do it, and be brief! Also, re-visit some of the limitations and what can be done to address them. However, don't promise anything if you have no intention to deliver!

Formatting
Conferences tend to be quite prescriptive about the formatting of submissions. Observe all formatting rules! In particular:

Don't mess with margins, font sizes or baseline skip! Some PC chairs (me included!) will use formatting checkers of various sorts. If you are found to have cheated, your paper may be rejected without review, and you deserve it. (Trust me, it happens, I've done it myself.) After all, these rules apply to all, and you shouldn't try to get an unfair advantage.

Don't use microscopic fonts in figures! People tend to be a bit more relaxed about enforcing font sizes in figures and tables (I wish the weren't), but it is an annoyance having to review a paper where you need a magnifying glass to read the figures.

You may think they read fine, but you're probably less than 30 years old and are sitting at a desk with good light. After the age of 40, eyesight weakens. Probably half the members of a typical PC are in the >40 age group, so you're annoying a lot of people. In addition, I do a lot of my reviewing with imperfect light conditions (especially in airplanes), making the problem worse. If I can't read the figures properly then I'll make some worst-case assumptions about them.

These days much reviewing is done on tablets rather than hardcopy (I do all my reviewing this way), and it's easier to magnify things. However, if I have to magnify your figure, it means you're cheating by helping yourself to additional space. I do not like cheats, and most other reviewers don't like them either.

Some Things People Frequently Get Wrong
This is my list of things that people most frequently get wrong, listed in no particular order, except that the most annoying ones are at the top. I'll keep adding to this from time to time.

If you are my student, I expect that you have read this, and have checked that any draft you give me to read observes the advice below. If not you'll get it back with not much more than “RTFSG;” printed on it.

Passive Voice
Overuse of passive voice is one of the most annoying mistakes I see in undergraduate theses. (And it seems it's particularly prevalent among EE students — is someone teaching you this???) Whatever the reason, stop it!
Overuse of passive voice is very poor style. It makes for a very boring read, and it creates the impression that you are not really taking responsibility for what you've written. If 1/4 or more of your sentences use passive voice, your prose is poor.

A typical occurrence (especial in U/G theses) is the use of passive voice as a way to avoid the first person, e.g., “a suitable protocol was designed to cope with that situation”, when the student means to say that they designed the protocol. This might be a case of shyness, but it comes across as trying to avoid responsibility for one's actions. At best it leaves the reader puzzling who had actually done the work. Show through your writing that you assume ownership and responsibility for what you have done, and make it always perfectly clear what you have contributed and what came from others! And yes, a thesis (like a paper) uses the first person plural.

Just to make it perfectly clear, I will mark you down for excessive use of passive voice in your thesis. No matter how good it is otherwise!

Buzzwords
Buzzwords are annoying to the informed reader and should be avoided, they create the impression of bragging (and often outright cluelessness). In my former life I found that editors of physics journals would systematically remove words like “novel”, “new” or ”innovative” in the title, abstract or intro. For good reason: if it ain't novel, why are you trying to publish it? In fact, you're creating the impression that doing something novel is unusual for you. Shy away from such words!
Similar with terms which are popular in the trade press but rarely used in scientific work—blend in with the standard terminology of the community.

Chart abuse
The term chart abuse was coined by Martin Gardner, who for a quarter of a century wrote the brilliant “Mathematical Games” column in Scientific American. It refers to all sort of ways of using graphs in an (intentionally or not) misleading way. In science, being misleading is a form of intellectual dishonesty.

Chart abuse example
A typical example is shown in the figure on the right. Whatever the quantity on the abscissa is, you're likely to have the impression that varying that quantity has a dramatic impact on whatever the ordinate quantity is, after all, it goes from almost full to almost empty, right? Of course, if you actually look at the units, you see that the dependent quantity varies by only 21%. This may or may not be significant, but it isn't anywhere near the rough order-of-magnitude change the graph seems to show on a cursory glance.

Note that not every such graph represents chart abuse, it depends a lot of the reader's expectations, the discussion of the data, and what is shown in other graphs. Just relying on showing the units may not be enough, as images can be very persuasive. Zooming in on details is a valid (and valuable) analysis tool. However, you must be aware that this graph is not showing the full story, and you need to be extra careful that this does not leave the reader with the wrong impression!

The opposite approach can also mislead: instead of exaggerating difference by zooming in, one can hide differences by zooming out, and using thick lines to pretend different lines are exactly on top of each other. This approach can easily hide a 5–10% difference. Whether or not such a difference is relevant depends on the context, but you need to allow the reader to judge for themselves.
Thanks Orna Agmon Ben-Yehuda for pointing me to this.

UNSW Engineering chart abuse
Here's a particularly impressive example closer to home (for me – it's from an education discussion paper of the UNSW Faculty of Engineering). It compares schools (what US universities would call departments) by student numbers and research income (not clear what the relevance of research income is for education). It also lists staff numbers in each school, but does not depict those graphically. Why not, given that staff numbers seem to have more obvious relevance to education than research income? They wouldn't want to downplay something, would they?

Looking at the numbers we can see that student-staff ratios vary dramatically across the schools. The school with 95 staff (let's call it S95) has a student-staff ratio (SSR) of 2.6 while school S112 has SSR112=36.5. Obviously, this is partially explained by the difference in research income (a ratio of 2.3 between the schools), clearly research income pays for many staff. So, let's look at the three schools with about the same research income of $10.4M±5% to eliminate that parameter. We find wildly different ratios: SSR102=5.7, SSR101=14.5, SSR112=36.5.

This is in stark contrast to the seemingly fairly balanced picture presented by the graphic. Now it's entirely possible that there are other relevant factors, but they aren't given, and the diagram seems designed to downplay the most striking difference, rather than explain it – a rather misleading representation of the data.

Another bad case of chart abuse is the gratuitous use of logarithmic scales; this is a great way to make execution time increases look insignificant. Do not expect reviewers/assessors to fall for it!

Someone put together a nice collection of bad graphs, all good example of how not to do it. (But I think their claim of “top ten worst graphs” is an exaggeration, I've seen worse (including the above!) I guess I'll have to start my own collection, stay tuned...)

Spelling
There is no excuse for presenting a draft that hasn't gone through a spell checker. If you're too lazy to do this, then I'm too lazy to read your work. Period. And if I have to read it (because I need to mark your thesis) you'll see the result in the mark.
Apostrophes
Incredible how many people cannot use them correctly (and I suspect that it's often laziness).
Apostrophes are used to mark possessions and attributions. Like the thread's priority. Note that there is no apostrophe in the case of the personal pronouns he, she and it: the thread used up its time slice. Bob's pretty clear about this one!
Apostrophes are used for contractions. Like I can't, or it's time. Note that these are generally not used in formal prose (such as reports and papers) as they sound colloquial.
That's pretty much it (says Bob). But keep in mind that apostrophes are actually useful, so don't leave them off completely!
See also acronyms

Capitalisation
Don't Randomly capitalise Words. Looks Ridiculous, doesn't it?
Capitals are used for:

words beginning a sentence;
names (proper nouns)
acronyms
certain types of words in high-level headings.
Capitals shouldn't be used for definitions, including defining acronyms: the definition doesn't turn the defined word into a proper noun (which would be the only reason to capitalise it). And they should be used even less without any obvious reason.
Note that (contrary to many “official” style guides) in scientific publishing (yes, that means you) numbered section, figure etc. references in papers are treated as proper names: In the next section we introduce the problem, and in Section 3.1 we demonstrate how to solve it. (By the way, note that the reference to a sub-section still calls it “Section”!)

Commas
This is probably what I get most often wrong myself (partially because of totally different rules in German and English). I quote the basic rules from Peters, but skip the detailed explanations. If someone wants to copy them from the book, be my guest.
[Commas] have a vital role to play in longer sentences, separating information into readable units, and guiding the reader as to the relationship between phrases and items in a series.
A single comma ensure correct reading of sentences which start with a longish introductory element: Before the close of the last Ice Age, Tasmania was joined to the mainland of Australia.
[ ... ]
Pairs of commas help in the middle of a sentence to set off any string of words which is either a parenthesis or in apposition to whatever went before.
The desert trees, casuarinas and acacias, were sprouting new green needles. (Apposition)
The dead canyons, all nature in them reduced to desiccation, came alive with the sound of rain slithering down the crevasses. (Parenthesis)
Note that a pair of [em-]dashes could have been used instead of commas with the parenthesis, in both formal and informal writing.
Sets of commas are a means of separating:
strings of predicative adjectives, as in: It looks big, bold, enticing.
items in a series, as in: The billabongs at sunset drew flocks of galahs, gang-gangs, budgerigars and cockatoos of all kinds.
A curious amount of heat has been generated over whether there or not there should be a comma between the two last items in such a series (the so-called serial comma debate). [ Details omitted, summary: don't put it except where required for clarity. US rules are strict here (but are ok to ignore). ]
[ ... ]
In reality, it's more complicated than this, the exact rules of commas in English are very much a black art IMHO. In fact, there are different schools of experts who will argue at lengths about the necessity or excessiveness of commas in particular situations. The silly serial comma aka. Oxford comma is a case in point. For some entertaining reading I recommend Holy Writ from The New Yorker's “Comma Queen”.

For us mortals I recommend following the basic rules, and else add commas where they help understanding, and otherwise leave them.

Colons (and lists)
Colons are used to indicate that examples or specific details are to come:
The sentence normally continues, and, consequently, the next word isn't capitalised, unless it would be capitalised anyway, or it's a slogan or a motto.
Alternatively, the examples or details may be given as complete sentences, in which case they should start in a new paragraph.
Bullet lists or enumerated lists set as paragraphs (so-called vertical lists) are introduced by a colon. Regarding their capitalisation and punctuation, there are three cases to distinguish:
If the list items are short (few words or simple phrase) and without internal punctuation, their first word is not capitalised and no punctuation is used (except possibly at the end of the last one). Example: see capitalisation.
If the list items contain internal punctuation, but are not all complete sentences, then their first word is not capitalised and each item is terminated by a semicolon (except the last, which is terminated by a full stop). Example: see the summary at the end of the general advise.
If the list items are each (one or more) complete sentences, they are written as such: first word capitalised, and each terminated with a full stop. Example: see colons.
Note: US rules differ.
Period (full stop)
The period is used to end a sentence, as well to identify an abbreviation. The two are actually distinguished in type-setting: a period designating an abbreviation (and nothing else) is followed by a normal inter-word space, while a period at the end of a sentence is followed by a longer inter-sentence space. Many formatters (incl. web browsers) automatically produce an inter-sentence space after each period; this is wrong if it is not the actual end of the sentence, and must be overwritten by forcing an inter-word space (e.g. in HTML say “ACME Ltd.&nbsp;is headquartered in Woolloomooloo”). LaTeX does it right for abbreviations ending in capitals, but otherwise the period must be followed by a backslash.
Quotation marks
There isn't complete agreement on that in the British-speaking world. I recommend the following rules, which are compatible with the British as well as the (stricter) American rules:
Quotation marks are for quotations. They are not to introduce new terms, they are for quoting someone/something, e.g. called “giblet” in [Bloe 99]. They are also used for irony (a small subset of what you'd use a smiley for), but this is rare in technical prose. E.g. Its “outstanding” performance made the system useless except for toy applications. Note that not all humour is irony!
Quotation marks are normally double ticks. Single quotation marks are used only for quotations inside quotations.
The begin and end quotation marks are different, as in the above examples.
If the quotation extends over several paragraphs, it should start a new paragraph, and the begin-quotation marks must be repeated at the beginning of each paragraph. However, in such a case it is much better to set off the quotation by indentation (as with the LaTeX quotation environment) and use no quotation marks at all.
There is some confusion about other punctuation. There are two basic cases:
The quotation ends with an exclamation or question mark. In this case the mark goes inside the quotation, and no period follows, even if the quotation marks the end of the sentence.
Otherwise, if the quotation is at the end of the sentence, put the period inside the quotation marks if the quotation would normally end in a period, otherwise put it outside (even though Americans might tell you otherwise.)
Btw, similar rules apply for parentheses. US rules differ (but are illogical, I ignore them).
Note that the LaTeX csquote package automates much of this.
Definitions/introductions of new terms
Use italics when introducing new terms. This makes it easy for the reader to find the definition again, particularly when not having the time to read the paper in one shot. Do not capitalise words when they are introduced (unless you'd normally capitalise them). Do not put them in quotations marks (see above).
Acronyms and Initialisms
Technically the difference between the two is that acronyms you pronounce as a word (FOSS) while initialisms are pronounced as individual letters (UNSW). The distinction is hardly ever made and both are generally lumped under the general term of “acronym”, as in the reminder of this document.
Properly define all acronyms on first use (except maybe those really everybody knows, such as CPU). An acronym is normally introduced by following the full term by the abbreviation, as in address mappings are cached in the translation look-aside buffer (TLB). The other order (use the acronym and put the expansion in parentheses) is occasionally acceptable if that helps the flow, but it should really be an exception. Don't introduce too many acronyms, and use standardised ones whenever possible.

Don't introduce acronyms in headings! If a term for which you want to use an acronym appears first in a heading, define the acronym on the next appearance (the first one in paragraph mode). Also, don't introduce an acronym which is then not used for a long time. In such a case it is also better to defer the introduction of the acronym.

A similar rule applies to abstracts. You may (occasionally) define an acronym in the abstract (because the abstract uses the same term multiple times). But in this case you'll need to re-introduce the acronym in the body of the document. The reason is that abstract and body live mostly separate lives. I read the abstract to decide whether a paper is interesting/relevant to me, but typically don't immediately read it then. By the time I get to read it, I will not re-read the abstract, as it's not expected to tell me anything the intro won't. So keep this in mind.

It sometimes happens that an acronym is introduced and used more-or-less heavily in an early part of a thesis or paper, is then not used for a long time, until it is used again much later. Remember that the reader may not read the whole thesis or paper in one go, and may have forgotten what the acronym stands for. In such a case (at least if it's an acronym that isn't widely used) it's better to re-state the definition when the term starts appearing again. A very gentle way to remind the reader of the meaning of an acronym is to use it just after its expanded form in a way that makes its meaning obvious. Example: In this paper we only consider the priority-inheritance protocol. We chose PIP because.... This is obviously only acceptable if the acronym has been introduced before. Basic rule: Be nice to the reader!

Acronyms are normally all upper case, however, in our discipline mixed case acronyms have become very common (e.g., QoS for quality of service). They should still start with a capital letter. Acronyms are almost never all lower case. The one exception is units of measurement (e.g. loc for lines of code, although journals would normally use LOC for this). If you find an all-capital acronym too imposing consider using SMALLCAPS. However, remember to be consistent: if you decide to use a special font for something like a specific acronym, make sure you always use the same font for the thing. Also, don't go overboard with fonts, kindergarten documents are hard to read.

What's the plural of CPU? CPUs or CPU's? The answer is clear (notwithstanding many people getting it wrong): CPUs is a plural while CPU's indicates a possession or attribution. Example: Of the system's two CPUs, only one was operational. The second CPU's power supply had been disconnected.

A special case of this is acronyms ending in s, e.g. OS. I have found a (seemingly authoritative) reference which claims that in this case you need an apostrophe, but Peters has no such special rule, and I really don't see why there should be one. I strongly recommend OSes over OS's for the plural, in order to clearly distinguish it from the possessive case. Note that UNIX is traditionally pluralised as UNIXen, like oxen, but I think that's tradition rather than a grammatical rule, and the usage UNIXes is at least as common.

In rare cases using no apostrophe for the plural might create confusions with mixed-case acronyms. In that case use an apostrophe if you really think that it improves clarity.

Units of measurement and their prefixes
Computer people are particularly notorious (others would say clueless) with respect to improper use of unit symbols. I regularly see “KB”, “kb”, “Kb” all (intending to) refer to the same thing (1024 bytes), all wrong. Specifically:
KB would be kelvin bytes, presumably a unit of information temperature, I don't think anyone has found a use for that unit yet;
kb would be kilo bits, which these days is probably only used as part of a unit of bandwidth for really slow links;
Kb would be the useless kelvin bits.
So, bit is “b”, byte is “B”, kilo is “k”, not “K”. Furthermore, the unit prefixes “k”, “M”, “G”, etc. strictly refer to powers of ten, i.e. 103, 106, 109. In IT contexts they frequently stand for powers of two, i.e. 210, 220, 230. This is of course confusing. If you think it is not, can you confidently tell me whether a Gigabit Ethernet is supposed to have a bandwidth of 109 b/s or 230 b/s?

There are in fact proper SI prefixes for power-of-two multiples: “Ki”, “Mi”, “Gi”, etc. Use them systematically!

Headings
Capitalise or not? Generally speaking, only top-level or, for larger documents, second-level section headings should be capitalised. For other headings capitalise the first word (of course), but otherwise nothing you wouldn't capitalise in normal text. If you capitalise words in a heading, only do so with nouns, adjectives, pronouns, verbs and adverbs.
Excess digits (pseudo accuracy)
A common annoyance is people quoting results with three or four digits accuracy, when the real accuracy is at best a few percent. For example, I commonly read statements like “we observed performance improvements of up to 27.81%.”. This pretends that the improvement figure is accurate to about one in 10,000. Of course, it's nowhere near that! It's the difference of two other figures (the baseline and the improved system), and the uncertainty in the difference is no better than twice that of the two values. This is misleading, as it gives the appearance of something (accuracy) that isn't there.
And even if the number was really that accurate? Does it matter whether your improvement is 27.81% or 27.82? What counts is the (binary) order of magnitude: whether it's around 15% or around 30%.

At least in this case everyone can immediately see that this is pseudo accuracy, and will mentally drop the n-1 excessive digits. That's not the case in tables where you present your actual results, which makes this a worse offence. As I argue in my discussion of benchmarking crimes, results must indicate the significance (accuracy) of data, typically by stating standard deviations. But don't undo this by pretending more accuracy with excessive digits! If you show three-digit results, I expect an accuracy well below a percent. And I get annoyed if I think you're trying to fool me!

Note that standard deviations (or other kinds of errors) are a second-order effect (just as the relative improvement discussed above). As such, they are only relevant to one digit! Stating absolute standard deviations to three digits is nonsense. It's actually an example of garbage math.

A good (or bad, as you look at it) example of excessive digits in the table that gets an honourable mention in the list of bad graphs discussed earlier. The discussion (rightly) also makes the point that trailing zeroes should not be suppressed where they carry information, i.e. are within the accuracy of the data. (For some reason, this only this only seems to affect people who write their papers in Word...)

Percentage vs Percentage Points
The confusion between these two seems to go together with the above point, and is a worrisome indication of a lack of appreciation of numbers that you should not see with serious researchers.
If your overhead (e.g. measured as relative latency increase over a reasonable baseline) changes from 20% to 30%, then this does in no way constitute a 10% increase, it's a 50% increase in overhead! Alternatively, you can say the increase is 10 percentage points, although the actual percentage increase is usually the more meaningful figure.

In any case, make sure you use the terminology correctly. In fact, incorrect usage can constitute a benchmarking crime!

Xkcd has a nice comic on this.

Footnotes
First rule: use them sparingly. Many disciplines (especially humanities) use them for citations, we don't. Footnotes are used for information which is useful, but is not essential for understanding the argument, and including it in the text would disrupt the flow (similar to parentheses). If you use more than about one every few pages, there's probably something wrong with your prose. Most papers get away without a single footnote.
Second rule: Footnotes should be fair-dinkum sentences, able to be read by themselves. A footnote like 5 KiB is a definitive no-no. Something like #define'd to 5 KiB. is very bad. Good is The buffer size is defined to be 5 KiB. (Except that anyone using a 5 KiB buffer should be shot.)

Since footnotes are sentences, it doesn't normally make sense to put them into the middle of a sentence. In particular, this means the footnote follows, rather than precedes, any punctuation. An example of correct use is We use the Fancy tool.\footnote{Fancy can be obtained from \url{https://fancy.org}.} Placing the footnote before the full stop is incorrect, as is spacing it off the full stop.

Hyphens, en-dashes and em-dashes
These are three kinds of dashes used in text:
The hyphen (LaTeX “-”, Unicode “-”, HTML “-”, plain ASCII “-”) is used for hyphenation (breaking words at the end of line), as well as for compound words. The former you never need to do explicitly, LaTeX does it for you. (You may help LaTeX in difficult cases, as in hy\-phe\-nate.)

The hyphen is generally to be used to overwrite the default binding of English. Attributes preceding a noun are by default bound right to left in English, which can produce an incorrect meaning. For example, single address space is right, as address qualifies space, and single qualifies address space. However, if this is itself used to qualify another noun, becoming an “ad hoc compound adjective“, it needs hyphens: single-address-space operating system. Without the hyphens, operating system would be qualified by space, and a space operating system is something different from what we are concerned with.

Hyphens may not only be required by adjectives qualifying a noun: The syscall requires the invoking process to be root-owned.

There are plenty of exceptions. For example, no hyphens are used for compound adjectives whose first part is an inflected adverb or adjective, examples are badly overclocked CPU, or lower rated memory. (Careful observers may have noticed that I tend to forget many of these exceptions, and as a result tend to over-hyphenate. Feel free to tell me!)

Finally there are compound nouns which use a hyphen, such as know-how. Use them sparingly!

I find this article from the Canadian government very useful.

The en-dash “–” (LaTeX “--”, Unicode “<Compose>--.”, “<Option>-”, HTML entity reference “&ndash;”, plain ASCII “-” as for the hyphen) is used for ranges, e.g. RAM sizes of 0.5–64 GiB are supported. The en-dash is used between single words or numbers without surrounding space, but has surrounding space if it is between items that have internal space. Example: during the time of 12 March – 15 May.

the em-dash “—” (LaTeX “---”, Unicode “<Compose>---”, “<Shift><Option>-”, HTML entity reference “&mdash;”, plain ASCII “--”) is used as a separator, somewhat similar to a semicolon. Note that when used un-spaced, LaTeX runs it right into the adjacent words, apparently that's what the rules say.
General advice, as for parentheses, is to use them sparingly. The excessive use of parenthetical remarks indicates lack of clarity or focus.

In Australian (and British) English, the (un-spaced) em-dash is not commonly used, a spaced en-dash tends to be used instead.

Split infinitives
Remember to never split infinitives! :-)
According to Peters that's a bullshit rule. It's often more elegant/readable to split the infinitive, so go ahead if it avoids clumsiness, but use it sparingly to avoid upsetting old-fashioned people.
Specific terms or phrases
Like vs. such as
When you are referring to a set, the members of which have in common a given characteristic, and you wish to give an example that is a member of that set, you should use such as. When you are referring to a set that does not include your example, but that contains members that resemble your example, you should use like. Examples: Students, such as those at UNSW, sometimes are having fun. Sometimes they behave like children with a new toy. (Note that British/Australian English is more relaxed about this rule than American English.)
Spaces
Some people add spaces in the weirdest places. I don't remember all of them, but came across another annoying case so I decided to start a spacing blacklist here. Stay tuned for more entries ;-)
Before colons (in definition lists or elsewhere)
Doesn't belong.
After opening or before closing parentheses (of any sort)
Parentheses aren't spaced of on the inside.
Some go the opposite way and omit spaces where they should appear, e.g.:

Before opening or after closing parentheses
Why should an opening parenthesis be glued to the preceding word? No matter whether this introduces an acronym or a non-essential remark, the outside of the parentheses like air to breath.
Before a unit of measurement
Units of measurement are spaced off the preceding number. However, a full space generally seems too much, so I recommend using a half space (e.g. LaTeX 100\,Hz gives 100 Hz), which also prevents a line break between the number and its unit.
Inclusive vs Royal “We”
Scientific literature is written in the first person plural (“we form”), and theses are no exception. This is meant to include the reader in the proceedings (“we” in the sense of “you and I together”). However, used wrongly it will sound odd, especially for a single-authored work (such as a thesis), sounding like a royal we (“we, the king of this realm”) and thus pretentious.
So, use it in a way that takes the reader with you. Examples: We will now look at the dependency of power on load. Or: We run the system at its maximum performance setting and measure core temperature. We obtain the results shown in Figure 5.

In particular, this means that you should be using present and future tense, and generally not past tense / present perfect. A statement like we obtained the results shown in Figure 5 is a royal we. The reader wasn't around when you did this, so the “we” can only refer to yourself, making it an obnoxious royal “we”.

Citations and Bibliography
Should you use numeric or alphabetic citations? Some conferences or journals have clear rules on this, so you'll obviously have to follow them. Conference papers are usually squeezed for space, so using numeric citation labels tends to be used as a space saver.
In all other cases, use alphabetic citation labels as these greatly enhance readability. At the least this should be the BibTeX alpha style. Particular for a PhD thesis, which has many citations, most of them familiar to the examiner, having meaningful alphabetic labels massively reduces the need to consult the bibliography. The recommended form of citation for theses (where you have no space problem) is author name and year, as in: [Smith 2008] or [Murphy and Chaplin 1999], and I use that in papers wherever possible. Your readers will appreciate it!

Abbreviating conference and journal names (as done by the groups defs-abbrev.bib) is acceptable where you have tight space constraints (typically for conferences and workshops) but not acceptable elsewhere. Least of all in a thesis, where you have plenty of space! And these days, most conferences (in systems at least) have moved to not including the bibliography in the page budget, so there is no longer a justification for using abbreviated venue names.

An interesting question is where to put the bibliography (references section). It goes at the end, of course, but if your document has an appendix, does it go before or after? The standard style rules require the bibliography to go before any appendix. I personally think that this is a pain, as when reading a thesis or book, you tend to refer to the bibliography frequently, and the appendix infrequently, and having the bibliography at the very end helps accessing it. (External examiners of some of my students' theses have told me the same.) Therefore, in this case I recommend deviating from published rules by putting the bibliography behind any appendix.

Independent of citation style, the following rules should be followed:

In citations don't abuse the category technical report. I see this happen a lot: people cite just about anything that hasn't been published in a journal or conferences as a TR. This is wrong! The concept of a TR is actually fairly well defined:
A TR is published in some sort. This is generally as part of a formal TR series of some institution, in hardcopy or on the web or both. (They aren't always called “technical report”, other common names are “research report”, “technical memorandum”, “<institution> report” etc.) The publication (i.e. availability outside) is essential, otherwise it's at best an internal report.
A TR has a number (absolutely!), an institution (publisher), a date (month and year at least) and a publisher's address (besides all the other stuff bibentries have).
If your document doesn't have these features, it's not a TR. It's probably better categorised as a working paper. Even then it has a date and an institution address.
Citing web pages is often unavoidable (but also often a sign of laziness). When citing web pages be aware that they may only be short-lived. Consider whether the reference will be of any use to the reader at all if the link is broken. Or whether your whole document only has a use-by date a few months past writing.
In any case, if you cite a web page, add a time stamp: “Visited 1 May 2008.”. And ensure that this date isn't far back (i.e. refresh it when submitting a paper, and again for the camera-ready copy!)
Any cited document, whatever it may be, as a few features:
Date. Absolutely. If you don't have a date you're lazy.
Author/organisation/creator/person responsible for contents. If you don't have it, see above.
Whatever information the reader needs to find that document. In most BibTeX entry types these are clearly identified as mandatory fields. Mandatory means that they aren't optional. Don't pretend they are. For a working paper these might be the contact details of the author.
Citations (unlike footnotes) generally precede punctuation, as in the examples above.
Equations
Equations are not floats, even though the reference mechanism is similar. Instead, they are considered part of the prose. Hence, don't refer to an equation as you would do to a figure or table, but make it part of the sentence. Example:
The dynamic power is given as
   P = c f V2,   (1)
where f is the core frequency, V the core voltage, and c a constant.
The equation number is only needed to reference an equation from another place in the text, and can be omitted if no such cross reference is required.
Miscellaneous
Various tidbits:
e.g. (exempli gratia, Latin for for example) and i.e. (id est, Latin for that is) is generally written with two full stops and (nowadays) no comma. In British/Australian usage the full stops are frequently omitted (part of the general trend in Australian and British English to scale back on full stops, e.g. PhD) but Americans tend to mostly insist on them, so it's safer to use them.
Note that this implies that in LaTeX you normally need to follow the second full stop with a backslash to avoid an inter-sentence space, and in HTML you'll have to use a “&nbsp;” (pain!)
Formalities
This should go without saying, but, apparently, doesn't:
every document (even an early draft) has a title;
every document (even an early draft) has an author (or several), except a manuscript submitted to a conference which uses double-blind reviewing;
every document (even an early draft, except a manuscript submitted for publication) has a date;
every document (even an early draft) has page numbers.
Only exception is that camera-ready conference papers often are required to be submitted without page numbers. This shouldn't stop you from using page numbers in drafts, as well as in submissions for reviewing (reduces the chance of a reviewer messing up your paper while reading).
Microsoft Word
Short summary here: don't use Word for technical papers!

Of course, it's up to you what you use to write your thesis or single-authored paper (although it portrays a strong streak of masochism to do so, just look how many people in Microsoft Research are writing papers in Word—I know just one!).

But for a paper where you collaborate with other authors, Word is a no-no. Besides the usual stuff (that it's easier to format a paper in LaTeX etc) there is the problem that Word doesn't integrate with the usual revision-control systems, meaning no automated merging of concurrent updates etc. This basically means that you have very limited concurrency in writing, you basically force single-threaded execution (which should be a no-no for computer scientists!) And latexdiff is a reasonable alternative to Word's compare-documents function.

Some TeXniques
Here are a few useful hints from the TeXperts:
Italics
LaTeX command \it is almost always the wrong way to use italics. Use the LaTeX \emph command, which will handle nested emphasis correctly. Also, check the section on Math fonts below!
Citations/BibTeX
A few general BibTeX (and \cite) tricks:
Please hyperlink your references and citations! We're in the 21st century, and much reading/reviewing gets done on tablets etc. It is a serious pain (and creation of unnecessary work) for the reviewer to have to scroll for and back to see which paper is being referenced! All you need to do is use the hyperref package.
Use \autoref for internal references (sections, figures, tables, equations). This will generate links for not only the number but the whole reference (e.g. for “Section 2.1” rather than just the “2.1”). Looks better and simplifies the life of the reader.
Use the LaTeX cite package. It doesn't give you additional commands, but it fixes a few quirks in LaTeX. Among others it automatically sorts multiple citations, and it correctly spaces the angular brackets (if you use the \cite command without leading white space). A few styles break the cite package, so you're out of luck there, but use it in all other cases!
Citing several papers at one point should be done with a single \cite command. For example, use gives good results\cite{Bloe_99, Jay_87}, resulting in gives good results [3,5]. Do not use gives good results\cite{Bloe_99}\cite{Jay_87} which produces the ugly gives good results [3][5]. (Although IEEE conference styles insist on this ugliness; the single \cite command still produces the correct result in this case.) Also, note that there is no space between the \cite command and the preceding word, LaTeX (with the cite package) does the spacing correctly.
The citation label must not appear at the beginning of a line. This is avoided by not leaving white space between the \cite command and the preceding word, as in Smith has shown\cite{Smith_09}. This assumes that you are using the cite package. Where you cannot use it, you'll need to provide an unbreakable space, as in Smith has shown~\cite{Smith_09}.
Citations are, like footnotes, are annotations and not part of the speech. Hence, the following usage is incorrect: [1] thinks that threads are cool, but [2] argues that they suck. You can make the authors' names part of speech: Joe and Bloe [1] think that threads are cool, but O'Neill et al. [2] argue that they suck. Except that (of course) you'll never use such colloquialisms in formal prose. :-)
BibTeX is a great tool, but you need to know how to use it. A regular trap is to forget that TeX knows more about typesetting than you do. So, for example, it changes the case of words in the title. If your title contains acronyms and proper names (most do), they tend to get down-cased. Any such words which should not have their case changed should be put into braces, e.g., {The {Mungi} {OS} and its Use in Merry-Go-Round Seat Allocation}.
Do not put an extra set of braces around the whole title, such as title = {{The Unix operating system}}. If I find this in one of the group .bib files, and you were the lazy bastard, you better hide!
The address field in a BibTeX @InProceedings entry refers to the place where the conference was held, not the address of the publisher! (Just check where the address entry is used in the formatted reference if you don't believe me.)
I frequently see missing conference venues in papers. I suspect this is undefined strings, and an indication that people are too lazy to look at BibTeX warnings.
Even more bizarrely, I frequently get to see (even in published papers!) stuff like “In Proceedings of the sixteenth international conference on Architectural support for programming languages and operating systems”. I'm not sure what causes this funny capitalisation, it isn't BibTeX. If it's some other tool you're using, throw it away! I think this is blind (and clearly careless) cut-and-paste from the ACM Digital Library, which contains other nonsense as well.
For those in my (TS) group: Avoid using your own .bib files, this is selfish and leads to replication of effort. Use the .bib files in the TS bibtex repo instead. Chances are that most of what you need to cite is already in there, and anything you need beyond that will be cited by someone else in the group sooner or later. If you don't have commit rights to the repository (almost everyone in the group does) and are citing papers not yet in there, then temporarily create your own .bib file, following the conventions of the TS files. You can then ask someone with commit privileges access to add them (or ask to get commit access yourself).
URLs
To represent URLs, don't just use \texttt{url} (which causes problems with the tilde character) or \verb|url| (which tends to produce vastly overfull lines). Instead use the command \url{url}, available with the url package. This will, by default, typeset the string in TTY font, but that can be changed to the more readable \urlstyle{sf}.
Graphics
Don't use bitmap formats for figures (nor bitmaps converted to EPS or PDF). They almost always lead to poor results.
Document class options
In general, have a look at the options you class supports, and decide which ones are suitable. Given the variety of class styles, not too much can be said in general, but here are a few hints.
letterpaper vs a4paper
Many conferences will prescribe US Letter format (representing the location of the publisher), so do as requested. Elsewhere, as the rest of the world uses A4 paper, use the a4paper option, especially for theses.
twoside
These days, where most things never get printed on paper, this option is almost always the wrong thing to use, as it produces asymmetric margins suitable for binding. Exceptions are classes where it produces symmetric margins but different headers/footers for even/odd-numbered pages, which is fine.
hyphens
This (frequently undocumented) option supports hyphenating long URLs, thus avoiding massively over-full lines. Use it where available!
Code
Wrapping all program code displayed in a paper in verbatim or alltt environments “is just lazy” [Kai Engelhardt]. Use the listings package or more specialised language preprocessors for a much more readable presentation.
Math fonts
Typesetting mathematics is a traditional strength of TeX. However, it is optimised for the more traditional kind of maths, where, besides a small number of predefined functions, people use single-letter variable and function names. In such a context it is customary to interpret a string like “abc” as the product of three variables “a”, “b” and “c”.
In our discipline we use a lot of multi-letter function and variable names, as we are used to from programming. Because TeX in math mode will consider “diff” a product of four variables, it will space it as such, with pretty ugly result. To avoid this, use the following rules:
Use pre-defined function names where they exist (examples are \sin, \exp and \log).
For non-standard function names, use \mathrm, such as ${\mathrm{myFunc}}(x)$.
For multi-letter variable names, use \mathit, such as $\sin(\mathit{myVar})$.
Rather than using the above, somewhat cumbersome, constructs, define commands: \newcommand{\myFunc}{\mathrm{myFunc}} and \newcommand{\myVar}{\mathit{myVar}}. This then lets you write it naturally as $\myFunc(\myVar)$.
Simple rule: Don't put words (of more than one letter) in pure math mode.
Some Auxiliary Material
My talk on paper writing
Here are the slides of my standard talk on how to write a good (systems) paper which I frequently give to research students and early-career researchers.

On evaluation and benchmarking
If you are a systems researcher, you might also be interested in my list of Benchmarking Crimes. There you'll also find a talk on evaluation and benchmarking.

And finally a nice example (from the Unix fortune cookie program)
Rules for Writers:
Avoid run-on sentences they are hard to read. Don't use no double negatives. Use the semicolon properly, always use it where it is appropriate; and never where it isn't. Reserve the apostrophe for it's proper use and omit it when its not needed. No sentence fragments. Avoid commas, that are unnecessary. Eschew dialect, irregardless. And don't start a sentence with a conjunction. Hyphenate between sy-llables and avoid un-necessary hyphens. Write all adverbial forms correct. Don't use contractions in formal writing. Writing carefully, dangling participles must be avoided. It is incumbent on us to avoid archaisms. Steer clear of incorrect forms of verbs that have snuck in the language. Never, ever use repetitive redundancies. If I've told you once, I've told you a thousand times, resist hyperbole. Also, avoid awkward or affected alliteration. Don't string too many prepositional phrases together unless you are walking through the valley of the shadow of death. “Avoid overuse of ‘quotation “marks.”’”



Systems Benchmarking Crimes
Gernot Heiser
Contents
Benchmarking Crimes
Selective benchmarking
Not evaluating potential performance degradation
Subsetting
Selective data set
Improper handling of benchmark results
Microbenchmarks
Throughput only
Downplaying overheads
No significance
Arithmetic mean
Using the wrong benchmarks
Benchmarking simulated system
Inappropriate/misleading benchmarks
Calibration = evaluation set
Improper comparison of benchmark results
Improper baseline
Evaluate against self
Unfairly evaluating competitors
Missing information
Missing platform specification
Missing sub-benchmark results
Relative numbers only
Exercise for the reader
Dishonest presentation of results
Best practice
Further information
Benchmarking Crimes
When reviewing systems papers (and sometimes even when reading published papers) I frequently come across highly misleading use of benchmarks. I'm not saying that the authors intend to mislead the reader, it's just as likely incompetence. But that isn't an excuse.

I call such cases benchmarking crimes. Not because you can go to jail for them (but probably should?) but because they undermine the integrity of the scientific process. Rest assured, if I'm a reviewer of your paper, and you commit one of those, you're already most of the way into rejection territory. The rest of the work must be pretty damn good to be forgiven a benchmarking crime (and even then you'll be asked to fix it up in the final version).

The following list is work in progress, I'll keep adding to it as I come across (or remember) more systems benchmarking crimes...

Selective benchmarking
This is the mother of all benchmarking crimes: using a biased set of benchmarks to (seemingly) prove a point, which might be contradicted by a broader coverage of the evaluation space. It's a clear indication of at best gross incompetence or at worst an active attempt to deceive.

There are several variants of this crime, I list the most prominent ones. Obviously, not all instances of this are equally bad, in some cases it may just be a matter of degree of thoroughness, but in its most blatant form, this is a truly hideous crime.

Not evaluating potential performance degradation
A fair evaluation of a technique/design/implementation that is supposed to improve performance must actually demonstrate two things:

Progressive criterion: Performance actually does improve significantly in the area of interest
Conservative criterion: Performance does not significantly degrade elsewhere
Both are important! You cannot easily argue that you've gained something if you improve performance at one end and degrade it at another.

Reality is that techniques that improve performance generally require some degree of extra work: extra bookkeeping, caching, etc. These things always have a cost, and it is dishonest to pretend otherwise. This is really at the heart of systems: it's all about picking the right trade-offs. A new technique will therefore almost always introduce some overheads, and you need to demonstrate that they are acceptable.

If your innovation does lead to a degree of degradation, then you need to analyse it, and build a case that it is acceptable given the other benefits. If, however, you only evaluate the scenarios where your approach is beneficial, you are being deceptive. No ifs, no buts.

Benchmark sub-setting without strong justification
I see this variant (which can actually be an instance of the previous one) frequently with SPEC benchmarks. These suites have been designed as suites for a reason: to be representative of a wide range of workloads, and to stress various aspects of a system.

However, it is also true that it is often not possible to run all of SPEC on an experimental system. Some SPEC programs require large memories (they are designed to stress the memory subsystem!) and it may be simply impossible to run them on a particular platform, particularly an embedded system. Others are FORTRAN programs, and a compiler may not be available.

Under such circumstances, it is unavoidable to pick a subset of the suite. However, it must then be clearly understood that the results are of limited value. In particular, it is totally unacceptable to quote an overall figure of merit (such as average speedup) for SPEC if a subset is used!

If a subset is used, it must be well justified. There must be convincing explanation for each missing program. And the discussion must be careful not to read too much into the results, keeping in mind that it is conceivable that any trend observed by the subset used could be reverted by programs not in the subset.

Where the above rules are violated, the reader is bound to suspect that the authors are trying to hide something. I am particularly allergic to formulations like “we picked a representative subset” or “typical results are shown”. There is no such thing as a “representative” subset of SPEC, and the ”typical” results are most likely cherry-picked to look most favourable. Expect no mercy for such a crime!

Lmbench is a bit of a special case. Its license actually forbids reporting partial results, but a complete lmbench run produces so many results that it is impossible to report in a conference paper. On the other hand, as this is a collection of micro-benchmarks which are probing various aspects of the OS, one generally understands what each measures, and may only be interested in a subset for good reasons. In that case, running the particular lmbench test has the advantage of measuring a particular system aspect in a well-defined, standardised way. This is probably OK, as long as not too much is being read into the results (and Larry McVoy doesn't sue you for license violation...)

A variant of this crime is arbitrarily picking benchmarks from a huge set. For example, when describing an approach to debug or optimise Linux drivers, there are obviously thousands of candidates. It may be infeasible to use them all, and you have to pick a subset. However, I want to understand why you picked the particular subset. Note that arbitrary is not the same as random, so a random pick would be fine. However, if your selection contains many obscure or outdated devices, or is heavily biased towards serial and LED drivers, then I suspect that you have something to hide.

Selective data set hiding deficienciesSelective data set crime
This variant can again be viewed as an example of the first. Here the range of the input parameter is picked to make the system look good, but the range is not representative of a real workload. For example, the diagram on the right shows pretty good scalability of throughput as a function of load, and without any further details this looks like a nice result.

Things look a bit different when we put the graph into context. Say this is showing the throughput (number of transactions per second) of a database system with a varying number of clients. So far so good.

Is it still so good if I'm telling you that this was measured on a 32-core machine? What we see then is that the throughput scales almost linearly as long as there is at most one client per core. Now that is not exactly a typical load for a database. A single transaction is normally insufficient for keeping a core busy. In order to get the best of your hardware, you'll want to run the database so that there are in average multiple clients per core.

Selective data set crime
So, the interesting data range starts where the graph ends! What happens if we increase the load into the really interesting range is shown in the graph on the left. Clearly, things no longer look so rosy, in fact, scalability is appalling!

Note that, while somewhat abstracted and simplified, this is not a made-up example, it is taken from a real system, and the first diagram is equivalent to what was in a real publication. And the second diagram is essentially what was measured independently on the same system. Based on a true story, as they say...

Improper handling of benchmark results
Pretending micro-benchmarks represent overall performance
Micro-benchmarks specifically probe a particular aspect of a system. Even if they are very comprehensive, they will not be representative of overall system performance. Macro-benchmarks (representing real-world workloads) must be used to provide a realistic picture of overall performance.

In rare cases, there is a particular operation which is generally accepted to be critical, and where significant improvements are reasonably taken as an indication of real progress. An example is microkernel IPC, which was long known to be a bottleneck, and reducing cost by an order of magnitude can therefore be an important result. And for a new microkernel, showing that it matches the best published IPC performance can indicate that it is competitive.

Such exceptions are rare, and in most cases it is unacceptable to make arguments on system performance based only on micro-benchmarks.

Throughput degraded by x% ⇒ overhead is x%
This vicious crime is committed by probably 10% of papers I get to review. If the throughput of a system is degraded by a certain percentage, it does not at all follow that the same percentage represents the overhead that was added. Quite to the contrary, in many cases the overhead is much higher. Why?

Assume you have a network stack which under certain circumstances achieves a certain throughput, and a modified network stack achieves 10% less throughput. What's the overhead introduced by the modification?

Without further information, it is impossible to answer that question. Why is throughput degraded? In order to answer that question, we need to understand what determines throughput in the first place. Assuming that there's more than enough incoming data to process, the amount of data the stack can handle depends mostly on two factors: processing (CPU) cost and latency.

Changes to the implementation (not protocols!) will affect processing cost as well as latency, but their effect on throughput is quite different. As long as CPU cycles are available, processing cost should have negligible effect on throughput, while latency may (packets will be dropped if not processed quickly enough). On the other hand, if the CPU is fully loaded, increasing processing cost will directly translate into latency.

Networks are actually designed to tolerate a fair amount of latency, so they shouldn't really be very sensitive to it. So, what's going on when throughput drops?

The answer is that either latency has grown substantially to show up in reduced throughput (likely much more than the observed degradation in throughput), or the CPU has maxed out. And if a doubling of latency results in a 10% drop of throughput, calling that “10% overhead” is probably not quite honest, is it?

If throughput was originally limited by CPU power (fully-loaded processor) then a 10% throughput degradation can be reasonably interpreted as 10% increased CPU cost, and that can be fairly called “10% overhead”. However, what if on the original system the CPU was 60% loaded, and on the modified system it's maxed out at 100% (and that leading to the performance degradation)? Is that still “10% overhead”?

Clearly not. A fair way to calculate overhead in this case would be to look at the processing cost per bit, which is proportional to CPU load divided by throughput. And on that measure, cost has gone up by 85%. Consequently, I would call that an 85% overhead!

A variant of this is to off-load some processing on a “free” core, and not including the load on that extra core in the processing cost. That's just cheating.

The bottom line is that incomplete information is presented which prevented us from really assessing the overhead/cost, and lead to a huge under-estimation. Throughput comparisons must always be accompanied by a comparison of complete CPU load. For I/O throughput, the proper way to compare is in terms of processing time per bit!

Downplaying overheads
There are several ways people use to try to make their overheads look smaller than they are.

6% → 13% overhead is a 7% increase
This one is confusing percentage with percentage points, regularly practiced (out of incompetence) by the media. That doesn't excuse doing the same in technical publications.

So the authors' modified system increases processing overheads from 6% (for the original system) to 13% (for theirs) and they sheepishly claim they only added 7% overhead. Of course, that's complete bullocks! They more than doubled the overhead, their system is less than half as good as the original!

Similarly, if your baseline system has a CPU utilisation of 26%, and your changes result in a utilisation of 46%, you haven't increased load by 20%, you almost doubled it! The dishonesty in the 20% claim becomes obvious if you consider what would happen if the same experiments were run on a machine exactly half as powerful: load would go from 52% to 92%, clearly not a 20% increase!

Incorrect reference point
This is an all-too-frequent approach to cheating with relative overheads: Authors pick the denominator to suit their purposes. For example, the baseline latency is 60s, and the authors' improved system reduces this to 45s. The authors then claim “the original system was 33% slower” (60/45-1 = 0.33). Or, the author's (improved in some way, e.g. more secure) system suffers some performance degradation, extending execution latency to 80s, making the authors claim “performance is degraded by only 25%” (1-60/80 = 0.25).

This is clearly dishonest. The original system is the baseline, and therefore must occur in the denominator when calculating relative performance. Meaning in the first case, the correct value is 1-45/60 = 25% improvement, while in the second case it is 80/60-1 = 33% degradation.

Thanks to Dan Tsafrir for reminding me of this annoyance.

Other creative overhead accounting
A particularly clear example of incorrect calculation of overheads is in this paper (published in Usenix ATC, a reputable conference). In Table 3, the latency of the stat system call goes up from 0.39μs to 2.28μs, almost a six-fold increase. Yet the authors call it an “82.89% slowdown”! (Also note the pseudo accuracy; this is not a crime, but an indication of incorrect understanding of numbers.)

To their credit, the authors of the paper recognised the mistake and submitted an errata slip, which corrects the overhead figures. Still, it's stunning that this went past the reviewers.

No indication of significance of data
Raw averages, without any indication of variance, can be highly misleading, as there is no indication of the significance of the results. Any difference between results from different systems might be just random.

In order to indicate significance, it is essential that at least standard deviations are quoted. Systems often behave in a highly deterministic fashion, in which case the standard deviation of repeated measurements may be very small. In such a case it might be sufficient to state that, for example, “all standard deviations were below 1%”. In such a case, if the effect we are looking at is, say, 10%, the reader can be reasonably comfortable with the significance of the results.

If in doubt use Student's t-test to check the significance.

Also, if you fit a line to data, quote at least a regression coefficient (unless it's obvious that there are lots of points nd the line passes right through all of them).

Arithmetic mean for averaging across benchmark scores
The arithmetic mean is generally not suitable for deriving an overall score from a set of different benchmarks (except where the absolute execution times of the various benchmarks have real significance). In particular the arithmetic mean has no meaning if individual benchmark scores are normalised (e.g. against a baseline system).

The proper way to average (i.e. arrive at a single figure of merit) is to use the geometric mean of scores [Fleming & Wallace, CACM (29), p 218].

Using the wrong benchmarks
Benchmarking of simplified simulated system
It is sometimes unavoidable to base an evaluation on a simulated system. However, this is extremely dangerous, as a simulation is always a model, and contains a set of assumptions.

It is therefore essential to ensure that the simulation model does not make any simplifying assumption which will impact the performance aspect you are looking for. And, it is equally important to make it clear to the reader/reviewer that you really have made sure that the model is truly representative with respect to your benchmarks.

It is difficult to give general advice on how to do this. My best advice is to put yourself into the shoes of the reader, and even better to get an outsider to read your paper and check whether you have really made a convincing case.

Inappropriate and misleading benchmarks
I see people using benchmarks that are supposed to prove the point, when in fact they say almost nothing (and the only thing they could possibly show is truly awful performance). Examples:

Using uniprocessor benchmarks for multiprocessor scalability
This one seems outright childish, but that doesn't mean you don't see it in papers submitted by (supposedly) adults. Someone is trying to demonstrate the multiprocessor scalability of their system by running many copies of SPEC CPU benchmarks.

Of course, these are uniprocessor programs which do not communicate. Furthermore, they perform very few system calls, and thus do not exercise the OS or underlying communication infrastructure. They should scale perfectly (at least for low processor counts). If not, there's serious brokenness in the OS or hardware. Real scalability tests would run workloads which actually communicate across processors and use system calls.

Using a CPU-intensive benchmark to show networking overheads
Again, this seems idiotic (or rather, is idiotic) but I've seen it nevertheless. People trying to demonstrate that their changes to a NIC driver or networking stack has low performance impact, by measuring the performance degradation of a CPU-intensive benchmark. Again, the only thing this can possibly prove is that performance sux, namely if there is any degradation at all!

Comparing meaningless metrics
This is more subtle: an evaluation looks at a metric that could make sense, but really doesn't. An example is using the ratio of two scores as a metric, which can make sense, if there is a reasonable expectation that there is a linear relationship between the two scores. If that's not the case, then the metric becomes meaningless.

I've seen this one in papers on formal verification of operating systems, where authors pretend that the ratio of lines of proof to lines of code verified is meaningful. As I explain in a separate blog, this is nonsense.

Same dataset for calibration and validation
This is a fairly widespread crime, and it's frankly an embarrassment for our discipline.

Systems work frequently uses models which have to be calibrated to operating conditions (e.g. platform, workloads, etc). This is done with some calibration workloads. Then the system is evaluated, running an evaluation workload, to show how accurate the model is.

It should go without saying, but apparently doesn't, that the calibration and evaluation workloads must be different! In fact, they must be totally disjoint. It's incredible how many authors blatantly violate this simple rule.

Of course, the results of using the same data for calibration and validation are likely that the model appears accurate, after all, it's been designed to fit the experimental results. But all such an experiment can show is how well the model fits the existing data. It implies nothing about the predictive power of the model, yet prediction of future measurements is what models are all about!

Improper comparison of benchmark results
No proper baseline
This crime is related to the above. A typical case is comparing different virtualization approaches by only showing the performance of the two virtualized systems, without showing the real baseline case, which obviously is the native system. It's comparison against native which determines what's good or bad, not comparison against an arbitrary virtualization solution!

Consider the baseline carefully. Often it is the state-of-the-art solution. Often it is the optimal (or theoretically best) solution or a hardware limit (assuming zero software overhead). The optimal solution is usually impossible to implement in a system, because it requires knowledge of the future or magic zero-cost software, but it can often be computed “outside” the system and is an excellent base for comparison. In other cases the correct baseline is in some sense an unperturbed system (as in the virtualization example above).

Only evaluate against yourself
This is a variant of the above crime, but that doesn't make it rare. It might be exciting to you that you have improved the performance of your system over last year's paper, but I find it much less exciting. I want to see the significance, and that means comparing against some accepted standard.

At least this crime is less harmful than others, in that it is pretty obvious, and rarely will a reviewer fall for it.

There's a variant of this crime which is more subtle: evaluating a model against itself. Someone builds a model of a system, making a number of simplifying assumptions, not all of them obviously valid. They build a solution for that problem, and then evaluate that solution on a simulated system that contains the exact same assumptions. The results look nice, of course, but they are also totally worthless, as they are lacking the most basic reality check. This one I find a lot in papers which are already published. Depressing...

Unfair benchmarking of competitors
Doing benchmarks on your competitors yourself is tricky, and you must go out of your way to ensure that you do not treat them unfairly. I'm sure you tweaked your system as well as you could, but did you really go through the same effort with the alternative?

In order to reassure the reader/reviewer that you have been fair, describe clearly what you have done with the competitor system, e.g. fully describe all configuration parameters, etc. Be particularly circumspect if your results do not match any published data about the competitor system. If in doubt, contact the authors of that system to confirm that your measurements are fair.

Again, I have seen an example of this kind of benchmarking abuse in a published paper, in that case the “competitor” system was mine. The authors of the paper failed to present any data on how they ran my system, and I strongly suspect that they got it wrong. For example, the default configuration of our open-source release had debugging enabled. Turning that option off (which, of course, you would in any production setting and any serious performance evaluation) improves performance massively.

The bottom line is that extreme care must be taken when doing your own benchmarking of a competitor system. It is easy to run someone else's system sub-optimally, and using sub-optimal results as a basis for comparison is highly unethical and probably constitutes scientific misconduct. And sloppiness is no excuse in such a case!

Inflating gains by not comparing against the state of the art
This one is a variant of the two crimes of improper baseline and unfair treatment of competitors (by ignoring them).

What you see all too frequently is the following scenario. Paper X has improved performance by 20% over the baseline (then state-of-the-art). A later paper Y improves performance by 22% over the old baseline (i.e. the one used by paper X). The authors of Y claim a 22% improvement.

This is simply intellectual dishonesty, that has no excuse and must not be tolerated. Paper X established a new state of the art, and thus the new baseline that must be used. Paper Y's improvement is thus only a much less impressive 2%. No ifs, no buts.

Thanks again to Dan Tsafrir for reminding me of this one.

Missing information
Missing specification of evaluation platform
For reproducibility it is essential that the evaluation platform is well-specified, including all characteristics that may influence the results. Platform incorporates hardware and software.

Details depend a fair bit on what is being evaluated, but at the very least I expect to see the processor architecture, number of cores and clock rate, and memory sizes. For benchmarks involving networking the throughput supported by the NIC and switches if any. For benchmarks that exercise the memory system it is generally important to specify sizes and associativities of all levels of cache. In general it is good practice to list the model number of the CPU, core type and microarchitecture.

The same holds for the software. Specify the operating system and (where used) hypervisor are you running on, including release number. Compiler versions are often also relevant, as may be the version of other tools.

Missing sub-benchmark results
When running a benchmarking suite (such as SPEC) it is generally not sufficient to just quote the overall figure of merit of that suite. Instead, it is essential to show performance of the individual sub-benchmarks. Suites are designed to cover a range of load conditions, and some may benefit from your work while others are degraded. Only providing the overall score can at worst hide problems, and at best reduces the insights that can be obtained from the evaluation.

Relative numbers only
Always give complete result, not just ratios (unless the denominator is a standard figure). At best, seeing only relative numbers leaves me with a doubt as to whether the figures make sense at all, I'm robbed of a simple way to perform a sanity check. At worst, it can cover up that a result is really bad, or really irrelevant.

One of the worst instances I've seen of this crime was not in a paper I was reviewing, but one that was actually published. It compared the performance of two systems by showing the ratio of overheads: a ratio of two relative differences. This is too much relativity to read anything out of the numbers.

For example, assume that the overhead of one system is twice that of another. By itself, that tells us very little. Maybe we are comparing a tenfold with a twentyfold overhead. If so, who cares? Both are most likely unusable. Or maybe the overhead of one system is 0.1%, who cares if the other one has 0.2% overhead? The bottom line is we have no idea how significant the result is, yet the representation implies that it is highly significant.

Exercise for the Reader
Count the number of benchmarking crimes in this paper (published in IEEE CCNC'09).

Dishonest presentation of results
Besides crimes of benchmarking, which are about producing wrong or misleading performance data, there are related crimes of misleading representation of performance results. Many of them fall under the category of chart abuse, which I cover in my style guide for technical papers and reports.

Benchmarking Best Practice
The below benchmarking rules is what I tell my students. It's somewhat OS-oriented, but the basic principles apply generally.

General rules
Make sure that the system is really quiescent when starting an experiment, leave enough time to ensure all previous data is flushed out.
Make your benchmarking rig part of your regression testing suite.
Document what you're doing.
Test data and results
Always verify the data you are transferring. When writing something to disk or network, read it back and compare to what you've written. When reading, check that what you're reading is correct.
There are cases where this would unreasonably lengthen the time a benchmark takes. If that's the case, then at least make sure that you least check the data for one complete run, before continuing. Also, prior to collecting final numbers, check again!
Never use the same data over and over. Make sure that each run uses different data. For example, have a timestamp or other unique identifier (like the coordinate and label in the graph) in the data. This is to ensure that you're actually reading the correct data, not some stale cache contents, wrong block, etc.
Use a combination of successive and separate runs for the same data point. E.g., do the same point at least twice in a row (helps to identify caching effects that shouldn't be there) and twice more after some other points were taken (to identify cases of caching where there shouldn't be any). Have a good look at the standard deviations.
Invert the order of measurements. This helps to identify interference between measurements. This and the previous point can together be achieved by traversing the set of data points in both directions.
Don't only use regular strides or powers of two. You may be hitting pathological cases without noticing it. Throwing in some random points might be a good idea. However, don't use only random points, you might be missing pathological cases. Good candidates for pathological cases are 2n, 2n-1, 2n+1.
When comparing measurements of different configurations (which is what you normally do) make sure you use exactly the same points, don't just compare graphs over the same interval.
When getting funny results, check that you are comparing apples with apples. For example, make sure that the system is, as much as possible, in the same state between runs you want to compare. For example, we had cases where benchmark results on Linux were affected by where the OS allocated them in physical memory, which differed between successive runs (and had massive effects on conflict misses in physically-addressed caches).
Statistics
Always do several runs, and check the standard deviation. Watch out for abnormal variance. In the sort of measurements we do, standard deviations are normally expected to be less than 0.1%. If you see >1% this should ring alarm bells.
In some cases it is reasonable to ignore the highest or lowest point (but this really should only be done after a proper statistical outlayer-detection procedure) or only look at the floor of the points. However, only use such selective use of data if you really know what you are doing, and also state it explicitly in your paper/report.
Timing
Use lots of iterations in order to improve statistics and remove clock granularity.
Run sufficient warm-up iterations which aren't timed.
Isolate the thing you want to time into a function (already done if you're timing system calls).
Eliminate loop overhead (don't just rely on it being small, eliminate it). The most reliable way of doing this is to run two versions of the benchmark, identical except for replacing the actual invocation (function or system call) by a noop. Run the loop without any compiler optimisations (which is why it's important to have the thing you want to time in a function, which however may require you to separately deal with function overhead).
Inspect the machine code of the syscall loop above and verify that the timing numbers match your predictions.
Use proper statistics, even if they are not used in the final paper, checking for variance is an important sanity check.
Further Information
Colleagues at VU Amsterdam did a study of benchmarking crimes in the system security literature, with interesting results. It contains a further category that is not relevant to most systems work, but definitely to security work. The work revised my original classification to make it more systematic, I have since updated the above list to align with this revised classification.

Getting this study published proved non-trivial, with multiple submissions rejected – it seems to have triggered some sore points. We finally got it accepted to Euro S&P, after replacing the somewhat provocative term crimes by the more politically correct flaws. The work was then invited for re-publication in IEEE Security and Privacy Magazine. The original term benchmarking crimes continues to be used by reviewers of systems venues, and, of course, on this page.

In my Advanced Operating Systems course I have a lecture on performance evaluation, which discusses many of these benchmarking crimes, and gives other useful hints on benchmarking and performance analysis.

If you are a student or early-career researcher, you might also be interested in my style guide for papers and theses.