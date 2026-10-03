"""Generated from Smithy shape ``com.amazonaws.personalize#CreateRecommenderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.name
    import capo_personalize.types.recommender_config
    import capo_personalize.types.tags


class CreateRecommenderRequest(TypedDict, closed=True):
    name: "capo_personalize.types.name.Name"
    """<p>The name of the recommender.</p>"""
    dataset_group_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the destination domain dataset group for the recommender.</p>"""
    recipe_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the recipe that the recommender will use. For a recommender, a recipe is a Domain dataset group use case. Only Domain dataset group use cases can be used to create a recommender. For information about use cases see <a href="https://docs.aws.amazon.com/personalize/latest/dg/domain-use-cases.html">Choosing recommender use cases</a>. </p>"""
    recommender_config: NotRequired[
        "capo_personalize.types.recommender_config.RecommenderConfig"
    ]
    """<p>The configuration details of the recommender.</p>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the recommender.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRecommenderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["datasetGroupArn"] = value["dataset_group_arn"]
    out["recipeArn"] = value["recipe_arn"]
    if "recommender_config" in value:
        import capo_personalize.types.recommender_config

        out["recommenderConfig"] = (
            capo_personalize.types.recommender_config.serialize_aws_json_1_1(
                value["recommender_config"]
            )
        )
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRecommenderRequest:
    out: CreateRecommenderRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRecommenderRequest.name required")
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        raise DeserializationError(
            "CreateRecommenderRequest.dataset_group_arn required"
        )
    if data.get("recipeArn") is not None:
        out["recipe_arn"] = data["recipeArn"]
    else:
        raise DeserializationError("CreateRecommenderRequest.recipe_arn required")
    if data.get("recommenderConfig") is not None:
        import capo_personalize.types.recommender_config

        out["recommender_config"] = (
            capo_personalize.types.recommender_config.deserialize_aws_json_1_1(
                data["recommenderConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
