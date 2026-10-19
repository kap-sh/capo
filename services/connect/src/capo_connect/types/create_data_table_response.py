"""Generated from Smithy shape ``com.amazonaws.connect#CreateDataTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_lock_version


class CreateDataTableResponse(TypedDict, closed=True):
    id: "capo_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the created data table. Does not include the version alias.</p>"""
    arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the created data table. Does not include the version alias.</p>"""
    lock_version: "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The lock version information for the created data table, used for optimistic locking and table versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataTableResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    import capo_connect.types.data_table_lock_version

    out["LockVersion"] = capo_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> CreateDataTableResponse:
    out: CreateDataTableResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("LockVersion") is not None:
        import capo_connect.types.data_table_lock_version

        out["lock_version"] = (
            capo_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError("CreateDataTableResponse.lock_version required")
    return out
