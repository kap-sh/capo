"""Generated from Smithy shape ``com.amazonaws.sns#OptInPhoneNumberInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.phone_number


class OptInPhoneNumberInput(TypedDict, closed=True):
    phone_number: "capo_sns.types.phone_number.PhoneNumber"
    """<p>The phone number to opt in. Use E.164 format.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptInPhoneNumberInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}phoneNumber", str(value["phone_number"])))


def deserialize_query(el: Element) -> OptInPhoneNumberInput:
    out: OptInPhoneNumberInput = {}  # type: ignore[typeddict-item]
    child_phone_number = el.find("phoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    else:
        out["phone_number"] = ""
    return out


def redact_sensitive(value: OptInPhoneNumberInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    return out
