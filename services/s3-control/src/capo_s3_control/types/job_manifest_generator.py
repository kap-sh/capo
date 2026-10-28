"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestGenerator``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError, SerializationError
from capo_s3_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_s3_control.types.s3_job_manifest_generator


class JobManifestGeneratorS3JobManifestGeneratorMember(TypedDict, closed=True):
    S3JobManifestGenerator: (
        "capo_s3_control.types.s3_job_manifest_generator.S3JobManifestGenerator"
    )


JobManifestGenerator: TypeAlias = (
    JobManifestGeneratorS3JobManifestGeneratorMember | UnknownUnionMember
)


# --- restXml ser/de ---
def serialize_xml(value: JobManifestGenerator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "$unknown" in value:
        raise SerializationError(
            f"JobManifestGenerator: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "S3JobManifestGenerator" in value:
        import capo_s3_control.types.s3_job_manifest_generator

        capo_s3_control.types.s3_job_manifest_generator.serialize_xml(
            value["S3JobManifestGenerator"], el, "S3JobManifestGenerator"
        )
    else:
        raise SerializationError("JobManifestGenerator: no variant present")


def deserialize_xml(el: Element) -> JobManifestGenerator:
    for child in el:
        if child.tag == "S3JobManifestGenerator":
            import capo_s3_control.types.s3_job_manifest_generator

            return {
                "S3JobManifestGenerator": capo_s3_control.types.s3_job_manifest_generator.deserialize_xml(
                    child
                )
            }
        else:
            return {"$unknown": {"name": child.tag}}
    raise DeserializationError("JobManifestGenerator: no recognized variant element")
