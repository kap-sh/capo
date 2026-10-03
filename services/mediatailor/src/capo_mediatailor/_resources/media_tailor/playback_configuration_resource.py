from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_mediatailor._auth._signers
import capo_mediatailor._auth._sigv4
from capo_mediatailor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer_min1
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.ad_conditioning_configuration
    import capo_mediatailor.types.ad_decision_server_configuration
    import capo_mediatailor.types.ads_personalization_concurrency
    import capo_mediatailor.types.ads_personalization_timeouts
    import capo_mediatailor.types.avail_suppression
    import capo_mediatailor.types.bumper
    import capo_mediatailor.types.cdn_configuration
    import capo_mediatailor.types.configuration_aliases_request
    import capo_mediatailor.types.dash_configuration_for_put
    import capo_mediatailor.types.delete_playback_configuration_request
    import capo_mediatailor.types.delete_playback_configuration_response
    import capo_mediatailor.types.function_mapping
    import capo_mediatailor.types.get_playback_configuration_request
    import capo_mediatailor.types.get_playback_configuration_response
    import capo_mediatailor.types.insertion_mode
    import capo_mediatailor.types.list_playback_configurations_request
    import capo_mediatailor.types.list_playback_configurations_response
    import capo_mediatailor.types.live_pre_roll_configuration
    import capo_mediatailor.types.manifest_processing_rules
    import capo_mediatailor.types.max_results
    import capo_mediatailor.types.playback_configuration
    import capo_mediatailor.types.put_playback_configuration_request
    import capo_mediatailor.types.put_playback_configuration_response
    import capo_mediatailor.types.yield_optimization_configuration
    from capo_mediatailor._services.async_media_tailor import (
        AsyncMediaTailorClient,
        AsyncMediaTailorClientConfig,
    )
    from capo_mediatailor._services.media_tailor import (
        MediaTailorClient,
        MediaTailorClientConfig,
    )


