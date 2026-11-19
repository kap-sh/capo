"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.lambda_function_recommendation

LambdaFunctionRecommendations: TypeAlias = list[
    "capo_compute_optimizer.types.lambda_function_recommendation.LambdaFunctionRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionRecommendations) -> list:
    import capo_compute_optimizer.types.lambda_function_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.lambda_function_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LambdaFunctionRecommendations:
    import capo_compute_optimizer.types.lambda_function_recommendation

    out: LambdaFunctionRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.lambda_function_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaFunctionRecommendations) -> list:
    import capo_compute_optimizer.types.lambda_function_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.lambda_function_recommendation.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> LambdaFunctionRecommendations:
    import capo_compute_optimizer.types.lambda_function_recommendation

    out: LambdaFunctionRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.lambda_function_recommendation.deserialize_cbor(
                item
            )
        )
    return out
