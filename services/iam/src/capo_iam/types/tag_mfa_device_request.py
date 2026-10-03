"""Generated from Smithy shape ``com.amazonaws.iam#TagMFADeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.serial_number_type
    import capo_iam.types.tag_list_type


class TagMFADeviceRequest(TypedDict, closed=True):
    serial_number: "capo_iam.types.serial_number_type.serialNumberType"
    """<p>The unique identifier for the IAM virtual MFA device to which you want to add tags. For virtual MFA devices, the serial number is the same as the ARN.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tags: "capo_iam.types.tag_list_type.tagListType"
    """<p>The list of tags that you want to attach to the IAM virtual MFA device. Each tag consists of a key name and an associated value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SerialNumber", str(value["serial_number"])))
    import capo_iam.types.tag_list_type

    capo_iam.types.tag_list_type.serialize_query(
        value["tags"], pairs, f"{key_prefix}Tags"
    )


def deserialize_query(el: Element) -> TagMFADeviceRequest:
    out: TagMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("TagMFADeviceRequest.serial_number required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_iam.types.tag_list_type

        out["tags"] = capo_iam.types.tag_list_type.deserialize_query(child_tags)
    else:
        raise DeserializationError("TagMFADeviceRequest.tags required")
    return out
