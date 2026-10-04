"""Generated from Smithy shape ``com.amazonaws.mediatailor#PutPlaybackConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer_min1
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.ad_conditioning_configuration
    import capo_mediatailor.types.ad_decision_server_configuration
    import capo_mediatailor.types.ads_personalization_concurrency
    import capo_mediatailor.types.ads_personalization_timeouts
    import capo_mediatailor.types.avail_suppression
    import capo_mediatailor.types.beaconing_configuration
    import capo_mediatailor.types.bumper
    import capo_mediatailor.types.cdn_configuration
    import capo_mediatailor.types.configuration_aliases_request
    import capo_mediatailor.types.dash_configuration_for_put
    import capo_mediatailor.types.function_mapping
    import capo_mediatailor.types.insertion_mode
    import capo_mediatailor.types.live_pre_roll_configuration
    import capo_mediatailor.types.manifest_processing_rules
    import capo_mediatailor.types.yield_optimization_configuration


class PutPlaybackConfigurationRequest(TypedDict, closed=True):
    ad_decision_server_url: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.</p>"""
    avail_suppression: NotRequired[
        "capo_mediatailor.types.avail_suppression.AvailSuppression"
    ]
    """<p>The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html">Ad Suppression</a>.</p>"""
    bumper: NotRequired["capo_mediatailor.types.bumper.Bumper"]
    """<p>The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html">Bumpers</a>.</p>"""
    cdn_configuration: NotRequired[
        "capo_mediatailor.types.cdn_configuration.CdnConfiguration"
    ]
    """<p>The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.</p>"""
    configuration_aliases: NotRequired[
        "capo_mediatailor.types.configuration_aliases_request.ConfigurationAliasesRequest"
    ]
    """<p>The player parameters and aliases used as dynamic variables during session initialization. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html">Domain Variables</a>.</p>"""
    dash_configuration: NotRequired[
        "capo_mediatailor.types.dash_configuration_for_put.DashConfigurationForPut"
    ]
    """<p>The configuration for DASH content.</p>"""
    insertion_mode: "capo_mediatailor.types.insertion_mode.InsertionMode"
    """<p>The setting that controls whether players can use stitched or guided ad insertion. The default, <code>STITCHED_ONLY</code>, forces all player sessions to use stitched (server-side) ad insertion. Choosing <code>PLAYER_SELECT</code> allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.</p>"""
    live_pre_roll_configuration: NotRequired[
        "capo_mediatailor.types.live_pre_roll_configuration.LivePreRollConfiguration"
    ]
    """<p>The configuration for pre-roll ad insertion.</p>"""
    manifest_processing_rules: NotRequired[
        "capo_mediatailor.types.manifest_processing_rules.ManifestProcessingRules"
    ]
    """<p>The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.</p>"""
    name: "capo_mediatailor.types.__string.__string"
    """<p>The identifier for the playback configuration.</p>"""
    personalization_threshold_seconds: NotRequired[
        "capo_mediatailor.types.__integer_min1.__integerMin1"
    ]
    """<p>Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to <i>ad replacement</i> in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html">Ad Behavior in AWS Elemental MediaTailor</a>.</p>"""
    slate_ad_url: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    transcode_profile_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.</p>"""
    video_content_source_url: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.</p>"""
    ad_conditioning_configuration: NotRequired[
        "capo_mediatailor.types.ad_conditioning_configuration.AdConditioningConfiguration"
    ]
    """<p>The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads. </p>"""
    ad_decision_server_configuration: NotRequired[
        "capo_mediatailor.types.ad_decision_server_configuration.AdDecisionServerConfiguration"
    ]
    """<p>The configuration for customizing HTTP requests to the ad decision server (ADS). This includes settings for request method, headers, body content, and compression options.</p>"""
    yield_optimization_configuration: NotRequired[
        "capo_mediatailor.types.yield_optimization_configuration.YieldOptimizationConfiguration"
    ]
    """<p>Configuration for Yield Optimization, which fills unsold ad inventory in ad breaks with programmatic ads from Amazon Publisher Services (APS).</p>"""
    function_mapping: NotRequired[
        "capo_mediatailor.types.function_mapping.FunctionMapping"
    ]
    """<p>A map of lifecycle hook event names to function identifiers. The function mapping specifies which function MediaTailor executes at each lifecycle hook during ad insertion. Valid keys are <code>PRE_SESSION_INITIALIZATION</code>, <code>PRE_ADS_REQUEST</code>, <code>POST_ADS_RESPONSE</code>, and <code>PRE_MANIFEST_INSERTION</code>. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-hooks.html">Functions lifecycle hooks</a> in the <i>MediaTailor User Guide</i>.</p>"""
    ads_personalization_timeouts: NotRequired[
        "capo_mediatailor.types.ads_personalization_timeouts.AdsPersonalizationTimeouts"
    ]
    """<p>The timeout settings for ad decision server interactions. These settings control how long MediaTailor waits for ADS responses and the total time budget for ad personalization across live, VOD, and prefetch workflows.</p>"""
    ads_personalization_concurrency: NotRequired[
        "capo_mediatailor.types.ads_personalization_concurrency.AdsPersonalizationConcurrency"
    ]
    """<p>The concurrency settings for ad decision server interactions. These settings control how many simultaneous ADS requests MediaTailor makes per manifest request.</p>"""
    beaconing_configuration: NotRequired[
        "capo_mediatailor.types.beaconing_configuration.BeaconingConfiguration"
    ]
    """<p>The beaconing configuration for this playback configuration, which controls whether MediaTailor includes beacons of its own in the ad tracking response. If you omit this setting, MediaTailor uses <code>INSIGHTS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPlaybackConfigurationRequest) -> dict:
    out: dict = {}
    if "ad_decision_server_url" in value:
        out["AdDecisionServerUrl"] = value["ad_decision_server_url"]
    if "avail_suppression" in value:
        import capo_mediatailor.types.avail_suppression

        out["AvailSuppression"] = (
            capo_mediatailor.types.avail_suppression.serialize_json(
                value["avail_suppression"]
            )
        )
    if "bumper" in value:
        import capo_mediatailor.types.bumper

        out["Bumper"] = capo_mediatailor.types.bumper.serialize_json(value["bumper"])
    if "cdn_configuration" in value:
        import capo_mediatailor.types.cdn_configuration

        out["CdnConfiguration"] = (
            capo_mediatailor.types.cdn_configuration.serialize_json(
                value["cdn_configuration"]
            )
        )
    if "configuration_aliases" in value:
        import capo_mediatailor.types.configuration_aliases_request

        out["ConfigurationAliases"] = (
            capo_mediatailor.types.configuration_aliases_request.serialize_json(
                value["configuration_aliases"]
            )
        )
    if "dash_configuration" in value:
        import capo_mediatailor.types.dash_configuration_for_put

        out["DashConfiguration"] = (
            capo_mediatailor.types.dash_configuration_for_put.serialize_json(
                value["dash_configuration"]
            )
        )
    import capo_mediatailor.types.insertion_mode

    out["InsertionMode"] = capo_mediatailor.types.insertion_mode.serialize_json(
        value.get("insertion_mode", "STITCHED_ONLY")
    )
    if "live_pre_roll_configuration" in value:
        import capo_mediatailor.types.live_pre_roll_configuration

        out["LivePreRollConfiguration"] = (
            capo_mediatailor.types.live_pre_roll_configuration.serialize_json(
                value["live_pre_roll_configuration"]
            )
        )
    if "manifest_processing_rules" in value:
        import capo_mediatailor.types.manifest_processing_rules

        out["ManifestProcessingRules"] = (
            capo_mediatailor.types.manifest_processing_rules.serialize_json(
                value["manifest_processing_rules"]
            )
        )
    out["Name"] = value["name"]
    if "personalization_threshold_seconds" in value:
        out["PersonalizationThresholdSeconds"] = value[
            "personalization_threshold_seconds"
        ]
    if "slate_ad_url" in value:
        out["SlateAdUrl"] = value["slate_ad_url"]
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    if "transcode_profile_name" in value:
        out["TranscodeProfileName"] = value["transcode_profile_name"]
    if "video_content_source_url" in value:
        out["VideoContentSourceUrl"] = value["video_content_source_url"]
    if "ad_conditioning_configuration" in value:
        import capo_mediatailor.types.ad_conditioning_configuration

        out["AdConditioningConfiguration"] = (
            capo_mediatailor.types.ad_conditioning_configuration.serialize_json(
                value["ad_conditioning_configuration"]
            )
        )
    if "ad_decision_server_configuration" in value:
        import capo_mediatailor.types.ad_decision_server_configuration

        out["AdDecisionServerConfiguration"] = (
            capo_mediatailor.types.ad_decision_server_configuration.serialize_json(
                value["ad_decision_server_configuration"]
            )
        )
    if "yield_optimization_configuration" in value:
        import capo_mediatailor.types.yield_optimization_configuration

        out["YieldOptimizationConfiguration"] = (
            capo_mediatailor.types.yield_optimization_configuration.serialize_json(
                value["yield_optimization_configuration"]
            )
        )
    if "function_mapping" in value:
        import capo_mediatailor.types.function_mapping

        out["FunctionMapping"] = capo_mediatailor.types.function_mapping.serialize_json(
            value["function_mapping"]
        )
    if "ads_personalization_timeouts" in value:
        import capo_mediatailor.types.ads_personalization_timeouts

        out["AdsPersonalizationTimeouts"] = (
            capo_mediatailor.types.ads_personalization_timeouts.serialize_json(
                value["ads_personalization_timeouts"]
            )
        )
    if "ads_personalization_concurrency" in value:
        import capo_mediatailor.types.ads_personalization_concurrency

        out["AdsPersonalizationConcurrency"] = (
            capo_mediatailor.types.ads_personalization_concurrency.serialize_json(
                value["ads_personalization_concurrency"]
            )
        )
    if "beaconing_configuration" in value:
        import capo_mediatailor.types.beaconing_configuration

        out["BeaconingConfiguration"] = (
            capo_mediatailor.types.beaconing_configuration.serialize_json(
                value["beaconing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutPlaybackConfigurationRequest:
    out: PutPlaybackConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AdDecisionServerUrl") is not None:
        out["ad_decision_server_url"] = data["AdDecisionServerUrl"]
    if data.get("AvailSuppression") is not None:
        import capo_mediatailor.types.avail_suppression

        out["avail_suppression"] = (
            capo_mediatailor.types.avail_suppression.deserialize_json(
                data["AvailSuppression"]
            )
        )
    if data.get("Bumper") is not None:
        import capo_mediatailor.types.bumper

        out["bumper"] = capo_mediatailor.types.bumper.deserialize_json(data["Bumper"])
    if data.get("CdnConfiguration") is not None:
        import capo_mediatailor.types.cdn_configuration

        out["cdn_configuration"] = (
            capo_mediatailor.types.cdn_configuration.deserialize_json(
                data["CdnConfiguration"]
            )
        )
    if data.get("ConfigurationAliases") is not None:
        import capo_mediatailor.types.configuration_aliases_request

        out["configuration_aliases"] = (
            capo_mediatailor.types.configuration_aliases_request.deserialize_json(
                data["ConfigurationAliases"]
            )
        )
    if data.get("DashConfiguration") is not None:
        import capo_mediatailor.types.dash_configuration_for_put

        out["dash_configuration"] = (
            capo_mediatailor.types.dash_configuration_for_put.deserialize_json(
                data["DashConfiguration"]
            )
        )
    if data.get("InsertionMode") is not None:
        import capo_mediatailor.types.insertion_mode

        out["insertion_mode"] = capo_mediatailor.types.insertion_mode.deserialize_json(
            data["InsertionMode"]
        )
    else:
        out["insertion_mode"] = "STITCHED_ONLY"
    if data.get("LivePreRollConfiguration") is not None:
        import capo_mediatailor.types.live_pre_roll_configuration

        out["live_pre_roll_configuration"] = (
            capo_mediatailor.types.live_pre_roll_configuration.deserialize_json(
                data["LivePreRollConfiguration"]
            )
        )
    if data.get("ManifestProcessingRules") is not None:
        import capo_mediatailor.types.manifest_processing_rules

        out["manifest_processing_rules"] = (
            capo_mediatailor.types.manifest_processing_rules.deserialize_json(
                data["ManifestProcessingRules"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PutPlaybackConfigurationRequest.name required")
    if data.get("PersonalizationThresholdSeconds") is not None:
        out["personalization_threshold_seconds"] = data[
            "PersonalizationThresholdSeconds"
        ]
    if data.get("SlateAdUrl") is not None:
        out["slate_ad_url"] = data["SlateAdUrl"]
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if data.get("TranscodeProfileName") is not None:
        out["transcode_profile_name"] = data["TranscodeProfileName"]
    if data.get("VideoContentSourceUrl") is not None:
        out["video_content_source_url"] = data["VideoContentSourceUrl"]
    if data.get("AdConditioningConfiguration") is not None:
        import capo_mediatailor.types.ad_conditioning_configuration

        out["ad_conditioning_configuration"] = (
            capo_mediatailor.types.ad_conditioning_configuration.deserialize_json(
                data["AdConditioningConfiguration"]
            )
        )
    if data.get("AdDecisionServerConfiguration") is not None:
        import capo_mediatailor.types.ad_decision_server_configuration

        out["ad_decision_server_configuration"] = (
            capo_mediatailor.types.ad_decision_server_configuration.deserialize_json(
                data["AdDecisionServerConfiguration"]
            )
        )
    if data.get("YieldOptimizationConfiguration") is not None:
        import capo_mediatailor.types.yield_optimization_configuration

        out["yield_optimization_configuration"] = (
            capo_mediatailor.types.yield_optimization_configuration.deserialize_json(
                data["YieldOptimizationConfiguration"]
            )
        )
    if data.get("FunctionMapping") is not None:
        import capo_mediatailor.types.function_mapping

        out["function_mapping"] = (
            capo_mediatailor.types.function_mapping.deserialize_json(
                data["FunctionMapping"]
            )
        )
    if data.get("AdsPersonalizationTimeouts") is not None:
        import capo_mediatailor.types.ads_personalization_timeouts

        out["ads_personalization_timeouts"] = (
            capo_mediatailor.types.ads_personalization_timeouts.deserialize_json(
                data["AdsPersonalizationTimeouts"]
            )
        )
    if data.get("AdsPersonalizationConcurrency") is not None:
        import capo_mediatailor.types.ads_personalization_concurrency

        out["ads_personalization_concurrency"] = (
            capo_mediatailor.types.ads_personalization_concurrency.deserialize_json(
                data["AdsPersonalizationConcurrency"]
            )
        )
    if data.get("BeaconingConfiguration") is not None:
        import capo_mediatailor.types.beaconing_configuration

        out["beaconing_configuration"] = (
            capo_mediatailor.types.beaconing_configuration.deserialize_json(
                data["BeaconingConfiguration"]
            )
        )
    return out
