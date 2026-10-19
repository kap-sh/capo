"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#VectorOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.serverless_vector_acceleration_status


class VectorOptions(TypedDict, closed=True):
    serverless_vector_acceleration: "capo_opensearchserverless.types.serverless_vector_acceleration_status.ServerlessVectorAccelerationStatus"
    """<p>Specifies whether serverless vector acceleration is enabled for the collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorOptions) -> dict:
    out: dict = {}
    out["ServerlessVectorAcceleration"] = value["serverless_vector_acceleration"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VectorOptions:
    out: VectorOptions = {}  # type: ignore[typeddict-item]
    if data.get("ServerlessVectorAcceleration") is not None:
        out["serverless_vector_acceleration"] = data["ServerlessVectorAcceleration"]
    else:
        out["serverless_vector_acceleration"] = ""
    return out
