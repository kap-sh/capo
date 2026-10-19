"""Generated from Smithy shape ``com.amazonaws.machinelearning#RDSDatabase``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.rds_database_name
    import capo_machine_learning.types.rds_instance_identifier


class RDSDatabase(TypedDict, closed=True):
    instance_identifier: (
        "capo_machine_learning.types.rds_instance_identifier.RDSInstanceIdentifier"
    )
    """<p>The ID of an RDS DB instance.</p>"""
    database_name: "capo_machine_learning.types.rds_database_name.RDSDatabaseName"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RDSDatabase) -> dict:
    out: dict = {}
    out["InstanceIdentifier"] = value["instance_identifier"]
    out["DatabaseName"] = value["database_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RDSDatabase:
    out: RDSDatabase = {}  # type: ignore[typeddict-item]
    if data.get("InstanceIdentifier") is not None:
        out["instance_identifier"] = data["InstanceIdentifier"]
    else:
        out["instance_identifier"] = ""
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    return out
