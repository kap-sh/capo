"""Generated from Smithy shape ``com.amazonaws.ivs#DeleteStreamKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.stream_key_arn


class DeleteStreamKeyRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.stream_key_arn.StreamKeyArn"
    """<p>ARN of the stream key to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStreamKeyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteStreamKeyRequest:
    out: DeleteStreamKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
