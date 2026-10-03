"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#Connection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class Connection(TypedDict, closed=True):
    replication_instance_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The ARN of the replication instance.</p>"""
    endpoint_arn: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The ARN string that uniquely identifies the endpoint.</p>"""
    status: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The connection status. This parameter can return one of the following values:</p> <ul> <li> <p> <code>"successful"</code> </p> </li> <li> <p> <code>"testing"</code> </p> </li> <li> <p> <code>"failed"</code> </p> </li> <li> <p> <code>"deleting"</code> </p> </li> </ul>"""
    last_failure_message: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The error message when the connection last failed.</p>"""
    endpoint_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier of the endpoint. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.</p>"""
    replication_instance_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The replication instance identifier. This parameter is stored as a lowercase string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Connection) -> dict:
    out: dict = {}
    if "replication_instance_arn" in value:
        out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    if "last_failure_message" in value:
        out["LastFailureMessage"] = value["last_failure_message"]
    if "endpoint_identifier" in value:
        out["EndpointIdentifier"] = value["endpoint_identifier"]
    if "replication_instance_identifier" in value:
        out["ReplicationInstanceIdentifier"] = value["replication_instance_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationInstanceArn") is not None:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("LastFailureMessage") is not None:
        out["last_failure_message"] = data["LastFailureMessage"]
    if data.get("EndpointIdentifier") is not None:
        out["endpoint_identifier"] = data["EndpointIdentifier"]
    if data.get("ReplicationInstanceIdentifier") is not None:
        out["replication_instance_identifier"] = data["ReplicationInstanceIdentifier"]
    return out
