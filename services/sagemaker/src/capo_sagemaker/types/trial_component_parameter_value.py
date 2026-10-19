"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentParameterValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.double_parameter_value
    import capo_sagemaker.types.string_parameter_value


class _TrialComponentParameterValue_StringValue(TypedDict, closed=True):
    StringValue: "capo_sagemaker.types.string_parameter_value.StringParameterValue"


class _TrialComponentParameterValue_NumberValue(TypedDict, closed=True):
    NumberValue: "capo_sagemaker.types.double_parameter_value.DoubleParameterValue"


TrialComponentParameterValue: TypeAlias = (
    _TrialComponentParameterValue_StringValue
    | _TrialComponentParameterValue_NumberValue
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentParameterValue) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"TrialComponentParameterValue: cannot serialize unknown variant {value.name!r}"
        )
    elif "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    elif "NumberValue" in value:
        return {
            "NumberValue": (
                "NaN"
                if value["NumberValue"] != value["NumberValue"]
                else "Infinity"
                if value["NumberValue"] == float("inf")
                else "-Infinity"
                if value["NumberValue"] == float("-inf")
                else value["NumberValue"]
            )
        }
    else:
        raise SerializationError("TrialComponentParameterValue: no variant present")


def deserialize_aws_json_1_1(data: dict) -> TrialComponentParameterValue:
    if data.get("StringValue") is not None:
        return {"StringValue": data["StringValue"]}
    elif data.get("NumberValue") is not None:
        return {"NumberValue": float(data["NumberValue"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "TrialComponentParameterValue: no recognized variant key"
        )
