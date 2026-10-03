"""Generated from Smithy shape ``com.amazonaws.personalize#Recommender``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.metrics
    import capo_personalize.types.name
    import capo_personalize.types.recommender_config
    import capo_personalize.types.recommender_update_summary
    import capo_personalize.types.status


class Recommender(TypedDict, closed=True):
    recommender_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recommender.</p>"""
    dataset_group_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Domain dataset group that contains the recommender.</p>"""
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the recommender.</p>"""
    recipe_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recipe (Domain dataset group use case) that the recommender was created for. </p>"""
    recommender_config: NotRequired[
        "capo_personalize.types.recommender_config.RecommenderConfig"
    ]
    """<p>The configuration details of the recommender.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the recommender was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the recommender was last updated.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the recommender.</p> <p>A recommender can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>STOP PENDING > STOP IN_PROGRESS > INACTIVE > START PENDING > START IN_PROGRESS > ACTIVE</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If a recommender fails, the reason behind the failure.</p>"""
    latest_recommender_update: NotRequired[
        "capo_personalize.types.recommender_update_summary.RecommenderUpdateSummary"
    ]
    """<p>Provides a summary of the latest updates to the recommender. </p>"""
    model_metrics: NotRequired["capo_personalize.types.metrics.Metrics"]
    """<p>Provides evaluation metrics that help you determine the performance of a recommender. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/evaluating-recommenders.html"> Evaluating a recommender</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recommender) -> dict:
    out: dict = {}
    if "recommender_arn" in value:
        out["recommenderArn"] = value["recommender_arn"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "recipe_arn" in value:
        out["recipeArn"] = value["recipe_arn"]
    if "recommender_config" in value:
        import capo_personalize.types.recommender_config

        out["recommenderConfig"] = (
            capo_personalize.types.recommender_config.serialize_aws_json_1_1(
                value["recommender_config"]
            )
        )
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "latest_recommender_update" in value:
        import capo_personalize.types.recommender_update_summary

        out["latestRecommenderUpdate"] = (
            capo_personalize.types.recommender_update_summary.serialize_aws_json_1_1(
                value["latest_recommender_update"]
            )
        )
    if "model_metrics" in value:
        import capo_personalize.types.metrics

        out["modelMetrics"] = capo_personalize.types.metrics.serialize_aws_json_1_1(
            value["model_metrics"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Recommender:
    out: Recommender = {}  # type: ignore[typeddict-item]
    if data.get("recommenderArn") is not None:
        out["recommender_arn"] = data["recommenderArn"]
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("recipeArn") is not None:
        out["recipe_arn"] = data["recipeArn"]
    if data.get("recommenderConfig") is not None:
        import capo_personalize.types.recommender_config

        out["recommender_config"] = (
            capo_personalize.types.recommender_config.deserialize_aws_json_1_1(
                data["recommenderConfig"]
            )
        )
    if data.get("creationDateTime") is not None:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if data.get("lastUpdatedDateTime") is not None:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("latestRecommenderUpdate") is not None:
        import capo_personalize.types.recommender_update_summary

        out["latest_recommender_update"] = (
            capo_personalize.types.recommender_update_summary.deserialize_aws_json_1_1(
                data["latestRecommenderUpdate"]
            )
        )
    if data.get("modelMetrics") is not None:
        import capo_personalize.types.metrics

        out["model_metrics"] = capo_personalize.types.metrics.deserialize_aws_json_1_1(
            data["modelMetrics"]
        )
    return out
