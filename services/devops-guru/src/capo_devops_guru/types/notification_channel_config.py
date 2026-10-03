"""Generated from Smithy shape ``com.amazonaws.devopsguru#NotificationChannelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_guru.types.notification_filter_config
    import capo_devops_guru.types.sns_channel_config


class NotificationChannelConfig(TypedDict, closed=True):
    sns: "capo_devops_guru.types.sns_channel_config.SnsChannelConfig"
    """<p> Information about a notification channel configured in DevOps Guru to send notifications when insights are created. </p> <p>If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see <a href="https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html">Permissions for Amazon SNS topics</a>.</p> <p>If you use an Amazon SNS topic that is encrypted by an Amazon Web Services Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see <a href="https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html">Permissions for Amazon Web Services KMS–encrypted Amazon SNS topics</a>.</p>"""
    filters: NotRequired[
        "capo_devops_guru.types.notification_filter_config.NotificationFilterConfig"
    ]
    """<p> The filter configurations for the Amazon SNS notification topic you use with DevOps Guru. If you do not provide filter configurations, the default configurations are to receive notifications for all message types of <code>High</code> or <code>Medium</code> severity. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationChannelConfig) -> dict:
    out: dict = {}
    import capo_devops_guru.types.sns_channel_config

    out["Sns"] = capo_devops_guru.types.sns_channel_config.serialize_json(value["sns"])
    if "filters" in value:
        import capo_devops_guru.types.notification_filter_config

        out["Filters"] = (
            capo_devops_guru.types.notification_filter_config.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotificationChannelConfig:
    out: NotificationChannelConfig = {}  # type: ignore[typeddict-item]
    if data.get("Sns") is not None:
        import capo_devops_guru.types.sns_channel_config

        out["sns"] = capo_devops_guru.types.sns_channel_config.deserialize_json(
            data["Sns"]
        )
    else:
        raise DeserializationError("NotificationChannelConfig.sns required")
    if data.get("Filters") is not None:
        import capo_devops_guru.types.notification_filter_config

        out["filters"] = (
            capo_devops_guru.types.notification_filter_config.deserialize_json(
                data["Filters"]
            )
        )
    return out
