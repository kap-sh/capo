"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterHistoryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.parameter_history

ParameterHistoryList: TypeAlias = list[
    "capo_ssm.types.parameter_history.ParameterHistory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterHistoryList) -> list:
    import capo_ssm.types.parameter_history

    out: list = []
    for item in value:
        out.append(capo_ssm.types.parameter_history.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterHistoryList:
    import capo_ssm.types.parameter_history

    out: ParameterHistoryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.parameter_history.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: ParameterHistoryList) -> list[Any]:
    import capo_ssm.types.parameter_history

    return [capo_ssm.types.parameter_history.redact_sensitive(item) for item in value]
