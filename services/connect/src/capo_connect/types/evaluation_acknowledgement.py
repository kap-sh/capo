"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAcknowledgement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.evaluation_acknowledger_comment_string
    import capo_connect.types.timestamp


class EvaluationAcknowledgement(TypedDict, closed=True):
    acknowledged_time: "capo_connect.types.timestamp.Timestamp"
    """<p>When the agent acknowledged the evaluation.</p>"""
    acknowledged_by: "capo_connect.types.arn.ARN"
    """<p>The agent who acknowledged the evaluation.</p>"""
    acknowledger_comment: NotRequired[
        "capo_connect.types.evaluation_acknowledger_comment_string.EvaluationAcknowledgerCommentString"
    ]
    """<p>A comment from the agent when they confirmed they acknowledged the evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAcknowledgement) -> dict:
    out: dict = {}
    import capo_connect.types.timestamp

    out["AcknowledgedTime"] = capo_connect.types.timestamp.serialize_json(
        value["acknowledged_time"]
    )
    out["AcknowledgedBy"] = value["acknowledged_by"]
    if "acknowledger_comment" in value:
        out["AcknowledgerComment"] = value["acknowledger_comment"]
    return out


def deserialize_json(data: dict) -> EvaluationAcknowledgement:
    out: EvaluationAcknowledgement = {}  # type: ignore[typeddict-item]
    if data.get("AcknowledgedTime") is not None:
        import capo_connect.types.timestamp

        out["acknowledged_time"] = capo_connect.types.timestamp.deserialize_json(
            data["AcknowledgedTime"]
        )
    else:
        import datetime

        out["acknowledged_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("AcknowledgedBy") is not None:
        out["acknowledged_by"] = data["AcknowledgedBy"]
    else:
        out["acknowledged_by"] = ""
    if data.get("AcknowledgerComment") is not None:
        out["acknowledger_comment"] = data["AcknowledgerComment"]
    return out
