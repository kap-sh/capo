"""Generated from Smithy shape ``com.amazonaws.ssm#OpsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_filter_key
    import capo_ssm.types.ops_filter_operator_type
    import capo_ssm.types.ops_filter_value_list


class OpsFilter(TypedDict, closed=True):
    key: "capo_ssm.types.ops_filter_key.OpsFilterKey"
    """<p>The name of the filter.</p>"""
    values: "capo_ssm.types.ops_filter_value_list.OpsFilterValueList"
    """<p>The filter value.</p>"""
    type: NotRequired["capo_ssm.types.ops_filter_operator_type.OpsFilterOperatorType"]
    """<p>The type of filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_ssm.types.ops_filter_value_list

    out["Values"] = capo_ssm.types.ops_filter_value_list.serialize_aws_json_1_1(
        value["values"]
    )
    if "type" in value:
        import capo_ssm.types.ops_filter_operator_type

        out["Type"] = capo_ssm.types.ops_filter_operator_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsFilter:
    out: OpsFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Values") is not None:
        import capo_ssm.types.ops_filter_value_list

        out["values"] = capo_ssm.types.ops_filter_value_list.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        out["values"] = []
    if data.get("Type") is not None:
        import capo_ssm.types.ops_filter_operator_type

        out["type"] = capo_ssm.types.ops_filter_operator_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
