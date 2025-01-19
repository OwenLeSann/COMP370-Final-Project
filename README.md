# Megalopolis Film Criticism Analysis
Welome/Overview - What is this project? What is it for?

The Megalopolis Film Criticism Analysis is a dats science project aiming to answer inform Lionsgate Films of the visibility and reception of Megalopolis by Francis Ford Coppola relative to other movies that have come out at a similar time. In particular we aim to answer two questions:

1. What are the 10 words with the highest tf-idf scores characterizing whether the online journalistic criticisms of Megalopolis are positive or negative?
2. What proportion of articles mention Megalopolis relative to mentions of other movies that were released within four weeks before or after Megalopolis' box-office debut?

Details regarding the assumptions and refinements in our question formulation can be found [here](https://github.com/OwenLeSann/COMP370-Final-Project/blob/main/report/question_formulation.txt).

We are using the [newscatcher](https://newscatcherapi.com/) to source over 500 non-duplicate journal movie criticism articles from the web. Five movies all published within a few days of Megalopolis (Megalopolis, The Substance, Joker 2, The Wild Robot, and Venom) and sampled from a +- 8 week interval of September 27, 2024 (the theatrical debut of Megalopolis) to avoid bias in the coverage of Megalopolis as opposed to other movies featured in the study. The scripts used to source and organize this data are included in the scripts directory.

All of the details regarding how our data was sourced, annotated, and analyzed, in addition to our results and conclusions are summarized in our [final report](https://github.com/OwenLeSann/COMP370-Final-Project/blob/main/report/megalopolis_critical_reception.pdf)

## Authors
Owen Le Sann\
Lucas Loghin\
Nino Lombardi

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/OwenLeSann/COMP370-Final-Project/blob/main/LICENSE) file for details.

