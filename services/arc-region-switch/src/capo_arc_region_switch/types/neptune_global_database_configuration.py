"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#NeptuneGlobalDatabaseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.neptune_default_behavior
    import capo_arc_region_switch.types.neptune_global_cluster_identifier
    import capo_arc_region_switch.types.neptune_ungraceful
    import capo_arc_region_switch.types.region_neptune_cluster_arn_map


class NeptuneGlobalDatabaseConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    behavior: (
        "capo_arc_region_switch.types.neptune_default_behavior.NeptuneDefaultBehavior"
    )
    """<p>The behavior for a global database, that is, only allow switchover or also allow failover.</p>"""
    ungraceful: NotRequired[
        "capo_arc_region_switch.types.neptune_ungraceful.NeptuneUngraceful"
    ]
    """<p>The settings for ungraceful execution.</p>"""
    global_cluster_identifier: "capo_arc_region_switch.types.neptune_global_cluster_identifier.NeptuneGlobalClusterIdentifier"
    """<p>The global cluster identifier for a Neptune global database.</p>"""
    region_database_cluster_arns: "capo_arc_region_switch.types.region_neptune_cluster_arn_map.RegionNeptuneClusterArnMap"
    """<p>The database cluster Amazon Resource Names (ARNs) for a Neptune global database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NeptuneGlobalDatabaseConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    import capo_arc_region_switch.types.neptune_default_behavior

    out["behavior"] = (
        capo_arc_region_switch.types.neptune_default_behavior.serialize_aws_json_1_0(
            value.get("behavior", "switchoverOnly")
        )
    )
    if "ungraceful" in value:
        import capo_arc_region_switch.types.neptune_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.neptune_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    out["globalClusterIdentifier"] = value["global_cluster_identifier"]
    import capo_arc_region_switch.types.region_neptune_cluster_arn_map

    out["regionDatabaseClusterArns"] = (
        capo_arc_region_switch.types.region_neptune_cluster_arn_map.serialize_aws_json_1_0(
            value["region_database_cluster_arns"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NeptuneGlobalDatabaseConfiguration:
    out: NeptuneGlobalDatabaseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("behavior") is not None:
        import capo_arc_region_switch.types.neptune_default_behavior

        out["behavior"] = (
            capo_arc_region_switch.types.neptune_default_behavior.deserialize_aws_json_1_0(
                data["behavior"]
            )
        )
    else:
        out["behavior"] = "switchoverOnly"
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.neptune_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.neptune_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    if data.get("globalClusterIdentifier") is not None:
        out["global_cluster_identifier"] = data["globalClusterIdentifier"]
    else:
        out["global_cluster_identifier"] = ""
    if data.get("regionDatabaseClusterArns") is not None:
        import capo_arc_region_switch.types.region_neptune_cluster_arn_map

        out["region_database_cluster_arns"] = (
            capo_arc_region_switch.types.region_neptune_cluster_arn_map.deserialize_aws_json_1_0(
                data["regionDatabaseClusterArns"]
            )
        )
    else:
        out["region_database_cluster_arns"] = {}
    return out
