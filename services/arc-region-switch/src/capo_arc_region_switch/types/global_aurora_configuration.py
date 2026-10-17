"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GlobalAuroraConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.aurora_cluster_arns
    import capo_arc_region_switch.types.global_aurora_default_behavior
    import capo_arc_region_switch.types.global_aurora_ungraceful
    import capo_arc_region_switch.types.global_cluster_identifier
    import capo_arc_region_switch.types.iam_role_arn


class GlobalAuroraConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    behavior: "capo_arc_region_switch.types.global_aurora_default_behavior.GlobalAuroraDefaultBehavior"
    """<p>The behavior for a global database, that is, only allow switchover or also allow failover.</p>"""
    ungraceful: NotRequired[
        "capo_arc_region_switch.types.global_aurora_ungraceful.GlobalAuroraUngraceful"
    ]
    """<p>The settings for ungraceful execution.</p>"""
    global_cluster_identifier: (
        "capo_arc_region_switch.types.global_cluster_identifier.GlobalClusterIdentifier"
    )
    """<p>The global cluster identifier for a global database.</p>"""
    database_cluster_arns: (
        "capo_arc_region_switch.types.aurora_cluster_arns.AuroraClusterArns"
    )
    """<p>The database cluster Amazon Resource Names (ARNs) for a global database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalAuroraConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    import capo_arc_region_switch.types.global_aurora_default_behavior

    out["behavior"] = (
        capo_arc_region_switch.types.global_aurora_default_behavior.serialize_aws_json_1_0(
            value.get("behavior", "switchoverOnly")
        )
    )
    if "ungraceful" in value:
        import capo_arc_region_switch.types.global_aurora_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.global_aurora_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    out["globalClusterIdentifier"] = value["global_cluster_identifier"]
    import capo_arc_region_switch.types.aurora_cluster_arns

    out["databaseClusterArns"] = (
        capo_arc_region_switch.types.aurora_cluster_arns.serialize_aws_json_1_0(
            value["database_cluster_arns"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalAuroraConfiguration:
    out: GlobalAuroraConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("behavior") is not None:
        import capo_arc_region_switch.types.global_aurora_default_behavior

        out["behavior"] = (
            capo_arc_region_switch.types.global_aurora_default_behavior.deserialize_aws_json_1_0(
                data["behavior"]
            )
        )
    else:
        out["behavior"] = "switchoverOnly"
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.global_aurora_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.global_aurora_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    if data.get("globalClusterIdentifier") is not None:
        out["global_cluster_identifier"] = data["globalClusterIdentifier"]
    else:
        raise DeserializationError(
            "GlobalAuroraConfiguration.global_cluster_identifier required"
        )
    if data.get("databaseClusterArns") is not None:
        import capo_arc_region_switch.types.aurora_cluster_arns

        out["database_cluster_arns"] = (
            capo_arc_region_switch.types.aurora_cluster_arns.deserialize_aws_json_1_0(
                data["databaseClusterArns"]
            )
        )
    else:
        raise DeserializationError(
            "GlobalAuroraConfiguration.database_cluster_arns required"
        )
    return out
