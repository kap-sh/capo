"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationReviewConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_review_notification_recipient_list
    import capo_connect.types.integer


class EvaluationReviewConfiguration(TypedDict, closed=True):
    review_notification_recipients: "capo_connect.types.evaluation_review_notification_recipient_list.EvaluationReviewNotificationRecipientList"
    """<p>List of recipients who should be notified when a review is requested.</p>"""
    eligibility_days: "capo_connect.types.integer.Integer"
    """<p>Number of days during which a request for review can be submitted for evaluations created from this form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationReviewConfiguration) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_review_notification_recipient_list

    out["ReviewNotificationRecipients"] = (
        capo_connect.types.evaluation_review_notification_recipient_list.serialize_json(
            value["review_notification_recipients"]
        )
    )
    out["EligibilityDays"] = value.get("eligibility_days", 0)
    return out


def deserialize_json(data: dict) -> EvaluationReviewConfiguration:
    out: EvaluationReviewConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ReviewNotificationRecipients") is not None:
        import capo_connect.types.evaluation_review_notification_recipient_list

        out["review_notification_recipients"] = (
            capo_connect.types.evaluation_review_notification_recipient_list.deserialize_json(
                data["ReviewNotificationRecipients"]
            )
        )
    else:
        out["review_notification_recipients"] = []
    if data.get("EligibilityDays") is not None:
        out["eligibility_days"] = data["EligibilityDays"]
    else:
        out["eligibility_days"] = 0
    return out
