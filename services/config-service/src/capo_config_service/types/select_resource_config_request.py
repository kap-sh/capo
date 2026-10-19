"""Generated from Smithy shape ``com.amazonaws.configservice#SelectResourceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.expression
    import capo_config_service.types.limit
    import capo_config_service.types.next_token


class SelectResourceConfigRequest(TypedDict, closed=True):
    expression: "capo_config_service.types.expression.Expression"
    """<p>The SQL query <code>SELECT</code> command.</p>"""
    limit: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of query results returned on each page. </p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectResourceConfigRequest) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SelectResourceConfigRequest:
    out: SelectResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        out["expression"] = ""
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
