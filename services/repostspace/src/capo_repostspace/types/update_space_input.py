"""Generated from Smithy shape ``com.amazonaws.repostspace#UpdateSpaceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.arn
    import capo_repostspace.types.space_description
    import capo_repostspace.types.space_id
    import capo_repostspace.types.supported_email_domains_parameters
    import capo_repostspace.types.tier_level


class UpdateSpaceInput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of this private re:Post.</p>"""
    description: NotRequired[
        "capo_repostspace.types.space_description.SpaceDescription"
    ]
    """<p>A description for the private re:Post. This is used only to help you identify this private re:Post.</p>"""
    tier: NotRequired["capo_repostspace.types.tier_level.TierLevel"]
    """<p>The pricing tier of this private re:Post.</p>"""
    role_arn: NotRequired["capo_repostspace.types.arn.Arn"]
    """<p>The IAM role that grants permissions to the private re:Post to convert unanswered questions into AWS support tickets.</p>"""
    supported_email_domains: NotRequired[
        "capo_repostspace.types.supported_email_domains_parameters.SupportedEmailDomainsParameters"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpaceInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "tier" in value:
        import capo_repostspace.types.tier_level

        out["tier"] = capo_repostspace.types.tier_level.serialize_json(value["tier"])
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


def deserialize_json(data: dict) -> UpdateSpaceInput:
    out: UpdateSpaceInput = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tier") is not None:
        import capo_repostspace.types.tier_level

        out["tier"] = capo_repostspace.types.tier_level.deserialize_json(data["tier"])
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


def redact_sensitive(value: UpdateSpaceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "supported_email_domains" in value:
        import capo_repostspace.types.supported_email_domains_parameters

        out["supported_email_domains"] = (
            capo_repostspace.types.supported_email_domains_parameters.redact_sensitive(
                value["supported_email_domains"]
            )
        )
    return out
