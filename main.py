from data_forge import forge, column

cols = [
    column("name", "string", "The name of the person this article is about."),
    column("killed", "year | none", "Year when they were killed, or none otherwise"),
    column("arrested", "list[year]", ""),
    column("executed", "year | none", ""),
    column(
        "attempt",
        "list[year]",
        "",
    ),
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
