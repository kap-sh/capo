"""Generated from Smithy shape ``com.amazonaws.sns#DeleteSMSSandboxPhoneNumberInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.phone_number_string


class DeleteSMSSandboxPhoneNumberInput(TypedDict, closed=True):
    phone_number: "capo_sns.types.phone_number_string.PhoneNumberString"
    """<p>The destination phone number to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSMSSandboxPhoneNumberInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}PhoneNumber", str(value["phone_number"])))


def deserialize_query(el: Element) -> DeleteSMSSandboxPhoneNumberInput:
    out: DeleteSMSSandboxPhoneNumberInput = {}  # type: ignore[typeddict-item]
    child_phone_number = el.find("PhoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    else:
        out["phone_number"] = ""
    return out


def redact_sensitive(value: DeleteSMSSandboxPhoneNumberInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    return out
