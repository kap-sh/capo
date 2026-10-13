"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GetBackendAuthResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.create_backend_auth_resource_config


class GetBackendAuthResponse(TypedDict, closed=True):
    app_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The app ID.</p>"""
    backend_environment_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of the backend environment.</p>"""
    error: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>If the request fails, this error is returned.</p>"""
    resource_config: NotRequired[
        "capo_amplifybackend.types.create_backend_auth_resource_config.CreateBackendAuthResourceConfig"
    ]
    """<p>The resource configuration for authorization requests to the backend of your Amplify project.</p>"""
    resource_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackendAuthResponse) -> dict:
    out: dict = {}
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "backend_environment_name" in value:
        out["backendEnvironmentName"] = value["backend_environment_name"]
    if "error" in value:
        out["error"] = value["error"]
    if "resource_config" in value:
        import capo_amplifybackend.types.create_backend_auth_resource_config

        out["resourceConfig"] = (
            capo_amplifybackend.types.create_backend_auth_resource_config.serialize_json(
                value["resource_config"]
            )
        )
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> GetBackendAuthResponse:
    out: GetBackendAuthResponse = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    if data.get("backendEnvironmentName") is not None:
        out["backend_environment_name"] = data["backendEnvironmentName"]
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("resourceConfig") is not None:
        import capo_amplifybackend.types.create_backend_auth_resource_config

        out["resource_config"] = (
            capo_amplifybackend.types.create_backend_auth_resource_config.deserialize_json(
                data["resourceConfig"]
            )
        )
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    return out


def redact_sensitive(value: GetBackendAuthResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resource_config" in value:
        import capo_amplifybackend.types.create_backend_auth_resource_config

        out["resource_config"] = (
            capo_amplifybackend.types.create_backend_auth_resource_config.redact_sensitive(
                value["resource_config"]
            )
        )
    return out
