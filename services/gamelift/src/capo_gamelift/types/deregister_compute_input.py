"""Generated from Smithy shape ``com.amazonaws.gamelift#DeregisterComputeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_name_or_arn
    import capo_gamelift.types.fleet_id_or_arn


class DeregisterComputeInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet the compute resource is currently registered to.</p>"""
    compute_name: NotRequired[
        "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
    ]
    """<p>The unique identifier of the compute resource to deregister. For an Anywhere fleet compute, use the registered compute name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterComputeInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterComputeInput:
    out: DeregisterComputeInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeregisterComputeInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    return out


def deserialize_cbor(data: dict) -> DeregisterComputeInput:
    out: DeregisterComputeInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    return out
