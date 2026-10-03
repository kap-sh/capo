"""Generated from Smithy shape ``com.amazonaws.iam#UntagMFADeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.serial_number_type
    import capo_iam.types.tag_key_list_type


class UntagMFADeviceRequest(TypedDict, closed=True):
    serial_number: "capo_iam.types.serial_number_type.serialNumberType"
    """<p>The unique identifier for the IAM virtual MFA device from which you want to remove tags. For virtual MFA devices, the serial number is the same as the ARN.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    tag_keys: "capo_iam.types.tag_key_list_type.tagKeyListType"
    """<p>A list of key names as a simple array of strings. The tags with matching keys are removed from the specified instance profile.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SerialNumber", str(value["serial_number"])))
    import capo_iam.types.tag_key_list_type

    capo_iam.types.tag_key_list_type.serialize_query(
        value["tag_keys"], pairs, f"{key_prefix}TagKeys"
    )


def deserialize_query(el: Element) -> UntagMFADeviceRequest:
    out: UntagMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("UntagMFADeviceRequest.serial_number required")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import capo_iam.types.tag_key_list_type

        out["tag_keys"] = capo_iam.types.tag_key_list_type.deserialize_query(
            child_tag_keys
        )
    else:
        raise DeserializationError("UntagMFADeviceRequest.tag_keys required")
    return out
