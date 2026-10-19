"""Generated from Smithy shape ``com.amazonaws.glue#FilterStringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.bool


class FilterStringConfiguration(TypedDict, closed=True):
    query_parameter_name: "str"
    """<p>The query parameter name used to send the constructed filter expression string in API requests.</p>"""
    quote_string_values: NotRequired["capo_glue.types.bool.Bool"]
    """<p>Indicates whether string and date values should be wrapped with a quote character in the filter expression.</p>"""
    quote_character: NotRequired["str"]
    """<p>The character used to quote values when <code>QuoteStringValues</code> is true. Defaults to double quotes if not specified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterStringConfiguration) -> dict:
    out: dict = {}
    out["QueryParameterName"] = value["query_parameter_name"]
    if "quote_string_values" in value:
        out["QuoteStringValues"] = value["quote_string_values"]
    if "quote_character" in value:
        out["QuoteCharacter"] = value["quote_character"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterStringConfiguration:
    out: FilterStringConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("QueryParameterName") is not None:
        out["query_parameter_name"] = data["QueryParameterName"]
    else:
        out["query_parameter_name"] = ""
    if data.get("QuoteStringValues") is not None:
        out["quote_string_values"] = data["QuoteStringValues"]
    if data.get("QuoteCharacter") is not None:
        out["quote_character"] = data["QuoteCharacter"]
    return out
