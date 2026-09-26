"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.arn
    import capo_network_security_manager.types.service_resource_type


class ResourceAssociation(TypedDict, closed=True):
    arn: "capo_network_security_manager.types.arn.Arn"
    """<p>The ARN of the associated resource.</p>"""
    resource_type: (
        "capo_network_security_manager.types.service_resource_type.ServiceResourceType"
    )
    """<p>The type of the associated resource, such as <code>Policy</code>, <code>Template</code>, or <code>Deployment</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceAssociation) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_network_security_manager.types.service_resource_type

    out["resourceType"] = (
        capo_network_security_manager.types.service_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> ResourceAssociation:
    out: ResourceAssociation = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ResourceAssociation.arn required")
    if data.get("resourceType") is not None:
        import capo_network_security_manager.types.service_resource_type

        out["resource_type"] = (
            capo_network_security_manager.types.service_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError("ResourceAssociation.resource_type required")
    return out
