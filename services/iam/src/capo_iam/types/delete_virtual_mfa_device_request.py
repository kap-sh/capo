"""Generated from Smithy shape ``com.amazonaws.iam#DeleteVirtualMFADeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.serial_number_type


class DeleteVirtualMFADeviceRequest(TypedDict, closed=True):
    serial_number: "capo_iam.types.serial_number_type.serialNumberType"
    """<p>The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the same as the ARN.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteVirtualMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SerialNumber", str(value["serial_number"])))


def deserialize_query(el: Element) -> DeleteVirtualMFADeviceRequest:
    out: DeleteVirtualMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError(
            "DeleteVirtualMFADeviceRequest.serial_number required"
        )
    return out
