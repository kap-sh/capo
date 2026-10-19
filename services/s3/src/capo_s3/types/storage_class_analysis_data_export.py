"""Generated from Smithy shape ``com.amazonaws.s3#StorageClassAnalysisDataExport``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.analytics_export_destination
    import capo_s3.types.storage_class_analysis_schema_version


class StorageClassAnalysisDataExport(TypedDict, closed=True):
    output_schema_version: "capo_s3.types.storage_class_analysis_schema_version.StorageClassAnalysisSchemaVersion"
    """<p>The version of the output schema to use when exporting data. Must be <code>V_1</code>.</p>"""
    destination: "capo_s3.types.analytics_export_destination.AnalyticsExportDestination"
    """<p>The place to store the data for an analysis.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StorageClassAnalysisDataExport, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.storage_class_analysis_schema_version

    capo_s3.types.storage_class_analysis_schema_version.serialize_xml(
        value["output_schema_version"], el, "OutputSchemaVersion"
    )
    import capo_s3.types.analytics_export_destination

    capo_s3.types.analytics_export_destination.serialize_xml(
        value["destination"], el, "Destination"
    )


def deserialize_xml(el: Element) -> StorageClassAnalysisDataExport:
    out: StorageClassAnalysisDataExport = {}  # type: ignore[typeddict-item]
    child_output_schema_version = el.find("OutputSchemaVersion")
    if child_output_schema_version is not None:
        import capo_s3.types.storage_class_analysis_schema_version

        out["output_schema_version"] = (
            capo_s3.types.storage_class_analysis_schema_version.deserialize_xml(
                child_output_schema_version
            )
        )
    else:
        import typing

        out["output_schema_version"] = typing.cast(
            "capo_s3.types.storage_class_analysis_schema_version.StorageClassAnalysisSchemaVersion",
            "",
        )
    child_destination = el.find("Destination")
    if child_destination is not None:
        import capo_s3.types.analytics_export_destination

        out["destination"] = capo_s3.types.analytics_export_destination.deserialize_xml(
            child_destination
        )
    else:
        raise DeserializationError(
            "StorageClassAnalysisDataExport.destination required"
        )
    return out
