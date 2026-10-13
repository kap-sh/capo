"""Generated from Smithy shape ``com.amazonaws.sns#CheckIfPhoneNumberIsOptedOutInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.phone_number


class CheckIfPhoneNumberIsOptedOutInput(TypedDict, closed=True):
    phone_number: "capo_sns.types.phone_number.PhoneNumber"
    """<p>The phone number for which you want to check the opt out status.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CheckIfPhoneNumberIsOptedOutInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}phoneNumber", str(value["phone_number"])))


def deserialize_query(el: Element) -> CheckIfPhoneNumberIsOptedOutInput:
    out: CheckIfPhoneNumberIsOptedOutInput = {}  # type: ignore[typeddict-item]
    child_phone_number = el.find("phoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    else:
        raise DeserializationError(
            "CheckIfPhoneNumberIsOptedOutInput.phone_number required"
        )
    return out


def redact_sensitive(value: CheckIfPhoneNumberIsOptedOutInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    return out
