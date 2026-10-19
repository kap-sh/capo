"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListListenersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.listener_summary_list
    import capo_vpc_lattice.types.next_token


class ListListenersResponse(TypedDict, closed=True):
    items: "capo_vpc_lattice.types.listener_summary_list.ListenerSummaryList"
    """<p>Information about the listeners.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListListenersResponse) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.listener_summary_list

    out["items"] = capo_vpc_lattice.types.listener_summary_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListListenersResponse:
    out: ListListenersResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_vpc_lattice.types.listener_summary_list

        out["items"] = capo_vpc_lattice.types.listener_summary_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
