"""Generated from Smithy shape ``com.amazonaws.voiceid#AuthenticationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.score


class AuthenticationConfiguration(TypedDict, closed=True):
    acceptance_threshold: "capo_voice_id.types.score.Score"
    """<p>The minimum threshold needed to successfully authenticate a speaker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AuthenticationConfiguration) -> dict:
    out: dict = {}
    out["AcceptanceThreshold"] = value["acceptance_threshold"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AuthenticationConfiguration:
    out: AuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AcceptanceThreshold") is not None:
        out["acceptance_threshold"] = data["AcceptanceThreshold"]
    else:
        out["acceptance_threshold"] = 0
    return out
