"""Generated from Smithy shape ``com.amazonaws.sns#ListOriginationNumbersResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.next_token
    import capo_sns.types.phone_number_information_list


class ListOriginationNumbersResult(TypedDict, closed=True):
    next_token: NotRequired["capo_sns.types.next_token.nextToken"]
    """<p>A <code>NextToken</code> string is returned when you call the <code>ListOriginationNumbers</code> operation if additional pages of records are available.</p>"""
    phone_numbers: NotRequired[
        "capo_sns.types.phone_number_information_list.PhoneNumberInformationList"
    ]
    """<p>A list of the calling account's verified and pending origination numbers.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListOriginationNumbersResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "phone_numbers" in value:
        import capo_sns.types.phone_number_information_list

        capo_sns.types.phone_number_information_list.serialize_query(
            value["phone_numbers"], pairs, f"{key_prefix}PhoneNumbers"
        )


def deserialize_query(el: Element) -> ListOriginationNumbersResult:
    out: ListOriginationNumbersResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_phone_numbers = el.find("PhoneNumbers")
    if child_phone_numbers is not None:
        import capo_sns.types.phone_number_information_list

        out["phone_numbers"] = (
            capo_sns.types.phone_number_information_list.deserialize_query(
                child_phone_numbers
            )
        )
    return out


def redact_sensitive(value: ListOriginationNumbersResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_numbers" in value:
        import capo_sns.types.phone_number_information_list

        out["phone_numbers"] = (
            capo_sns.types.phone_number_information_list.redact_sensitive(
                value["phone_numbers"]
            )
        )
    return out
