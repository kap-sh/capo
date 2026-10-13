"""Generated from Smithy shape ``com.amazonaws.eventbridge#ListTargetsByRuleResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.next_token
    import capo_eventbridge.types.target_list


class ListTargetsByRuleResponse(TypedDict, closed=True):
    targets: NotRequired["capo_eventbridge.types.target_list.TargetList"]
    """<p>The targets assigned to the rule.</p>"""
    next_token: NotRequired["capo_eventbridge.types.next_token.NextToken"]
    """<p>A token indicating there are more results available. If there are no more results, no token is included in the response.</p> <p>The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.</p> <p> Using an expired pagination token results in an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTargetsByRuleResponse) -> dict:
    out: dict = {}
    if "targets" in value:
        import capo_eventbridge.types.target_list

        out["Targets"] = capo_eventbridge.types.target_list.serialize_aws_json_1_1(
            value["targets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTargetsByRuleResponse:
    out: ListTargetsByRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("Targets") is not None:
        import capo_eventbridge.types.target_list

        out["targets"] = capo_eventbridge.types.target_list.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListTargetsByRuleResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "targets" in value:
        import capo_eventbridge.types.target_list

        out["targets"] = capo_eventbridge.types.target_list.redact_sensitive(
            value["targets"]
        )
    return out
