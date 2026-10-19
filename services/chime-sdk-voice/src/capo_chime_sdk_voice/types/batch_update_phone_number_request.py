"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#BatchUpdatePhoneNumberRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.update_phone_number_request_item_list


class BatchUpdatePhoneNumberRequest(TypedDict, closed=True):
    update_phone_number_request_items: "capo_chime_sdk_voice.types.update_phone_number_request_item_list.UpdatePhoneNumberRequestItemList"
    """<p>Lists the phone numbers in the update request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdatePhoneNumberRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.update_phone_number_request_item_list

    out["UpdatePhoneNumberRequestItems"] = (
        capo_chime_sdk_voice.types.update_phone_number_request_item_list.serialize_json(
            value["update_phone_number_request_items"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdatePhoneNumberRequest:
    out: BatchUpdatePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if data.get("UpdatePhoneNumberRequestItems") is not None:
        import capo_chime_sdk_voice.types.update_phone_number_request_item_list

        out["update_phone_number_request_items"] = (
            capo_chime_sdk_voice.types.update_phone_number_request_item_list.deserialize_json(
                data["UpdatePhoneNumberRequestItems"]
            )
        )
    else:
        out["update_phone_number_request_items"] = []
    return out


def redact_sensitive(value: BatchUpdatePhoneNumberRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "update_phone_number_request_items" in value:
        import capo_chime_sdk_voice.types.update_phone_number_request_item_list

        out["update_phone_number_request_items"] = (
            capo_chime_sdk_voice.types.update_phone_number_request_item_list.redact_sensitive(
                value["update_phone_number_request_items"]
            )
        )
    return out
