"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_arn
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.domain_status


class CreateDomainResponse(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    domain_arn: "capo_connectcases.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) for the Cases domain.</p>"""
    domain_status: "capo_connectcases.types.domain_status.DomainStatus"
    """<p>The status of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainResponse) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["domainArn"] = value["domain_arn"]
    out["domainStatus"] = value["domain_status"]
    return out


def deserialize_json(data: dict) -> CreateDomainResponse:
    out: CreateDomainResponse = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    else:
        out["domain_arn"] = ""
    if data.get("domainStatus") is not None:
        out["domain_status"] = data["domainStatus"]
    else:
        out["domain_status"] = ""
    return out
