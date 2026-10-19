"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobS3OutputConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.key_prefix


class ProtectedJobS3OutputConfigurationInput(TypedDict, closed=True):
    bucket: "str"
    """<p> The S3 bucket for job output.</p>"""
    key_prefix: NotRequired["capo_cleanrooms.types.key_prefix.KeyPrefix"]
    """<p>The S3 prefix to unload the protected job results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobS3OutputConfigurationInput) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    return out


def deserialize_json(data: dict) -> ProtectedJobS3OutputConfigurationInput:
    out: ProtectedJobS3OutputConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("keyPrefix") is not None:
        out["key_prefix"] = data["keyPrefix"]
    return out
