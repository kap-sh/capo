"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceProfile``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.account_id_string
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.receiver_address
    import capo_invoicing.types.sensitive_basic_string_without_space


class InvoiceProfile(TypedDict, closed=True):
    account_id: NotRequired["capo_invoicing.types.account_id_string.AccountIdString"]
    """<p> The account ID the invoice profile is generated for. </p>"""
    receiver_name: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p> The name of the person receiving the invoice profile. </p>"""
    receiver_address: NotRequired[
        "capo_invoicing.types.receiver_address.ReceiverAddress"
    ]
    """<p>The address of the receiver that will be printed on the invoice. </p>"""
    receiver_email: NotRequired[
        "capo_invoicing.types.sensitive_basic_string_without_space.SensitiveBasicStringWithoutSpace"
    ]
    """<p>The email address for the invoice profile receiver. </p>"""
    issuer: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p> This specifies the issuing entity of the invoice. </p>"""
    tax_registration_number: NotRequired[
        "capo_invoicing.types.sensitive_basic_string_without_space.SensitiveBasicStringWithoutSpace"
    ]
    """<p> Your Tax Registration Number (TRN) information. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceProfile) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "receiver_name" in value:
        out["ReceiverName"] = value["receiver_name"]
    if "receiver_address" in value:
        import capo_invoicing.types.receiver_address

        out["ReceiverAddress"] = (
            capo_invoicing.types.receiver_address.serialize_aws_json_1_0(
                value["receiver_address"]
            )
        )
    if "receiver_email" in value:
        out["ReceiverEmail"] = value["receiver_email"]
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
    if "tax_registration_number" in value:
        out["TaxRegistrationNumber"] = value["tax_registration_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceProfile:
    out: InvoiceProfile = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("ReceiverName") is not None:
        out["receiver_name"] = data["ReceiverName"]
    if data.get("ReceiverAddress") is not None:
        import capo_invoicing.types.receiver_address

        out["receiver_address"] = (
            capo_invoicing.types.receiver_address.deserialize_aws_json_1_0(
                data["ReceiverAddress"]
            )
        )
    if data.get("ReceiverEmail") is not None:
        out["receiver_email"] = data["ReceiverEmail"]
    if data.get("Issuer") is not None:
        out["issuer"] = data["Issuer"]
    if data.get("TaxRegistrationNumber") is not None:
        out["tax_registration_number"] = data["TaxRegistrationNumber"]
    return out


def redact_sensitive(value: InvoiceProfile) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "receiver_address" in value:
        out["receiver_address"] = "*** Sensitive Data Redacted ***"
    if "receiver_email" in value:
        out["receiver_email"] = "*** Sensitive Data Redacted ***"
    if "tax_registration_number" in value:
        out["tax_registration_number"] = "*** Sensitive Data Redacted ***"
    return out
