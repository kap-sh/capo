"""Generated from Smithy shape ``com.amazonaws.billing#AdditionalRecipient``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.sensitive_email


class AdditionalRecipient(TypedDict, closed=True):
    email: "capo_billing.types.sensitive_email.SensitiveEmail"
    """<p>The email address of the recipient. This value is 3–256 characters and must be a valid email address.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AdditionalRecipient) -> dict:
    out: dict = {}
    out["email"] = value["email"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AdditionalRecipient:
    out: AdditionalRecipient = {}  # type: ignore[typeddict-item]
    if data.get("email") is not None:
        out["email"] = data["email"]
    else:
        out["email"] = ""
    return out


def redact_sensitive(value: AdditionalRecipient) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    return out
