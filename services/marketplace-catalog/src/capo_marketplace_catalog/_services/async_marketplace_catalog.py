"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#AWSMPSeymour``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_marketplace_catalog._auth._signers
import capo_marketplace_catalog._auth._sigv4
from capo_marketplace_catalog._auth._identity import Credentials
from capo_marketplace_catalog._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_marketplace_catalog._auth._zapros_handler import AuthMiddleware
from capo_marketplace_catalog._pagination import resolve_path as _resolve_path
from capo_marketplace_catalog._services._aws_config import aaws_config
from capo_marketplace_catalog._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.assessment_identifier
    import capo_marketplace_catalog.types.assessment_summary
    import capo_marketplace_catalog.types.assessment_target_filter
    import capo_marketplace_catalog.types.batch_describe_entities_request
    import capo_marketplace_catalog.types.batch_describe_entities_response
    import capo_marketplace_catalog.types.cancel_change_set_request
    import capo_marketplace_catalog.types.cancel_change_set_response
    import capo_marketplace_catalog.types.catalog
    import capo_marketplace_catalog.types.change_set_name
    import capo_marketplace_catalog.types.change_set_summary_list_item
    import capo_marketplace_catalog.types.client_request_token
    import capo_marketplace_catalog.types.control_assessment
    import capo_marketplace_catalog.types.delete_resource_policy_request
    import capo_marketplace_catalog.types.delete_resource_policy_response
    import capo_marketplace_catalog.types.describe_assessment_max_result_integer
    import capo_marketplace_catalog.types.describe_assessment_request
    import capo_marketplace_catalog.types.describe_assessment_response
    import capo_marketplace_catalog.types.describe_change_set_request
    import capo_marketplace_catalog.types.describe_change_set_response
    import capo_marketplace_catalog.types.describe_entity_request
    import capo_marketplace_catalog.types.describe_entity_response
    import capo_marketplace_catalog.types.entity_request_list
    import capo_marketplace_catalog.types.entity_summary
    import capo_marketplace_catalog.types.entity_type
    import capo_marketplace_catalog.types.entity_type_filters
    import capo_marketplace_catalog.types.entity_type_sort
    import capo_marketplace_catalog.types.filter_list
    import capo_marketplace_catalog.types.framework_filters
    import capo_marketplace_catalog.types.framework_id
    import capo_marketplace_catalog.types.get_resource_policy_request
    import capo_marketplace_catalog.types.get_resource_policy_response
    import capo_marketplace_catalog.types.intent
    import capo_marketplace_catalog.types.list_assessments_max_result_integer
    import capo_marketplace_catalog.types.list_assessments_request
    import capo_marketplace_catalog.types.list_assessments_response
    import capo_marketplace_catalog.types.list_change_sets_max_result_integer
    import capo_marketplace_catalog.types.list_change_sets_request
    import capo_marketplace_catalog.types.list_change_sets_response
    import capo_marketplace_catalog.types.list_entities_max_result_integer
    import capo_marketplace_catalog.types.list_entities_request
    import capo_marketplace_catalog.types.list_entities_response
    import capo_marketplace_catalog.types.list_tags_for_resource_request
    import capo_marketplace_catalog.types.list_tags_for_resource_response
    import capo_marketplace_catalog.types.next_token
    import capo_marketplace_catalog.types.ownership_type
    import capo_marketplace_catalog.types.put_resource_policy_request
    import capo_marketplace_catalog.types.put_resource_policy_response
    import capo_marketplace_catalog.types.requested_change_list
    import capo_marketplace_catalog.types.resource_arn
    import capo_marketplace_catalog.types.resource_id
    import capo_marketplace_catalog.types.resource_policy_json
    import capo_marketplace_catalog.types.sort
    import capo_marketplace_catalog.types.start_change_set_request
    import capo_marketplace_catalog.types.start_change_set_response
    import capo_marketplace_catalog.types.tag_key_list
    import capo_marketplace_catalog.types.tag_list
    import capo_marketplace_catalog.types.tag_resource_request
    import capo_marketplace_catalog.types.tag_resource_response
    import capo_marketplace_catalog.types.untag_resource_request
    import capo_marketplace_catalog.types.untag_resource_response


class AsyncMarketplaceCatalogClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncMarketplaceCatalogClient:
    """A client for the ``MarketplaceCatalog`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncMarketplaceCatalogClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncMarketplaceCatalogClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def batch_describe_entities(
        self,
        entity_request_list: "capo_marketplace_catalog.types.entity_request_list.EntityRequestList",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
    ) -> "capo_marketplace_catalog.types.batch_describe_entities_response.BatchDescribeEntitiesResponse":
        """<p>Returns metadata and content for multiple entities. This is the Batch version of the <code>DescribeEntity</code> API and uses the same IAM permission action as <code>DescribeEntity</code> API.</p>

        Args:
            entity_request_list: <p>List of entity IDs and the catalogs the entities are present in.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.batch_describe_entities_request.BatchDescribeEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.batch_describe_entities_response.BatchDescribeEntitiesResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.batch_describe_entities

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.batch_describe_entities.async_batch_describe_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.batch_describe_entities_request.BatchDescribeEntitiesRequest = {
            "entity_request_list": entity_request_list
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_change_set(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        change_set_id: "capo_marketplace_catalog.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
    ) -> "capo_marketplace_catalog.types.cancel_change_set_response.CancelChangeSetResponse":
        """<p>Used to cancel an open change request. Must be sent before the status of the request changes to <code>APPLYING</code>, the final stage of completing your change request. You can describe a change during the 60-day request history retention period for API calls.</p>

        Args:
            catalog: <p>Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code>.</p>
            change_set_id: <p>Required. The unique identifier of the <code>StartChangeSet</code> request that you want to cancel.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is currently in use.</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.cancel_change_set_request.CancelChangeSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.cancel_change_set_response.CancelChangeSetResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.cancel_change_set

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.cancel_change_set.async_cancel_change_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.cancel_change_set_request.CancelChangeSetRequest = {
            "catalog": catalog,
            "change_set_id": change_set_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "capo_marketplace_catalog.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
    ) -> "capo_marketplace_catalog.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a resource-based policy on an entity that is identified by its resource ARN.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the entity resource that is associated with the resource policy.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_assessment(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        assessment_identifier: "capo_marketplace_catalog.types.assessment_identifier.AssessmentIdentifier",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
        max_results: Optional[
            "capo_marketplace_catalog.types.describe_assessment_max_result_integer.DescribeAssessmentMaxResultInteger"
        ] = None,
        next_token: Optional[
            "capo_marketplace_catalog.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_catalog.types.describe_assessment_response.DescribeAssessmentResponse":
        """<p>Returns the metadata and detailed results of a single assessment, including the framework that was evaluated, the overall assessment result, and a paginated list of individual control evaluation results.</p> <p>To list available assessments before describing one, use the <code>ListAssessments</code> action.</p>

        Args:
            catalog: <p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            assessment_identifier: <p>The unique identifier of the assessment to describe. You can provide either the assessment ID (for example, <code>assessment-12345</code>) or the full assessment ARN (for example, <code>arn:aws:aws-marketplace:us-east-1::AWSMarketplace/Assessment/assessment-12345</code>).</p>
            max_results: <p>Specifies the upper limit of <code>ControlAssessment</code> elements returned on a single page. If a value isn't provided, the default value is 50. Valid values range from 1 to 100.</p>
            next_token: <p>The value of the next token, if it exists. <code>null</code> if there are no more results.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.describe_assessment_request.DescribeAssessmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.describe_assessment_response.DescribeAssessmentResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.describe_assessment

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.describe_assessment.async_describe_assessment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.describe_assessment_request.DescribeAssessmentRequest = {
            "catalog": catalog,
            "assessment_identifier": assessment_identifier,
        }
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

    async def iter_describe_assessment(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        assessment_identifier: "capo_marketplace_catalog.types.assessment_identifier.AssessmentIdentifier",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
        max_results: Optional[
            "capo_marketplace_catalog.types.describe_assessment_max_result_integer.DescribeAssessmentMaxResultInteger"
        ] = None,
        next_token: Optional[
            "capo_marketplace_catalog.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_catalog.types.control_assessment.ControlAssessment]":
        _token = next_token
        while True:
            _response = await self.describe_assessment(
                catalog,
                assessment_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("control_assessments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_change_set(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        change_set_id: "capo_marketplace_catalog.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
    ) -> "capo_marketplace_catalog.types.describe_change_set_response.DescribeChangeSetResponse":
        """<p>Provides information about a given change set.</p>

        Args:
            catalog: <p>Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            change_set_id: <p>Required. The unique identifier for the <code>StartChangeSet</code> request that you want to describe the details for.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.describe_change_set_request.DescribeChangeSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.describe_change_set_response.DescribeChangeSetResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.describe_change_set

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.describe_change_set.async_describe_change_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.describe_change_set_request.DescribeChangeSetRequest = {
            "catalog": catalog,
            "change_set_id": change_set_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_entity(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        entity_id: "capo_marketplace_catalog.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
    ) -> (
        "capo_marketplace_catalog.types.describe_entity_response.DescribeEntityResponse"
    ):
        """<p>Returns the metadata and content of the entity.</p>

        Args:
            catalog: <p>Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            entity_id: <p>Required. The unique ID of the entity to describe.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.resource_not_supported_exception.ResourceNotSupportedException: <p>Currently, the specified resource is not supported.</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.describe_entity_request.DescribeEntityRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.describe_entity_response.DescribeEntityResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.describe_entity

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.describe_entity.async_describe_entity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.describe_entity_request.DescribeEntityRequest = {
            "catalog": catalog,
            "entity_id": entity_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_marketplace_catalog.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
    ) -> "capo_marketplace_catalog.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Gets a resource-based policy of an entity that is identified by its resource ARN.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the entity resource that is associated with the resource policy.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_assessments(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
        framework_id: Optional[
            "capo_marketplace_catalog.types.framework_id.FrameworkId"
        ] = None,
        assessment_target_filter: Optional[
            "capo_marketplace_catalog.types.assessment_target_filter.AssessmentTargetFilter"
        ] = None,
        framework_filters: Optional[
            "capo_marketplace_catalog.types.framework_filters.FrameworkFilters"
        ] = None,
        max_results: Optional[
            "capo_marketplace_catalog.types.list_assessments_max_result_integer.ListAssessmentsMaxResultInteger"
        ] = None,
        next_token: Optional[
            "capo_marketplace_catalog.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_catalog.types.list_assessments_response.ListAssessmentsResponse":
        """<p>Returns a paginated list of assessments associated with an entity or change set in AWS Marketplace. An <i>assessment</i> is the result of evaluating a product or change set against a framework, such as AMI Security or Container Security.</p> <p>Use the <code>AssessmentTargetFilter</code> to scope results to a specific entity or change set, and use <code>FrameworkFilters</code> to scope results to a single framework. To retrieve detailed control-level results for an individual assessment, use the <code>DescribeAssessment</code> action.</p> <p>Results are sorted by assessment creation time in descending order.</p>

        Args:
            catalog: <p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            framework_id: <p>The unique identifier of a framework. When specified, only assessments performed against this framework are returned. For example, <code>AMISecurity</code>.</p>
            assessment_target_filter: <p>Filters the list of assessments to those performed against a specific entity or change set.</p>
            framework_filters: <p>Framework-specific filters. Set exactly one member to filter results to assessments performed against that framework.</p>
            max_results: <p>Specifies the upper limit of the elements on a single page. If a value isn't provided, the default value is 20. Valid values range from 1 to 100.</p>
            next_token: <p>The value of the next token, if it exists. <code>null</code> if there are no more results.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.list_assessments_request.ListAssessmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.list_assessments_response.ListAssessmentsResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.list_assessments

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.list_assessments.async_list_assessments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.list_assessments_request.ListAssessmentsRequest = {
            "catalog": catalog
        }
        if framework_id is not None:
            input_["framework_id"] = framework_id
        if assessment_target_filter is not None:
            input_["assessment_target_filter"] = assessment_target_filter
        if framework_filters is not None:
            input_["framework_filters"] = framework_filters
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

    async def iter_list_assessments(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
        framework_id: Optional[
            "capo_marketplace_catalog.types.framework_id.FrameworkId"
        ] = None,
        assessment_target_filter: Optional[
            "capo_marketplace_catalog.types.assessment_target_filter.AssessmentTargetFilter"
        ] = None,
        framework_filters: Optional[
            "capo_marketplace_catalog.types.framework_filters.FrameworkFilters"
        ] = None,
        max_results: Optional[
            "capo_marketplace_catalog.types.list_assessments_max_result_integer.ListAssessmentsMaxResultInteger"
        ] = None,
        next_token: Optional[
            "capo_marketplace_catalog.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_catalog.types.assessment_summary.AssessmentSummary]":
        _token = next_token
        while True:
            _response = await self.list_assessments(
                catalog,
                config_overrides=config_overrides,
                framework_id=framework_id,
                assessment_target_filter=assessment_target_filter,
                framework_filters=framework_filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("assessment_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_change_sets(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
        filter_list: Optional[
            "capo_marketplace_catalog.types.filter_list.FilterList"
        ] = None,
        sort: Optional["capo_marketplace_catalog.types.sort.Sort"] = None,
        max_results: Optional[
            "capo_marketplace_catalog.types.list_change_sets_max_result_integer.ListChangeSetsMaxResultInteger"
        ] = None,
        next_token: Optional[
            "capo_marketplace_catalog.types.next_token.NextToken"
        ] = None,
    ) -> "capo_marketplace_catalog.types.list_change_sets_response.ListChangeSetsResponse":
        """<p>Returns the list of change sets owned by the account being used to make the call. You can filter this list by providing any combination of <code>entityId</code>, <code>ChangeSetName</code>, and status. If you provide more than one filter, the API operation applies a logical AND between the filters.</p> <p>You can describe a change during the 60-day request history retention period for API calls.</p>

        Args:
            catalog: <p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            filter_list: <p>An array of filter objects.</p>
            sort: <p>An object that contains two attributes, <code>SortBy</code> and <code>SortOrder</code>.</p>
            max_results: <p>The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results. By default, this value is 20.</p>
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.list_change_sets_request.ListChangeSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.list_change_sets_response.ListChangeSetsResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.list_change_sets

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.list_change_sets.async_list_change_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.list_change_sets_request.ListChangeSetsRequest = {
            "catalog": catalog
        }
        if filter_list is not None:
            input_["filter_list"] = filter_list
        if sort is not None:
            input_["sort"] = sort
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

    async def iter_list_change_sets(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
        filter_list: Optional[
            "capo_marketplace_catalog.types.filter_list.FilterList"
        ] = None,
        sort: Optional["capo_marketplace_catalog.types.sort.Sort"] = None,
        max_results: Optional[
            "capo_marketplace_catalog.types.list_change_sets_max_result_integer.ListChangeSetsMaxResultInteger"
        ] = None,
        next_token: Optional[
            "capo_marketplace_catalog.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_catalog.types.change_set_summary_list_item.ChangeSetSummaryListItem]":
        _token = next_token
        while True:
            _response = await self.list_change_sets(
                catalog,
                config_overrides=config_overrides,
                filter_list=filter_list,
                sort=sort,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("change_set_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_entities(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        entity_type: "capo_marketplace_catalog.types.entity_type.EntityType",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
        filter_list: Optional[
            "capo_marketplace_catalog.types.filter_list.FilterList"
        ] = None,
        sort: Optional["capo_marketplace_catalog.types.sort.Sort"] = None,
        next_token: Optional[
            "capo_marketplace_catalog.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_marketplace_catalog.types.list_entities_max_result_integer.ListEntitiesMaxResultInteger"
        ] = None,
        ownership_type: Optional[
            "capo_marketplace_catalog.types.ownership_type.OwnershipType"
        ] = None,
        entity_type_filters: Optional[
            "capo_marketplace_catalog.types.entity_type_filters.EntityTypeFilters"
        ] = None,
        entity_type_sort: Optional[
            "capo_marketplace_catalog.types.entity_type_sort.EntityTypeSort"
        ] = None,
    ) -> "capo_marketplace_catalog.types.list_entities_response.ListEntitiesResponse":
        """<p>Provides the list of entities of a given type.</p>

        Args:
            catalog: <p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            entity_type: <p>The type of entities to retrieve. Valid values are: <code>AmiProduct</code>, <code>ContainerProduct</code>, <code>DataProduct</code>, <code>SaaSProduct</code>, <code>ProcurementPolicy</code>, <code>Experience</code>, <code>Audience</code>, <code>BrandingSettings</code>, <code>Offer</code>, <code>OfferSet</code>, <code>Seller</code>, <code>ResaleAuthorization</code>, <code>Solution</code>.</p>
            filter_list: <p>An array of filter objects. Each filter object contains two attributes, <code>filterName</code> and <code>filterValues</code>.</p>
            sort: <p>An object that contains two attributes, <code>SortBy</code> and <code>SortOrder</code>.</p>
            next_token: <p>The value of the next token, if it exists. Null if there are no more results.</p>
            max_results: <p>Specifies the upper limit of the elements on a single page. If a value isn't provided, the default value is 20.</p>
            ownership_type: <p>Filters the returned set of entities based on their owner. The default is <code>SELF</code>. To list entities shared with you through AWS Resource Access Manager (AWS RAM), set to <code>SHARED</code>. Entities shared through the AWS Marketplace Catalog API <code>PutResourcePolicy</code> operation can't be discovered through the <code>SHARED</code> parameter.</p>
            entity_type_filters: <p>A Union object containing filter shapes for all <code>EntityType</code>s. Each <code>EntityTypeFilter</code> shape will have filters applicable for that <code>EntityType</code> that can be used to search or filter entities.</p>
            entity_type_sort: <p>A Union object containing <code>Sort</code> shapes for all <code>EntityType</code>s. Each <code>EntityTypeSort</code> shape will have <code>SortBy</code> and <code>SortOrder</code> applicable for fields on that <code>EntityType</code>. This can be used to sort the results of the filter query.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.list_entities_request.ListEntitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.list_entities_response.ListEntitiesResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.list_entities

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.list_entities.async_list_entities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.list_entities_request.ListEntitiesRequest = {
            "catalog": catalog,
            "entity_type": entity_type,
        }
        if filter_list is not None:
            input_["filter_list"] = filter_list
        if sort is not None:
            input_["sort"] = sort
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if ownership_type is not None:
            input_["ownership_type"] = ownership_type
        if entity_type_filters is not None:
            input_["entity_type_filters"] = entity_type_filters
        if entity_type_sort is not None:
            input_["entity_type_sort"] = entity_type_sort

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_entities(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        entity_type: "capo_marketplace_catalog.types.entity_type.EntityType",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
        filter_list: Optional[
            "capo_marketplace_catalog.types.filter_list.FilterList"
        ] = None,
        sort: Optional["capo_marketplace_catalog.types.sort.Sort"] = None,
        next_token: Optional[
            "capo_marketplace_catalog.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_marketplace_catalog.types.list_entities_max_result_integer.ListEntitiesMaxResultInteger"
        ] = None,
        ownership_type: Optional[
            "capo_marketplace_catalog.types.ownership_type.OwnershipType"
        ] = None,
        entity_type_filters: Optional[
            "capo_marketplace_catalog.types.entity_type_filters.EntityTypeFilters"
        ] = None,
        entity_type_sort: Optional[
            "capo_marketplace_catalog.types.entity_type_sort.EntityTypeSort"
        ] = None,
    ) -> "AsyncIterator[capo_marketplace_catalog.types.entity_summary.EntitySummary]":
        _token = next_token
        while True:
            _response = await self.list_entities(
                catalog,
                entity_type,
                config_overrides=config_overrides,
                filter_list=filter_list,
                sort=sort,
                next_token=_token,
                max_results=max_results,
                ownership_type=ownership_type,
                entity_type_filters=entity_type_filters,
                entity_type_sort=entity_type_sort,
            )
            _page = _resolve_path(_response, ("entity_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_marketplace_catalog.types.resource_arn.ResourceARN",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
    ) -> "capo_marketplace_catalog.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all tags that have been added to a resource (either an <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities">entity</a> or <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets">change set</a>).</p>

        Args:
            resource_arn: <p>Required. The Amazon Resource Name (ARN) associated with the resource you want to list tags on.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "capo_marketplace_catalog.types.resource_arn.ResourceARN",
        policy: "capo_marketplace_catalog.types.resource_policy_json.ResourcePolicyJson",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
    ) -> "capo_marketplace_catalog.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Attaches a resource-based policy to an entity. Examples of an entity include: <code>AmiProduct</code> and <code>ContainerProduct</code>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the entity resource you want to associate with a resource policy.</p>
            policy: <p>The policy document to set; formatted in JSON.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_change_set(
        self,
        catalog: "capo_marketplace_catalog.types.catalog.Catalog",
        change_set: "capo_marketplace_catalog.types.requested_change_list.RequestedChangeList",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
        change_set_name: Optional[
            "capo_marketplace_catalog.types.change_set_name.ChangeSetName"
        ] = None,
        client_request_token: Optional[
            "capo_marketplace_catalog.types.client_request_token.ClientRequestToken"
        ] = None,
        change_set_tags: Optional[
            "capo_marketplace_catalog.types.tag_list.TagList"
        ] = None,
        intent: Optional["capo_marketplace_catalog.types.intent.Intent"] = None,
    ) -> "capo_marketplace_catalog.types.start_change_set_response.StartChangeSetResponse":
        """<p>Allows you to request changes for your entities. Within a single <code>ChangeSet</code>, you can't start the same change type against the same entity multiple times. Additionally, when a <code>ChangeSet</code> is running, all the entities targeted by the different changes are locked until the change set has completed (either succeeded, cancelled, or failed). If you try to start a change set containing a change against an entity that is already locked, you will receive a <code>ResourceInUseException</code> error.</p> <p>For example, you can't start the <code>ChangeSet</code> described in the <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_StartChangeSet.html#API_StartChangeSet_Examples">example</a> later in this topic because it contains two changes to run the same change type (<code>AddRevisions</code>) against the same entity (<code>entity-id@1</code>).</p> <p>For more information about working with change sets, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets"> Working with change sets</a>. For information about change types for single-AMI products, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#working-with-single-AMI-products">Working with single-AMI products</a>. Also, for more information about change types available for container-based products, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html#working-with-container-products">Working with container products</a>.</p> <p>To download "DetailsDocument" shapes, see <a href="https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python">Python</a> and <a href="https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-java/tree/main">Java</a> shapes on GitHub.</p>

        Args:
            catalog: <p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>
            change_set: <p>Array of <code>change</code> object.</p>
            change_set_name: <p>Optional case sensitive string of up to 100 ASCII characters. The change set name can be used to filter the list of change sets. </p>
            client_request_token: <p>A unique token to identify the request to ensure idempotency.</p>
            change_set_tags: <p>A list of objects specifying each key name and value for the <code>ChangeSetTags</code> property.</p>
            intent: <p>The intent related to the request. The default is <code>APPLY</code>. To test your request before applying changes to your entities, use <code>VALIDATE</code>. This feature is currently available for adding versions to single-AMI products. For more information, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#ami-add-version">Add a new version</a>.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_in_use_exception.ResourceInUseException: <p>The resource is currently in use.</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The maximum number of open requests per account has been exceeded.</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.start_change_set_request.StartChangeSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.start_change_set_response.StartChangeSetResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.start_change_set

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.start_change_set.async_start_change_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.start_change_set_request.StartChangeSetRequest = {
            "catalog": catalog,
            "change_set": change_set,
        }
        if change_set_name is not None:
            input_["change_set_name"] = change_set_name
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if change_set_tags is not None:
            input_["change_set_tags"] = change_set_tags
        if intent is not None:
            input_["intent"] = intent

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_marketplace_catalog.types.resource_arn.ResourceARN",
        tags: "capo_marketplace_catalog.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
    ) -> "capo_marketplace_catalog.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource (either an <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities">entity</a> or <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets">change set</a>).</p>

        Args:
            resource_arn: <p>Required. The Amazon Resource Name (ARN) associated with the resource you want to tag.</p>
            tags: <p>Required. A list of objects specifying each key name and value. Number of objects allowed: 1-50.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.tag_resource

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_marketplace_catalog.types.resource_arn.ResourceARN",
        tag_keys: "capo_marketplace_catalog.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncMarketplaceCatalogClientConfig] = None,
    ) -> "capo_marketplace_catalog.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or list of tags from a resource (either an <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities">entity</a> or <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets">change set</a>).</p>

        Args:
            resource_arn: <p>Required. The Amazon Resource Name (ARN) associated with the resource you want to remove the tag from.</p>
            tag_keys: <p>Required. A list of key names of tags to be removed. Number of strings allowed: 0-256.</p>

        Raises:
            capo_marketplace_catalog.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p> <p>HTTP status code: 403</p>
            capo_marketplace_catalog.errors.internal_service_exception.InternalServiceException: <p>There was an internal service exception.</p> <p>HTTP status code: 500</p>
            capo_marketplace_catalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource wasn't found.</p> <p>HTTP status code: 404</p>
            capo_marketplace_catalog.errors.throttling_exception.ThrottlingException: <p>Too many requests.</p> <p>HTTP status code: 429</p>
            capo_marketplace_catalog.errors.validation_exception.ValidationException: <p>An error occurred during validation.</p> <p>HTTP status code: 422</p>
            capo_marketplace_catalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_marketplace_catalog.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_marketplace_catalog.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_marketplace_catalog._operations.awsmp_seymour.untag_resource

            (
                output,
                http_response,
            ) = await capo_marketplace_catalog._operations.awsmp_seymour.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_catalog.types.untag_resource_request.UntagResourceRequest = {
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
