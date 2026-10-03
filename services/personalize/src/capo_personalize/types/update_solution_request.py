"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateSolutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.perform_auto_training
    import capo_personalize.types.perform_incremental_update
    import capo_personalize.types.solution_update_config


class UpdateSolutionRequest(TypedDict, closed=True):
    solution_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the solution to update.</p>"""
    perform_auto_training: NotRequired[
        "capo_personalize.types.perform_auto_training.PerformAutoTraining"
    ]
    """<p>Whether the solution uses automatic training to create new solution versions (trained models). You can change the training frequency by specifying a <code>schedulingExpression</code> in the <code>AutoTrainingConfig</code> as part of solution configuration. </p> <p> If you turn on automatic training, the first automatic training starts within one hour after the solution update completes. If you manually create a solution version within the hour, the solution skips the first automatic training. For more information about automatic training, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html">Configuring automatic training</a>. </p> <p> After training starts, you can get the solution version's Amazon Resource Name (ARN) with the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html">ListSolutionVersions</a> API operation. To get its status, use the <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html">DescribeSolutionVersion</a>. </p>"""
    perform_incremental_update: NotRequired[
        "capo_personalize.types.perform_incremental_update.PerformIncrementalUpdate"
    ]
    """<p>Whether to perform incremental training updates on your model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe.</p>"""
    solution_update_config: NotRequired[
        "capo_personalize.types.solution_update_config.SolutionUpdateConfig"
    ]
    """<p>The new configuration details of the solution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSolutionRequest) -> dict:
    out: dict = {}
    out["solutionArn"] = value["solution_arn"]
    if "perform_auto_training" in value:
        out["performAutoTraining"] = value["perform_auto_training"]
    if "perform_incremental_update" in value:
        out["performIncrementalUpdate"] = value["perform_incremental_update"]
    if "solution_update_config" in value:
        import capo_personalize.types.solution_update_config

        out["solutionUpdateConfig"] = (
            capo_personalize.types.solution_update_config.serialize_aws_json_1_1(
                value["solution_update_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSolutionRequest:
    out: UpdateSolutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("solutionArn") is not None:
        out["solution_arn"] = data["solutionArn"]
    else:
        raise DeserializationError("UpdateSolutionRequest.solution_arn required")
    if data.get("performAutoTraining") is not None:
        out["perform_auto_training"] = data["performAutoTraining"]
    if data.get("performIncrementalUpdate") is not None:
        out["perform_incremental_update"] = data["performIncrementalUpdate"]
    if data.get("solutionUpdateConfig") is not None:
        import capo_personalize.types.solution_update_config

        out["solution_update_config"] = (
            capo_personalize.types.solution_update_config.deserialize_aws_json_1_1(
                data["solutionUpdateConfig"]
            )
        )
    return out
