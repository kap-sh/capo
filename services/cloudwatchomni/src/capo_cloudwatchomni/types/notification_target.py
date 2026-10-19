"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NotificationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.notification_target_metadata
    import capo_cloudwatchomni.types.notification_target_type


class NotificationTarget(TypedDict, closed=True):
    type: "capo_cloudwatchomni.types.notification_target_type.NotificationTargetType"
    """The type of notification target."""
    arn: "capo_cloudwatchomni.types.arn.Arn"
    """The Amazon Resource Name (ARN) of the notification target. For {@code slack} and {@code pagerduty}, an integration ARN as returned by {@code ListIntegrations}."""
    metadata: NotRequired[
        "capo_cloudwatchomni.types.notification_target_metadata.NotificationTargetMetadata"
    ]
    """Additional target-specific metadata."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NotificationTarget) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.notification_target_type

    out["type"] = capo_cloudwatchomni.types.notification_target_type.serialize_cbor(
        value["type"]
    )
    out["arn"] = value["arn"]
    if "metadata" in value:
        import capo_cloudwatchomni.types.notification_target_metadata

        out["metadata"] = (
            capo_cloudwatchomni.types.notification_target_metadata.serialize_cbor(
                value["metadata"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> NotificationTarget:
    out: NotificationTarget = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_cloudwatchomni.types.notification_target_type

        out["type"] = (
            capo_cloudwatchomni.types.notification_target_type.deserialize_cbor(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cloudwatchomni.types.notification_target_type.NotificationTargetType",
            "",
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("metadata") is not None:
        import capo_cloudwatchomni.types.notification_target_metadata

        out["metadata"] = (
            capo_cloudwatchomni.types.notification_target_metadata.deserialize_cbor(
                data["metadata"]
            )
        )
    return out
