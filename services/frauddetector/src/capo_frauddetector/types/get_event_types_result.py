"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEventTypesResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.event_type_list
    import capo_frauddetector.types.string


class GetEventTypesResult(TypedDict, closed=True):
    event_types: NotRequired["capo_frauddetector.types.event_type_list.eventTypeList"]
    """<p>An array of event types.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next page token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventTypesResult) -> dict:
    out: dict = {}
    if "event_types" in value:
        import capo_frauddetector.types.event_type_list

        out["eventTypes"] = (
            capo_frauddetector.types.event_type_list.serialize_aws_json_1_1(
                value["event_types"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventTypesResult:
    out: GetEventTypesResult = {}  # type: ignore[typeddict-item]
    if data.get("eventTypes") is not None:
        import capo_frauddetector.types.event_type_list

        out["event_types"] = (
            capo_frauddetector.types.event_type_list.deserialize_aws_json_1_1(
                data["eventTypes"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: GetEventTypesResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "event_types" in value:
        import capo_frauddetector.types.event_type_list

        out["event_types"] = capo_frauddetector.types.event_type_list.redact_sensitive(
            value["event_types"]
        )
    return out
