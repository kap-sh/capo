"""Generated from Smithy shape ``com.amazonaws.invoicing#UpdateInvoiceUnitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.description_string
    import capo_invoicing.types.invoice_unit_arn_string
    import capo_invoicing.types.invoice_unit_rule
    import capo_invoicing.types.tax_inheritance_disabled_flag


class UpdateInvoiceUnitRequest(TypedDict, closed=True):
    invoice_unit_arn: (
        "capo_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"
    )
    """<p>The ARN to identify an invoice unit. This information can't be modified or deleted. </p>"""
    description: NotRequired[
        "capo_invoicing.types.description_string.DescriptionString"
    ]
    """<p>The assigned description for an invoice unit. This information can't be modified or deleted. </p>"""
    tax_inheritance_disabled: NotRequired[
        "capo_invoicing.types.tax_inheritance_disabled_flag.TaxInheritanceDisabledFlag"
    ]
    """<p>Whether the invoice unit based tax inheritance is/ should be enabled or disabled. </p>"""
    rule: NotRequired["capo_invoicing.types.invoice_unit_rule.InvoiceUnitRule"]
    """<p>The <code>InvoiceUnitRule</code> object used to update invoice units. </p>"""
    client_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p> A unique, case-sensitive identifier that you provide to ensure idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateInvoiceUnitRequest) -> dict:
    out: dict = {}
    out["InvoiceUnitArn"] = value["invoice_unit_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tax_inheritance_disabled" in value:
        out["TaxInheritanceDisabled"] = value["tax_inheritance_disabled"]
    if "rule" in value:
        import capo_invoicing.types.invoice_unit_rule

        out["Rule"] = capo_invoicing.types.invoice_unit_rule.serialize_aws_json_1_0(
            value["rule"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateInvoiceUnitRequest:
    out: UpdateInvoiceUnitRequest = {}  # type: ignore[typeddict-item]
    if data.get("InvoiceUnitArn") is not None:
        out["invoice_unit_arn"] = data["InvoiceUnitArn"]
    else:
        out["invoice_unit_arn"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("TaxInheritanceDisabled") is not None:
        out["tax_inheritance_disabled"] = data["TaxInheritanceDisabled"]
    if data.get("Rule") is not None:
        import capo_invoicing.types.invoice_unit_rule

        out["rule"] = capo_invoicing.types.invoice_unit_rule.deserialize_aws_json_1_0(
            data["Rule"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
