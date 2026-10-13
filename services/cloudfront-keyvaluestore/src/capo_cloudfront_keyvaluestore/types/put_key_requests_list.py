"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#PutKeyRequestsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.put_key_request_list_item

PutKeyRequestsList: TypeAlias = list[
    "capo_cloudfront_keyvaluestore.types.put_key_request_list_item.PutKeyRequestListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: PutKeyRequestsList) -> list:
    import capo_cloudfront_keyvaluestore.types.put_key_request_list_item

    out: list = []
    for item in value:
        out.append(
            capo_cloudfront_keyvaluestore.types.put_key_request_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PutKeyRequestsList:
    import capo_cloudfront_keyvaluestore.types.put_key_request_list_item

    out: PutKeyRequestsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudfront_keyvaluestore.types.put_key_request_list_item.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: PutKeyRequestsList) -> list[Any]:
    import capo_cloudfront_keyvaluestore.types.put_key_request_list_item

    return [
        capo_cloudfront_keyvaluestore.types.put_key_request_list_item.redact_sensitive(
            item
        )
        for item in value
    ]
