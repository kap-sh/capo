"""Generated from Smithy shape ``com.amazonaws.s3control#S3ComputeObjectChecksumOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.compute_object_checksum_algorithm
    import capo_s3_control.types.compute_object_checksum_type


class S3ComputeObjectChecksumOperation(TypedDict, closed=True):
    checksum_algorithm: NotRequired[
        "capo_s3_control.types.compute_object_checksum_algorithm.ComputeObjectChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm that you want Amazon S3 to use to create the checksum. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the Amazon S3 User Guide.</p>"""
    checksum_type: NotRequired[
        "capo_s3_control.types.compute_object_checksum_type.ComputeObjectChecksumType"
    ]
    """<p>Indicates the checksum type that you want Amazon S3 to use to calculate the object's checksum value. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the Amazon S3 User Guide.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: S3ComputeObjectChecksumOperation, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "checksum_algorithm" in value:
        import capo_s3_control.types.compute_object_checksum_algorithm

        capo_s3_control.types.compute_object_checksum_algorithm.serialize_xml(
            value["checksum_algorithm"], el, "ChecksumAlgorithm"
        )
    if "checksum_type" in value:
        import capo_s3_control.types.compute_object_checksum_type

        capo_s3_control.types.compute_object_checksum_type.serialize_xml(
            value["checksum_type"], el, "ChecksumType"
        )


def deserialize_xml(el: Element) -> S3ComputeObjectChecksumOperation:
    out: S3ComputeObjectChecksumOperation = {}  # type: ignore[typeddict-item]
    child_checksum_algorithm = el.find("ChecksumAlgorithm")
    if child_checksum_algorithm is not None:
        import capo_s3_control.types.compute_object_checksum_algorithm

        out["checksum_algorithm"] = (
            capo_s3_control.types.compute_object_checksum_algorithm.deserialize_xml(
                child_checksum_algorithm
            )
        )
    child_checksum_type = el.find("ChecksumType")
    if child_checksum_type is not None:
        import capo_s3_control.types.compute_object_checksum_type

        out["checksum_type"] = (
            capo_s3_control.types.compute_object_checksum_type.deserialize_xml(
                child_checksum_type
            )
        )
    return out
