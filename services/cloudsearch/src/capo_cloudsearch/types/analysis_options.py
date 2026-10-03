"""Generated from Smithy shape ``com.amazonaws.cloudsearch#AnalysisOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.algorithmic_stemming
    import capo_cloudsearch.types.string


class AnalysisOptions(TypedDict, closed=True):
    synonyms: NotRequired["capo_cloudsearch.types.string.String"]
    """<p>A JSON object that defines synonym groups and aliases. A synonym group is an array of arrays, where each sub-array is a group of terms where each term in the group is considered a synonym of every other term in the group. The aliases value is an object that contains a collection of string:value pairs where the string specifies a term and the array of values specifies each of the aliases for that term. An alias is considered a synonym of the specified term, but the term is not considered a synonym of the alias. For more information about specifying synonyms, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html#synonyms">Synonyms</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>"""
    stopwords: NotRequired["capo_cloudsearch.types.string.String"]
    """<p>A JSON array of terms to ignore during indexing and searching. For example, <code>["a", "an", "the", "of"]</code>. The stopwords dictionary must explicitly list each word you want to ignore. Wildcards and regular expressions are not supported. </p>"""
    stemming_dictionary: NotRequired["capo_cloudsearch.types.string.String"]
    """<p>A JSON object that contains a collection of string:value pairs that each map a term to its stem. For example, <code>{"term1": "stem1", "term2": "stem2", "term3": "stem3"}</code>. The stemming dictionary is applied in addition to any algorithmic stemming. This enables you to override the results of the algorithmic stemming to correct specific cases of overstemming or understemming. The maximum size of a stemming dictionary is 500 KB.</p>"""
    japanese_tokenization_dictionary: NotRequired[
        "capo_cloudsearch.types.string.String"
    ]
    """<p>A JSON array that contains a collection of terms, tokens, readings and part of speech for Japanese Tokenizaiton. The Japanese tokenization dictionary enables you to override the default tokenization for selected terms. This is only valid for Japanese language fields.</p>"""
    algorithmic_stemming: NotRequired[
        "capo_cloudsearch.types.algorithmic_stemming.AlgorithmicStemming"
    ]
    """<p>The level of algorithmic stemming to perform: <code>none</code>, <code>minimal</code>, <code>light</code>, or <code>full</code>. The available levels vary depending on the language. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/text-processing.html#text-processing-settings" target="_blank">Language Specific Text Processing Settings</a> in the <i>Amazon CloudSearch Developer Guide</i> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AnalysisOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "synonyms" in value:
        pairs.append((f"{key_prefix}Synonyms", str(value["synonyms"])))
    if "stopwords" in value:
        pairs.append((f"{key_prefix}Stopwords", str(value["stopwords"])))
    if "stemming_dictionary" in value:
        pairs.append(
            (f"{key_prefix}StemmingDictionary", str(value["stemming_dictionary"]))
        )
    if "japanese_tokenization_dictionary" in value:
        pairs.append(
            (
                f"{key_prefix}JapaneseTokenizationDictionary",
                str(value["japanese_tokenization_dictionary"]),
            )
        )
    if "algorithmic_stemming" in value:
        import capo_cloudsearch.types.algorithmic_stemming

        capo_cloudsearch.types.algorithmic_stemming.serialize_query(
            value["algorithmic_stemming"], pairs, f"{key_prefix}AlgorithmicStemming"
        )


def deserialize_query(el: Element) -> AnalysisOptions:
    out: AnalysisOptions = {}  # type: ignore[typeddict-item]
    child_synonyms = el.find("Synonyms")
    if child_synonyms is not None:
        out["synonyms"] = str(child_synonyms.text or "")
    child_stopwords = el.find("Stopwords")
    if child_stopwords is not None:
        out["stopwords"] = str(child_stopwords.text or "")
    child_stemming_dictionary = el.find("StemmingDictionary")
    if child_stemming_dictionary is not None:
        out["stemming_dictionary"] = str(child_stemming_dictionary.text or "")
    child_japanese_tokenization_dictionary = el.find("JapaneseTokenizationDictionary")
    if child_japanese_tokenization_dictionary is not None:
        out["japanese_tokenization_dictionary"] = str(
            child_japanese_tokenization_dictionary.text or ""
        )
    child_algorithmic_stemming = el.find("AlgorithmicStemming")
    if child_algorithmic_stemming is not None:
        import capo_cloudsearch.types.algorithmic_stemming

        out["algorithmic_stemming"] = (
            capo_cloudsearch.types.algorithmic_stemming.deserialize_query(
                child_algorithmic_stemming
            )
        )
    return out
