"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.job_manifest_field_list
    import capo_s3_control.types.job_manifest_format


class JobManifestSpec(TypedDict, closed=True):
    format: "capo_s3_control.types.job_manifest_format.JobManifestFormat"
    """<p>Indicates which of the available formats the specified manifest uses.</p>"""
    fields: NotRequired[
        "capo_s3_control.types.job_manifest_field_list.JobManifestFieldList"
    ]
    """<p>If the specified manifest object is in the <code>S3BatchOperations_CSV_20180820</code> format, this element describes which columns contain the required data.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobManifestSpec, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.job_manifest_format

    capo_s3_control.types.job_manifest_format.serialize_xml(
        value["format"], el, "Format"
    )
    if "fields" in value:
        import capo_s3_control.types.job_manifest_field_list

        capo_s3_control.types.job_manifest_field_list.serialize_xml(
            value["fields"], el, "Fields"
        )


def deserialize_xml(el: Element) -> JobManifestSpec:
    out: JobManifestSpec = {}  # type: ignore[typeddict-item]
    child_format = el.find("Format")
    if child_format is not None:
        import capo_s3_control.types.job_manifest_format

        out["format"] = capo_s3_control.types.job_manifest_format.deserialize_xml(
            child_format
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_s3_control.types.job_manifest_format.JobManifestFormat", ""
        )
    child_fields = el.find("Fields")
    if child_fields is not None:
        import capo_s3_control.types.job_manifest_field_list

        out["fields"] = capo_s3_control.types.job_manifest_field_list.deserialize_xml(
            child_fields
        )
    return out
