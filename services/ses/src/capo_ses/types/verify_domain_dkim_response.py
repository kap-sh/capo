"""Generated from Smithy shape ``com.amazonaws.ses#VerifyDomainDkimResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.verification_token_list


class VerifyDomainDkimResponse(TypedDict, closed=True):
    dkim_tokens: "capo_ses.types.verification_token_list.VerificationTokenList"
    """<p>A set of character strings that represent the domain's identity. If the identity is an email address, the tokens represent the domain of that address.</p> <p>Using these tokens, you need to create DNS CNAME records that point to DKIM public keys that are hosted by Amazon SES. Amazon Web Services eventually detects that you've updated your DNS records. This detection process might take up to 72 hours. After successful detection, Amazon SES is able to DKIM-sign email originating from that domain. (This only applies to domain identities, not email address identities.)</p> <p>For more information about creating DNS records using DKIM tokens, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html">Amazon SES Developer Guide</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifyDomainDkimResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.verification_token_list

    capo_ses.types.verification_token_list.serialize_query(
        value["dkim_tokens"], pairs, f"{key_prefix}DkimTokens"
    )


def deserialize_query(el: Element) -> VerifyDomainDkimResponse:
    out: VerifyDomainDkimResponse = {}  # type: ignore[typeddict-item]
    child_dkim_tokens = el.find("DkimTokens")
    if child_dkim_tokens is not None:
        import capo_ses.types.verification_token_list

        out["dkim_tokens"] = capo_ses.types.verification_token_list.deserialize_query(
            child_dkim_tokens
        )
    else:
        raise DeserializationError("VerifyDomainDkimResponse.dkim_tokens required")
    return out
