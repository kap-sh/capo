"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EksResourceScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.eks_capacity_monitoring_approach
    import capo_arc_region_switch.types.eks_clusters
    import capo_arc_region_switch.types.eks_resource_scaling_ungraceful
    import capo_arc_region_switch.types.kubernetes_resource_type
    import capo_arc_region_switch.types.kubernetes_scaling_apps


class EksResourceScalingConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    kubernetes_resource_type: (
        "capo_arc_region_switch.types.kubernetes_resource_type.KubernetesResourceType"
    )
    """<p>The Kubernetes resource type for the configuration.</p>"""
    scaling_resources: NotRequired[
        "capo_arc_region_switch.types.kubernetes_scaling_apps.KubernetesScalingApps"
    ]
    """<p>The scaling resources for the configuration.</p>"""
    eks_clusters: NotRequired["capo_arc_region_switch.types.eks_clusters.EksClusters"]
    """<p>The clusters for the configuration.</p>"""
    ungraceful: NotRequired[
        "capo_arc_region_switch.types.eks_resource_scaling_ungraceful.EksResourceScalingUngraceful"
    ]
    """<p>The settings for ungraceful execution.</p>"""
    target_percent: "int"
    """<p>The target percentage for the configuration. The default is 100.</p>"""
    capacity_monitoring_approach: "capo_arc_region_switch.types.eks_capacity_monitoring_approach.EksCapacityMonitoringApproach"
    """<p>The monitoring approach for the configuration, that is, whether it was sampled in the last 24 hours or autoscaled in the last 24 hours.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EksResourceScalingConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    import capo_arc_region_switch.types.kubernetes_resource_type

    out["kubernetesResourceType"] = (
        capo_arc_region_switch.types.kubernetes_resource_type.serialize_aws_json_1_0(
            value["kubernetes_resource_type"]
        )
    )
    if "scaling_resources" in value:
        import capo_arc_region_switch.types.kubernetes_scaling_apps

        out["scalingResources"] = (
            capo_arc_region_switch.types.kubernetes_scaling_apps.serialize_aws_json_1_0(
                value["scaling_resources"]
            )
        )
    if "eks_clusters" in value:
        import capo_arc_region_switch.types.eks_clusters

        out["eksClusters"] = (
            capo_arc_region_switch.types.eks_clusters.serialize_aws_json_1_0(
                value["eks_clusters"]
            )
        )
    if "ungraceful" in value:
        import capo_arc_region_switch.types.eks_resource_scaling_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.eks_resource_scaling_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    out["targetPercent"] = value.get("target_percent", 100)
    import capo_arc_region_switch.types.eks_capacity_monitoring_approach

    out["capacityMonitoringApproach"] = (
        capo_arc_region_switch.types.eks_capacity_monitoring_approach.serialize_aws_json_1_0(
            value.get("capacity_monitoring_approach", "sampledMaxInLast24Hours")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EksResourceScalingConfiguration:
    out: EksResourceScalingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("kubernetesResourceType") is not None:
        import capo_arc_region_switch.types.kubernetes_resource_type

        out["kubernetes_resource_type"] = (
            capo_arc_region_switch.types.kubernetes_resource_type.deserialize_aws_json_1_0(
                data["kubernetesResourceType"]
            )
        )
    else:
        raise DeserializationError(
            "EksResourceScalingConfiguration.kubernetes_resource_type required"
        )
    if data.get("scalingResources") is not None:
        import capo_arc_region_switch.types.kubernetes_scaling_apps

        out["scaling_resources"] = (
            capo_arc_region_switch.types.kubernetes_scaling_apps.deserialize_aws_json_1_0(
                data["scalingResources"]
            )
        )
    if data.get("eksClusters") is not None:
        import capo_arc_region_switch.types.eks_clusters

        out["eks_clusters"] = (
            capo_arc_region_switch.types.eks_clusters.deserialize_aws_json_1_0(
                data["eksClusters"]
            )
        )
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.eks_resource_scaling_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.eks_resource_scaling_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    if data.get("targetPercent") is not None:
        out["target_percent"] = data["targetPercent"]
    else:
        out["target_percent"] = 100
    if data.get("capacityMonitoringApproach") is not None:
        import capo_arc_region_switch.types.eks_capacity_monitoring_approach

        out["capacity_monitoring_approach"] = (
            capo_arc_region_switch.types.eks_capacity_monitoring_approach.deserialize_aws_json_1_0(
                data["capacityMonitoringApproach"]
            )
        )
    else:
        out["capacity_monitoring_approach"] = "sampledMaxInLast24Hours"
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EksResourceScalingConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    import capo_arc_region_switch.types.kubernetes_resource_type

    out["kubernetesResourceType"] = (
        capo_arc_region_switch.types.kubernetes_resource_type.serialize_cbor(
            value["kubernetes_resource_type"]
        )
    )
    if "scaling_resources" in value:
        import capo_arc_region_switch.types.kubernetes_scaling_apps

        out["scalingResources"] = (
            capo_arc_region_switch.types.kubernetes_scaling_apps.serialize_cbor(
                value["scaling_resources"]
            )
        )
    if "eks_clusters" in value:
        import capo_arc_region_switch.types.eks_clusters

        out["eksClusters"] = capo_arc_region_switch.types.eks_clusters.serialize_cbor(
            value["eks_clusters"]
        )
    if "ungraceful" in value:
        import capo_arc_region_switch.types.eks_resource_scaling_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.eks_resource_scaling_ungraceful.serialize_cbor(
                value["ungraceful"]
            )
        )
    out["targetPercent"] = value.get("target_percent", 100)
    import capo_arc_region_switch.types.eks_capacity_monitoring_approach

    out["capacityMonitoringApproach"] = (
        capo_arc_region_switch.types.eks_capacity_monitoring_approach.serialize_cbor(
            value.get("capacity_monitoring_approach", "sampledMaxInLast24Hours")
        )
    )
    return out


def deserialize_cbor(data: dict) -> EksResourceScalingConfiguration:
    out: EksResourceScalingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("kubernetesResourceType") is not None:
        import capo_arc_region_switch.types.kubernetes_resource_type

        out["kubernetes_resource_type"] = (
            capo_arc_region_switch.types.kubernetes_resource_type.deserialize_cbor(
                data["kubernetesResourceType"]
            )
        )
    else:
        raise DeserializationError(
            "EksResourceScalingConfiguration.kubernetes_resource_type required"
        )
    if data.get("scalingResources") is not None:
        import capo_arc_region_switch.types.kubernetes_scaling_apps

        out["scaling_resources"] = (
            capo_arc_region_switch.types.kubernetes_scaling_apps.deserialize_cbor(
                data["scalingResources"]
            )
        )
    if data.get("eksClusters") is not None:
        import capo_arc_region_switch.types.eks_clusters

        out["eks_clusters"] = (
            capo_arc_region_switch.types.eks_clusters.deserialize_cbor(
                data["eksClusters"]
            )
        )
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.eks_resource_scaling_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.eks_resource_scaling_ungraceful.deserialize_cbor(
                data["ungraceful"]
            )
        )
    if data.get("targetPercent") is not None:
        out["target_percent"] = data["targetPercent"]
    else:
        out["target_percent"] = 100
    if data.get("capacityMonitoringApproach") is not None:
        import capo_arc_region_switch.types.eks_capacity_monitoring_approach

        out["capacity_monitoring_approach"] = (
            capo_arc_region_switch.types.eks_capacity_monitoring_approach.deserialize_cbor(
                data["capacityMonitoringApproach"]
            )
        )
    else:
        out["capacity_monitoring_approach"] = "sampledMaxInLast24Hours"
    return out
