"""Generated from Smithy shape ``com.amazonaws.invoicing#GetInvoicePDFRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.string_without_new_line


class GetInvoicePDFRequest(TypedDict, closed=True):
    invoice_id: "capo_invoicing.types.string_without_new_line.StringWithoutNewLine"
    """<p> Your unique invoice ID. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetInvoicePDFRequest) -> dict:
    out: dict = {}
    out["InvoiceId"] = value["invoice_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetInvoicePDFRequest:
    out: GetInvoicePDFRequest = {}  # type: ignore[typeddict-item]
    if data.get("InvoiceId") is not None:
        out["invoice_id"] = data["InvoiceId"]
    else:
        out["invoice_id"] = ""
    return out
