"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationFsxLustreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.location_arn


class CreateLocationFsxLustreResponse(TypedDict, closed=True):
    location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The Amazon Resource Name (ARN) of the FSx for Lustre file system location that you created. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationFsxLustreResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationFsxLustreResponse:
    out: CreateLocationFsxLustreResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateLocationFsxLustreResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    return out


def deserialize_cbor(data: dict) -> CreateLocationFsxLustreResponse:
    out: CreateLocationFsxLustreResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    return out
