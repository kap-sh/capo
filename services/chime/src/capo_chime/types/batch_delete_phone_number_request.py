"""Generated from Smithy shape ``com.amazonaws.chime#BatchDeletePhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string_list


class BatchDeletePhoneNumberRequest(TypedDict, closed=True):
    phone_number_ids: "capo_chime.types.non_empty_string_list.NonEmptyStringList"
    """<p>List of phone number IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeletePhoneNumberRequest) -> dict:
    out: dict = {}
    import capo_chime.types.non_empty_string_list

    out["PhoneNumberIds"] = capo_chime.types.non_empty_string_list.serialize_json(
        value["phone_number_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeletePhoneNumberRequest:
    out: BatchDeletePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberIds") is not None:
        import capo_chime.types.non_empty_string_list

        out["phone_number_ids"] = (
            capo_chime.types.non_empty_string_list.deserialize_json(
                data["PhoneNumberIds"]
            )
        )
    else:
        out["phone_number_ids"] = []
    return out
