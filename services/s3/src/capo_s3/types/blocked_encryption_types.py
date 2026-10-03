"""Generated from Smithy shape ``com.amazonaws.s3#BlockedEncryptionTypes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.encryption_type_list


class BlockedEncryptionTypes(TypedDict, closed=True):
    encryption_type: NotRequired[
        "capo_s3.types.encryption_type_list.EncryptionTypeList"
    ]
    """<p>The object encryption type that you want to block or unblock for an Amazon S3 general purpose bucket.</p> <note> <p>Currently, this parameter only supports blocking or unblocking server side encryption with customer-provided keys (SSE-C). For more information about SSE-C, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html">Using server-side encryption with customer-provided keys (SSE-C)</a>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: BlockedEncryptionTypes, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "encryption_type" in value:
        import capo_s3.types.encryption_type_list

        capo_s3.types.encryption_type_list.serialize_xml_flat(
            value["encryption_type"], el, "EncryptionType"
        )


def deserialize_xml(el: Element) -> BlockedEncryptionTypes:
    out: BlockedEncryptionTypes = {}  # type: ignore[typeddict-item]
    if el.find("EncryptionType") is not None:
        import capo_s3.types.encryption_type_list

        out["encryption_type"] = (
            capo_s3.types.encryption_type_list.deserialize_xml_flat(
                el, "EncryptionType"
            )
        )
    return out
