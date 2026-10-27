"""Generated from Smithy shape ``com.amazonaws.ivs#ListChannelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_ad_configuration_arn
    import capo_ivs.types.channel_failover_slate_configuration_arn
    import capo_ivs.types.channel_name
    import capo_ivs.types.channel_playback_restriction_policy_arn
    import capo_ivs.types.channel_recording_configuration_arn
    import capo_ivs.types.max_channel_results
    import capo_ivs.types.pagination_token


class ListChannelsRequest(TypedDict, closed=True):
    filter_by_name: NotRequired["capo_ivs.types.channel_name.ChannelName"]
    """<p>Filters the channel list to match the specified name.</p>"""
    filter_by_recording_configuration_arn: NotRequired[
        "capo_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
    ]
    """<p>Filters the channel list to match the specified recording-configuration ARN.</p>"""
    filter_by_playback_restriction_policy_arn: NotRequired[
        "capo_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
    ]
    """<p>Filters the channel list to match the specified policy.</p>"""
    filter_by_ad_configuration_arn: NotRequired[
        "capo_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
    ]
    """<p>Filters the channel list to match the specified ad configuration ARN.</p>"""
    filter_by_failover_slate_configuration_arn: NotRequired[
        "capo_ivs.types.channel_failover_slate_configuration_arn.ChannelFailoverSlateConfigurationArn"
    ]
    """<p>Filters the channel list to match the specified failover-slate-configuration ARN.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>The first channel to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired["capo_ivs.types.max_channel_results.MaxChannelResults"]
    """<p>Maximum number of channels to return. Default: 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsRequest) -> dict:
    out: dict = {}
    if "filter_by_name" in value:
        out["filterByName"] = value["filter_by_name"]
    if "filter_by_recording_configuration_arn" in value:
        out["filterByRecordingConfigurationArn"] = value[
            "filter_by_recording_configuration_arn"
        ]
    if "filter_by_playback_restriction_policy_arn" in value:
        out["filterByPlaybackRestrictionPolicyArn"] = value[
            "filter_by_playback_restriction_policy_arn"
        ]
    if "filter_by_ad_configuration_arn" in value:
        out["filterByAdConfigurationArn"] = value["filter_by_ad_configuration_arn"]
    if "filter_by_failover_slate_configuration_arn" in value:
        out["filterByFailoverSlateConfigurationArn"] = value[
            "filter_by_failover_slate_configuration_arn"
        ]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListChannelsRequest:
    out: ListChannelsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filterByName") is not None:
        out["filter_by_name"] = data["filterByName"]
    if data.get("filterByRecordingConfigurationArn") is not None:
        out["filter_by_recording_configuration_arn"] = data[
            "filterByRecordingConfigurationArn"
        ]
    if data.get("filterByPlaybackRestrictionPolicyArn") is not None:
        out["filter_by_playback_restriction_policy_arn"] = data[
            "filterByPlaybackRestrictionPolicyArn"
        ]
    if data.get("filterByAdConfigurationArn") is not None:
        out["filter_by_ad_configuration_arn"] = data["filterByAdConfigurationArn"]
    if data.get("filterByFailoverSlateConfigurationArn") is not None:
        out["filter_by_failover_slate_configuration_arn"] = data[
            "filterByFailoverSlateConfigurationArn"
        ]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
