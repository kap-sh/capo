"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSearchMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.auto_evaluation_status
    import capo_connect.types.boolean
    import capo_connect.types.contact_id
    import capo_connect.types.contact_participant_role
    import capo_connect.types.evaluation_acknowledger_comment_string
    import capo_connect.types.evaluation_score_percentage
    import capo_connect.types.integer
    import capo_connect.types.performance_category_name
    import capo_connect.types.resource_id
    import capo_connect.types.timestamp


class EvaluationSearchMetadata(TypedDict, closed=True):
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    evaluator_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the person who evaluated the contact.</p>"""
    contact_agent_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The unique ID of the agent who handled the contact.</p>"""
    calibration_session_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The calibration session ID that this evaluation belongs to.</p>"""
    score_percentage: (
        "capo_connect.types.evaluation_score_percentage.EvaluationScorePercentage"
    )
    """<p>The total evaluation score expressed as a percentage.</p>"""
    score_automatic_fail: "capo_connect.types.boolean.Boolean"
    """<p>The flag that marks the item as automatic fail. If the item or a child item gets an automatic fail answer, this flag is true.</p>"""
    score_not_applicable: "capo_connect.types.boolean.Boolean"
    """<p>The flag to mark the item as not applicable for scoring.</p>"""
    auto_evaluation_enabled: "capo_connect.types.boolean.Boolean"
    """<p>Whether auto-evaluation is enabled.</p>"""
    auto_evaluation_status: NotRequired[
        "capo_connect.types.auto_evaluation_status.AutoEvaluationStatus"
    ]
    """<p>The status of the contact auto evaluation. </p>"""
    acknowledged_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>When the evaluation was acknowledged by the agent.</p>"""
    acknowledged_by: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The agent who acknowledged the evaluation.</p>"""
    acknowledger_comment: NotRequired[
        "capo_connect.types.evaluation_acknowledger_comment_string.EvaluationAcknowledgerCommentString"
    ]
    """<p>The comment from the agent when they acknowledged the evaluation.</p>"""
    sampling_job_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>Identifier of the sampling job.</p>"""
    review_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>Identifier for the review.</p>"""
    contact_participant_role: NotRequired[
        "capo_connect.types.contact_participant_role.ContactParticipantRole"
    ]
    """<p>Role of a contact participant in the evaluation.</p>"""
    contact_participant_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>Identifier for a contact participant in the evaluation.</p>"""
    earned_points: NotRequired["capo_connect.types.integer.Integer"]
    """<p>The points earned for the evaluation.</p>"""
    max_base_point: NotRequired["capo_connect.types.integer.Integer"]
    """<p>The maximum base points possible for the evaluation.</p>"""
    performance_category: NotRequired[
        "capo_connect.types.performance_category_name.PerformanceCategoryName"
    ]
    """<p>The performance category for the evaluation score.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSearchMetadata) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["EvaluatorArn"] = value["evaluator_arn"]
    if "contact_agent_id" in value:
        out["ContactAgentId"] = value["contact_agent_id"]
    if "calibration_session_id" in value:
        out["CalibrationSessionId"] = value["calibration_session_id"]
    out["ScorePercentage"] = (
        "NaN"
        if value.get("score_percentage", 0) != value.get("score_percentage", 0)
        else "Infinity"
        if value.get("score_percentage", 0) == float("inf")
        else "-Infinity"
        if value.get("score_percentage", 0) == float("-inf")
        else value.get("score_percentage", 0)
    )
    out["ScoreAutomaticFail"] = value.get("score_automatic_fail", False)
    out["ScoreNotApplicable"] = value.get("score_not_applicable", False)
    out["AutoEvaluationEnabled"] = value.get("auto_evaluation_enabled", False)
    if "auto_evaluation_status" in value:
        import capo_connect.types.auto_evaluation_status

        out["AutoEvaluationStatus"] = (
            capo_connect.types.auto_evaluation_status.serialize_json(
                value["auto_evaluation_status"]
            )
        )
    if "acknowledged_time" in value:
        import capo_connect.types.timestamp

        out["AcknowledgedTime"] = capo_connect.types.timestamp.serialize_json(
            value["acknowledged_time"]
        )
    if "acknowledged_by" in value:
        out["AcknowledgedBy"] = value["acknowledged_by"]
    if "acknowledger_comment" in value:
        out["AcknowledgerComment"] = value["acknowledger_comment"]
    if "sampling_job_id" in value:
        out["SamplingJobId"] = value["sampling_job_id"]
    if "review_id" in value:
        out["ReviewId"] = value["review_id"]
    if "contact_participant_role" in value:
        import capo_connect.types.contact_participant_role

        out["ContactParticipantRole"] = (
            capo_connect.types.contact_participant_role.serialize_json(
                value["contact_participant_role"]
            )
        )
    if "contact_participant_id" in value:
        out["ContactParticipantId"] = value["contact_participant_id"]
    if "earned_points" in value:
        out["EarnedPoints"] = value["earned_points"]
    if "max_base_point" in value:
        out["MaxBasePoint"] = value["max_base_point"]
    if "performance_category" in value:
        import capo_connect.types.performance_category_name

        out["PerformanceCategory"] = (
            capo_connect.types.performance_category_name.serialize_json(
                value["performance_category"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationSearchMetadata:
    out: EvaluationSearchMetadata = {}  # type: ignore[typeddict-item]
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
    if data.get("ScorePercentage") is not None:
        out["score_percentage"] = float(data["ScorePercentage"])
    else:
        out["score_percentage"] = 0
    if data.get("ScoreAutomaticFail") is not None:
        out["score_automatic_fail"] = data["ScoreAutomaticFail"]
    else:
        out["score_automatic_fail"] = False
    if data.get("ScoreNotApplicable") is not None:
        out["score_not_applicable"] = data["ScoreNotApplicable"]
    else:
        out["score_not_applicable"] = False
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
    if data.get("AcknowledgedTime") is not None:
        import capo_connect.types.timestamp

        out["acknowledged_time"] = capo_connect.types.timestamp.deserialize_json(
            data["AcknowledgedTime"]
        )
    if data.get("AcknowledgedBy") is not None:
        out["acknowledged_by"] = data["AcknowledgedBy"]
    if data.get("AcknowledgerComment") is not None:
        out["acknowledger_comment"] = data["AcknowledgerComment"]
    if data.get("SamplingJobId") is not None:
        out["sampling_job_id"] = data["SamplingJobId"]
    if data.get("ReviewId") is not None:
        out["review_id"] = data["ReviewId"]
    if data.get("ContactParticipantRole") is not None:
        import capo_connect.types.contact_participant_role

        out["contact_participant_role"] = (
            capo_connect.types.contact_participant_role.deserialize_json(
                data["ContactParticipantRole"]
            )
        )
    if data.get("ContactParticipantId") is not None:
        out["contact_participant_id"] = data["ContactParticipantId"]
    if data.get("EarnedPoints") is not None:
        out["earned_points"] = data["EarnedPoints"]
    if data.get("MaxBasePoint") is not None:
        out["max_base_point"] = data["MaxBasePoint"]
    if data.get("PerformanceCategory") is not None:
        import capo_connect.types.performance_category_name

        out["performance_category"] = (
            capo_connect.types.performance_category_name.deserialize_json(
                data["PerformanceCategory"]
            )
        )
    return out
