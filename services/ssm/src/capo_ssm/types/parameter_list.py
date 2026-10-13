"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.parameter

ParameterList: TypeAlias = list["capo_ssm.types.parameter.Parameter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterList) -> list:
    import capo_ssm.types.parameter

    out: list = []
    for item in value:
        out.append(capo_ssm.types.parameter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterList:
    import capo_ssm.types.parameter

    out: ParameterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.parameter.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: ParameterList) -> list[Any]:
    import capo_ssm.types.parameter

    return [capo_ssm.types.parameter.redact_sensitive(item) for item in value]
