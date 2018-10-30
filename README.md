# GAP Coreference Dataset

GAP is a gender-balanced dataset containing 8,908 coreference-labeled pairs of (ambiguous pronoun, antecedent name), sampled from Wikipedia and released by [Google AI Language](https://ai.google/research/teams/language/) for the evaluation of coreference resolution in practical applications.

http://goo.gl/language/gap-coreference

## Motivation

Coreference resolution is an important task for natural language understanding and the resolution of ambiguous pronouns a longstanding challenge.
Nonetheless, existing corpora do not capture ambiguous pronouns in sufficient volume or diversity to accurately indicate the practical utility of models.

[Google AI Language's](https://ai.google/research/teams/language/) GAP dataset is an evaluation benchmark comprising 8,908 coreference-labeled pairs of (ambiguous pronoun, antecedent name), sampled from Wikipedia to provide diverse coverage of challenges posed by real-world text.
Importantly, GAP is gender-balanced to address the gender bias in coreference systems noted in our and other's analysis.

More details are available in [our paper](https://arxiv.org/abs/1810.05201) (which should be cited if you use or discuss GAP in your work):

</p>
<div class="highlight highlight-source-shell"><pre>
@inproceedings{webster2018gap,
  title =     {Mind the GAP: A Balanced Corpus of Gendered Ambiguou},
  author =    {Webster, Kellie and Recasens, Marta and Axelrod, Vera and Baldridge, Jason},
  booktitle = {Transactions of the ACL},
  year =      {2018},
  pages =     {to appear},
}
</pre></div>

## Dataset Description

The GAP dataset release comprises three .tsv files, each with eleven columns.

The files are:
 * **test** 4,000 pairs, to be used for official evaluation
 * **development** 4,000 pairs, may be used for model development
 * **validation** 908 pairs, may be used for parameter tuning

The columns contain:

Column | Header         | Description
:-----:|----------------|--------------------------------------------
1      | ID             | Unique identifer for an example (two pairs)
2      | Text           | Text containing the ambiguous pronoun and two candidate names. About a paragraph in length
3      | Pronoun        | The pronoun, text
4      | Pronoun-offset | Character offset of Pronoun in Column 2 (Text)
5      | A ^            | The first name, text
6      | A-offset       | Character offset of A in Column 2 (Text)
7      | A-coref        | Whether A corefers with the pronoun, TRUE or FALSE
8      | B ^            | The second name, text
9      | B-offset       | Character offset of B in Column 2 (Text)
10     | B-coref        | Whether B corefers with the pronoun, TRUE or FALSE
11     | URL ^^         | The URL of the source Wikipedia page

^ Please note that systems should detect mentions for inference automatically, and access labeled spans only to output predictions.

^^ Please also note that there are two task settings, *snippet-context* in which the URL column may **not** be used, and *page-context* where the URL, and the denoted Wikipedia page, may be used.

## Benchmarks

Performance on GAP may be benchmarked against the syntactic parallelism baseline from our above paper on the test set:

Task Setting      | M    | F    |  B     | O
:----------------:|------|------|--------|------
*snippet-context* | 69.4 | 64.4 | *0.93* | 66.9
*page-context*    | 72.3 | 68.8 | *0.95* | 70.6

where the metrics are F1 score on **M**asculine and **F**eminine examples, **O**verall, and a **B**ias factor calculated as **F** / **M**.

## Contact
To contact us, please use gap-coreference@google.com
