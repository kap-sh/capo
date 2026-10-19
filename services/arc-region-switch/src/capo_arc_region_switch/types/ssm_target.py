"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#SsmTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.ssm_target_key
    import capo_arc_region_switch.types.ssm_target_value_list


class SsmTarget(TypedDict, closed=True):
    key: "capo_arc_region_switch.types.ssm_target_key.SsmTargetKey"
    """<p>The target key, such as <code>tag:Environment</code> or <code>InstanceIds</code>.</p>"""
    values: "capo_arc_region_switch.types.ssm_target_value_list.SsmTargetValueList"
    """<p>The values matched by this target key. Multiple values combine with a logical OR.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SsmTarget) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_arc_region_switch.types.ssm_target_value_list

    out["values"] = (
        capo_arc_region_switch.types.ssm_target_value_list.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SsmTarget:
    out: SsmTarget = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("values") is not None:
        import capo_arc_region_switch.types.ssm_target_value_list

        out["values"] = (
            capo_arc_region_switch.types.ssm_target_value_list.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
