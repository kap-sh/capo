"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutPartnerEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.put_partner_events_request_entry_list


class PutPartnerEventsRequest(TypedDict, closed=True):
    entries: "capo_cloudwatch_events.types.put_partner_events_request_entry_list.PutPartnerEventsRequestEntryList"
    """<p>The list of events to write to the event bus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPartnerEventsRequest) -> dict:
    out: dict = {}
    import capo_cloudwatch_events.types.put_partner_events_request_entry_list

    out["Entries"] = (
        capo_cloudwatch_events.types.put_partner_events_request_entry_list.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPartnerEventsRequest:
    out: PutPartnerEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Entries") is not None:
        import capo_cloudwatch_events.types.put_partner_events_request_entry_list

        out["entries"] = (
            capo_cloudwatch_events.types.put_partner_events_request_entry_list.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    return out
