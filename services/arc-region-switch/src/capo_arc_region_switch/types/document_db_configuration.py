"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#DocumentDbConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.document_db_cluster_arns
    import capo_arc_region_switch.types.document_db_default_behavior
    import capo_arc_region_switch.types.document_db_global_cluster_identifier
    import capo_arc_region_switch.types.document_db_ungraceful
    import capo_arc_region_switch.types.iam_role_arn


class DocumentDbConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    behavior: "capo_arc_region_switch.types.document_db_default_behavior.DocumentDbDefaultBehavior"
    """<p>The behavior for a global cluster, that is, only allow switchover or also allow failover.</p>"""
    ungraceful: NotRequired[
        "capo_arc_region_switch.types.document_db_ungraceful.DocumentDbUngraceful"
    ]
    """<p>The settings for ungraceful execution.</p>"""
    global_cluster_identifier: "capo_arc_region_switch.types.document_db_global_cluster_identifier.DocumentDbGlobalClusterIdentifier"
    """<p>The global cluster identifier for a DocumentDB global cluster.</p>"""
    database_cluster_arns: (
        "capo_arc_region_switch.types.document_db_cluster_arns.DocumentDbClusterArns"
    )
    """<p>The database cluster Amazon Resource Names (ARNs) for a DocumentDB global cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DocumentDbConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    import capo_arc_region_switch.types.document_db_default_behavior

    out["behavior"] = (
        capo_arc_region_switch.types.document_db_default_behavior.serialize_aws_json_1_0(
            value.get("behavior", "switchoverOnly")
        )
    )
    if "ungraceful" in value:
        import capo_arc_region_switch.types.document_db_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.document_db_ungraceful.serialize_aws_json_1_0(
                value["ungraceful"]
            )
        )
    out["globalClusterIdentifier"] = value["global_cluster_identifier"]
    import capo_arc_region_switch.types.document_db_cluster_arns

    out["databaseClusterArns"] = (
        capo_arc_region_switch.types.document_db_cluster_arns.serialize_aws_json_1_0(
            value["database_cluster_arns"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DocumentDbConfiguration:
    out: DocumentDbConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("behavior") is not None:
        import capo_arc_region_switch.types.document_db_default_behavior

        out["behavior"] = (
            capo_arc_region_switch.types.document_db_default_behavior.deserialize_aws_json_1_0(
                data["behavior"]
            )
        )
    else:
        out["behavior"] = "switchoverOnly"
    if data.get("ungraceful") is not None:
        import capo_arc_region_switch.types.document_db_ungraceful

        out["ungraceful"] = (
            capo_arc_region_switch.types.document_db_ungraceful.deserialize_aws_json_1_0(
                data["ungraceful"]
            )
        )
    if data.get("globalClusterIdentifier") is not None:
        out["global_cluster_identifier"] = data["globalClusterIdentifier"]
    else:
        out["global_cluster_identifier"] = ""
    if data.get("databaseClusterArns") is not None:
        import capo_arc_region_switch.types.document_db_cluster_arns

        out["database_cluster_arns"] = (
            capo_arc_region_switch.types.document_db_cluster_arns.deserialize_aws_json_1_0(
                data["databaseClusterArns"]
            )
        )
    else:
        out["database_cluster_arns"] = []
    return out
