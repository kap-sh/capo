"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateContributorInsightsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.contributor_insights_action
    import capo_dynamodb.types.contributor_insights_mode
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.table_arn


class UpdateContributorInsightsInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    index_name: NotRequired["capo_dynamodb.types.index_name.IndexName"]
    """<p>The global secondary index name, if applicable.</p>"""
    contributor_insights_action: (
        "capo_dynamodb.types.contributor_insights_action.ContributorInsightsAction"
    )
    """<p>Represents the contributor insights action.</p>"""
    contributor_insights_mode: NotRequired[
        "capo_dynamodb.types.contributor_insights_mode.ContributorInsightsMode"
    ]
    """<p>Specifies whether to track all access and throttled events or throttled events only for the DynamoDB table or index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateContributorInsightsInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    import capo_dynamodb.types.contributor_insights_action

    out["ContributorInsightsAction"] = (
        capo_dynamodb.types.contributor_insights_action.serialize_aws_json_1_0(
            value["contributor_insights_action"]
        )
    )
    if "contributor_insights_mode" in value:
        import capo_dynamodb.types.contributor_insights_mode

        out["ContributorInsightsMode"] = (
            capo_dynamodb.types.contributor_insights_mode.serialize_aws_json_1_0(
                value["contributor_insights_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateContributorInsightsInput:
    out: UpdateContributorInsightsInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("IndexName") is not None:
        out["index_name"] = data["IndexName"]
    if data.get("ContributorInsightsAction") is not None:
        import capo_dynamodb.types.contributor_insights_action

        out["contributor_insights_action"] = (
            capo_dynamodb.types.contributor_insights_action.deserialize_aws_json_1_0(
                data["ContributorInsightsAction"]
            )
        )
    else:
        import typing

        out["contributor_insights_action"] = typing.cast(
            "capo_dynamodb.types.contributor_insights_action.ContributorInsightsAction",
            "",
        )
    if data.get("ContributorInsightsMode") is not None:
        import capo_dynamodb.types.contributor_insights_mode

        out["contributor_insights_mode"] = (
            capo_dynamodb.types.contributor_insights_mode.deserialize_aws_json_1_0(
                data["ContributorInsightsMode"]
            )
        )
    return out
