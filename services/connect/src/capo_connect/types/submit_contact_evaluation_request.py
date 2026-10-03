"""Generated from Smithy shape ``com.amazonaws.connect#SubmitContactEvaluationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_answers_input_map
    import capo_connect.types.evaluation_notes_map
    import capo_connect.types.evaluator_user_union
    import capo_connect.types.instance_id
    import capo_connect.types.resource_id


class SubmitContactEvaluationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    evaluation_id: "capo_connect.types.resource_id.ResourceId"
    """<p>A unique identifier for the contact evaluation.</p>"""
    answers: NotRequired[
        "capo_connect.types.evaluation_answers_input_map.EvaluationAnswersInputMap"
    ]
    """<p>A map of question identifiers to answer value.</p>"""
    notes: NotRequired["capo_connect.types.evaluation_notes_map.EvaluationNotesMap"]
    """<p>A map of question identifiers to note value.</p>"""
    submitted_by: NotRequired[
        "capo_connect.types.evaluator_user_union.EvaluatorUserUnion"
    ]
    """<p>The ID of the user who submitted the contact evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmitContactEvaluationRequest) -> dict:
    out: dict = {}
    if "answers" in value:
        import capo_connect.types.evaluation_answers_input_map

        out["Answers"] = capo_connect.types.evaluation_answers_input_map.serialize_json(
            value["answers"]
        )
    if "notes" in value:
        import capo_connect.types.evaluation_notes_map

        out["Notes"] = capo_connect.types.evaluation_notes_map.serialize_json(
            value["notes"]
        )
    if "submitted_by" in value:
        import capo_connect.types.evaluator_user_union

        out["SubmittedBy"] = capo_connect.types.evaluator_user_union.serialize_json(
            value["submitted_by"]
        )
    return out


def deserialize_json(data: dict) -> SubmitContactEvaluationRequest:
    out: SubmitContactEvaluationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Answers") is not None:
        import capo_connect.types.evaluation_answers_input_map

        out["answers"] = (
            capo_connect.types.evaluation_answers_input_map.deserialize_json(
                data["Answers"]
            )
        )
    if data.get("Notes") is not None:
        import capo_connect.types.evaluation_notes_map

        out["notes"] = capo_connect.types.evaluation_notes_map.deserialize_json(
            data["Notes"]
        )
    if data.get("SubmittedBy") is not None:
        import capo_connect.types.evaluator_user_union

        out["submitted_by"] = capo_connect.types.evaluator_user_union.deserialize_json(
            data["SubmittedBy"]
        )
    return out
