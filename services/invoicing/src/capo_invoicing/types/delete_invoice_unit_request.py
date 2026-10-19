"""Generated from Smithy shape ``com.amazonaws.invoicing#DeleteInvoiceUnitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.invoice_unit_arn_string


class DeleteInvoiceUnitRequest(TypedDict, closed=True):
    invoice_unit_arn: (
        "capo_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"
    )
    """<p> The ARN to identify an invoice unit. This information can't be modified or deleted. </p>"""
    client_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p> A unique, case-sensitive identifier that you provide to ensure idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteInvoiceUnitRequest) -> dict:
    out: dict = {}
    out["InvoiceUnitArn"] = value["invoice_unit_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteInvoiceUnitRequest:
    out: DeleteInvoiceUnitRequest = {}  # type: ignore[typeddict-item]
    if data.get("InvoiceUnitArn") is not None:
        out["invoice_unit_arn"] = data["InvoiceUnitArn"]
    else:
        out["invoice_unit_arn"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
