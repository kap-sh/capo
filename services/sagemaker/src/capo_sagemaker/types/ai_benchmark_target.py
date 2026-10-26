"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkTarget``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_benchmark_endpoint


class _AIBenchmarkTarget_Endpoint(TypedDict, closed=True):
    Endpoint: "capo_sagemaker.types.ai_benchmark_endpoint.AIBenchmarkEndpoint"


AIBenchmarkTarget: TypeAlias = _AIBenchmarkTarget_Endpoint | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkTarget) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AIBenchmarkTarget: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Endpoint" in value:
        import capo_sagemaker.types.ai_benchmark_endpoint

        return {
            "Endpoint": capo_sagemaker.types.ai_benchmark_endpoint.serialize_aws_json_1_1(
                value["Endpoint"]
            )
        }
    else:
        raise SerializationError("AIBenchmarkTarget: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AIBenchmarkTarget:
    if data.get("Endpoint") is not None:
        import capo_sagemaker.types.ai_benchmark_endpoint

        return {
            "Endpoint": capo_sagemaker.types.ai_benchmark_endpoint.deserialize_aws_json_1_1(
                data["Endpoint"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AIBenchmarkTarget: no recognized variant key")
