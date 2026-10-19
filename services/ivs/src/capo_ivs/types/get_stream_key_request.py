"""Generated from Smithy shape ``com.amazonaws.ivs#GetStreamKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.stream_key_arn


class GetStreamKeyRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.stream_key_arn.StreamKeyArn"
    """<p>ARN for the stream key to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamKeyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetStreamKeyRequest:
    out: GetStreamKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
