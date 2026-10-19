"""Generated from Smithy shape ``com.amazonaws.securityir#ListInvestigationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.investigation_action_list


class ListInvestigationsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>Investigation performed by an agent for a security incident for next Token</p>"""
    investigation_actions: (
        "capo_security_ir.types.investigation_action_list.InvestigationActionList"
    )
    """<p>Investigation performed by an agent for a security incid…Unique identifier for the specific investigation&gt;</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_security_ir.types.investigation_action_list

    out["investigationActions"] = (
        capo_security_ir.types.investigation_action_list.serialize_json(
            value["investigation_actions"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListInvestigationsResponse:
    out: ListInvestigationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("investigationActions") is not None:
        import capo_security_ir.types.investigation_action_list

        out["investigation_actions"] = (
            capo_security_ir.types.investigation_action_list.deserialize_json(
                data["investigationActions"]
            )
        )
    else:
        out["investigation_actions"] = []
    return out
