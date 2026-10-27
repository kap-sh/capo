"""Generated from Smithy shape ``com.amazonaws.billing#ApproverDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.sensitive_email
    import capo_billing.types.sensitive_string


class ApproverDetails(TypedDict, closed=True):
    name: "capo_billing.types.sensitive_string.SensitiveString"
    """<p>The name of the approver as it appears on the contract. This value can be up to 256 characters.</p>"""
    title: "capo_billing.types.sensitive_string.SensitiveString"
    """<p>The title of the approver, such as <code>Chief Financial Officer</code>. This value can be up to 256 characters.</p>"""
    email: "capo_billing.types.sensitive_email.SensitiveEmail"
    """<p>The email address of the approver. This value is 3–256 characters and must be a valid email address.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ApproverDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["title"] = value["title"]
    out["email"] = value["email"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ApproverDetails:
    out: ApproverDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("email") is not None:
        out["email"] = data["email"]
    else:
        out["email"] = ""
    return out


def redact_sensitive(value: ApproverDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    return out
