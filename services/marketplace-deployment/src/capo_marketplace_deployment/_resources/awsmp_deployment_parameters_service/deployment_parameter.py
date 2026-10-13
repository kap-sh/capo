from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_marketplace_deployment._auth._signers
import capo_marketplace_deployment._auth._sigv4
from capo_marketplace_deployment._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_marketplace_deployment.types.catalog
    import capo_marketplace_deployment.types.client_token
    import capo_marketplace_deployment.types.deployment_parameter_input
    import capo_marketplace_deployment.types.put_deployment_parameter_request
    import capo_marketplace_deployment.types.put_deployment_parameter_response
    import capo_marketplace_deployment.types.resource_id
    import capo_marketplace_deployment.types.tags_map
    from capo_marketplace_deployment._services.async_marketplace_deployment import (
        AsyncMarketplaceDeploymentClient,
        AsyncMarketplaceDeploymentClientConfig,
    )
    from capo_marketplace_deployment._services.marketplace_deployment import (
        MarketplaceDeploymentClient,
        MarketplaceDeploymentClientConfig,
    )


class DeploymentParameter:
    def __init__(self, service: MarketplaceDeploymentClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_marketplace_deployment.types.catalog.Catalog",
        product_id: "capo_marketplace_deployment.types.resource_id.ResourceId",
        agreement_id: "capo_marketplace_deployment.types.resource_id.ResourceId",
        deployment_parameter: "capo_marketplace_deployment.types.deployment_parameter_input.DeploymentParameterInput",
        *,
        config_overrides: Optional[MarketplaceDeploymentClientConfig] = None,
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

            >>> client.create(agreement_id='agmt-1234', catalog='AWSMarketplace', product_id='product-1234', deployment_parameter={'name': 'ExampleDeploymentParameterName', 'secretString': '{"apiKey": "helloWorldApiKey", "entityId": "fooBarEntityId"}'}, client_token='some-unique-uuid-between-32-and-64-characters')
            Creating a simple deployment parameter, with tags and expiration.
            The following example demonstrates creating a simple deployment parameter named "ExampleSimpleDeploymentParameterName". If multiple secrets are not required, the `secretString` may be provided in String format. The provided tags are only applied on resource creation and will be ignored if the operation results in an update. The API response includes the tags present on the resource after completion of the operation.

            >>> client.create(agreement_id='agmt-1234', catalog='AWSMarketplace', product_id='product-1234', deployment_parameter={'name': 'ExampleSimpleDeploymentParameterName', 'secretString': 'MySimpleValue'}, client_token='some-unique-uuid-between-32-and-64-characters', expiration_date='2099-11-18T08:52:46.397Z', tags={'FooKey': 'BarValue', 'HelloKey': 'WorldValue'})
        """

        def _handler(
            req: "OperationRequest[capo_marketplace_deployment.types.put_deployment_parameter_request.PutDeploymentParameterRequest]",
        ) -> OperationResponse[
            "capo_marketplace_deployment.types.put_deployment_parameter_response.PutDeploymentParameterResponse"
        ]:
            import capo_marketplace_deployment._operations.awsmp_deployment_parameters_service.put_deployment_parameter

            output, http_response = (
                capo_marketplace_deployment._operations.awsmp_deployment_parameters_service.put_deployment_parameter.put_deployment_parameter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_marketplace_deployment.types.put_deployment_parameter_request.PutDeploymentParameterRequest",
        ) -> dict[str, Any]:
            import capo_marketplace_deployment.types.put_deployment_parameter_request

            return capo_marketplace_deployment.types.put_deployment_parameter_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("PutDeploymentParameter", redact_input=_redact_input),
        )
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDeploymentParameter:
    def __init__(self, service: AsyncMarketplaceDeploymentClient) -> None:
        self._service = service

    async def create(
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

            >>> await client.create(agreement_id='agmt-1234', catalog='AWSMarketplace', product_id='product-1234', deployment_parameter={'name': 'ExampleDeploymentParameterName', 'secretString': '{"apiKey": "helloWorldApiKey", "entityId": "fooBarEntityId"}'}, client_token='some-unique-uuid-between-32-and-64-characters')
            Creating a simple deployment parameter, with tags and expiration.
            The following example demonstrates creating a simple deployment parameter named "ExampleSimpleDeploymentParameterName". If multiple secrets are not required, the `secretString` may be provided in String format. The provided tags are only applied on resource creation and will be ignored if the operation results in an update. The API response includes the tags present on the resource after completion of the operation.

            >>> await client.create(agreement_id='agmt-1234', catalog='AWSMarketplace', product_id='product-1234', deployment_parameter={'name': 'ExampleSimpleDeploymentParameterName', 'secretString': 'MySimpleValue'}, client_token='some-unique-uuid-between-32-and-64-characters', expiration_date='2099-11-18T08:52:46.397Z', tags={'FooKey': 'BarValue', 'HelloKey': 'WorldValue'})
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

        def _redact_input(
            input_: "capo_marketplace_deployment.types.put_deployment_parameter_request.PutDeploymentParameterRequest",
        ) -> dict[str, Any]:
            import capo_marketplace_deployment.types.put_deployment_parameter_request

            return capo_marketplace_deployment.types.put_deployment_parameter_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("PutDeploymentParameter", redact_input=_redact_input),
        )
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
