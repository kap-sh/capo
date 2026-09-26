"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#UpdateScopeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.scope_configuration
    import capo_network_security_manager.types.scope_identifier
    import capo_network_security_manager.types.update_token


class UpdateScopeInput(TypedDict, closed=True):
    scope_identifier: (
        "capo_network_security_manager.types.scope_identifier.ScopeIdentifier"
    )
    """<p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>"""
    update_token: "capo_network_security_manager.types.update_token.UpdateToken"
    """<p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>"""
    scope_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the scope.</p>"""
    scope_configuration: NotRequired[
        "capo_network_security_manager.types.scope_configuration.ScopeConfiguration"
    ]
    """<p>The configuration that defines which accounts and resources are in scope. If you don't include this member, the scope keeps its existing configuration.</p> <p>A new configuration can change which accounts and resources are selected, but it can't add or remove the account filter itself: a scope created for multi-account use stays multi-account, and a scope created for single-account use stays single-account.</p>"""
    is_published: "capo_network_security_manager.types.is_published.IsPublished"
    """<p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>"""
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScopeInput) -> dict:
    out: dict = {}
    out["updateToken"] = value["update_token"]
    if "scope_description" in value:
        out["scopeDescription"] = value["scope_description"]
    if "scope_configuration" in value:
        import capo_network_security_manager.types.scope_configuration

        out["scopeConfiguration"] = (
            capo_network_security_manager.types.scope_configuration.serialize_json(
                value["scope_configuration"]
            )
        )
    out["isPublished"] = value["is_published"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateScopeInput:
    out: UpdateScopeInput = {}  # type: ignore[typeddict-item]
    if data.get("updateToken") is not None:
        out["update_token"] = data["updateToken"]
    else:
        raise DeserializationError("UpdateScopeInput.update_token required")
    if data.get("scopeDescription") is not None:
        out["scope_description"] = data["scopeDescription"]
    if data.get("scopeConfiguration") is not None:
        import capo_network_security_manager.types.scope_configuration

        out["scope_configuration"] = (
            capo_network_security_manager.types.scope_configuration.deserialize_json(
                data["scopeConfiguration"]
            )
        )
    if data.get("isPublished") is not None:
        out["is_published"] = data["isPublished"]
    else:
        raise DeserializationError("UpdateScopeInput.is_published required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
