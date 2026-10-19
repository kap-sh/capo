"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CustomDecodingInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.custom_decoding_signal_interface_name


class CustomDecodingInterface(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.custom_decoding_signal_interface_name.CustomDecodingSignalInterfaceName"
    """<p>The name of the interface.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomDecodingInterface) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomDecodingInterface:
    out: CustomDecodingInterface = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
