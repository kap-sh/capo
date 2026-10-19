"""Generated from Smithy shape ``com.amazonaws.voiceid#DeleteFraudsterRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.fraudster_id


class DeleteFraudsterRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the fraudster.</p>"""
    fraudster_id: "capo_voice_id.types.fraudster_id.FraudsterId"
    """<p>The identifier of the fraudster you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFraudsterRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["FraudsterId"] = value["fraudster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFraudsterRequest:
    out: DeleteFraudsterRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        out["domain_id"] = ""
    if data.get("FraudsterId") is not None:
        out["fraudster_id"] = data["FraudsterId"]
    else:
        out["fraudster_id"] = ""
    return out


def redact_sensitive(value: DeleteFraudsterRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fraudster_id" in value:
        out["fraudster_id"] = "*** Sensitive Data Redacted ***"
    return out
