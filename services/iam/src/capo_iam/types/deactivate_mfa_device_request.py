"""Generated from Smithy shape ``com.amazonaws.iam#DeactivateMFADeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.existing_user_name_type
    import capo_iam.types.serial_number_type


class DeactivateMFADeviceRequest(TypedDict, closed=True):
    user_name: NotRequired[
        "capo_iam.types.existing_user_name_type.existingUserNameType"
    ]
    """<p>The name of the user whose MFA device you want to deactivate.</p> <p>This parameter is optional. If no user name is included, it defaults to the principal making the request. When you make this request with root user credentials, you must use an <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html">AssumeRoot</a> session to omit the user name.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    serial_number: "capo_iam.types.serial_number_type.serialNumberType"
    """<p>The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeactivateMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}SerialNumber", str(value["serial_number"])))


def deserialize_query(el: Element) -> DeactivateMFADeviceRequest:
    out: DeactivateMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("DeactivateMFADeviceRequest.serial_number required")
    return out
