"""Generated from Smithy shape ``com.amazonaws.ssm#NodeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.node_filter_key
    import capo_ssm.types.node_filter_operator_type
    import capo_ssm.types.node_filter_value_list


class NodeFilter(TypedDict, closed=True):
    key: "capo_ssm.types.node_filter_key.NodeFilterKey"
    """<p>The name of the filter.</p>"""
    values: "capo_ssm.types.node_filter_value_list.NodeFilterValueList"
    """<p>A filter value supported by the specified key. For example, for the key <code>PlatformType</code>, supported values include <code>Linux</code> and <code>Windows</code>.</p>"""
    type: NotRequired["capo_ssm.types.node_filter_operator_type.NodeFilterOperatorType"]
    """<p>The type of filter operator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.node_filter_key

    out["Key"] = capo_ssm.types.node_filter_key.serialize_aws_json_1_1(value["key"])
    import capo_ssm.types.node_filter_value_list

    out["Values"] = capo_ssm.types.node_filter_value_list.serialize_aws_json_1_1(
        value["values"]
    )
    if "type" in value:
        import capo_ssm.types.node_filter_operator_type

        out["Type"] = capo_ssm.types.node_filter_operator_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NodeFilter:
    out: NodeFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_ssm.types.node_filter_key

        out["key"] = capo_ssm.types.node_filter_key.deserialize_aws_json_1_1(
            data["Key"]
        )
    else:
        import typing

        out["key"] = typing.cast("capo_ssm.types.node_filter_key.NodeFilterKey", "")
    if data.get("Values") is not None:
        import capo_ssm.types.node_filter_value_list

        out["values"] = capo_ssm.types.node_filter_value_list.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        out["values"] = []
    if data.get("Type") is not None:
        import capo_ssm.types.node_filter_operator_type

        out["type"] = capo_ssm.types.node_filter_operator_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
