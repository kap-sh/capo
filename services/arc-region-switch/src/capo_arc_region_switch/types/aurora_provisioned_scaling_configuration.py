"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AuroraProvisionedScalingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.global_cluster_identifier
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.region_aurora_cluster_map
    import capo_arc_region_switch.types.region_aurora_instance_arn_map


class AuroraProvisionedScalingConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    global_cluster_identifier: (
        "capo_arc_region_switch.types.global_cluster_identifier.GlobalClusterIdentifier"
    )
    """<p>The global cluster identifier for a global database.</p>"""
    region_database_cluster_arns: (
        "capo_arc_region_switch.types.region_aurora_cluster_map.RegionAuroraClusterMap"
    )
    """<p>Per-Region configuration that maps each Region to the Aurora database cluster ARN for scaling.</p>"""
    instance_arns: "capo_arc_region_switch.types.region_aurora_instance_arn_map.RegionAuroraInstanceArnMap"
    """<p>Per-Region configuration that maps each Region to the Aurora database instance ARN for scaling.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AuroraProvisionedScalingConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["globalClusterIdentifier"] = value["global_cluster_identifier"]
    import capo_arc_region_switch.types.region_aurora_cluster_map

    out["regionDatabaseClusterArns"] = (
        capo_arc_region_switch.types.region_aurora_cluster_map.serialize_aws_json_1_0(
            value["region_database_cluster_arns"]
        )
    )
    import capo_arc_region_switch.types.region_aurora_instance_arn_map

    out["instanceArns"] = (
        capo_arc_region_switch.types.region_aurora_instance_arn_map.serialize_aws_json_1_0(
            value["instance_arns"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AuroraProvisionedScalingConfiguration:
    out: AuroraProvisionedScalingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("globalClusterIdentifier") is not None:
        out["global_cluster_identifier"] = data["globalClusterIdentifier"]
    else:
        out["global_cluster_identifier"] = ""
    if data.get("regionDatabaseClusterArns") is not None:
        import capo_arc_region_switch.types.region_aurora_cluster_map

        out["region_database_cluster_arns"] = (
            capo_arc_region_switch.types.region_aurora_cluster_map.deserialize_aws_json_1_0(
                data["regionDatabaseClusterArns"]
            )
        )
    else:
        out["region_database_cluster_arns"] = {}
    if data.get("instanceArns") is not None:
        import capo_arc_region_switch.types.region_aurora_instance_arn_map

        out["instance_arns"] = (
            capo_arc_region_switch.types.region_aurora_instance_arn_map.deserialize_aws_json_1_0(
                data["instanceArns"]
            )
        )
    else:
        out["instance_arns"] = {}
    return out
