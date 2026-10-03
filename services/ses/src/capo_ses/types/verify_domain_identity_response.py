"""Generated from Smithy shape ``com.amazonaws.ses#VerifyDomainIdentityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.verification_token


class VerifyDomainIdentityResponse(TypedDict, closed=True):
    verification_token: "capo_ses.types.verification_token.VerificationToken"
    """<p>A TXT record that you must place in the DNS settings of the domain to complete domain verification with Amazon SES.</p> <p>As Amazon SES searches for the TXT record, the domain's verification status is "Pending". When Amazon SES detects the record, the domain's verification status changes to "Success". If Amazon SES is unable to detect the record within 72 hours, the domain's verification status changes to "Failed." In that case, to verify the domain, you must restart the verification process from the beginning. The domain's verification status also changes to "Success" when it is DKIM verified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifyDomainIdentityResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}VerificationToken", str(value["verification_token"])))


def deserialize_query(el: Element) -> VerifyDomainIdentityResponse:
    out: VerifyDomainIdentityResponse = {}  # type: ignore[typeddict-item]
    child_verification_token = el.find("VerificationToken")
    if child_verification_token is not None:
        out["verification_token"] = str(child_verification_token.text or "")
    else:
        raise DeserializationError(
            "VerifyDomainIdentityResponse.verification_token required"
        )
    return out
