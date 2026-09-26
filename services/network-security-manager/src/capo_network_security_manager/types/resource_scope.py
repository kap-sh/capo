"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.resource_set


class ResourceScope(TypedDict, closed=True):
    include_all: NotRequired["bool"]
    """<p>Includes all resources of the resource type.</p>"""
    include: NotRequired["capo_network_security_manager.types.resource_set.ResourceSet"]
    """<p>Includes the resources that match the specified criteria or explicit ARNs.</p>"""
    exclude: NotRequired["capo_network_security_manager.types.resource_set.ResourceSet"]
    """<p>Excludes the resources that match the specified criteria or explicit ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceScope) -> dict:
    out: dict = {}
    if "include_all" in value:
        out["includeAll"] = value["include_all"]
    if "include" in value:
        import capo_network_security_manager.types.resource_set

        out["include"] = (
            capo_network_security_manager.types.resource_set.serialize_json(
                value["include"]
            )
        )
    if "exclude" in value:
        import capo_network_security_manager.types.resource_set

        out["exclude"] = (
            capo_network_security_manager.types.resource_set.serialize_json(
                value["exclude"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceScope:
    out: ResourceScope = {}  # type: ignore[typeddict-item]
    if data.get("includeAll") is not None:
        out["include_all"] = data["includeAll"]
    if data.get("include") is not None:
        import capo_network_security_manager.types.resource_set

        out["include"] = (
            capo_network_security_manager.types.resource_set.deserialize_json(
                data["include"]
            )
        )
    if data.get("exclude") is not None:
        import capo_network_security_manager.types.resource_set

        out["exclude"] = (
            capo_network_security_manager.types.resource_set.deserialize_json(
                data["exclude"]
            )
        )
    return out
