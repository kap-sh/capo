"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#KendraConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boolean
    import capo_lex_models_v2.types.kendra_index_arn
    import capo_lex_models_v2.types.query_filter_string


class KendraConfiguration(TypedDict, closed=True):
    kendra_index: "capo_lex_models_v2.types.kendra_index_arn.KendraIndexArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the <code>AMAZON.KendraSearchIntent</code> intent to search. The index must be in the same account and Region as the Amazon Lex bot.</p>"""
    query_filter_string_enabled: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Determines whether the <code>AMAZON.KendraSearchIntent</code> intent uses a custom query string to query the Amazon Kendra index.</p>"""
    query_filter_string: NotRequired[
        "capo_lex_models_v2.types.query_filter_string.QueryFilterString"
    ]
    """<p>A query filter that Amazon Lex sends to Amazon Kendra to filter the response from a query. The filter is in the format defined by Amazon Kendra. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/filtering.html">Filtering queries</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KendraConfiguration) -> dict:
    out: dict = {}
    out["kendraIndex"] = value["kendra_index"]
    out["queryFilterStringEnabled"] = value.get("query_filter_string_enabled", False)
    if "query_filter_string" in value:
        out["queryFilterString"] = value["query_filter_string"]
    return out


def deserialize_json(data: dict) -> KendraConfiguration:
    out: KendraConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kendraIndex") is not None:
        out["kendra_index"] = data["kendraIndex"]
    else:
        raise DeserializationError("KendraConfiguration.kendra_index required")
    if data.get("queryFilterStringEnabled") is not None:
        out["query_filter_string_enabled"] = data["queryFilterStringEnabled"]
    else:
        out["query_filter_string_enabled"] = False
    if data.get("queryFilterString") is not None:
        out["query_filter_string"] = data["queryFilterString"]
    return out
