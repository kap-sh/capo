"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemEventFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_event_filter_key
    import capo_ssm.types.ops_item_event_filter_operator
    import capo_ssm.types.ops_item_event_filter_values


class OpsItemEventFilter(TypedDict, closed=True):
    key: "capo_ssm.types.ops_item_event_filter_key.OpsItemEventFilterKey"
    """<p>The name of the filter key. Currently, the only supported value is <code>OpsItemId</code>.</p>"""
    values: "capo_ssm.types.ops_item_event_filter_values.OpsItemEventFilterValues"
    """<p>The values for the filter, consisting of one or more OpsItem IDs.</p>"""
    operator: "capo_ssm.types.ops_item_event_filter_operator.OpsItemEventFilterOperator"
    """<p>The operator used by the filter call. Currently, the only supported value is <code>Equal</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemEventFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.ops_item_event_filter_key

    out["Key"] = capo_ssm.types.ops_item_event_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    import capo_ssm.types.ops_item_event_filter_values

    out["Values"] = capo_ssm.types.ops_item_event_filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    import capo_ssm.types.ops_item_event_filter_operator

    out["Operator"] = (
        capo_ssm.types.ops_item_event_filter_operator.serialize_aws_json_1_1(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemEventFilter:
    out: OpsItemEventFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_ssm.types.ops_item_event_filter_key

        out["key"] = capo_ssm.types.ops_item_event_filter_key.deserialize_aws_json_1_1(
            data["Key"]
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.ops_item_event_filter_key.OpsItemEventFilterKey", ""
        )
    if data.get("Values") is not None:
        import capo_ssm.types.ops_item_event_filter_values

        out["values"] = (
            capo_ssm.types.ops_item_event_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    if data.get("Operator") is not None:
        import capo_ssm.types.ops_item_event_filter_operator

        out["operator"] = (
            capo_ssm.types.ops_item_event_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_ssm.types.ops_item_event_filter_operator.OpsItemEventFilterOperator",
            "",
        )
    return out