class PlaybackConfigurationResource:
    def __init__(self, service: MediaTailorClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        ad_decision_server_url: Optional[
            "capo_mediatailor.types.__string.__string"
        ] = None,
        avail_suppression: Optional[
            "capo_mediatailor.types.avail_suppression.AvailSuppression"
        ] = None,
        bumper: Optional["capo_mediatailor.types.bumper.Bumper"] = None,
        cdn_configuration: Optional[
            "capo_mediatailor.types.cdn_configuration.CdnConfiguration"
        ] = None,
        configuration_aliases: Optional[
            "capo_mediatailor.types.configuration_aliases_request.ConfigurationAliasesRequest"
        ] = None,
        dash_configuration: Optional[
            "capo_mediatailor.types.dash_configuration_for_put.DashConfigurationForPut"
        ] = None,
        insertion_mode: Optional[
            "capo_mediatailor.types.insertion_mode.InsertionMode"
        ] = None,
        live_pre_roll_configuration: Optional[
            "capo_mediatailor.types.live_pre_roll_configuration.LivePreRollConfiguration"
        ] = None,
        manifest_processing_rules: Optional[
            "capo_mediatailor.types.manifest_processing_rules.ManifestProcessingRules"
        ] = None,
        personalization_threshold_seconds: Optional[
            "capo_mediatailor.types.__integer_min1.__integerMin1"
        ] = None,
        slate_ad_url: Optional["capo_mediatailor.types.__string.__string"] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
        transcode_profile_name: Optional[
            "capo_mediatailor.types.__string.__string"
        ] = None,
        video_content_source_url: Optional[
            "capo_mediatailor.types.__string.__string"
        ] = None,
        ad_conditioning_configuration: Optional[
            "capo_mediatailor.types.ad_conditioning_configuration.AdConditioningConfiguration"
        ] = None,
        ad_decision_server_configuration: Optional[
            "capo_mediatailor.types.ad_decision_server_configuration.AdDecisionServerConfiguration"
        ] = None,
        yield_optimization_configuration: Optional[
            "capo_mediatailor.types.yield_optimization_configuration.YieldOptimizationConfiguration"
        ] = None,
        function_mapping: Optional[
            "capo_mediatailor.types.function_mapping.FunctionMapping"
        ] = None,
        ads_personalization_timeouts: Optional[
            "capo_mediatailor.types.ads_personalization_timeouts.AdsPersonalizationTimeouts"
        ] = None,
        ads_personalization_concurrency: Optional[
            "capo_mediatailor.types.ads_personalization_concurrency.AdsPersonalizationConcurrency"
        ] = None,
    ) -> "capo_mediatailor.types.put_playback_configuration_response.PutPlaybackConfigurationResponse":
        """<p>Creates a playback configuration. For information about MediaTailor configurations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html">Working with configurations in AWS Elemental MediaTailor</a>.</p>

        Args:
            ad_decision_server_url: <p>The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.</p>
            avail_suppression: <p>The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html">Ad Suppression</a>.</p>
            bumper: <p>The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html">Bumpers</a>.</p>
            cdn_configuration: <p>The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.</p>
            configuration_aliases: <p>The player parameters and aliases used as dynamic variables during session initialization. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html">Domain Variables</a>.</p>
            dash_configuration: <p>The configuration for DASH content.</p>
            insertion_mode: <p>The setting that controls whether players can use stitched or guided ad insertion. The default, <code>STITCHED_ONLY</code>, forces all player sessions to use stitched (server-side) ad insertion. Choosing <code>PLAYER_SELECT</code> allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.</p>
            live_pre_roll_configuration: <p>The configuration for pre-roll ad insertion.</p>
            manifest_processing_rules: <p>The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.</p>
            name: <p>The identifier for the playback configuration.</p>
            personalization_threshold_seconds: <p>Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to <i>ad replacement</i> in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html">Ad Behavior in AWS Elemental MediaTailor</a>.</p>
            slate_ad_url: <p>The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.</p>
            tags: <p>The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            transcode_profile_name: <p>The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.</p>
            video_content_source_url: <p>The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.</p>
            ad_conditioning_configuration: <p>The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads. </p>
            ad_decision_server_configuration: <p>The configuration for customizing HTTP requests to the ad decision server (ADS). This includes settings for request method, headers, body content, and compression options.</p>
            yield_optimization_configuration: <p>Configuration for Yield Optimization, which fills unsold ad inventory in ad breaks with programmatic ads from Amazon Publisher Services (APS).</p>
            function_mapping: <p>A map of lifecycle hook event names to function identifiers. The function mapping specifies which function MediaTailor executes at each lifecycle hook during ad insertion. Valid keys are <code>PRE_SESSION_INITIALIZATION</code>, <code>PRE_ADS_REQUEST</code>, <code>POST_ADS_RESPONSE</code>, and <code>PRE_MANIFEST_INSERTION</code>. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-hooks.html">Functions lifecycle hooks</a> in the <i>MediaTailor User Guide</i>.</p>
            ads_personalization_timeouts: <p>The timeout settings for ad decision server interactions. These settings control how long MediaTailor waits for ADS responses and the total time budget for ad personalization across live, VOD, and prefetch workflows.</p>
            ads_personalization_concurrency: <p>The concurrency settings for ad decision server interactions. These settings control how many simultaneous ADS requests MediaTailor makes per manifest request.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.put_playback_configuration_request.PutPlaybackConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.put_playback_configuration_response.PutPlaybackConfigurationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.put_playback_configuration

            output, http_response = (
                capo_mediatailor._operations.media_tailor.put_playback_configuration.put_playback_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.put_playback_configuration_request.PutPlaybackConfigurationRequest = {
            "name": name
        }
        if ad_decision_server_url is not None:
            input_["ad_decision_server_url"] = ad_decision_server_url
        if avail_suppression is not None:
            input_["avail_suppression"] = avail_suppression
        if bumper is not None:
            input_["bumper"] = bumper
        if cdn_configuration is not None:
            input_["cdn_configuration"] = cdn_configuration
        if configuration_aliases is not None:
            input_["configuration_aliases"] = configuration_aliases
        if dash_configuration is not None:
            input_["dash_configuration"] = dash_configuration
        if insertion_mode is not None:
            input_["insertion_mode"] = insertion_mode
        if live_pre_roll_configuration is not None:
            input_["live_pre_roll_configuration"] = live_pre_roll_configuration
        if manifest_processing_rules is not None:
            input_["manifest_processing_rules"] = manifest_processing_rules
        if personalization_threshold_seconds is not None:
            input_["personalization_threshold_seconds"] = (
                personalization_threshold_seconds
            )
        if slate_ad_url is not None:
            input_["slate_ad_url"] = slate_ad_url
        if tags is not None:
            input_["tags"] = tags
        if transcode_profile_name is not None:
            input_["transcode_profile_name"] = transcode_profile_name
        if video_content_source_url is not None:
            input_["video_content_source_url"] = video_content_source_url
        if ad_conditioning_configuration is not None:
            input_["ad_conditioning_configuration"] = ad_conditioning_configuration
        if ad_decision_server_configuration is not None:
            input_["ad_decision_server_configuration"] = (
                ad_decision_server_configuration
            )
        if yield_optimization_configuration is not None:
            input_["yield_optimization_configuration"] = (
                yield_optimization_configuration
            )
        if function_mapping is not None:
            input_["function_mapping"] = function_mapping
        if ads_personalization_timeouts is not None:
            input_["ads_personalization_timeouts"] = ads_personalization_timeouts
        if ads_personalization_concurrency is not None:
            input_["ads_personalization_concurrency"] = ads_personalization_concurrency

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.get_playback_configuration_response.GetPlaybackConfigurationResponse":
        """<p>Retrieves a playback configuration. For information about MediaTailor configurations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html">Working with configurations in AWS Elemental MediaTailor</a>.</p>

        Args:
            name: <p>The identifier for the playback configuration.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.get_playback_configuration_request.GetPlaybackConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.get_playback_configuration_response.GetPlaybackConfigurationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_playback_configuration

            output, http_response = (
                capo_mediatailor._operations.media_tailor.get_playback_configuration.get_playback_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_playback_configuration_request.GetPlaybackConfigurationRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_playback_configuration_response.DeletePlaybackConfigurationResponse":
        """<p>Deletes a playback configuration. For information about MediaTailor configurations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html">Working with configurations in AWS Elemental MediaTailor</a>.</p>

        Args:
            name: <p>The name of the playback configuration.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_playback_configuration_request.DeletePlaybackConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_playback_configuration_response.DeletePlaybackConfigurationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_playback_configuration

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_playback_configuration.delete_playback_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_playback_configuration_request.DeletePlaybackConfigurationRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_playback_configurations_response.ListPlaybackConfigurationsResponse":
        """<p>Retrieves existing playback configurations. For information about MediaTailor configurations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html">Working with Configurations in AWS Elemental MediaTailor</a>.</p>

        Args:
            max_results: <p>The maximum number of playback configurations that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> playback configurations, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListPlaybackConfigurations</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_playback_configurations_request.ListPlaybackConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_playback_configurations_response.ListPlaybackConfigurationsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_playback_configurations

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_playback_configurations.list_playback_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_playback_configurations_request.ListPlaybackConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPlaybackConfigurationResource:
    def __init__(self, service: AsyncMediaTailorClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        ad_decision_server_url: Optional[
            "capo_mediatailor.types.__string.__string"
        ] = None,
        avail_suppression: Optional[
            "capo_mediatailor.types.avail_suppression.AvailSuppression"
        ] = None,
        bumper: Optional["capo_mediatailor.types.bumper.Bumper"] = None,
        cdn_configuration: Optional[
            "capo_mediatailor.types.cdn_configuration.CdnConfiguration"
        ] = None,
        configuration_aliases: Optional[
            "capo_mediatailor.types.configuration_aliases_request.ConfigurationAliasesRequest"
        ] = None,
        dash_configuration: Optional[
            "capo_mediatailor.types.dash_configuration_for_put.DashConfigurationForPut"
        ] = None,
        insertion_mode: Optional[
            "capo_mediatailor.types.insertion_mode.InsertionMode"
        ] = None,
        live_pre_roll_configuration: Optional[
            "capo_mediatailor.types.live_pre_roll_configuration.LivePreRollConfiguration"
        ] = None,
        manifest_processing_rules: Optional[
            "capo_mediatailor.types.manifest_processing_rules.ManifestProcessingRules"
        ] = None,
        personalization_threshold_seconds: Optional[
            "capo_mediatailor.types.__integer_min1.__integerMin1"
        ] = None,
        slate_ad_url: Optional["capo_mediatailor.types.__string.__string"] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
        transcode_profile_name: Optional[
            "capo_mediatailor.types.__string.__string"
        ] = None,
        video_content_source_url: Optional[
            "capo_mediatailor.types.__string.__string"
        ] = None,
        ad_conditioning_configuration: Optional[
            "capo_mediatailor.types.ad_conditioning_configuration.AdConditioningConfiguration"
        ] = None,
        ad_decision_server_configuration: Optional[
            "capo_mediatailor.types.ad_decision_server_configuration.AdDecisionServerConfiguration"
        ] = None,
        yield_optimization_configuration: Optional[
            "capo_mediatailor.types.yield_optimization_configuration.YieldOptimizationConfiguration"
        ] = None,
        function_mapping: Optional[
            "capo_mediatailor.types.function_mapping.FunctionMapping"
        ] = None,
        ads_personalization_timeouts: Optional[
            "capo_mediatailor.types.ads_personalization_timeouts.AdsPersonalizationTimeouts"
        ] = None,
        ads_personalization_concurrency: Optional[
            "capo_mediatailor.types.ads_personalization_concurrency.AdsPersonalizationConcurrency"
        ] = None,
    ) -> "capo_mediatailor.types.put_playback_configuration_response.PutPlaybackConfigurationResponse":
        """<p>Creates a playback configuration. For information about MediaTailor configurations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html">Working with configurations in AWS Elemental MediaTailor</a>.</p>

        Args:
            ad_decision_server_url: <p>The URL for the ad decision server (ADS). This includes the specification of static parameters and placeholders for dynamic parameters. AWS Elemental MediaTailor substitutes player-specific and session-specific parameters as needed when calling the ADS. Alternately, for testing you can provide a static VAST URL. The maximum length is 25,000 characters.</p>
            avail_suppression: <p>The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html">Ad Suppression</a>.</p>
            bumper: <p>The configuration for bumpers. Bumpers are short audio or video clips that play at the start or before the end of an ad break. To learn more about bumpers, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html">Bumpers</a>.</p>
            cdn_configuration: <p>The configuration for using a content delivery network (CDN), like Amazon CloudFront, for content and ad segment management.</p>
            configuration_aliases: <p>The player parameters and aliases used as dynamic variables during session initialization. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html">Domain Variables</a>.</p>
            dash_configuration: <p>The configuration for DASH content.</p>
            insertion_mode: <p>The setting that controls whether players can use stitched or guided ad insertion. The default, <code>STITCHED_ONLY</code>, forces all player sessions to use stitched (server-side) ad insertion. Choosing <code>PLAYER_SELECT</code> allows players to select either stitched or guided ad insertion at session-initialization time. The default for players that do not specify an insertion mode is stitched.</p>
            live_pre_roll_configuration: <p>The configuration for pre-roll ad insertion.</p>
            manifest_processing_rules: <p>The configuration for manifest processing rules. Manifest processing rules enable customization of the personalized manifests created by MediaTailor.</p>
            name: <p>The identifier for the playback configuration.</p>
            personalization_threshold_seconds: <p>Defines the maximum duration of underfilled ad time (in seconds) allowed in an ad break. If the duration of underfilled ad time exceeds the personalization threshold, then the personalization of the ad break is abandoned and the underlying content is shown. This feature applies to <i>ad replacement</i> in live and VOD streams, rather than ad insertion, because it relies on an underlying content stream. For more information about ad break behavior, including ad replacement and insertion, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html">Ad Behavior in AWS Elemental MediaTailor</a>.</p>
            slate_ad_url: <p>The URL for a high-quality video asset to transcode and use to fill in time that's not used by ads. AWS Elemental MediaTailor shows the slate to fill in gaps in media content. Configuring the slate is optional for non-VPAID configurations. For VPAID, the slate is required because MediaTailor provides it in the slots that are designated for dynamic ad content. The slate must be a high-quality asset that contains both audio and video.</p>
            tags: <p>The tags to assign to the playback configuration. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            transcode_profile_name: <p>The name that is used to associate this playback configuration with a custom transcode profile. This overrides the dynamic transcoding defaults of MediaTailor. Use this only if you have already set up custom profiles with the help of AWS Support.</p>
            video_content_source_url: <p>The URL prefix for the parent manifest for the stream, minus the asset ID. The maximum length is 512 characters.</p>
            ad_conditioning_configuration: <p>The setting that indicates what conditioning MediaTailor will perform on ads that the ad decision server (ADS) returns, and what priority MediaTailor uses when inserting ads. </p>
            ad_decision_server_configuration: <p>The configuration for customizing HTTP requests to the ad decision server (ADS). This includes settings for request method, headers, body content, and compression options.</p>
            yield_optimization_configuration: <p>Configuration for Yield Optimization, which fills unsold ad inventory in ad breaks with programmatic ads from Amazon Publisher Services (APS).</p>
            function_mapping: <p>A map of lifecycle hook event names to function identifiers. The function mapping specifies which function MediaTailor executes at each lifecycle hook during ad insertion. Valid keys are <code>PRE_SESSION_INITIALIZATION</code>, <code>PRE_ADS_REQUEST</code>, <code>POST_ADS_RESPONSE</code>, and <code>PRE_MANIFEST_INSERTION</code>. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-hooks.html">Functions lifecycle hooks</a> in the <i>MediaTailor User Guide</i>.</p>
            ads_personalization_timeouts: <p>The timeout settings for ad decision server interactions. These settings control how long MediaTailor waits for ADS responses and the total time budget for ad personalization across live, VOD, and prefetch workflows.</p>
            ads_personalization_concurrency: <p>The concurrency settings for ad decision server interactions. These settings control how many simultaneous ADS requests MediaTailor makes per manifest request.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.put_playback_configuration_request.PutPlaybackConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.put_playback_configuration_response.PutPlaybackConfigurationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.put_playback_configuration

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.put_playback_configuration.async_put_playback_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.put_playback_configuration_request.PutPlaybackConfigurationRequest = {
            "name": name
        }
        if ad_decision_server_url is not None:
            input_["ad_decision_server_url"] = ad_decision_server_url
        if avail_suppression is not None:
            input_["avail_suppression"] = avail_suppression
        if bumper is not None:
            input_["bumper"] = bumper
        if cdn_configuration is not None:
            input_["cdn_configuration"] = cdn_configuration
        if configuration_aliases is not None:
            input_["configuration_aliases"] = configuration_aliases
        if dash_configuration is not None:
            input_["dash_configuration"] = dash_configuration
        if insertion_mode is not None:
            input_["insertion_mode"] = insertion_mode
        if live_pre_roll_configuration is not None:
            input_["live_pre_roll_configuration"] = live_pre_roll_configuration
        if manifest_processing_rules is not None:
            input_["manifest_processing_rules"] = manifest_processing_rules
        if personalization_threshold_seconds is not None:
            input_["personalization_threshold_seconds"] = (
                personalization_threshold_seconds
            )
        if slate_ad_url is not None:
            input_["slate_ad_url"] = slate_ad_url
        if tags is not None:
            input_["tags"] = tags
        if transcode_profile_name is not None:
            input_["transcode_profile_name"] = transcode_profile_name
        if video_content_source_url is not None:
            input_["video_content_source_url"] = video_content_source_url
        if ad_conditioning_configuration is not None:
            input_["ad_conditioning_configuration"] = ad_conditioning_configuration
        if ad_decision_server_configuration is not None:
            input_["ad_decision_server_configuration"] = (
                ad_decision_server_configuration
            )
        if yield_optimization_configuration is not None:
            input_["yield_optimization_configuration"] = (
                yield_optimization_configuration
            )
        if function_mapping is not None:
            input_["function_mapping"] = function_mapping
        if ads_personalization_timeouts is not None:
            input_["ads_personalization_timeouts"] = ads_personalization_timeouts
        if ads_personalization_concurrency is not None:
            input_["ads_personalization_concurrency"] = ads_personalization_concurrency

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.get_playback_configuration_response.GetPlaybackConfigurationResponse":
        """<p>Retrieves a playback configuration. For information about MediaTailor configurations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html">Working with configurations in AWS Elemental MediaTailor</a>.</p>

        Args:
            name: <p>The identifier for the playback configuration.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.get_playback_configuration_request.GetPlaybackConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.get_playback_configuration_response.GetPlaybackConfigurationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_playback_configuration

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.get_playback_configuration.async_get_playback_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_playback_configuration_request.GetPlaybackConfigurationRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_playback_configuration_response.DeletePlaybackConfigurationResponse":
        """<p>Deletes a playback configuration. For information about MediaTailor configurations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html">Working with configurations in AWS Elemental MediaTailor</a>.</p>

        Args:
            name: <p>The name of the playback configuration.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.delete_playback_configuration_request.DeletePlaybackConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.delete_playback_configuration_response.DeletePlaybackConfigurationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_playback_configuration

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.delete_playback_configuration.async_delete_playback_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_playback_configuration_request.DeletePlaybackConfigurationRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_playback_configurations_response.ListPlaybackConfigurationsResponse":
        """<p>Retrieves existing playback configurations. For information about MediaTailor configurations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html">Working with Configurations in AWS Elemental MediaTailor</a>.</p>

        Args:
            max_results: <p>The maximum number of playback configurations that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> playback configurations, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListPlaybackConfigurations</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.list_playback_configurations_request.ListPlaybackConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.list_playback_configurations_response.ListPlaybackConfigurationsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_playback_configurations

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.list_playback_configurations.async_list_playback_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_playback_configurations_request.ListPlaybackConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
