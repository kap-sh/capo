"""Generated from Smithy shape ``com.amazonaws.ssm#NodeAggregator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.node_aggregator_list
    import capo_ssm.types.node_aggregator_type
    import capo_ssm.types.node_attribute_name
    import capo_ssm.types.node_type_name


class NodeAggregator(TypedDict, closed=True):
    aggregator_type: "capo_ssm.types.node_aggregator_type.NodeAggregatorType"
    """<p>The aggregator type for limiting a node summary. Currently, only <code>Count</code> is supported.</p>"""
    type_name: "capo_ssm.types.node_type_name.NodeTypeName"
    """<p>The data type name to use for viewing counts of nodes. Currently, only <code>Instance</code> is supported.</p>"""
    attribute_name: "capo_ssm.types.node_attribute_name.NodeAttributeName"
    """<p>The name of a node attribute on which to limit the count of nodes.</p>"""
    aggregators: NotRequired["capo_ssm.types.node_aggregator_list.NodeAggregatorList"]
    """<p>Information about aggregators used to refine a node summary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeAggregator) -> dict:
    out: dict = {}
    import capo_ssm.types.node_aggregator_type

    out["AggregatorType"] = capo_ssm.types.node_aggregator_type.serialize_aws_json_1_1(
        value["aggregator_type"]
    )
    import capo_ssm.types.node_type_name

    out["TypeName"] = capo_ssm.types.node_type_name.serialize_aws_json_1_1(
        value["type_name"]
    )
    import capo_ssm.types.node_attribute_name

    out["AttributeName"] = capo_ssm.types.node_attribute_name.serialize_aws_json_1_1(
        value["attribute_name"]
    )
    if "aggregators" in value:
        import capo_ssm.types.node_aggregator_list

        out["Aggregators"] = capo_ssm.types.node_aggregator_list.serialize_aws_json_1_1(
            value["aggregators"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NodeAggregator:
    out: NodeAggregator = {}  # type: ignore[typeddict-item]
    if data.get("AggregatorType") is not None:
        import capo_ssm.types.node_aggregator_type

        out["aggregator_type"] = (
            capo_ssm.types.node_aggregator_type.deserialize_aws_json_1_1(
                data["AggregatorType"]
            )
        )
    else:
        import typing

        out["aggregator_type"] = typing.cast(
            "capo_ssm.types.node_aggregator_type.NodeAggregatorType", ""
        )
    if data.get("TypeName") is not None:
        import capo_ssm.types.node_type_name

        out["type_name"] = capo_ssm.types.node_type_name.deserialize_aws_json_1_1(
            data["TypeName"]
        )
    else:
        import typing

        out["type_name"] = typing.cast("capo_ssm.types.node_type_name.NodeTypeName", "")
    if data.get("AttributeName") is not None:
        import capo_ssm.types.node_attribute_name

        out["attribute_name"] = (
            capo_ssm.types.node_attribute_name.deserialize_aws_json_1_1(
                data["AttributeName"]
            )
        )
    else:
        import typing

        out["attribute_name"] = typing.cast(
            "capo_ssm.types.node_attribute_name.NodeAttributeName", ""
        )
    if data.get("Aggregators") is not None:
        import capo_ssm.types.node_aggregator_list

        out["aggregators"] = (
            capo_ssm.types.node_aggregator_list.deserialize_aws_json_1_1(
                data["Aggregators"]
            )
        )
    return out
