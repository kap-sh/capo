"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationEcsCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class InvestigationEcsCluster(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the cluster.</p>"""
    arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    status: NotRequired["capo_guardduty.types.string.String"]
    """<p>The status of the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationEcsCluster) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> InvestigationEcsCluster:
    out: InvestigationEcsCluster = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
