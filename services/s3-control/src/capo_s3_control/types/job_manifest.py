"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.job_manifest_location
    import capo_s3_control.types.job_manifest_spec


class JobManifest(TypedDict, closed=True):
    spec: "capo_s3_control.types.job_manifest_spec.JobManifestSpec"
    """<p>Describes the format of the specified job's manifest. If the manifest is in CSV format, also describes the columns contained within the manifest.</p>"""
    location: "capo_s3_control.types.job_manifest_location.JobManifestLocation"
    """<p>Contains the information required to locate the specified job's manifest. Manifests can't be imported from directory buckets. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html">Directory buckets</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobManifest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.job_manifest_spec

    capo_s3_control.types.job_manifest_spec.serialize_xml(value["spec"], el, "Spec")
    import capo_s3_control.types.job_manifest_location

    capo_s3_control.types.job_manifest_location.serialize_xml(
        value["location"], el, "Location"
    )


def deserialize_xml(el: Element) -> JobManifest:
    out: JobManifest = {}  # type: ignore[typeddict-item]
    child_spec = el.find("Spec")
    if child_spec is not None:
        import capo_s3_control.types.job_manifest_spec

        out["spec"] = capo_s3_control.types.job_manifest_spec.deserialize_xml(
            child_spec
        )
    else:
        raise DeserializationError("JobManifest.spec required")
    child_location = el.find("Location")
    if child_location is not None:
        import capo_s3_control.types.job_manifest_location

        out["location"] = capo_s3_control.types.job_manifest_location.deserialize_xml(
            child_location
        )
    else:
        raise DeserializationError("JobManifest.location required")
    return out
