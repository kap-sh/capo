"""Generated from Smithy shape ``com.amazonaws.omics#SseConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.encryption_type


class SseConfig(TypedDict, closed=True):
    type: "capo_omics.types.encryption_type.EncryptionType"
    """<p>The encryption type.</p>"""
    key_arn: NotRequired["str"]
    """<p>An encryption key ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SseConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "key_arn" in value:
        out["keyArn"] = value["key_arn"]
    return out


def deserialize_json(data: dict) -> SseConfig:
    out: SseConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("keyArn") is not None:
        out["key_arn"] = data["keyArn"]
    return out
