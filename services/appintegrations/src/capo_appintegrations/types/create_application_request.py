"""Generated from Smithy shape ``com.amazonaws.appintegrations#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appintegrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appintegrations.types.application_config
    import capo_appintegrations.types.application_name
    import capo_appintegrations.types.application_namespace
    import capo_appintegrations.types.application_source_config
    import capo_appintegrations.types.application_type
    import capo_appintegrations.types.auth_config
    import capo_appintegrations.types.boolean
    import capo_appintegrations.types.description
    import capo_appintegrations.types.idempotency_token
    import capo_appintegrations.types.iframe_config
    import capo_appintegrations.types.initialization_timeout
    import capo_appintegrations.types.permission_list
    import capo_appintegrations.types.publication_list
    import capo_appintegrations.types.subscription_list
    import capo_appintegrations.types.tag_map


class CreateApplicationRequest(TypedDict, closed=True):
    name: "capo_appintegrations.types.application_name.ApplicationName"
    """<p>The name of the application.</p>"""
    namespace: "capo_appintegrations.types.application_namespace.ApplicationNamespace"
    """<p>The namespace of the application.</p>"""
    description: NotRequired["capo_appintegrations.types.description.Description"]
    """<p>The description of the application.</p>"""
    application_source_config: (
        "capo_appintegrations.types.application_source_config.ApplicationSourceConfig"
    )
    """<p>The configuration for where the application should be loaded from.</p>"""
    subscriptions: NotRequired[
        "capo_appintegrations.types.subscription_list.SubscriptionList"
    ]
    """<p>The events that the application subscribes.</p>"""
    publications: NotRequired[
        "capo_appintegrations.types.publication_list.PublicationList"
    ]
    """<p>The events that the application publishes.</p>"""
    client_token: NotRequired[
        "capo_appintegrations.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["capo_appintegrations.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    permissions: NotRequired[
        "capo_appintegrations.types.permission_list.PermissionList"
    ]
    """<p>The configuration of events or requests that the application has access to.</p>"""
    is_service: "capo_appintegrations.types.boolean.Boolean"
    """<p>Indicates whether the application is a service.</p>"""
    initialization_timeout: NotRequired[
        "capo_appintegrations.types.initialization_timeout.InitializationTimeout"
    ]
    """<p>The maximum time in milliseconds allowed to establish a connection with the workspace.</p>"""
    application_config: NotRequired[
        "capo_appintegrations.types.application_config.ApplicationConfig"
    ]
    """<p>The configuration settings for the application.</p>"""
    iframe_config: NotRequired["capo_appintegrations.types.iframe_config.IframeConfig"]
    """<p>The iframe configuration for the application.</p>"""
    application_type: NotRequired[
        "capo_appintegrations.types.application_type.ApplicationType"
    ]
    """<p>The type of application.</p>"""
    auth_config: NotRequired["capo_appintegrations.types.auth_config.AuthConfig"]
    """<p>The authentication settings that Connect Customer uses when calling the external application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Namespace"] = value["namespace"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_appintegrations.types.application_source_config

    out["ApplicationSourceConfig"] = (
        capo_appintegrations.types.application_source_config.serialize_json(
            value["application_source_config"]
        )
    )
    if "subscriptions" in value:
        import capo_appintegrations.types.subscription_list

        out["Subscriptions"] = (
            capo_appintegrations.types.subscription_list.serialize_json(
                value["subscriptions"]
            )
        )
    if "publications" in value:
        import capo_appintegrations.types.publication_list

        out["Publications"] = (
            capo_appintegrations.types.publication_list.serialize_json(
                value["publications"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_appintegrations.types.tag_map

        out["Tags"] = capo_appintegrations.types.tag_map.serialize_json(value["tags"])
    if "permissions" in value:
        import capo_appintegrations.types.permission_list

        out["Permissions"] = capo_appintegrations.types.permission_list.serialize_json(
            value["permissions"]
        )
    out["IsService"] = value.get("is_service", False)
    if "initialization_timeout" in value:
        out["InitializationTimeout"] = value["initialization_timeout"]
    if "application_config" in value:
        import capo_appintegrations.types.application_config

        out["ApplicationConfig"] = (
            capo_appintegrations.types.application_config.serialize_json(
                value["application_config"]
            )
        )
    if "iframe_config" in value:
        import capo_appintegrations.types.iframe_config

        out["IframeConfig"] = capo_appintegrations.types.iframe_config.serialize_json(
            value["iframe_config"]
        )
    if "application_type" in value:
        import capo_appintegrations.types.application_type

        out["ApplicationType"] = (
            capo_appintegrations.types.application_type.serialize_json(
                value["application_type"]
            )
        )
    if "auth_config" in value:
        import capo_appintegrations.types.auth_config

        out["AuthConfig"] = capo_appintegrations.types.auth_config.serialize_json(
            value["auth_config"]
        )
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateApplicationRequest.name required")
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    else:
        raise DeserializationError("CreateApplicationRequest.namespace required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ApplicationSourceConfig") is not None:
        import capo_appintegrations.types.application_source_config

        out["application_source_config"] = (
            capo_appintegrations.types.application_source_config.deserialize_json(
                data["ApplicationSourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateApplicationRequest.application_source_config required"
        )
    if data.get("Subscriptions") is not None:
        import capo_appintegrations.types.subscription_list

        out["subscriptions"] = (
            capo_appintegrations.types.subscription_list.deserialize_json(
                data["Subscriptions"]
            )
        )
    if data.get("Publications") is not None:
        import capo_appintegrations.types.publication_list

        out["publications"] = (
            capo_appintegrations.types.publication_list.deserialize_json(
                data["Publications"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_appintegrations.types.tag_map

        out["tags"] = capo_appintegrations.types.tag_map.deserialize_json(data["Tags"])
    if data.get("Permissions") is not None:
        import capo_appintegrations.types.permission_list

        out["permissions"] = (
            capo_appintegrations.types.permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if data.get("IsService") is not None:
        out["is_service"] = data["IsService"]
    else:
        out["is_service"] = False
    if data.get("InitializationTimeout") is not None:
        out["initialization_timeout"] = data["InitializationTimeout"]
    if data.get("ApplicationConfig") is not None:
        import capo_appintegrations.types.application_config

        out["application_config"] = (
            capo_appintegrations.types.application_config.deserialize_json(
                data["ApplicationConfig"]
            )
        )
    if data.get("IframeConfig") is not None:
        import capo_appintegrations.types.iframe_config

        out["iframe_config"] = (
            capo_appintegrations.types.iframe_config.deserialize_json(
                data["IframeConfig"]
            )
        )
    if data.get("ApplicationType") is not None:
        import capo_appintegrations.types.application_type

        out["application_type"] = (
            capo_appintegrations.types.application_type.deserialize_json(
                data["ApplicationType"]
            )
        )
    if data.get("AuthConfig") is not None:
        import capo_appintegrations.types.auth_config

        out["auth_config"] = capo_appintegrations.types.auth_config.deserialize_json(
            data["AuthConfig"]
        )
    return out
