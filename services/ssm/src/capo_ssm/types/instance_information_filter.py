"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceInformationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_information_filter_key
    import capo_ssm.types.instance_information_filter_value_set


class InstanceInformationFilter(TypedDict, closed=True):
    key: "capo_ssm.types.instance_information_filter_key.InstanceInformationFilterKey"
    """<p>The name of the filter. </p>"""
    value_set: "capo_ssm.types.instance_information_filter_value_set.InstanceInformationFilterValueSet"
    """<p>The filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInformationFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.instance_information_filter_key

    out["key"] = capo_ssm.types.instance_information_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    import capo_ssm.types.instance_information_filter_value_set

    out["valueSet"] = (
        capo_ssm.types.instance_information_filter_value_set.serialize_aws_json_1_1(
            value["value_set"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceInformationFilter:
    out: InstanceInformationFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        import capo_ssm.types.instance_information_filter_key

        out["key"] = (
            capo_ssm.types.instance_information_filter_key.deserialize_aws_json_1_1(
                data["key"]
            )
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.instance_information_filter_key.InstanceInformationFilterKey",
            "",
        )
    if data.get("valueSet") is not None:
        import capo_ssm.types.instance_information_filter_value_set

        out["value_set"] = (
            capo_ssm.types.instance_information_filter_value_set.deserialize_aws_json_1_1(
                data["valueSet"]
            )
        )
    else:
        out["value_set"] = []
    return out
