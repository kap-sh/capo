"""Generated from Smithy shape ``com.amazonaws.invoicing#ListProcurementPortalSuppliersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.max_results
    import capo_invoicing.types.procurement_portal_id_string


class ListProcurementPortalSuppliersRequest(TypedDict, closed=True):
    portal_identifier: (
        "capo_invoicing.types.procurement_portal_id_string.ProcurementPortalIdString"
    )
    """<p>The unique identifier of the procurement portal for which to list suppliers. Use the <code>PortalIdentifier</code> value returned by <code>ListProcurementPortals</code>.</p>"""
    next_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The token for the next set of results. You received this token from a previous call.</p>"""
    max_results: NotRequired["capo_invoicing.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. Default is 100.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProcurementPortalSuppliersRequest) -> dict:
    out: dict = {}
    out["PortalIdentifier"] = value["portal_identifier"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProcurementPortalSuppliersRequest:
    out: ListProcurementPortalSuppliersRequest = {}  # type: ignore[typeddict-item]
    if data.get("PortalIdentifier") is not None:
        out["portal_identifier"] = data["PortalIdentifier"]
    else:
        raise DeserializationError(
            "ListProcurementPortalSuppliersRequest.portal_identifier required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
