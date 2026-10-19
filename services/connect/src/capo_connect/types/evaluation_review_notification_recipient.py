"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewNotificationRecipient``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_review_notification_recipient_type
    import capo_connect.types.evaluation_review_notification_recipient_value


class EvaluationReviewNotificationRecipient(TypedDict, closed=True):
    type: "capo_connect.types.evaluation_review_notification_recipient_type.EvaluationReviewNotificationRecipientType"
    """<p>The type of notification recipient.</p>"""
    value: "capo_connect.types.evaluation_review_notification_recipient_value.EvaluationReviewNotificationRecipientValue"
    """<p>The value associated with the notification recipient type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewNotificationRecipient) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_review_notification_recipient_type

    out["Type"] = (
        capo_connect.types.evaluation_review_notification_recipient_type.serialize_json(
            value["type"]
        )
    )
    import capo_connect.types.evaluation_review_notification_recipient_value

    out["Value"] = (
        capo_connect.types.evaluation_review_notification_recipient_value.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationReviewNotificationRecipient:
    out: EvaluationReviewNotificationRecipient = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_connect.types.evaluation_review_notification_recipient_type

        out["type"] = (
            capo_connect.types.evaluation_review_notification_recipient_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_connect.types.evaluation_review_notification_recipient_type.EvaluationReviewNotificationRecipientType",
            "",
        )
    if data.get("Value") is not None:
        import capo_connect.types.evaluation_review_notification_recipient_value

        out["value"] = (
            capo_connect.types.evaluation_review_notification_recipient_value.deserialize_json(
                data["Value"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationReviewNotificationRecipient.value required"
        )
    return out
