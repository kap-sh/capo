"""Generated from Smithy shape ``com.amazonaws.securitylake#NotificationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securitylake.errors import DeserializationError, SerializationError
from capo_securitylake.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securitylake.types.https_notification_configuration
    import capo_securitylake.types.sqs_notification_configuration


class _NotificationConfiguration_sqsNotificationConfiguration(TypedDict, closed=True):
    sqsNotificationConfiguration: "capo_securitylake.types.sqs_notification_configuration.SqsNotificationConfiguration"


class _NotificationConfiguration_httpsNotificationConfiguration(TypedDict, closed=True):
    httpsNotificationConfiguration: "capo_securitylake.types.https_notification_configuration.HttpsNotificationConfiguration"


NotificationConfiguration: TypeAlias = (
    _NotificationConfiguration_sqsNotificationConfiguration
    | _NotificationConfiguration_httpsNotificationConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"NotificationConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "sqsNotificationConfiguration" in value:
        import capo_securitylake.types.sqs_notification_configuration

        return {
            "sqsNotificationConfiguration": capo_securitylake.types.sqs_notification_configuration.serialize_json(
                value["sqsNotificationConfiguration"]
            )
        }
    elif "httpsNotificationConfiguration" in value:
        import capo_securitylake.types.https_notification_configuration

        return {
            "httpsNotificationConfiguration": capo_securitylake.types.https_notification_configuration.serialize_json(
                value["httpsNotificationConfiguration"]
            )
        }
    else:
        raise SerializationError("NotificationConfiguration: no variant present")


def deserialize_json(data: dict) -> NotificationConfiguration:
    if data.get("sqsNotificationConfiguration") is not None:
        import capo_securitylake.types.sqs_notification_configuration

        return {
            "sqsNotificationConfiguration": capo_securitylake.types.sqs_notification_configuration.deserialize_json(
                data["sqsNotificationConfiguration"]
            )
        }
    elif data.get("httpsNotificationConfiguration") is not None:
        import capo_securitylake.types.https_notification_configuration

        return {
            "httpsNotificationConfiguration": capo_securitylake.types.https_notification_configuration.deserialize_json(
                data["httpsNotificationConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "NotificationConfiguration: no recognized variant key"
        )
