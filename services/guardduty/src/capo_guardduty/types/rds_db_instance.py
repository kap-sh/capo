"""Generated from Smithy shape ``com.amazonaws.guardduty#RdsDbInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class RdsDbInstance(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_guardduty.types.string.String"]
    """<p>The identifier of the database instance.</p>"""
    db_cluster_identifier: NotRequired["capo_guardduty.types.string.String"]
    """<p>The identifier of the database cluster that contains the instance.</p>"""
    db_instance_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the database instance.</p>"""
    dbi_resource_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique resource ID of the database instance.</p>"""
    engine: NotRequired["capo_guardduty.types.string.String"]
    """<p>The database engine of the instance.</p>"""
    engine_version: NotRequired["capo_guardduty.types.string.String"]
    """<p>The version of the database engine.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsDbInstance) -> dict:
    out: dict = {}
    if "db_instance_identifier" in value:
        out["dbInstanceIdentifier"] = value["db_instance_identifier"]
    if "db_cluster_identifier" in value:
        out["dbClusterIdentifier"] = value["db_cluster_identifier"]
    if "db_instance_arn" in value:
        out["dbInstanceArn"] = value["db_instance_arn"]
    if "dbi_resource_id" in value:
        out["dbiResourceId"] = value["dbi_resource_id"]
    if "engine" in value:
        out["engine"] = value["engine"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    return out


def deserialize_json(data: dict) -> RdsDbInstance:
    out: RdsDbInstance = {}  # type: ignore[typeddict-item]
    if data.get("dbInstanceIdentifier") is not None:
        out["db_instance_identifier"] = data["dbInstanceIdentifier"]
    if data.get("dbClusterIdentifier") is not None:
        out["db_cluster_identifier"] = data["dbClusterIdentifier"]
    if data.get("dbInstanceArn") is not None:
        out["db_instance_arn"] = data["dbInstanceArn"]
    if data.get("dbiResourceId") is not None:
        out["dbi_resource_id"] = data["dbiResourceId"]
    if data.get("engine") is not None:
        out["engine"] = data["engine"]
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    return out
