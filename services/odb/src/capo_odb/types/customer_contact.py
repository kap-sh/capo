"""Generated from Smithy shape ``com.amazonaws.odb#CustomerContact``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.sensitive_string


class CustomerContact(TypedDict, closed=True):
    email: NotRequired["capo_odb.types.sensitive_string.SensitiveString"]
    """<p>The email address of the contact.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomerContact) -> dict:
    out: dict = {}
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomerContact:
    out: CustomerContact = {}  # type: ignore[typeddict-item]
    if data.get("email") is not None:
        out["email"] = data["email"]
    return out


def redact_sensitive(value: CustomerContact) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    return out
