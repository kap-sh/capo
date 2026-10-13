"""Generated from Smithy shape ``com.amazonaws.sns#VerifySMSSandboxPhoneNumberInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.otp_code
    import capo_sns.types.phone_number_string


class VerifySMSSandboxPhoneNumberInput(TypedDict, closed=True):
    phone_number: "capo_sns.types.phone_number_string.PhoneNumberString"
    """<p>The destination phone number to verify.</p>"""
    one_time_password: "capo_sns.types.otp_code.OTPCode"
    """<p>The OTP sent to the destination number from the <code>CreateSMSSandBoxPhoneNumber</code> call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifySMSSandboxPhoneNumberInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PhoneNumber", str(value["phone_number"])))
    pairs.append((f"{key_prefix}OneTimePassword", str(value["one_time_password"])))


def deserialize_query(el: Element) -> VerifySMSSandboxPhoneNumberInput:
    out: VerifySMSSandboxPhoneNumberInput = {}  # type: ignore[typeddict-item]
    child_phone_number = el.find("PhoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    else:
        raise DeserializationError(
            "VerifySMSSandboxPhoneNumberInput.phone_number required"
        )
    child_one_time_password = el.find("OneTimePassword")
    if child_one_time_password is not None:
        out["one_time_password"] = str(child_one_time_password.text or "")
    else:
        raise DeserializationError(
            "VerifySMSSandboxPhoneNumberInput.one_time_password required"
        )
    return out


def redact_sensitive(value: VerifySMSSandboxPhoneNumberInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    return out
