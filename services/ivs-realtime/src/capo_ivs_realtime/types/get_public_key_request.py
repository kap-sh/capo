"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetPublicKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.public_key_arn


class GetPublicKeyRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.public_key_arn.PublicKeyArn"
    """<p>ARN of the public key for which the information is to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPublicKeyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetPublicKeyRequest:
    out: GetPublicKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
