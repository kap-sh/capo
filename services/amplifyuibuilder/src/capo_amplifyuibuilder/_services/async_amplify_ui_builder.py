"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#AmplifyUIBuilder``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_amplifyuibuilder._auth._signers
import capo_amplifyuibuilder._auth._sigv4
from capo_amplifyuibuilder._auth._identity import Credentials
from capo_amplifyuibuilder._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_amplifyuibuilder._auth._zapros_handler import AuthMiddleware
from capo_amplifyuibuilder._pagination import resolve_path as _resolve_path
from capo_amplifyuibuilder._resources.amplify_ui_builder.codegen_job_resource import (
    AsyncCodegenJobResource,
)
from capo_amplifyuibuilder._resources.amplify_ui_builder.component_resource import (
    AsyncComponentResource,
)
from capo_amplifyuibuilder._resources.amplify_ui_builder.form_resource import (
    AsyncFormResource,
)
from capo_amplifyuibuilder._resources.amplify_ui_builder.theme_resource import (
    AsyncThemeResource,
)
from capo_amplifyuibuilder._services._aws_config import aaws_config
from capo_amplifyuibuilder._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.app_id
    import capo_amplifyuibuilder.types.codegen_job_summary
    import capo_amplifyuibuilder.types.component
    import capo_amplifyuibuilder.types.component_summary
    import capo_amplifyuibuilder.types.create_component_data
    import capo_amplifyuibuilder.types.create_component_request
    import capo_amplifyuibuilder.types.create_component_response
    import capo_amplifyuibuilder.types.create_form_data
    import capo_amplifyuibuilder.types.create_form_request
    import capo_amplifyuibuilder.types.create_form_response
    import capo_amplifyuibuilder.types.create_theme_data
    import capo_amplifyuibuilder.types.create_theme_request
    import capo_amplifyuibuilder.types.create_theme_response
    import capo_amplifyuibuilder.types.delete_component_request
    import capo_amplifyuibuilder.types.delete_form_request
    import capo_amplifyuibuilder.types.delete_theme_request
    import capo_amplifyuibuilder.types.exchange_code_for_token_request
    import capo_amplifyuibuilder.types.exchange_code_for_token_request_body
    import capo_amplifyuibuilder.types.exchange_code_for_token_response
    import capo_amplifyuibuilder.types.export_components_request
    import capo_amplifyuibuilder.types.export_components_response
    import capo_amplifyuibuilder.types.export_forms_request
    import capo_amplifyuibuilder.types.export_forms_response
    import capo_amplifyuibuilder.types.export_themes_request
    import capo_amplifyuibuilder.types.export_themes_response
    import capo_amplifyuibuilder.types.form
    import capo_amplifyuibuilder.types.form_summary
    import capo_amplifyuibuilder.types.get_codegen_job_request
    import capo_amplifyuibuilder.types.get_codegen_job_response
    import capo_amplifyuibuilder.types.get_component_request
    import capo_amplifyuibuilder.types.get_component_response
    import capo_amplifyuibuilder.types.get_form_request
    import capo_amplifyuibuilder.types.get_form_response
    import capo_amplifyuibuilder.types.get_metadata_request
    import capo_amplifyuibuilder.types.get_metadata_response
    import capo_amplifyuibuilder.types.get_theme_request
    import capo_amplifyuibuilder.types.get_theme_response
    import capo_amplifyuibuilder.types.list_codegen_jobs_limit
    import capo_amplifyuibuilder.types.list_codegen_jobs_request
    import capo_amplifyuibuilder.types.list_codegen_jobs_response
    import capo_amplifyuibuilder.types.list_components_request
    import capo_amplifyuibuilder.types.list_components_response
    import capo_amplifyuibuilder.types.list_entity_limit
    import capo_amplifyuibuilder.types.list_forms_request
    import capo_amplifyuibuilder.types.list_forms_response
    import capo_amplifyuibuilder.types.list_tags_for_resource_request
    import capo_amplifyuibuilder.types.list_tags_for_resource_response
    import capo_amplifyuibuilder.types.list_themes_request
    import capo_amplifyuibuilder.types.list_themes_response
    import capo_amplifyuibuilder.types.put_metadata_flag_body
    import capo_amplifyuibuilder.types.put_metadata_flag_request
    import capo_amplifyuibuilder.types.refresh_token_request
    import capo_amplifyuibuilder.types.refresh_token_request_body
    import capo_amplifyuibuilder.types.refresh_token_response
    import capo_amplifyuibuilder.types.start_codegen_job_data
    import capo_amplifyuibuilder.types.start_codegen_job_request
    import capo_amplifyuibuilder.types.start_codegen_job_response
    import capo_amplifyuibuilder.types.tag_key_list
    import capo_amplifyuibuilder.types.tag_resource_request
    import capo_amplifyuibuilder.types.tag_resource_response
    import capo_amplifyuibuilder.types.tags
    import capo_amplifyuibuilder.types.theme
    import capo_amplifyuibuilder.types.theme_summary
    import capo_amplifyuibuilder.types.token_providers
    import capo_amplifyuibuilder.types.untag_resource_request
    import capo_amplifyuibuilder.types.untag_resource_response
    import capo_amplifyuibuilder.types.update_component_data
    import capo_amplifyuibuilder.types.update_component_request
    import capo_amplifyuibuilder.types.update_component_response
    import capo_amplifyuibuilder.types.update_form_data
    import capo_amplifyuibuilder.types.update_form_request
    import capo_amplifyuibuilder.types.update_form_response
    import capo_amplifyuibuilder.types.update_theme_data
    import capo_amplifyuibuilder.types.update_theme_request
    import capo_amplifyuibuilder.types.update_theme_response
    import capo_amplifyuibuilder.types.uuid


class AsyncAmplifyUIBuilderClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncAmplifyUIBuilderClient:
    """A client for the ``AmplifyUIBuilder`` service.

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
        self._config = AsyncAmplifyUIBuilderClientConfig(
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

        # resources
        self.codegen_job_resource = AsyncCodegenJobResource(self)
        self.component_resource = AsyncComponentResource(self)
        self.form_resource = AsyncFormResource(self)
        self.theme_resource = AsyncThemeResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncAmplifyUIBuilderClientConfig = config_overrides or {}
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

    async def exchange_code_for_token(
        self,
        provider: "capo_amplifyuibuilder.types.token_providers.TokenProviders",
        request: "capo_amplifyuibuilder.types.exchange_code_for_token_request_body.ExchangeCodeForTokenRequestBody",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.exchange_code_for_token_response.ExchangeCodeForTokenResponse":
        """<note> <p>This is for internal use.</p> </note> <p>Amplify uses this action to exchange an access code for a token.</p>

        Args:
            provider: <p>The third-party provider for the token. The only valid value is <code>figma</code>.</p>
            request: <p>Describes the configuration of the request.</p>

        Raises:
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.exchange_code_for_token_request.ExchangeCodeForTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.exchange_code_for_token_response.ExchangeCodeForTokenResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.exchange_code_for_token

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.exchange_code_for_token.async_exchange_code_for_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.exchange_code_for_token_request.ExchangeCodeForTokenRequest = {
            "provider": provider,
            "request": request,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_metadata(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.get_metadata_response.GetMetadataResponse":
        """<p>Returns existing metadata for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>

        Raises:
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.unauthorized_exception.UnauthorizedException: <p>You don't have permission to perform this operation.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.get_metadata_request.GetMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.get_metadata_response.GetMetadataResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_metadata

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.get_metadata.async_get_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.get_metadata_request.GetMetadataRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags for a specified Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) to use to list tags.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.unauthorized_exception.UnauthorizedException: <p>You don't have permission to perform this operation.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_metadata_flag(
        self,
        app_id: str,
        environment_name: str,
        feature_name: str,
        body: "capo_amplifyuibuilder.types.put_metadata_flag_body.PutMetadataFlagBody",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> None:
        """<p>Stores the metadata information about a feature on a form.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            feature_name: <p>The name of the feature associated with the metadata.</p>
            body: <p>The metadata information to store.</p>

        Raises:
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.unauthorized_exception.UnauthorizedException: <p>You don't have permission to perform this operation.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.put_metadata_flag_request.PutMetadataFlagRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.put_metadata_flag

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.put_metadata_flag.async_put_metadata_flag(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.put_metadata_flag_request.PutMetadataFlagRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "feature_name": feature_name,
            "body": body,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def refresh_token(
        self,
        provider: "capo_amplifyuibuilder.types.token_providers.TokenProviders",
        refresh_token_body: "capo_amplifyuibuilder.types.refresh_token_request_body.RefreshTokenRequestBody",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.refresh_token_response.RefreshTokenResponse":
        """<note> <p>This is for internal use.</p> </note> <p>Amplify uses this action to refresh a previously issued access token that might have expired.</p>

        Args:
            provider: <p>The third-party provider for the token. The only valid value is <code>figma</code>.</p>
            refresh_token_body: <p>Information about the refresh token request.</p>

        Raises:
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.refresh_token_request.RefreshTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.refresh_token_response.RefreshTokenResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.refresh_token

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.refresh_token.async_refresh_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.refresh_token_request.RefreshTokenRequest = {
            "provider": provider,
            "refresh_token_body": refresh_token_body,
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
        resource_arn: str,
        tags: "capo_amplifyuibuilder.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.tag_resource_response.TagResourceResponse":
        """<p>Tags the resource with a tag key and value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) to use to tag a resource.</p>
            tags: <p>A list of tag key value pairs for a specified Amazon Resource Name (ARN).</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.unauthorized_exception.UnauthorizedException: <p>You don't have permission to perform this operation.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.tag_resource

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: str,
        tag_keys: "capo_amplifyuibuilder.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.untag_resource_response.UntagResourceResponse":
        """<p>Untags a resource with a specified Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) to use to untag a resource.</p>
            tag_keys: <p>The tag keys to use to untag a resource.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.unauthorized_exception.UnauthorizedException: <p>You don't have permission to perform this operation.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.untag_resource

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_codegen_job(
        self,
        app_id: "capo_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        codegen_job_to_create: "capo_amplifyuibuilder.types.start_codegen_job_data.StartCodegenJobData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse"
    ):
        """<p>Starts a code generation job for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The idempotency token used to ensure that the code generation job request completes only once.</p>
            codegen_job_to_create: <p>The code generation job resource configuration.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.start_codegen_job_response.StartCodegenJobResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.start_codegen_job.async_start_codegen_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.start_codegen_job_request.StartCodegenJobRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "codegen_job_to_create": codegen_job_to_create,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_codegen_job(
        self,
        app_id: "capo_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse":
        """<p>Returns an existing code generation job.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the code generation job.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app associated with the code generation job.</p>
            id: <p>The unique ID of the code generation job.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.get_codegen_job_response.GetCodegenJobResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.get_codegen_job.async_get_codegen_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.get_codegen_job_request.GetCodegenJobRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_codegen_jobs(
        self,
        app_id: "capo_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_codegen_jobs_limit.ListCodegenJobsLimit"
        ] = None,
    ) -> (
        "capo_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse"
    ):
        """<p>Retrieves a list of code generation jobs for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of jobs to retrieve.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.list_codegen_jobs_response.ListCodegenJobsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.list_codegen_jobs.async_list_codegen_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.list_codegen_jobs_request.ListCodegenJobsRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_codegen_jobs(
        self,
        app_id: "capo_amplifyuibuilder.types.app_id.AppId",
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_codegen_jobs_limit.ListCodegenJobsLimit"
        ] = None,
    ) -> "AsyncIterator[capo_amplifyuibuilder.types.codegen_job_summary.CodegenJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_codegen_jobs(
                app_id,
                environment_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_component(
        self,
        app_id: str,
        environment_name: str,
        component_to_create: "capo_amplifyuibuilder.types.create_component_data.CreateComponentData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_amplifyuibuilder.types.create_component_response.CreateComponentResponse"
    ):
        """<p>Creates a new component for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to associate with the component.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            component_to_create: <p>Represents the configuration of the component to create.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. </p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.create_component_request.CreateComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.create_component_response.CreateComponentResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.create_component

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.create_component.async_create_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.create_component_request.CreateComponentRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "component_to_create": component_to_create,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_component(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.get_component_response.GetComponentResponse":
        """<p>Returns an existing component for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID of the component.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.get_component_request.GetComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.get_component_response.GetComponentResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_component

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.get_component.async_get_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.get_component_request.GetComponentRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_component(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        updated_component: "capo_amplifyuibuilder.types.update_component_data.UpdateComponentData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_amplifyuibuilder.types.update_component_response.UpdateComponentResponse"
    ):
        """<p>Updates an existing component.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the component.</p>
            client_token: <p>The unique client token.</p>
            updated_component: <p>The configuration of the updated component.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.update_component_request.UpdateComponentRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.update_component_response.UpdateComponentResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.update_component

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.update_component.async_update_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.update_component_request.UpdateComponentRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
            "updated_component": updated_component,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_component(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> None:
        """<p>Deletes a component from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the component to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the component to delete.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.delete_component_request.DeleteComponentRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.delete_component

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.delete_component.async_delete_component(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.delete_component_request.DeleteComponentRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_components(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
        ] = None,
    ) -> "capo_amplifyuibuilder.types.list_components_response.ListComponentsResponse":
        """<p>Retrieves a list of components for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of components to retrieve.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.list_components_request.ListComponentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.list_components_response.ListComponentsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_components

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.list_components.async_list_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.list_components_request.ListComponentsRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_components(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
        ] = None,
    ) -> (
        "AsyncIterator[capo_amplifyuibuilder.types.component_summary.ComponentSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_components(
                app_id,
                environment_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def export_components(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.export_components_response.ExportComponentsResponse":
        """<p>Exports component configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export components to.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.export_components_request.ExportComponentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.export_components_response.ExportComponentsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.export_components

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.export_components.async_export_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.export_components_request.ExportComponentsRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_export_components(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_amplifyuibuilder.types.component.Component]":
        _token = next_token
        while True:
            _response = await self.export_components(
                app_id,
                environment_name,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_form(
        self,
        app_id: str,
        environment_name: str,
        form_to_create: "capo_amplifyuibuilder.types.create_form_data.CreateFormData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.create_form_response.CreateFormResponse":
        """<p>Creates a new form for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to associate with the form.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            form_to_create: <p>Represents the configuration of the form to create.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. </p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.create_form_request.CreateFormRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.create_form_response.CreateFormResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.create_form

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.create_form.async_create_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.create_form_request.CreateFormRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "form_to_create": form_to_create,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_form(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.get_form_response.GetFormResponse":
        """<p>Returns an existing form for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID of the form.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.get_form_request.GetFormRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.get_form_response.GetFormResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_form

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.get_form.async_get_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.get_form_request.GetFormRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_form(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        updated_form: "capo_amplifyuibuilder.types.update_form_data.UpdateFormData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.update_form_response.UpdateFormResponse":
        """<p>Updates an existing form.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the form.</p>
            client_token: <p>The unique client token.</p>
            updated_form: <p>The request accepts the following data in JSON format.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.update_form_request.UpdateFormRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.update_form_response.UpdateFormResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.update_form

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.update_form.async_update_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.update_form_request.UpdateFormRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
            "updated_form": updated_form,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_form(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> None:
        """<p>Deletes a form from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the form to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the form to delete.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.delete_form_request.DeleteFormRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.delete_form

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.delete_form.async_delete_form(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.delete_form_request.DeleteFormRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_forms(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
        ] = None,
    ) -> "capo_amplifyuibuilder.types.list_forms_response.ListFormsResponse":
        """<p>Retrieves a list of forms for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of forms to retrieve.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.list_forms_request.ListFormsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.list_forms_response.ListFormsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_forms

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.list_forms.async_list_forms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.list_forms_request.ListFormsRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_forms(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
        ] = None,
    ) -> "AsyncIterator[capo_amplifyuibuilder.types.form_summary.FormSummary]":
        _token = next_token
        while True:
            _response = await self.list_forms(
                app_id,
                environment_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def export_forms(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.export_forms_response.ExportFormsResponse":
        """<p>Exports form configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export forms to.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.export_forms_request.ExportFormsRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.export_forms_response.ExportFormsResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.export_forms

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.export_forms.async_export_forms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.export_forms_request.ExportFormsRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_export_forms(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_amplifyuibuilder.types.form.Form]":
        _token = next_token
        while True:
            _response = await self.export_forms(
                app_id,
                environment_name,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_theme(
        self,
        app_id: str,
        environment_name: str,
        theme_to_create: "capo_amplifyuibuilder.types.create_theme_data.CreateThemeData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.create_theme_response.CreateThemeResponse":
        """<p>Creates a theme to apply to the components in an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the theme.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            client_token: <p>The unique client token.</p>
            theme_to_create: <p>Represents the configuration of the theme to create.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account. </p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.create_theme_request.CreateThemeRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.create_theme_response.CreateThemeResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.create_theme

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.create_theme.async_create_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.create_theme_request.CreateThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "theme_to_create": theme_to_create,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_theme(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> "capo_amplifyuibuilder.types.get_theme_response.GetThemeResponse":
        """<p>Returns an existing theme for an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the theme.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.get_theme_request.GetThemeRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.get_theme_response.GetThemeResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.get_theme

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.get_theme.async_get_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.get_theme_request.GetThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_theme(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        updated_theme: "capo_amplifyuibuilder.types.update_theme_data.UpdateThemeData",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.update_theme_response.UpdateThemeResponse":
        """<p>Updates an existing theme.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            id: <p>The unique ID for the theme.</p>
            client_token: <p>The unique client token.</p>
            updated_theme: <p>The configuration of the updated theme.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_conflict_exception.ResourceConflictException: <p>The resource specified in the request conflicts with an existing resource.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.update_theme_request.UpdateThemeRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.update_theme_response.UpdateThemeResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.update_theme

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.update_theme.async_update_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.update_theme_request.UpdateThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
            "updated_theme": updated_theme,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_theme(
        self,
        app_id: str,
        environment_name: str,
        id: "capo_amplifyuibuilder.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
    ) -> None:
        """<p>Deletes a theme from an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app associated with the theme to delete.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            id: <p>The unique ID of the theme to delete.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist, or access was denied.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.delete_theme_request.DeleteThemeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.delete_theme

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.delete_theme.async_delete_theme(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.delete_theme_request.DeleteThemeRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_themes(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
        ] = None,
    ) -> "capo_amplifyuibuilder.types.list_themes_response.ListThemesResponse":
        """<p>Retrieves a list of themes for a specified Amplify app and backend environment.</p>

        Args:
            app_id: <p>The unique ID for the Amplify app.</p>
            environment_name: <p>The name of the backend environment that is a part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>
            max_results: <p>The maximum number of theme results to return in the response.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.list_themes_request.ListThemesRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.list_themes_response.ListThemesResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.list_themes

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.list_themes.async_list_themes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.list_themes_request.ListThemesRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_themes(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
        ] = None,
    ) -> "AsyncIterator[capo_amplifyuibuilder.types.theme_summary.ThemeSummary]":
        _token = next_token
        while True:
            _response = await self.list_themes(
                app_id,
                environment_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def export_themes(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_amplifyuibuilder.types.export_themes_response.ExportThemesResponse":
        """<p>Exports theme configurations to code that is ready to integrate into an Amplify app.</p>

        Args:
            app_id: <p>The unique ID of the Amplify app to export the themes to.</p>
            environment_name: <p>The name of the backend environment that is part of the Amplify app.</p>
            next_token: <p>The token to request the next page of results.</p>

        Raises:
            capo_amplifyuibuilder.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. Please retry your request.</p>
            capo_amplifyuibuilder.errors.invalid_parameter_exception.InvalidParameterException: <p>An invalid or out-of-range value was supplied for the input parameter.</p>
            capo_amplifyuibuilder.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amplifyuibuilder.types.export_themes_request.ExportThemesRequest]",
        ) -> AsyncOperationResponse[
            "capo_amplifyuibuilder.types.export_themes_response.ExportThemesResponse"
        ]:
            import capo_amplifyuibuilder._operations.amplify_ui_builder.export_themes

            (
                output,
                http_response,
            ) = await capo_amplifyuibuilder._operations.amplify_ui_builder.export_themes.async_export_themes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifyuibuilder.types.export_themes_request.ExportThemesRequest = {
            "app_id": app_id,
            "environment_name": environment_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_export_themes(
        self,
        app_id: str,
        environment_name: str,
        *,
        config_overrides: Optional[AsyncAmplifyUIBuilderClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_amplifyuibuilder.types.theme.Theme]":
        _token = next_token
        while True:
            _response = await self.export_themes(
                app_id,
                environment_name,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
