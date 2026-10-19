"""Generated from Smithy shape ``com.amazonaws.connect#CreateDataTableAttributeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.data_table_id
    import capo_connect.types.data_table_lock_version
    import capo_connect.types.data_table_name


class CreateDataTableAttributeResponse(TypedDict, closed=True):
    name: "capo_connect.types.data_table_name.DataTableName"
    """<p>The name of the created attribute since it also serves as the identifier. This could be different than the parameter passed in since it will be trimmed for whitespace.</p>"""
    attribute_id: NotRequired["capo_connect.types.data_table_id.DataTableId"]
    """<p>The unique identifier assigned to the created attribute.</p>"""
    lock_version: "capo_connect.types.data_table_lock_version.DataTableLockVersion"
    """<p>The lock version information for the data table and attribute, used for optimistic locking and versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataTableAttributeResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "attribute_id" in value:
        out["AttributeId"] = value["attribute_id"]
    import capo_connect.types.data_table_lock_version

    out["LockVersion"] = capo_connect.types.data_table_lock_version.serialize_json(
        value["lock_version"]
    )
    return out


def deserialize_json(data: dict) -> CreateDataTableAttributeResponse:
    out: CreateDataTableAttributeResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("AttributeId") is not None:
        out["attribute_id"] = data["AttributeId"]
    if data.get("LockVersion") is not None:
        import capo_connect.types.data_table_lock_version

        out["lock_version"] = (
            capo_connect.types.data_table_lock_version.deserialize_json(
                data["LockVersion"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataTableAttributeResponse.lock_version required"
        )
    return out
