"""Generated from Smithy shape ``com.amazonaws.appstream#DisassociateApplicationFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.name


class DisassociateApplicationFleetRequest(TypedDict, closed=True):
    fleet_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the fleet.</p>"""
    application_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateApplicationFleetRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateApplicationFleetRequest:
    out: DisassociateApplicationFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateApplicationFleetRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_cbor(data: dict) -> DisassociateApplicationFleetRequest:
    out: DisassociateApplicationFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    return out
