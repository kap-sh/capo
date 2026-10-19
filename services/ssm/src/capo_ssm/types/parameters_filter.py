"""Generated from Smithy shape ``com.amazonaws.ssm#ParametersFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.parameters_filter_key
    import capo_ssm.types.parameters_filter_value_list


class ParametersFilter(TypedDict, closed=True):
    key: "capo_ssm.types.parameters_filter_key.ParametersFilterKey"
    """<p>The name of the filter.</p>"""
    values: "capo_ssm.types.parameters_filter_value_list.ParametersFilterValueList"
    """<p>The filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParametersFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.parameters_filter_key

    out["Key"] = capo_ssm.types.parameters_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    import capo_ssm.types.parameters_filter_value_list

    out["Values"] = capo_ssm.types.parameters_filter_value_list.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParametersFilter:
    out: ParametersFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_ssm.types.parameters_filter_key

        out["key"] = capo_ssm.types.parameters_filter_key.deserialize_aws_json_1_1(
            data["Key"]
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.parameters_filter_key.ParametersFilterKey", ""
        )
    if data.get("Values") is not None:
        import capo_ssm.types.parameters_filter_value_list

        out["values"] = (
            capo_ssm.types.parameters_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
