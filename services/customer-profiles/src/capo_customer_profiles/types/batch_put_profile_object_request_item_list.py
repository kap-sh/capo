"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchPutProfileObjectRequestItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.batch_put_profile_object_request_item

BatchPutProfileObjectRequestItemList: TypeAlias = list[
    "capo_customer_profiles.types.batch_put_profile_object_request_item.BatchPutProfileObjectRequestItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutProfileObjectRequestItemList) -> list:
    import capo_customer_profiles.types.batch_put_profile_object_request_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.batch_put_profile_object_request_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchPutProfileObjectRequestItemList:
    import capo_customer_profiles.types.batch_put_profile_object_request_item

    out: BatchPutProfileObjectRequestItemList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_customer_profiles.types.batch_put_profile_object_request_item.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: BatchPutProfileObjectRequestItemList) -> list[Any]:
    import capo_customer_profiles.types.batch_put_profile_object_request_item

    return [
        capo_customer_profiles.types.batch_put_profile_object_request_item.redact_sensitive(
            item
        )
        for item in value
    ]
