"""Generated from Smithy shape ``com.amazonaws.frauddetector#TrainingDataSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.label_schema
    import capo_frauddetector.types.list_of_strings


class TrainingDataSchema(TypedDict, closed=True):
    model_variables: "capo_frauddetector.types.list_of_strings.ListOfStrings"
    """<p>The training data schema variables.</p>"""
    label_schema: NotRequired["capo_frauddetector.types.label_schema.LabelSchema"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingDataSchema) -> dict:
    out: dict = {}
    import capo_frauddetector.types.list_of_strings

    out["modelVariables"] = (
        capo_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
            value["model_variables"]
        )
    )
    if "label_schema" in value:
        import capo_frauddetector.types.label_schema

        out["labelSchema"] = (
            capo_frauddetector.types.label_schema.serialize_aws_json_1_1(
                value["label_schema"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingDataSchema:
    out: TrainingDataSchema = {}  # type: ignore[typeddict-item]
    if data.get("modelVariables") is not None:
        import capo_frauddetector.types.list_of_strings

        out["model_variables"] = (
            capo_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["modelVariables"]
            )
        )
    else:
        out["model_variables"] = []
    if data.get("labelSchema") is not None:
        import capo_frauddetector.types.label_schema

        out["label_schema"] = (
            capo_frauddetector.types.label_schema.deserialize_aws_json_1_1(
                data["labelSchema"]
            )
        )
    return out
