"""Generated from Smithy shape ``com.amazonaws.s3#InventoryTableConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.inventory_configuration_state
    import capo_s3.types.metadata_table_encryption_configuration


class InventoryTableConfiguration(TypedDict, closed=True):
    configuration_state: (
        "capo_s3.types.inventory_configuration_state.InventoryConfigurationState"
    )
    """<p> The configuration state of the inventory table, indicating whether the inventory table is enabled or disabled. </p>"""
    encryption_configuration: NotRequired[
        "capo_s3.types.metadata_table_encryption_configuration.MetadataTableEncryptionConfiguration"
    ]
    """<p> The encryption configuration for the inventory table. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: InventoryTableConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.inventory_configuration_state

    capo_s3.types.inventory_configuration_state.serialize_xml(
        value["configuration_state"], el, "ConfigurationState"
    )
    if "encryption_configuration" in value:
        import capo_s3.types.metadata_table_encryption_configuration

        capo_s3.types.metadata_table_encryption_configuration.serialize_xml(
            value["encryption_configuration"], el, "EncryptionConfiguration"
        )


def deserialize_xml(el: Element) -> InventoryTableConfiguration:
    out: InventoryTableConfiguration = {}  # type: ignore[typeddict-item]
    child_configuration_state = el.find("ConfigurationState")
    if child_configuration_state is not None:
        import capo_s3.types.inventory_configuration_state

        out["configuration_state"] = (
            capo_s3.types.inventory_configuration_state.deserialize_xml(
                child_configuration_state
            )
        )
    else:
        import typing

        out["configuration_state"] = typing.cast(
            "capo_s3.types.inventory_configuration_state.InventoryConfigurationState",
            "",
        )
    child_encryption_configuration = el.find("EncryptionConfiguration")
    if child_encryption_configuration is not None:
        import capo_s3.types.metadata_table_encryption_configuration

        out["encryption_configuration"] = (
            capo_s3.types.metadata_table_encryption_configuration.deserialize_xml(
                child_encryption_configuration
            )
        )
    return out
