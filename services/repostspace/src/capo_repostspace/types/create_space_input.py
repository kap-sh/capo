"""Generated from Smithy shape ``com.amazonaws.repostspace#CreateSpaceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.arn
    import capo_repostspace.types.kms_key
    import capo_repostspace.types.space_description
    import capo_repostspace.types.space_name
    import capo_repostspace.types.space_subdomain
    import capo_repostspace.types.supported_email_domains_parameters
    import capo_repostspace.types.tags
    import capo_repostspace.types.tier_level


class CreateSpaceInput(TypedDict, closed=True):
    name: "capo_repostspace.types.space_name.SpaceName"
    """<p>The name for the private re:Post. This must be unique in your account.</p>"""
    subdomain: "capo_repostspace.types.space_subdomain.SpaceSubdomain"
    """<p>The subdomain that you use to access your AWS re:Post Private private re:Post. All custom subdomains must be approved by AWS before use. In addition to your custom subdomain, all private re:Posts are issued an AWS generated subdomain for immediate use.</p>"""
    tier: "capo_repostspace.types.tier_level.TierLevel"
    """<p>The pricing tier for the private re:Post.</p>"""
    description: NotRequired[
        "capo_repostspace.types.space_description.SpaceDescription"
    ]
    """<p>A description for the private re:Post. This is used only to help you identify this private re:Post.</p>"""
    user_kms_key: NotRequired["capo_repostspace.types.kms_key.KMSKey"]
    """<p>The AWS KMS key ARN that’s used for the AWS KMS encryption. If you don't provide a key, your data is encrypted by default with a key that AWS owns and manages for you.</p>"""
    tags: NotRequired["capo_repostspace.types.tags.Tags"]
    """<p>The list of tags associated with the private re:Post.</p>"""
    role_arn: NotRequired["capo_repostspace.types.arn.Arn"]
    """<p>The IAM role that grants permissions to the private re:Post to convert unanswered questions into AWS support tickets.</p>"""
    supported_email_domains: NotRequired[
        "capo_repostspace.types.supported_email_domains_parameters.SupportedEmailDomainsParameters"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSpaceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["subdomain"] = value["subdomain"]
    import capo_repostspace.types.tier_level

    out["tier"] = capo_repostspace.types.tier_level.serialize_json(value["tier"])
    if "description" in value:
        out["description"] = value["description"]
    if "user_kms_key" in value:
        out["userKMSKey"] = value["user_kms_key"]
    if "tags" in value:
        import capo_repostspace.types.tags

        out["tags"] = capo_repostspace.types.tags.serialize_json(value["tags"])
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "supported_email_domains" in value:
        import capo_repostspace.types.supported_email_domains_parameters

        out["supportedEmailDomains"] = (
            capo_repostspace.types.supported_email_domains_parameters.serialize_json(
                value["supported_email_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSpaceInput:
    out: CreateSpaceInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("subdomain") is not None:
        out["subdomain"] = data["subdomain"]
    else:
        out["subdomain"] = ""
    if data.get("tier") is not None:
        import capo_repostspace.types.tier_level

        out["tier"] = capo_repostspace.types.tier_level.deserialize_json(data["tier"])
    else:
        import typing

        out["tier"] = typing.cast("capo_repostspace.types.tier_level.TierLevel", "")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("userKMSKey") is not None:
        out["user_kms_key"] = data["userKMSKey"]
    if data.get("tags") is not None:
        import capo_repostspace.types.tags

        out["tags"] = capo_repostspace.types.tags.deserialize_json(data["tags"])
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("supportedEmailDomains") is not None:
        import capo_repostspace.types.supported_email_domains_parameters

        out["supported_email_domains"] = (
            capo_repostspace.types.supported_email_domains_parameters.deserialize_json(
                data["supportedEmailDomains"]
            )
        )
    return out


def redact_sensitive(value: CreateSpaceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    if "supported_email_domains" in value:
        import capo_repostspace.types.supported_email_domains_parameters

        out["supported_email_domains"] = (
            capo_repostspace.types.supported_email_domains_parameters.redact_sensitive(
                value["supported_email_domains"]
            )
        )
    return out
