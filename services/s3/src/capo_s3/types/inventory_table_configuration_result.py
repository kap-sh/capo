"""Generated from Smithy shape ``com.amazonaws.s3#InventoryTableConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.error_details
    import capo_s3.types.inventory_configuration_state
    import capo_s3.types.metadata_table_status
    import capo_s3.types.s3_tables_arn
    import capo_s3.types.s3_tables_name


class InventoryTableConfigurationResult(TypedDict, closed=True):
    configuration_state: (
        "capo_s3.types.inventory_configuration_state.InventoryConfigurationState"
    )
    """<p> The configuration state of the inventory table, indicating whether the inventory table is enabled or disabled. </p>"""
    table_status: NotRequired["capo_s3.types.metadata_table_status.MetadataTableStatus"]
    """<p> The status of the inventory table. The status values are: </p> <ul> <li> <p> <code>CREATING</code> - The inventory table is in the process of being created in the specified Amazon Web Services managed table bucket.</p> </li> <li> <p> <code>BACKFILLING</code> - The inventory table is in the process of being backfilled. When you enable the inventory table for your metadata configuration, the table goes through a process known as backfilling, during which Amazon S3 scans your general purpose bucket to retrieve the initial metadata for all objects in the bucket. Depending on the number of objects in your bucket, this process can take several hours. When the backfilling process is finished, the status of your inventory table changes from <code>BACKFILLING</code> to <code>ACTIVE</code>. After backfilling is completed, updates to your objects are reflected in the inventory table within one hour.</p> </li> <li> <p> <code>ACTIVE</code> - The inventory table has been created successfully, and records are being delivered to the table. </p> </li> <li> <p> <code>FAILED</code> - Amazon S3 is unable to create the inventory table, or Amazon S3 is unable to deliver records.</p> </li> </ul>"""
    error: NotRequired["capo_s3.types.error_details.ErrorDetails"]
    table_name: NotRequired["capo_s3.types.s3_tables_name.S3TablesName"]
    """<p> The name of the inventory table. </p>"""
    table_arn: NotRequired["capo_s3.types.s3_tables_arn.S3TablesArn"]
    """<p> The Amazon Resource Name (ARN) for the inventory table. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: InventoryTableConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.inventory_configuration_state

    capo_s3.types.inventory_configuration_state.serialize_xml(
        value["configuration_state"], el, "ConfigurationState"
    )
    if "table_status" in value:
        SubElement(el, "TableStatus").text = str(value["table_status"])
    if "error" in value:
        import capo_s3.types.error_details

        capo_s3.types.error_details.serialize_xml(value["error"], el, "Error")
    if "table_name" in value:
        SubElement(el, "TableName").text = str(value["table_name"])
    if "table_arn" in value:
        SubElement(el, "TableArn").text = str(value["table_arn"])


def deserialize_xml(el: Element) -> InventoryTableConfigurationResult:
    out: InventoryTableConfigurationResult = {}  # type: ignore[typeddict-item]
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
    child_table_status = el.find("TableStatus")
    if child_table_status is not None:
        out["table_status"] = str(child_table_status.text or "")
    child_error = el.find("Error")
    if child_error is not None:
        import capo_s3.types.error_details

        out["error"] = capo_s3.types.error_details.deserialize_xml(child_error)
    child_table_name = el.find("TableName")
    if child_table_name is not None:
        out["table_name"] = str(child_table_name.text or "")
    child_table_arn = el.find("TableArn")
    if child_table_arn is not None:
        out["table_arn"] = str(child_table_arn.text or "")
    return out
