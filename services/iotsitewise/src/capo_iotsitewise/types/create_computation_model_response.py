"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateComputationModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.computation_model_status
    import capo_iotsitewise.types.id


class CreateComputationModelResponse(TypedDict, closed=True):
    computation_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the computation model.</p>"""
    computation_model_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the computation model, which has the following format.</p> <p> <code>arn:${Partition}:iotsitewise:${Region}:${Account}:computation-model/${ComputationModelId}</code> </p>"""
    computation_model_status: (
        "capo_iotsitewise.types.computation_model_status.ComputationModelStatus"
    )
    """<p>The status of the computation model, containing a state (CREATING after successfully calling this operation) and any error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateComputationModelResponse) -> dict:
    out: dict = {}
    out["computationModelId"] = value["computation_model_id"]
    out["computationModelArn"] = value["computation_model_arn"]
    import capo_iotsitewise.types.computation_model_status

    out["computationModelStatus"] = (
        capo_iotsitewise.types.computation_model_status.serialize_json(
            value["computation_model_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateComputationModelResponse:
    out: CreateComputationModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("computationModelId") is not None:
        out["computation_model_id"] = data["computationModelId"]
    else:
        raise DeserializationError(
            "CreateComputationModelResponse.computation_model_id required"
        )
    if data.get("computationModelArn") is not None:
        out["computation_model_arn"] = data["computationModelArn"]
    else:
        raise DeserializationError(
            "CreateComputationModelResponse.computation_model_arn required"
        )
    if data.get("computationModelStatus") is not None:
        import capo_iotsitewise.types.computation_model_status

        out["computation_model_status"] = (
            capo_iotsitewise.types.computation_model_status.deserialize_json(
                data["computationModelStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CreateComputationModelResponse.computation_model_status required"
        )
    return out
