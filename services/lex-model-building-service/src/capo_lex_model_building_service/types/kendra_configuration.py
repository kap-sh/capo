"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#KendraConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.kendra_index_arn
    import capo_lex_model_building_service.types.query_filter_string
    import capo_lex_model_building_service.types.role_arn


class KendraConfiguration(TypedDict, closed=True):
    kendra_index: (
        "capo_lex_model_building_service.types.kendra_index_arn.KendraIndexArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the AMAZON.KendraSearchIntent intent to search. The index must be in the same account and Region as the Amazon Lex bot. If the Amazon Kendra index does not exist, you get an exception when you call the <code>PutIntent</code> operation.</p>"""
    query_filter_string: NotRequired[
        "capo_lex_model_building_service.types.query_filter_string.QueryFilterString"
    ]
    """<p>A query filter that Amazon Lex sends to Amazon Kendra to filter the response from the query. The filter is in the format defined by Amazon Kendra. For more information, see <a href="http://docs.aws.amazon.com/kendra/latest/dg/filtering.html">Filtering queries</a>.</p> <p>You can override this filter string with a new filter string at runtime.</p>"""
    role: "capo_lex_model_building_service.types.role_arn.roleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permission to search the Amazon Kendra index. The role must be in the same account and Region as the Amazon Lex bot. If the role does not exist, you get an exception when you call the <code>PutIntent</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KendraConfiguration) -> dict:
    out: dict = {}
    out["kendraIndex"] = value["kendra_index"]
    if "query_filter_string" in value:
        out["queryFilterString"] = value["query_filter_string"]
    out["role"] = value["role"]
    return out


def deserialize_json(data: dict) -> KendraConfiguration:
    out: KendraConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kendraIndex") is not None:
        out["kendra_index"] = data["kendraIndex"]
    else:
        raise DeserializationError("KendraConfiguration.kendra_index required")
    if data.get("queryFilterString") is not None:
        out["query_filter_string"] = data["queryFilterString"]
    if data.get("role") is not None:
        out["role"] = data["role"]
    else:
        raise DeserializationError("KendraConfiguration.role required")
    return out
