"""Generated from Smithy shape ``com.amazonaws.ses#VerifyEmailIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.address


class VerifyEmailIdentityRequest(TypedDict, closed=True):
    email_address: "capo_ses.types.address.Address"
    """<p>The email address to be verified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifyEmailIdentityRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EmailAddress", str(value["email_address"])))


def deserialize_query(el: Element) -> VerifyEmailIdentityRequest:
    out: VerifyEmailIdentityRequest = {}  # type: ignore[typeddict-item]
    child_email_address = el.find("EmailAddress")
    if child_email_address is not None:
        out["email_address"] = str(child_email_address.text or "")
    else:
        out["email_address"] = ""
    return out
