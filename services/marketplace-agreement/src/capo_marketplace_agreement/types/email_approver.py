"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#EmailApprover``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.approver_name
    import capo_marketplace_agreement.types.email_address


class EmailApprover(TypedDict, closed=True):
    email_address: "capo_marketplace_agreement.types.email_address.EmailAddress"
    """<p>The email address of the approver.</p>"""
    name: NotRequired["capo_marketplace_agreement.types.approver_name.ApproverName"]
    """<p>The name of the approver.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EmailApprover) -> dict:
    out: dict = {}
    out["emailAddress"] = value["email_address"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EmailApprover:
    out: EmailApprover = {}  # type: ignore[typeddict-item]
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        out["email_address"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EmailApprover) -> dict:
    out: dict = {}
    out["emailAddress"] = value["email_address"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> EmailApprover:
    out: EmailApprover = {}  # type: ignore[typeddict-item]
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        out["email_address"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


def redact_sensitive(value: EmailApprover) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
