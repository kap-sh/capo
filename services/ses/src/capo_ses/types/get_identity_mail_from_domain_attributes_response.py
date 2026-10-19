"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityMailFromDomainAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.mail_from_domain_attributes


class GetIdentityMailFromDomainAttributesResponse(TypedDict, closed=True):
    mail_from_domain_attributes: (
        "capo_ses.types.mail_from_domain_attributes.MailFromDomainAttributes"
    )
    """<p>A map of identities to custom MAIL FROM attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityMailFromDomainAttributesResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.mail_from_domain_attributes

    capo_ses.types.mail_from_domain_attributes.serialize_query(
        value["mail_from_domain_attributes"],
        pairs,
        f"{key_prefix}MailFromDomainAttributes",
    )


def deserialize_query(el: Element) -> GetIdentityMailFromDomainAttributesResponse:
    out: GetIdentityMailFromDomainAttributesResponse = {}  # type: ignore[typeddict-item]
    child_mail_from_domain_attributes = el.find("MailFromDomainAttributes")
    if child_mail_from_domain_attributes is not None:
        import capo_ses.types.mail_from_domain_attributes

        out["mail_from_domain_attributes"] = (
            capo_ses.types.mail_from_domain_attributes.deserialize_query(
                child_mail_from_domain_attributes
            )
        )
    else:
        out["mail_from_domain_attributes"] = {}
    return out
