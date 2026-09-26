"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#CreateScopeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.scope_configuration
    import capo_network_security_manager.types.scope_name
    import capo_network_security_manager.types.tag_map


class CreateScopeInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""
    scope_name: "capo_network_security_manager.types.scope_name.ScopeName"
    """<p>The name of the scope.</p>"""
    scope_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the scope.</p>"""
    scope_configuration: (
        "capo_network_security_manager.types.scope_configuration.ScopeConfiguration"
    )
    """<p>The configuration that defines which accounts and resources are in scope.</p>"""
    is_published: "capo_network_security_manager.types.is_published.IsPublished"
    """<p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>"""
    tags: NotRequired["capo_network_security_manager.types.tag_map.TagMap"]
    """<p>The tags to add to the resource when it is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScopeInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["scopeName"] = value["scope_name"]
    if "scope_description" in value:
        out["scopeDescription"] = value["scope_description"]
    import capo_network_security_manager.types.scope_configuration

    out["scopeConfiguration"] = (
        capo_network_security_manager.types.scope_configuration.serialize_json(
            value["scope_configuration"]
        )
    )
    out["isPublished"] = value.get("is_published", True)
    if "tags" in value:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateScopeInput:
    out: CreateScopeInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("scopeName") is not None:
        out["scope_name"] = data["scopeName"]
    else:
        raise DeserializationError("CreateScopeInput.scope_name required")
    if data.get("scopeDescription") is not None:
        out["scope_description"] = data["scopeDescription"]
    if data.get("scopeConfiguration") is not None:
        import capo_network_security_manager.types.scope_configuration

        out["scope_configuration"] = (
            capo_network_security_manager.types.scope_configuration.deserialize_json(
                data["scopeConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreateScopeInput.scope_configuration required")
    if data.get("isPublished") is not None:
        out["is_published"] = data["isPublished"]
    else:
        out["is_published"] = True
    if data.get("tags") is not None:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
