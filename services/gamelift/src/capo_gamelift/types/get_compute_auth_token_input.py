"""Generated from Smithy shape ``com.amazonaws.gamelift#GetComputeAuthTokenInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.compute_name_or_arn
    import capo_gamelift.types.fleet_id_or_arn


class GetComputeAuthTokenInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet that the compute is registered to.</p>"""
    compute_name: NotRequired[
        "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
    ]
    """<p>The name of the compute resource you are requesting the authentication token for. For an Anywhere fleet compute, use the registered compute name. For an EC2 fleet instance, use the instance ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComputeAuthTokenInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComputeAuthTokenInput:
    out: GetComputeAuthTokenInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetComputeAuthTokenInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    return out


def deserialize_cbor(data: dict) -> GetComputeAuthTokenInput:
    out: GetComputeAuthTokenInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("ComputeName") is not None:
        out["compute_name"] = data["ComputeName"]
    return out
