"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateRecommenderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.recommender_config


class UpdateRecommenderRequest(TypedDict, closed=True):
    recommender_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the recommender to modify.</p>"""
    recommender_config: "capo_personalize.types.recommender_config.RecommenderConfig"
    """<p>The configuration details of the recommender.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRecommenderRequest) -> dict:
    out: dict = {}
    out["recommenderArn"] = value["recommender_arn"]
    import capo_personalize.types.recommender_config

    out["recommenderConfig"] = (
        capo_personalize.types.recommender_config.serialize_aws_json_1_1(
            value["recommender_config"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRecommenderRequest:
    out: UpdateRecommenderRequest = {}  # type: ignore[typeddict-item]
    if data.get("recommenderArn") is not None:
        out["recommender_arn"] = data["recommenderArn"]
    else:
        out["recommender_arn"] = ""
    if data.get("recommenderConfig") is not None:
        import capo_personalize.types.recommender_config

        out["recommender_config"] = (
            capo_personalize.types.recommender_config.deserialize_aws_json_1_1(
                data["recommenderConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRecommenderRequest.recommender_config required"
        )
    return out
