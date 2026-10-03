"""Generated from Smithy shape ``com.amazonaws.personalize#Solution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.auto_ml_result
    import capo_personalize.types.date
    import capo_personalize.types.event_type
    import capo_personalize.types.name
    import capo_personalize.types.perform_auto_ml
    import capo_personalize.types.perform_auto_training
    import capo_personalize.types.perform_hpo
    import capo_personalize.types.perform_incremental_update
    import capo_personalize.types.solution_config
    import capo_personalize.types.solution_update_summary
    import capo_personalize.types.solution_version_summary
    import capo_personalize.types.status


class Solution(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the solution.</p>"""
    solution_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the solution.</p>"""
    perform_hpo: "capo_personalize.types.perform_hpo.PerformHPO"
    """<p>Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is <code>false</code>.</p>"""
    perform_auto_ml: "capo_personalize.types.perform_auto_ml.PerformAutoML"
    """<important> <p>We don't recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize recipes. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/determining-use-case.html">Determining your use case.</a> </p> </important> <p>When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from the list specified in the solution configuration (<code>recipeArn</code> must not be specified). When false (the default), Amazon Personalize uses <code>recipeArn</code> for training.</p>"""
    perform_auto_training: NotRequired[
        "capo_personalize.types.perform_auto_training.PerformAutoTraining"
    ]
    """<p>Specifies whether the solution automatically creates solution versions. The default is <code>True</code> and the solution automatically creates new solution versions every 7 days.</p> <p>For more information about auto training, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html">Creating and configuring a solution</a>.</p>"""
    perform_incremental_update: NotRequired[
        "capo_personalize.types.perform_incremental_update.PerformIncrementalUpdate"
    ]
    """<p>A Boolean value that indicates whether incremental training updates are performed on the model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe</p>"""
    recipe_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the recipe used to create the solution. This is required when <code>performAutoML</code> is false.</p>"""
    dataset_group_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group that provides the training data.</p>"""
    event_type: NotRequired["capo_personalize.types.event_type.EventType"]
    """<p>The event type (for example, 'click' or 'like') that is used for training the model. If no <code>eventType</code> is provided, Amazon Personalize uses all interactions for training with equal weight regardless of type.</p>"""
    solution_config: NotRequired[
        "capo_personalize.types.solution_config.SolutionConfig"
    ]
    """<p>Describes the configuration properties for the solution.</p>"""
    auto_ml_result: NotRequired["capo_personalize.types.auto_ml_result.AutoMLResult"]
    """<p>When <code>performAutoML</code> is true, specifies the best recipe found.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the solution.</p> <p>A solution can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The creation date and time (in Unix time) of the solution.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the solution was last updated.</p>"""
    latest_solution_version: NotRequired[
        "capo_personalize.types.solution_version_summary.SolutionVersionSummary"
    ]
    """<p>Describes the latest version of the solution, including the status and the ARN.</p>"""
    latest_solution_update: NotRequired[
        "capo_personalize.types.solution_update_summary.SolutionUpdateSummary"
    ]
    """<p>Provides a summary of the latest updates to the solution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Solution) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "solution_arn" in value:
        out["solutionArn"] = value["solution_arn"]
    out["performHPO"] = value.get("perform_hpo", False)
    out["performAutoML"] = value.get("perform_auto_ml", False)
    if "perform_auto_training" in value:
        out["performAutoTraining"] = value["perform_auto_training"]
    if "perform_incremental_update" in value:
        out["performIncrementalUpdate"] = value["perform_incremental_update"]
    if "recipe_arn" in value:
        out["recipeArn"] = value["recipe_arn"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "event_type" in value:
        out["eventType"] = value["event_type"]
    if "solution_config" in value:
        import capo_personalize.types.solution_config

        out["solutionConfig"] = (
            capo_personalize.types.solution_config.serialize_aws_json_1_1(
                value["solution_config"]
            )
        )
    if "auto_ml_result" in value:
        import capo_personalize.types.auto_ml_result

        out["autoMLResult"] = (
            capo_personalize.types.auto_ml_result.serialize_aws_json_1_1(
                value["auto_ml_result"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
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
    if "latest_solution_version" in value:
        import capo_personalize.types.solution_version_summary

        out["latestSolutionVersion"] = (
            capo_personalize.types.solution_version_summary.serialize_aws_json_1_1(
                value["latest_solution_version"]
            )
        )
    if "latest_solution_update" in value:
        import capo_personalize.types.solution_update_summary

        out["latestSolutionUpdate"] = (
            capo_personalize.types.solution_update_summary.serialize_aws_json_1_1(
                value["latest_solution_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Solution:
    out: Solution = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("solutionArn") is not None:
        out["solution_arn"] = data["solutionArn"]
    if data.get("performHPO") is not None:
        out["perform_hpo"] = data["performHPO"]
    else:
        out["perform_hpo"] = False
    if data.get("performAutoML") is not None:
        out["perform_auto_ml"] = data["performAutoML"]
    else:
        out["perform_auto_ml"] = False
    if data.get("performAutoTraining") is not None:
        out["perform_auto_training"] = data["performAutoTraining"]
    if data.get("performIncrementalUpdate") is not None:
        out["perform_incremental_update"] = data["performIncrementalUpdate"]
    if data.get("recipeArn") is not None:
        out["recipe_arn"] = data["recipeArn"]
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    if data.get("solutionConfig") is not None:
        import capo_personalize.types.solution_config

        out["solution_config"] = (
            capo_personalize.types.solution_config.deserialize_aws_json_1_1(
                data["solutionConfig"]
            )
        )
    if data.get("autoMLResult") is not None:
        import capo_personalize.types.auto_ml_result

        out["auto_ml_result"] = (
            capo_personalize.types.auto_ml_result.deserialize_aws_json_1_1(
                data["autoMLResult"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
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
    if data.get("latestSolutionVersion") is not None:
        import capo_personalize.types.solution_version_summary

        out["latest_solution_version"] = (
            capo_personalize.types.solution_version_summary.deserialize_aws_json_1_1(
                data["latestSolutionVersion"]
            )
        )
    if data.get("latestSolutionUpdate") is not None:
        import capo_personalize.types.solution_update_summary

        out["latest_solution_update"] = (
            capo_personalize.types.solution_update_summary.deserialize_aws_json_1_1(
                data["latestSolutionUpdate"]
            )
        )
    return out
