"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EvaluationErrorList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.evaluation_error_item

EvaluationErrorList: TypeAlias = list[
    "capo_verifiedpermissions.types.evaluation_error_item.EvaluationErrorItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationErrorList) -> list:
    import capo_verifiedpermissions.types.evaluation_error_item

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.evaluation_error_item.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EvaluationErrorList:
    import capo_verifiedpermissions.types.evaluation_error_item

    out: EvaluationErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.evaluation_error_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: EvaluationErrorList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
