"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListViewsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.view_summary_list


class ListViewsResponse(TypedDict, closed=True):
    items: "capo_cloudwatchomni.types.view_summary_list.ViewSummaryList"
    """The list of view summaries."""
    next_token: NotRequired["str"]
    """A token to retrieve the next page of results, or null if there are no more results."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListViewsResponse) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.view_summary_list

    out["items"] = capo_cloudwatchomni.types.view_summary_list.serialize_cbor(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListViewsResponse:
    out: ListViewsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_cloudwatchomni.types.view_summary_list

        out["items"] = capo_cloudwatchomni.types.view_summary_list.deserialize_cbor(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
