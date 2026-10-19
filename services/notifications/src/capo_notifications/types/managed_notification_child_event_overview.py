"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationChildEventOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.account_id
    import capo_notifications.types.creation_time
    import capo_notifications.types.managed_notification_child_event_summary
    import capo_notifications.types.managed_notification_configuration_os_arn
    import capo_notifications.types.managed_notification_event_arn
    import capo_notifications.types.organizational_unit_id


class ManagedNotificationChildEventOverview(TypedDict, closed=True):
    arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationChildEvent</code>.</p>"""
    managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code>.</p>"""
    related_account: "capo_notifications.types.account_id.AccountId"
    """<p>The account that related to the <code>ManagedNotificationChildEvent</code>.</p>"""
    creation_time: "capo_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>ManagedNotificationChildEvent</code>.</p>"""
    child_event: "capo_notifications.types.managed_notification_child_event_summary.ManagedNotificationChildEventSummary"
    """<p>The content of the <code>ManagedNotificationChildEvent</code>.</p>"""
    aggregate_managed_notification_event_arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn"
    """<p>The Amazon Resource Name (ARN) of the ManagedNotificationEvent that is associated with this <code>ManagedNotificationChildEvent</code>.</p>"""
    organizational_unit_id: NotRequired[
        "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The Organizational Unit Id that an AWS account belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationChildEventOverview) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    out["relatedAccount"] = value["related_account"]
    import capo_notifications.types.creation_time

    out["creationTime"] = capo_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_notifications.types.managed_notification_child_event_summary

    out["childEvent"] = (
        capo_notifications.types.managed_notification_child_event_summary.serialize_json(
            value["child_event"]
        )
    )
    out["aggregateManagedNotificationEventArn"] = value[
        "aggregate_managed_notification_event_arn"
    ]
    if "organizational_unit_id" in value:
        out["organizationalUnitId"] = value["organizational_unit_id"]
    return out


def deserialize_json(data: dict) -> ManagedNotificationChildEventOverview:
    out: ManagedNotificationChildEventOverview = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("managedNotificationConfigurationArn") is not None:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        out["managed_notification_configuration_arn"] = ""
    if data.get("relatedAccount") is not None:
        out["related_account"] = data["relatedAccount"]
    else:
        out["related_account"] = ""
    if data.get("creationTime") is not None:
        import capo_notifications.types.creation_time

        out["creation_time"] = capo_notifications.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("childEvent") is not None:
        import capo_notifications.types.managed_notification_child_event_summary

        out["child_event"] = (
            capo_notifications.types.managed_notification_child_event_summary.deserialize_json(
                data["childEvent"]
            )
        )
    else:
        raise DeserializationError(
            "ManagedNotificationChildEventOverview.child_event required"
        )
    if data.get("aggregateManagedNotificationEventArn") is not None:
        out["aggregate_managed_notification_event_arn"] = data[
            "aggregateManagedNotificationEventArn"
        ]
    else:
        out["aggregate_managed_notification_event_arn"] = ""
    if data.get("organizationalUnitId") is not None:
        out["organizational_unit_id"] = data["organizationalUnitId"]
    return out
