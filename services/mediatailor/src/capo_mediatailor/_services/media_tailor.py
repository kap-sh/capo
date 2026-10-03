"""Generated from Smithy shape ``com.amazonaws.mediatailor#MediaTailor``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_mediatailor._auth._signers
import capo_mediatailor._auth._sigv4
from capo_mediatailor._auth._identity import Credentials
from capo_mediatailor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mediatailor._auth._zapros_handler import AuthMiddleware
from capo_mediatailor._pagination import resolve_path as _resolve_path
from capo_mediatailor._resources.media_tailor.channel_resource import ChannelResource
from capo_mediatailor._resources.media_tailor.function_resource import FunctionResource
from capo_mediatailor._resources.media_tailor.live_source_resource import (
    LiveSourceResource,
)
from capo_mediatailor._resources.media_tailor.playback_configuration_resource import (
    PlaybackConfigurationResource,
)
from capo_mediatailor._resources.media_tailor.prefetch_schedule_resource import (
    PrefetchScheduleResource,
)
from capo_mediatailor._resources.media_tailor.source_location_resource import (
    SourceLocationResource,
)
from capo_mediatailor._resources.media_tailor.vod_source_resource import (
    VodSourceResource,
)
from capo_mediatailor._services._aws_config import aws_config
from capo_mediatailor._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer
    import capo_mediatailor.types.__integer_min1
    import capo_mediatailor.types.__integer_min1_max100
    import capo_mediatailor.types.__list_of__string
    import capo_mediatailor.types.__list_of_ad_break
    import capo_mediatailor.types.__list_of_audience_media
    import capo_mediatailor.types.__list_of_logging_strategies
    import capo_mediatailor.types.__list_of_segment_delivery_configuration
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.access_configuration
    import capo_mediatailor.types.ad_conditioning_configuration
    import capo_mediatailor.types.ad_decision_server_configuration
    import capo_mediatailor.types.ads_interaction_log
    import capo_mediatailor.types.ads_personalization_concurrency
    import capo_mediatailor.types.ads_personalization_timeouts
    import capo_mediatailor.types.alert
    import capo_mediatailor.types.audiences
    import capo_mediatailor.types.avail_suppression
    import capo_mediatailor.types.aws_service_request_configuration
    import capo_mediatailor.types.bumper
    import capo_mediatailor.types.cdn_configuration
    import capo_mediatailor.types.channel
    import capo_mediatailor.types.concurrent_executor_configuration
    import capo_mediatailor.types.configuration_aliases_request
    import capo_mediatailor.types.configure_logs_for_channel_request
    import capo_mediatailor.types.configure_logs_for_channel_response
    import capo_mediatailor.types.configure_logs_for_playback_configuration_request
    import capo_mediatailor.types.configure_logs_for_playback_configuration_response
    import capo_mediatailor.types.create_channel_request
    import capo_mediatailor.types.create_channel_response
    import capo_mediatailor.types.create_live_source_request
    import capo_mediatailor.types.create_live_source_response
    import capo_mediatailor.types.create_prefetch_schedule_request
    import capo_mediatailor.types.create_prefetch_schedule_response
    import capo_mediatailor.types.create_program_request
    import capo_mediatailor.types.create_program_response
    import capo_mediatailor.types.create_source_location_request
    import capo_mediatailor.types.create_source_location_response
    import capo_mediatailor.types.create_vod_source_request
    import capo_mediatailor.types.create_vod_source_response
    import capo_mediatailor.types.custom_output_configuration
    import capo_mediatailor.types.dash_configuration_for_put
    import capo_mediatailor.types.default_segment_delivery_configuration
    import capo_mediatailor.types.delete_channel_policy_request
    import capo_mediatailor.types.delete_channel_policy_response
    import capo_mediatailor.types.delete_channel_request
    import capo_mediatailor.types.delete_channel_response
    import capo_mediatailor.types.delete_function_request
    import capo_mediatailor.types.delete_function_response
    import capo_mediatailor.types.delete_live_source_request
    import capo_mediatailor.types.delete_live_source_response
    import capo_mediatailor.types.delete_playback_configuration_request
    import capo_mediatailor.types.delete_playback_configuration_response
    import capo_mediatailor.types.delete_prefetch_schedule_request
    import capo_mediatailor.types.delete_prefetch_schedule_response
    import capo_mediatailor.types.delete_program_request
    import capo_mediatailor.types.delete_program_response
    import capo_mediatailor.types.delete_source_location_request
    import capo_mediatailor.types.delete_source_location_response
    import capo_mediatailor.types.delete_vod_source_request
    import capo_mediatailor.types.delete_vod_source_response
    import capo_mediatailor.types.describe_channel_request
    import capo_mediatailor.types.describe_channel_response
    import capo_mediatailor.types.describe_live_source_request
    import capo_mediatailor.types.describe_live_source_response
    import capo_mediatailor.types.describe_program_request
    import capo_mediatailor.types.describe_program_response
    import capo_mediatailor.types.describe_source_location_request
    import capo_mediatailor.types.describe_source_location_response
    import capo_mediatailor.types.describe_vod_source_request
    import capo_mediatailor.types.describe_vod_source_response
    import capo_mediatailor.types.function
    import capo_mediatailor.types.function_mapping
    import capo_mediatailor.types.function_type
    import capo_mediatailor.types.get_channel_policy_request
    import capo_mediatailor.types.get_channel_policy_response
    import capo_mediatailor.types.get_channel_schedule_request
    import capo_mediatailor.types.get_channel_schedule_response
    import capo_mediatailor.types.get_function_request
    import capo_mediatailor.types.get_function_response
    import capo_mediatailor.types.get_playback_configuration_request
    import capo_mediatailor.types.get_playback_configuration_response
    import capo_mediatailor.types.get_prefetch_schedule_request
    import capo_mediatailor.types.get_prefetch_schedule_response
    import capo_mediatailor.types.http_configuration
    import capo_mediatailor.types.http_package_configurations
    import capo_mediatailor.types.http_request_configuration
    import capo_mediatailor.types.insertion_mode
    import capo_mediatailor.types.list_alerts_request
    import capo_mediatailor.types.list_alerts_response
    import capo_mediatailor.types.list_channels_request
    import capo_mediatailor.types.list_channels_response
    import capo_mediatailor.types.list_functions_request
    import capo_mediatailor.types.list_functions_response
    import capo_mediatailor.types.list_live_sources_request
    import capo_mediatailor.types.list_live_sources_response
    import capo_mediatailor.types.list_playback_configurations_request
    import capo_mediatailor.types.list_playback_configurations_response
    import capo_mediatailor.types.list_prefetch_schedule_type
    import capo_mediatailor.types.list_prefetch_schedules_request
    import capo_mediatailor.types.list_prefetch_schedules_response
    import capo_mediatailor.types.list_source_locations_request
    import capo_mediatailor.types.list_source_locations_response
    import capo_mediatailor.types.list_tags_for_resource_request
    import capo_mediatailor.types.list_tags_for_resource_response
    import capo_mediatailor.types.list_vod_sources_request
    import capo_mediatailor.types.list_vod_sources_response
    import capo_mediatailor.types.live_pre_roll_configuration
    import capo_mediatailor.types.live_source
    import capo_mediatailor.types.log_types
    import capo_mediatailor.types.manifest_processing_rules
    import capo_mediatailor.types.manifest_service_interaction_log
    import capo_mediatailor.types.max_results
    import capo_mediatailor.types.playback_configuration
    import capo_mediatailor.types.playback_mode
    import capo_mediatailor.types.prefetch_consumption
    import capo_mediatailor.types.prefetch_retrieval
    import capo_mediatailor.types.prefetch_schedule
    import capo_mediatailor.types.prefetch_schedule_type
    import capo_mediatailor.types.put_channel_policy_request
    import capo_mediatailor.types.put_channel_policy_response
    import capo_mediatailor.types.put_function_request
    import capo_mediatailor.types.put_function_response
    import capo_mediatailor.types.put_playback_configuration_request
    import capo_mediatailor.types.put_playback_configuration_response
    import capo_mediatailor.types.recurring_prefetch_configuration
    import capo_mediatailor.types.request_outputs
    import capo_mediatailor.types.schedule_configuration
    import capo_mediatailor.types.schedule_entry
    import capo_mediatailor.types.sequential_executor_configuration
    import capo_mediatailor.types.slate_source
    import capo_mediatailor.types.source_location
    import capo_mediatailor.types.start_channel_request
    import capo_mediatailor.types.start_channel_response
    import capo_mediatailor.types.stop_channel_request
    import capo_mediatailor.types.stop_channel_response
    import capo_mediatailor.types.tag_resource_request
    import capo_mediatailor.types.tier
    import capo_mediatailor.types.time_shift_configuration
    import capo_mediatailor.types.untag_resource_request
    import capo_mediatailor.types.update_channel_request
    import capo_mediatailor.types.update_channel_response
    import capo_mediatailor.types.update_live_source_request
    import capo_mediatailor.types.update_live_source_response
    import capo_mediatailor.types.update_program_request
    import capo_mediatailor.types.update_program_response
    import capo_mediatailor.types.update_program_schedule_configuration
    import capo_mediatailor.types.update_source_location_request
    import capo_mediatailor.types.update_source_location_response
    import capo_mediatailor.types.update_vod_source_request
    import capo_mediatailor.types.update_vod_source_response
    import capo_mediatailor.types.vast_request_configuration
    import capo_mediatailor.types.vod_source
    import capo_mediatailor.types.yield_optimization_configuration


class MediaTailorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class MediaTailorClient:
    """A client for the ``MediaTailor`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = MediaTailorClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.channel_resource = ChannelResource(self)
        self.function_resource = FunctionResource(self)
        self.live_source_resource = LiveSourceResource(self)
        self.playback_configuration_resource = PlaybackConfigurationResource(self)
        self.prefetch_schedule_resource = PrefetchScheduleResource(self)
        self.source_location_resource = SourceLocationResource(self)
        self.vod_source_resource = VodSourceResource(self)

    def operation_options(
        self, config_overrides: Optional[MediaTailorClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MediaTailorClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def configure_logs_for_playback_configuration(
        self,
        percent_enabled: "capo_mediatailor.types.__integer.__integer",
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        enabled_logging_strategies: Optional[
            "capo_mediatailor.types.__list_of_logging_strategies.__listOfLoggingStrategies"
        ] = None,
        ads_interaction_log: Optional[
            "capo_mediatailor.types.ads_interaction_log.AdsInteractionLog"
        ] = None,
        manifest_service_interaction_log: Optional[
            "capo_mediatailor.types.manifest_service_interaction_log.ManifestServiceInteractionLog"
        ] = None,
    ) -> "capo_mediatailor.types.configure_logs_for_playback_configuration_response.ConfigureLogsForPlaybackConfigurationResponse":
        """<p>Defines where AWS Elemental MediaTailor sends logs for the playback configuration.</p>

        Args:
            percent_enabled: <p>The percentage of session logs that MediaTailor sends to your CloudWatch Logs account. For example, if your playback configuration has 1000 sessions and percentEnabled is set to <code>60</code>, MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html">debug log mode</a>.</p> <p>Valid values: <code>0</code> - <code>100</code> </p>
            playback_configuration_name: <p>The name of the playback configuration.</p>
            enabled_logging_strategies: <p>The method used for collecting logs from AWS Elemental MediaTailor. To configure MediaTailor to send logs directly to Amazon CloudWatch Logs, choose <code>LEGACY_CLOUDWATCH</code>. To configure MediaTailor to send logs to CloudWatch, which then vends the logs to your destination of choice, choose <code>VENDED_LOGS</code>. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.</p> <p>To use vended logs, you must configure the delivery destination in Amazon CloudWatch, as described in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-vended-logs-permissions-V2">Enable logging from AWS services, Logging that requires additional permissions [V2]</a>.</p>
            ads_interaction_log: <p>The event types that MediaTailor emits in logs for interactions with the ADS.</p>
            manifest_service_interaction_log: <p>The event types that MediaTailor emits in logs for interactions with the origin server.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.configure_logs_for_playback_configuration_request.ConfigureLogsForPlaybackConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.configure_logs_for_playback_configuration_response.ConfigureLogsForPlaybackConfigurationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.configure_logs_for_playback_configuration

            output, http_response = (
                capo_mediatailor._operations.media_tailor.configure_logs_for_playback_configuration.configure_logs_for_playback_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.configure_logs_for_playback_configuration_request.ConfigureLogsForPlaybackConfigurationRequest = {
            "percent_enabled": percent_enabled,
            "playback_configuration_name": playback_configuration_name,
        }
        if enabled_logging_strategies is not None:
            input_["enabled_logging_strategies"] = enabled_logging_strategies
        if ads_interaction_log is not None:
            input_["ads_interaction_log"] = ads_interaction_log
        if manifest_service_interaction_log is not None:
            input_["manifest_service_interaction_log"] = (
                manifest_service_interaction_log
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_alerts(
        self,
        resource_arn: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_alerts_response.ListAlertsResponse":
        """<p>Lists the alerts that are associated with a MediaTailor channel assembly resource.</p>

        Args:
            max_results: <p>The maximum number of alerts that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> alerts, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListAlerts</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_alerts_request.ListAlertsRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_alerts_response.ListAlertsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_alerts

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_alerts.list_alerts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_alerts_request.ListAlertsRequest = {
            "resource_arn": resource_arn
        }
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

    def iter_list_alerts(
        self,
        resource_arn: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediatailor.types.alert.Alert]":
        _token = next_token
        while True:
            _response = self.list_alerts(
                resource_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>A list of tags that are associated with this resource. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with this resource.</p>

        Raises:
            capo_mediatailor.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data.</p>
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_tags_for_resource

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_mediatailor.types.__string.__string",
        tags: "capo_mediatailor.types.__map_of__string.__mapOf__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> None:
        """<p>The resource to tag. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource.</p>
            tags: <p>The tags to assign to the resource. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data.</p>
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mediatailor._operations.media_tailor.tag_resource

            output, http_response = (
                capo_mediatailor._operations.media_tailor.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_mediatailor.types.__string.__string",
        tag_keys: "capo_mediatailor.types.__list_of__string.__listOf__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> None:
        """<p>The resource to untag.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to untag.</p>
            tag_keys: <p>The tag keys associated with the resource.</p>

        Raises:
            capo_mediatailor.errors.bad_request_exception.BadRequestException: <p>A request contains unexpected data.</p>
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mediatailor._operations.media_tailor.untag_resource

            output, http_response = (
                capo_mediatailor._operations.media_tailor.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        outputs: "capo_mediatailor.types.request_outputs.RequestOutputs",
        playback_mode: "capo_mediatailor.types.playback_mode.PlaybackMode",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        filler_slate: Optional[
            "capo_mediatailor.types.slate_source.SlateSource"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
        tier: Optional["capo_mediatailor.types.tier.Tier"] = None,
        time_shift_configuration: Optional[
            "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
        ] = None,
        audiences: Optional["capo_mediatailor.types.audiences.Audiences"] = None,
    ) -> "capo_mediatailor.types.create_channel_response.CreateChannelResponse":
        """<p>Creates a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            filler_slate: <p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>
            outputs: <p>The channel's output properties.</p>
            playback_mode: <p>The type of playback mode to use for this channel.</p> <p> <code>LINEAR</code> - The programs in the schedule play once back-to-back in the schedule.</p> <p> <code>LOOP</code> - The programs in the schedule play back-to-back in an endless loop. When the last program in the schedule stops playing, playback loops back to the first program in the schedule.</p>
            tags: <p>The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            tier: <p>The tier of the channel.</p>
            time_shift_configuration: <p> The time-shifted viewing configuration you want to associate to the channel. </p>
            audiences: <p>The list of audiences defined in channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_channel_request.CreateChannelRequest = {
            "channel_name": channel_name,
            "outputs": outputs,
            "playback_mode": playback_mode,
        }
        if filler_slate is not None:
            input_["filler_slate"] = filler_slate
        if tags is not None:
            input_["tags"] = tags
        if tier is not None:
            input_["tier"] = tier
        if time_shift_configuration is not None:
            input_["time_shift_configuration"] = time_shift_configuration
        if audiences is not None:
            input_["audiences"] = audiences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.describe_channel_response.DescribeChannelResponse":
        """<p>Describes a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.describe_channel_request.DescribeChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.describe_channel_response.DescribeChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.describe_channel.describe_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_channel_request.DescribeChannelRequest = {
            "channel_name": channel_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        outputs: "capo_mediatailor.types.request_outputs.RequestOutputs",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        filler_slate: Optional[
            "capo_mediatailor.types.slate_source.SlateSource"
        ] = None,
        time_shift_configuration: Optional[
            "capo_mediatailor.types.time_shift_configuration.TimeShiftConfiguration"
        ] = None,
        audiences: Optional["capo_mediatailor.types.audiences.Audiences"] = None,
    ) -> "capo_mediatailor.types.update_channel_response.UpdateChannelResponse":
        """<p>Updates a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            filler_slate: <p>The slate used to fill gaps between programs in the schedule. You must configure filler slate if your channel uses the <code>LINEAR</code> <code>PlaybackMode</code>. MediaTailor doesn't support filler slate for channels using the <code>LOOP</code> <code>PlaybackMode</code>.</p>
            outputs: <p>The channel's output properties.</p>
            time_shift_configuration: <p> The time-shifted viewing configuration you want to associate to the channel. </p>
            audiences: <p>The list of audiences defined in channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.update_channel_response.UpdateChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_channel_request.UpdateChannelRequest = {
            "channel_name": channel_name,
            "outputs": outputs,
        }
        if filler_slate is not None:
            input_["filler_slate"] = filler_slate
        if time_shift_configuration is not None:
            input_["time_shift_configuration"] = time_shift_configuration
        if audiences is not None:
            input_["audiences"] = audiences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_channel_response.DeleteChannelResponse":
        """<p>Deletes a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_channel_response.DeleteChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_channel_request.DeleteChannelRequest = {
            "channel_name": channel_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_channels(
        self,
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_channels_response.ListChannelsResponse":
        """<p>Retrieves information about the channels that are associated with the current AWS account.</p>

        Args:
            max_results: <p>The maximum number of channels that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> channels, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListChannels</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_channels

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_channels_request.ListChannelsRequest = {}
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

    def iter_list_channels(
        self,
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediatailor.types.channel.Channel]":
        _token = next_token
        while True:
            _response = self.list_channels(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def configure_logs_for_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        log_types: "capo_mediatailor.types.log_types.LogTypes",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.configure_logs_for_channel_response.ConfigureLogsForChannelResponse":
        """<p>Configures Amazon CloudWatch log settings for a channel.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            log_types: <p>The types of logs to collect.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.configure_logs_for_channel_request.ConfigureLogsForChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.configure_logs_for_channel_response.ConfigureLogsForChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.configure_logs_for_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.configure_logs_for_channel.configure_logs_for_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.configure_logs_for_channel_request.ConfigureLogsForChannelRequest = {
            "channel_name": channel_name,
            "log_types": log_types,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channel_schedule(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        duration_minutes: Optional["capo_mediatailor.types.__string.__string"] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
        audience: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.get_channel_schedule_response.GetChannelScheduleResponse":
        """<p>Retrieves information about your channel's schedule.</p>

        Args:
            channel_name: <p>The name of the channel associated with this Channel Schedule.</p>
            duration_minutes: <p>The duration in minutes of the channel schedule.</p>
            max_results: <p>The maximum number of channel schedules that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> channel schedules, use the value of <code>NextToken</code> in the response to get the next page of results.</p>
            next_token: <p>(Optional) If the playback configuration has more than <code>MaxResults</code> channel schedules, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>GetChannelScheduleRequest</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p> <p>If the previous response didn't include a <code>NextToken</code> element, there are no more channel schedules to get.</p>
            audience: <p>The single audience for GetChannelScheduleRequest.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.get_channel_schedule_request.GetChannelScheduleRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.get_channel_schedule_response.GetChannelScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_channel_schedule

            output, http_response = (
                capo_mediatailor._operations.media_tailor.get_channel_schedule.get_channel_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_channel_schedule_request.GetChannelScheduleRequest = {
            "channel_name": channel_name
        }
        if duration_minutes is not None:
            input_["duration_minutes"] = duration_minutes
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if audience is not None:
            input_["audience"] = audience

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_channel_schedule(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        duration_minutes: Optional["capo_mediatailor.types.__string.__string"] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
        audience: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediatailor.types.schedule_entry.ScheduleEntry]":
        _token = next_token
        while True:
            _response = self.get_channel_schedule(
                channel_name,
                config_overrides=config_overrides,
                duration_minutes=duration_minutes,
                max_results=max_results,
                next_token=_token,
                audience=audience,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.start_channel_response.StartChannelResponse":
        """<p>Starts a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.start_channel_request.StartChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.start_channel_response.StartChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.start_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.start_channel.start_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.start_channel_request.StartChannelRequest = {
            "channel_name": channel_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_channel(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.stop_channel_response.StopChannelResponse":
        """<p>Stops a channel. For information about MediaTailor channels, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html">Working with channels</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.stop_channel_request.StopChannelRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.stop_channel_response.StopChannelResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.stop_channel

            output, http_response = (
                capo_mediatailor._operations.media_tailor.stop_channel.stop_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.stop_channel_request.StopChannelRequest = {
            "channel_name": channel_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_channel_policy(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        policy: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.put_channel_policy_response.PutChannelPolicyResponse":
        """<p>Creates an IAM policy for the channel. IAM policies are used to control access to your channel.</p>

        Args:
            channel_name: <p>The channel name associated with this Channel Policy.</p>
            policy: <p>Adds an IAM role that determines the permissions of your channel.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.put_channel_policy_request.PutChannelPolicyRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.put_channel_policy_response.PutChannelPolicyResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.put_channel_policy

            output, http_response = (
                capo_mediatailor._operations.media_tailor.put_channel_policy.put_channel_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.put_channel_policy_request.PutChannelPolicyRequest = {
            "channel_name": channel_name,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_channel_policy(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.get_channel_policy_response.GetChannelPolicyResponse":
        """<p>Returns the channel's IAM policy. IAM policies are used to control access to your channel.</p>

        Args:
            channel_name: <p>The name of the channel associated with this Channel Policy.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.get_channel_policy_request.GetChannelPolicyRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.get_channel_policy_response.GetChannelPolicyResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_channel_policy

            output, http_response = (
                capo_mediatailor._operations.media_tailor.get_channel_policy.get_channel_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_channel_policy_request.GetChannelPolicyRequest = {
            "channel_name": channel_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel_policy(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_channel_policy_response.DeleteChannelPolicyResponse":
        """<p>The channel policy to delete.</p>

        Args:
            channel_name: <p>The name of the channel associated with this channel policy.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_channel_policy_request.DeleteChannelPolicyRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_channel_policy_response.DeleteChannelPolicyResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_channel_policy

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_channel_policy.delete_channel_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_channel_policy_request.DeleteChannelPolicyRequest = {
            "channel_name": channel_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_program(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        program_name: "capo_mediatailor.types.__string.__string",
        schedule_configuration: "capo_mediatailor.types.schedule_configuration.ScheduleConfiguration",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        ad_breaks: Optional[
            "capo_mediatailor.types.__list_of_ad_break.__listOfAdBreak"
        ] = None,
        live_source_name: Optional["capo_mediatailor.types.__string.__string"] = None,
        vod_source_name: Optional["capo_mediatailor.types.__string.__string"] = None,
        audience_media: Optional[
            "capo_mediatailor.types.__list_of_audience_media.__listOfAudienceMedia"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_program_response.CreateProgramResponse":
        """<p>Creates a program within a channel. For information about programs, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html">Working with programs</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            ad_breaks: <p>The ad break configuration settings.</p>
            channel_name: <p>The name of the channel for this Program.</p>
            live_source_name: <p>The name of the LiveSource for this Program.</p>
            program_name: <p>The name of the Program.</p>
            schedule_configuration: <p>The schedule configuration settings.</p>
            source_location_name: <p>The name of the source location.</p>
            vod_source_name: <p>The name that's used to refer to a VOD source.</p>
            audience_media: <p>The list of AudienceMedia defined in program.</p>
            tags: <p>The tags to assign to the program. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_program_request.CreateProgramRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_program_response.CreateProgramResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_program

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_program.create_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_program_request.CreateProgramRequest = {
            "channel_name": channel_name,
            "program_name": program_name,
            "schedule_configuration": schedule_configuration,
            "source_location_name": source_location_name,
        }
        if ad_breaks is not None:
            input_["ad_breaks"] = ad_breaks
        if live_source_name is not None:
            input_["live_source_name"] = live_source_name
        if vod_source_name is not None:
            input_["vod_source_name"] = vod_source_name
        if audience_media is not None:
            input_["audience_media"] = audience_media
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_program(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        program_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.describe_program_response.DescribeProgramResponse":
        """<p>Describes a program within a channel. For information about programs, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html">Working with programs</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel associated with this Program.</p>
            program_name: <p>The name of the program.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.describe_program_request.DescribeProgramRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.describe_program_response.DescribeProgramResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_program

            output, http_response = (
                capo_mediatailor._operations.media_tailor.describe_program.describe_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_program_request.DescribeProgramRequest = {
            "channel_name": channel_name,
            "program_name": program_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_program(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        program_name: "capo_mediatailor.types.__string.__string",
        schedule_configuration: "capo_mediatailor.types.update_program_schedule_configuration.UpdateProgramScheduleConfiguration",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        ad_breaks: Optional[
            "capo_mediatailor.types.__list_of_ad_break.__listOfAdBreak"
        ] = None,
        audience_media: Optional[
            "capo_mediatailor.types.__list_of_audience_media.__listOfAudienceMedia"
        ] = None,
    ) -> "capo_mediatailor.types.update_program_response.UpdateProgramResponse":
        """<p>Updates a program within a channel.</p>

        Args:
            ad_breaks: <p>The ad break configuration settings.</p>
            channel_name: <p>The name of the channel for this Program.</p>
            program_name: <p>The name of the Program.</p>
            schedule_configuration: <p>The schedule configuration settings.</p>
            audience_media: <p>The list of AudienceMedia defined in program.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.update_program_request.UpdateProgramRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.update_program_response.UpdateProgramResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_program

            output, http_response = (
                capo_mediatailor._operations.media_tailor.update_program.update_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_program_request.UpdateProgramRequest = {
            "channel_name": channel_name,
            "program_name": program_name,
            "schedule_configuration": schedule_configuration,
        }
        if ad_breaks is not None:
            input_["ad_breaks"] = ad_breaks
        if audience_media is not None:
            input_["audience_media"] = audience_media

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_program(
        self,
        channel_name: "capo_mediatailor.types.__string.__string",
        program_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_program_response.DeleteProgramResponse":
        """<p>Deletes a program within a channel. For information about programs, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html">Working with programs</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            channel_name: <p>The name of the channel.</p>
            program_name: <p>The name of the program.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_program_request.DeleteProgramRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_program_response.DeleteProgramResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_program

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_program.delete_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_program_request.DeleteProgramRequest = {
            "channel_name": channel_name,
            "program_name": program_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_function(
        self,
        function_id: "capo_mediatailor.types.__string.__string",
        function_type: "capo_mediatailor.types.function_type.FunctionType",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        description: Optional["capo_mediatailor.types.__string.__string"] = None,
        http_request_configuration: Optional[
            "capo_mediatailor.types.http_request_configuration.HttpRequestConfiguration"
        ] = None,
        aws_service_request_configuration: Optional[
            "capo_mediatailor.types.aws_service_request_configuration.AwsServiceRequestConfiguration"
        ] = None,
        custom_output_configuration: Optional[
            "capo_mediatailor.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        concurrent_executor_configuration: Optional[
            "capo_mediatailor.types.concurrent_executor_configuration.ConcurrentExecutorConfiguration"
        ] = None,
        sequential_executor_configuration: Optional[
            "capo_mediatailor.types.sequential_executor_configuration.SequentialExecutorConfiguration"
        ] = None,
        vast_request_configuration: Optional[
            "capo_mediatailor.types.vast_request_configuration.VastRequestConfiguration"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.put_function_response.PutFunctionResponse":
        """<p>Creates or updates a function. A function defines reusable logic that MediaTailor executes at lifecycle hooks during ad insertion. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function. The identifier must be unique within your account.</p>
            function_type: <p>The type of the function, which determines what the function can do at runtime. Valid values:</p> <ul> <li> <p> <code>CUSTOM_OUTPUT</code> – Evaluates expressions and produces output bindings with no external calls.</p> </li> <li> <p> <code>HTTP_REQUEST</code> – Makes an HTTP call to an external service and evaluates output expressions that can reference the response.</p> </li> <li> <p> <code>AWS_SERVICE_REQUEST</code> – Makes an authenticated request to a supported AWS service API and evaluates output expressions that can reference the response.</p> </li> <li> <p> <code>VAST_REQUEST</code> – Calls a VAST endpoint, parses the response as VAST, and makes the parsed ads available to output expressions.</p> </li> <li> <p> <code>SEQUENTIAL_EXECUTOR</code> – Runs a sequence of child functions in order, passing data between steps through temporary data.</p> </li> <li> <p> <code>CONCURRENT_EXECUTOR</code> – Runs a set of child functions in parallel, up to a maximum concurrency, and combines their output when all functions complete.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types.html">Function types and composition</a> in the <i>MediaTailor User Guide</i>.</p>
            description: <p>A description of the function.</p>
            http_request_configuration: <p>The configuration for an <code>HTTP_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>HTTP_REQUEST</code>.</p>
            aws_service_request_configuration: <p>The configuration for an <code>AWS_SERVICE_REQUEST</code> function. You must specify this parameter when <code>FunctionType</code> is <code>AWS_SERVICE_REQUEST</code>.</p>
            custom_output_configuration: <p>The configuration for a <code>CUSTOM_OUTPUT</code> function. Specifies the runtime and output expressions. Required when <code>FunctionType</code> is <code>CUSTOM_OUTPUT</code>.</p>
            concurrent_executor_configuration: <p>The configuration for a <code>CONCURRENT_EXECUTOR</code> function. Specifies the list of child functions to run in parallel, the maximum concurrency, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>CONCURRENT_EXECUTOR</code>.</p>
            sequential_executor_configuration: <p>The configuration for a <code>SEQUENTIAL_EXECUTOR</code> function. Specifies the ordered list of child functions to execute, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>SEQUENTIAL_EXECUTOR</code>.</p>
            vast_request_configuration: <p>The configuration for a <code>VAST_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>VAST_REQUEST</code>.</p>
            tags: <p>The tags to assign to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.put_function_request.PutFunctionRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.put_function_response.PutFunctionResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.put_function

            output, http_response = (
                capo_mediatailor._operations.media_tailor.put_function.put_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.put_function_request.PutFunctionRequest = {
            "function_id": function_id,
            "function_type": function_type,
        }
        if description is not None:
            input_["description"] = description
        if http_request_configuration is not None:
            input_["http_request_configuration"] = http_request_configuration
        if aws_service_request_configuration is not None:
            input_["aws_service_request_configuration"] = (
                aws_service_request_configuration
            )
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if concurrent_executor_configuration is not None:
            input_["concurrent_executor_configuration"] = (
                concurrent_executor_configuration
            )
        if sequential_executor_configuration is not None:
            input_["sequential_executor_configuration"] = (
                sequential_executor_configuration
            )
        if vast_request_configuration is not None:
            input_["vast_request_configuration"] = vast_request_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_function(
        self,
        function_id: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.get_function_response.GetFunctionResponse":
        """<p>Retrieves the configuration and metadata for a function. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.get_function_request.GetFunctionRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.get_function_response.GetFunctionResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_function

            output, http_response = (
                capo_mediatailor._operations.media_tailor.get_function.get_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_function_request.GetFunctionRequest = {
            "function_id": function_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_function(
        self,
        function_id: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_function_response.DeleteFunctionResponse":
        """<p>Deletes a function. MediaTailor prevents deletion of a function that is still referenced by a playback configuration or by another function. Remove all references before deleting. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function to delete.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_function

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_function_request.DeleteFunctionRequest = {
            "function_id": function_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_functions(
        self,
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_functions_response.ListFunctionsResponse":
        """<p>Retrieves all functions associated with your AWS account in the current Region. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of functions that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> functions, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses token-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListFunctions</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_functions_request.ListFunctionsRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_functions_response.ListFunctionsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_functions

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_functions.list_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_functions_request.ListFunctionsRequest = {}
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

    def iter_list_functions(
        self,
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediatailor.types.function.Function]":
        _token = next_token
        while True:
            _response = self.list_functions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_live_source(
        self,
        http_package_configurations: "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        live_source_name: "capo_mediatailor.types.__string.__string",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_live_source_response.CreateLiveSourceResponse":
        """<p>The live source configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configuration parameters for this live source.</p>
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location.</p>
            tags: <p>The tags to assign to the live source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_live_source_request.CreateLiveSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_live_source_response.CreateLiveSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_live_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_live_source.create_live_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_live_source_request.CreateLiveSourceRequest = {
            "http_package_configurations": http_package_configurations,
            "live_source_name": live_source_name,
            "source_location_name": source_location_name,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_live_source(
        self,
        live_source_name: "capo_mediatailor.types.__string.__string",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.describe_live_source_response.DescribeLiveSourceResponse":
        """<p>The live source to describe.</p>

        Args:
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location associated with this Live Source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.describe_live_source_request.DescribeLiveSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.describe_live_source_response.DescribeLiveSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_live_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.describe_live_source.describe_live_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_live_source_request.DescribeLiveSourceRequest = {
            "live_source_name": live_source_name,
            "source_location_name": source_location_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_live_source(
        self,
        http_package_configurations: "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        live_source_name: "capo_mediatailor.types.__string.__string",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.update_live_source_response.UpdateLiveSourceResponse":
        """<p>Updates a live source's configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configurations for the live source on this account.</p>
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location associated with this Live Source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.update_live_source_request.UpdateLiveSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.update_live_source_response.UpdateLiveSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_live_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.update_live_source.update_live_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_live_source_request.UpdateLiveSourceRequest = {
            "http_package_configurations": http_package_configurations,
            "live_source_name": live_source_name,
            "source_location_name": source_location_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_live_source(
        self,
        live_source_name: "capo_mediatailor.types.__string.__string",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_live_source_response.DeleteLiveSourceResponse":
        """<p>The live source to delete.</p>

        Args:
            live_source_name: <p>The name of the live source.</p>
            source_location_name: <p>The name of the source location associated with this Live Source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_live_source_request.DeleteLiveSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_live_source_response.DeleteLiveSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_live_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_live_source.delete_live_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_live_source_request.DeleteLiveSourceRequest = {
            "live_source_name": live_source_name,
            "source_location_name": source_location_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_live_sources(
        self,
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_live_sources_response.ListLiveSourcesResponse":
        """<p>Lists the live sources contained in a source location. A source represents a piece of content.</p>

        Args:
            max_results: <p>The maximum number of live sources that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> live sources, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListLiveSources</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            source_location_name: <p>The name of the source location associated with this Live Sources list.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_live_sources_request.ListLiveSourcesRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_live_sources_response.ListLiveSourcesResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_live_sources

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_live_sources.list_live_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_live_sources_request.ListLiveSourcesRequest = {
            "source_location_name": source_location_name
        }
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

    def iter_list_live_sources(
        self,
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediatailor.types.live_source.LiveSource]":
        _token = next_token
        while True:
            _response = self.list_live_sources(
                source_location_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_playback_configuration(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def get_playback_configuration(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def delete_playback_configuration(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def list_playback_configurations(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_playback_configurations(
        self,
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> (
        "Iterator[capo_mediatailor.types.playback_configuration.PlaybackConfiguration]"
    ):
        _token = next_token
        while True:
            _response = self.list_playback_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_prefetch_schedule(
        self,
        name: "capo_mediatailor.types.__string.__string",
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        consumption: Optional[
            "capo_mediatailor.types.prefetch_consumption.PrefetchConsumption"
        ] = None,
        retrieval: Optional[
            "capo_mediatailor.types.prefetch_retrieval.PrefetchRetrieval"
        ] = None,
        recurring_prefetch_configuration: Optional[
            "capo_mediatailor.types.recurring_prefetch_configuration.RecurringPrefetchConfiguration"
        ] = None,
        schedule_type: Optional[
            "capo_mediatailor.types.prefetch_schedule_type.PrefetchScheduleType"
        ] = None,
        stream_id: Optional["capo_mediatailor.types.__string.__string"] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_prefetch_schedule_response.CreatePrefetchScheduleResponse":
        """<p>Creates a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Using ad prefetching</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            consumption: <p>The configuration settings for how and when MediaTailor consumes prefetched ads from the ad decision server for single prefetch schedules. Each consumption configuration contains an end time and an optional start time that define the <i>consumption window</i>. Prefetch schedules automatically expire no earlier than seven days after the end time.</p>
            name: <p>The name to assign to the schedule request.</p>
            playback_configuration_name: <p>The name to assign to the playback configuration.</p>
            retrieval: <p>The configuration settings for retrieval of prefetched ads from the ad decision server. Only one set of prefetched ads will be retrieved and subsequently consumed for each ad break.</p>
            recurring_prefetch_configuration: <p>The configuration that defines how and when MediaTailor performs ad prefetching in a live event.</p>
            schedule_type: <p>The frequency that MediaTailor creates prefetch schedules. <code>SINGLE</code> indicates that this schedule applies to one ad break. <code>RECURRING</code> indicates that MediaTailor automatically creates a schedule for each ad avail in a live event.</p> <p>For more information about the prefetch types and when you might use each, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Prefetching ads in Elemental MediaTailor.</a> </p>
            stream_id: <p>An optional stream identifier that MediaTailor uses to prefetch ads for multiple streams that use the same playback configuration. If <code>StreamId</code> is specified, MediaTailor returns all of the prefetch schedules with an exact match on <code>StreamId</code>. If not specified, MediaTailor returns all of the prefetch schedules for the playback configuration, regardless of <code>StreamId</code>.</p>
            tags: <p>The tags to assign to the prefetch schedule. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_prefetch_schedule_request.CreatePrefetchScheduleRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_prefetch_schedule_response.CreatePrefetchScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_prefetch_schedule

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_prefetch_schedule.create_prefetch_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_prefetch_schedule_request.CreatePrefetchScheduleRequest = {
            "name": name,
            "playback_configuration_name": playback_configuration_name,
        }
        if consumption is not None:
            input_["consumption"] = consumption
        if retrieval is not None:
            input_["retrieval"] = retrieval
        if recurring_prefetch_configuration is not None:
            input_["recurring_prefetch_configuration"] = (
                recurring_prefetch_configuration
            )
        if schedule_type is not None:
            input_["schedule_type"] = schedule_type
        if stream_id is not None:
            input_["stream_id"] = stream_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_prefetch_schedule(
        self,
        name: "capo_mediatailor.types.__string.__string",
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.get_prefetch_schedule_response.GetPrefetchScheduleResponse":
        """<p>Retrieves a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Using ad prefetching</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            name: <p>The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.</p>
            playback_configuration_name: <p>Returns information about the prefetch schedule for a specific playback configuration. If you call <code>GetPrefetchSchedule</code> on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.get_prefetch_schedule_request.GetPrefetchScheduleRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.get_prefetch_schedule_response.GetPrefetchScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_prefetch_schedule

            output, http_response = (
                capo_mediatailor._operations.media_tailor.get_prefetch_schedule.get_prefetch_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_prefetch_schedule_request.GetPrefetchScheduleRequest = {
            "name": name,
            "playback_configuration_name": playback_configuration_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_prefetch_schedule(
        self,
        name: "capo_mediatailor.types.__string.__string",
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_prefetch_schedule_response.DeletePrefetchScheduleResponse":
        """<p>Deletes a prefetch schedule for a specific playback configuration. If you call <code>DeletePrefetchSchedule</code> on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code. For more information about ad prefetching, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Using ad prefetching</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            name: <p>The name of the prefetch schedule. If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.</p>
            playback_configuration_name: <p>The name of the playback configuration for this prefetch schedule.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_prefetch_schedule_request.DeletePrefetchScheduleRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_prefetch_schedule_response.DeletePrefetchScheduleResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_prefetch_schedule

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_prefetch_schedule.delete_prefetch_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_prefetch_schedule_request.DeletePrefetchScheduleRequest = {
            "name": name,
            "playback_configuration_name": playback_configuration_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_prefetch_schedules(
        self,
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional[
            "capo_mediatailor.types.__integer_min1_max100.__integerMin1Max100"
        ] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
        schedule_type: Optional[
            "capo_mediatailor.types.list_prefetch_schedule_type.ListPrefetchScheduleType"
        ] = None,
        stream_id: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_prefetch_schedules_response.ListPrefetchSchedulesResponse":
        """<p>Lists the prefetch schedules for a playback configuration.</p>

        Args:
            max_results: <p>The maximum number of prefetch schedules that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> prefetch schedules, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListPrefetchSchedules</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            playback_configuration_name: <p>Retrieves the prefetch schedule(s) for a specific playback configuration.</p>
            schedule_type: <p>The type of prefetch schedules that you want to list. <code>SINGLE</code> indicates that you want to list the configured single prefetch schedules. <code>RECURRING</code> indicates that you want to list the configured recurring prefetch schedules. <code>ALL</code> indicates that you want to list all configured prefetch schedules.</p>
            stream_id: <p>An optional filtering parameter whereby MediaTailor filters the prefetch schedules to include only specific streams.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_prefetch_schedules_request.ListPrefetchSchedulesRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_prefetch_schedules_response.ListPrefetchSchedulesResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_prefetch_schedules

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_prefetch_schedules.list_prefetch_schedules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_prefetch_schedules_request.ListPrefetchSchedulesRequest = {
            "playback_configuration_name": playback_configuration_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if schedule_type is not None:
            input_["schedule_type"] = schedule_type
        if stream_id is not None:
            input_["stream_id"] = stream_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_prefetch_schedules(
        self,
        playback_configuration_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional[
            "capo_mediatailor.types.__integer_min1_max100.__integerMin1Max100"
        ] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
        schedule_type: Optional[
            "capo_mediatailor.types.list_prefetch_schedule_type.ListPrefetchScheduleType"
        ] = None,
        stream_id: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediatailor.types.prefetch_schedule.PrefetchSchedule]":
        _token = next_token
        while True:
            _response = self.list_prefetch_schedules(
                playback_configuration_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                schedule_type=schedule_type,
                stream_id=stream_id,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_source_location(
        self,
        http_configuration: "capo_mediatailor.types.http_configuration.HttpConfiguration",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        access_configuration: Optional[
            "capo_mediatailor.types.access_configuration.AccessConfiguration"
        ] = None,
        default_segment_delivery_configuration: Optional[
            "capo_mediatailor.types.default_segment_delivery_configuration.DefaultSegmentDeliveryConfiguration"
        ] = None,
        segment_delivery_configurations: Optional[
            "capo_mediatailor.types.__list_of_segment_delivery_configuration.__listOfSegmentDeliveryConfiguration"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_source_location_response.CreateSourceLocationResponse":
        """<p>Creates a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            access_configuration: <p>Access configuration parameters. Configures the type of authentication used to access content from your source location.</p>
            default_segment_delivery_configuration: <p>The optional configuration for the server that serves segments.</p>
            http_configuration: <p>The source's HTTP package configurations.</p>
            segment_delivery_configurations: <p>A list of the segment delivery configurations associated with this resource.</p>
            source_location_name: <p>The name associated with the source location.</p>
            tags: <p>The tags to assign to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_source_location_request.CreateSourceLocationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_source_location_response.CreateSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_source_location

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_source_location.create_source_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_source_location_request.CreateSourceLocationRequest = {
            "http_configuration": http_configuration,
            "source_location_name": source_location_name,
        }
        if access_configuration is not None:
            input_["access_configuration"] = access_configuration
        if default_segment_delivery_configuration is not None:
            input_["default_segment_delivery_configuration"] = (
                default_segment_delivery_configuration
            )
        if segment_delivery_configurations is not None:
            input_["segment_delivery_configurations"] = segment_delivery_configurations
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_source_location(
        self,
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.describe_source_location_response.DescribeSourceLocationResponse":
        """<p>Describes a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            source_location_name: <p>The name of the source location.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.describe_source_location_request.DescribeSourceLocationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.describe_source_location_response.DescribeSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_source_location

            output, http_response = (
                capo_mediatailor._operations.media_tailor.describe_source_location.describe_source_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_source_location_request.DescribeSourceLocationRequest = {
            "source_location_name": source_location_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_source_location(
        self,
        http_configuration: "capo_mediatailor.types.http_configuration.HttpConfiguration",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        access_configuration: Optional[
            "capo_mediatailor.types.access_configuration.AccessConfiguration"
        ] = None,
        default_segment_delivery_configuration: Optional[
            "capo_mediatailor.types.default_segment_delivery_configuration.DefaultSegmentDeliveryConfiguration"
        ] = None,
        segment_delivery_configurations: Optional[
            "capo_mediatailor.types.__list_of_segment_delivery_configuration.__listOfSegmentDeliveryConfiguration"
        ] = None,
    ) -> "capo_mediatailor.types.update_source_location_response.UpdateSourceLocationResponse":
        """<p>Updates a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            access_configuration: <p>Access configuration parameters. Configures the type of authentication used to access content from your source location.</p>
            default_segment_delivery_configuration: <p>The optional configuration for the host server that serves segments.</p>
            http_configuration: <p>The HTTP configuration for the source location.</p>
            segment_delivery_configurations: <p>A list of the segment delivery configurations associated with this resource.</p>
            source_location_name: <p>The name of the source location.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.update_source_location_request.UpdateSourceLocationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.update_source_location_response.UpdateSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_source_location

            output, http_response = (
                capo_mediatailor._operations.media_tailor.update_source_location.update_source_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_source_location_request.UpdateSourceLocationRequest = {
            "http_configuration": http_configuration,
            "source_location_name": source_location_name,
        }
        if access_configuration is not None:
            input_["access_configuration"] = access_configuration
        if default_segment_delivery_configuration is not None:
            input_["default_segment_delivery_configuration"] = (
                default_segment_delivery_configuration
            )
        if segment_delivery_configurations is not None:
            input_["segment_delivery_configurations"] = segment_delivery_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_source_location(
        self,
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_source_location_response.DeleteSourceLocationResponse":
        """<p>Deletes a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            source_location_name: <p>The name of the source location.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_source_location_request.DeleteSourceLocationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_source_location_response.DeleteSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_source_location

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_source_location.delete_source_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_source_location_request.DeleteSourceLocationRequest = {
            "source_location_name": source_location_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_source_locations(
        self,
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_source_locations_response.ListSourceLocationsResponse":
        """<p>Lists the source locations for a channel. A source location defines the host server URL, and contains a list of sources.</p>

        Args:
            max_results: <p> The maximum number of source locations that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> source locations, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListSourceLocations</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_source_locations_request.ListSourceLocationsRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_source_locations_response.ListSourceLocationsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_source_locations

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_source_locations.list_source_locations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_source_locations_request.ListSourceLocationsRequest = {}
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

    def iter_list_source_locations(
        self,
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediatailor.types.source_location.SourceLocation]":
        _token = next_token
        while True:
            _response = self.list_source_locations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_vod_source(
        self,
        http_package_configurations: "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        source_location_name: "capo_mediatailor.types.__string.__string",
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_vod_source_response.CreateVodSourceResponse":
        """<p>The VOD source configuration parameters.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configuration parameters for this VOD source.</p>
            source_location_name: <p>The name of the source location for this VOD source.</p>
            tags: <p>The tags to assign to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            vod_source_name: <p>The name associated with the VOD source.&gt;</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_vod_source_request.CreateVodSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_vod_source_response.CreateVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_vod_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_vod_source.create_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_vod_source_request.CreateVodSourceRequest = {
            "http_package_configurations": http_package_configurations,
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_vod_source(
        self,
        source_location_name: "capo_mediatailor.types.__string.__string",
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> (
        "capo_mediatailor.types.describe_vod_source_response.DescribeVodSourceResponse"
    ):
        """<p>Provides details about a specific video on demand (VOD) source in a specific source location.</p>

        Args:
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD Source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.describe_vod_source_request.DescribeVodSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.describe_vod_source_response.DescribeVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_vod_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.describe_vod_source.describe_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_vod_source_request.DescribeVodSourceRequest = {
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_vod_source(
        self,
        http_package_configurations: "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        source_location_name: "capo_mediatailor.types.__string.__string",
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.update_vod_source_response.UpdateVodSourceResponse":
        """<p>Updates a VOD source's configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configurations for the VOD source on this account.</p>
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.update_vod_source_request.UpdateVodSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.update_vod_source_response.UpdateVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_vod_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.update_vod_source.update_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_vod_source_request.UpdateVodSourceRequest = {
            "http_package_configurations": http_package_configurations,
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vod_source(
        self,
        source_location_name: "capo_mediatailor.types.__string.__string",
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_vod_source_response.DeleteVodSourceResponse":
        """<p>The video on demand (VOD) source to delete.</p>

        Args:
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_vod_source_request.DeleteVodSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_vod_source_response.DeleteVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_vod_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_vod_source.delete_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_vod_source_request.DeleteVodSourceRequest = {
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_vod_sources(
        self,
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_vod_sources_response.ListVodSourcesResponse":
        """<p>Lists the VOD sources contained in a source location. A source represents a piece of content.</p>

        Args:
            max_results: <p> The maximum number of VOD sources that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> VOD sources, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListVodSources</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            source_location_name: <p>The name of the source location associated with this VOD Source list.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_vod_sources_request.ListVodSourcesRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_vod_sources_response.ListVodSourcesResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_vod_sources

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_vod_sources.list_vod_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_vod_sources_request.ListVodSourcesRequest = {
            "source_location_name": source_location_name
        }
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

    def iter_list_vod_sources(
        self,
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediatailor.types.vod_source.VodSource]":
        _token = next_token
        while True:
            _response = self.list_vod_sources(
                source_location_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
