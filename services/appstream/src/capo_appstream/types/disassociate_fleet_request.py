"""Generated from Smithy shape ``com.amazonaws.appstream#DisassociateFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string


class DisassociateFleetRequest(TypedDict, closed=True):
    fleet_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the fleet.</p>"""
    stack_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the stack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFleetRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFleetRequest:
    out: DisassociateFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateFleetRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    return out


def deserialize_cbor(data: dict) -> DisassociateFleetRequest:
    out: DisassociateFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("StackName") is not None:
        out["stack_name"] = data["StackName"]
    return out
