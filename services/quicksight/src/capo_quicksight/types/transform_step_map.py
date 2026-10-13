"""Generated from Smithy shape ``com.amazonaws.quicksight#TransformStepMap``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_entity_resource_id
    import capo_quicksight.types.transform_step

TransformStepMap: TypeAlias = dict[
    "capo_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId",
    "capo_quicksight.types.transform_step.TransformStep",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TransformStepMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.transform_step

        out[key] = capo_quicksight.types.transform_step.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TransformStepMap:
    out: TransformStepMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_quicksight.types.transform_step

        out[key] = capo_quicksight.types.transform_step.deserialize_json(value)
    return out


def redact_sensitive(value: TransformStepMap) -> dict[str, Any]:
    import capo_quicksight.types.transform_step

    return {
        key: capo_quicksight.types.transform_step.redact_sensitive(item)
        for key, item in value.items()
    }
