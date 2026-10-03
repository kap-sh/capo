"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TimestreamSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class TimestreamSettings(TypedDict, closed=True):
    database_name: "capo_database_migration_service.types.string.String"
    """<p>Database name for the endpoint.</p>"""
    memory_duration: (
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    )
    """<p>Set this attribute to specify the length of time to store all of the tables in memory that are migrated into Amazon Timestream from the source database. Time is measured in units of hours. When Timestream data comes in, it first resides in memory for the specified duration, which allows quick access to it.</p>"""
    magnetic_duration: (
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    )
    """<p>Set this attribute to specify the default magnetic duration applied to the Amazon Timestream tables in days. This is the number of days that records remain in magnetic store before being discarded. For more information, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html">Storage</a> in the <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/">Amazon Timestream Developer Guide</a>.</p>"""
    cdc_inserts_and_updates: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to <code>true</code> to specify that DMS only applies inserts and updates, and not deletes. Amazon Timestream does not allow deleting records, so if this value is <code>false</code>, DMS nulls out the corresponding record in the Timestream database rather than deleting it.</p>"""
    enable_magnetic_store_writes: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this attribute to <code>true</code> to enable memory store writes. When this value is <code>false</code>, DMS does not write records that are older in days than the value specified in <code>MagneticDuration</code>, because Amazon Timestream does not allow memory writes by default. For more information, see <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/storage.html">Storage</a> in the <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/">Amazon Timestream Developer Guide</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimestreamSettings) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["MemoryDuration"] = value["memory_duration"]
    out["MagneticDuration"] = value["magnetic_duration"]
    if "cdc_inserts_and_updates" in value:
        out["CdcInsertsAndUpdates"] = value["cdc_inserts_and_updates"]
    if "enable_magnetic_store_writes" in value:
        out["EnableMagneticStoreWrites"] = value["enable_magnetic_store_writes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TimestreamSettings:
    out: TimestreamSettings = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("TimestreamSettings.database_name required")
    if data.get("MemoryDuration") is not None:
        out["memory_duration"] = data["MemoryDuration"]
    else:
        raise DeserializationError("TimestreamSettings.memory_duration required")
    if data.get("MagneticDuration") is not None:
        out["magnetic_duration"] = data["MagneticDuration"]
    else:
        raise DeserializationError("TimestreamSettings.magnetic_duration required")
    if data.get("CdcInsertsAndUpdates") is not None:
        out["cdc_inserts_and_updates"] = data["CdcInsertsAndUpdates"]
    if data.get("EnableMagneticStoreWrites") is not None:
        out["enable_magnetic_store_writes"] = data["EnableMagneticStoreWrites"]
    return out
