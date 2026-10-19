"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#Dataset``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.dataset_input_config
    import capo_cleanroomsml.types.dataset_type


class Dataset(TypedDict, closed=True):
    type: "capo_cleanroomsml.types.dataset_type.DatasetType"
    """<p>What type of information is found in the dataset.</p>"""
    input_config: "capo_cleanroomsml.types.dataset_input_config.DatasetInputConfig"
    """<p>A DatasetInputConfig object that defines the data source and schema mapping.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dataset) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.dataset_type

    out["type"] = capo_cleanroomsml.types.dataset_type.serialize_json(value["type"])
    import capo_cleanroomsml.types.dataset_input_config

    out["inputConfig"] = capo_cleanroomsml.types.dataset_input_config.serialize_json(
        value["input_config"]
    )
    return out


def deserialize_json(data: dict) -> Dataset:
    out: Dataset = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_cleanroomsml.types.dataset_type

        out["type"] = capo_cleanroomsml.types.dataset_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanroomsml.types.dataset_type.DatasetType", ""
        )
    if data.get("inputConfig") is not None:
        import capo_cleanroomsml.types.dataset_input_config

        out["input_config"] = (
            capo_cleanroomsml.types.dataset_input_config.deserialize_json(
                data["inputConfig"]
            )
        )
    else:
        raise DeserializationError("Dataset.input_config required")
    return out
