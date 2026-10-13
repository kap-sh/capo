"""Generated from Smithy shape ``com.amazonaws.sns#ListSMSSandboxPhoneNumbersResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.sms_sandbox_phone_number_list
    import capo_sns.types.string


class ListSMSSandboxPhoneNumbersResult(TypedDict, closed=True):
    phone_numbers: (
        "capo_sns.types.sms_sandbox_phone_number_list.SMSSandboxPhoneNumberList"
    )
    """<p>A list of the calling account's pending and verified phone numbers.</p>"""
    next_token: NotRequired["capo_sns.types.string.String"]
    """<p>A <code>NextToken</code> string is returned when you call the <code>ListSMSSandboxPhoneNumbersInput</code> operation if additional pages of records are available.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListSMSSandboxPhoneNumbersResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_sns.types.sms_sandbox_phone_number_list

    capo_sns.types.sms_sandbox_phone_number_list.serialize_query(
        value["phone_numbers"], pairs, f"{key_prefix}PhoneNumbers"
    )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListSMSSandboxPhoneNumbersResult:
    out: ListSMSSandboxPhoneNumbersResult = {}  # type: ignore[typeddict-item]
    child_phone_numbers = el.find("PhoneNumbers")
    if child_phone_numbers is not None:
        import capo_sns.types.sms_sandbox_phone_number_list

        out["phone_numbers"] = (
            capo_sns.types.sms_sandbox_phone_number_list.deserialize_query(
                child_phone_numbers
            )
        )
    else:
        raise DeserializationError(
            "ListSMSSandboxPhoneNumbersResult.phone_numbers required"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


def redact_sensitive(value: ListSMSSandboxPhoneNumbersResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_numbers" in value:
        import capo_sns.types.sms_sandbox_phone_number_list

        out["phone_numbers"] = (
            capo_sns.types.sms_sandbox_phone_number_list.redact_sensitive(
                value["phone_numbers"]
            )
        )
    return out
