"""Generated from Smithy shape ``com.amazonaws.voiceid#EvaluateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.session_name_or_id


class EvaluateSessionRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain where the session started.</p>"""
    session_name_or_id: "capo_voice_id.types.session_name_or_id.SessionNameOrId"
    """<p>The session identifier, or name of the session, that you want to evaluate. In Voice ID integration, this is the Contact-Id.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluateSessionRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["SessionNameOrId"] = value["session_name_or_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EvaluateSessionRequest:
    out: EvaluateSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        out["domain_id"] = ""
    if data.get("SessionNameOrId") is not None:
        out["session_name_or_id"] = data["SessionNameOrId"]
    else:
        out["session_name_or_id"] = ""
    return out
