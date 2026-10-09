"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#MediaPackageVod``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_mediapackage_vod._auth._signers
import capo_mediapackage_vod._auth._sigv4
from capo_mediapackage_vod._auth._identity import Credentials
from capo_mediapackage_vod._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mediapackage_vod._auth._zapros_handler import AuthMiddleware
from capo_mediapackage_vod._pagination import resolve_path as _resolve_path
from capo_mediapackage_vod._services._aws_config import aaws_config
from capo_mediapackage_vod._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__list_of__string
    import capo_mediapackage_vod.types.__map_of__string
    import capo_mediapackage_vod.types.__string
    import capo_mediapackage_vod.types.asset_shallow
    import capo_mediapackage_vod.types.authorization
    import capo_mediapackage_vod.types.cmaf_package
    import capo_mediapackage_vod.types.configure_logs_request
    import capo_mediapackage_vod.types.configure_logs_response
    import capo_mediapackage_vod.types.create_asset_request
    import capo_mediapackage_vod.types.create_asset_response
    import capo_mediapackage_vod.types.create_packaging_configuration_request
    import capo_mediapackage_vod.types.create_packaging_configuration_response
    import capo_mediapackage_vod.types.create_packaging_group_request
    import capo_mediapackage_vod.types.create_packaging_group_response
    import capo_mediapackage_vod.types.dash_package
    import capo_mediapackage_vod.types.delete_asset_request
    import capo_mediapackage_vod.types.delete_asset_response
    import capo_mediapackage_vod.types.delete_packaging_configuration_request
    import capo_mediapackage_vod.types.delete_packaging_configuration_response
    import capo_mediapackage_vod.types.delete_packaging_group_request
    import capo_mediapackage_vod.types.delete_packaging_group_response
    import capo_mediapackage_vod.types.describe_asset_request
    import capo_mediapackage_vod.types.describe_asset_response
    import capo_mediapackage_vod.types.describe_packaging_configuration_request
    import capo_mediapackage_vod.types.describe_packaging_configuration_response
    import capo_mediapackage_vod.types.describe_packaging_group_request
    import capo_mediapackage_vod.types.describe_packaging_group_response
    import capo_mediapackage_vod.types.egress_access_logs
    import capo_mediapackage_vod.types.hls_package
    import capo_mediapackage_vod.types.list_assets_request
    import capo_mediapackage_vod.types.list_assets_response
    import capo_mediapackage_vod.types.list_packaging_configurations_request
    import capo_mediapackage_vod.types.list_packaging_configurations_response
    import capo_mediapackage_vod.types.list_packaging_groups_request
    import capo_mediapackage_vod.types.list_packaging_groups_response
    import capo_mediapackage_vod.types.list_tags_for_resource_request
    import capo_mediapackage_vod.types.list_tags_for_resource_response
    import capo_mediapackage_vod.types.max_results
    import capo_mediapackage_vod.types.mss_package
    import capo_mediapackage_vod.types.packaging_configuration
    import capo_mediapackage_vod.types.packaging_group
    import capo_mediapackage_vod.types.tag_resource_request
    import capo_mediapackage_vod.types.tags
    import capo_mediapackage_vod.types.untag_resource_request
    import capo_mediapackage_vod.types.update_packaging_group_request
    import capo_mediapackage_vod.types.update_packaging_group_response


class AsyncMediaPackageVodClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMediaPackageVodClient:
    """A client for the ``MediaPackageVod`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncMediaPackageVodClientConfig(
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
        self, config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMediaPackageVodClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def configure_logs(
        self,
        id: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        egress_access_logs: Optional[
            "capo_mediapackage_vod.types.egress_access_logs.EgressAccessLogs"
        ] = None,
    ) -> "capo_mediapackage_vod.types.configure_logs_response.ConfigureLogsResponse":
        """Changes the packaging group's properities to configure log subscription

        Args:
            id: The ID of a MediaPackage VOD PackagingGroup resource.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.configure_logs_request.ConfigureLogsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.configure_logs_response.ConfigureLogsResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.configure_logs

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.configure_logs.async_configure_logs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.configure_logs_request.ConfigureLogsRequest = {
            "id": id
        }
        if egress_access_logs is not None:
            input_["egress_access_logs"] = egress_access_logs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_asset(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        id: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
        packaging_group_id: Optional[
            "capo_mediapackage_vod.types.__string.__string"
        ] = None,
        resource_id: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
        source_arn: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
        source_role_arn: Optional[
            "capo_mediapackage_vod.types.__string.__string"
        ] = None,
        tags: Optional["capo_mediapackage_vod.types.tags.Tags"] = None,
    ) -> "capo_mediapackage_vod.types.create_asset_response.CreateAssetResponse":
        """Creates a new MediaPackage VOD Asset resource.

        Args:
            id: The unique identifier for the Asset.
            packaging_group_id: The ID of the PackagingGroup for the Asset.
            resource_id: The resource ID to include in SPEKE key requests.
            source_arn: ARN of the source object in S3.
            source_role_arn: The IAM role ARN used to access the source S3 bucket.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.create_asset_request.CreateAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.create_asset_response.CreateAssetResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.create_asset

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.create_asset.async_create_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.create_asset_request.CreateAssetRequest = {}
        if id is not None:
            input_["id"] = id
        if packaging_group_id is not None:
            input_["packaging_group_id"] = packaging_group_id
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if source_arn is not None:
            input_["source_arn"] = source_arn
        if source_role_arn is not None:
            input_["source_role_arn"] = source_role_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_packaging_configuration(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        cmaf_package: Optional[
            "capo_mediapackage_vod.types.cmaf_package.CmafPackage"
        ] = None,
        dash_package: Optional[
            "capo_mediapackage_vod.types.dash_package.DashPackage"
        ] = None,
        hls_package: Optional[
            "capo_mediapackage_vod.types.hls_package.HlsPackage"
        ] = None,
        id: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
        mss_package: Optional[
            "capo_mediapackage_vod.types.mss_package.MssPackage"
        ] = None,
        packaging_group_id: Optional[
            "capo_mediapackage_vod.types.__string.__string"
        ] = None,
        tags: Optional["capo_mediapackage_vod.types.tags.Tags"] = None,
    ) -> "capo_mediapackage_vod.types.create_packaging_configuration_response.CreatePackagingConfigurationResponse":
        """Creates a new MediaPackage VOD PackagingConfiguration resource.

        Args:
            id: The ID of the PackagingConfiguration.
            packaging_group_id: The ID of a PackagingGroup.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.create_packaging_configuration_request.CreatePackagingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.create_packaging_configuration_response.CreatePackagingConfigurationResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.create_packaging_configuration

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.create_packaging_configuration.async_create_packaging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.create_packaging_configuration_request.CreatePackagingConfigurationRequest = {}
        if cmaf_package is not None:
            input_["cmaf_package"] = cmaf_package
        if dash_package is not None:
            input_["dash_package"] = dash_package
        if hls_package is not None:
            input_["hls_package"] = hls_package
        if id is not None:
            input_["id"] = id
        if mss_package is not None:
            input_["mss_package"] = mss_package
        if packaging_group_id is not None:
            input_["packaging_group_id"] = packaging_group_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_packaging_group(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        authorization: Optional[
            "capo_mediapackage_vod.types.authorization.Authorization"
        ] = None,
        egress_access_logs: Optional[
            "capo_mediapackage_vod.types.egress_access_logs.EgressAccessLogs"
        ] = None,
        id: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
        tags: Optional["capo_mediapackage_vod.types.tags.Tags"] = None,
    ) -> "capo_mediapackage_vod.types.create_packaging_group_response.CreatePackagingGroupResponse":
        """Creates a new MediaPackage VOD PackagingGroup resource.

        Args:
            id: The ID of the PackagingGroup.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.create_packaging_group_request.CreatePackagingGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.create_packaging_group_response.CreatePackagingGroupResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.create_packaging_group

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.create_packaging_group.async_create_packaging_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.create_packaging_group_request.CreatePackagingGroupRequest = {}
        if authorization is not None:
            input_["authorization"] = authorization
        if egress_access_logs is not None:
            input_["egress_access_logs"] = egress_access_logs
        if id is not None:
            input_["id"] = id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset(
        self,
        id: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
    ) -> "capo_mediapackage_vod.types.delete_asset_response.DeleteAssetResponse":
        """Deletes an existing MediaPackage VOD Asset resource.

        Args:
            id: The ID of the MediaPackage VOD Asset resource to delete.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.delete_asset_request.DeleteAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.delete_asset_response.DeleteAssetResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.delete_asset

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.delete_asset.async_delete_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.delete_asset_request.DeleteAssetRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_packaging_configuration(
        self,
        id: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
    ) -> "capo_mediapackage_vod.types.delete_packaging_configuration_response.DeletePackagingConfigurationResponse":
        """Deletes a MediaPackage VOD PackagingConfiguration resource.

        Args:
            id: The ID of the MediaPackage VOD PackagingConfiguration resource to delete.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.delete_packaging_configuration_request.DeletePackagingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.delete_packaging_configuration_response.DeletePackagingConfigurationResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.delete_packaging_configuration

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.delete_packaging_configuration.async_delete_packaging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.delete_packaging_configuration_request.DeletePackagingConfigurationRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_packaging_group(
        self,
        id: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
    ) -> "capo_mediapackage_vod.types.delete_packaging_group_response.DeletePackagingGroupResponse":
        """Deletes a MediaPackage VOD PackagingGroup resource.

        Args:
            id: The ID of the MediaPackage VOD PackagingGroup resource to delete.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.delete_packaging_group_request.DeletePackagingGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.delete_packaging_group_response.DeletePackagingGroupResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.delete_packaging_group

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.delete_packaging_group.async_delete_packaging_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.delete_packaging_group_request.DeletePackagingGroupRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_asset(
        self,
        id: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
    ) -> "capo_mediapackage_vod.types.describe_asset_response.DescribeAssetResponse":
        """Returns a description of a MediaPackage VOD Asset resource.

        Args:
            id: The ID of an MediaPackage VOD Asset resource.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.describe_asset_request.DescribeAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.describe_asset_response.DescribeAssetResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.describe_asset

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.describe_asset.async_describe_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.describe_asset_request.DescribeAssetRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_packaging_configuration(
        self,
        id: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
    ) -> "capo_mediapackage_vod.types.describe_packaging_configuration_response.DescribePackagingConfigurationResponse":
        """Returns a description of a MediaPackage VOD PackagingConfiguration resource.

        Args:
            id: The ID of a MediaPackage VOD PackagingConfiguration resource.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.describe_packaging_configuration_request.DescribePackagingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.describe_packaging_configuration_response.DescribePackagingConfigurationResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.describe_packaging_configuration

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.describe_packaging_configuration.async_describe_packaging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.describe_packaging_configuration_request.DescribePackagingConfigurationRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_packaging_group(
        self,
        id: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
    ) -> "capo_mediapackage_vod.types.describe_packaging_group_response.DescribePackagingGroupResponse":
        """Returns a description of a MediaPackage VOD PackagingGroup resource.

        Args:
            id: The ID of a MediaPackage VOD PackagingGroup resource.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.describe_packaging_group_request.DescribePackagingGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.describe_packaging_group_response.DescribePackagingGroupResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.describe_packaging_group

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.describe_packaging_group.async_describe_packaging_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.describe_packaging_group_request.DescribePackagingGroupRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_assets(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        max_results: Optional[
            "capo_mediapackage_vod.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
        packaging_group_id: Optional[
            "capo_mediapackage_vod.types.__string.__string"
        ] = None,
    ) -> "capo_mediapackage_vod.types.list_assets_response.ListAssetsResponse":
        """Returns a collection of MediaPackage VOD Asset resources.

        Args:
            max_results: Upper bound on number of records to return.
            next_token: A token used to resume pagination from the end of a previous request.
            packaging_group_id: Returns Assets associated with the specified PackagingGroup.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.list_assets_request.ListAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.list_assets_response.ListAssetsResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.list_assets

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.list_assets.async_list_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.list_assets_request.ListAssetsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if packaging_group_id is not None:
            input_["packaging_group_id"] = packaging_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_assets(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        max_results: Optional[
            "capo_mediapackage_vod.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
        packaging_group_id: Optional[
            "capo_mediapackage_vod.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[capo_mediapackage_vod.types.asset_shallow.AssetShallow]":
        _token = next_token
        while True:
            _response = await self.list_assets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                packaging_group_id=packaging_group_id,
            )
            _page = _resolve_path(_response, ("assets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_packaging_configurations(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        max_results: Optional[
            "capo_mediapackage_vod.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
        packaging_group_id: Optional[
            "capo_mediapackage_vod.types.__string.__string"
        ] = None,
    ) -> "capo_mediapackage_vod.types.list_packaging_configurations_response.ListPackagingConfigurationsResponse":
        """Returns a collection of MediaPackage VOD PackagingConfiguration resources.

        Args:
            max_results: Upper bound on number of records to return.
            next_token: A token used to resume pagination from the end of a previous request.
            packaging_group_id: Returns MediaPackage VOD PackagingConfigurations associated with the specified PackagingGroup.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.list_packaging_configurations_request.ListPackagingConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.list_packaging_configurations_response.ListPackagingConfigurationsResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.list_packaging_configurations

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.list_packaging_configurations.async_list_packaging_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.list_packaging_configurations_request.ListPackagingConfigurationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if packaging_group_id is not None:
            input_["packaging_group_id"] = packaging_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_packaging_configurations(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        max_results: Optional[
            "capo_mediapackage_vod.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
        packaging_group_id: Optional[
            "capo_mediapackage_vod.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[capo_mediapackage_vod.types.packaging_configuration.PackagingConfiguration]":
        _token = next_token
        while True:
            _response = await self.list_packaging_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                packaging_group_id=packaging_group_id,
            )
            _page = _resolve_path(_response, ("packaging_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_packaging_groups(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        max_results: Optional[
            "capo_mediapackage_vod.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
    ) -> "capo_mediapackage_vod.types.list_packaging_groups_response.ListPackagingGroupsResponse":
        """Returns a collection of MediaPackage VOD PackagingGroup resources.

        Args:
            max_results: Upper bound on number of records to return.
            next_token: A token used to resume pagination from the end of a previous request.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.list_packaging_groups_request.ListPackagingGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.list_packaging_groups_response.ListPackagingGroupsResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.list_packaging_groups

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.list_packaging_groups.async_list_packaging_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.list_packaging_groups_request.ListPackagingGroupsRequest = {}
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

    async def iter_list_packaging_groups(
        self,
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        max_results: Optional[
            "capo_mediapackage_vod.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_mediapackage_vod.types.__string.__string"] = None,
    ) -> "AsyncIterator[capo_mediapackage_vod.types.packaging_group.PackagingGroup]":
        _token = next_token
        while True:
            _response = await self.list_packaging_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("packaging_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
    ) -> "capo_mediapackage_vod.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """Returns a list of the tags assigned to the specified resource.

        Args:
            resource_arn: The Amazon Resource Name (ARN) for the resource. You can get this from the response to any request to the resource.

        Raises:
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        tags: Optional[
            "capo_mediapackage_vod.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> None:
        """Adds tags to the specified resource. You can specify one or more tags to add.

        Args:
            resource_arn: The Amazon Resource Name (ARN) for the resource. You can get this from the response to any request to the resource.
            tags: A collection of tags associated with a resource

        Raises:
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_mediapackage_vod._operations.media_package_vod.tag_resource

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        tag_keys: Optional[
            "capo_mediapackage_vod.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> None:
        """Removes tags from the specified resource. You can specify one or more tags to remove.

        Args:
            resource_arn: The Amazon Resource Name (ARN) for the resource. You can get this from the response to any request to the resource.
            tag_keys: A comma-separated list of the tag keys to remove from the resource.

        Raises:
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_mediapackage_vod._operations.media_package_vod.untag_resource

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_packaging_group(
        self,
        id: "capo_mediapackage_vod.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaPackageVodClientConfig] = None,
        authorization: Optional[
            "capo_mediapackage_vod.types.authorization.Authorization"
        ] = None,
    ) -> "capo_mediapackage_vod.types.update_packaging_group_response.UpdatePackagingGroupResponse":
        """Updates a specific packaging group. You can't change the id attribute or any other system-generated attributes.

        Args:
            id: The ID of a MediaPackage VOD PackagingGroup resource.

        Raises:
            capo_mediapackage_vod.errors.forbidden_exception.ForbiddenException: The client is not authorized to access the requested resource.
            capo_mediapackage_vod.errors.internal_server_error_exception.InternalServerErrorException: An unexpected error occurred.
            capo_mediapackage_vod.errors.not_found_exception.NotFoundException: The requested resource does not exist.
            capo_mediapackage_vod.errors.service_unavailable_exception.ServiceUnavailableException: An unexpected error occurred.
            capo_mediapackage_vod.errors.too_many_requests_exception.TooManyRequestsException: The client has exceeded their resource or throttling limits.
            capo_mediapackage_vod.errors.unprocessable_entity_exception.UnprocessableEntityException: The parameters sent in the request are not valid.
            capo_mediapackage_vod.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediapackage_vod.types.update_packaging_group_request.UpdatePackagingGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediapackage_vod.types.update_packaging_group_response.UpdatePackagingGroupResponse"
        ]:
            import capo_mediapackage_vod._operations.media_package_vod.update_packaging_group

            (
                output,
                http_response,
            ) = await capo_mediapackage_vod._operations.media_package_vod.update_packaging_group.async_update_packaging_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediapackage_vod.types.update_packaging_group_request.UpdatePackagingGroupRequest = {
            "id": id
        }
        if authorization is not None:
            input_["authorization"] = authorization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
