article_summaries = {
    "article_1": "Subject-matter and objectives: This article outlines the GDPR's purpose, which is to protect individuals' rights regarding their personal data and to regulate the processing of such data.",
    "article_2": "Material scope: Specifies the data processing activities that fall under the GDPR, including processing in the context of EU member states' activities, regardless of whether the processing occurs in the EU or not.",
    "article_3": "Territorial scope: Defines the geographical scope of the GDPR, applying to organizations based in the EU and those outside the EU that offer goods or services to, or monitor the behavior of, EU data subjects.",
    "article_4": "Definitions: Provides definitions for key terms used in the regulation, such as 'personal data', 'processing', 'controller', and 'processor'.",
    "article_5": "Principles relating to processing of personal data: Lists the core principles for processing personal data, including lawfulness, fairness, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity, and confidentiality.",
    "article_6": "Lawfulness of processing: Specifies the lawful bases for processing personal data, such as consent, contract necessity, legal obligation, vital interests, public task, and legitimate interests.",
    "article_7": "Conditions for consent: Details the conditions for obtaining valid consent from data subjects, emphasizing that consent must be freely given, specific, informed, and unambiguous.",
    "article_8": "Conditions applicable to child's consent in relation to information society services: Sets the age of consent for data processing related to information society services at 16, with the possibility for member states to lower it to no less than 13 years.",
    "article_9": "Processing of special categories of personal data: Prohibits processing of sensitive data (e.g., racial or ethnic origin, political opinions, religious beliefs) unless specific conditions are met, such as explicit consent or necessity for certain legal purposes.",
    "article_10": "Processing of personal data relating to criminal convictions and offences: States that processing personal data related to criminal convictions and offences requires a legal basis under EU or member state law.",
    "article_11": "Processing which does not require identification: Covers processing of data that doesn't require the identification of a data subject, setting limitations and obligations for controllers in such cases.",
    "article_12": "Transparent information, communication and modalities for the exercise of the rights of the data subject: Obligates controllers to provide information about data processing in a concise, transparent, and easily accessible form.",
    "article_13": "Information to be provided where personal data are collected from the data subject: Details the information that must be provided to data subjects when their data is collected directly, including the purpose of processing and the data retention period.",
    "article_14": "Information to be provided where personal data have not been obtained from the data subject: Specifies the information to be provided when data is not obtained directly from the data subject, including the source of the data.",
    "article_15": "Right of access by the data subject: Grants data subjects the right to access their personal data and obtain copies of it, along with other details about how and why their data is processed.",
    "article_16": "Right to rectification: Gives data subjects the right to have inaccurate personal data corrected and incomplete data completed.",
    "article_17": "Right to erasure ('right to be forgotten'): Allows data subjects to have their personal data erased under certain conditions, such as when the data is no longer necessary for its original purpose.",
    "article_18": "Right to restriction of processing: Provides data subjects the right to restrict processing of their data under certain circumstances, such as when the accuracy of the data is contested.",
    "article_19": "Notification obligation regarding rectification or erasure of personal data or restriction of processing: Requires controllers to notify all recipients of the data about any rectification, erasure, or restriction of processing, unless this proves impossible or involves disproportionate effort.",
    "article_20": "Right to data portability: Grants data subjects the right to receive their personal data in a structured, commonly used, and machine-readable format, and to transfer that data to another controller.",
    "article_21": "Right to object: Gives data subjects the right to object to the processing of their personal data based on certain grounds, including processing for direct marketing, research, or based on a public or legitimate interest."
}

