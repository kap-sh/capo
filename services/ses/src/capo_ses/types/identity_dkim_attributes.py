"""Generated from Smithy shape ``com.amazonaws.ses#IdentityDkimAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.enabled
    import capo_ses.types.verification_status
    import capo_ses.types.verification_token_list


class IdentityDkimAttributes(TypedDict, closed=True):
    dkim_enabled: "capo_ses.types.enabled.Enabled"
    """<p>Is true if DKIM signing is enabled for email sent from the identity. It's false otherwise. The default value is true.</p>"""
    dkim_verification_status: "capo_ses.types.verification_status.VerificationStatus"
    """<p>Describes whether Amazon SES has successfully verified the DKIM DNS records (tokens) published in the domain name's DNS. (This only applies to domain identities, not email address identities.)</p>"""
    dkim_tokens: NotRequired[
        "capo_ses.types.verification_token_list.VerificationTokenList"
    ]
    """<p>A set of character strings that represent the domain's identity. Using these tokens, you need to create DNS CNAME records that point to DKIM public keys that are hosted by Amazon SES. Amazon Web Services eventually detects that you've updated your DNS records. This detection process might take up to 72 hours. After successful detection, Amazon SES is able to DKIM-sign email originating from that domain. (This only applies to domain identities, not email address identities.)</p> <p>For more information about creating DNS records using DKIM tokens, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html">Amazon SES Developer Guide</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IdentityDkimAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (
            f"{key_prefix}DkimEnabled",
            "true" if value.get("dkim_enabled", False) else "false",
        )
    )
    import capo_ses.types.verification_status

    capo_ses.types.verification_status.serialize_query(
        value["dkim_verification_status"], pairs, f"{key_prefix}DkimVerificationStatus"
    )
    if "dkim_tokens" in value:
        import capo_ses.types.verification_token_list

        capo_ses.types.verification_token_list.serialize_query(
            value["dkim_tokens"], pairs, f"{key_prefix}DkimTokens"
        )


def deserialize_query(el: Element) -> IdentityDkimAttributes:
    out: IdentityDkimAttributes = {}  # type: ignore[typeddict-item]
    child_dkim_enabled = el.find("DkimEnabled")
    if child_dkim_enabled is not None:
        out["dkim_enabled"] = (child_dkim_enabled.text or "").lower() == "true"
    else:
        out["dkim_enabled"] = False
    child_dkim_verification_status = el.find("DkimVerificationStatus")
    if child_dkim_verification_status is not None:
        import capo_ses.types.verification_status

        out["dkim_verification_status"] = (
            capo_ses.types.verification_status.deserialize_query(
                child_dkim_verification_status
            )
        )
    else:
        raise DeserializationError(
            "IdentityDkimAttributes.dkim_verification_status required"
        )
    child_dkim_tokens = el.find("DkimTokens")
    if child_dkim_tokens is not None:
        import capo_ses.types.verification_token_list

        out["dkim_tokens"] = capo_ses.types.verification_token_list.deserialize_query(
            child_dkim_tokens
        )
    return out
