"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#CreateAppInstanceUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.client_request_token
    import capo_chime_sdk_identity.types.expiration_settings
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.tag_list
    import capo_chime_sdk_identity.types.user_id
    import capo_chime_sdk_identity.types.user_name


class CreateAppInstanceUserRequest(TypedDict, closed=True):
    app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code> request.</p>"""
    app_instance_user_id: "capo_chime_sdk_identity.types.user_id.UserId"
    """<p>The user ID of the <code>AppInstance</code>.</p>"""
    name: "capo_chime_sdk_identity.types.user_name.UserName"
    """<p>The user's name.</p>"""
    metadata: NotRequired["capo_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The request's metadata. Limited to a 1KB string in UTF-8.</p>"""
    client_request_token: (
        "capo_chime_sdk_identity.types.client_request_token.ClientRequestToken"
    )
    """<p>The unique ID of the request. Use different tokens to request additional <code>AppInstances</code>.</p>"""
    tags: NotRequired["capo_chime_sdk_identity.types.tag_list.TagList"]
    """<p>Tags assigned to the <code>AppInstanceUser</code>.</p>"""
    expiration_settings: NotRequired[
        "capo_chime_sdk_identity.types.expiration_settings.ExpirationSettings"
    ]
    """<p>Settings that control the interval after which the <code>AppInstanceUser</code> is automatically deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppInstanceUserRequest) -> dict:
    out: dict = {}
    out["AppInstanceArn"] = value["app_instance_arn"]
    out["AppInstanceUserId"] = value["app_instance_user_id"]
    out["Name"] = value["name"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_chime_sdk_identity.types.tag_list

        out["Tags"] = capo_chime_sdk_identity.types.tag_list.serialize_json(
            value["tags"]
        )
    if "expiration_settings" in value:
        import capo_chime_sdk_identity.types.expiration_settings

        out["ExpirationSettings"] = (
            capo_chime_sdk_identity.types.expiration_settings.serialize_json(
                value["expiration_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAppInstanceUserRequest:
    out: CreateAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceArn") is not None:
        out["app_instance_arn"] = data["AppInstanceArn"]
    else:
        raise DeserializationError(
            "CreateAppInstanceUserRequest.app_instance_arn required"
        )
    if data.get("AppInstanceUserId") is not None:
        out["app_instance_user_id"] = data["AppInstanceUserId"]
    else:
        raise DeserializationError(
            "CreateAppInstanceUserRequest.app_instance_user_id required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateAppInstanceUserRequest.name required")
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError(
            "CreateAppInstanceUserRequest.client_request_token required"
        )
    if data.get("Tags") is not None:
        import capo_chime_sdk_identity.types.tag_list

        out["tags"] = capo_chime_sdk_identity.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if data.get("ExpirationSettings") is not None:
        import capo_chime_sdk_identity.types.expiration_settings

        out["expiration_settings"] = (
            capo_chime_sdk_identity.types.expiration_settings.deserialize_json(
                data["ExpirationSettings"]
            )
        )
    return out


def redact_sensitive(value: CreateAppInstanceUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instance_user_id" in value:
        out["app_instance_user_id"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        import capo_chime_sdk_identity.types.tag_list

        out["tags"] = capo_chime_sdk_identity.types.tag_list.redact_sensitive(
            value["tags"]
        )
    return out
