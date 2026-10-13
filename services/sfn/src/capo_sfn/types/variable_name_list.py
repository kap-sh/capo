"""Generated from Smithy shape ``com.amazonaws.sfn#VariableNameList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_sfn.types.variable_name

VariableNameList: TypeAlias = list["capo_sfn.types.variable_name.VariableName"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VariableNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> VariableNameList:
    return [item for item in data if item is not None]


def redact_sensitive(value: VariableNameList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
