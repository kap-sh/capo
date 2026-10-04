"""Generated from Smithy shape ``com.amazonaws.mediatailor#PlaybackConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

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
    import capo_mediatailor.types.configuration_aliases_response
    import capo_mediatailor.types.dash_configuration
    import capo_mediatailor.types.function_mapping
    import capo_mediatailor.types.hls_configuration
    import capo_mediatailor.types.insertion_mode
    import capo_mediatailor.types.live_pre_roll_configuration
    import capo_mediatailor.types.log_configuration
    import capo_mediatailor.types.manifest_processing_rules
    import capo_mediatailor.types.yield_optimization_configuration


class PlaybackConfiguration(TypedDict, closed=True):
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
        "capo_mediatailor.types.configuration_aliases_response.ConfigurationAliasesResponse"
    ]
    """<p>The player parameters and aliases used as dynamic variables during session initialization. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html">Domain Variables</a>.</p>"""
    dash_configuration: NotRequired[
        "capo_mediatailor.types.dash_configuration.DashConfiguration"
    ]
    """<p>The configuration for a DASH source.</p>"""
    hls_configuration: NotRequired[
        "capo_mediatailor.types.hls_configuration.HlsConfiguration"
    ]
    """<p>The configuration for HLS content.</p>"""
    insertion_mode: "capo_mediatailor.types.insertion_mode.InsertionMode"
    """<p>The setting that controls whether players can use stitched or guided ad insertion. The default, <code>STITCHED_ONLY</code>, forces all player sessions to use stitched (server-side) ad insertion. Choosing <code>PLAYER_SELECT</code> allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.</p>"""
    live_pre_roll_configuration: NotRequired[
        "capo_mediatailor.types.live_pre_roll_configuration.LivePreRollConfiguration"
    ]
    """<p>The configuration for pre-roll ad insertion.</p>"""
    log_configuration: NotRequired[
        "capo_mediatailor.types.log_configuration.LogConfiguration"
    ]
    """<p>Defines where AWS Elemental MediaTailor sends logs for the playback configuration.</p>"""
    manifest_processing_rules: NotRequired[
        "capo_mediatailor.types.manifest_processing_rules.ManifestProcessingRules"
    ]
    """<p>The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.</p>"""
    name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The identifier for the playback configuration.</p>"""
    personalization_threshold_seconds: NotRequired[
        "capo_mediatailor.types.__integer_min1.__integerMin1"
    ]
    """<p>Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to <i>ad replacement</i> in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html">Ad Behavior in AWS Elemental MediaTailor</a>.</p>"""
    playback_configuration_arn: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) for the playback configuration.</p>"""
    playback_endpoint_prefix: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The URL that your player accesses to get a manifest from AWS Elemental MediaTailor.</p>"""
    dual_stack_playback_endpoint_prefix: NotRequired[
        "capo_mediatailor.types.__string.__string"
    ]
    """<p>The dual-stack (IPv4 and IPv6) URL that your player accesses to get a manifest from AWS Elemental MediaTailor.</p>"""
    session_initialization_endpoint_prefix: NotRequired[
        "capo_mediatailor.types.__string.__string"
    ]
    """<p>The URL that your player uses to initialize a session that uses client-side reporting.</p>"""
    dual_stack_session_initialization_endpoint_prefix: NotRequired[
        "capo_mediatailor.types.__string.__string"
    ]
    """<p>The dual-stack (IPv4 and IPv6) URL that your player uses to initialize a session that uses client-side reporting.</p>"""
    slate_ad_url: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The URL for a video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID playback configurations. For VPAID, the slate is required because MediaTailor provides it in the slots designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    transcode_profile_name: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.</p>"""
    video_content_source_url: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.</p>"""
    ad_conditioning_configuration: NotRequired[
        "capo_mediatailor.types.ad_conditioning_configuration.AdConditioningConfiguration"
    ]
    """<p>The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads.</p>"""
    ad_decision_server_configuration: NotRequired[
        "capo_mediatailor.types.ad_decision_server_configuration.AdDecisionServerConfiguration"
    ]
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
    """<p>The beaconing configuration for this playback configuration, which controls whether MediaTailor includes beacons of its own in the ad tracking response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackConfiguration) -> dict:
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
        import capo_mediatailor.types.configuration_aliases_response

        out["ConfigurationAliases"] = (
            capo_mediatailor.types.configuration_aliases_response.serialize_json(
                value["configuration_aliases"]
            )
        )
    if "dash_configuration" in value:
        import capo_mediatailor.types.dash_configuration

        out["DashConfiguration"] = (
            capo_mediatailor.types.dash_configuration.serialize_json(
                value["dash_configuration"]
            )
        )
    if "hls_configuration" in value:
        import capo_mediatailor.types.hls_configuration

        out["HlsConfiguration"] = (
            capo_mediatailor.types.hls_configuration.serialize_json(
                value["hls_configuration"]
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
    if "log_configuration" in value:
        import capo_mediatailor.types.log_configuration

        out["LogConfiguration"] = (
            capo_mediatailor.types.log_configuration.serialize_json(
                value["log_configuration"]
            )
        )
    if "manifest_processing_rules" in value:
        import capo_mediatailor.types.manifest_processing_rules

        out["ManifestProcessingRules"] = (
            capo_mediatailor.types.manifest_processing_rules.serialize_json(
                value["manifest_processing_rules"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "personalization_threshold_seconds" in value:
        out["PersonalizationThresholdSeconds"] = value[
            "personalization_threshold_seconds"
        ]
    if "playback_configuration_arn" in value:
        out["PlaybackConfigurationArn"] = value["playback_configuration_arn"]
    if "playback_endpoint_prefix" in value:
        out["PlaybackEndpointPrefix"] = value["playback_endpoint_prefix"]
    if "dual_stack_playback_endpoint_prefix" in value:
        out["DualStackPlaybackEndpointPrefix"] = value[
            "dual_stack_playback_endpoint_prefix"
        ]
    if "session_initialization_endpoint_prefix" in value:
        out["SessionInitializationEndpointPrefix"] = value[
            "session_initialization_endpoint_prefix"
        ]
    if "dual_stack_session_initialization_endpoint_prefix" in value:
        out["DualStackSessionInitializationEndpointPrefix"] = value[
            "dual_stack_session_initialization_endpoint_prefix"
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


def deserialize_json(data: dict) -> PlaybackConfiguration:
    out: PlaybackConfiguration = {}  # type: ignore[typeddict-item]
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
        import capo_mediatailor.types.configuration_aliases_response

        out["configuration_aliases"] = (
            capo_mediatailor.types.configuration_aliases_response.deserialize_json(
                data["ConfigurationAliases"]
            )
        )
    if data.get("DashConfiguration") is not None:
        import capo_mediatailor.types.dash_configuration

        out["dash_configuration"] = (
            capo_mediatailor.types.dash_configuration.deserialize_json(
                data["DashConfiguration"]
            )
        )
    if data.get("HlsConfiguration") is not None:
        import capo_mediatailor.types.hls_configuration

        out["hls_configuration"] = (
            capo_mediatailor.types.hls_configuration.deserialize_json(
                data["HlsConfiguration"]
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
    if data.get("LogConfiguration") is not None:
        import capo_mediatailor.types.log_configuration

        out["log_configuration"] = (
            capo_mediatailor.types.log_configuration.deserialize_json(
                data["LogConfiguration"]
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
    if data.get("PersonalizationThresholdSeconds") is not None:
        out["personalization_threshold_seconds"] = data[
            "PersonalizationThresholdSeconds"
        ]
    if data.get("PlaybackConfigurationArn") is not None:
        out["playback_configuration_arn"] = data["PlaybackConfigurationArn"]
    if data.get("PlaybackEndpointPrefix") is not None:
        out["playback_endpoint_prefix"] = data["PlaybackEndpointPrefix"]
    if data.get("DualStackPlaybackEndpointPrefix") is not None:
        out["dual_stack_playback_endpoint_prefix"] = data[
            "DualStackPlaybackEndpointPrefix"
        ]
    if data.get("SessionInitializationEndpointPrefix") is not None:
        out["session_initialization_endpoint_prefix"] = data[
            "SessionInitializationEndpointPrefix"
        ]
    if data.get("DualStackSessionInitializationEndpointPrefix") is not None:
        out["dual_stack_session_initialization_endpoint_prefix"] = data[
            "DualStackSessionInitializationEndpointPrefix"
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
