"""Generated from Smithy shape ``com.amazonaws.devopsguru#NotificationFilterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.insight_severities
    import capo_devops_guru.types.notification_message_types


class NotificationFilterConfig(TypedDict, closed=True):
    severities: NotRequired[
        "capo_devops_guru.types.insight_severities.InsightSeverities"
    ]
    """<p> The severity levels that you want to receive notifications for. For example, you can choose to receive notifications only for insights with <code>HIGH</code> and <code>MEDIUM</code> severity levels. For more information, see <a href="https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities">Understanding insight severities</a>. </p>"""
    message_types: NotRequired[
        "capo_devops_guru.types.notification_message_types.NotificationMessageTypes"
    ]
    """<p> The events that you want to receive notifications for. For example, you can choose to receive notifications only when the severity level is upgraded or a new insight is created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationFilterConfig) -> dict:
    out: dict = {}
    if "severities" in value:
        import capo_devops_guru.types.insight_severities

        out["Severities"] = capo_devops_guru.types.insight_severities.serialize_json(
            value["severities"]
        )
    if "message_types" in value:
        import capo_devops_guru.types.notification_message_types

        out["MessageTypes"] = (
            capo_devops_guru.types.notification_message_types.serialize_json(
                value["message_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotificationFilterConfig:
    out: NotificationFilterConfig = {}  # type: ignore[typeddict-item]
    if data.get("Severities") is not None:
        import capo_devops_guru.types.insight_severities

        out["severities"] = capo_devops_guru.types.insight_severities.deserialize_json(
            data["Severities"]
        )
    if data.get("MessageTypes") is not None:
        import capo_devops_guru.types.notification_message_types

        out["message_types"] = (
            capo_devops_guru.types.notification_message_types.deserialize_json(
                data["MessageTypes"]
            )
        )
    return out
