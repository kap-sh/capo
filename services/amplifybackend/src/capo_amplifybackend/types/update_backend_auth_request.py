"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.update_backend_auth_resource_config


class UpdateBackendAuthRequest(TypedDict, closed=True):
    app_id: "capo_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "capo_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    resource_config: NotRequired[
        "capo_amplifybackend.types.update_backend_auth_resource_config.UpdateBackendAuthResourceConfig"
    ]
    """<p>The resource configuration for this request object.</p>"""
    resource_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthRequest) -> dict:
    out: dict = {}
    if "resource_config" in value:
        import capo_amplifybackend.types.update_backend_auth_resource_config

        out["resourceConfig"] = (
            capo_amplifybackend.types.update_backend_auth_resource_config.serialize_json(
                value["resource_config"]
            )
        )
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthRequest:
    out: UpdateBackendAuthRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceConfig") is not None:
        import capo_amplifybackend.types.update_backend_auth_resource_config

        out["resource_config"] = (
            capo_amplifybackend.types.update_backend_auth_resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    return out


def redact_sensitive(value: UpdateBackendAuthRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resource_config" in value:
        import capo_amplifybackend.types.update_backend_auth_resource_config

        out["resource_config"] = (
            capo_amplifybackend.types.update_backend_auth_resource_config.redact_sensitive(
                value["resource_config"]
            )
        )
    return out
