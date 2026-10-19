"""Generated from Smithy shape ``com.amazonaws.personalize#StopRecommenderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class StopRecommenderRequest(TypedDict, closed=True):
    recommender_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the recommender to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopRecommenderRequest) -> dict:
    out: dict = {}
    out["recommenderArn"] = value["recommender_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopRecommenderRequest:
    out: StopRecommenderRequest = {}  # type: ignore[typeddict-item]
    if data.get("recommenderArn") is not None:
        out["recommender_arn"] = data["recommenderArn"]
    else:
        out["recommender_arn"] = ""
    return out
