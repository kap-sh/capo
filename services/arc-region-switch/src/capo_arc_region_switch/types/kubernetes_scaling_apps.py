"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#KubernetesScalingApps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.kubernetes_scaling_application

KubernetesScalingApps: TypeAlias = list[
    "capo_arc_region_switch.types.kubernetes_scaling_application.KubernetesScalingApplication"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KubernetesScalingApps) -> list:
    import capo_arc_region_switch.types.kubernetes_scaling_application

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.kubernetes_scaling_application.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> KubernetesScalingApps:
    import capo_arc_region_switch.types.kubernetes_scaling_application

    out: KubernetesScalingApps = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.kubernetes_scaling_application.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KubernetesScalingApps) -> list:
    import capo_arc_region_switch.types.kubernetes_scaling_application

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.kubernetes_scaling_application.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> KubernetesScalingApps:
    import capo_arc_region_switch.types.kubernetes_scaling_application

    out: KubernetesScalingApps = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_arc_region_switch.types.kubernetes_scaling_application.deserialize_cbor(
                item
            )
        )
    return out
