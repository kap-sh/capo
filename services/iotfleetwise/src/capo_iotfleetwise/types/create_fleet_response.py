"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateFleetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.fleet_id


class CreateFleetResponse(TypedDict, closed=True):
    id: "capo_iotfleetwise.types.fleet_id.fleetId"
    """<p> The ID of the created fleet. </p>"""
    arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The ARN of the created fleet. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateFleetResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateFleetResponse:
    out: CreateFleetResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
