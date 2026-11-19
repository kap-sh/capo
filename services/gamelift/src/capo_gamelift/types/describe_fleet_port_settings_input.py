"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetPortSettingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.location_string_model


class DescribeFleetPortSettingsInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to retrieve port settings for. You can use either the fleet ID or ARN value.</p>"""
    location: NotRequired[
        "capo_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>A remote location to check for status of port setting updates. Use the Amazon Web Services Region code format, such as <code>us-west-2</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetPortSettingsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetPortSettingsInput:
    out: DescribeFleetPortSettingsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFleetPortSettingsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "location" in value:
        out["Location"] = value["location"]
    return out


def deserialize_cbor(data: dict) -> DescribeFleetPortSettingsInput:
    out: DescribeFleetPortSettingsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    return out
