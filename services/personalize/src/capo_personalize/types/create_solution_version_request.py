"""Generated from Smithy shape ``com.amazonaws.personalize#CreateSolutionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.name
    import capo_personalize.types.tags
    import capo_personalize.types.training_mode


class CreateSolutionVersionRequest(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the solution version.</p>"""
    solution_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the solution containing the training configuration information.</p>"""
    training_mode: NotRequired["capo_personalize.types.training_mode.TrainingMode"]
    """<p>The scope of training to be performed when creating the solution version. The default is <code>FULL</code>. This creates a completely new model based on the entirety of the training data from the datasets in your dataset group. </p> <p>If you use <a href="https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html">User-Personalization</a>, you can specify a training mode of <code>UPDATE</code>. This updates the model to consider new items for recommendations. It is not a full retraining. You should still complete a full retraining weekly. If you specify <code>UPDATE</code>, Amazon Personalize will stop automatic updates for the solution version. To resume updates, create a new solution with training mode set to <code>FULL</code> and deploy it in a campaign. For more information about automatic updates, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/use-case-recipe-features.html#maintaining-with-automatic-updates">Automatic updates</a>. </p> <p>The <code>UPDATE</code> option can only be used when you already have an active solution version created from the input solution using the <code>FULL</code> option and the input solution was trained with the <a href="https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html">User-Personalization</a> recipe or the legacy <a href="https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-hrnn-coldstart.html">HRNN-Coldstart</a> recipe.</p>"""
    tags: NotRequired["capo_personalize.types.tags.Tags"]
    """<p>A list of <a href="https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html">tags</a> to apply to the solution version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSolutionVersionRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["solutionArn"] = value["solution_arn"]
    if "training_mode" in value:
        import capo_personalize.types.training_mode

        out["trainingMode"] = (
            capo_personalize.types.training_mode.serialize_aws_json_1_1(
                value["training_mode"]
            )
        )
    if "tags" in value:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSolutionVersionRequest:
    out: CreateSolutionVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("solutionArn") is not None:
        out["solution_arn"] = data["solutionArn"]
    else:
        raise DeserializationError("CreateSolutionVersionRequest.solution_arn required")
    if data.get("trainingMode") is not None:
        import capo_personalize.types.training_mode

        out["training_mode"] = (
            capo_personalize.types.training_mode.deserialize_aws_json_1_1(
                data["trainingMode"]
            )
        )
    if data.get("tags") is not None:
        import capo_personalize.types.tags

        out["tags"] = capo_personalize.types.tags.deserialize_aws_json_1_1(data["tags"])
    return out
