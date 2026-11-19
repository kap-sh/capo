"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateLocationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.location_model


class CreateLocationOutput(TypedDict, closed=True):
    location: NotRequired["capo_gamelift.types.location_model.LocationModel"]
    """<p>The details of the custom location you created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationOutput) -> dict:
    out: dict = {}
    if "location" in value:
        import capo_gamelift.types.location_model

        out["Location"] = capo_gamelift.types.location_model.serialize_aws_json_1_1(
            value["location"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationOutput:
    out: CreateLocationOutput = {}  # type: ignore[typeddict-item]
    if data.get("Location") is not None:
        import capo_gamelift.types.location_model

        out["location"] = capo_gamelift.types.location_model.deserialize_aws_json_1_1(
            data["Location"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateLocationOutput) -> dict:
    out: dict = {}
    if "location" in value:
        import capo_gamelift.types.location_model

        out["Location"] = capo_gamelift.types.location_model.serialize_cbor(
            value["location"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateLocationOutput:
    out: CreateLocationOutput = {}  # type: ignore[typeddict-item]
    if data.get("Location") is not None:
        import capo_gamelift.types.location_model

        out["location"] = capo_gamelift.types.location_model.deserialize_cbor(
            data["Location"]
        )
    return out
