"""Generated from Smithy shape ``com.amazonaws.connectcases#DomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_arn
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.domain_name


class DomainSummary(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the domain.</p>"""
    domain_arn: "capo_connectcases.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) of the domain.</p>"""
    name: "capo_connectcases.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummary) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["domainArn"] = value["domain_arn"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DomainSummary:
    out: DomainSummary = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    else:
        out["domain_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
