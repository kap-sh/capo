"""Generated from Smithy shape ``com.amazonaws.guardduty#Signal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.activities
    import capo_guardduty.types.actor_ids
    import capo_guardduty.types.double
    import capo_guardduty.types.endpoint_ids
    import capo_guardduty.types.indicators
    import capo_guardduty.types.integer
    import capo_guardduty.types.resource_uids
    import capo_guardduty.types.signal_description
    import capo_guardduty.types.signal_type
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class Signal(TypedDict, closed=True):
    uid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique identifier of the signal.</p>"""
    type: NotRequired["capo_guardduty.types.signal_type.SignalType"]
    """<p>The type of the signal used to identify an attack sequence.</p> <p>Signals can be GuardDuty findings or activities observed in data sources that GuardDuty monitors. For more information, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html">Foundational data sources</a> in the <i>Amazon GuardDuty User Guide</i>.</p> <p>A signal type can be one of the valid values listed in this API. Here are the related descriptions:</p> <ul> <li> <p> <code>FINDING</code> - Individually generated GuardDuty finding.</p> </li> <li> <p> <code>CLOUD_TRAIL</code> - Activity observed from CloudTrail logs</p> </li> <li> <p> <code>S3_DATA_EVENTS</code> - Activity observed from CloudTrail data events for S3. Activities associated with this type will show up only when you have enabled GuardDuty S3 Protection feature in your account. For more information about S3 Protection and steps to enable it, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html">S3 Protection</a> in the <i>Amazon GuardDuty User Guide</i>.</p> </li> </ul>"""
    description: NotRequired[
        "capo_guardduty.types.signal_description.SignalDescription"
    ]
    """<p>The description of the signal.</p>"""
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the signal. For example, when signal type is <code>FINDING</code>, the signal name is the name of the finding.</p>"""
    created_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the first finding or activity related to this signal was observed.</p>"""
    updated_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when this signal was last observed.</p>"""
    first_seen_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the first finding or activity related to this signal was observed.</p>"""
    last_seen_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp when the last finding or activity related to this signal was observed.</p>"""
    severity: NotRequired["capo_guardduty.types.double.Double"]
    """<p>The severity associated with the signal. For more information about severity, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings-severity.html">Findings severity levels</a> in the <i>Amazon GuardDuty User Guide</i>.</p>"""
    count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of times this signal was observed.</p>"""
    resource_uids: NotRequired["capo_guardduty.types.resource_uids.ResourceUids"]
    """<p>Information about the unique identifiers of the resources involved in the signal.</p>"""
    actor_ids: NotRequired["capo_guardduty.types.actor_ids.ActorIds"]
    """<p>Information about the IDs of the threat actors involved in the signal.</p>"""
    endpoint_ids: NotRequired["capo_guardduty.types.endpoint_ids.EndpointIds"]
    """<p>Information about the endpoint IDs associated with this signal.</p>"""
    signal_indicators: NotRequired["capo_guardduty.types.indicators.Indicators"]
    """<p>Contains information about the indicators associated with the signals.</p>"""
    activities: NotRequired["capo_guardduty.types.activities.Activities"]
    """<p>Contains information about the activities, such as API calls, that were observed for this signal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Signal) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "type" in value:
        import capo_guardduty.types.signal_type

        out["type"] = capo_guardduty.types.signal_type.serialize_json(value["type"])
    if "description" in value:
        out["description"] = value["description"]
    if "name" in value:
        out["name"] = value["name"]
    if "created_at" in value:
        import capo_guardduty.types.timestamp

        out["createdAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_guardduty.types.timestamp

        out["updatedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "first_seen_at" in value:
        import capo_guardduty.types.timestamp

        out["firstSeenAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["first_seen_at"]
        )
    if "last_seen_at" in value:
        import capo_guardduty.types.timestamp

        out["lastSeenAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["last_seen_at"]
        )
    if "severity" in value:
        out["severity"] = (
            "NaN"
            if value["severity"] != value["severity"]
            else "Infinity"
            if value["severity"] == float("inf")
            else "-Infinity"
            if value["severity"] == float("-inf")
            else value["severity"]
        )
    if "count" in value:
        out["count"] = value["count"]
    if "resource_uids" in value:
        import capo_guardduty.types.resource_uids

        out["resourceUids"] = capo_guardduty.types.resource_uids.serialize_json(
            value["resource_uids"]
        )
    if "actor_ids" in value:
        import capo_guardduty.types.actor_ids

        out["actorIds"] = capo_guardduty.types.actor_ids.serialize_json(
            value["actor_ids"]
        )
    if "endpoint_ids" in value:
        import capo_guardduty.types.endpoint_ids

        out["endpointIds"] = capo_guardduty.types.endpoint_ids.serialize_json(
            value["endpoint_ids"]
        )
    if "signal_indicators" in value:
        import capo_guardduty.types.indicators

        out["signalIndicators"] = capo_guardduty.types.indicators.serialize_json(
            value["signal_indicators"]
        )
    if "activities" in value:
        import capo_guardduty.types.activities

        out["activities"] = capo_guardduty.types.activities.serialize_json(
            value["activities"]
        )
    return out


def deserialize_json(data: dict) -> Signal:
    out: Signal = {}  # type: ignore[typeddict-item]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    if data.get("type") is not None:
        import capo_guardduty.types.signal_type

        out["type"] = capo_guardduty.types.signal_type.deserialize_json(data["type"])
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("createdAt") is not None:
        import capo_guardduty.types.timestamp

        out["created_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_guardduty.types.timestamp

        out["updated_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("firstSeenAt") is not None:
        import capo_guardduty.types.timestamp

        out["first_seen_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["firstSeenAt"]
        )
    if data.get("lastSeenAt") is not None:
        import capo_guardduty.types.timestamp

        out["last_seen_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["lastSeenAt"]
        )
    if data.get("severity") is not None:
        out["severity"] = float(data["severity"])
    if data.get("count") is not None:
        out["count"] = data["count"]
    if data.get("resourceUids") is not None:
        import capo_guardduty.types.resource_uids

        out["resource_uids"] = capo_guardduty.types.resource_uids.deserialize_json(
            data["resourceUids"]
        )
    if data.get("actorIds") is not None:
        import capo_guardduty.types.actor_ids

        out["actor_ids"] = capo_guardduty.types.actor_ids.deserialize_json(
            data["actorIds"]
        )
    if data.get("endpointIds") is not None:
        import capo_guardduty.types.endpoint_ids

        out["endpoint_ids"] = capo_guardduty.types.endpoint_ids.deserialize_json(
            data["endpointIds"]
        )
    if data.get("signalIndicators") is not None:
        import capo_guardduty.types.indicators

        out["signal_indicators"] = capo_guardduty.types.indicators.deserialize_json(
            data["signalIndicators"]
        )
    if data.get("activities") is not None:
        import capo_guardduty.types.activities

        out["activities"] = capo_guardduty.types.activities.deserialize_json(
            data["activities"]
        )
    return out
