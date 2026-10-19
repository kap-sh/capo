"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.domain_name


class DeleteDomainRequest(TypedDict, closed=True):
    domain_name: "capo_lightsail.types.domain_name.DomainName"
    """<p>The specific domain name to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDomainRequest) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDomainRequest:
    out: DeleteDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    return out
