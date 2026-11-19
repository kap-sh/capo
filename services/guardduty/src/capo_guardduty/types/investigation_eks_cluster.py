"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationEksCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class InvestigationEksCluster(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the cluster.</p>"""
    arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    status: NotRequired["capo_guardduty.types.string.String"]
    """<p>The status of the cluster.</p>"""
    vpc_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the VPC that is associated with the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationEksCluster) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> InvestigationEksCluster:
    out: InvestigationEksCluster = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    return out
