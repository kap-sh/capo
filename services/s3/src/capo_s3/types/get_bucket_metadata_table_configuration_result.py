"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketMetadataTableConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.error_details
    import capo_s3.types.metadata_table_configuration_result
    import capo_s3.types.metadata_table_status


class GetBucketMetadataTableConfigurationResult(TypedDict, closed=True):
    metadata_table_configuration_result: "capo_s3.types.metadata_table_configuration_result.MetadataTableConfigurationResult"
    """<p> The V1 S3 Metadata configuration for a general purpose bucket. </p>"""
    status: "capo_s3.types.metadata_table_status.MetadataTableStatus"
    """<p> The status of the metadata table. The status values are: </p> <ul> <li> <p> <code>CREATING</code> - The metadata table is in the process of being created in the specified table bucket.</p> </li> <li> <p> <code>ACTIVE</code> - The metadata table has been created successfully, and records are being delivered to the table. </p> </li> <li> <p> <code>FAILED</code> - Amazon S3 is unable to create the metadata table, or Amazon S3 is unable to deliver records. See <code>ErrorDetails</code> for details.</p> </li> </ul>"""
    error: NotRequired["capo_s3.types.error_details.ErrorDetails"]
    """<p> If the <code>CreateBucketMetadataTableConfiguration</code> request succeeds, but S3 Metadata was unable to create the table, this structure contains the error code and error message. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketMetadataTableConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.metadata_table_configuration_result

    capo_s3.types.metadata_table_configuration_result.serialize_xml(
        value["metadata_table_configuration_result"],
        el,
        "MetadataTableConfigurationResult",
    )
    SubElement(el, "Status").text = str(value["status"])
    if "error" in value:
        import capo_s3.types.error_details

        capo_s3.types.error_details.serialize_xml(value["error"], el, "Error")


def deserialize_xml(el: Element) -> GetBucketMetadataTableConfigurationResult:
    out: GetBucketMetadataTableConfigurationResult = {}  # type: ignore[typeddict-item]
    child_metadata_table_configuration_result = el.find(
        "MetadataTableConfigurationResult"
    )
    if child_metadata_table_configuration_result is not None:
        import capo_s3.types.metadata_table_configuration_result

        out["metadata_table_configuration_result"] = (
            capo_s3.types.metadata_table_configuration_result.deserialize_xml(
                child_metadata_table_configuration_result
            )
        )
    else:
        raise DeserializationError(
            "GetBucketMetadataTableConfigurationResult.metadata_table_configuration_result required"
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        out["status"] = ""
    child_error = el.find("Error")
    if child_error is not None:
        import capo_s3.types.error_details

        out["error"] = capo_s3.types.error_details.deserialize_xml(child_error)
    return out
