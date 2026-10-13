"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetCredentialLockerResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.credential_locker_arn
    import capo_iot_managed_integrations.types.credential_locker_created_at
    import capo_iot_managed_integrations.types.credential_locker_id
    import capo_iot_managed_integrations.types.credential_locker_name
    import capo_iot_managed_integrations.types.tags_map


class GetCredentialLockerResponse(TypedDict, closed=True):
    id: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential locker.</p>"""
    arn: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_arn.CredentialLockerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the credential locker.</p>"""
    name: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_name.CredentialLockerName"
    ]
    """<p>The name of the credential locker.</p>"""
    created_at: NotRequired[
        "capo_iot_managed_integrations.types.credential_locker_created_at.CredentialLockerCreatedAt"
    ]
    """<p>The timestamp value of when the credential locker requset occurred.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the credential locker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCredentialLockerResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_at" in value:
        import capo_iot_managed_integrations.types.credential_locker_created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.credential_locker_created_at.serialize_json(
                value["created_at"]
            )
        )
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetCredentialLockerResponse:
    out: GetCredentialLockerResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedAt") is not None:
        import capo_iot_managed_integrations.types.credential_locker_created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.credential_locker_created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: GetCredentialLockerResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
