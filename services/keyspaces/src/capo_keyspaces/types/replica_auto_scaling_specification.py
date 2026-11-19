"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicaAutoScalingSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.auto_scaling_specification
    import capo_keyspaces.types.region


class ReplicaAutoScalingSpecification(TypedDict, closed=True):
    region: NotRequired["capo_keyspaces.types.region.region"]
    """<p>The Amazon Web Services Region.</p>"""
    auto_scaling_specification: NotRequired[
        "capo_keyspaces.types.auto_scaling_specification.AutoScalingSpecification"
    ]
    """<p>The auto scaling settings for a multi-Region table in the specified Amazon Web Services Region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicaAutoScalingSpecification) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "auto_scaling_specification" in value:
        import capo_keyspaces.types.auto_scaling_specification

        out["autoScalingSpecification"] = (
            capo_keyspaces.types.auto_scaling_specification.serialize_aws_json_1_0(
                value["auto_scaling_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicaAutoScalingSpecification:
    out: ReplicaAutoScalingSpecification = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("autoScalingSpecification") is not None:
        import capo_keyspaces.types.auto_scaling_specification

        out["auto_scaling_specification"] = (
            capo_keyspaces.types.auto_scaling_specification.deserialize_aws_json_1_0(
                data["autoScalingSpecification"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReplicaAutoScalingSpecification) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "auto_scaling_specification" in value:
        import capo_keyspaces.types.auto_scaling_specification

        out["autoScalingSpecification"] = (
            capo_keyspaces.types.auto_scaling_specification.serialize_cbor(
                value["auto_scaling_specification"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ReplicaAutoScalingSpecification:
    out: ReplicaAutoScalingSpecification = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("autoScalingSpecification") is not None:
        import capo_keyspaces.types.auto_scaling_specification

        out["auto_scaling_specification"] = (
            capo_keyspaces.types.auto_scaling_specification.deserialize_cbor(
                data["autoScalingSpecification"]
            )
        )
    return out
