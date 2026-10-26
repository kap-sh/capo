"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegratedResourceInputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.integrated_resource
    import capo_securityagent.types.provider_resource_capabilities


class IntegratedResourceInputItem(TypedDict, closed=True):
    resource: "capo_securityagent.types.integrated_resource.IntegratedResource"
    """<p>The integrated resource to update.</p>"""
    capabilities: NotRequired[
        "capo_securityagent.types.provider_resource_capabilities.ProviderResourceCapabilities"
    ]
    """<p>The capabilities to enable for the integrated resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegratedResourceInputItem) -> dict:
    out: dict = {}
    import capo_securityagent.types.integrated_resource

    out["resource"] = capo_securityagent.types.integrated_resource.serialize_json(
        value["resource"]
    )
    if "capabilities" in value:
        import capo_securityagent.types.provider_resource_capabilities

        out["capabilities"] = (
            capo_securityagent.types.provider_resource_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntegratedResourceInputItem:
    out: IntegratedResourceInputItem = {}  # type: ignore[typeddict-item]
    if data.get("resource") is not None:
        import capo_securityagent.types.integrated_resource

        out["resource"] = capo_securityagent.types.integrated_resource.deserialize_json(
            data["resource"]
        )
    else:
        out["resource"] = {"$unknown": {"name": ""}}
    if data.get("capabilities") is not None:
        import capo_securityagent.types.provider_resource_capabilities

        out["capabilities"] = (
            capo_securityagent.types.provider_resource_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    return out
