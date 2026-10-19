"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetDecoderManifestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.resource_name


class GetDecoderManifestRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the decoder manifest to retrieve information about. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDecoderManifestRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDecoderManifestRequest:
    out: GetDecoderManifestRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
