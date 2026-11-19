"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteLocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.custom_location_name_or_arn_model


class DeleteLocationInput(TypedDict, closed=True):
    location_name: NotRequired[
        "capo_gamelift.types.custom_location_name_or_arn_model.CustomLocationNameOrArnModel"
    ]
    """<p>The location name of the custom location to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLocationInput) -> dict:
    out: dict = {}
    if "location_name" in value:
        out["LocationName"] = value["location_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLocationInput:
    out: DeleteLocationInput = {}  # type: ignore[typeddict-item]
    if data.get("LocationName") is not None:
        out["location_name"] = data["LocationName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteLocationInput) -> dict:
    out: dict = {}
    if "location_name" in value:
        out["LocationName"] = value["location_name"]
    return out


def deserialize_cbor(data: dict) -> DeleteLocationInput:
    out: DeleteLocationInput = {}  # type: ignore[typeddict-item]
    if data.get("LocationName") is not None:
        out["location_name"] = data["LocationName"]
    return out
