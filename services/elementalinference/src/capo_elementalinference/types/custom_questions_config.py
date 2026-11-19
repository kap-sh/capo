"""Generated from Smithy shape ``com.amazonaws.elementalinference#CustomQuestionsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_set_reference


class CustomQuestionsConfig(TypedDict, closed=True):
    shot: NotRequired[
        "capo_elementalinference.types.question_set_reference.QuestionSetReference"
    ]
    """<p>The version of a question set to ask Elemental Inference about each shot.</p>"""
    scene: NotRequired[
        "capo_elementalinference.types.question_set_reference.QuestionSetReference"
    ]
    """<p>The version of a question set to ask Elemental Inference about each scene.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomQuestionsConfig) -> dict:
    out: dict = {}
    if "shot" in value:
        import capo_elementalinference.types.question_set_reference

        out["shot"] = (
            capo_elementalinference.types.question_set_reference.serialize_json(
                value["shot"]
            )
        )
    if "scene" in value:
        import capo_elementalinference.types.question_set_reference

        out["scene"] = (
            capo_elementalinference.types.question_set_reference.serialize_json(
                value["scene"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomQuestionsConfig:
    out: CustomQuestionsConfig = {}  # type: ignore[typeddict-item]
    if data.get("shot") is not None:
        import capo_elementalinference.types.question_set_reference

        out["shot"] = (
            capo_elementalinference.types.question_set_reference.deserialize_json(
                data["shot"]
            )
        )
    if data.get("scene") is not None:
        import capo_elementalinference.types.question_set_reference

        out["scene"] = (
            capo_elementalinference.types.question_set_reference.deserialize_json(
                data["scene"]
            )
        )
    return out
