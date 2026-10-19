"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateDecoderManifestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.resource_name


class CreateDecoderManifestResponse(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the created decoder manifest. </p>"""
    arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The ARN of the created decoder manifest. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDecoderManifestResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDecoderManifestResponse:
    out: CreateDecoderManifestResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
