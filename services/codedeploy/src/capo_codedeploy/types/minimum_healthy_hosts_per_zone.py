"""Generated from Smithy shape ``com.amazonaws.codedeploy#MinimumHealthyHostsPerZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.minimum_healthy_hosts_per_zone_type
    import capo_codedeploy.types.minimum_healthy_hosts_per_zone_value


class MinimumHealthyHostsPerZone(TypedDict, closed=True):
    type: NotRequired[
        "capo_codedeploy.types.minimum_healthy_hosts_per_zone_type.MinimumHealthyHostsPerZoneType"
    ]
    """<p>The <code>type</code> associated with the <code>MinimumHealthyHostsPerZone</code> option.</p>"""
    value: "capo_codedeploy.types.minimum_healthy_hosts_per_zone_value.MinimumHealthyHostsPerZoneValue"
    """<p>The <code>value</code> associated with the <code>MinimumHealthyHostsPerZone</code> option.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MinimumHealthyHostsPerZone) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codedeploy.types.minimum_healthy_hosts_per_zone_type

        out["type"] = (
            capo_codedeploy.types.minimum_healthy_hosts_per_zone_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> MinimumHealthyHostsPerZone:
    out: MinimumHealthyHostsPerZone = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codedeploy.types.minimum_healthy_hosts_per_zone_type

        out["type"] = (
            capo_codedeploy.types.minimum_healthy_hosts_per_zone_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MinimumHealthyHostsPerZone) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codedeploy.types.minimum_healthy_hosts_per_zone_type

        out["type"] = (
            capo_codedeploy.types.minimum_healthy_hosts_per_zone_type.serialize_cbor(
                value["type"]
            )
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_cbor(data: dict) -> MinimumHealthyHostsPerZone:
    out: MinimumHealthyHostsPerZone = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codedeploy.types.minimum_healthy_hosts_per_zone_type

        out["type"] = (
            capo_codedeploy.types.minimum_healthy_hosts_per_zone_type.deserialize_cbor(
                data["type"]
            )
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
