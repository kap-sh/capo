"""Generated from Smithy shape ``com.amazonaws.detective#UpdateInvestigationStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.graph_arn
    import capo_detective.types.investigation_id
    import capo_detective.types.state


class UpdateInvestigationStateRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The Amazon Resource Name (ARN) of the behavior graph.</p>"""
    investigation_id: "capo_detective.types.investigation_id.InvestigationId"
    """<p>The investigation ID of the investigation report.</p>"""
    state: "capo_detective.types.state.State"
    """<p>The current state of the investigation. An archived investigation indicates you have completed reviewing the investigation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInvestigationStateRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    out["InvestigationId"] = value["investigation_id"]
    import capo_detective.types.state

    out["State"] = capo_detective.types.state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> UpdateInvestigationStateRequest:
    out: UpdateInvestigationStateRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    if data.get("InvestigationId") is not None:
        out["investigation_id"] = data["InvestigationId"]
    else:
        out["investigation_id"] = ""
    if data.get("State") is not None:
        import capo_detective.types.state

        out["state"] = capo_detective.types.state.deserialize_json(data["State"])
    else:
        import typing

        out["state"] = typing.cast("capo_detective.types.state.State", "")
    return out
