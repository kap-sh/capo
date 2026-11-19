"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetLambdaFunctionRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.lambda_function_recommendations
    import capo_compute_optimizer.types.next_token


class GetLambdaFunctionRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of function recommendations.</p> <p>This value is null when there are no more pages of function recommendations to return.</p>"""
    lambda_function_recommendations: NotRequired[
        "capo_compute_optimizer.types.lambda_function_recommendations.LambdaFunctionRecommendations"
    ]
    """<p>An array of objects that describe function recommendations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetLambdaFunctionRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "lambda_function_recommendations" in value:
        import capo_compute_optimizer.types.lambda_function_recommendations

        out["lambdaFunctionRecommendations"] = (
            capo_compute_optimizer.types.lambda_function_recommendations.serialize_aws_json_1_0(
                value["lambda_function_recommendations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetLambdaFunctionRecommendationsResponse:
    out: GetLambdaFunctionRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("lambdaFunctionRecommendations") is not None:
        import capo_compute_optimizer.types.lambda_function_recommendations

        out["lambda_function_recommendations"] = (
            capo_compute_optimizer.types.lambda_function_recommendations.deserialize_aws_json_1_0(
                data["lambdaFunctionRecommendations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetLambdaFunctionRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "lambda_function_recommendations" in value:
        import capo_compute_optimizer.types.lambda_function_recommendations

        out["lambdaFunctionRecommendations"] = (
            capo_compute_optimizer.types.lambda_function_recommendations.serialize_cbor(
                value["lambda_function_recommendations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetLambdaFunctionRecommendationsResponse:
    out: GetLambdaFunctionRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("lambdaFunctionRecommendations") is not None:
        import capo_compute_optimizer.types.lambda_function_recommendations

        out["lambda_function_recommendations"] = (
            capo_compute_optimizer.types.lambda_function_recommendations.deserialize_cbor(
                data["lambdaFunctionRecommendations"]
            )
        )
    return out
