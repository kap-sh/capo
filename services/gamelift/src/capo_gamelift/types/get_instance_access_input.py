"""Generated from Smithy shape ``com.amazonaws.gamelift#GetInstanceAccessInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.instance_id


class GetInstanceAccessInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet that contains the instance you want to access. You can request access to instances in EC2 fleets with the following statuses: <code>ACTIVATING</code>, <code>ACTIVE</code>, or <code>ERROR</code>. Use either a fleet ID or an ARN value. </p> <note> <p>You can access fleets in <code>ERROR</code> status for a short period of time before Amazon GameLift Servers deletes them.</p> </note>"""
    instance_id: NotRequired["capo_gamelift.types.instance_id.InstanceId"]
    """<p>A unique identifier for the instance you want to access. You can access an instance in any status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceAccessInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceAccessInput:
    out: GetInstanceAccessInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetInstanceAccessInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    return out


def deserialize_cbor(data: dict) -> GetInstanceAccessInput:
    out: GetInstanceAccessInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    return out
