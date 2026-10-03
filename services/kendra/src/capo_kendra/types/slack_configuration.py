"""Generated from Smithy shape ``com.amazonaws.kendra#SlackConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.data_source_inclusions_exclusions_strings
    import capo_kendra.types.data_source_to_index_field_mapping_list
    import capo_kendra.types.data_source_vpc_configuration
    import capo_kendra.types.look_back_period
    import capo_kendra.types.private_channel_filter
    import capo_kendra.types.public_channel_filter
    import capo_kendra.types.secret_arn
    import capo_kendra.types.since_crawl_date
    import capo_kendra.types.slack_entity_list
    import capo_kendra.types.team_id


class SlackConfiguration(TypedDict, closed=True):
    team_id: "capo_kendra.types.team_id.TeamId"
    """<p>The identifier of the team in the Slack workspace. For example, <i>T0123456789</i>.</p> <p>You can find your team ID in the URL of the main page of your Slack workspace. When you log in to Slack via a browser, you are directed to the URL of the main page. For example, <i>https://app.slack.com/client/<b>T0123456789</b>/...</i>.</p>"""
    secret_arn: "capo_kendra.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs required to connect to your Slack workspace team. The secret must contain a JSON structure with the following keys:</p> <ul> <li> <p>slackToken—The user or bot token created in Slack. For more information on creating a token in Slack, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/data-source-slack.html#slack-authentication">Authentication for a Slack data source</a>.</p> </li> </ul>"""
    vpc_configuration: NotRequired[
        "capo_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    """<p>Configuration information for an Amazon Virtual Private Cloud to connect to your Slack. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html">Configuring a VPC</a>.</p>"""
    slack_entity_list: "capo_kendra.types.slack_entity_list.SlackEntityList"
    """<p>Specify whether to index public channels, private channels, group messages, and direct messages. You can specify one or more of these options.</p>"""
    use_change_log: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to use the Slack change log to determine which documents require updating in the index. Depending on the Slack change log's size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in Slack.</p>"""
    crawl_bot_message: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index bot messages from your Slack workspace team.</p>"""
    exclude_archived: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to exclude archived messages to index from your Slack workspace team.</p>"""
    since_crawl_date: "capo_kendra.types.since_crawl_date.SinceCrawlDate"
    """<p>The date to start crawling your data from your Slack workspace team. The date must follow this format: <code>yyyy-mm-dd</code>.</p>"""
    look_back_period: NotRequired["capo_kendra.types.look_back_period.LookBackPeriod"]
    """<p>The number of hours for change log to look back from when you last synchronized your data. You can look back up to 7 days or 168 hours.</p> <p>Change log updates your index only if new content was added since you last synced your data. Updated or deleted content from before you last synced does not get updated in your index. To capture updated or deleted content before you last synced, set the <code>LookBackPeriod</code> to the number of hours you want change log to look back.</p>"""
    private_channel_filter: NotRequired[
        "capo_kendra.types.private_channel_filter.PrivateChannelFilter"
    ]
    """<p>The list of private channel names from your Slack workspace team. You use this if you want to index specific private channels, not all private channels. You can also use regular expression patterns to filter private channels.</p>"""
    public_channel_filter: NotRequired[
        "capo_kendra.types.public_channel_filter.PublicChannelFilter"
    ]
    """<p>The list of public channel names to index from your Slack workspace team. You use this if you want to index specific public channels, not all public channels. You can also use regular expression patterns to filter public channels.</p>"""
    inclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to include certain attached files in your Slack workspace team. Files that match the patterns are included in the index. Files that don't match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    exclusion_patterns: NotRequired[
        "capo_kendra.types.data_source_inclusions_exclusions_strings.DataSourceInclusionsExclusionsStrings"
    ]
    """<p>A list of regular expression patterns to exclude certain attached files in your Slack workspace team. Files that match the patterns are excluded from the index. Files that don’t match the patterns are included in the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isn't included in the index.</p>"""
    field_mappings: NotRequired[
        "capo_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>A list of <code>DataSourceToIndexFieldMapping</code> objects that map Slack data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the <code>UpdateIndex</code> API before you map to Slack fields. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html">Mapping data source fields</a>. The Slack data source field names must exist in your Slack custom metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SlackConfiguration) -> dict:
    out: dict = {}
    out["TeamId"] = value["team_id"]
    out["SecretArn"] = value["secret_arn"]
    if "vpc_configuration" in value:
        import capo_kendra.types.data_source_vpc_configuration

        out["VpcConfiguration"] = (
            capo_kendra.types.data_source_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    import capo_kendra.types.slack_entity_list

    out["SlackEntityList"] = capo_kendra.types.slack_entity_list.serialize_aws_json_1_1(
        value["slack_entity_list"]
    )
    out["UseChangeLog"] = value.get("use_change_log", False)
    out["CrawlBotMessage"] = value.get("crawl_bot_message", False)
    out["ExcludeArchived"] = value.get("exclude_archived", False)
    out["SinceCrawlDate"] = value["since_crawl_date"]
    if "look_back_period" in value:
        out["LookBackPeriod"] = value["look_back_period"]
    if "private_channel_filter" in value:
        import capo_kendra.types.private_channel_filter

        out["PrivateChannelFilter"] = (
            capo_kendra.types.private_channel_filter.serialize_aws_json_1_1(
                value["private_channel_filter"]
            )
        )
    if "public_channel_filter" in value:
        import capo_kendra.types.public_channel_filter

        out["PublicChannelFilter"] = (
            capo_kendra.types.public_channel_filter.serialize_aws_json_1_1(
                value["public_channel_filter"]
            )
        )
    if "inclusion_patterns" in value:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["InclusionPatterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["inclusion_patterns"]
            )
        )
    if "exclusion_patterns" in value:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["ExclusionPatterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.serialize_aws_json_1_1(
                value["exclusion_patterns"]
            )
        )
    if "field_mappings" in value:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SlackConfiguration:
    out: SlackConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TeamId") is not None:
        out["team_id"] = data["TeamId"]
    else:
        raise DeserializationError("SlackConfiguration.team_id required")
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("SlackConfiguration.secret_arn required")
    if data.get("VpcConfiguration") is not None:
        import capo_kendra.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            capo_kendra.types.data_source_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    if data.get("SlackEntityList") is not None:
        import capo_kendra.types.slack_entity_list

        out["slack_entity_list"] = (
            capo_kendra.types.slack_entity_list.deserialize_aws_json_1_1(
                data["SlackEntityList"]
            )
        )
    else:
        raise DeserializationError("SlackConfiguration.slack_entity_list required")
    if data.get("UseChangeLog") is not None:
        out["use_change_log"] = data["UseChangeLog"]
    else:
        out["use_change_log"] = False
    if data.get("CrawlBotMessage") is not None:
        out["crawl_bot_message"] = data["CrawlBotMessage"]
    else:
        out["crawl_bot_message"] = False
    if data.get("ExcludeArchived") is not None:
        out["exclude_archived"] = data["ExcludeArchived"]
    else:
        out["exclude_archived"] = False
    if data.get("SinceCrawlDate") is not None:
        out["since_crawl_date"] = data["SinceCrawlDate"]
    else:
        raise DeserializationError("SlackConfiguration.since_crawl_date required")
    if data.get("LookBackPeriod") is not None:
        out["look_back_period"] = data["LookBackPeriod"]
    if data.get("PrivateChannelFilter") is not None:
        import capo_kendra.types.private_channel_filter

        out["private_channel_filter"] = (
            capo_kendra.types.private_channel_filter.deserialize_aws_json_1_1(
                data["PrivateChannelFilter"]
            )
        )
    if data.get("PublicChannelFilter") is not None:
        import capo_kendra.types.public_channel_filter

        out["public_channel_filter"] = (
            capo_kendra.types.public_channel_filter.deserialize_aws_json_1_1(
                data["PublicChannelFilter"]
            )
        )
    if data.get("InclusionPatterns") is not None:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["inclusion_patterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["InclusionPatterns"]
            )
        )
    if data.get("ExclusionPatterns") is not None:
        import capo_kendra.types.data_source_inclusions_exclusions_strings

        out["exclusion_patterns"] = (
            capo_kendra.types.data_source_inclusions_exclusions_strings.deserialize_aws_json_1_1(
                data["ExclusionPatterns"]
            )
        )
    if data.get("FieldMappings") is not None:
        import capo_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            capo_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    return out
