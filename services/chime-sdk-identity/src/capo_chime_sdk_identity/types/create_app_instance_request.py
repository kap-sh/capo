"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#CreateAppInstanceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.client_request_token
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.non_empty_resource_name
    import capo_chime_sdk_identity.types.tag_list


class CreateAppInstanceRequest(TypedDict, closed=True):
    name: "capo_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName"
    """<p>The name of the <code>AppInstance</code>.</p>"""
    metadata: NotRequired["capo_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The metadata of the <code>AppInstance</code>. Limited to a 1KB string in UTF-8.</p>"""
    client_request_token: (
        "capo_chime_sdk_identity.types.client_request_token.ClientRequestToken"
    )
    """<p>The unique ID of the request. Use different tokens to create different <code>AppInstances</code>.</p>"""
    tags: NotRequired["capo_chime_sdk_identity.types.tag_list.TagList"]
    """<p>Tags assigned to the <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppInstanceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_chime_sdk_identity.types.tag_list

        out["Tags"] = capo_chime_sdk_identity.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateAppInstanceRequest:
    out: CreateAppInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        out["client_request_token"] = ""
    if data.get("Tags") is not None:
        import capo_chime_sdk_identity.types.tag_list

        out["tags"] = capo_chime_sdk_identity.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateAppInstanceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
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
