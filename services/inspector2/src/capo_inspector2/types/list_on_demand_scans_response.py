"""Generated from Smithy shape ``com.amazonaws.inspector2#ListOnDemandScansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.on_demand_scan_list
    import capo_inspector2.types.on_demand_scan_next_token


class ListOnDemandScansResponse(TypedDict, closed=True):
    items: "capo_inspector2.types.on_demand_scan_list.OnDemandScanList"
    """<p>The list of on-demand scans that match the request.</p>"""
    next_token: NotRequired[
        "capo_inspector2.types.on_demand_scan_next_token.OnDemandScanNextToken"
    ]
    """<p>A pagination token to use in a subsequent request to retrieve the next page of results. This field is absent when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOnDemandScansResponse) -> dict:
    out: dict = {}
    import capo_inspector2.types.on_demand_scan_list

    out["items"] = capo_inspector2.types.on_demand_scan_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOnDemandScansResponse:
    out: ListOnDemandScansResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_inspector2.types.on_demand_scan_list

        out["items"] = capo_inspector2.types.on_demand_scan_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
