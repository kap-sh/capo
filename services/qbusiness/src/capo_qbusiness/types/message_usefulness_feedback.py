"""Generated from Smithy shape ``com.amazonaws.qbusiness#MessageUsefulnessFeedback``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.message_usefulness
    import capo_qbusiness.types.message_usefulness_comment
    import capo_qbusiness.types.message_usefulness_reason
    import capo_qbusiness.types.timestamp


class MessageUsefulnessFeedback(TypedDict, closed=True):
    usefulness: "capo_qbusiness.types.message_usefulness.MessageUsefulness"
    """<p>The usefulness value assigned by an end user to a message.</p>"""
    reason: NotRequired[
        "capo_qbusiness.types.message_usefulness_reason.MessageUsefulnessReason"
    ]
    """<p>The reason for a usefulness rating.</p>"""
    comment: NotRequired[
        "capo_qbusiness.types.message_usefulness_comment.MessageUsefulnessComment"
    ]
    """<p>A comment given by an end user on the usefulness of an AI-generated chat message.</p>"""
    submitted_at: "capo_qbusiness.types.timestamp.Timestamp"
    """<p>The timestamp for when the feedback was submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageUsefulnessFeedback) -> dict:
    out: dict = {}
    import capo_qbusiness.types.message_usefulness

    out["usefulness"] = capo_qbusiness.types.message_usefulness.serialize_json(
        value["usefulness"]
    )
    if "reason" in value:
        import capo_qbusiness.types.message_usefulness_reason

        out["reason"] = capo_qbusiness.types.message_usefulness_reason.serialize_json(
            value["reason"]
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    import capo_qbusiness.types.timestamp

    out["submittedAt"] = capo_qbusiness.types.timestamp.serialize_json(
        value["submitted_at"]
    )
    return out


def deserialize_json(data: dict) -> MessageUsefulnessFeedback:
    out: MessageUsefulnessFeedback = {}  # type: ignore[typeddict-item]
    if data.get("usefulness") is not None:
        import capo_qbusiness.types.message_usefulness

        out["usefulness"] = capo_qbusiness.types.message_usefulness.deserialize_json(
            data["usefulness"]
        )
    else:
        import typing

        out["usefulness"] = typing.cast(
            "capo_qbusiness.types.message_usefulness.MessageUsefulness", ""
        )
    if data.get("reason") is not None:
        import capo_qbusiness.types.message_usefulness_reason

        out["reason"] = capo_qbusiness.types.message_usefulness_reason.deserialize_json(
            data["reason"]
        )
    if data.get("comment") is not None:
        out["comment"] = data["comment"]
    if data.get("submittedAt") is not None:
        import capo_qbusiness.types.timestamp

        out["submitted_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["submittedAt"]
        )
    else:
        import datetime

        out["submitted_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
