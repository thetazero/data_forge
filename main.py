from data_forge import forge, column

cols = [
    column("name", "string", "The name of the person this article is about."),
    column("military_experience", "true|false",
           "If the person has military experience"),
    column("citizienship", "list[str]",
           "List of citizienships the person has had."),
    column("birth_date", "date",
           "The date of birth of the person, just the year, like 1948."),
]
urls = ["https://en.wikipedia.org/wiki/Osama_bin_Laden",
        "https://en.wikipedia.org/wiki/Saleh_Al-Qaraawi",
        "https://en.wikipedia.org/wiki/Abu_Bakar_Ba%27asyir"]
res = forge(cols, urls)

for r in res.parsed_result:
    print(r)
