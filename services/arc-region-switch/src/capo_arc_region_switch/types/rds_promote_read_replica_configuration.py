"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RdsPromoteReadReplicaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.rds_db_instance_arn_map


class RdsPromoteReadReplicaConfiguration(TypedDict, closed=True):
    timeout_minutes: "int"
    """<p>The timeout value specified for the configuration.</p>"""
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross-account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    db_instance_arn_map: (
        "capo_arc_region_switch.types.rds_db_instance_arn_map.RdsDbInstanceArnMap"
    )
    """<p>A map of database instance ARNs for each Region in the plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RdsPromoteReadReplicaConfiguration) -> dict:
    out: dict = {}
    out["timeoutMinutes"] = value.get("timeout_minutes", 60)
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    import capo_arc_region_switch.types.rds_db_instance_arn_map

    out["dbInstanceArnMap"] = (
        capo_arc_region_switch.types.rds_db_instance_arn_map.serialize_aws_json_1_0(
            value["db_instance_arn_map"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RdsPromoteReadReplicaConfiguration:
    out: RdsPromoteReadReplicaConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    else:
        out["timeout_minutes"] = 60
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("dbInstanceArnMap") is not None:
        import capo_arc_region_switch.types.rds_db_instance_arn_map

        out["db_instance_arn_map"] = (
            capo_arc_region_switch.types.rds_db_instance_arn_map.deserialize_aws_json_1_0(
                data["dbInstanceArnMap"]
            )
        )
    else:
        out["db_instance_arn_map"] = {}
    return out
