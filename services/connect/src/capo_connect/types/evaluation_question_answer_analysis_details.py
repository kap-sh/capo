"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationQuestionAnswerAnalysisDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.evaluation_contact_lens_answer_analysis_details
    import capo_connect.types.evaluation_gen_ai_answer_analysis_details


class _EvaluationQuestionAnswerAnalysisDetails_GenAI(TypedDict, closed=True):
    GenAI: "capo_connect.types.evaluation_gen_ai_answer_analysis_details.EvaluationGenAIAnswerAnalysisDetails"


class _EvaluationQuestionAnswerAnalysisDetails_ContactLens(TypedDict, closed=True):
    ContactLens: "capo_connect.types.evaluation_contact_lens_answer_analysis_details.EvaluationContactLensAnswerAnalysisDetails"


EvaluationQuestionAnswerAnalysisDetails: TypeAlias = (
    _EvaluationQuestionAnswerAnalysisDetails_GenAI
    | _EvaluationQuestionAnswerAnalysisDetails_ContactLens
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationQuestionAnswerAnalysisDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EvaluationQuestionAnswerAnalysisDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "GenAI" in value:
        import capo_connect.types.evaluation_gen_ai_answer_analysis_details

        return {
            "GenAI": capo_connect.types.evaluation_gen_ai_answer_analysis_details.serialize_json(
                value["GenAI"]
            )
        }
    elif "ContactLens" in value:
        import capo_connect.types.evaluation_contact_lens_answer_analysis_details

        return {
            "ContactLens": capo_connect.types.evaluation_contact_lens_answer_analysis_details.serialize_json(
                value["ContactLens"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationQuestionAnswerAnalysisDetails: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationQuestionAnswerAnalysisDetails:
    if data.get("GenAI") is not None:
        import capo_connect.types.evaluation_gen_ai_answer_analysis_details

        return {
            "GenAI": capo_connect.types.evaluation_gen_ai_answer_analysis_details.deserialize_json(
                data["GenAI"]
            )
        }
    elif data.get("ContactLens") is not None:
        import capo_connect.types.evaluation_contact_lens_answer_analysis_details

        return {
            "ContactLens": capo_connect.types.evaluation_contact_lens_answer_analysis_details.deserialize_json(
                data["ContactLens"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "EvaluationQuestionAnswerAnalysisDetails: no recognized variant key"
        )
