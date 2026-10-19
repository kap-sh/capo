"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelDataBindingUsageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.computation_model_id_list
    import capo_iotsitewise.types.matched_data_binding


class ComputationModelDataBindingUsageSummary(TypedDict, closed=True):
    computation_model_ids: (
        "capo_iotsitewise.types.computation_model_id_list.ComputationModelIdList"
    )
    """<p>The list of computation model IDs that use this data binding. This allows identification of all computation models affected by changes to the referenced data source.</p>"""
    matched_data_binding: (
        "capo_iotsitewise.types.matched_data_binding.MatchedDataBinding"
    )
    """<p>The data binding matched by the filter criteria. Contains details about specific data binding values used by the computation models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelDataBindingUsageSummary) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.computation_model_id_list

    out["computationModelIds"] = (
        capo_iotsitewise.types.computation_model_id_list.serialize_json(
            value["computation_model_ids"]
        )
    )
    import capo_iotsitewise.types.matched_data_binding

    out["matchedDataBinding"] = (
        capo_iotsitewise.types.matched_data_binding.serialize_json(
            value["matched_data_binding"]
        )
    )
    return out


def deserialize_json(data: dict) -> ComputationModelDataBindingUsageSummary:
    out: ComputationModelDataBindingUsageSummary = {}  # type: ignore[typeddict-item]
    if data.get("computationModelIds") is not None:
        import capo_iotsitewise.types.computation_model_id_list

        out["computation_model_ids"] = (
            capo_iotsitewise.types.computation_model_id_list.deserialize_json(
                data["computationModelIds"]
            )
        )
    else:
        out["computation_model_ids"] = []
    if data.get("matchedDataBinding") is not None:
        import capo_iotsitewise.types.matched_data_binding

        out["matched_data_binding"] = (
            capo_iotsitewise.types.matched_data_binding.deserialize_json(
                data["matchedDataBinding"]
            )
        )
    else:
        raise DeserializationError(
            "ComputationModelDataBindingUsageSummary.matched_data_binding required"
        )
    return out
