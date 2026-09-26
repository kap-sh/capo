"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ListPoliciesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.policy_summary_list


class ListPoliciesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_network_security_manager.types.next_token.NextToken"]
    """<p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>"""
    policies: (
        "capo_network_security_manager.types.policy_summary_list.PolicySummaryList"
    )
    """<p>The list of policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPoliciesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_network_security_manager.types.policy_summary_list

    out["policies"] = (
        capo_network_security_manager.types.policy_summary_list.serialize_json(
            value["policies"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListPoliciesOutput:
    out: ListPoliciesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("policies") is not None:
        import capo_network_security_manager.types.policy_summary_list

        out["policies"] = (
            capo_network_security_manager.types.policy_summary_list.deserialize_json(
                data["policies"]
            )
        )
    else:
        raise DeserializationError("ListPoliciesOutput.policies required")
    return out
