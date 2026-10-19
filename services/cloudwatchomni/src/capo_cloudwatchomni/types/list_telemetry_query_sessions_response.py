"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListTelemetryQuerySessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.session_summary_list


class ListTelemetryQuerySessionsResponse(TypedDict, closed=True):
    sessions: "capo_cloudwatchomni.types.session_summary_list.SessionSummaryList"
    """The list of session summaries."""
    next_token: NotRequired["str"]
    """A token to retrieve the next page of results, or null if there are no more results."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTelemetryQuerySessionsResponse) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.session_summary_list

    out["sessions"] = capo_cloudwatchomni.types.session_summary_list.serialize_cbor(
        value["sessions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTelemetryQuerySessionsResponse:
    out: ListTelemetryQuerySessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessions") is not None:
        import capo_cloudwatchomni.types.session_summary_list

        out["sessions"] = (
            capo_cloudwatchomni.types.session_summary_list.deserialize_cbor(
                data["sessions"]
            )
        )
    else:
        out["sessions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
