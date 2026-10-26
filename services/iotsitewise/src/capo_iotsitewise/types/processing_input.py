"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ProcessingInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError, SerializationError
from capo_iotsitewise.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_item
    import capo_iotsitewise.types.timeseries_list


class _ProcessingInput_timeseries(TypedDict, closed=True):
    timeseries: "capo_iotsitewise.types.timeseries_list.TimeseriesList"


class _ProcessingInput_dataset(TypedDict, closed=True):
    dataset: "capo_iotsitewise.types.dataset_item.DatasetItem"


ProcessingInput: TypeAlias = (
    _ProcessingInput_timeseries | _ProcessingInput_dataset | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProcessingInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProcessingInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "timeseries" in value:
        import capo_iotsitewise.types.timeseries_list

        return {
            "timeseries": capo_iotsitewise.types.timeseries_list.serialize_json(
                value["timeseries"]
            )
        }
    elif "dataset" in value:
        import capo_iotsitewise.types.dataset_item

        return {
            "dataset": capo_iotsitewise.types.dataset_item.serialize_json(
                value["dataset"]
            )
        }
    else:
        raise SerializationError("ProcessingInput: no variant present")


def deserialize_json(data: dict) -> ProcessingInput:
    if data.get("timeseries") is not None:
        import capo_iotsitewise.types.timeseries_list

        return {
            "timeseries": capo_iotsitewise.types.timeseries_list.deserialize_json(
                data["timeseries"]
            )
        }
    elif data.get("dataset") is not None:
        import capo_iotsitewise.types.dataset_item

        return {
            "dataset": capo_iotsitewise.types.dataset_item.deserialize_json(
                data["dataset"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProcessingInput: no recognized variant key")
