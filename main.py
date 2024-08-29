from data_forge import forge, column

cols = [
    column("name", "string", "The name of the person this article is about."),
    column("military_experience", "true|false",
           "If the person has military experience"),
    column("citizenship", "list[str]",
           "List of citizenships the person has had."),
    column("birth_date", "date",
           "The date of birth of the person, just the year, like 1948."),
    column("education", "Unknown | PhD | Master | Bachelor | Associate | High School | Secondary | Primary",
           "The highest level of education the person has completed, or Unknown if it is not known."),
    column("area_of_study", "string",
           "The area of study the person has studied in."),
    column("religion", "Christianity | Islam | Hinduism | Judaism | Buddhism | Sikhism | Other | None | Uknown", "The religion that the person identifies with, if it is something else then write it, or unknown if it is not known."),
]
urls = [
    "https://en.wikipedia.org/wiki/Osama_bin_Laden",
#     "https://en.wikipedia.org/wiki/Saleh_Al-Qaraawi",
#     "https://en.wikipedia.org/wiki/Abu_Bakar_Ba%27asyir",
#     "https://en.wikipedia.org/wiki/Gulbuddin_Hekmatyar",
]
res = forge(cols, urls)

for r in res.parsed_result:
    print(r)

res.to_csv("output/result.csv")
res.to_json("output/result.json")
