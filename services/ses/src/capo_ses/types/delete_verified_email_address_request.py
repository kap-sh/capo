"""Generated from Smithy shape ``com.amazonaws.ses#DeleteVerifiedEmailAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.address


class DeleteVerifiedEmailAddressRequest(TypedDict, closed=True):
    email_address: "capo_ses.types.address.Address"
    """<p>An email address to be removed from the list of verified addresses.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteVerifiedEmailAddressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EmailAddress", str(value["email_address"])))


def deserialize_query(el: Element) -> DeleteVerifiedEmailAddressRequest:
    out: DeleteVerifiedEmailAddressRequest = {}  # type: ignore[typeddict-item]
    child_email_address = el.find("EmailAddress")
    if child_email_address is not None:
        out["email_address"] = str(child_email_address.text or "")
    else:
        out["email_address"] = ""
    return out
