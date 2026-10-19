"""Generated from Smithy shape ``com.amazonaws.connect#BatchCreateDataTableValueSuccessResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_lock_version
    import capo_connect.types.data_table_name
    import capo_connect.types.primary_values_set


class BatchCreateDataTableValueSuccessResult(TypedDict, closed=True):
    primary_values: "capo_connect.types.primary_values_set.PrimaryValuesSet"
    """<p>The result's primary values.</p>"""
    attribute_name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The result's attribute name.</p>"""
    record_id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The result's record ID.</p>"""
    lock_version: "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The result's lock version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDataTableValueSuccessResult) -> dict:
    out: dict = {}
    import capo_connect.types.primary_values_set

    out["PrimaryValues"] = capo_connect.types.primary_values_set.serialize_json(
        value["primary_values"]
    )
    out["AttributeName"] = value["attribute_name"]
    out["RecordId"] = value["record_id"]
    import capo_connect.types.data_table_lock_version

    out["LockVersion"] = capo_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> BatchCreateDataTableValueSuccessResult:
    out: BatchCreateDataTableValueSuccessResult = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryValues") is not None:
        import capo_connect.types.primary_values_set

        out["primary_values"] = capo_connect.types.primary_values_set.deserialize_json(
            data["PrimaryValues"]
        )
    else:
        out["primary_values"] = []
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("RecordId") is not None:
        out["record_id"] = data["RecordId"]
    else:
        out["record_id"] = ""
    if data.get("LockVersion") is not None:
        import capo_connect.types.data_table_lock_version

        out["lock_version"] = (
            capo_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateDataTableValueSuccessResult.lock_version required"
        )
    return out
