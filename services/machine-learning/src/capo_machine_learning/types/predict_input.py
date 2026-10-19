"""Generated from Smithy shape ``com.amazonaws.machinelearning#PredictInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.record
    import capo_machine_learning.types.vip_url


class PredictInput(TypedDict, closed=True):
    ml_model_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>A unique identifier of the <code>MLModel</code>.</p>"""
    record: "capo_machine_learning.types.record.Record"
    predict_endpoint: "capo_machine_learning.types.vip_url.VipURL"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictInput) -> dict:
    out: dict = {}
    out["MLModelId"] = value["ml_model_id"]
    import capo_machine_learning.types.record

    out["Record"] = capo_machine_learning.types.record.serialize_aws_json_1_1(
        value["record"]
    )
    out["PredictEndpoint"] = value["predict_endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictInput:
    out: PredictInput = {}  # type: ignore[typeddict-item]
    if data.get("MLModelId") is not None:
        out["ml_model_id"] = data["MLModelId"]
    else:
        out["ml_model_id"] = ""
    if data.get("Record") is not None:
        import capo_machine_learning.types.record

        out["record"] = capo_machine_learning.types.record.deserialize_aws_json_1_1(
            data["Record"]
        )
    else:
        out["record"] = {}
    if data.get("PredictEndpoint") is not None:
        out["predict_endpoint"] = data["PredictEndpoint"]
    else:
        out["predict_endpoint"] = ""
    return out
