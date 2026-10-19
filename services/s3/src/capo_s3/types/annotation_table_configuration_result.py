"""Generated from Smithy shape ``com.amazonaws.s3#AnnotationTableConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.annotation_configuration_state
    import capo_s3.types.error_details
    import capo_s3.types.metadata_table_status
    import capo_s3.types.role
    import capo_s3.types.s3_tables_arn
    import capo_s3.types.s3_tables_name


class AnnotationTableConfigurationResult(TypedDict, closed=True):
    configuration_state: (
        "capo_s3.types.annotation_configuration_state.AnnotationConfigurationState"
    )
    """<p>The current configuration state of the annotation table.</p>"""
    table_status: NotRequired["capo_s3.types.metadata_table_status.MetadataTableStatus"]
    """<p>The provisioning status of the annotation table. Possible values: <code>CREATING</code>, <code>BACKFILLING</code>, <code>ACTIVE</code>, <code>FAILED</code>.</p>"""
    error: NotRequired["capo_s3.types.error_details.ErrorDetails"]
    table_name: NotRequired["capo_s3.types.s3_tables_name.S3TablesName"]
    """<p>The name of the annotation table.</p>"""
    table_arn: NotRequired["capo_s3.types.s3_tables_arn.S3TablesArn"]
    """<p>The ARN of the annotation table.</p>"""
    role: NotRequired["capo_s3.types.role.Role"]
    """<p>The ARN of the IAM role associated with the annotation table.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AnnotationTableConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.annotation_configuration_state

    capo_s3.types.annotation_configuration_state.serialize_xml(
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
    if "role" in value:
        SubElement(el, "Role").text = str(value["role"])


def deserialize_xml(el: Element) -> AnnotationTableConfigurationResult:
    out: AnnotationTableConfigurationResult = {}  # type: ignore[typeddict-item]
    child_configuration_state = el.find("ConfigurationState")
    if child_configuration_state is not None:
        import capo_s3.types.annotation_configuration_state

        out["configuration_state"] = (
            capo_s3.types.annotation_configuration_state.deserialize_xml(
                child_configuration_state
            )
        )
    else:
        import typing

        out["configuration_state"] = typing.cast(
            "capo_s3.types.annotation_configuration_state.AnnotationConfigurationState",
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
    child_role = el.find("Role")
    if child_role is not None:
        out["role"] = str(child_role.text or "")
    return out
