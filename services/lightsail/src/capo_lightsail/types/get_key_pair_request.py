"""Generated from Smithy shape ``com.amazonaws.lightsail#GetKeyPairRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class GetKeyPairRequest(TypedDict, closed=True):
    key_pair_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the key pair for which you are requesting information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyPairRequest) -> dict:
    out: dict = {}
    out["keyPairName"] = value["key_pair_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyPairRequest:
    out: GetKeyPairRequest = {}  # type: ignore[typeddict-item]
    if data.get("keyPairName") is not None:
        out["key_pair_name"] = data["keyPairName"]
    else:
        out["key_pair_name"] = ""
    return out
