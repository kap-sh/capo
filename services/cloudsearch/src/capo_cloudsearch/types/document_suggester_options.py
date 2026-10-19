"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DocumentSuggesterOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.field_name
    import capo_cloudsearch.types.string
    import capo_cloudsearch.types.suggester_fuzzy_matching


class DocumentSuggesterOptions(TypedDict, closed=True):
    source_field: "capo_cloudsearch.types.field_name.FieldName"
    """<p>The name of the index field you want to use for suggestions. </p>"""
    fuzzy_matching: NotRequired[
        "capo_cloudsearch.types.suggester_fuzzy_matching.SuggesterFuzzyMatching"
    ]
    """<p>The level of fuzziness allowed when suggesting matches for a string: <code>none</code>, <code>low</code>, or <code>high</code>. With none, the specified string is treated as an exact prefix. With low, suggestions must differ from the specified string by no more than one character. With high, suggestions can differ by up to two characters. The default is none. </p>"""
    sort_expression: NotRequired["capo_cloudsearch.types.string.String"]
    """<p>An expression that computes a score for each suggestion to control how they are sorted. The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of 2^31-1. A document's relevance score is not computed for suggestions, so sort expressions cannot reference the <code>_score</code> value. To sort suggestions using a numeric field or existing expression, simply specify the name of the field or expression. If no expression is configured for the suggester, the suggestions are sorted with the closest matches listed first.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DocumentSuggesterOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SourceField", str(value["source_field"])))
    if "fuzzy_matching" in value:
        import capo_cloudsearch.types.suggester_fuzzy_matching

        capo_cloudsearch.types.suggester_fuzzy_matching.serialize_query(
            value["fuzzy_matching"], pairs, f"{key_prefix}FuzzyMatching"
        )
    if "sort_expression" in value:
        pairs.append((f"{key_prefix}SortExpression", str(value["sort_expression"])))


def deserialize_query(el: Element) -> DocumentSuggesterOptions:
    out: DocumentSuggesterOptions = {}  # type: ignore[typeddict-item]
    child_source_field = el.find("SourceField")
    if child_source_field is not None:
        out["source_field"] = str(child_source_field.text or "")
    else:
        out["source_field"] = ""
    child_fuzzy_matching = el.find("FuzzyMatching")
    if child_fuzzy_matching is not None:
        import capo_cloudsearch.types.suggester_fuzzy_matching

        out["fuzzy_matching"] = (
            capo_cloudsearch.types.suggester_fuzzy_matching.deserialize_query(
                child_fuzzy_matching
            )
        )
    child_sort_expression = el.find("SortExpression")
    if child_sort_expression is not None:
        out["sort_expression"] = str(child_sort_expression.text or "")
    return out
