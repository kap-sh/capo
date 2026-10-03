"""Generated from Smithy shape ``com.amazonaws.iam#EnableMFADeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.authentication_code_type
    import capo_iam.types.existing_user_name_type
    import capo_iam.types.serial_number_type


class EnableMFADeviceRequest(TypedDict, closed=True):
    user_name: "capo_iam.types.existing_user_name_type.existingUserNameType"
    """<p>The name of the IAM user for whom you want to enable the MFA device.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    serial_number: "capo_iam.types.serial_number_type.serialNumberType"
    """<p>The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: =,.@:/-</p>"""
    authentication_code1: (
        "capo_iam.types.authentication_code_type.authenticationCodeType"
    )
    """<p>An authentication code emitted by the device. </p> <p>The format for this parameter is a string of six digits.</p> <important> <p>Submit your request immediately after generating the authentication codes. If you generate the codes and then wait too long to submit the request, the MFA device successfully associates with the user but the MFA device becomes out of sync. This happens because time-based one-time passwords (TOTP) expire after a short period of time. If this happens, you can <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_sync.html">resync the device</a>.</p> </important>"""
    authentication_code2: (
        "capo_iam.types.authentication_code_type.authenticationCodeType"
    )
    """<p>A subsequent authentication code emitted by the device.</p> <p>The format for this parameter is a string of six digits.</p> <important> <p>Submit your request immediately after generating the authentication codes. If you generate the codes and then wait too long to submit the request, the MFA device successfully associates with the user but the MFA device becomes out of sync. This happens because time-based one-time passwords (TOTP) expire after a short period of time. If this happens, you can <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_sync.html">resync the device</a>.</p> </important>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableMFADeviceRequest, pairs: list[tuple[str, str]], prefix: str
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


def deserialize_query(el: Element) -> EnableMFADeviceRequest:
    out: EnableMFADeviceRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("EnableMFADeviceRequest.user_name required")
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    else:
        raise DeserializationError("EnableMFADeviceRequest.serial_number required")
    child_authentication_code1 = el.find("AuthenticationCode1")
    if child_authentication_code1 is not None:
        out["authentication_code1"] = str(child_authentication_code1.text or "")
    else:
        raise DeserializationError(
            "EnableMFADeviceRequest.authentication_code1 required"
        )
    child_authentication_code2 = el.find("AuthenticationCode2")
    if child_authentication_code2 is not None:
        out["authentication_code2"] = str(child_authentication_code2.text or "")
    else:
        raise DeserializationError(
            "EnableMFADeviceRequest.authentication_code2 required"
        )
    return out
