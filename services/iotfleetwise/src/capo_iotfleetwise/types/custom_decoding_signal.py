"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CustomDecodingSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.custom_decoding_id


class CustomDecodingSignal(TypedDict, closed=True):
    id: "capo_iotfleetwise.types.custom_decoding_id.CustomDecodingId"
    """<p>The ID of the signal.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomDecodingSignal) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomDecodingSignal:
    out: CustomDecodingSignal = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
