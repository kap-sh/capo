"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListOmniDashboardsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.next_token
    import capo_cloudwatchomni.types.omni_dashboard_summary_list


class ListOmniDashboardsOutput(TypedDict, closed=True):
    items: (
        "capo_cloudwatchomni.types.omni_dashboard_summary_list.OmniDashboardSummaryList"
    )
    """The list of dashboard summaries."""
    next_token: NotRequired["capo_cloudwatchomni.types.next_token.NextToken"]
    """A token to retrieve the next page of results, or null if there are no more results."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOmniDashboardsOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.omni_dashboard_summary_list

    out["items"] = capo_cloudwatchomni.types.omni_dashboard_summary_list.serialize_cbor(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListOmniDashboardsOutput:
    out: ListOmniDashboardsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_cloudwatchomni.types.omni_dashboard_summary_list

        out["items"] = (
            capo_cloudwatchomni.types.omni_dashboard_summary_list.deserialize_cbor(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
