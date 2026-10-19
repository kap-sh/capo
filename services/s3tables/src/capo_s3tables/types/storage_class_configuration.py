"""Generated from Smithy shape ``com.amazonaws.s3tables#StorageClassConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.storage_class


class StorageClassConfiguration(TypedDict, closed=True):
    storage_class: "capo_s3tables.types.storage_class.StorageClass"
    """<p>The storage class for the table or table bucket. Valid values include storage classes optimized for different access patterns and cost profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageClassConfiguration) -> dict:
    out: dict = {}
    import capo_s3tables.types.storage_class

    out["storageClass"] = capo_s3tables.types.storage_class.serialize_json(
        value["storage_class"]
    )
    return out


def deserialize_json(data: dict) -> StorageClassConfiguration:
    out: StorageClassConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageClass") is not None:
        import capo_s3tables.types.storage_class

        out["storage_class"] = capo_s3tables.types.storage_class.deserialize_json(
            data["storageClass"]
        )
    else:
        import typing

        out["storage_class"] = typing.cast(
            "capo_s3tables.types.storage_class.StorageClass", ""
        )
    return out
