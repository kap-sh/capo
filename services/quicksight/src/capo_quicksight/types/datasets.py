"""Generated from Smithy shape ``com.amazonaws.quicksight#Datasets``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.dataset_metadata

Datasets: TypeAlias = list["capo_quicksight.types.dataset_metadata.DatasetMetadata"]


# --- restJson1 ser/de ---
def serialize_json(value: Datasets) -> list:
    import capo_quicksight.types.dataset_metadata

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.dataset_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> Datasets:
    import capo_quicksight.types.dataset_metadata

    out: Datasets = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.dataset_metadata.deserialize_json(item))
    return out


def redact_sensitive(value: Datasets) -> list[Any]:
    import capo_quicksight.types.dataset_metadata

    return [
        capo_quicksight.types.dataset_metadata.redact_sensitive(item) for item in value
    ]
