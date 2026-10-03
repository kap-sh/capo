"""Generated from Smithy shape ``com.amazonaws.iam#ResyncMFADeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.authentication_code_type
    import capo_iam.types.existing_user_name_type
    import capo_iam.types.serial_number_type


class ResyncMFADeviceRequest(TypedDict, closed=True):
    user_name: "capo_iam.types.existing_user_name_type.existingUserNameType"
    """<p>The name of the user whose MFA device you want to resynchronize.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    serial_number: "capo_iam.types.serial_number_type.serialNumberType"
    """<p>Serial number that uniquely identifies the MFA device.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    authentication_code1: (
        "capo_iam.types.authentication_code_type.authenticationCodeType"
    )
    """<p>An authentication code emitted by the device.</p> <p>The format for this parameter is a sequence of six digits.</p>"""
    authentication_code2: (
        "capo_iam.types.authentication_code_type.authenticationCodeType"
    )
    """<p>A subsequent authentication code emitted by the device.</p> <p>The format for this parameter is a sequence of six digits.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResyncMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}UserName", str(value["user_name"])))
    pairs.append((f"{key_prefix}SerialNumber", str(value["serial_number"])))
    pairs.append(
        (f"{key_prefix}AuthenticationCode1", str(value["authentication_code1"]))
    )
    pairs.append(
        (f"{key_prefix}AuthenticationCode2", str(value["authentication_code2"]))
    )


def deserialize_query(el: Element) -> ResyncMFADeviceRequest:
    out: ResyncMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("ResyncMFADeviceRequest.user_name required")
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("ResyncMFADeviceRequest.serial_number required")
    child_authentication_code1 = el.find("AuthenticationCode1")
    if child_authentication_code1 is not None:
        out["authentication_code1"] = str(child_authentication_code1.text or "")
    else:
        raise DeserializationError(
            "ResyncMFADeviceRequest.authentication_code1 required"
        )
    child_authentication_code2 = el.find("AuthenticationCode2")
    if child_authentication_code2 is not None:
        out["authentication_code2"] = str(child_authentication_code2.text or "")
    else:
        raise DeserializationError(
            "ResyncMFADeviceRequest.authentication_code2 required"
        )
    return out
