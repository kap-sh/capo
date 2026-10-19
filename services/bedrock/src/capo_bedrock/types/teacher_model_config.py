"""Generated from Smithy shape ``com.amazonaws.bedrock#TeacherModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.teacher_model_identifier


class TeacherModelConfig(TypedDict, closed=True):
    teacher_model_identifier: (
        "capo_bedrock.types.teacher_model_identifier.TeacherModelIdentifier"
    )
    """<p>The identifier of the teacher model.</p>"""
    max_response_length_for_inference: NotRequired["int"]
    """<p>The maximum number of tokens requested when the customization job invokes the teacher model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TeacherModelConfig) -> dict:
    out: dict = {}
    out["teacherModelIdentifier"] = value["teacher_model_identifier"]
    if "max_response_length_for_inference" in value:
        out["maxResponseLengthForInference"] = value[
            "max_response_length_for_inference"
        ]
    return out


def deserialize_json(data: dict) -> TeacherModelConfig:
    out: TeacherModelConfig = {}  # type: ignore[typeddict-item]
    if data.get("teacherModelIdentifier") is not None:
        out["teacher_model_identifier"] = data["teacherModelIdentifier"]
    else:
        out["teacher_model_identifier"] = ""
    if data.get("maxResponseLengthForInference") is not None:
        out["max_response_length_for_inference"] = data["maxResponseLengthForInference"]
    return out
