"""Generated from Smithy shape ``com.amazonaws.personalize#BatchInferenceJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.hyper_parameters
    import capo_personalize.types.ranking_influence


class BatchInferenceJobConfig(TypedDict, closed=True):
    item_exploration_config: NotRequired[
        "capo_personalize.types.hyper_parameters.HyperParameters"
    ]
    """<p>A string to string map specifying the exploration configuration hyperparameters, including <code>explorationWeight</code> and <code>explorationItemAgeCutOff</code>, you want to use to configure the amount of item exploration Amazon Personalize uses when recommending items. See <a href="https://docs.aws.amazon.com/personalize/latest/dg/native-recipe-new-item-USER_PERSONALIZATION.html">User-Personalization</a>.</p>"""
    ranking_influence: NotRequired[
        "capo_personalize.types.ranking_influence.RankingInfluence"
    ]
    """<p>A map of ranking influence values for POPULARITY and FRESHNESS. For each key, specify a numerical value between 0.0 and 1.0 that determines how much influence that ranking factor has on the final recommendations. A value closer to 1.0 gives more weight to the factor, while a value closer to 0.0 reduces its influence.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchInferenceJobConfig) -> dict:
    out: dict = {}
    if "item_exploration_config" in value:
        import capo_personalize.types.hyper_parameters

        out["itemExplorationConfig"] = (
            capo_personalize.types.hyper_parameters.serialize_aws_json_1_1(
                value["item_exploration_config"]
            )
        )
    if "ranking_influence" in value:
        import capo_personalize.types.ranking_influence

        out["rankingInfluence"] = (
            capo_personalize.types.ranking_influence.serialize_aws_json_1_1(
                value["ranking_influence"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchInferenceJobConfig:
    out: BatchInferenceJobConfig = {}  # type: ignore[typeddict-item]
    if data.get("itemExplorationConfig") is not None:
        import capo_personalize.types.hyper_parameters

        out["item_exploration_config"] = (
            capo_personalize.types.hyper_parameters.deserialize_aws_json_1_1(
                data["itemExplorationConfig"]
            )
        )
    if data.get("rankingInfluence") is not None:
        import capo_personalize.types.ranking_influence

        out["ranking_influence"] = (
            capo_personalize.types.ranking_influence.deserialize_aws_json_1_1(
                data["rankingInfluence"]
            )
        )
    return out
