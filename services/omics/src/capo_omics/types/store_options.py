"""Generated from Smithy shape ``com.amazonaws.omics#StoreOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, SerializationError
from capo_omics.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_omics.types.tsv_store_options


class _StoreOptions_tsvStoreOptions(TypedDict, closed=True):
    tsvStoreOptions: "capo_omics.types.tsv_store_options.TsvStoreOptions"


StoreOptions: TypeAlias = _StoreOptions_tsvStoreOptions | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: StoreOptions) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"StoreOptions: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "tsvStoreOptions" in value:
        import capo_omics.types.tsv_store_options

        return {
            "tsvStoreOptions": capo_omics.types.tsv_store_options.serialize_json(
                value["tsvStoreOptions"]
            )
        }
    else:
        raise SerializationError("StoreOptions: no variant present")


def deserialize_json(data: dict) -> StoreOptions:
    if data.get("tsvStoreOptions") is not None:
        import capo_omics.types.tsv_store_options

        return {
            "tsvStoreOptions": capo_omics.types.tsv_store_options.deserialize_json(
                data["tsvStoreOptions"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("StoreOptions: no recognized variant key")
