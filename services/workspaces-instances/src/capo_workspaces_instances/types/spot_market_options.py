"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#SpotMarketOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_workspaces_instances.types.instance_interruption_behavior_enum
    import capo_workspaces_instances.types.non_negative_integer
    import capo_workspaces_instances.types.spot_instance_type_enum
    import capo_workspaces_instances.types.string64


class SpotMarketOptions(TypedDict, closed=True):
    block_duration_minutes: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Duration of spot instance block reservation.</p>"""
    instance_interruption_behavior: NotRequired[
        "capo_workspaces_instances.types.instance_interruption_behavior_enum.InstanceInterruptionBehaviorEnum"
    ]
    """<p>Specifies behavior when spot instance is interrupted.</p>"""
    max_price: NotRequired["capo_workspaces_instances.types.string64.String64"]
    """<p>Maximum hourly price for spot instance.</p>"""
    spot_instance_type: NotRequired[
        "capo_workspaces_instances.types.spot_instance_type_enum.SpotInstanceTypeEnum"
    ]
    """<p>Defines the type of spot instance request.</p>"""
    valid_until_utc: NotRequired["datetime.datetime"]
    """<p>Timestamp until which spot instance request is valid.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpotMarketOptions) -> dict:
    out: dict = {}
    if "block_duration_minutes" in value:
        out["BlockDurationMinutes"] = value["block_duration_minutes"]
    if "instance_interruption_behavior" in value:
        import capo_workspaces_instances.types.instance_interruption_behavior_enum

        out["InstanceInterruptionBehavior"] = (
            capo_workspaces_instances.types.instance_interruption_behavior_enum.serialize_aws_json_1_0(
                value["instance_interruption_behavior"]
            )
        )
    if "max_price" in value:
        out["MaxPrice"] = value["max_price"]
    if "spot_instance_type" in value:
        import capo_workspaces_instances.types.spot_instance_type_enum

        out["SpotInstanceType"] = (
            capo_workspaces_instances.types.spot_instance_type_enum.serialize_aws_json_1_0(
                value["spot_instance_type"]
            )
        )
    if "valid_until_utc" in value:
        import capo_workspaces_instances.types._prelude.timestamp

        out["ValidUntilUtc"] = (
            capo_workspaces_instances.types._prelude.timestamp.serialize_aws_json_1_0(
                value["valid_until_utc"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SpotMarketOptions:
    out: SpotMarketOptions = {}  # type: ignore[typeddict-item]
    if data.get("BlockDurationMinutes") is not None:
        out["block_duration_minutes"] = data["BlockDurationMinutes"]
    if data.get("InstanceInterruptionBehavior") is not None:
        import capo_workspaces_instances.types.instance_interruption_behavior_enum

        out["instance_interruption_behavior"] = (
            capo_workspaces_instances.types.instance_interruption_behavior_enum.deserialize_aws_json_1_0(
                data["InstanceInterruptionBehavior"]
            )
        )
    if data.get("MaxPrice") is not None:
        out["max_price"] = data["MaxPrice"]
    if data.get("SpotInstanceType") is not None:
        import capo_workspaces_instances.types.spot_instance_type_enum

        out["spot_instance_type"] = (
            capo_workspaces_instances.types.spot_instance_type_enum.deserialize_aws_json_1_0(
                data["SpotInstanceType"]
            )
        )
    if data.get("ValidUntilUtc") is not None:
        import capo_workspaces_instances.types._prelude.timestamp

        out["valid_until_utc"] = (
            capo_workspaces_instances.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ValidUntilUtc"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SpotMarketOptions) -> dict:
    out: dict = {}
    if "block_duration_minutes" in value:
        out["BlockDurationMinutes"] = value["block_duration_minutes"]
    if "instance_interruption_behavior" in value:
        import capo_workspaces_instances.types.instance_interruption_behavior_enum

        out["InstanceInterruptionBehavior"] = (
            capo_workspaces_instances.types.instance_interruption_behavior_enum.serialize_cbor(
                value["instance_interruption_behavior"]
            )
        )
    if "max_price" in value:
        out["MaxPrice"] = value["max_price"]
    if "spot_instance_type" in value:
        import capo_workspaces_instances.types.spot_instance_type_enum

        out["SpotInstanceType"] = (
            capo_workspaces_instances.types.spot_instance_type_enum.serialize_cbor(
                value["spot_instance_type"]
            )
        )
    if "valid_until_utc" in value:
        import capo_workspaces_instances.types._prelude.timestamp

        out["ValidUntilUtc"] = (
            capo_workspaces_instances.types._prelude.timestamp.serialize_cbor(
                value["valid_until_utc"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SpotMarketOptions:
    out: SpotMarketOptions = {}  # type: ignore[typeddict-item]
    if data.get("BlockDurationMinutes") is not None:
        out["block_duration_minutes"] = data["BlockDurationMinutes"]
    if data.get("InstanceInterruptionBehavior") is not None:
        import capo_workspaces_instances.types.instance_interruption_behavior_enum

        out["instance_interruption_behavior"] = (
            capo_workspaces_instances.types.instance_interruption_behavior_enum.deserialize_cbor(
                data["InstanceInterruptionBehavior"]
            )
        )
    if data.get("MaxPrice") is not None:
        out["max_price"] = data["MaxPrice"]
    if data.get("SpotInstanceType") is not None:
        import capo_workspaces_instances.types.spot_instance_type_enum

        out["spot_instance_type"] = (
            capo_workspaces_instances.types.spot_instance_type_enum.deserialize_cbor(
                data["SpotInstanceType"]
            )
        )
    if data.get("ValidUntilUtc") is not None:
        import capo_workspaces_instances.types._prelude.timestamp

        out["valid_until_utc"] = (
            capo_workspaces_instances.types._prelude.timestamp.deserialize_cbor(
                data["ValidUntilUtc"]
            )
        )
    return out
