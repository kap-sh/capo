"""Generated from Smithy shape ``com.amazonaws.ses#IdentityVerificationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.verification_status
    import capo_ses.types.verification_token


class IdentityVerificationAttributes(TypedDict, closed=True):
    verification_status: "capo_ses.types.verification_status.VerificationStatus"
    """<p>The verification status of the identity: "Pending", "Success", "Failed", or "TemporaryFailure".</p>"""
    verification_token: NotRequired[
        "capo_ses.types.verification_token.VerificationToken"
    ]
    """<p>The verification token for a domain identity. Null for email address identities.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IdentityVerificationAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.verification_status

    capo_ses.types.verification_status.serialize_query(
        value["verification_status"], pairs, f"{key_prefix}VerificationStatus"
    )
    if "verification_token" in value:
        pairs.append(
            (f"{key_prefix}VerificationToken", str(value["verification_token"]))
        )


def deserialize_query(el: Element) -> IdentityVerificationAttributes:
    out: IdentityVerificationAttributes = {}  # type: ignore[typeddict-item]
    child_verification_status = el.find("VerificationStatus")
    if child_verification_status is not None:
        import capo_ses.types.verification_status

        out["verification_status"] = (
            capo_ses.types.verification_status.deserialize_query(
                child_verification_status
            )
        )
    else:
        raise DeserializationError(
            "IdentityVerificationAttributes.verification_status required"
        )
    child_verification_token = el.find("VerificationToken")
    if child_verification_token is not None:
        out["verification_token"] = str(child_verification_token.text or "")
    return out
