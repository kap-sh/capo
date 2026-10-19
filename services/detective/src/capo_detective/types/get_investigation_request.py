"""Generated from Smithy shape ``com.amazonaws.detective#GetInvestigationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.graph_arn
    import capo_detective.types.investigation_id


class GetInvestigationRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The Amazon Resource Name (ARN) of the behavior graph.</p>"""
    investigation_id: "capo_detective.types.investigation_id.InvestigationId"
    """<p>The investigation ID of the investigation report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvestigationRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    out["InvestigationId"] = value["investigation_id"]
    return out


def deserialize_json(data: dict) -> GetInvestigationRequest:
    out: GetInvestigationRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    if data.get("InvestigationId") is not None:
        out["investigation_id"] = data["InvestigationId"]
    else:
        out["investigation_id"] = ""
    return out
