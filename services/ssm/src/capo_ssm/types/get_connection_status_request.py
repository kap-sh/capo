"""Generated from Smithy shape ``com.amazonaws.ssm#GetConnectionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.session_target


class GetConnectionStatusRequest(TypedDict, closed=True):
    target: "capo_ssm.types.session_target.SessionTarget"
    """<p>The managed node ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionStatusRequest) -> dict:
    out: dict = {}
    out["Target"] = value["target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionStatusRequest:
    out: GetConnectionStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    else:
        out["target"] = ""
    return out
