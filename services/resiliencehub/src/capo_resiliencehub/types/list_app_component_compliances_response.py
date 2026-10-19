"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppComponentCompliancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.component_compliances_list
    import capo_resiliencehub.types.next_token


class ListAppComponentCompliancesResponse(TypedDict, closed=True):
    component_compliances: (
        "capo_resiliencehub.types.component_compliances_list.ComponentCompliancesList"
    )
    """<p>The compliances for an Resilience Hub Application Component, returned as an object. This object contains the names of the Application Components, compliances, costs, resiliency scores, outage scores, and more.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppComponentCompliancesResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.component_compliances_list

    out["componentCompliances"] = (
        capo_resiliencehub.types.component_compliances_list.serialize_json(
            value["component_compliances"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppComponentCompliancesResponse:
    out: ListAppComponentCompliancesResponse = {}  # type: ignore[typeddict-item]
    if data.get("componentCompliances") is not None:
        import capo_resiliencehub.types.component_compliances_list

        out["component_compliances"] = (
            capo_resiliencehub.types.component_compliances_list.deserialize_json(
                data["componentCompliances"]
            )
        )
    else:
        out["component_compliances"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
