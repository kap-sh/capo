"""Generated from Smithy shape ``com.amazonaws.pinpoint#GCMChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string


class GCMChannelResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the GCM channel applies to.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time when the GCM channel was enabled.</p>"""
    credential: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Web API Key, also referred to as an <i>API_KEY</i> or <i>server key</i>, that you received from Google to communicate with Google services.</p>"""
    default_authentication_method: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The default authentication method used for GCM. Values are either "TOKEN" or "KEY". Defaults to "KEY".</p>"""
    enabled: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the GCM channel is enabled for the application.</p>"""
    has_credential: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>(Not used) This property is retained only for backward compatibility.</p>"""
    has_fcm_service_credentials: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Returns true if the JSON file provided by Google during registration process was used in the <b>ServiceJson</b> field of the request.</p>"""
    id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>(Deprecated) An identifier for the GCM channel. This property is retained only for backward compatibility.</p>"""
    is_archived: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the GCM channel is archived.</p>"""
    last_modified_by: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The user who last modified the GCM channel.</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time when the GCM channel was last modified.</p>"""
    platform: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The type of messaging or notification platform for the channel. For the GCM channel, this value is GCM.</p>"""
    version: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The current version of the GCM channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GCMChannelResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "credential" in value:
        out["Credential"] = value["credential"]
    if "default_authentication_method" in value:
        out["DefaultAuthenticationMethod"] = value["default_authentication_method"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "has_credential" in value:
        out["HasCredential"] = value["has_credential"]
    if "has_fcm_service_credentials" in value:
        out["HasFcmServiceCredentials"] = value["has_fcm_service_credentials"]
    if "id" in value:
        out["Id"] = value["id"]
    if "is_archived" in value:
        out["IsArchived"] = value["is_archived"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> GCMChannelResponse:
    out: GCMChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("CreationDate") is not None:
        out["creation_date"] = data["CreationDate"]
    if data.get("Credential") is not None:
        out["credential"] = data["Credential"]
    if data.get("DefaultAuthenticationMethod") is not None:
        out["default_authentication_method"] = data["DefaultAuthenticationMethod"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("HasCredential") is not None:
        out["has_credential"] = data["HasCredential"]
    if data.get("HasFcmServiceCredentials") is not None:
        out["has_fcm_service_credentials"] = data["HasFcmServiceCredentials"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("IsArchived") is not None:
        out["is_archived"] = data["IsArchived"]
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    if data.get("LastModifiedDate") is not None:
        out["last_modified_date"] = data["LastModifiedDate"]
    if data.get("Platform") is not None:
        out["platform"] = data["Platform"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
