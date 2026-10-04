"""Generated from Smithy shape ``com.amazonaws.identitystore#IdentityStores``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store

IdentityStores: TypeAlias = list[
    "capo_identitystore.types.identity_store.IdentityStore"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityStores) -> list:
    import capo_identitystore.types.identity_store

    out: list = []
    for item in value:
        out.append(capo_identitystore.types.identity_store.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IdentityStores:
    import capo_identitystore.types.identity_store

    out: IdentityStores = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_identitystore.types.identity_store.deserialize_aws_json_1_1(item)
        )
    return out
