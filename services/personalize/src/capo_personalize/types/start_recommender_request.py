"""Generated from Smithy shape ``com.amazonaws.personalize#StartRecommenderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class StartRecommenderRequest(TypedDict, closed=True):
    recommender_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the recommender to start.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRecommenderRequest) -> dict:
    out: dict = {}
    out["recommenderArn"] = value["recommender_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRecommenderRequest:
    out: StartRecommenderRequest = {}  # type: ignore[typeddict-item]
    if data.get("recommenderArn") is not None:
        out["recommender_arn"] = data["recommenderArn"]
    else:
        out["recommender_arn"] = ""
    return out
