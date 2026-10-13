"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketInventoryConfigurationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.inventory_configuration


class GetBucketInventoryConfigurationOutput(TypedDict, closed=True):
    inventory_configuration: NotRequired[
        "capo_s3.types.inventory_configuration.InventoryConfiguration"
    ]
    """<p>Specifies the inventory configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketInventoryConfigurationOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "inventory_configuration" in value:
        import capo_s3.types.inventory_configuration

        capo_s3.types.inventory_configuration.serialize_xml(
            value["inventory_configuration"], el, "InventoryConfiguration"
        )


def deserialize_xml(el: Element) -> GetBucketInventoryConfigurationOutput:
    out: GetBucketInventoryConfigurationOutput = {}  # type: ignore[typeddict-item]
    child_inventory_configuration = el.find("InventoryConfiguration")
    if child_inventory_configuration is not None:
        import capo_s3.types.inventory_configuration

        out["inventory_configuration"] = (
            capo_s3.types.inventory_configuration.deserialize_xml(
                child_inventory_configuration
            )
        )
    return out


def redact_sensitive(value: GetBucketInventoryConfigurationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inventory_configuration" in value:
        import capo_s3.types.inventory_configuration

        out["inventory_configuration"] = (
            capo_s3.types.inventory_configuration.redact_sensitive(
                value["inventory_configuration"]
            )
        )
    return out
