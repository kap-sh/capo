"""Generated from Smithy shape ``com.amazonaws.personalize#CampaignConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.boolean
    import capo_personalize.types.hyper_parameters
    import capo_personalize.types.ranking_influence


class CampaignConfig(TypedDict, closed=True):
    item_exploration_config: NotRequired[
        "capo_personalize.types.hyper_parameters.HyperParameters"
    ]
    """<p>Specifies the exploration configuration hyperparameters, including <code>explorationWeight</code> and <code>explorationItemAgeCutOff</code>, you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. Provide <code>itemExplorationConfig</code> data only if your solution uses the <a href="https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html">User-Personalization</a> recipe.</p>"""
    enable_metadata_with_recommendations: NotRequired[
        "capo_personalize.types.boolean.Boolean"
    ]
    """<p>Whether metadata with recommendations is enabled for the campaign. If enabled, you can specify the columns from your Items dataset in your request for recommendations. Amazon Personalize returns this data for each item in the recommendation response. For information about enabling metadata for a campaign, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-return-metadata">Enabling metadata in recommendations for a campaign</a>.</p> <p> If you enable metadata in recommendations, you will incur additional costs. For more information, see <a href="https://aws.amazon.com/personalize/pricing/">Amazon Personalize pricing</a>. </p>"""
    sync_with_latest_solution_version: NotRequired[
        "capo_personalize.types.boolean.Boolean"
    ]
    """<p>Whether the campaign automatically updates to use the latest solution version (trained model) of a solution. If you specify <code>True</code>, you must specify the ARN of your <i>solution</i> for the <code>SolutionVersionArn</code> parameter. It must be in <code>SolutionArn/$LATEST</code> format. The default is <code>False</code> and you must manually update the campaign to deploy the latest solution version. </p> <p> For more information about automatic campaign updates, see <a href="https://docs.aws.amazon.com/personalize/latest/dg/campaigns.html#create-campaign-automatic-latest-sv-update">Enabling automatic campaign updates</a>. </p>"""
    ranking_influence: NotRequired[
        "capo_personalize.types.ranking_influence.RankingInfluence"
    ]
    """<p>A map of ranking influence values for POPULARITY and FRESHNESS. For each key, specify a numerical value between 0.0 and 1.0 that determines how much influence that ranking factor has on the final recommendations. A value closer to 1.0 gives more weight to the factor, while a value closer to 0.0 reduces its influence. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CampaignConfig) -> dict:
    out: dict = {}
    if "item_exploration_config" in value:
        import capo_personalize.types.hyper_parameters

        out["itemExplorationConfig"] = (
            capo_personalize.types.hyper_parameters.serialize_aws_json_1_1(
                value["item_exploration_config"]
            )
        )
    if "enable_metadata_with_recommendations" in value:
        out["enableMetadataWithRecommendations"] = value[
            "enable_metadata_with_recommendations"
        ]
    if "sync_with_latest_solution_version" in value:
        out["syncWithLatestSolutionVersion"] = value[
            "sync_with_latest_solution_version"
        ]
    if "ranking_influence" in value:
        import capo_personalize.types.ranking_influence

        out["rankingInfluence"] = (
            capo_personalize.types.ranking_influence.serialize_aws_json_1_1(
                value["ranking_influence"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CampaignConfig:
    out: CampaignConfig = {}  # type: ignore[typeddict-item]
    if data.get("itemExplorationConfig") is not None:
        import capo_personalize.types.hyper_parameters

        out["item_exploration_config"] = (
            capo_personalize.types.hyper_parameters.deserialize_aws_json_1_1(
                data["itemExplorationConfig"]
            )
        )
    if data.get("enableMetadataWithRecommendations") is not None:
        out["enable_metadata_with_recommendations"] = data[
            "enableMetadataWithRecommendations"
        ]
    if data.get("syncWithLatestSolutionVersion") is not None:
        out["sync_with_latest_solution_version"] = data["syncWithLatestSolutionVersion"]
    if data.get("rankingInfluence") is not None:
        import capo_personalize.types.ranking_influence

        out["ranking_influence"] = (
            capo_personalize.types.ranking_influence.deserialize_aws_json_1_1(
                data["rankingInfluence"]
            )
        )
    return out
