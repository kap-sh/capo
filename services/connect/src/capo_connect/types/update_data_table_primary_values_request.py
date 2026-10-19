"""Generated from Smithy shape ``com.amazonaws.connect#UpdateDataTablePrimaryValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_lock_version
    import capo_connect.types.instance_id
    import capo_connect.types.primary_values_set


class UpdateDataTablePrimaryValuesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias. If the version is provided as part of the identifier or ARN, the version must be one of the two available system managed aliases, $SAVED or $LATEST.</p>"""
    primary_values: "capo_connect.types.primary_values_set.PrimaryValuesSet"
    """<p>The current primary values for the record. Required and must include values for all primary attributes. Fails if the table has primary attributes and some primary values are omitted.</p>"""
    new_primary_values: "capo_connect.types.primary_values_set.PrimaryValuesSet"
    """<p>The new primary values for the record. Required and must include values for all primary attributes. The combination must be unique within the table.</p>"""
    lock_version: "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The lock version information required for optimistic locking to prevent concurrent modifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataTablePrimaryValuesRequest) -> dict:
    out: dict = {}
    import capo_connect.types.primary_values_set

    out["PrimaryValues"] = capo_connect.types.primary_values_set.serialize_json(
        value["primary_values"]
    )
    import capo_connect.types.primary_values_set

    out["NewPrimaryValues"] = capo_connect.types.primary_values_set.serialize_json(
        value["new_primary_values"]
    )
    import capo_connect.types.data_table_lock_version

    out["LockVersion"] = capo_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataTablePrimaryValuesRequest:
    out: UpdateDataTablePrimaryValuesRequest = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryValues") is not None:
        import capo_connect.types.primary_values_set

        out["primary_values"] = capo_connect.types.primary_values_set.deserialize_json(
            data["PrimaryValues"]
        )
    else:
        out["primary_values"] = []
    if data.get("NewPrimaryValues") is not None:
        import capo_connect.types.primary_values_set

        out["new_primary_values"] = (
            capo_connect.types.primary_values_set.deserialize_json(
                data["NewPrimaryValues"]
            )
        )
    else:
        out["new_primary_values"] = []
    if data.get("LockVersion") is not None:
        import capo_connect.types.data_table_lock_version

        out["lock_version"] = (
            capo_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataTablePrimaryValuesRequest.lock_version required"
        )
    return out
