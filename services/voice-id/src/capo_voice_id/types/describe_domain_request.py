"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id


class DescribeDomainRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that you are describing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDomainRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeDomainRequest:
    out: DescribeDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        out["domain_id"] = ""
    return out
