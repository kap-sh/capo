"""Generated from Smithy shape ``com.amazonaws.machinelearning#CreateMLModelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name
    import capo_machine_learning.types.ml_model_type
    import capo_machine_learning.types.recipe
    import capo_machine_learning.types.s3_url
    import capo_machine_learning.types.training_parameters


class CreateMLModelInput(TypedDict, closed=True):
    ml_model_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>A user-supplied ID that uniquely identifies the <code>MLModel</code>.</p>"""
    ml_model_name: NotRequired["capo_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>MLModel</code>.</p>"""
    ml_model_type: "capo_machine_learning.types.ml_model_type.MLModelType"
    """<p>The category of supervised learning that this <code>MLModel</code> will address. Choose from the following types:</p> <ul> <li> <p>Choose <code>REGRESSION</code> if the <code>MLModel</code> will be used to predict a numeric value.</p> </li> <li> <p>Choose <code>BINARY</code> if the <code>MLModel</code> result has two possible values.</p> </li> <li> <p>Choose <code>MULTICLASS</code> if the <code>MLModel</code> result has a limited number of values.</p> </li> </ul> <p> For more information, see the <a href="https://docs.aws.amazon.com/machine-learning/latest/dg">Amazon Machine Learning Developer Guide</a>.</p>"""
    parameters: NotRequired[
        "capo_machine_learning.types.training_parameters.TrainingParameters"
    ]
    """<p>A list of the training parameters in the <code>MLModel</code>. The list is implemented as a map of key-value pairs.</p> <p>The following is the current set of training parameters:</p> <ul> <li> <p> <code>sgd.maxMLModelSizeInBytes</code> - The maximum allowed size of the model. Depending on the input data, the size of the model might affect its performance.</p> <p> The value is an integer that ranges from <code>100000</code> to <code>2147483648</code>. The default value is <code>33554432</code>.</p> </li> <li> <p> <code>sgd.maxPasses</code> - The number of times that the training process traverses the observations to build the <code>MLModel</code>. The value is an integer that ranges from <code>1</code> to <code>10000</code>. The default value is <code>10</code>.</p> </li> <li> <p> <code>sgd.shuffleType</code> - Whether Amazon ML shuffles the training data. Shuffling the data improves a model's ability to find the optimal solution for a variety of data types. The valid values are <code>auto</code> and <code>none</code>. The default value is <code>none</code>. We strongly recommend that you shuffle your data.</p> </li> <li> <p> <code>sgd.l1RegularizationAmount</code> - The coefficient regularization L1 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to zero, resulting in a sparse feature set. If you use this parameter, start by specifying a small value, such as <code>1.0E-08</code>.</p> <p>The value is a double that ranges from <code>0</code> to <code>MAX_DOUBLE</code>. The default is to not use L1 normalization. This parameter can't be used when <code>L2</code> is specified. Use this parameter sparingly.</p> </li> <li> <p> <code>sgd.l2RegularizationAmount</code> - The coefficient regularization L2 norm. It controls overfitting the data by penalizing large coefficients. This tends to drive coefficients to small, nonzero values. If you use this parameter, start by specifying a small value, such as <code>1.0E-08</code>.</p> <p>The value is a double that ranges from <code>0</code> to <code>MAX_DOUBLE</code>. The default is to not use L2 normalization. This parameter can't be used when <code>L1</code> is specified. Use this parameter sparingly.</p> </li> </ul>"""
    training_data_source_id: "capo_machine_learning.types.entity_id.EntityId"
    """<p>The <code>DataSource</code> that points to the training data.</p>"""
    recipe: NotRequired["capo_machine_learning.types.recipe.Recipe"]
    """<p>The data recipe for creating the <code>MLModel</code>. You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.</p>"""
    recipe_uri: NotRequired["capo_machine_learning.types.s3_url.S3Url"]
    """<p>The Amazon Simple Storage Service (Amazon S3) location and file name that contains the <code>MLModel</code> recipe. You must specify either the recipe or its URI. If you don't specify a recipe or its URI, Amazon ML creates a default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMLModelInput) -> dict:
    out: dict = {}
    out["MLModelId"] = value["ml_model_id"]
    if "ml_model_name" in value:
        out["MLModelName"] = value["ml_model_name"]
    import capo_machine_learning.types.ml_model_type

    out["MLModelType"] = (
        capo_machine_learning.types.ml_model_type.serialize_aws_json_1_1(
            value["ml_model_type"]
        )
    )
    if "parameters" in value:
        import capo_machine_learning.types.training_parameters

        out["Parameters"] = (
            capo_machine_learning.types.training_parameters.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    out["TrainingDataSourceId"] = value["training_data_source_id"]
    if "recipe" in value:
        out["Recipe"] = value["recipe"]
    if "recipe_uri" in value:
        out["RecipeUri"] = value["recipe_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMLModelInput:
    out: CreateMLModelInput = {}  # type: ignore[typeddict-item]
    if data.get("MLModelId") is not None:
        out["ml_model_id"] = data["MLModelId"]
    else:
        raise DeserializationError("CreateMLModelInput.ml_model_id required")
    if data.get("MLModelName") is not None:
        out["ml_model_name"] = data["MLModelName"]
    if data.get("MLModelType") is not None:
        import capo_machine_learning.types.ml_model_type

        out["ml_model_type"] = (
            capo_machine_learning.types.ml_model_type.deserialize_aws_json_1_1(
                data["MLModelType"]
            )
        )
    else:
        raise DeserializationError("CreateMLModelInput.ml_model_type required")
    if data.get("Parameters") is not None:
        import capo_machine_learning.types.training_parameters

        out["parameters"] = (
            capo_machine_learning.types.training_parameters.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    if data.get("TrainingDataSourceId") is not None:
        out["training_data_source_id"] = data["TrainingDataSourceId"]
    else:
        raise DeserializationError(
            "CreateMLModelInput.training_data_source_id required"
        )
    if data.get("Recipe") is not None:
        out["recipe"] = data["Recipe"]
    if data.get("RecipeUri") is not None:
        out["recipe_uri"] = data["RecipeUri"]
    return out
