"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePatchStateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_patch_state_filter_key
    import capo_ssm.types.instance_patch_state_filter_values
    import capo_ssm.types.instance_patch_state_operator_type


class InstancePatchStateFilter(TypedDict, closed=True):
    key: "capo_ssm.types.instance_patch_state_filter_key.InstancePatchStateFilterKey"
    """<p>The key for the filter. Supported values include the following:</p> <ul> <li> <p> <code>InstalledCount</code> </p> </li> <li> <p> <code>InstalledOtherCount</code> </p> </li> <li> <p> <code>InstalledPendingRebootCount</code> </p> </li> <li> <p> <code>InstalledRejectedCount</code> </p> </li> <li> <p> <code>MissingCount</code> </p> </li> <li> <p> <code>FailedCount</code> </p> </li> <li> <p> <code>UnreportedNotApplicableCount</code> </p> </li> <li> <p> <code>NotApplicableCount</code> </p> </li> </ul>"""
    values: "capo_ssm.types.instance_patch_state_filter_values.InstancePatchStateFilterValues"
    """<p>The value for the filter. Must be an integer greater than or equal to 0.</p>"""
    type: "capo_ssm.types.instance_patch_state_operator_type.InstancePatchStateOperatorType"
    """<p>The type of comparison that should be performed for the value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePatchStateFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_ssm.types.instance_patch_state_filter_values

    out["Values"] = (
        capo_ssm.types.instance_patch_state_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    import capo_ssm.types.instance_patch_state_operator_type

    out["Type"] = (
        capo_ssm.types.instance_patch_state_operator_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstancePatchStateFilter:
    out: InstancePatchStateFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Values") is not None:
        import capo_ssm.types.instance_patch_state_filter_values

        out["values"] = (
            capo_ssm.types.instance_patch_state_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    if data.get("Type") is not None:
        import capo_ssm.types.instance_patch_state_operator_type

        out["type"] = (
            capo_ssm.types.instance_patch_state_operator_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_ssm.types.instance_patch_state_operator_type.InstancePatchStateOperatorType",
            "",
        )
    return out
