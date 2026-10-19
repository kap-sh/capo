"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.auto_evaluation_details
    import capo_connect.types.contact_id
    import capo_connect.types.evaluation_acknowledgement
    import capo_connect.types.evaluation_contact_participant
    import capo_connect.types.evaluation_review_metadata
    import capo_connect.types.evaluation_score
    import capo_connect.types.resource_id


class EvaluationMetadata(TypedDict, closed=True):
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    evaluator_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the evaluation.</p>"""
    contact_agent_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The identifier of the agent who performed the contact.</p>"""
    calibration_session_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The calibration session ID that this evaluation belongs to.</p>"""
    score: NotRequired["capo_connect.types.evaluation_score.EvaluationScore"]
    """<p>The overall score of the contact evaluation.</p>"""
    auto_evaluation: NotRequired[
        "capo_connect.types.auto_evaluation_details.AutoEvaluationDetails"
    ]
    """<p>Information related to automated evaluation.</p>"""
    acknowledgement: NotRequired[
        "capo_connect.types.evaluation_acknowledgement.EvaluationAcknowledgement"
    ]
    """<p>Information related to evaluation acknowledgement.</p>"""
    review: NotRequired[
        "capo_connect.types.evaluation_review_metadata.EvaluationReviewMetadata"
    ]
    """<p>Information about reviews of this evaluation.</p>"""
    contact_participant: NotRequired[
        "capo_connect.types.evaluation_contact_participant.EvaluationContactParticipant"
    ]
    """<p>Information about a contact participant in this evaluation.</p>"""
    sampling_job_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>Identifier of the sampling job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationMetadata) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["EvaluatorArn"] = value["evaluator_arn"]
    if "contact_agent_id" in value:
        out["ContactAgentId"] = value["contact_agent_id"]
    if "calibration_session_id" in value:
        out["CalibrationSessionId"] = value["calibration_session_id"]
    if "score" in value:
        import capo_connect.types.evaluation_score

        out["Score"] = capo_connect.types.evaluation_score.serialize_json(
            value["score"]
        )
    if "auto_evaluation" in value:
        import capo_connect.types.auto_evaluation_details

        out["AutoEvaluation"] = (
            capo_connect.types.auto_evaluation_details.serialize_json(
                value["auto_evaluation"]
            )
        )
    if "acknowledgement" in value:
        import capo_connect.types.evaluation_acknowledgement

        out["Acknowledgement"] = (
            capo_connect.types.evaluation_acknowledgement.serialize_json(
                value["acknowledgement"]
            )
        )
    if "review" in value:
        import capo_connect.types.evaluation_review_metadata

        out["Review"] = capo_connect.types.evaluation_review_metadata.serialize_json(
            value["review"]
        )
    if "contact_participant" in value:
        import capo_connect.types.evaluation_contact_participant

        out["ContactParticipant"] = (
            capo_connect.types.evaluation_contact_participant.serialize_json(
                value["contact_participant"]
            )
        )
    if "sampling_job_id" in value:
        out["SamplingJobId"] = value["sampling_job_id"]
    return out


def deserialize_json(data: dict) -> EvaluationMetadata:
    out: EvaluationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        out["contact_id"] = ""
    if data.get("EvaluatorArn") is not None:
        out["evaluator_arn"] = data["EvaluatorArn"]
    else:
        out["evaluator_arn"] = ""
    if data.get("ContactAgentId") is not None:
        out["contact_agent_id"] = data["ContactAgentId"]
    if data.get("CalibrationSessionId") is not None:
        out["calibration_session_id"] = data["CalibrationSessionId"]
    if data.get("Score") is not None:
        import capo_connect.types.evaluation_score

        out["score"] = capo_connect.types.evaluation_score.deserialize_json(
            data["Score"]
        )
    if data.get("AutoEvaluation") is not None:
        import capo_connect.types.auto_evaluation_details

        out["auto_evaluation"] = (
            capo_connect.types.auto_evaluation_details.deserialize_json(
                data["AutoEvaluation"]
            )
        )
    if data.get("Acknowledgement") is not None:
        import capo_connect.types.evaluation_acknowledgement

        out["acknowledgement"] = (
            capo_connect.types.evaluation_acknowledgement.deserialize_json(
                data["Acknowledgement"]
            )
        )
    if data.get("Review") is not None:
        import capo_connect.types.evaluation_review_metadata

        out["review"] = capo_connect.types.evaluation_review_metadata.deserialize_json(
            data["Review"]
        )
    if data.get("ContactParticipant") is not None:
        import capo_connect.types.evaluation_contact_participant

        out["contact_participant"] = (
            capo_connect.types.evaluation_contact_participant.deserialize_json(
                data["ContactParticipant"]
            )
        )
    if data.get("SamplingJobId") is not None:
        out["sampling_job_id"] = data["SamplingJobId"]
    return out
