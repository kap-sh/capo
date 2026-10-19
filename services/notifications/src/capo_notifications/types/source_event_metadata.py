"""Generated from Smithy shape ``com.amazonaws.notifications#SourceEventMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_notifications.types.account_id
    import capo_notifications.types.region
    import capo_notifications.types.resources
    import capo_notifications.types.source


class SourceEventMetadata(TypedDict, closed=True):
    event_type_version: "str"
    """<p>The version of the type of event.</p>"""
    source_event_id: "str"
    """<p>The source event id.</p>"""
    event_origin_region: NotRequired["capo_notifications.types.region.Region"]
    """<p>The Region the event originated from.</p>"""
    related_account: "capo_notifications.types.account_id.AccountId"
    """<p>The primary Amazon Web Services account of <code>SourceEvent</code>.</p>"""
    source: "capo_notifications.types.source.Source"
    """<p>The Amazon Web Services service the event originates from. For example <code>aws.cloudwatch</code>.</p>"""
    event_occurrence_time: "datetime.datetime"
    """<p>The date and time the source event occurred. This is based on the Source Event.</p>"""
    event_type: "str"
    """<p>The type of event. For example, an Amazon CloudWatch state change.</p>"""
    related_resources: "capo_notifications.types.resources.Resources"
    """<p>A list of resources related to this <code>NotificationEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceEventMetadata) -> dict:
    out: dict = {}
    out["eventTypeVersion"] = value["event_type_version"]
    out["sourceEventId"] = value["source_event_id"]
    if "event_origin_region" in value:
        out["eventOriginRegion"] = value["event_origin_region"]
    out["relatedAccount"] = value["related_account"]
    out["source"] = value["source"]
    import capo_notifications._protocol.serialize

    out["eventOccurrenceTime"] = capo_notifications._protocol.serialize.fmt_date_time(
        value["event_occurrence_time"]
    )
    out["eventType"] = value["event_type"]
    import capo_notifications.types.resources

    out["relatedResources"] = capo_notifications.types.resources.serialize_json(
        value["related_resources"]
    )
    return out


def deserialize_json(data: dict) -> SourceEventMetadata:
    out: SourceEventMetadata = {}  # type: ignore[typeddict-item]
    if data.get("eventTypeVersion") is not None:
        out["event_type_version"] = data["eventTypeVersion"]
    else:
        out["event_type_version"] = ""
    if data.get("sourceEventId") is not None:
        out["source_event_id"] = data["sourceEventId"]
    else:
        out["source_event_id"] = ""
    if data.get("eventOriginRegion") is not None:
        out["event_origin_region"] = data["eventOriginRegion"]
    if data.get("relatedAccount") is not None:
        out["related_account"] = data["relatedAccount"]
    else:
        out["related_account"] = ""
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("eventOccurrenceTime") is not None:
        import datetime

        out["event_occurrence_time"] = datetime.datetime.fromisoformat(
            data["eventOccurrenceTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["event_occurrence_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    else:
        out["event_type"] = ""
    if data.get("relatedResources") is not None:
        import capo_notifications.types.resources

        out["related_resources"] = capo_notifications.types.resources.deserialize_json(
            data["relatedResources"]
        )
    else:
        out["related_resources"] = []
    return out
