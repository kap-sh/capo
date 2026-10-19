"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.auto_evaluation_status
    import capo_connect.types.boolean
    import capo_connect.types.evaluation_acknowledgement_summary
    import capo_connect.types.evaluation_contact_participant
    import capo_connect.types.evaluation_form_title
    import capo_connect.types.evaluation_score
    import capo_connect.types.evaluation_status
    import capo_connect.types.evaluation_type
    import capo_connect.types.resource_id
    import capo_connect.types.timestamp


class EvaluationSummary(TypedDict, closed=True):
    evaluation_id: "capo_connect.types.resource_id.ResourceId"
    """<p>A unique identifier for the contact evaluation.</p>"""
    evaluation_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the contact evaluation resource.</p>"""
    evaluation_form_title: (
        "capo_connect.types.evaluation_form_title.EvaluationFormTitle"
    )
    """<p>A title of the evaluation form.</p>"""
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    calibration_session_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The calibration session ID that this evaluation belongs to.</p>"""
    status: "capo_connect.types.evaluation_status.EvaluationStatus"
    """<p>The status of the contact evaluation.</p>"""
    auto_evaluation_enabled: "capo_connect.types.boolean.Boolean"
    """<p>Whether automated evaluation is enabled.</p>"""
    auto_evaluation_status: NotRequired[
        "capo_connect.types.auto_evaluation_status.AutoEvaluationStatus"
    ]
    """<p>The status of the contact auto evaluation. </p>"""
    evaluator_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the evaluation.</p>"""
    score: NotRequired["capo_connect.types.evaluation_score.EvaluationScore"]
    """<p>The overall score of the contact evaluation.</p>"""
    acknowledgement: NotRequired[
        "capo_connect.types.evaluation_acknowledgement_summary.EvaluationAcknowledgementSummary"
    ]
    """<p>Information related to evaluation acknowledgement.</p>"""
    evaluation_type: NotRequired["capo_connect.types.evaluation_type.EvaluationType"]
    """<p>Type of the evaluation. </p>"""
    created_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation was created.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation was last updated.</p>"""
    contact_participant: NotRequired[
        "capo_connect.types.evaluation_contact_participant.EvaluationContactParticipant"
    ]
    """<p>Information about a contact participant in the evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSummary) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    out["EvaluationArn"] = value["evaluation_arn"]
    out["EvaluationFormTitle"] = value["evaluation_form_title"]
    out["EvaluationFormId"] = value["evaluation_form_id"]
    if "calibration_session_id" in value:
        out["CalibrationSessionId"] = value["calibration_session_id"]
    import capo_connect.types.evaluation_status

    out["Status"] = capo_connect.types.evaluation_status.serialize_json(value["status"])
    out["AutoEvaluationEnabled"] = value.get("auto_evaluation_enabled", False)
    if "auto_evaluation_status" in value:
        import capo_connect.types.auto_evaluation_status

        out["AutoEvaluationStatus"] = (
            capo_connect.types.auto_evaluation_status.serialize_json(
                value["auto_evaluation_status"]
            )
        )
    out["EvaluatorArn"] = value["evaluator_arn"]
    if "score" in value:
        import capo_connect.types.evaluation_score

        out["Score"] = capo_connect.types.evaluation_score.serialize_json(
            value["score"]
        )
    if "acknowledgement" in value:
        import capo_connect.types.evaluation_acknowledgement_summary

        out["Acknowledgement"] = (
            capo_connect.types.evaluation_acknowledgement_summary.serialize_json(
                value["acknowledgement"]
            )
        )
    if "evaluation_type" in value:
        import capo_connect.types.evaluation_type

        out["EvaluationType"] = capo_connect.types.evaluation_type.serialize_json(
            value["evaluation_type"]
        )
    import capo_connect.types.timestamp

    out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import capo_connect.types.timestamp

    out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "contact_participant" in value:
        import capo_connect.types.evaluation_contact_participant

        out["ContactParticipant"] = (
            capo_connect.types.evaluation_contact_participant.serialize_json(
                value["contact_participant"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationSummary:
    out: EvaluationSummary = {}  # type: ignore[typeddict-item]
    if data.get("EvaluationId") is not None:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        out["evaluation_id"] = ""
    if data.get("EvaluationArn") is not None:
        out["evaluation_arn"] = data["EvaluationArn"]
    else:
        out["evaluation_arn"] = ""
    if data.get("EvaluationFormTitle") is not None:
        out["evaluation_form_title"] = data["EvaluationFormTitle"]
    else:
        out["evaluation_form_title"] = ""
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        out["evaluation_form_id"] = ""
    if data.get("CalibrationSessionId") is not None:
        out["calibration_session_id"] = data["CalibrationSessionId"]
    if data.get("Status") is not None:
        import capo_connect.types.evaluation_status

        out["status"] = capo_connect.types.evaluation_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connect.types.evaluation_status.EvaluationStatus", ""
        )
    if data.get("AutoEvaluationEnabled") is not None:
        out["auto_evaluation_enabled"] = data["AutoEvaluationEnabled"]
    else:
        out["auto_evaluation_enabled"] = False
    if data.get("AutoEvaluationStatus") is not None:
        import capo_connect.types.auto_evaluation_status

        out["auto_evaluation_status"] = (
            capo_connect.types.auto_evaluation_status.deserialize_json(
                data["AutoEvaluationStatus"]
            )
        )
    if data.get("EvaluatorArn") is not None:
        out["evaluator_arn"] = data["EvaluatorArn"]
    else:
        out["evaluator_arn"] = ""
    if data.get("Score") is not None:
        import capo_connect.types.evaluation_score

        out["score"] = capo_connect.types.evaluation_score.deserialize_json(
            data["Score"]
        )
    if data.get("Acknowledgement") is not None:
        import capo_connect.types.evaluation_acknowledgement_summary

        out["acknowledgement"] = (
            capo_connect.types.evaluation_acknowledgement_summary.deserialize_json(
                data["Acknowledgement"]
            )
        )
    if data.get("EvaluationType") is not None:
        import capo_connect.types.evaluation_type

        out["evaluation_type"] = capo_connect.types.evaluation_type.deserialize_json(
            data["EvaluationType"]
        )
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ContactParticipant") is not None:
        import capo_connect.types.evaluation_contact_participant

        out["contact_participant"] = (
            capo_connect.types.evaluation_contact_participant.deserialize_json(
                data["ContactParticipant"]
            )
        )
    return out
