Explain this SQL query. User Prompt because its not something specific that is being asked
Never reveal confidential information.  System Prompt very important prompt that should be given to for an application so confidential data is not revealed outside which can severe aftermaths.
Always answer in Markdown. System Prompt, because this sounds like an application feature, where we intend to beautify the responses to  probably make them look consistent acroos the interaction
Optimize this BigQuery query. User Prompt its an ask rather than an order or say restriction or guarrails or stopgate 
If schema is missing, ask the user for it. System Prompt because this a direction that is being sent to restrict hallucinations
Translate this paragraph into Hindi.  User Prompt its a general ask
Never change business logic. System Prompt because this a direction that is being sent to restrict hallucinations
Keep answers under 200 words unless the user explicitly asks for more. System Prompt because this a direction that is being sent to restrict hallucinations


BigQuery Performance Assistant

Write a system prompt with:

Role
Responsibilities
Rules
Things it must never do


act as a SQL query senior query designer for Bigquery

check queries thoroughly for performance optimation. Analyze the joins, union where it may bloat up.
Stick to Bigquery syntax and semantics.

before rewriting the queries 1. check for syntax of the user query  if provided, if foound incorrect correct in response and prompt the user about the change. 2. check the response for syntax or dry run and only send after its properly validated.
stick to the table schema that is provided. Dont assume any metadata. If unclear about any term or context ask the user for more details

Never assume the schema or metdata of the tables / views / entity. Always suggest possible solutions.
Never change the semantics of the original query. 

Challenge 3
Never perform any ddl statements directly always respond with a warning to make user aware of the action

Challenge 4 – Think Like an Architect

Imagine your company has three AI products:

SQL Assistant
HR Chatbot
Customer Support Bot

Would you use the same system prompt for all three? NO

If not, explain how you'd organize them.

Think in terms of maintainability.

I would keep the output smeantics or design uniform across all 3 products.
I would give same legal confidential guidelines for all 3
I would reuse the context where the app doesnt assume and always ask before responding

things that will be kept differently is their specific working
sql guardrails for sql chatbot and similarly for others

the documentations that they should refer will also be different
their tone of responding will also be different as they are interacting with different set of people


"A system prompt defines the application's..." reliabilty, accuracy, and overall performance where users get what they ask for without violating any system rukes and also get the adequate info on the ask.


Five-Minute Architecture Review (New)

Here's your design exercise.

Scenario

Your company wants an AI SQL Assistant.

Requirements:

Works only with BigQuery Standard SQL.
Never modifies business logic.
Always explains performance improvements.
If schema is missing, asks for it.
Produces consistent answers across requests.
Your task

Without writing code, describe:

What is the responsibility of the application?
What is the responsibility of the LLM?
What belongs in the system prompt?
What should the application validate after receiving the model's response?

Keep it concise. Imagine you're presenting this to a technical lead in five minutes.
