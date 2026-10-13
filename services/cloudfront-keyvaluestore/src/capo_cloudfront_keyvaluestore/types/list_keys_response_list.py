"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#ListKeysResponseList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.list_keys_response_list_item

ListKeysResponseList: TypeAlias = list[
    "capo_cloudfront_keyvaluestore.types.list_keys_response_list_item.ListKeysResponseListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListKeysResponseList) -> list:
    import capo_cloudfront_keyvaluestore.types.list_keys_response_list_item

    out: list = []
    for item in value:
        out.append(
            capo_cloudfront_keyvaluestore.types.list_keys_response_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListKeysResponseList:
    import capo_cloudfront_keyvaluestore.types.list_keys_response_list_item

    out: ListKeysResponseList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudfront_keyvaluestore.types.list_keys_response_list_item.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ListKeysResponseList) -> list[Any]:
    import capo_cloudfront_keyvaluestore.types.list_keys_response_list_item

    return [
        capo_cloudfront_keyvaluestore.types.list_keys_response_list_item.redact_sensitive(
            item
        )
        for item in value
    ]
