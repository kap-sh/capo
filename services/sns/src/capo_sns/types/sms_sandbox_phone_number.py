"""Generated from Smithy shape ``com.amazonaws.sns#SMSSandboxPhoneNumber``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.phone_number_string
    import capo_sns.types.sms_sandbox_phone_number_verification_status


class SMSSandboxPhoneNumber(TypedDict, closed=True):
    phone_number: NotRequired["capo_sns.types.phone_number_string.PhoneNumberString"]
    """<p>The destination phone number.</p>"""
    status: NotRequired[
        "capo_sns.types.sms_sandbox_phone_number_verification_status.SMSSandboxPhoneNumberVerificationStatus"
    ]
    """<p>The destination phone number's verification status.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SMSSandboxPhoneNumber, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "phone_number" in value:
        pairs.append((f"{key_prefix}PhoneNumber", str(value["phone_number"])))
    if "status" in value:
        import capo_sns.types.sms_sandbox_phone_number_verification_status

        capo_sns.types.sms_sandbox_phone_number_verification_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_query(el: Element) -> SMSSandboxPhoneNumber:
    out: SMSSandboxPhoneNumber = {}  # type: ignore[typeddict-item]
    child_phone_number = el.find("PhoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_sns.types.sms_sandbox_phone_number_verification_status

        out["status"] = (
            capo_sns.types.sms_sandbox_phone_number_verification_status.deserialize_query(
                child_status
            )
        )
    return out


def redact_sensitive(value: SMSSandboxPhoneNumber) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    return out
