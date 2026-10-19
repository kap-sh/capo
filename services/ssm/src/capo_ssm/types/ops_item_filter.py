"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_filter_key
    import capo_ssm.types.ops_item_filter_operator
    import capo_ssm.types.ops_item_filter_values


class OpsItemFilter(TypedDict, closed=True):
    key: "capo_ssm.types.ops_item_filter_key.OpsItemFilterKey"
    """<p>The name of the filter.</p>"""
    values: "capo_ssm.types.ops_item_filter_values.OpsItemFilterValues"
    """<p>The filter value.</p>"""
    operator: "capo_ssm.types.ops_item_filter_operator.OpsItemFilterOperator"
    """<p>The operator used by the filter call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.ops_item_filter_key

    out["Key"] = capo_ssm.types.ops_item_filter_key.serialize_aws_json_1_1(value["key"])
    import capo_ssm.types.ops_item_filter_values

    out["Values"] = capo_ssm.types.ops_item_filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    import capo_ssm.types.ops_item_filter_operator

    out["Operator"] = capo_ssm.types.ops_item_filter_operator.serialize_aws_json_1_1(
        value["operator"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemFilter:
    out: OpsItemFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_ssm.types.ops_item_filter_key

        out["key"] = capo_ssm.types.ops_item_filter_key.deserialize_aws_json_1_1(
            data["Key"]
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.ops_item_filter_key.OpsItemFilterKey", ""
        )
    if data.get("Values") is not None:
        import capo_ssm.types.ops_item_filter_values

        out["values"] = capo_ssm.types.ops_item_filter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        out["values"] = []
    if data.get("Operator") is not None:
        import capo_ssm.types.ops_item_filter_operator

        out["operator"] = (
            capo_ssm.types.ops_item_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_ssm.types.ops_item_filter_operator.OpsItemFilterOperator", ""
        )
    return out
