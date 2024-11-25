# Megalopolis Film Criticism Analysis
Welome/Overview - What is this project? What is it for?

The Megalopolis Film Criticism Analysis is a dats science project aiming to answer inform Lionsgate Films of the visibility and reception of Megalopolis by Francis Ford Coppola relative to other movies that have come out at a similar time. In particular we aim to answer two questions:

1. What are the 10 words with the highest tf-idf scores characterizing whether the online journalistic criticisms of Megalopolis are positive or negative?
2. What proportion of articles mention Megalopolis relative to mentions of other movies that were released within four weeks before or after Megalopolis' box-office debut?

Details regarding the assumptions and refinements in our question formulation can be found [here](https://github.com/OwenLeSann/COMP370-Final-Project/blob/main/question_formulation.txt).

All of the details regarding how our data was sourced, annotated, and analyzed, in addition to our results and conclusions can be found in our final report listed below!

### TODOs
notes from author(s) to other authors/users

* In the formal report, it may be a good idea to add a definitions section for infrequently used terms such as 'journalistic criticism' and its distinction from 'academic criticism' concerning [film criticism](https://en.wikipedia.org/wiki/Film_criticism).

* Prove if there exists evidence suggesting that a greater volume of press coverage is directly corelated to greater gain or loss in box office earnings respective of positive or negative criticisms.

* Maybe consider formatting question formulation text file in markdown.

* So as to avoid bias, data should probably be randomly sampled from NewsApi: look into how we should sample data/how many API calls we'll need to/can perform (given sampling and time constraints).

* Question may need to be reformulated depending on available data and how annotation/analysis goes.

* Grammar/spelling check final report and all .md/.txt files

### Gotchas
TODO: Nasty surprises to be aware of

## Getting Started
Maybe break these into subsections for each technical part of the DS process: Data collection, annotation, analysis.
### Prerequisites
TODO: Tools, programming languages and libraries needed to interact with project.

For collecting the data we used the following tools:
* MiniConda
* Python
    - csv
    - argparse
    - requests
    - datetime
    - pandas
* Jupyter Notebook

All on Ubuntu 22 Linux environment hosted on Amazon Lightsail EC2 instance.

### Installing
TODO: Steps to install these tools.

### Data
We are using the [newscatcher](https://newscatcherapi.com/) to source over 500 non-duplicate journal movie criticism articles from the web. Five movies all published within a few days of Megalopolis (Megalopolis, The Substance, Joker 2, The Wild Robot, and Venom) and sampled from a +- 6 week interval of September 27, 2024 (the theatrical debut of Megalopolis) to avoid bias in the coverage of Megalopolis as opposed to other movies featured in the study. The scripts used to source and organize this data are included in the scripts directory.

## Usage

Remove below subsection later.
### Editing .md Files in VSCode
Here are the steps to write and preview Markdown in VS Code for Mac:

1. Create a new VS Code doc, saved as a markdown file.

2. Press CMD (⌘) + \ to Split the Editor.

3. Right-click in the new split-view and press CMD (⌘) + SHIFT + V.

You now have markdown on the left and the rendered result on the right.

### Usage steps
TODO:
Steps to use tools provided in this project.

## Report
TODO: Section to link final report discussing all findings, . May need to detail steps to access report.

## Authors
Owen Le Sann\
Lucas Loghin\
Nino Lombardi

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/OwenLeSann/COMP370-Final-Project/blob/main/LICENSE) file for details.

