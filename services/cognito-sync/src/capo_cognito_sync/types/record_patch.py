"""Generated from Smithy shape ``com.amazonaws.cognitosync#RecordPatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.date
    import capo_cognito_sync.types.long
    import capo_cognito_sync.types.operation
    import capo_cognito_sync.types.record_key
    import capo_cognito_sync.types.record_value


class RecordPatch(TypedDict, closed=True):
    op: "capo_cognito_sync.types.operation.Operation"
    """An operation, either replace or remove."""
    key: "capo_cognito_sync.types.record_key.RecordKey"
    """The key associated with the record patch."""
    value: NotRequired["capo_cognito_sync.types.record_value.RecordValue"]
    """The value associated with the record patch."""
    sync_count: "capo_cognito_sync.types.long.Long"
    """Last known server sync count for this record. Set to 0 if unknown."""
    device_last_modified_date: NotRequired["capo_cognito_sync.types.date.Date"]
    """The last modified date of the client device."""


# --- restJson1 ser/de ---
def serialize_json(value: RecordPatch) -> dict:
    out: dict = {}
    import capo_cognito_sync.types.operation

    out["Op"] = capo_cognito_sync.types.operation.serialize_json(value["op"])
    out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    out["SyncCount"] = value["sync_count"]
    if "device_last_modified_date" in value:
        import capo_cognito_sync.types.date

        out["DeviceLastModifiedDate"] = capo_cognito_sync.types.date.serialize_json(
            value["device_last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> RecordPatch:
    out: RecordPatch = {}  # type: ignore[typeddict-item]
    if data.get("Op") is not None:
        import capo_cognito_sync.types.operation

        out["op"] = capo_cognito_sync.types.operation.deserialize_json(data["Op"])
    else:
        import typing

        out["op"] = typing.cast("capo_cognito_sync.types.operation.Operation", "")
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("SyncCount") is not None:
        out["sync_count"] = data["SyncCount"]
    else:
        out["sync_count"] = 0
    if data.get("DeviceLastModifiedDate") is not None:
        import capo_cognito_sync.types.date

        out["device_last_modified_date"] = (
            capo_cognito_sync.types.date.deserialize_json(
                data["DeviceLastModifiedDate"]
            )
        )
    return out
