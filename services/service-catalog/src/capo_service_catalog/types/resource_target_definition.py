"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceTargetDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.property_name
    import capo_service_catalog.types.requires_recreation
    import capo_service_catalog.types.resource_attribute


class ResourceTargetDefinition(TypedDict, closed=True):
    attribute: NotRequired[
        "capo_service_catalog.types.resource_attribute.ResourceAttribute"
    ]
    """<p>The attribute to be changed.</p>"""
    name: NotRequired["capo_service_catalog.types.property_name.PropertyName"]
    """<p>If the attribute is <code>Properties</code>, the value is the name of the property. Otherwise, the value is null.</p>"""
    requires_recreation: NotRequired[
        "capo_service_catalog.types.requires_recreation.RequiresRecreation"
    ]
    """<p>If the attribute is <code>Properties</code>, indicates whether a change to this property causes the resource to be re-created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTargetDefinition) -> dict:
    out: dict = {}
    if "attribute" in value:
        import capo_service_catalog.types.resource_attribute

        out["Attribute"] = (
            capo_service_catalog.types.resource_attribute.serialize_aws_json_1_1(
                value["attribute"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "requires_recreation" in value:
        import capo_service_catalog.types.requires_recreation

        out["RequiresRecreation"] = (
            capo_service_catalog.types.requires_recreation.serialize_aws_json_1_1(
                value["requires_recreation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceTargetDefinition:
    out: ResourceTargetDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Attribute") is not None:
        import capo_service_catalog.types.resource_attribute

        out["attribute"] = (
            capo_service_catalog.types.resource_attribute.deserialize_aws_json_1_1(
                data["Attribute"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("RequiresRecreation") is not None:
        import capo_service_catalog.types.requires_recreation

        out["requires_recreation"] = (
            capo_service_catalog.types.requires_recreation.deserialize_aws_json_1_1(
                data["RequiresRecreation"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceTargetDefinition) -> dict:
    out: dict = {}
    if "attribute" in value:
        import capo_service_catalog.types.resource_attribute

        out["Attribute"] = capo_service_catalog.types.resource_attribute.serialize_cbor(
            value["attribute"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "requires_recreation" in value:
        import capo_service_catalog.types.requires_recreation

        out["RequiresRecreation"] = (
            capo_service_catalog.types.requires_recreation.serialize_cbor(
                value["requires_recreation"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ResourceTargetDefinition:
    out: ResourceTargetDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Attribute") is not None:
        import capo_service_catalog.types.resource_attribute

        out["attribute"] = (
            capo_service_catalog.types.resource_attribute.deserialize_cbor(
                data["Attribute"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("RequiresRecreation") is not None:
        import capo_service_catalog.types.requires_recreation

        out["requires_recreation"] = (
            capo_service_catalog.types.requires_recreation.deserialize_cbor(
                data["RequiresRecreation"]
            )
        )
    return out
