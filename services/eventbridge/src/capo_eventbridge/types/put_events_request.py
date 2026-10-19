"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.endpoint_id
    import capo_eventbridge.types.put_events_request_entry_list


class PutEventsRequest(TypedDict, closed=True):
    entries: (
        "capo_eventbridge.types.put_events_request_entry_list.PutEventsRequestEntryList"
    )
    """<p>The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.</p>"""
    endpoint_id: NotRequired["capo_eventbridge.types.endpoint_id.EndpointId"]
    """<p>The URL subdomain of the endpoint. For example, if the URL for Endpoint is https://abcde.veo.endpoints.event.amazonaws.com, then the EndpointId is <code>abcde.veo</code>.</p> <important> <p>When using Java, you must include <code>auth-crt</code> on the class path.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventsRequest) -> dict:
    out: dict = {}
    import capo_eventbridge.types.put_events_request_entry_list

    out["Entries"] = (
        capo_eventbridge.types.put_events_request_entry_list.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEventsRequest:
    out: PutEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Entries") is not None:
        import capo_eventbridge.types.put_events_request_entry_list

        out["entries"] = (
            capo_eventbridge.types.put_events_request_entry_list.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    if data.get("EndpointId") is not None:
        out["endpoint_id"] = data["EndpointId"]
    return out
