"""Generated from Smithy shape ``com.amazonaws.securityagent#TargetDomain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.target_domain_id
    import capo_securityagent.types.target_domain_status
    import capo_securityagent.types.verification_details


class TargetDomain(TypedDict, closed=True):
    target_domain_id: "capo_securityagent.types.target_domain_id.TargetDomainId"
    """<p>The unique identifier of the target domain.</p>"""
    domain_name: "str"
    """<p>The domain name of the target domain.</p>"""
    verification_status: NotRequired[
        "capo_securityagent.types.target_domain_status.TargetDomainStatus"
    ]
    """<p>The current verification status of the target domain.</p>"""
    verification_status_reason: NotRequired["str"]
    """<p>The reason for the current target domain verification status.</p>"""
    verification_details: NotRequired[
        "capo_securityagent.types.verification_details.VerificationDetails"
    ]
    """<p>The verification details for the target domain.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the target domain was created, in UTC format.</p>"""
    verified_at: NotRequired["datetime.datetime"]
    """<p>The date and time the target domain was verified, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetDomain) -> dict:
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
    if "verification_status_reason" in value:
        out["verificationStatusReason"] = value["verification_status_reason"]
    if "verification_details" in value:
        import capo_securityagent.types.verification_details

        out["verificationDetails"] = (
            capo_securityagent.types.verification_details.serialize_json(
                value["verification_details"]
            )
        )
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "verified_at" in value:
        import capo_securityagent._protocol.serialize

        out["verifiedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["verified_at"]
        )
    return out


def deserialize_json(data: dict) -> TargetDomain:
    out: TargetDomain = {}  # type: ignore[typeddict-item]
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
    if data.get("verificationStatusReason") is not None:
        out["verification_status_reason"] = data["verificationStatusReason"]
    if data.get("verificationDetails") is not None:
        import capo_securityagent.types.verification_details

        out["verification_details"] = (
            capo_securityagent.types.verification_details.deserialize_json(
                data["verificationDetails"]
            )
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("verifiedAt") is not None:
        import datetime

        out["verified_at"] = datetime.datetime.fromisoformat(
            data["verifiedAt"].replace("Z", "+00:00")
        )
    return out
