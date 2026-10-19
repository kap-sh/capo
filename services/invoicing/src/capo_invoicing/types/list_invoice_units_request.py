"""Generated from Smithy shape ``com.amazonaws.invoicing#ListInvoiceUnitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.as_of_timestamp
    import capo_invoicing.types.filters
    import capo_invoicing.types.max_results_integer
    import capo_invoicing.types.next_token_string


class ListInvoiceUnitsRequest(TypedDict, closed=True):
    filters: NotRequired["capo_invoicing.types.filters.Filters"]
    """<p> An optional input to the list API. If multiple filters are specified, the returned list will be a configuration that match all of the provided filters. Supported filter types are <code>InvoiceReceivers</code>, <code>Names</code>, and <code>Accounts</code>. </p>"""
    next_token: NotRequired["capo_invoicing.types.next_token_string.NextTokenString"]
    """<p>The next token used to indicate where the returned list should start from. </p>"""
    max_results: NotRequired[
        "capo_invoicing.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>The maximum number of invoice units that can be returned. </p>"""
    as_of: NotRequired["capo_invoicing.types.as_of_timestamp.AsOfTimestamp"]
    """<p> The state of an invoice unit at a specified time. You can see legacy invoice units that are currently deleted if the <code>AsOf</code> time is set to before it was deleted. If an <code>AsOf</code> is not provided, the default value is the current time. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListInvoiceUnitsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_invoicing.types.filters

        out["Filters"] = capo_invoicing.types.filters.serialize_aws_json_1_0(
            value["filters"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "as_of" in value:
        import capo_invoicing.types.as_of_timestamp

        out["AsOf"] = capo_invoicing.types.as_of_timestamp.serialize_aws_json_1_0(
            value["as_of"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListInvoiceUnitsRequest:
    out: ListInvoiceUnitsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_invoicing.types.filters

        out["filters"] = capo_invoicing.types.filters.deserialize_aws_json_1_0(
            data["Filters"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("AsOf") is not None:
        import capo_invoicing.types.as_of_timestamp

        out["as_of"] = capo_invoicing.types.as_of_timestamp.deserialize_aws_json_1_0(
            data["AsOf"]
        )
    return out
