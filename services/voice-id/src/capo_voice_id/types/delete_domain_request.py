"""Generated from Smithy shape ``com.amazonaws.voiceid#DeleteDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id


class DeleteDomainRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDomainRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDomainRequest:
    out: DeleteDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        out["domain_id"] = ""
    return out
