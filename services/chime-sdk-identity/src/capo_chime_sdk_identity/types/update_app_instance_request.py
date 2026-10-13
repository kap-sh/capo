"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#UpdateAppInstanceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.non_empty_resource_name


class UpdateAppInstanceRequest(TypedDict, closed=True):
    app_instance_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstance</code>.</p>"""
    name: "capo_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName"
    """<p>The name that you want to change.</p>"""
    metadata: "capo_chime_sdk_identity.types.metadata.Metadata"
    """<p>The metadata that you want to change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppInstanceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> UpdateAppInstanceRequest:
    out: UpdateAppInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateAppInstanceRequest.name required")
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    else:
        raise DeserializationError("UpdateAppInstanceRequest.metadata required")
    return out


def redact_sensitive(value: UpdateAppInstanceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
