"""Generated from Smithy shape ``com.amazonaws.mediapackage#MediaPackage``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_mediapackage._auth._signers
import capo_mediapackage._auth._sigv4
from capo_mediapackage._auth._identity import Credentials
from capo_mediapackage._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mediapackage._auth._zapros_handler import AuthMiddleware
from capo_mediapackage._pagination import resolve_path as _resolve_path
from capo_mediapackage._services._aws_config import aws_config
from capo_mediapackage._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_mediapackage.types.__integer
    import capo_mediapackage.types.__list_of__string
    import capo_mediapackage.types.__map_of__string
    import capo_mediapackage.types.__string
    import capo_mediapackage.types.authorization
    import capo_mediapackage.types.channel
    import capo_mediapackage.types.cmaf_package_create_or_update_parameters
    import capo_mediapackage.types.configure_logs_request
    import capo_mediapackage.types.configure_logs_response
    import capo_mediapackage.types.create_channel_request
    import capo_mediapackage.types.create_channel_response
    import capo_mediapackage.types.create_harvest_job_request
    import capo_mediapackage.types.create_harvest_job_response
    import capo_mediapackage.types.create_origin_endpoint_request
    import capo_mediapackage.types.create_origin_endpoint_response
    import capo_mediapackage.types.dash_package
    import capo_mediapackage.types.delete_channel_request
    import capo_mediapackage.types.delete_channel_response
    import capo_mediapackage.types.delete_origin_endpoint_request
    import capo_mediapackage.types.delete_origin_endpoint_response
    import capo_mediapackage.types.describe_channel_request
    import capo_mediapackage.types.describe_channel_response
    import capo_mediapackage.types.describe_harvest_job_request
    import capo_mediapackage.types.describe_harvest_job_response
    import capo_mediapackage.types.describe_origin_endpoint_request
    import capo_mediapackage.types.describe_origin_endpoint_response
    import capo_mediapackage.types.egress_access_logs
    import capo_mediapackage.types.harvest_job
    import capo_mediapackage.types.hls_package
    import capo_mediapackage.types.ingress_access_logs
    import capo_mediapackage.types.list_channels_request
    import capo_mediapackage.types.list_channels_response
    import capo_mediapackage.types.list_harvest_jobs_request
    import capo_mediapackage.types.list_harvest_jobs_response
    import capo_mediapackage.types.list_origin_endpoints_request
    import capo_mediapackage.types.list_origin_endpoints_response
    import capo_mediapackage.types.list_tags_for_resource_request
    import capo_mediapackage.types.list_tags_for_resource_response
    import capo_mediapackage.types.max_results
    import capo_mediapackage.types.mss_package
    import capo_mediapackage.types.origin_endpoint
    import capo_mediapackage.types.origination
    import capo_mediapackage.types.rotate_channel_credentials_request
    import capo_mediapackage.types.rotate_channel_credentials_response
    import capo_mediapackage.types.rotate_ingest_endpoint_credentials_request
    import capo_mediapackage.types.rotate_ingest_endpoint_credentials_response
    import capo_mediapackage.types.s3_destination
    import capo_mediapackage.types.tag_resource_request
    import capo_mediapackage.types.tags
    import capo_mediapackage.types.untag_resource_request
    import capo_mediapackage.types.update_channel_request
    import capo_mediapackage.types.update_channel_response
    import capo_mediapackage.types.update_origin_endpoint_request
    import capo_mediapackage.types.update_origin_endpoint_response


class MediaPackageClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class MediaPackageClient:
    """A client for the ``MediaPackage`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = MediaPackageClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[MediaPackageClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MediaPackageClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def configure_logs(
        self,
        id: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        egress_access_logs: Optional[
            "capo_mediapackage.types.egress_access_logs.EgressAccessLogs"
        ] = None,
        ingress_access_logs: Optional[
            "capo_mediapackage.types.ingress_access_logs.IngressAccessLogs"
        ] = None,
    ) -> "capo_mediapackage.types.configure_logs_response.ConfigureLogsResponse":
        """Changes the Channel's properities to configure log subscription

        Args:
            id: The ID of the channel to log subscription.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.configure_logs_request.ConfigureLogsRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.configure_logs_response.ConfigureLogsResponse"
        ]:
            import capo_mediapackage._operations.media_package.configure_logs

            output, http_response = (
                capo_mediapackage._operations.media_package.configure_logs.configure_logs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.configure_logs_request.ConfigureLogsRequest = {
            "id": id
        }
        if egress_access_logs is not None:
            input_["egress_access_logs"] = egress_access_logs
        if ingress_access_logs is not None:
            input_["ingress_access_logs"] = ingress_access_logs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel(
        self,
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        description: Optional["capo_mediapackage.types.__string.__string"] = None,
        id: Optional["capo_mediapackage.types.__string.__string"] = None,
        tags: Optional["capo_mediapackage.types.tags.Tags"] = None,
    ) -> "capo_mediapackage.types.create_channel_response.CreateChannelResponse":
        """Creates a new Channel.

        Args:
            description: A short text description of the Channel.
            id: The ID of the Channel. The ID must be unique within the region and it cannot be changed after a Channel is created.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_mediapackage._operations.media_package.create_channel

            output, http_response = (
                capo_mediapackage._operations.media_package.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.create_channel_request.CreateChannelRequest = {}
        if description is not None:
            input_["description"] = description
        if id is not None:
            input_["id"] = id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_harvest_job(
        self,
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        end_time: Optional["capo_mediapackage.types.__string.__string"] = None,
        id: Optional["capo_mediapackage.types.__string.__string"] = None,
        origin_endpoint_id: Optional[
            "capo_mediapackage.types.__string.__string"
        ] = None,
        s3_destination: Optional[
            "capo_mediapackage.types.s3_destination.S3Destination"
        ] = None,
        start_time: Optional["capo_mediapackage.types.__string.__string"] = None,
    ) -> "capo_mediapackage.types.create_harvest_job_response.CreateHarvestJobResponse":
        """Creates a new HarvestJob record.

        Args:
            end_time: The end of the time-window which will be harvested
            id: The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted
            origin_endpoint_id: The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted.
            start_time: The start of the time-window which will be harvested

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.create_harvest_job_request.CreateHarvestJobRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.create_harvest_job_response.CreateHarvestJobResponse"
        ]:
            import capo_mediapackage._operations.media_package.create_harvest_job

            output, http_response = (
                capo_mediapackage._operations.media_package.create_harvest_job.create_harvest_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.create_harvest_job_request.CreateHarvestJobRequest = {}
        if end_time is not None:
            input_["end_time"] = end_time
        if id is not None:
            input_["id"] = id
        if origin_endpoint_id is not None:
            input_["origin_endpoint_id"] = origin_endpoint_id
        if s3_destination is not None:
            input_["s3_destination"] = s3_destination
        if start_time is not None:
            input_["start_time"] = start_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_origin_endpoint(
        self,
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        authorization: Optional[
            "capo_mediapackage.types.authorization.Authorization"
        ] = None,
        channel_id: Optional["capo_mediapackage.types.__string.__string"] = None,
        cmaf_package: Optional[
            "capo_mediapackage.types.cmaf_package_create_or_update_parameters.CmafPackageCreateOrUpdateParameters"
        ] = None,
        dash_package: Optional[
            "capo_mediapackage.types.dash_package.DashPackage"
        ] = None,
        description: Optional["capo_mediapackage.types.__string.__string"] = None,
        hls_package: Optional["capo_mediapackage.types.hls_package.HlsPackage"] = None,
        id: Optional["capo_mediapackage.types.__string.__string"] = None,
        manifest_name: Optional["capo_mediapackage.types.__string.__string"] = None,
        mss_package: Optional["capo_mediapackage.types.mss_package.MssPackage"] = None,
        origination: Optional["capo_mediapackage.types.origination.Origination"] = None,
        startover_window_seconds: Optional[
            "capo_mediapackage.types.__integer.__integer"
        ] = None,
        tags: Optional["capo_mediapackage.types.tags.Tags"] = None,
        time_delay_seconds: Optional[
            "capo_mediapackage.types.__integer.__integer"
        ] = None,
        whitelist: Optional[
            "capo_mediapackage.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_mediapackage.types.create_origin_endpoint_response.CreateOriginEndpointResponse":
        """Creates a new OriginEndpoint record.

        Args:
            channel_id: The ID of the Channel that the OriginEndpoint will be associated with. This cannot be changed after the OriginEndpoint is created.
            description: A short text description of the OriginEndpoint.
            id: The ID of the OriginEndpoint. The ID must be unique within the region and it cannot be changed after the OriginEndpoint is created.
            manifest_name: A short string that will be used as the filename of the OriginEndpoint URL (defaults to "index").
            origination: Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
            startover_window_seconds: Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
            time_delay_seconds: Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
            whitelist: A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.create_origin_endpoint_request.CreateOriginEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.create_origin_endpoint_response.CreateOriginEndpointResponse"
        ]:
            import capo_mediapackage._operations.media_package.create_origin_endpoint

            output, http_response = (
                capo_mediapackage._operations.media_package.create_origin_endpoint.create_origin_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.create_origin_endpoint_request.CreateOriginEndpointRequest = {}
        if authorization is not None:
            input_["authorization"] = authorization
        if channel_id is not None:
            input_["channel_id"] = channel_id
        if cmaf_package is not None:
            input_["cmaf_package"] = cmaf_package
        if dash_package is not None:
            input_["dash_package"] = dash_package
        if description is not None:
            input_["description"] = description
        if hls_package is not None:
            input_["hls_package"] = hls_package
        if id is not None:
            input_["id"] = id
        if manifest_name is not None:
            input_["manifest_name"] = manifest_name
        if mss_package is not None:
            input_["mss_package"] = mss_package
        if origination is not None:
            input_["origination"] = origination
        if startover_window_seconds is not None:
            input_["startover_window_seconds"] = startover_window_seconds
        if tags is not None:
            input_["tags"] = tags
        if time_delay_seconds is not None:
            input_["time_delay_seconds"] = time_delay_seconds
        if whitelist is not None:
            input_["whitelist"] = whitelist

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel(
        self,
        id: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
    ) -> "capo_mediapackage.types.delete_channel_response.DeleteChannelResponse":
        """Deletes an existing Channel.

        Args:
            id: The ID of the Channel to delete.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.delete_channel_response.DeleteChannelResponse"
        ]:
            import capo_mediapackage._operations.media_package.delete_channel

            output, http_response = (
                capo_mediapackage._operations.media_package.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.delete_channel_request.DeleteChannelRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_origin_endpoint(
        self,
        id: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
    ) -> "capo_mediapackage.types.delete_origin_endpoint_response.DeleteOriginEndpointResponse":
        """Deletes an existing OriginEndpoint.

        Args:
            id: The ID of the OriginEndpoint to delete.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.delete_origin_endpoint_request.DeleteOriginEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.delete_origin_endpoint_response.DeleteOriginEndpointResponse"
        ]:
            import capo_mediapackage._operations.media_package.delete_origin_endpoint

            output, http_response = (
                capo_mediapackage._operations.media_package.delete_origin_endpoint.delete_origin_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.delete_origin_endpoint_request.DeleteOriginEndpointRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel(
        self,
        id: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
    ) -> "capo_mediapackage.types.describe_channel_response.DescribeChannelResponse":
        """Gets details about a Channel.

        Args:
            id: The ID of a Channel.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.describe_channel_request.DescribeChannelRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.describe_channel_response.DescribeChannelResponse"
        ]:
            import capo_mediapackage._operations.media_package.describe_channel

            output, http_response = (
                capo_mediapackage._operations.media_package.describe_channel.describe_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.describe_channel_request.DescribeChannelRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_harvest_job(
        self,
        id: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
    ) -> "capo_mediapackage.types.describe_harvest_job_response.DescribeHarvestJobResponse":
        """Gets details about an existing HarvestJob.

        Args:
            id: The ID of the HarvestJob.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.describe_harvest_job_request.DescribeHarvestJobRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.describe_harvest_job_response.DescribeHarvestJobResponse"
        ]:
            import capo_mediapackage._operations.media_package.describe_harvest_job

            output, http_response = (
                capo_mediapackage._operations.media_package.describe_harvest_job.describe_harvest_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.describe_harvest_job_request.DescribeHarvestJobRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_origin_endpoint(
        self,
        id: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
    ) -> "capo_mediapackage.types.describe_origin_endpoint_response.DescribeOriginEndpointResponse":
        """Gets details about an existing OriginEndpoint.

        Args:
            id: The ID of the OriginEndpoint.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.describe_origin_endpoint_request.DescribeOriginEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.describe_origin_endpoint_response.DescribeOriginEndpointResponse"
        ]:
            import capo_mediapackage._operations.media_package.describe_origin_endpoint

            output, http_response = (
                capo_mediapackage._operations.media_package.describe_origin_endpoint.describe_origin_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.describe_origin_endpoint_request.DescribeOriginEndpointRequest = {
            "id": id
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
        config_overrides: Optional[MediaPackageClientConfig] = None,
        max_results: Optional["capo_mediapackage.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediapackage.types.__string.__string"] = None,
    ) -> "capo_mediapackage.types.list_channels_response.ListChannelsResponse":
        """Returns a collection of Channels.

        Args:
            max_results: Upper bound on number of records to return.
            next_token: A token used to resume pagination from the end of a previous request.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_mediapackage._operations.media_package.list_channels

            output, http_response = (
                capo_mediapackage._operations.media_package.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.list_channels_request.ListChannelsRequest = {}
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
        config_overrides: Optional[MediaPackageClientConfig] = None,
        max_results: Optional["capo_mediapackage.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediapackage.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediapackage.types.channel.Channel]":
        _token = next_token
        while True:
            _response = self.list_channels(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channels",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_harvest_jobs(
        self,
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        include_channel_id: Optional[
            "capo_mediapackage.types.__string.__string"
        ] = None,
        include_status: Optional["capo_mediapackage.types.__string.__string"] = None,
        max_results: Optional["capo_mediapackage.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediapackage.types.__string.__string"] = None,
    ) -> "capo_mediapackage.types.list_harvest_jobs_response.ListHarvestJobsResponse":
        """Returns a collection of HarvestJob records.

        Args:
            include_channel_id: When specified, the request will return only HarvestJobs associated with the given Channel ID.
            include_status: When specified, the request will return only HarvestJobs in the given status.
            max_results: The upper bound on the number of records to return.
            next_token: A token used to resume pagination from the end of a previous request.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.list_harvest_jobs_request.ListHarvestJobsRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.list_harvest_jobs_response.ListHarvestJobsResponse"
        ]:
            import capo_mediapackage._operations.media_package.list_harvest_jobs

            output, http_response = (
                capo_mediapackage._operations.media_package.list_harvest_jobs.list_harvest_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.list_harvest_jobs_request.ListHarvestJobsRequest = {}
        if include_channel_id is not None:
            input_["include_channel_id"] = include_channel_id
        if include_status is not None:
            input_["include_status"] = include_status
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

    def iter_list_harvest_jobs(
        self,
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        include_channel_id: Optional[
            "capo_mediapackage.types.__string.__string"
        ] = None,
        include_status: Optional["capo_mediapackage.types.__string.__string"] = None,
        max_results: Optional["capo_mediapackage.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediapackage.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediapackage.types.harvest_job.HarvestJob]":
        _token = next_token
        while True:
            _response = self.list_harvest_jobs(
                config_overrides=config_overrides,
                include_channel_id=include_channel_id,
                include_status=include_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("harvest_jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_origin_endpoints(
        self,
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        channel_id: Optional["capo_mediapackage.types.__string.__string"] = None,
        max_results: Optional["capo_mediapackage.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediapackage.types.__string.__string"] = None,
    ) -> "capo_mediapackage.types.list_origin_endpoints_response.ListOriginEndpointsResponse":
        """Returns a collection of OriginEndpoint records.

        Args:
            channel_id: When specified, the request will return only OriginEndpoints associated with the given Channel ID.
            max_results: The upper bound on the number of records to return.
            next_token: A token used to resume pagination from the end of a previous request.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.list_origin_endpoints_request.ListOriginEndpointsRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.list_origin_endpoints_response.ListOriginEndpointsResponse"
        ]:
            import capo_mediapackage._operations.media_package.list_origin_endpoints

            output, http_response = (
                capo_mediapackage._operations.media_package.list_origin_endpoints.list_origin_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.list_origin_endpoints_request.ListOriginEndpointsRequest = {}
        if channel_id is not None:
            input_["channel_id"] = channel_id
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

    def iter_list_origin_endpoints(
        self,
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        channel_id: Optional["capo_mediapackage.types.__string.__string"] = None,
        max_results: Optional["capo_mediapackage.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediapackage.types.__string.__string"] = None,
    ) -> "Iterator[capo_mediapackage.types.origin_endpoint.OriginEndpoint]":
        _token = next_token
        while True:
            _response = self.list_origin_endpoints(
                config_overrides=config_overrides,
                channel_id=channel_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("origin_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
    ) -> "capo_mediapackage.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        def _handler(
            req: "OperationRequest[capo_mediapackage.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mediapackage._operations.media_package.list_tags_for_resource

            output, http_response = (
                capo_mediapackage._operations.media_package.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def rotate_channel_credentials(
        self,
        id: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
    ) -> "capo_mediapackage.types.rotate_channel_credentials_response.RotateChannelCredentialsResponse":
        """Changes the Channel's first IngestEndpoint's username and password. WARNING - This API is deprecated. Please use RotateIngestEndpointCredentials instead

        Args:
            id: The ID of the channel to update.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.rotate_channel_credentials_request.RotateChannelCredentialsRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.rotate_channel_credentials_response.RotateChannelCredentialsResponse"
        ]:
            import capo_mediapackage._operations.media_package.rotate_channel_credentials

            output, http_response = (
                capo_mediapackage._operations.media_package.rotate_channel_credentials.rotate_channel_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.rotate_channel_credentials_request.RotateChannelCredentialsRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def rotate_ingest_endpoint_credentials(
        self,
        id: "capo_mediapackage.types.__string.__string",
        ingest_endpoint_id: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
    ) -> "capo_mediapackage.types.rotate_ingest_endpoint_credentials_response.RotateIngestEndpointCredentialsResponse":
        """Rotate the IngestEndpoint's username and password, as specified by the IngestEndpoint's id.

        Args:
            id: The ID of the channel the IngestEndpoint is on.
            ingest_endpoint_id: The id of the IngestEndpoint whose credentials should be rotated

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.rotate_ingest_endpoint_credentials_request.RotateIngestEndpointCredentialsRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.rotate_ingest_endpoint_credentials_response.RotateIngestEndpointCredentialsResponse"
        ]:
            import capo_mediapackage._operations.media_package.rotate_ingest_endpoint_credentials

            output, http_response = (
                capo_mediapackage._operations.media_package.rotate_ingest_endpoint_credentials.rotate_ingest_endpoint_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.rotate_ingest_endpoint_credentials_request.RotateIngestEndpointCredentialsRequest = {
            "id": id,
            "ingest_endpoint_id": ingest_endpoint_id,
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
        resource_arn: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        tags: Optional[
            "capo_mediapackage.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> None:
        def _handler(
            req: "OperationRequest[capo_mediapackage.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mediapackage._operations.media_package.tag_resource

            output, http_response = (
                capo_mediapackage._operations.media_package.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
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

    def untag_resource(
        self,
        resource_arn: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        tag_keys: Optional[
            "capo_mediapackage.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> None:
        """untag_resource

        Args:
            tag_keys: The key(s) of tag to be deleted

        Raises:
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mediapackage._operations.media_package.untag_resource

            output, http_response = (
                capo_mediapackage._operations.media_package.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel(
        self,
        id: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        description: Optional["capo_mediapackage.types.__string.__string"] = None,
    ) -> "capo_mediapackage.types.update_channel_response.UpdateChannelResponse":
        """Updates an existing Channel.

        Args:
            description: A short text description of the Channel.
            id: The ID of the Channel to update.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.update_channel_response.UpdateChannelResponse"
        ]:
            import capo_mediapackage._operations.media_package.update_channel

            output, http_response = (
                capo_mediapackage._operations.media_package.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.update_channel_request.UpdateChannelRequest = {
            "id": id
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_origin_endpoint(
        self,
        id: "capo_mediapackage.types.__string.__string",
        *,
        config_overrides: Optional[MediaPackageClientConfig] = None,
        authorization: Optional[
            "capo_mediapackage.types.authorization.Authorization"
        ] = None,
        cmaf_package: Optional[
            "capo_mediapackage.types.cmaf_package_create_or_update_parameters.CmafPackageCreateOrUpdateParameters"
        ] = None,
        dash_package: Optional[
            "capo_mediapackage.types.dash_package.DashPackage"
        ] = None,
        description: Optional["capo_mediapackage.types.__string.__string"] = None,
        hls_package: Optional["capo_mediapackage.types.hls_package.HlsPackage"] = None,
        manifest_name: Optional["capo_mediapackage.types.__string.__string"] = None,
        mss_package: Optional["capo_mediapackage.types.mss_package.MssPackage"] = None,
        origination: Optional["capo_mediapackage.types.origination.Origination"] = None,
        startover_window_seconds: Optional[
            "capo_mediapackage.types.__integer.__integer"
        ] = None,
        time_delay_seconds: Optional[
            "capo_mediapackage.types.__integer.__integer"
        ] = None,
        whitelist: Optional[
            "capo_mediapackage.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_mediapackage.types.update_origin_endpoint_response.UpdateOriginEndpointResponse":
        """Updates an existing OriginEndpoint.

        Args:
            description: A short text description of the OriginEndpoint.
            id: The ID of the OriginEndpoint to update.
            manifest_name: A short string that will be appended to the end of the Endpoint URL.
            origination: Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
            startover_window_seconds: Maximum duration (in seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
            time_delay_seconds: Amount of delay (in seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
            whitelist: A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.

        Raises:
            capo_mediapackage.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediapackage.types.update_origin_endpoint_request.UpdateOriginEndpointRequest]",
        ) -> OperationResponse[
            "capo_mediapackage.types.update_origin_endpoint_response.UpdateOriginEndpointResponse"
        ]:
            import capo_mediapackage._operations.media_package.update_origin_endpoint

            output, http_response = (
                capo_mediapackage._operations.media_package.update_origin_endpoint.update_origin_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage.types.update_origin_endpoint_request.UpdateOriginEndpointRequest = {
            "id": id
        }
        if authorization is not None:
            input_["authorization"] = authorization
        if cmaf_package is not None:
            input_["cmaf_package"] = cmaf_package
        if dash_package is not None:
            input_["dash_package"] = dash_package
        if description is not None:
            input_["description"] = description
        if hls_package is not None:
            input_["hls_package"] = hls_package
        if manifest_name is not None:
            input_["manifest_name"] = manifest_name
        if mss_package is not None:
            input_["mss_package"] = mss_package
        if origination is not None:
            input_["origination"] = origination
        if startover_window_seconds is not None:
            input_["startover_window_seconds"] = startover_window_seconds
        if time_delay_seconds is not None:
            input_["time_delay_seconds"] = time_delay_seconds
        if whitelist is not None:
            input_["whitelist"] = whitelist

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
