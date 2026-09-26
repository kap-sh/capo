"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ListRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.rule_summary_list


class ListRulesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_network_security_manager.types.next_token.NextToken"]
    """<p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>"""
    rules: "capo_network_security_manager.types.rule_summary_list.RuleSummaryList"
    """<p>The list of rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_network_security_manager.types.rule_summary_list

    out["rules"] = capo_network_security_manager.types.rule_summary_list.serialize_json(
        value["rules"]
    )
    return out


def deserialize_json(data: dict) -> ListRulesOutput:
    out: ListRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("rules") is not None:
        import capo_network_security_manager.types.rule_summary_list

        out["rules"] = (
            capo_network_security_manager.types.rule_summary_list.deserialize_json(
                data["rules"]
            )
        )
    else:
        raise DeserializationError("ListRulesOutput.rules required")
    return out
