"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#QnAKendraConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boolean
    import capo_lex_models_v2.types.kendra_index_arn
    import capo_lex_models_v2.types.query_filter_string


class QnAKendraConfiguration(TypedDict, closed=True):
    kendra_index: "capo_lex_models_v2.types.kendra_index_arn.KendraIndexArn"
    """<p>The ARN of the Amazon Kendra index to use.</p>"""
    query_filter_string_enabled: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Specifies whether to enable an Amazon Kendra filter string or not.</p>"""
    query_filter_string: NotRequired[
        "capo_lex_models_v2.types.query_filter_string.QueryFilterString"
    ]
    """<p>Contains the Amazon Kendra filter string to use if enabled. For more information on the Amazon Kendra search filter JSON format, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/filtering.html#search-filtering">Using document attributes to filter search results</a>.</p>"""
    exact_response: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Specifies whether to return an exact response from the Amazon Kendra index or to let the Amazon Bedrock model you select generate a response based on the results. To use this feature, you must first add FAQ questions to your index by following the steps at <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html">Adding frequently asked questions (FAQs) to an index</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QnAKendraConfiguration) -> dict:
    out: dict = {}
    out["kendraIndex"] = value["kendra_index"]
    out["queryFilterStringEnabled"] = value.get("query_filter_string_enabled", False)
    if "query_filter_string" in value:
        out["queryFilterString"] = value["query_filter_string"]
    out["exactResponse"] = value.get("exact_response", False)
    return out


def deserialize_json(data: dict) -> QnAKendraConfiguration:
    out: QnAKendraConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kendraIndex") is not None:
        out["kendra_index"] = data["kendraIndex"]
    else:
        raise DeserializationError("QnAKendraConfiguration.kendra_index required")
    if data.get("queryFilterStringEnabled") is not None:
        out["query_filter_string_enabled"] = data["queryFilterStringEnabled"]
    else:
        out["query_filter_string_enabled"] = False
    if data.get("queryFilterString") is not None:
        out["query_filter_string"] = data["queryFilterString"]
    if data.get("exactResponse") is not None:
        out["exact_response"] = data["exactResponse"]
    else:
        out["exact_response"] = False
    return out
