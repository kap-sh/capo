"""Generated from Smithy shape ``com.amazonaws.iam#GetMFADeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.serial_number_type
    import capo_iam.types.user_name_type


class GetMFADeviceRequest(TypedDict, closed=True):
    serial_number: "capo_iam.types.serial_number_type.serialNumberType"
    """<p>Serial number that uniquely identifies the MFA device. For this API, we only accept FIDO security key <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">ARNs</a>.</p>"""
    user_name: NotRequired["capo_iam.types.user_name_type.userNameType"]
    """<p>The friendly name identifying the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SerialNumber", str(value["serial_number"])))
    if "user_name" in value:
        pairs.append((f"{key_prefix}UserName", str(value["user_name"])))


def deserialize_query(el: Element) -> GetMFADeviceRequest:
    out: GetMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("GetMFADeviceRequest.serial_number required")
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    return out
