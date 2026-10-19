"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAnswerData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.evaluation_answer_data_numeric_value
    import capo_connect.types.evaluation_answer_data_string_value
    import capo_connect.types.evaluation_answer_data_string_value_list
    import capo_connect.types.iso8601_datetime


class _EvaluationAnswerData_StringValue(TypedDict, closed=True):
    StringValue: "capo_connect.types.evaluation_answer_data_string_value.EvaluationAnswerDataStringValue"


class _EvaluationAnswerData_NumericValue(TypedDict, closed=True):
    NumericValue: "capo_connect.types.evaluation_answer_data_numeric_value.EvaluationAnswerDataNumericValue"


class _EvaluationAnswerData_StringValues(TypedDict, closed=True):
    StringValues: "capo_connect.types.evaluation_answer_data_string_value_list.EvaluationAnswerDataStringValueList"


class _EvaluationAnswerData_DateTimeValue(TypedDict, closed=True):
    DateTimeValue: "capo_connect.types.iso8601_datetime.ISO8601Datetime"


class _EvaluationAnswerData_NotApplicable(TypedDict, closed=True):
    NotApplicable: "capo_connect.types.boolean.Boolean"


EvaluationAnswerData: TypeAlias = (
    _EvaluationAnswerData_StringValue
    | _EvaluationAnswerData_NumericValue
    | _EvaluationAnswerData_StringValues
    | _EvaluationAnswerData_DateTimeValue
    | _EvaluationAnswerData_NotApplicable
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAnswerData) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluationAnswerData: cannot serialize unknown variant {value.name!r}"
        )
    elif "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    elif "NumericValue" in value:
        return {
            "NumericValue": (
                "NaN"
                if value["NumericValue"] != value["NumericValue"]
                else "Infinity"
                if value["NumericValue"] == float("inf")
                else "-Infinity"
                if value["NumericValue"] == float("-inf")
                else value["NumericValue"]
            )
        }
    elif "StringValues" in value:
        import capo_connect.types.evaluation_answer_data_string_value_list

        return {
            "StringValues": capo_connect.types.evaluation_answer_data_string_value_list.serialize_json(
                value["StringValues"]
            )
        }
    elif "DateTimeValue" in value:
        return {"DateTimeValue": value["DateTimeValue"]}
    elif "NotApplicable" in value:
        return {"NotApplicable": value["NotApplicable"]}
    else:
        raise SerializationError("EvaluationAnswerData: no variant present")


def deserialize_json(data: dict) -> EvaluationAnswerData:
    if data.get("StringValue") is not None:
        return {"StringValue": data["StringValue"]}
    elif data.get("NumericValue") is not None:
        return {"NumericValue": float(data["NumericValue"])}
    elif data.get("StringValues") is not None:
        import capo_connect.types.evaluation_answer_data_string_value_list

        return {
            "StringValues": capo_connect.types.evaluation_answer_data_string_value_list.deserialize_json(
                data["StringValues"]
            )
        }
    elif data.get("DateTimeValue") is not None:
        return {"DateTimeValue": data["DateTimeValue"]}
    elif data.get("NotApplicable") is not None:
        return {"NotApplicable": data["NotApplicable"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("EvaluationAnswerData: no recognized variant key")
