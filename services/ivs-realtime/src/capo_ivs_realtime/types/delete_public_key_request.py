"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DeletePublicKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.public_key_arn


class DeletePublicKeyRequest(TypedDict, closed=True):
    arn: "capo_ivs_realtime.types.public_key_arn.PublicKeyArn"
    """<p>ARN of the public key to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePublicKeyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeletePublicKeyRequest:
    out: DeletePublicKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
