"""Generated from Smithy shape ``com.amazonaws.personalize#CreateSolutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.boolean
    import capo_personalize.types.event_type
    import capo_personalize.types.name
    import capo_personalize.types.perform_auto_ml
    import capo_personalize.types.perform_auto_training
    import capo_personalize.types.perform_incremental_update
    import capo_personalize.types.solution_config
    import capo_personalize.types.tags


class CreateSolutionRequest(TypedDict, closed=True):
    name: "capo_personalize.types.name.Name"
    """<p>The name for the solution.</p>"""
    perform_hpo: NotRequired["capo_personalize.types.boolean.Boolean"]
    """<p>Whether to perform hyperparameter optimization (HPO) on the specified or selected recipe. The default is <code>false</code>.</p> <p>When performing AutoML, this parameter is always <code>true</code> and you should not set it to <code>false</code>.</p>"""
    perform_auto_ml: "capo_personalize.types.perform_auto_ml.PerformAutoML"
    """<important> <p>We don't recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize recipes. For more information, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html">Choosing a recipe</a>.</p> </important> <p>Whether to perform automated machine learning (AutoML). The default is <code>false</code>. For this case, you must specify <code>recipeArn</code>.</p> <p>When set to <code>true</code>, Amazon Personalize analyzes your training data and selects the optimal USER_PERSONALIZATION recipe and hyperparameters. In this case, you must omit <code>recipeArn</code>. Amazon Personalize determines the optimal recipe by running tests with different values for the hyperparameters. AutoML lengthens the training process as compared to selecting a specific recipe.</p>"""
    perform_auto_training: NotRequired[
        "capo_personalize.types.perform_auto_training.PerformAutoTraining"
    ]
    """<p>Whether the solution uses automatic training to create new solution versions (trained models). The default is <code>True</code> and the solution automatically creates new solution versions every 7 days. You can change the training frequency by specifying a <code>schedulingExpression</code> in the <code>AutoTrainingConfig</code> as part of solution configuration. For more information about automatic training, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html">Configuring automatic training</a>.</p> <p> Automatic solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within the hour, the solution skips the first automatic training. </p> <p> After training starts, you can get the solution version's Amazon Resource Name (ARN) with the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html">ListSolutionVersions</a> API operation. To get its status, use the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html">DescribeSolutionVersion</a>. </p>"""
    perform_incremental_update: NotRequired[
        "capo_personalize.types.perform_incremental_update.PerformIncrementalUpdate"
    ]
    """<p>Whether to perform incremental training updates on your model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe.</p>"""
    recipe_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the recipe to use for model training. This is required when <code>performAutoML</code> is false. For information about different Amazon Personalize recipes and their ARNs, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html">Choosing a recipe</a>. </p>"""
    dataset_group_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset group that provides the training data.</p>"""
    event_type: NotRequired["capo_personalize.types.event_type.EventType"]
    """<p>When your have multiple event types (using an <code>EVENT_TYPE</code> schema field), this parameter specifies which event type (for example, 'click' or 'like') is used for training the model.</p> <p>If you do not provide an <code>eventType</code>, Amazon Personalize will use all interactions for training with equal weight regardless of type.</p>"""
    solution_config: NotRequired[
        "capo_personalize.types.solution_config.SolutionConfig"
    ]
    """<p>The configuration properties for the solution. When <code>performAutoML</code> is set to true, Amazon Personalize only evaluates the <code>autoMLConfig</code> section of the solution configuration.</p> <note> <p>Amazon Personalize doesn't support configuring the <code>hpoObjective</code> at this time.</p> </note>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the solution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSolutionRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "perform_hpo" in value:
        out["performHPO"] = value["perform_hpo"]
    out["performAutoML"] = value.get("perform_auto_ml", False)
    if "perform_auto_training" in value:
        out["performAutoTraining"] = value["perform_auto_training"]
    if "perform_incremental_update" in value:
        out["performIncrementalUpdate"] = value["perform_incremental_update"]
    if "recipe_arn" in value:
        out["recipeArn"] = value["recipe_arn"]
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
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSolutionRequest:
    out: CreateSolutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSolutionRequest.name required")
    if data.get("performHPO") is not None:
        out["perform_hpo"] = data["performHPO"]
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
    else:
        raise DeserializationError("CreateSolutionRequest.dataset_group_arn required")
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    if data.get("solutionConfig") is not None:
        import capo_personalize.types.solution_config

        out["solution_config"] = (
            capo_personalize.types.solution_config.deserialize_aws_json_1_1(
                data["solutionConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
