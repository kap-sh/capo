"""Generated from Smithy shape ``com.amazonaws.ivs#GetPlaybackKeyPairRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.playback_key_pair_arn


class GetPlaybackKeyPairRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.playback_key_pair_arn.PlaybackKeyPairArn"
    """<p>ARN of the key pair to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaybackKeyPairRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetPlaybackKeyPairRequest:
    out: GetPlaybackKeyPairRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
