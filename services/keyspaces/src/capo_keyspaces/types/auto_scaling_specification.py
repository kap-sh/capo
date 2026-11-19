"""Generated from Smithy shape ``com.amazonaws.keyspaces#AutoScalingSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.auto_scaling_settings


class AutoScalingSpecification(TypedDict, closed=True):
    write_capacity_auto_scaling: NotRequired[
        "capo_keyspaces.types.auto_scaling_settings.AutoScalingSettings"
    ]
    """<p>The auto scaling settings for the table's write capacity.</p>"""
    read_capacity_auto_scaling: NotRequired[
        "capo_keyspaces.types.auto_scaling_settings.AutoScalingSettings"
    ]
    """<p>The auto scaling settings for the table's read capacity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingSpecification) -> dict:
    out: dict = {}
    if "write_capacity_auto_scaling" in value:
        import capo_keyspaces.types.auto_scaling_settings

        out["writeCapacityAutoScaling"] = (
            capo_keyspaces.types.auto_scaling_settings.serialize_aws_json_1_0(
                value["write_capacity_auto_scaling"]
            )
        )
    if "read_capacity_auto_scaling" in value:
        import capo_keyspaces.types.auto_scaling_settings

        out["readCapacityAutoScaling"] = (
            capo_keyspaces.types.auto_scaling_settings.serialize_aws_json_1_0(
                value["read_capacity_auto_scaling"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingSpecification:
    out: AutoScalingSpecification = {}  # type: ignore[typeddict-item]
    if data.get("writeCapacityAutoScaling") is not None:
        import capo_keyspaces.types.auto_scaling_settings

        out["write_capacity_auto_scaling"] = (
            capo_keyspaces.types.auto_scaling_settings.deserialize_aws_json_1_0(
                data["writeCapacityAutoScaling"]
            )
        )
    if data.get("readCapacityAutoScaling") is not None:
        import capo_keyspaces.types.auto_scaling_settings

        out["read_capacity_auto_scaling"] = (
            capo_keyspaces.types.auto_scaling_settings.deserialize_aws_json_1_0(
                data["readCapacityAutoScaling"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoScalingSpecification) -> dict:
    out: dict = {}
    if "write_capacity_auto_scaling" in value:
        import capo_keyspaces.types.auto_scaling_settings

        out["writeCapacityAutoScaling"] = (
            capo_keyspaces.types.auto_scaling_settings.serialize_cbor(
                value["write_capacity_auto_scaling"]
            )
        )
    if "read_capacity_auto_scaling" in value:
        import capo_keyspaces.types.auto_scaling_settings

        out["readCapacityAutoScaling"] = (
            capo_keyspaces.types.auto_scaling_settings.serialize_cbor(
                value["read_capacity_auto_scaling"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AutoScalingSpecification:
    out: AutoScalingSpecification = {}  # type: ignore[typeddict-item]
    if data.get("writeCapacityAutoScaling") is not None:
        import capo_keyspaces.types.auto_scaling_settings

        out["write_capacity_auto_scaling"] = (
            capo_keyspaces.types.auto_scaling_settings.deserialize_cbor(
                data["writeCapacityAutoScaling"]
            )
        )
    if data.get("readCapacityAutoScaling") is not None:
        import capo_keyspaces.types.auto_scaling_settings

        out["read_capacity_auto_scaling"] = (
            capo_keyspaces.types.auto_scaling_settings.deserialize_cbor(
                data["readCapacityAutoScaling"]
            )
        )
    return out
