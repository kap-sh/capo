"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendAuthResourceConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.auth_resources
    import capo_amplifybackend.types.create_backend_auth_identity_pool_config
    import capo_amplifybackend.types.create_backend_auth_user_pool_config
    import capo_amplifybackend.types.service


class CreateBackendAuthResourceConfig(TypedDict, closed=True):
    auth_resources: NotRequired[
        "capo_amplifybackend.types.auth_resources.AuthResources"
    ]
    """<p>Defines whether you want to configure only authentication or both authentication and authorization settings.</p>"""
    identity_pool_configs: NotRequired[
        "capo_amplifybackend.types.create_backend_auth_identity_pool_config.CreateBackendAuthIdentityPoolConfig"
    ]
    """<p>Describes the authorization configuration for the Amazon Cognito identity pool, provisioned as a part of your auth resource in the Amplify project.</p>"""
    service: NotRequired["capo_amplifybackend.types.service.Service"]
    """<p>Defines the service name to use when configuring an authentication resource in your Amplify project.</p>"""
    user_pool_configs: NotRequired[
        "capo_amplifybackend.types.create_backend_auth_user_pool_config.CreateBackendAuthUserPoolConfig"
    ]
    """<p>Describes authentication configuration for the Amazon Cognito user pool, provisioned as a part of your auth resource in the Amplify project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendAuthResourceConfig) -> dict:
    out: dict = {}
    if "auth_resources" in value:
        import capo_amplifybackend.types.auth_resources

        out["authResources"] = capo_amplifybackend.types.auth_resources.serialize_json(
            value["auth_resources"]
        )
    if "identity_pool_configs" in value:
        import capo_amplifybackend.types.create_backend_auth_identity_pool_config

        out["identityPoolConfigs"] = (
            capo_amplifybackend.types.create_backend_auth_identity_pool_config.serialize_json(
                value["identity_pool_configs"]
            )
        )
    if "service" in value:
        import capo_amplifybackend.types.service

        out["service"] = capo_amplifybackend.types.service.serialize_json(
            value["service"]
        )
    if "user_pool_configs" in value:
        import capo_amplifybackend.types.create_backend_auth_user_pool_config

        out["userPoolConfigs"] = (
            capo_amplifybackend.types.create_backend_auth_user_pool_config.serialize_json(
                value["user_pool_configs"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateBackendAuthResourceConfig:
    out: CreateBackendAuthResourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("authResources") is not None:
        import capo_amplifybackend.types.auth_resources

        out["auth_resources"] = (
            capo_amplifybackend.types.auth_resources.deserialize_json(
                data["authResources"]
            )
        )
    if data.get("identityPoolConfigs") is not None:
        import capo_amplifybackend.types.create_backend_auth_identity_pool_config

        out["identity_pool_configs"] = (
            capo_amplifybackend.types.create_backend_auth_identity_pool_config.deserialize_json(
                data["identityPoolConfigs"]
            )
        )
    if data.get("service") is not None:
        import capo_amplifybackend.types.service

        out["service"] = capo_amplifybackend.types.service.deserialize_json(
            data["service"]
        )
    if data.get("userPoolConfigs") is not None:
        import capo_amplifybackend.types.create_backend_auth_user_pool_config

        out["user_pool_configs"] = (
            capo_amplifybackend.types.create_backend_auth_user_pool_config.deserialize_json(
                data["userPoolConfigs"]
            )
        )
    return out


def redact_sensitive(value: CreateBackendAuthResourceConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_pool_configs" in value:
        import capo_amplifybackend.types.create_backend_auth_user_pool_config

        out["user_pool_configs"] = (
            capo_amplifybackend.types.create_backend_auth_user_pool_config.redact_sensitive(
                value["user_pool_configs"]
            )
        )
    return out
