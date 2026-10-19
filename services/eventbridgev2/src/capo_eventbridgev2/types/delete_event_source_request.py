"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DeleteEventSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_source_arn


class DeleteEventSourceRequest(TypedDict, closed=True):
    event_source_arn: "capo_eventbridgev2.types.event_source_arn.EventSourceArn"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteEventSourceRequest) -> dict:
    out: dict = {}
    out["EventSourceArn"] = value["event_source_arn"]
    return out


def deserialize_cbor(data: dict) -> DeleteEventSourceRequest:
    out: DeleteEventSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventSourceArn") is not None:
        out["event_source_arn"] = data["EventSourceArn"]
    else:
        out["event_source_arn"] = ""
    return out
