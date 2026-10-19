"""Generated from Smithy shape ``com.amazonaws.invoicing#ListProcurementPortalSuppliersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.procurement_portal_suppliers


class ListProcurementPortalSuppliersResponse(TypedDict, closed=True):
    procurement_portal_suppliers: (
        "capo_invoicing.types.procurement_portal_suppliers.ProcurementPortalSuppliers"
    )
    """<p>The list of suppliers configured for the specified procurement portal.</p>"""
    next_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The token to use to retrieve the next set of results, or null if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProcurementPortalSuppliersResponse) -> dict:
    out: dict = {}
    import capo_invoicing.types.procurement_portal_suppliers

    out["ProcurementPortalSuppliers"] = (
        capo_invoicing.types.procurement_portal_suppliers.serialize_aws_json_1_0(
            value["procurement_portal_suppliers"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProcurementPortalSuppliersResponse:
    out: ListProcurementPortalSuppliersResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProcurementPortalSuppliers") is not None:
        import capo_invoicing.types.procurement_portal_suppliers

        out["procurement_portal_suppliers"] = (
            capo_invoicing.types.procurement_portal_suppliers.deserialize_aws_json_1_0(
                data["ProcurementPortalSuppliers"]
            )
        )
    else:
        out["procurement_portal_suppliers"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
