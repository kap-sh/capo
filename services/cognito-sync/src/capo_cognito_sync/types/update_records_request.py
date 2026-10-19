"""Generated from Smithy shape ``com.amazonaws.cognitosync#UpdateRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.client_context
    import capo_cognito_sync.types.dataset_name
    import capo_cognito_sync.types.device_id
    import capo_cognito_sync.types.identity_id
    import capo_cognito_sync.types.identity_pool_id
    import capo_cognito_sync.types.record_patch_list
    import capo_cognito_sync.types.sync_session_token


class UpdateRecordsRequest(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    identity_id: "capo_cognito_sync.types.identity_id.IdentityId"
    """A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region."""
    dataset_name: "capo_cognito_sync.types.dataset_name.DatasetName"
    """A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (dash), and '.' (dot)."""
    device_id: NotRequired["capo_cognito_sync.types.device_id.DeviceId"]
    """<p>The unique ID generated for this device by Cognito.</p>"""
    record_patches: NotRequired[
        "capo_cognito_sync.types.record_patch_list.RecordPatchList"
    ]
    """A list of patch operations."""
    sync_session_token: "capo_cognito_sync.types.sync_session_token.SyncSessionToken"
    """The SyncSessionToken returned by a previous call to ListRecords for this dataset and identity."""
    client_context: NotRequired["capo_cognito_sync.types.client_context.ClientContext"]
    """Intended to supply a device ID that will populate the lastModifiedBy field referenced in other methods. The ClientContext field is not yet implemented."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecordsRequest) -> dict:
    out: dict = {}
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "record_patches" in value:
        import capo_cognito_sync.types.record_patch_list

        out["RecordPatches"] = capo_cognito_sync.types.record_patch_list.serialize_json(
            value["record_patches"]
        )
    out["SyncSessionToken"] = value["sync_session_token"]
    return out


def deserialize_json(data: dict) -> UpdateRecordsRequest:
    out: UpdateRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    if data.get("RecordPatches") is not None:
        import capo_cognito_sync.types.record_patch_list

        out["record_patches"] = (
            capo_cognito_sync.types.record_patch_list.deserialize_json(
                data["RecordPatches"]
            )
        )
    if data.get("SyncSessionToken") is not None:
        out["sync_session_token"] = data["SyncSessionToken"]
    else:
        out["sync_session_token"] = ""
    return out
