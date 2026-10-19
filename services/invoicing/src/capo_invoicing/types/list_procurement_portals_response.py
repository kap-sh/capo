"""Generated from Smithy shape ``com.amazonaws.invoicing#ListProcurementPortalsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.procurement_portals


class ListProcurementPortalsResponse(TypedDict, closed=True):
    procurement_portals: "capo_invoicing.types.procurement_portals.ProcurementPortals"
    """<p>The list of procurement portals available for configuration.</p>"""
    next_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>The token to use to retrieve the next set of results, or null if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProcurementPortalsResponse) -> dict:
    out: dict = {}
    import capo_invoicing.types.procurement_portals

    out["ProcurementPortals"] = (
        capo_invoicing.types.procurement_portals.serialize_aws_json_1_0(
            value["procurement_portals"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProcurementPortalsResponse:
    out: ListProcurementPortalsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProcurementPortals") is not None:
        import capo_invoicing.types.procurement_portals

        out["procurement_portals"] = (
            capo_invoicing.types.procurement_portals.deserialize_aws_json_1_0(
                data["ProcurementPortals"]
            )
        )
    else:
        out["procurement_portals"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
