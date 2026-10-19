"""Generated from Smithy shape ``com.amazonaws.connect#UpdateDataTableMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_description
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_lock_level
    import capo_connect.types.data_table_name
    import capo_connect.types.instance_id
    import capo_connect.types.time_zone


class UpdateDataTableMetadataRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If the version is provided as part of the identifier or ARN, the version must be $LATEST. Providing any other alias fails with an error.</p>"""
    name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The updated name for the data table. Must conform to Connect human readable string specification and have 1-127 characters. Must be unique for the instance using case-insensitive comparison.</p>"""
    description: NotRequired[
        "capo_connect.types.data_table_description.DataTableDescription"
    ]
    """<p>The updated description for the data table. Must conform to Connect human readable string specification and have 0-250 characters.</p>"""
    value_lock_level: "capo_connect.types.data_table_lock_level.DataTableLockLevel"
    """<p>The updated value lock level for the data table. One of DATA_TABLE, PRIMARY_VALUE, ATTRIBUTE, VALUE, and NONE.</p>"""
    time_zone: "capo_connect.types.time_zone.TimeZone"
    """<p>The updated IANA timezone identifier to use when resolving time based dynamic values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataTableMetadataRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_connect.types.data_table_lock_level

    out["ValueLockLevel"] = capo_connect.types.data_table_lock_level.serialize_json(
        value["value_lock_level"]
    )
    out["TimeZone"] = value["time_zone"]
    return out


def deserialize_json(data: dict) -> UpdateDataTableMetadataRequest:
    out: UpdateDataTableMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ValueLockLevel") is not None:
        import capo_connect.types.data_table_lock_level

        out["value_lock_level"] = (
            capo_connect.types.data_table_lock_level.deserialize_json(
                data["ValueLockLevel"]
            )
        )
    else:
        import typing

        out["value_lock_level"] = typing.cast(
            "capo_connect.types.data_table_lock_level.DataTableLockLevel", ""
        )
    if data.get("TimeZone") is not None:
        out["time_zone"] = data["TimeZone"]
    else:
        out["time_zone"] = ""
    return out
