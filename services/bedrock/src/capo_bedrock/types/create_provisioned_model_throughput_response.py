"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateProvisionedModelThroughputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.provisioned_model_arn


class CreateProvisionedModelThroughputResponse(TypedDict, closed=True):
    provisioned_model_arn: (
        "capo_bedrock.types.provisioned_model_arn.ProvisionedModelArn"
    )
    """<p>The Amazon Resource Name (ARN) for this Provisioned Throughput.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisionedModelThroughputResponse) -> dict:
    out: dict = {}
    out["provisionedModelArn"] = value["provisioned_model_arn"]
    return out


def deserialize_json(data: dict) -> CreateProvisionedModelThroughputResponse:
    out: CreateProvisionedModelThroughputResponse = {}  # type: ignore[typeddict-item]
    if data.get("provisionedModelArn") is not None:
        out["provisioned_model_arn"] = data["provisionedModelArn"]
    else:
        out["provisioned_model_arn"] = ""
    return out
