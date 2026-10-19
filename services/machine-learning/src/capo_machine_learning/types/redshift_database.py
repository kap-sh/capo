"""Generated from Smithy shape ``com.amazonaws.machinelearning#RedshiftDatabase``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.redshift_cluster_identifier
    import capo_machine_learning.types.redshift_database_name


class RedshiftDatabase(TypedDict, closed=True):
    database_name: (
        "capo_machine_learning.types.redshift_database_name.RedshiftDatabaseName"
    )
    cluster_identifier: "capo_machine_learning.types.redshift_cluster_identifier.RedshiftClusterIdentifier"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDatabase) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["ClusterIdentifier"] = value["cluster_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftDatabase:
    out: RedshiftDatabase = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("ClusterIdentifier") is not None:
        out["cluster_identifier"] = data["ClusterIdentifier"]
    else:
        out["cluster_identifier"] = ""
    return out
