"""Generated from Smithy shape ``com.amazonaws.acm#AcmeAccount``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_acm.types.acme_account_status
    import capo_acm.types.acme_external_account_binding_arn
    import capo_acm.types.contact_list


class AcmeAccount(TypedDict, closed=True):
    account_url: NotRequired["str"]
    """<p>The URL of the ACME account.</p>"""
    public_key_thumbprint: NotRequired["str"]
    """<p>The thumbprint of the public key associated with the ACME account.</p>"""
    status: NotRequired["capo_acm.types.acme_account_status.AcmeAccountStatus"]
    """<p>The status of the ACME account.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time at which the ACME account was created.</p>"""
    acme_external_account_binding_arn: NotRequired[
        "capo_acm.types.acme_external_account_binding_arn.AcmeExternalAccountBindingArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the external account binding associated with this ACME account.</p>"""
    contacts: NotRequired["capo_acm.types.contact_list.ContactList"]
    """<p>The contact information for the ACME account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeAccount) -> dict:
    out: dict = {}
    if "account_url" in value:
        out["AccountUrl"] = value["account_url"]
    if "public_key_thumbprint" in value:
        out["PublicKeyThumbprint"] = value["public_key_thumbprint"]
    if "status" in value:
        import capo_acm.types.acme_account_status

        out["Status"] = capo_acm.types.acme_account_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "created_at" in value:
        import capo_acm.types._prelude.timestamp

        out["CreatedAt"] = capo_acm.types._prelude.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "acme_external_account_binding_arn" in value:
        out["AcmeExternalAccountBindingArn"] = value[
            "acme_external_account_binding_arn"
        ]
    if "contacts" in value:
        import capo_acm.types.contact_list

        out["Contacts"] = capo_acm.types.contact_list.serialize_aws_json_1_1(
            value["contacts"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcmeAccount:
    out: AcmeAccount = {}  # type: ignore[typeddict-item]
    if data.get("AccountUrl") is not None:
        out["account_url"] = data["AccountUrl"]
    if data.get("PublicKeyThumbprint") is not None:
        out["public_key_thumbprint"] = data["PublicKeyThumbprint"]
    if data.get("Status") is not None:
        import capo_acm.types.acme_account_status

        out["status"] = capo_acm.types.acme_account_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("CreatedAt") is not None:
        import capo_acm.types._prelude.timestamp

        out["created_at"] = capo_acm.types._prelude.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("AcmeExternalAccountBindingArn") is not None:
        out["acme_external_account_binding_arn"] = data["AcmeExternalAccountBindingArn"]
    if data.get("Contacts") is not None:
        import capo_acm.types.contact_list

        out["contacts"] = capo_acm.types.contact_list.deserialize_aws_json_1_1(
            data["Contacts"]
        )
    return out


def redact_sensitive(value: AcmeAccount) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contacts" in value:
        out["contacts"] = "*** Sensitive Data Redacted ***"
    return out
