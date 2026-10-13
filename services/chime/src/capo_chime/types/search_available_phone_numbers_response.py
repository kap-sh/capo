"""Generated from Smithy shape ``com.amazonaws.chime#SearchAvailablePhoneNumbersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.e164_phone_number_list
    import capo_chime.types.string


class SearchAvailablePhoneNumbersResponse(TypedDict, closed=True):
    e164_phone_numbers: NotRequired[
        "capo_chime.types.e164_phone_number_list.E164PhoneNumberList"
    ]
    """<p>List of phone numbers, in E.164 format.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token used to retrieve the next page of search results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAvailablePhoneNumbersResponse) -> dict:
    out: dict = {}
    if "e164_phone_numbers" in value:
        import capo_chime.types.e164_phone_number_list

        out["E164PhoneNumbers"] = (
            capo_chime.types.e164_phone_number_list.serialize_json(
                value["e164_phone_numbers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchAvailablePhoneNumbersResponse:
    out: SearchAvailablePhoneNumbersResponse = {}  # type: ignore[typeddict-item]
    if data.get("E164PhoneNumbers") is not None:
        import capo_chime.types.e164_phone_number_list

        out["e164_phone_numbers"] = (
            capo_chime.types.e164_phone_number_list.deserialize_json(
                data["E164PhoneNumbers"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: SearchAvailablePhoneNumbersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "e164_phone_numbers" in value:
        import capo_chime.types.e164_phone_number_list

        out["e164_phone_numbers"] = (
            capo_chime.types.e164_phone_number_list.redact_sensitive(
                value["e164_phone_numbers"]
            )
        )
    return out
