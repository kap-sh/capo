"""Generated from Smithy shape ``com.amazonaws.securityagent#TargetDomainSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.target_domain_id
    import capo_securityagent.types.target_domain_status


class TargetDomainSummary(TypedDict, closed=True):
    target_domain_id: "capo_securityagent.types.target_domain_id.TargetDomainId"
    """<p>The unique identifier of the target domain.</p>"""
    domain_name: "str"
    """<p>The domain name of the target domain.</p>"""
    verification_status: NotRequired[
        "capo_securityagent.types.target_domain_status.TargetDomainStatus"
    ]
    """<p>The current verification status of the target domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetDomainSummary) -> dict:
    out: dict = {}
    out["targetDomainId"] = value["target_domain_id"]
    out["domainName"] = value["domain_name"]
    if "verification_status" in value:
        import capo_securityagent.types.target_domain_status

        out["verificationStatus"] = (
            capo_securityagent.types.target_domain_status.serialize_json(
                value["verification_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> TargetDomainSummary:
    out: TargetDomainSummary = {}  # type: ignore[typeddict-item]
    if data.get("targetDomainId") is not None:
        out["target_domain_id"] = data["targetDomainId"]
    else:
        out["target_domain_id"] = ""
    if data.get("domainName") is not None:
        out["domain_name"] = data["domainName"]
    else:
        out["domain_name"] = ""
    if data.get("verificationStatus") is not None:
        import capo_securityagent.types.target_domain_status

        out["verification_status"] = (
            capo_securityagent.types.target_domain_status.deserialize_json(
                data["verificationStatus"]
            )
        )
    return out
