"""Generated from Smithy shape ``com.amazonaws.kms#CustomKeyStoresList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.custom_key_stores_list_entry

CustomKeyStoresList: TypeAlias = list[
    "capo_kms.types.custom_key_stores_list_entry.CustomKeyStoresListEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomKeyStoresList) -> list:
    import capo_kms.types.custom_key_stores_list_entry

    out: list = []
    for item in value:
        out.append(
            capo_kms.types.custom_key_stores_list_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomKeyStoresList:
    import capo_kms.types.custom_key_stores_list_entry

    out: CustomKeyStoresList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kms.types.custom_key_stores_list_entry.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: CustomKeyStoresList) -> list[Any]:
    import capo_kms.types.custom_key_stores_list_entry

    return [
        capo_kms.types.custom_key_stores_list_entry.redact_sensitive(item)
        for item in value
    ]
