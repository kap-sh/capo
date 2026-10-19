"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemRelatedItemsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_related_items_filter_key
    import capo_ssm.types.ops_item_related_items_filter_operator
    import capo_ssm.types.ops_item_related_items_filter_values


class OpsItemRelatedItemsFilter(TypedDict, closed=True):
    key: "capo_ssm.types.ops_item_related_items_filter_key.OpsItemRelatedItemsFilterKey"
    """<p>The name of the filter key. Supported values include <code>ResourceUri</code>, <code>ResourceType</code>, or <code>AssociationId</code>.</p>"""
    values: "capo_ssm.types.ops_item_related_items_filter_values.OpsItemRelatedItemsFilterValues"
    """<p>The values for the filter.</p>"""
    operator: "capo_ssm.types.ops_item_related_items_filter_operator.OpsItemRelatedItemsFilterOperator"
    """<p>The operator used by the filter call. The only supported operator is <code>EQUAL</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemRelatedItemsFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.ops_item_related_items_filter_key

    out["Key"] = (
        capo_ssm.types.ops_item_related_items_filter_key.serialize_aws_json_1_1(
            value["key"]
        )
    )
    import capo_ssm.types.ops_item_related_items_filter_values

    out["Values"] = (
        capo_ssm.types.ops_item_related_items_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    import capo_ssm.types.ops_item_related_items_filter_operator

    out["Operator"] = (
        capo_ssm.types.ops_item_related_items_filter_operator.serialize_aws_json_1_1(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemRelatedItemsFilter:
    out: OpsItemRelatedItemsFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_ssm.types.ops_item_related_items_filter_key

        out["key"] = (
            capo_ssm.types.ops_item_related_items_filter_key.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.ops_item_related_items_filter_key.OpsItemRelatedItemsFilterKey",
            "",
        )
    if data.get("Values") is not None:
        import capo_ssm.types.ops_item_related_items_filter_values

        out["values"] = (
            capo_ssm.types.ops_item_related_items_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    if data.get("Operator") is not None:
        import capo_ssm.types.ops_item_related_items_filter_operator

        out["operator"] = (
            capo_ssm.types.ops_item_related_items_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_ssm.types.ops_item_related_items_filter_operator.OpsItemRelatedItemsFilterOperator",
            "",
        )
    return out
