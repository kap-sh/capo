"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.action_link
    import capo_datazone.types.domain_id
    import capo_datazone.types.message
    import capo_datazone.types.metadata_map
    import capo_datazone.types.notification_type
    import capo_datazone.types.task_id
    import capo_datazone.types.task_status
    import capo_datazone.types.title
    import capo_datazone.types.topic


class NotificationOutput(TypedDict, closed=True):
    identifier: "capo_datazone.types.task_id.TaskId"
    """<p>The identifier of the notification.</p>"""
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of a Amazon DataZone domain in which the notification exists.</p>"""
    type: "capo_datazone.types.notification_type.NotificationType"
    """<p>The type of the notification.</p>"""
    topic: "capo_datazone.types.topic.Topic"
    """<p>The topic of the notification.</p>"""
    title: "capo_datazone.types.title.Title"
    """<p>The title of the notification.</p>"""
    message: "capo_datazone.types.message.Message"
    """<p>The message included in the notification.</p>"""
    status: NotRequired["capo_datazone.types.task_status.TaskStatus"]
    """<p>The status included in the notification.</p>"""
    action_link: "capo_datazone.types.action_link.ActionLink"
    """<p>The action link included in the notification.</p>"""
    creation_timestamp: "datetime.datetime"
    """<p>The timestamp of when a notification was created.</p>"""
    last_updated_timestamp: "datetime.datetime"
    """<p>The timestamp of when the notification was last updated.</p>"""
    metadata: NotRequired["capo_datazone.types.metadata_map.MetadataMap"]
    """<p>The metadata included in the notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationOutput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["domainIdentifier"] = value["domain_identifier"]
    import capo_datazone.types.notification_type

    out["type"] = capo_datazone.types.notification_type.serialize_json(value["type"])
    import capo_datazone.types.topic

    out["topic"] = capo_datazone.types.topic.serialize_json(value["topic"])
    out["title"] = value["title"]
    out["message"] = value["message"]
    if "status" in value:
        import capo_datazone.types.task_status

        out["status"] = capo_datazone.types.task_status.serialize_json(value["status"])
    out["actionLink"] = value["action_link"]
    import capo_datazone.types._prelude.timestamp

    out["creationTimestamp"] = capo_datazone.types._prelude.timestamp.serialize_json(
        value["creation_timestamp"]
    )
    import capo_datazone.types._prelude.timestamp

    out["lastUpdatedTimestamp"] = capo_datazone.types._prelude.timestamp.serialize_json(
        value["last_updated_timestamp"]
    )
    if "metadata" in value:
        import capo_datazone.types.metadata_map

        out["metadata"] = capo_datazone.types.metadata_map.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> NotificationOutput:
    out: NotificationOutput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("domainIdentifier") is not None:
        out["domain_identifier"] = data["domainIdentifier"]
    else:
        out["domain_identifier"] = ""
    if data.get("type") is not None:
        import capo_datazone.types.notification_type

        out["type"] = capo_datazone.types.notification_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_datazone.types.notification_type.NotificationType", ""
        )
    if data.get("topic") is not None:
        import capo_datazone.types.topic

        out["topic"] = capo_datazone.types.topic.deserialize_json(data["topic"])
    else:
        raise DeserializationError("NotificationOutput.topic required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("status") is not None:
        import capo_datazone.types.task_status

        out["status"] = capo_datazone.types.task_status.deserialize_json(data["status"])
    if data.get("actionLink") is not None:
        out["action_link"] = data["actionLink"]
    else:
        out["action_link"] = ""
    if data.get("creationTimestamp") is not None:
        import capo_datazone.types._prelude.timestamp

        out["creation_timestamp"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["creationTimestamp"]
            )
        )
    else:
        import datetime

        out["creation_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_datazone.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTimestamp"]
            )
        )
    else:
        import datetime

        out["last_updated_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("metadata") is not None:
        import capo_datazone.types.metadata_map

        out["metadata"] = capo_datazone.types.metadata_map.deserialize_json(
            data["metadata"]
        )
    return out


def redact_sensitive(value: NotificationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    if "action_link" in value:
        out["action_link"] = "*** Sensitive Data Redacted ***"
    return out
