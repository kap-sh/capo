"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_filter_key
    import capo_ssm.types.automation_execution_filter_value_list


class AutomationExecutionFilter(TypedDict, closed=True):
    key: "capo_ssm.types.automation_execution_filter_key.AutomationExecutionFilterKey"
    """<p>One or more keys to limit the results.</p>"""
    values: "capo_ssm.types.automation_execution_filter_value_list.AutomationExecutionFilterValueList"
    """<p>The values used to limit the execution information associated with the filter's key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.automation_execution_filter_key

    out["Key"] = capo_ssm.types.automation_execution_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    import capo_ssm.types.automation_execution_filter_value_list

    out["Values"] = (
        capo_ssm.types.automation_execution_filter_value_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationExecutionFilter:
    out: AutomationExecutionFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_ssm.types.automation_execution_filter_key

        out["key"] = (
            capo_ssm.types.automation_execution_filter_key.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.automation_execution_filter_key.AutomationExecutionFilterKey",
            "",
        )
    if data.get("Values") is not None:
        import capo_ssm.types.automation_execution_filter_value_list

        out["values"] = (
            capo_ssm.types.automation_execution_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
