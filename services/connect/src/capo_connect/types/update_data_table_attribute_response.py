"""Generated from Smithy shape ``com.amazonaws.connect#UpdateDataTableAttributeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.data_table_lock_version
    import capo_connect.types.data_table_name


class UpdateDataTableAttributeResponse(TypedDict, closed=True):
    name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The trimmed name and identifier for the updated attribute.</p>"""
    lock_version: "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The new lock version for the attribute after the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataTableAttributeResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_connect.types.data_table_lock_version

    out["LockVersion"] = capo_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataTableAttributeResponse:
    out: UpdateDataTableAttributeResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("LockVersion") is not None:
        import capo_connect.types.data_table_lock_version

        out["lock_version"] = (
            capo_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDataTableAttributeResponse.lock_version required"
        )
    return out
