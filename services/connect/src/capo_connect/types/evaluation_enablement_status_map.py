"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationEnablementStatusMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_enablement_status
    import capo_connect.types.reference_id

EvaluationEnablementStatusMap: TypeAlias = dict[
    "capo_connect.types.reference_id.ReferenceId",
    "capo_connect.types.evaluation_enablement_status.EvaluationEnablementStatus",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EvaluationEnablementStatusMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_connect.types.evaluation_enablement_status

        out[key] = capo_connect.types.evaluation_enablement_status.serialize_json(value)
    return out


def deserialize_json(data: dict) -> EvaluationEnablementStatusMap:
    out: EvaluationEnablementStatusMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_connect.types.evaluation_enablement_status

        out[key] = capo_connect.types.evaluation_enablement_status.deserialize_json(
            value
        )
    return out