choose_article_prompt_template = """
The following is a request from a user who whats to get information from GDPR articles - {request}

You have access to the articles but you need to find the right article, out of 21, which contains the information needed to answer user's request.
To help you with the decision I will give you the list of all 21 article descriptions below, try to read carefuly and understand which article contains the information about the request

article_1: Subject-matter and objectives: This article outlines the GDPR's purpose, which is to protect individuals' rights regarding their personal data and to regulate the processing of such data.
article_2: Material scope: Specifies the data processing activities that fall under the GDPR, including processing in the context of EU member states' activities, regardless of whether the processing occurs in the EU or not.
article_3: Territorial scope: Defines the geographical scope of the GDPR, applying to organizations based in the EU and those outside the EU that offer goods or services to, or monitor the behavior of, EU data subjects.
article_4: Definitions: Provides definitions for key terms used in the regulation, such as 'personal data', 'processing', 'controller', and 'processor'.
article_5: Principles relating to processing of personal data: Lists the core principles for processing personal data, including lawfulness, fairness, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity, and confidentiality.
article_6: Lawfulness of processing: Specifies the lawful bases for processing personal data, such as consent, contract necessity, legal obligation, vital interests, public task, and legitimate interests.
article_7: Conditions for consent: Details the conditions for obtaining valid consent from data subjects, emphasizing that consent must be freely given, specific, informed, and unambiguous.
article_8: Conditions applicable to child's consent in relation to information society services: Sets the age of consent for data processing related to information society services at 16, with the possibility for member states to lower it to no less than 13 years.
article_9: Processing of special categories of personal data: Prohibits processing of sensitive data (e.g., racial or ethnic origin, political opinions, religious beliefs) unless specific conditions are met, such as explicit consent or necessity for certain legal purposes.
article_10: Processing of personal data relating to criminal convictions and offences: States that processing personal data related to criminal convictions and offences requires a legal basis under EU or member state law.
article_11: Processing which does not require identification: Covers processing of data that doesn't require the identification of a data subject, setting limitations and obligations for controllers in such cases.
article_12: Transparent information, communication and modalities for the exercise of the rights of the data subject: Obligates controllers to provide information about data processing in a concise, transparent, and easily accessible form.
article_13: Information to be provided where personal data are collected from the data subject: Details the information that must be provided to data subjects when their data is collected directly, including the purpose of processing and the data retention period.
article_14: Information to be provided where personal data have not been obtained from the data subject: Specifies the information to be provided when data is not obtained directly from the data subject, including the source of the data.
article_15: Right of access by the data subject: Grants data subjects the right to access their personal data and obtain copies of it, along with other details about how and why their data is processed.
article_16: Right to rectification: Gives data subjects the right to have inaccurate personal data corrected and incomplete data completed.
article_17: Right to erasure ('right to be forgotten'): Allows data subjects to have their personal data erased under certain conditions, such as when the data is no longer necessary for its original purpose.
article_18: Right to restriction of processing: Provides data subjects the right to restrict processing of their data under certain circumstances, such as when the accuracy of the data is contested.
article_19: Notification obligation regarding rectification or erasure of personal data or restriction of processing: Requires controllers to notify all recipients of the data about any rectification, erasure, or restriction of processing, unless this proves impossible or involves disproportionate effort.
article_20: Right to data portability: Grants data subjects the right to receive their personal data in a structured, commonly used, and machine-readable format, and to transfer that data to another controller.
article_21: Right to object: Gives data subjects the right to object to the processing of their personal data based on certain grounds, including processing for direct marketing, research, or based on a public or legitimate interest.

Respond only with the key and nothing else, for example - article_11
Only answer None if no article matches the request.
"""

modify_request_prompt_template = """
User wrote the following request - {request}, I need to search their request in a vector database of GDPR articles, I need you to modify the request in a way that I can perform better search because it will only contain the necessary information.
With each user request try to understand the information they are looking for and rephrase it in a way that I can perform a search with that, use the keywords in the sentence.
Don't write anything else except for the sentence itself. Don't say sure here is your... ONLY RETURN THE MODIFIED SENTENCE!!!
"""

final_answer_prompt = """
You are a GDPR professional assistant made to help humans by answering all of their questions regarding several of GDPR compliance articles, more specificaly 1 to 21.

These are all of your previous conversations - {chat_history}

Here is the human's latest request - {request}

And finaly here are relevant document chunks joined with '\\n-----\\n' found in the article that might help you generate a good answer - {relevant_documents}

Pay close attention to the request and make sure to properly fulfil.

{human_input}
"""