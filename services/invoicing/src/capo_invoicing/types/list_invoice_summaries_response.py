"""Generated from Smithy shape ``com.amazonaws.invoicing#ListInvoiceSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.invoice_summaries
    import capo_invoicing.types.next_token_string


class ListInvoiceSummariesResponse(TypedDict, closed=True):
    invoice_summaries: "capo_invoicing.types.invoice_summaries.InvoiceSummaries"
    """<p>List of key (summary level) invoice details without line item details.</p>"""
    next_token: NotRequired["capo_invoicing.types.next_token_string.NextTokenString"]
    """<p>The token to use to retrieve the next set of results, or null if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInvoiceSummariesResponse) -> dict:
    out: dict = {}
    import capo_invoicing.types.invoice_summaries

    out["InvoiceSummaries"] = (
        capo_invoicing.types.invoice_summaries.serialize_aws_json_1_0(
            value["invoice_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInvoiceSummariesResponse:
    out: ListInvoiceSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("InvoiceSummaries") is not None:
        import capo_invoicing.types.invoice_summaries

        out["invoice_summaries"] = (
            capo_invoicing.types.invoice_summaries.deserialize_aws_json_1_0(
                data["InvoiceSummaries"]
            )
        )
    else:
        out["invoice_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
