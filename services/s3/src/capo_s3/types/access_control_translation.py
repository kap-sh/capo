"""Generated from Smithy shape ``com.amazonaws.s3#AccessControlTranslation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.owner_override


class AccessControlTranslation(TypedDict, closed=True):
    owner: "capo_s3.types.owner_override.OwnerOverride"
    """<p>Specifies the replica ownership. For default and valid values, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTreplication.html">PUT bucket replication</a> in the <i>Amazon S3 API Reference</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AccessControlTranslation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.owner_override

    capo_s3.types.owner_override.serialize_xml(value["owner"], el, "Owner")


def deserialize_xml(el: Element) -> AccessControlTranslation:
    out: AccessControlTranslation = {}  # type: ignore[typeddict-item]
    child_owner = el.find("Owner")
    if child_owner is not None:
        import capo_s3.types.owner_override

        out["owner"] = capo_s3.types.owner_override.deserialize_xml(child_owner)
    else:
        raise DeserializationError("AccessControlTranslation.owner required")
    return out
