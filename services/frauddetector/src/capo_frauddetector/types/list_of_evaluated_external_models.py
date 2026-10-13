"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfEvaluatedExternalModels``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.evaluated_external_model

ListOfEvaluatedExternalModels: TypeAlias = list[
    "capo_frauddetector.types.evaluated_external_model.EvaluatedExternalModel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfEvaluatedExternalModels) -> list:
    import capo_frauddetector.types.evaluated_external_model

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.evaluated_external_model.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfEvaluatedExternalModels:
    import capo_frauddetector.types.evaluated_external_model

    out: ListOfEvaluatedExternalModels = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_frauddetector.types.evaluated_external_model.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: ListOfEvaluatedExternalModels) -> list[Any]:
    import capo_frauddetector.types.evaluated_external_model

    return [
        capo_frauddetector.types.evaluated_external_model.redact_sensitive(item)
        for item in value
    ]
