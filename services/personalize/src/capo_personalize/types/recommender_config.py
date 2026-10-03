"""Generated from Smithy shape ``com.amazonaws.personalize#RecommenderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.boolean
    import capo_personalize.types.hyper_parameters
    import capo_personalize.types.training_data_config
    import capo_personalize.types.transactions_per_second


class RecommenderConfig(TypedDict, closed=True):
    item_exploration_config: NotRequired[
        "capo_personalize.types.hyper_parameters.HyperParameters"
    ]
    """<p>Specifies the exploration configuration hyperparameters, including <code>explorationWeight</code> and <code>explorationItemAgeCutOff</code>, you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. Provide <code>itemExplorationConfig</code> data only if your recommenders generate personalized recommendations for a user (not popular items or similar items).</p>"""
    min_recommendation_requests_per_second: NotRequired[
        "capo_personalize.types.transactions_per_second.TransactionsPerSecond"
    ]
    """<p>Specifies the requested minimum provisioned recommendation requests per second that Amazon Personalize will support. A high <code>minRecommendationRequestsPerSecond</code> will increase your bill. We recommend starting with 1 for <code>minRecommendationRequestsPerSecond</code> (the default). Track your usage using Amazon CloudWatch metrics, and increase the <code>minRecommendationRequestsPerSecond</code> as necessary.</p>"""
    training_data_config: NotRequired[
        "capo_personalize.types.training_data_config.TrainingDataConfig"
    ]
    """<p> Specifies the training data configuration to use when creating a domain recommender. </p>"""
    enable_metadata_with_recommendations: NotRequired[
        "capo_personalize.types.boolean.Boolean"
    ]
    """<p>Whether metadata with recommendations is enabled for the recommender. If enabled, you can specify the columns from your Items dataset in your request for recommendations. Amazon Personalize returns this data for each item in the recommendation response. For information about enabling metadata for a recommender, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/creating-recommenders.html#create-recommender-return-metadata">Enabling metadata in recommendations for a recommender</a>.</p> <p> If you enable metadata in recommendations, you will incur additional costs. For more information, see <a href="https://aws.amazon.com/personalize/pricing/">Amazon Personalize pricing</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommenderConfig) -> dict:
    out: dict = {}
    if "item_exploration_config" in value:
        import capo_personalize.types.hyper_parameters

        out["itemExplorationConfig"] = (
            capo_personalize.types.hyper_parameters.serialize_aws_json_1_1(
                value["item_exploration_config"]
            )
        )
    if "min_recommendation_requests_per_second" in value:
        out["minRecommendationRequestsPerSecond"] = value[
            "min_recommendation_requests_per_second"
        ]
    if "training_data_config" in value:
        import capo_personalize.types.training_data_config

        out["trainingDataConfig"] = (
            capo_personalize.types.training_data_config.serialize_aws_json_1_1(
                value["training_data_config"]
            )
        )
    if "enable_metadata_with_recommendations" in value:
        out["enableMetadataWithRecommendations"] = value[
            "enable_metadata_with_recommendations"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommenderConfig:
    out: RecommenderConfig = {}  # type: ignore[typeddict-item]
    if data.get("itemExplorationConfig") is not None:
        import capo_personalize.types.hyper_parameters

        out["item_exploration_config"] = (
            capo_personalize.types.hyper_parameters.deserialize_aws_json_1_1(
                data["itemExplorationConfig"]
            )
        )
    if data.get("minRecommendationRequestsPerSecond") is not None:
        out["min_recommendation_requests_per_second"] = data[
            "minRecommendationRequestsPerSecond"
        ]
    if data.get("trainingDataConfig") is not None:
        import capo_personalize.types.training_data_config

        out["training_data_config"] = (
            capo_personalize.types.training_data_config.deserialize_aws_json_1_1(
                data["trainingDataConfig"]
            )
        )
    if data.get("enableMetadataWithRecommendations") is not None:
        out["enable_metadata_with_recommendations"] = data[
            "enableMetadataWithRecommendations"
        ]
    return out
