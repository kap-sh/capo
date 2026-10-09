"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#AWSMPDeploymentParametersService``."""

import datetime
import uuid
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_marketplace_deployment._auth._signers
import capo_marketplace_deployment._auth._sigv4
from capo_marketplace_deployment._auth._identity import Credentials
from capo_marketplace_deployment._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_marketplace_deployment._auth._zapros_handler import AuthMiddleware
from capo_marketplace_deployment._resources.awsmp_deployment_parameters_service.deployment_parameter import (
    AsyncDeploymentParameter,
)
from capo_marketplace_deployment._services._aws_config import aaws_config
from capo_marketplace_deployment._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_marketplace_deployment.types.catalog
    import capo_marketplace_deployment.types.client_token
    import capo_marketplace_deployment.types.deployment_parameter_input
    import capo_marketplace_deployment.types.list_tags_for_resource_request
    import capo_marketplace_deployment.types.list_tags_for_resource_response
    import capo_marketplace_deployment.types.put_deployment_parameter_request
    import capo_marketplace_deployment.types.put_deployment_parameter_response
    import capo_marketplace_deployment.types.resource_id
    import capo_marketplace_deployment.types.string_list
    import capo_marketplace_deployment.types.tag_resource_request
    import capo_marketplace_deployment.types.tag_resource_response
    import capo_marketplace_deployment.types.tags
    import capo_marketplace_deployment.types.tags_map
    import capo_marketplace_deployment.types.untag_resource_request
    import capo_marketplace_deployment.types.untag_resource_response


class AsyncMarketplaceDeploymentClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMarketplaceDeploymentClient:
    """A client for the ``MarketplaceDeployment`` service.

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
        self._config = AsyncMarketplaceDeploymentClientConfig(
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
        self.deployment_parameter = AsyncDeploymentParameter(self)

    def operation_options(
        self, config_overrides: Optional[AsyncMarketplaceDeploymentClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMarketplaceDeploymentClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncMarketplaceDeploymentClientConfig] = None,
    ) -> "capo_marketplace_deployment.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags that have been added to a deployment parameter resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the deployment parameter resource you want to list tags on.</p>

        Raises:
            capo_marketplace_deployment.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_marketplace_deployment.errors.internal_server_exception.InternalServerException: <p>There was an internal service exception.</p>
            capo_marketplace_deployment.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_marketplace_deployment.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p>
            capo_marketplace_deployment.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p>
            capo_marketplace_deployment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Listing tags for a deployment parameter
            The following example demonstrates listing the tags for a deployment parameter. If no tags are present, the API will return an empty map.

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:aws-marketplace:us-east-1:123456789012:DeploymentParameter:catalogs/AWSMarketplace/products/product-1234/dp-uniqueidentifier')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_deployment.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_deployment.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_marketplace_deployment._operations.awsmp_deployment_parameters_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_marketplace_deployment._operations.awsmp_deployment_parameters_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_deployment.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncMarketplaceDeploymentClientConfig] = None,
        tags: Optional["capo_marketplace_deployment.types.tags.Tags"] = None,
    ) -> "capo_marketplace_deployment.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource you want to tag.</p>
            tags: <p>A map of key-value pairs, where each pair represents a tag present on the resource.</p>

        Raises:
            capo_marketplace_deployment.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_marketplace_deployment.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_marketplace_deployment.errors.internal_server_exception.InternalServerException: <p>There was an internal service exception.</p>
            capo_marketplace_deployment.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_marketplace_deployment.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p>
            capo_marketplace_deployment.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p>
            capo_marketplace_deployment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Adding tags to a deployment parameter
            The following example demonstrates adding two tags to a deployment parameter. There is no output from this API.

            >>> await client.tag_resource(resource_arn='arn:aws:aws-marketplace:us-east-1:123456789012:DeploymentParameter:catalogs/AWSMarketplace/products/product-1234/dp-uniqueidentifier', tags={'FooKey': 'BarValue', 'HelloKey': 'WorldValue'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_deployment.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_deployment.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_marketplace_deployment._operations.awsmp_deployment_parameters_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_marketplace_deployment._operations.awsmp_deployment_parameters_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_deployment.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: str,
        tag_keys: "capo_marketplace_deployment.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncMarketplaceDeploymentClientConfig] = None,
    ) -> "capo_marketplace_deployment.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or list of tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from.</p>
            tag_keys: <p>A list of key names of tags to be removed.</p>

        Raises:
            capo_marketplace_deployment.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_marketplace_deployment.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_marketplace_deployment.errors.internal_server_exception.InternalServerException: <p>There was an internal service exception.</p>
            capo_marketplace_deployment.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_marketplace_deployment.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p>
            capo_marketplace_deployment.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p>
            capo_marketplace_deployment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Removing tags from a deployment parameter
            The following example demonstrates removing two tags from a deployment parameter. For each, both the tag and the associated value are removed. There is no output from this API.

            >>> await client.untag_resource(resource_arn='arn:aws:aws-marketplace:us-east-1:123456789012:DeploymentParameter:catalogs/AWSMarketplace/products/product-1234/dp-uniqueidentifier', tag_keys=['FooKey', 'HelloKey'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_deployment.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_deployment.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_marketplace_deployment._operations.awsmp_deployment_parameters_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_marketplace_deployment._operations.awsmp_deployment_parameters_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_deployment.types.untag_resource_request.UntagResourceRequest = {
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

    async def put_deployment_parameter(
        self,
        catalog: "capo_marketplace_deployment.types.catalog.Catalog",
        product_id: "capo_marketplace_deployment.types.resource_id.ResourceId",
        agreement_id: "capo_marketplace_deployment.types.resource_id.ResourceId",
        deployment_parameter: "capo_marketplace_deployment.types.deployment_parameter_input.DeploymentParameterInput",
        *,
        config_overrides: Optional[AsyncMarketplaceDeploymentClientConfig] = None,
        tags: Optional["capo_marketplace_deployment.types.tags_map.TagsMap"] = None,
        expiration_date: Optional[datetime.datetime] = None,
        client_token: Optional[
            "capo_marketplace_deployment.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_marketplace_deployment.types.put_deployment_parameter_response.PutDeploymentParameterResponse":
        """<p>Creates or updates a deployment parameter and is targeted by <code>catalog</code> and <code>agreementId</code>.</p>

        Args:
            catalog: <p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            product_id: <p>The product for which AWS Marketplace will save secrets for the buyer’s account.</p>
            agreement_id: <p>The unique identifier of the agreement.</p>
            deployment_parameter: <p>The deployment parameter targeted to the acceptor of an agreement for which to create the AWS Secret Manager resource.</p>
            tags: <p>A map of key-value pairs, where each pair represents a tag saved to the resource. Tags will only be applied for create operations, and they'll be ignored if the resource already exists.</p>
            expiration_date: <p>The date when deployment parameters expire and are scheduled for deletion.</p>
            client_token: <p>The idempotency token for deployment parameters. A unique identifier for the new version.</p> <note> <p>This field is not required if you're calling using an AWS SDK. Otherwise, a <code>clientToken</code> must be provided with the request.</p> </note>

        Raises:
            capo_marketplace_deployment.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_marketplace_deployment.errors.conflict_exception.ConflictException: <p>The request configuration has conflicts. For details, see the accompanying error message.</p>
            capo_marketplace_deployment.errors.internal_server_exception.InternalServerException: <p>There was an internal service exception.</p>
            capo_marketplace_deployment.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p>
            capo_marketplace_deployment.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The maximum number of requests per account has been exceeded.</p>
            capo_marketplace_deployment.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p>
            capo_marketplace_deployment.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p>
            capo_marketplace_deployment.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Creating or updating a deployment parameter
            The following example demonstrates creating or updating a deployment parameter named "ExampleDeploymentParameterName". The secret will be saved in the Buyer account associated with the passed `agreementId`, with the value set to the provided `secretString`. Note that the deployment parameter `secretString` can be passed in JSON string format, allowing [json-key specific CloudFormation dynamic references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) from a single deployment parameter.

            >>> await client.put_deployment_parameter(agreement_id='agmt-1234', catalog='AWSMarketplace', product_id='product-1234', deployment_parameter={'name': 'ExampleDeploymentParameterName', 'secretString': '{"apiKey": "helloWorldApiKey", "entityId": "fooBarEntityId"}'}, client_token='some-unique-uuid-between-32-and-64-characters')
            Creating a simple deployment parameter, with tags and expiration.
            The following example demonstrates creating a simple deployment parameter named "ExampleSimpleDeploymentParameterName". If multiple secrets are not required, the `secretString` may be provided in String format. The provided tags are only applied on resource creation and will be ignored if the operation results in an update. The API response includes the tags present on the resource after completion of the operation.

            >>> await client.put_deployment_parameter(agreement_id='agmt-1234', catalog='AWSMarketplace', product_id='product-1234', deployment_parameter={'name': 'ExampleSimpleDeploymentParameterName', 'secretString': 'MySimpleValue'}, client_token='some-unique-uuid-between-32-and-64-characters', expiration_date='2099-11-18T08:52:46.397Z', tags={'FooKey': 'BarValue', 'HelloKey': 'WorldValue'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_deployment.types.put_deployment_parameter_request.PutDeploymentParameterRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_deployment.types.put_deployment_parameter_response.PutDeploymentParameterResponse"
        ]:
            import capo_marketplace_deployment._operations.awsmp_deployment_parameters_service.put_deployment_parameter

            (
                output,
                http_response,
            ) = await capo_marketplace_deployment._operations.awsmp_deployment_parameters_service.put_deployment_parameter.async_put_deployment_parameter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_deployment.types.put_deployment_parameter_request.PutDeploymentParameterRequest = {
            "catalog": catalog,
            "product_id": product_id,
            "agreement_id": agreement_id,
            "deployment_parameter": deployment_parameter,
        }
        if tags is not None:
            input_["tags"] = tags
        if expiration_date is not None:
            input_["expiration_date"] = expiration_date
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
