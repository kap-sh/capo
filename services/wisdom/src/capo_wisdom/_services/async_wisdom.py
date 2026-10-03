"""Generated from Smithy shape ``com.amazonaws.wisdom#WisdomService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_wisdom._auth._signers
import capo_wisdom._auth._sigv4
from capo_wisdom._auth._identity import Credentials
from capo_wisdom._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_wisdom._auth._zapros_handler import AuthMiddleware
from capo_wisdom._pagination import resolve_path as _resolve_path
from capo_wisdom._resources.wisdom_service.assistant import AsyncAssistant
from capo_wisdom._resources.wisdom_service.knowledge_base import AsyncKnowledgeBase
from capo_wisdom._services._aws_config import aaws_config
from capo_wisdom._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_wisdom.types.arn
    import capo_wisdom.types.assistant_association_input_data
    import capo_wisdom.types.assistant_association_summary
    import capo_wisdom.types.assistant_summary
    import capo_wisdom.types.assistant_type
    import capo_wisdom.types.association_type
    import capo_wisdom.types.channels
    import capo_wisdom.types.client_token
    import capo_wisdom.types.contact_attributes
    import capo_wisdom.types.content_metadata
    import capo_wisdom.types.content_summary
    import capo_wisdom.types.content_title
    import capo_wisdom.types.content_type
    import capo_wisdom.types.create_assistant_association_request
    import capo_wisdom.types.create_assistant_association_response
    import capo_wisdom.types.create_assistant_request
    import capo_wisdom.types.create_assistant_response
    import capo_wisdom.types.create_content_request
    import capo_wisdom.types.create_content_response
    import capo_wisdom.types.create_knowledge_base_request
    import capo_wisdom.types.create_knowledge_base_response
    import capo_wisdom.types.create_quick_response_request
    import capo_wisdom.types.create_quick_response_response
    import capo_wisdom.types.create_session_request
    import capo_wisdom.types.create_session_response
    import capo_wisdom.types.delete_assistant_association_request
    import capo_wisdom.types.delete_assistant_association_response
    import capo_wisdom.types.delete_assistant_request
    import capo_wisdom.types.delete_assistant_response
    import capo_wisdom.types.delete_content_request
    import capo_wisdom.types.delete_content_response
    import capo_wisdom.types.delete_import_job_request
    import capo_wisdom.types.delete_import_job_response
    import capo_wisdom.types.delete_knowledge_base_request
    import capo_wisdom.types.delete_knowledge_base_response
    import capo_wisdom.types.delete_quick_response_request
    import capo_wisdom.types.delete_quick_response_response
    import capo_wisdom.types.description
    import capo_wisdom.types.external_source_configuration
    import capo_wisdom.types.get_assistant_association_request
    import capo_wisdom.types.get_assistant_association_response
    import capo_wisdom.types.get_assistant_request
    import capo_wisdom.types.get_assistant_response
    import capo_wisdom.types.get_content_request
    import capo_wisdom.types.get_content_response
    import capo_wisdom.types.get_content_summary_request
    import capo_wisdom.types.get_content_summary_response
    import capo_wisdom.types.get_import_job_request
    import capo_wisdom.types.get_import_job_response
    import capo_wisdom.types.get_knowledge_base_request
    import capo_wisdom.types.get_knowledge_base_response
    import capo_wisdom.types.get_quick_response_request
    import capo_wisdom.types.get_quick_response_response
    import capo_wisdom.types.get_recommendations_request
    import capo_wisdom.types.get_recommendations_response
    import capo_wisdom.types.get_session_request
    import capo_wisdom.types.get_session_response
    import capo_wisdom.types.grouping_configuration
    import capo_wisdom.types.import_job_summary
    import capo_wisdom.types.import_job_type
    import capo_wisdom.types.knowledge_base_summary
    import capo_wisdom.types.knowledge_base_type
    import capo_wisdom.types.language_code
    import capo_wisdom.types.list_assistant_associations_request
    import capo_wisdom.types.list_assistant_associations_response
    import capo_wisdom.types.list_assistants_request
    import capo_wisdom.types.list_assistants_response
    import capo_wisdom.types.list_contents_request
    import capo_wisdom.types.list_contents_response
    import capo_wisdom.types.list_import_jobs_request
    import capo_wisdom.types.list_import_jobs_response
    import capo_wisdom.types.list_knowledge_bases_request
    import capo_wisdom.types.list_knowledge_bases_response
    import capo_wisdom.types.list_quick_responses_request
    import capo_wisdom.types.list_quick_responses_response
    import capo_wisdom.types.list_tags_for_resource_request
    import capo_wisdom.types.list_tags_for_resource_response
    import capo_wisdom.types.max_results
    import capo_wisdom.types.name
    import capo_wisdom.types.next_token
    import capo_wisdom.types.non_empty_string
    import capo_wisdom.types.notify_recommendations_received_request
    import capo_wisdom.types.notify_recommendations_received_response
    import capo_wisdom.types.query_assistant_request
    import capo_wisdom.types.query_assistant_response
    import capo_wisdom.types.query_text
    import capo_wisdom.types.quick_response_data_provider
    import capo_wisdom.types.quick_response_description
    import capo_wisdom.types.quick_response_name
    import capo_wisdom.types.quick_response_search_expression
    import capo_wisdom.types.quick_response_search_result_data
    import capo_wisdom.types.quick_response_summary
    import capo_wisdom.types.quick_response_type
    import capo_wisdom.types.recommendation_id_list
    import capo_wisdom.types.remove_knowledge_base_template_uri_request
    import capo_wisdom.types.remove_knowledge_base_template_uri_response
    import capo_wisdom.types.rendering_configuration
    import capo_wisdom.types.result_data
    import capo_wisdom.types.search_content_request
    import capo_wisdom.types.search_content_response
    import capo_wisdom.types.search_expression
    import capo_wisdom.types.search_quick_responses_request
    import capo_wisdom.types.search_quick_responses_response
    import capo_wisdom.types.search_sessions_request
    import capo_wisdom.types.search_sessions_response
    import capo_wisdom.types.server_side_encryption_configuration
    import capo_wisdom.types.session_summary
    import capo_wisdom.types.short_cut_key
    import capo_wisdom.types.source_configuration
    import capo_wisdom.types.start_content_upload_request
    import capo_wisdom.types.start_content_upload_response
    import capo_wisdom.types.start_import_job_request
    import capo_wisdom.types.start_import_job_response
    import capo_wisdom.types.tag_key_list
    import capo_wisdom.types.tag_resource_request
    import capo_wisdom.types.tag_resource_response
    import capo_wisdom.types.tags
    import capo_wisdom.types.time_to_live
    import capo_wisdom.types.untag_resource_request
    import capo_wisdom.types.untag_resource_response
    import capo_wisdom.types.update_content_request
    import capo_wisdom.types.update_content_response
    import capo_wisdom.types.update_knowledge_base_template_uri_request
    import capo_wisdom.types.update_knowledge_base_template_uri_response
    import capo_wisdom.types.update_quick_response_request
    import capo_wisdom.types.update_quick_response_response
    import capo_wisdom.types.upload_id
    import capo_wisdom.types.uri
    import capo_wisdom.types.uuid
    import capo_wisdom.types.uuid_or_arn
    import capo_wisdom.types.wait_time_seconds


class AsyncWisdomClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncWisdomClient:
    """A client for the ``Wisdom`` service.

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
        self._config = AsyncWisdomClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.assistant = AsyncAssistant(self)
        self.knowledge_base = AsyncKnowledgeBase(self)

    def operation_options(
        self, config_overrides: Optional[AsyncWisdomClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncWisdomClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_wisdom.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> (
        "capo_wisdom.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_wisdom.types.arn.Arn",
        tags: "capo_wisdom.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.too_many_tags_exception.TooManyTagsException: <p>Amazon Connect Wisdom throws this exception if you have too many tags in your tag set.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_wisdom.types.arn.Arn",
        tag_keys: "capo_wisdom.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys.</p>

        Raises:
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_assistant(
        self,
        name: "capo_wisdom.types.name.Name",
        type: "capo_wisdom.types.assistant_type.AssistantType",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        client_token: Optional["capo_wisdom.types.client_token.ClientToken"] = None,
        description: Optional["capo_wisdom.types.description.Description"] = None,
        tags: Optional["capo_wisdom.types.tags.Tags"] = None,
        server_side_encryption_configuration: Optional[
            "capo_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
    ) -> "capo_wisdom.types.create_assistant_response.CreateAssistantResponse":
        """<p>Creates an Amazon Connect Wisdom assistant.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the assistant.</p>
            type: <p>The type of assistant.</p>
            description: <p>The description of the assistant.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>The customer managed key must have a policy that allows <code>kms:CreateGrant</code>, <code> kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Wisdom, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html">Enable Amazon Connect Wisdom for your instance</a>.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.create_assistant_request.CreateAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.create_assistant_response.CreateAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.create_assistant

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.create_assistant.async_create_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.create_assistant_request.CreateAssistantRequest = {
            "name": name,
            "type": type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_assistant(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.get_assistant_response.GetAssistantResponse":
        """<p>Retrieves information about an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_assistant_request.GetAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_assistant_response.GetAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_assistant

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_assistant.async_get_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.get_assistant_request.GetAssistantRequest = {
            "assistant_id": assistant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_assistant(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.delete_assistant_response.DeleteAssistantResponse":
        """<p>Deletes an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.delete_assistant_request.DeleteAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.delete_assistant_response.DeleteAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.delete_assistant

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.delete_assistant.async_delete_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.delete_assistant_request.DeleteAssistantRequest = {
            "assistant_id": assistant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_assistants(
        self,
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.list_assistants_response.ListAssistantsResponse":
        """<p>Lists information about assistants.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.list_assistants_request.ListAssistantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.list_assistants_response.ListAssistantsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.list_assistants

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.list_assistants.async_list_assistants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.list_assistants_request.ListAssistantsRequest = {}
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

    async def iter_list_assistants(
        self,
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_wisdom.types.assistant_summary.AssistantSummary]":
        _token = next_token
        while True:
            _response = await self.list_assistants(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("assistant_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_recommendations(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
        wait_time_seconds: Optional[
            "capo_wisdom.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "capo_wisdom.types.get_recommendations_response.GetRecommendationsResponse":
        """<p>Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_NotifyRecommendationsReceived.html">NotifyRecommendationsReceived</a>. This API supports long-polling behavior with the <code>waitTimeSeconds</code> parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_QueryAssistant.html">QueryAssistant</a>.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            wait_time_seconds: <p>The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_recommendations_request.GetRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_recommendations_response.GetRecommendationsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_recommendations

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_recommendations.async_get_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.get_recommendations_request.GetRecommendationsRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def notify_recommendations_received(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        recommendation_ids: "capo_wisdom.types.recommendation_id_list.RecommendationIdList",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse":
        """<p>Removes the specified recommendations from the specified assistant's queue of newly available recommendations. You can use this API in conjunction with <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a> and a <code>waitTimeSeconds</code> input for long-polling behavior and avoiding duplicate recommendations.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            recommendation_ids: <p>The identifiers of the recommendations.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.notify_recommendations_received

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.notify_recommendations_received.async_notify_recommendations_received(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
            "recommendation_ids": recommendation_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def query_assistant(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        query_text: "capo_wisdom.types.query_text.QueryText",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.query_assistant_response.QueryAssistantResponse":
        """<p>Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a>. </p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_text: <p>The text to search for.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.query_assistant_request.QueryAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.query_assistant_response.QueryAssistantResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.query_assistant

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.query_assistant.async_query_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.query_assistant_request.QueryAssistantRequest = {
            "assistant_id": assistant_id,
            "query_text": query_text,
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

    async def iter_query_assistant(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        query_text: "capo_wisdom.types.query_text.QueryText",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_wisdom.types.result_data.ResultData]":
        _token = next_token
        while True:
            _response = await self.query_assistant(
                assistant_id,
                query_text,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_sessions(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_wisdom.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.search_sessions_response.SearchSessionsResponse":
        """<p>Searches for sessions.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.search_sessions_request.SearchSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.search_sessions_response.SearchSessionsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.search_sessions

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.search_sessions.async_search_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.search_sessions_request.SearchSessionsRequest = {
            "assistant_id": assistant_id,
            "search_expression": search_expression,
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

    async def iter_search_sessions(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_wisdom.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_wisdom.types.session_summary.SessionSummary]":
        _token = next_token
        while True:
            _response = await self.search_sessions(
                assistant_id,
                search_expression,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("session_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_assistant_association(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        association_type: "capo_wisdom.types.association_type.AssociationType",
        association: "capo_wisdom.types.assistant_association_input_data.AssistantAssociationInputData",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        client_token: Optional["capo_wisdom.types.client_token.ClientToken"] = None,
        tags: Optional["capo_wisdom.types.tags.Tags"] = None,
    ) -> "capo_wisdom.types.create_assistant_association_response.CreateAssistantAssociationResponse":
        """<p>Creates an association between an Amazon Connect Wisdom assistant and another resource. Currently, the only supported association is with a knowledge base. An assistant can have only a single association.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            association_type: <p>The type of association.</p>
            association: <p>The identifier of the associated resource.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.create_assistant_association_request.CreateAssistantAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.create_assistant_association_response.CreateAssistantAssociationResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.create_assistant_association

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.create_assistant_association.async_create_assistant_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.create_assistant_association_request.CreateAssistantAssociationRequest = {
            "assistant_id": assistant_id,
            "association_type": association_type,
            "association": association,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_assistant_association(
        self,
        assistant_association_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.get_assistant_association_response.GetAssistantAssociationResponse":
        """<p>Retrieves information about an assistant association.</p>

        Args:
            assistant_association_id: <p>The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_assistant_association_request.GetAssistantAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_assistant_association_response.GetAssistantAssociationResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_assistant_association

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_assistant_association.async_get_assistant_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.get_assistant_association_request.GetAssistantAssociationRequest = {
            "assistant_association_id": assistant_association_id,
            "assistant_id": assistant_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_assistant_association(
        self,
        assistant_association_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.delete_assistant_association_response.DeleteAssistantAssociationResponse":
        """<p>Deletes an assistant association.</p>

        Args:
            assistant_association_id: <p>The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.delete_assistant_association_request.DeleteAssistantAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.delete_assistant_association_response.DeleteAssistantAssociationResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.delete_assistant_association

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.delete_assistant_association.async_delete_assistant_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.delete_assistant_association_request.DeleteAssistantAssociationRequest = {
            "assistant_association_id": assistant_association_id,
            "assistant_id": assistant_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_assistant_associations(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.list_assistant_associations_response.ListAssistantAssociationsResponse":
        """<p>Lists information about assistant associations.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.list_assistant_associations_request.ListAssistantAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.list_assistant_associations_response.ListAssistantAssociationsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.list_assistant_associations

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.list_assistant_associations.async_list_assistant_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.list_assistant_associations_request.ListAssistantAssociationsRequest = {
            "assistant_id": assistant_id
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

    async def iter_list_assistant_associations(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_wisdom.types.assistant_association_summary.AssistantAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_assistant_associations(
                assistant_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("assistant_association_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_session(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        name: "capo_wisdom.types.name.Name",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        client_token: Optional["capo_wisdom.types.client_token.ClientToken"] = None,
        description: Optional["capo_wisdom.types.description.Description"] = None,
        tags: Optional["capo_wisdom.types.tags.Tags"] = None,
    ) -> "capo_wisdom.types.create_session_response.CreateSessionResponse":
        """<p>Creates a session. A session is a contextual container used for generating recommendations. Amazon Connect creates a new Wisdom session for each contact on which Wisdom is enabled.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            name: <p>The name of the session.</p>
            description: <p>The description.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.create_session_request.CreateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.create_session_response.CreateSessionResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.create_session

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.create_session.async_create_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.create_session_request.CreateSessionRequest = {
            "assistant_id": assistant_id,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_session(
        self,
        assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.get_session_response.GetSessionResponse":
        """<p>Retrieves information for a specified session.</p>

        Args:
            assistant_id: <p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_session_response.GetSessionResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_session

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.get_session_request.GetSessionRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_knowledge_base(
        self,
        name: "capo_wisdom.types.name.Name",
        knowledge_base_type: "capo_wisdom.types.knowledge_base_type.KnowledgeBaseType",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        client_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        source_configuration: Optional[
            "capo_wisdom.types.source_configuration.SourceConfiguration"
        ] = None,
        rendering_configuration: Optional[
            "capo_wisdom.types.rendering_configuration.RenderingConfiguration"
        ] = None,
        server_side_encryption_configuration: Optional[
            "capo_wisdom.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        description: Optional["capo_wisdom.types.description.Description"] = None,
        tags: Optional["capo_wisdom.types.tags.Tags"] = None,
    ) -> "capo_wisdom.types.create_knowledge_base_response.CreateKnowledgeBaseResponse":
        """<p>Creates a knowledge base.</p> <note> <p>When using this API, you cannot reuse <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html">Amazon AppIntegrations</a> DataIntegrations with external knowledge bases such as Salesforce and ServiceNow. If you do, you'll get an <code>InvalidRequestException</code> error. </p> <p>For example, you're programmatically managing your external knowledge base, and you want to add or remove one of the fields that is being ingested from Salesforce. Do the following:</p> <ol> <li> <p>Call <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteKnowledgeBase.html">DeleteKnowledgeBase</a>.</p> </li> <li> <p>Call <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html">DeleteDataIntegration</a>.</p> </li> <li> <p>Call <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> to recreate the DataIntegration or a create different one.</p> </li> <li> <p>Call CreateKnowledgeBase.</p> </li> </ol> </note>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the knowledge base.</p>
            knowledge_base_type: <p>The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically. </p>
            source_configuration: <p>The source of the knowledge base content. Only set this argument for EXTERNAL knowledge bases.</p>
            rendering_configuration: <p>Information about how to render the content.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, and <code>kms:Decrypt/kms:GenerateDataKey</code> permissions to the IAM identity using the key to invoke Wisdom.</p> <p>For more information about setting up a customer managed key for Wisdom, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html">Enable Amazon Connect Wisdom for your instance</a>.</p>
            description: <p>The description.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.create_knowledge_base_request.CreateKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.create_knowledge_base_response.CreateKnowledgeBaseResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.create_knowledge_base

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.create_knowledge_base.async_create_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.create_knowledge_base_request.CreateKnowledgeBaseRequest = {
            "name": name,
            "knowledge_base_type": knowledge_base_type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if rendering_configuration is not None:
            input_["rendering_configuration"] = rendering_configuration
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_knowledge_base(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.get_knowledge_base_response.GetKnowledgeBaseResponse":
        """<p>Retrieves information about the knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_knowledge_base_request.GetKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_knowledge_base_response.GetKnowledgeBaseResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_knowledge_base

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_knowledge_base.async_get_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.get_knowledge_base_request.GetKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_knowledge_base(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse":
        """<p>Deletes the knowledge base.</p> <note> <p>When you use this API to delete an external knowledge base such as Salesforce or ServiceNow, you must also delete the <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html">Amazon AppIntegrations</a> DataIntegration. This is because you can't reuse the DataIntegration after it's been associated with an external knowledge base. However, you can delete and recreate it. See <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html">DeleteDataIntegration</a> and <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> in the <i>Amazon AppIntegrations API Reference</i>.</p> </note>

        Args:
            knowledge_base_id: <p>The knowledge base to delete content from. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.delete_knowledge_base

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.delete_knowledge_base.async_delete_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_knowledge_bases(
        self,
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.list_knowledge_bases_response.ListKnowledgeBasesResponse":
        """<p>Lists the knowledge bases.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.list_knowledge_bases_request.ListKnowledgeBasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.list_knowledge_bases_response.ListKnowledgeBasesResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.list_knowledge_bases

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.list_knowledge_bases.async_list_knowledge_bases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.list_knowledge_bases_request.ListKnowledgeBasesRequest = {}
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

    async def iter_list_knowledge_bases(
        self,
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_wisdom.types.knowledge_base_summary.KnowledgeBaseSummary]":
        _token = next_token
        while True:
            _response = await self.list_knowledge_bases(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("knowledge_base_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def delete_import_job(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        import_job_id: "capo_wisdom.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.delete_import_job_response.DeleteImportJobResponse":
        """<p>Deletes the quick response import job.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>
            import_job_id: <p>The identifier of the import job to be deleted.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.delete_import_job_request.DeleteImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.delete_import_job_response.DeleteImportJobResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.delete_import_job

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.delete_import_job.async_delete_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.delete_import_job_request.DeleteImportJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "import_job_id": import_job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_import_job(
        self,
        import_job_id: "capo_wisdom.types.uuid.Uuid",
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.get_import_job_response.GetImportJobResponse":
        """<p>Retrieves the started import job.</p>

        Args:
            import_job_id: <p>The identifier of the import job to retrieve.</p>
            knowledge_base_id: <p>The identifier of the knowledge base that the import job belongs to.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_import_job_request.GetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_import_job_response.GetImportJobResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_import_job

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_import_job.async_get_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.get_import_job_request.GetImportJobRequest = {
            "import_job_id": import_job_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_import_jobs(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.list_import_jobs_response.ListImportJobsResponse":
        """<p>Lists information about import jobs.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.list_import_jobs_request.ListImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.list_import_jobs_response.ListImportJobsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.list_import_jobs

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.list_import_jobs.async_list_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.list_import_jobs_request.ListImportJobsRequest = {
            "knowledge_base_id": knowledge_base_id
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

    async def iter_list_import_jobs(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_wisdom.types.import_job_summary.ImportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_import_jobs(
                knowledge_base_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("import_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def remove_knowledge_base_template_uri(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.remove_knowledge_base_template_uri_response.RemoveKnowledgeBaseTemplateUriResponse":
        """<p>Removes a URI template from a knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.remove_knowledge_base_template_uri_request.RemoveKnowledgeBaseTemplateUriRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.remove_knowledge_base_template_uri_response.RemoveKnowledgeBaseTemplateUriResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.remove_knowledge_base_template_uri

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.remove_knowledge_base_template_uri.async_remove_knowledge_base_template_uri(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.remove_knowledge_base_template_uri_request.RemoveKnowledgeBaseTemplateUriRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_content(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_wisdom.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.search_content_response.SearchContentResponse":
        """<p>Searches for content in a specified knowledge base. Can be used to get a specific content resource by its name.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.search_content_request.SearchContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.search_content_response.SearchContentResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.search_content

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.search_content.async_search_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.search_content_request.SearchContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
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

    async def iter_search_content(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_wisdom.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_wisdom.types.content_summary.ContentSummary]":
        _token = next_token
        while True:
            _response = await self.search_content(
                knowledge_base_id,
                search_expression,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("content_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_quick_responses(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_wisdom.types.quick_response_search_expression.QuickResponseSearchExpression",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
        attributes: Optional[
            "capo_wisdom.types.contact_attributes.ContactAttributes"
        ] = None,
    ) -> (
        "capo_wisdom.types.search_quick_responses_response.SearchQuickResponsesResponse"
    ):
        """<p>Searches existing Wisdom quick responses in a Wisdom knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression for querying the quick response.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            attributes: <p>The <a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-attrib-list.html#user-defined-attributes">user-defined Amazon Connect contact attributes</a> to be resolved when search results are returned.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.search_quick_responses_request.SearchQuickResponsesRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.search_quick_responses_response.SearchQuickResponsesResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.search_quick_responses

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.search_quick_responses.async_search_quick_responses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.search_quick_responses_request.SearchQuickResponsesRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_quick_responses(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_wisdom.types.quick_response_search_expression.QuickResponseSearchExpression",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
        attributes: Optional[
            "capo_wisdom.types.contact_attributes.ContactAttributes"
        ] = None,
    ) -> "AsyncIterator[capo_wisdom.types.quick_response_search_result_data.QuickResponseSearchResultData]":
        _token = next_token
        while True:
            _response = await self.search_quick_responses(
                knowledge_base_id,
                search_expression,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                attributes=attributes,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_content_upload(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        content_type: "capo_wisdom.types.content_type.ContentType",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        presigned_url_time_to_live: Optional[
            "capo_wisdom.types.time_to_live.TimeToLive"
        ] = None,
    ) -> "capo_wisdom.types.start_content_upload_response.StartContentUploadResponse":
        """<p>Get a URL to upload content to a knowledge base. To upload content, first make a PUT request to the returned URL with your file, making sure to include the required headers. Then use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_CreateContent.html">CreateContent</a> to finalize the content creation process or <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_UpdateContent.html">UpdateContent</a> to modify an existing resource. You can only upload content to a knowledge base of type CUSTOM.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            content_type: <p>The type of content to upload.</p>
            presigned_url_time_to_live: <p>The expected expiration time of the generated presigned URL, specified in minutes.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.start_content_upload_request.StartContentUploadRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.start_content_upload_response.StartContentUploadResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.start_content_upload

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.start_content_upload.async_start_content_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.start_content_upload_request.StartContentUploadRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_type": content_type,
        }
        if presigned_url_time_to_live is not None:
            input_["presigned_url_time_to_live"] = presigned_url_time_to_live

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_import_job(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        import_job_type: "capo_wisdom.types.import_job_type.ImportJobType",
        upload_id: "capo_wisdom.types.upload_id.UploadId",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        client_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        metadata: Optional["capo_wisdom.types.content_metadata.ContentMetadata"] = None,
        external_source_configuration: Optional[
            "capo_wisdom.types.external_source_configuration.ExternalSourceConfiguration"
        ] = None,
    ) -> "capo_wisdom.types.start_import_job_response.StartImportJobResponse":
        """<p>Start an asynchronous job to import Wisdom resources from an uploaded source file. Before calling this API, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a> to upload an asset that contains the resource data.</p> <ul> <li> <p>For importing Wisdom quick responses, you need to upload a csv file including the quick responses. For information about how to format the csv file for importing quick responses, see <a href="https://docs.aws.amazon.com/console/connect/quick-responses/add-data">Import quick responses</a>.</p> </li> </ul>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p> <ul> <li> <p>For importing Wisdom quick responses, this should be a <code>QUICK_RESPONSES</code> type knowledge base.</p> </li> </ul>
            import_job_type: <p>The type of the import job.</p> <ul> <li> <p>For importing quick response resource, set the value to <code>QUICK_RESPONSES</code>.</p> </li> </ul>
            upload_id: <p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>.</p>
            client_token: <p>The tags used to organize, track, or control access for this resource.</p>
            metadata: <p>The metadata fields of the imported Wisdom resources.</p>
            external_source_configuration: <p>The configuration information of the external source that the resource data are imported from.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.start_import_job_request.StartImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.start_import_job_response.StartImportJobResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.start_import_job

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.start_import_job.async_start_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.start_import_job_request.StartImportJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "import_job_type": import_job_type,
            "upload_id": upload_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if metadata is not None:
            input_["metadata"] = metadata
        if external_source_configuration is not None:
            input_["external_source_configuration"] = external_source_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_knowledge_base_template_uri(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        template_uri: "capo_wisdom.types.uri.Uri",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.update_knowledge_base_template_uri_response.UpdateKnowledgeBaseTemplateUriResponse":
        """<p>Updates the template URI of a knowledge base. This is only supported for knowledge bases of type EXTERNAL. Include a single variable in <code>${variable}</code> format; this interpolated by Wisdom using ingested content. For example, if you ingest a Salesforce article, it has an <code>Id</code> value, and you can set the template URI to <code>https://myInstanceName.lightning.force.com/lightning/r/Knowledge__kav/*${Id}*/view</code>. </p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            template_uri: <p>The template URI to update.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.update_knowledge_base_template_uri_request.UpdateKnowledgeBaseTemplateUriRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.update_knowledge_base_template_uri_response.UpdateKnowledgeBaseTemplateUriResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.update_knowledge_base_template_uri

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.update_knowledge_base_template_uri.async_update_knowledge_base_template_uri(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.update_knowledge_base_template_uri_request.UpdateKnowledgeBaseTemplateUriRequest = {
            "knowledge_base_id": knowledge_base_id,
            "template_uri": template_uri,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_content(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        name: "capo_wisdom.types.name.Name",
        upload_id: "capo_wisdom.types.upload_id.UploadId",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        title: Optional["capo_wisdom.types.content_title.ContentTitle"] = None,
        override_link_out_uri: Optional["capo_wisdom.types.uri.Uri"] = None,
        metadata: Optional["capo_wisdom.types.content_metadata.ContentMetadata"] = None,
        client_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_wisdom.types.tags.Tags"] = None,
    ) -> "capo_wisdom.types.create_content_response.CreateContentResponse":
        """<p>Creates Wisdom content. Before to calling this API, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a> to upload an asset.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            name: <p>The name of the content. Each piece of content in a knowledge base must have a unique name. You can retrieve a piece of content using only its knowledge base and its name with the <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_SearchContent.html">SearchContent</a> API.</p>
            title: <p>The title of the content. If not set, the title is equal to the name.</p>
            override_link_out_uri: <p>The URI you want to use for the article. If the knowledge base has a templateUri, setting this argument overrides it for this piece of content.</p>
            metadata: <p>A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Wisdom, you can store an external version identifier as metadata to utilize for determining drift.</p>
            upload_id: <p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.create_content_request.CreateContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.create_content_response.CreateContentResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.create_content

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.create_content.async_create_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.create_content_request.CreateContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "name": name,
            "upload_id": upload_id,
        }
        if title is not None:
            input_["title"] = title
        if override_link_out_uri is not None:
            input_["override_link_out_uri"] = override_link_out_uri
        if metadata is not None:
            input_["metadata"] = metadata
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_content(
        self,
        content_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.get_content_response.GetContentResponse":
        """<p>Retrieves content, including a pre-signed URL to download the content.</p>

        Args:
            content_id: <p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_content_request.GetContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_content_response.GetContentResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_content

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_content.async_get_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.get_content_request.GetContentRequest = {
            "content_id": content_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_content(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        content_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        revision_id: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        title: Optional["capo_wisdom.types.content_title.ContentTitle"] = None,
        override_link_out_uri: Optional["capo_wisdom.types.uri.Uri"] = None,
        remove_override_link_out_uri: Optional[bool] = None,
        metadata: Optional["capo_wisdom.types.content_metadata.ContentMetadata"] = None,
        upload_id: Optional["capo_wisdom.types.upload_id.UploadId"] = None,
    ) -> "capo_wisdom.types.update_content_response.UpdateContentResponse":
        """<p>Updates information about the content.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN</p>
            content_id: <p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            revision_id: <p>The <code>revisionId</code> of the content resource to update, taken from an earlier call to <code>GetContent</code>, <code>GetContentSummary</code>, <code>SearchContent</code>, or <code>ListContents</code>. If included, this argument acts as an optimistic lock to ensure content was not modified since it was last read. If it has been modified, this API throws a <code>PreconditionFailedException</code>.</p>
            title: <p>The title of the content.</p>
            override_link_out_uri: <p>The URI for the article. If the knowledge base has a templateUri, setting this argument overrides it for this piece of content. To remove an existing <code>overrideLinkOurUri</code>, exclude this argument and set <code>removeOverrideLinkOutUri</code> to true.</p>
            remove_override_link_out_uri: <p>Unset the existing <code>overrideLinkOutUri</code> if it exists.</p>
            metadata: <p>A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Wisdom, you can store an external version identifier as metadata to utilize for determining drift.</p>
            upload_id: <p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>. </p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.precondition_failed_exception.PreconditionFailedException: <p>The provided <code>revisionId</code> does not match, indicating the content has been modified since it was last read.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.update_content_request.UpdateContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.update_content_response.UpdateContentResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.update_content

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.update_content.async_update_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.update_content_request.UpdateContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_id": content_id,
        }
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if title is not None:
            input_["title"] = title
        if override_link_out_uri is not None:
            input_["override_link_out_uri"] = override_link_out_uri
        if remove_override_link_out_uri is not None:
            input_["remove_override_link_out_uri"] = remove_override_link_out_uri
        if metadata is not None:
            input_["metadata"] = metadata
        if upload_id is not None:
            input_["upload_id"] = upload_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_content(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        content_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.delete_content_response.DeleteContentResponse":
        """<p>Deletes the content.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            content_id: <p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.delete_content_request.DeleteContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.delete_content_response.DeleteContentResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.delete_content

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.delete_content.async_delete_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.delete_content_request.DeleteContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_id": content_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_contents(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.list_contents_response.ListContentsResponse":
        """<p>Lists the content.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.list_contents_request.ListContentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.list_contents_response.ListContentsResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.list_contents

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.list_contents.async_list_contents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.list_contents_request.ListContentsRequest = {
            "knowledge_base_id": knowledge_base_id
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

    async def iter_list_contents(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional["capo_wisdom.types.next_token.NextToken"] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_wisdom.types.content_summary.ContentSummary]":
        _token = next_token
        while True:
            _response = await self.list_contents(
                knowledge_base_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("content_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_content_summary(
        self,
        content_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.get_content_summary_response.GetContentSummaryResponse":
        """<p>Retrieves summary information about the content.</p>

        Args:
            content_id: <p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_content_summary_request.GetContentSummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_content_summary_response.GetContentSummaryResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_content_summary

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_content_summary.async_get_content_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.get_content_summary_request.GetContentSummaryRequest = {
            "content_id": content_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_quick_response(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        name: "capo_wisdom.types.quick_response_name.QuickResponseName",
        content: "capo_wisdom.types.quick_response_data_provider.QuickResponseDataProvider",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        content_type: Optional[
            "capo_wisdom.types.quick_response_type.QuickResponseType"
        ] = None,
        grouping_configuration: Optional[
            "capo_wisdom.types.grouping_configuration.GroupingConfiguration"
        ] = None,
        description: Optional[
            "capo_wisdom.types.quick_response_description.QuickResponseDescription"
        ] = None,
        shortcut_key: Optional["capo_wisdom.types.short_cut_key.ShortCutKey"] = None,
        is_active: Optional[bool] = None,
        channels: Optional["capo_wisdom.types.channels.Channels"] = None,
        language: Optional["capo_wisdom.types.language_code.LanguageCode"] = None,
        client_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_wisdom.types.tags.Tags"] = None,
    ) -> "capo_wisdom.types.create_quick_response_response.CreateQuickResponseResponse":
        """<p>Creates a Wisdom quick response.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            name: <p>The name of the quick response.</p>
            content: <p>The content of the quick response.</p>
            content_type: <p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for a quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for a quick response written in richtext.</p> </li> </ul>
            grouping_configuration: <p>The configuration information of the user groups that the quick response is accessible to.</p>
            description: <p>The description of the quick response.</p>
            shortcut_key: <p>The shortcut key of the quick response. The value should be unique across the knowledge base. </p>
            is_active: <p>Whether the quick response is active.</p>
            channels: <p>The Amazon Connect channels this quick response applies to.</p>
            language: <p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.create_quick_response_request.CreateQuickResponseRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.create_quick_response_response.CreateQuickResponseResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.create_quick_response

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.create_quick_response.async_create_quick_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.create_quick_response_request.CreateQuickResponseRequest = {
            "knowledge_base_id": knowledge_base_id,
            "name": name,
            "content": content,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if grouping_configuration is not None:
            input_["grouping_configuration"] = grouping_configuration
        if description is not None:
            input_["description"] = description
        if shortcut_key is not None:
            input_["shortcut_key"] = shortcut_key
        if is_active is not None:
            input_["is_active"] = is_active
        if channels is not None:
            input_["channels"] = channels
        if language is not None:
            input_["language"] = language
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_quick_response(
        self,
        quick_response_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.get_quick_response_response.GetQuickResponseResponse":
        """<p>Retrieves the quick response.</p>

        Args:
            quick_response_id: <p>The identifier of the quick response.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should be a QUICK_RESPONSES type knowledge base.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.get_quick_response_request.GetQuickResponseRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.get_quick_response_response.GetQuickResponseResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.get_quick_response

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.get_quick_response.async_get_quick_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.get_quick_response_request.GetQuickResponseRequest = {
            "quick_response_id": quick_response_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_quick_response(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        quick_response_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        name: Optional[
            "capo_wisdom.types.quick_response_name.QuickResponseName"
        ] = None,
        content: Optional[
            "capo_wisdom.types.quick_response_data_provider.QuickResponseDataProvider"
        ] = None,
        content_type: Optional[
            "capo_wisdom.types.quick_response_type.QuickResponseType"
        ] = None,
        grouping_configuration: Optional[
            "capo_wisdom.types.grouping_configuration.GroupingConfiguration"
        ] = None,
        remove_grouping_configuration: Optional[bool] = None,
        description: Optional[
            "capo_wisdom.types.quick_response_description.QuickResponseDescription"
        ] = None,
        remove_description: Optional[bool] = None,
        shortcut_key: Optional["capo_wisdom.types.short_cut_key.ShortCutKey"] = None,
        remove_shortcut_key: Optional[bool] = None,
        is_active: Optional[bool] = None,
        channels: Optional["capo_wisdom.types.channels.Channels"] = None,
        language: Optional["capo_wisdom.types.language_code.LanguageCode"] = None,
    ) -> "capo_wisdom.types.update_quick_response_response.UpdateQuickResponseResponse":
        """<p>Updates an existing Wisdom quick response.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            quick_response_id: <p>The identifier of the quick response.</p>
            name: <p>The name of the quick response.</p>
            content: <p>The updated content of the quick response.</p>
            content_type: <p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for quick response written in richtext.</p> </li> </ul>
            grouping_configuration: <p>The updated grouping configuration of the quick response.</p>
            remove_grouping_configuration: <p>Whether to remove the grouping configuration of the quick response.</p>
            description: <p>The updated description of the quick response.</p>
            remove_description: <p>Whether to remove the description from the quick response.</p>
            shortcut_key: <p>The shortcut key of the quick response. The value should be unique across the knowledge base.</p>
            remove_shortcut_key: <p>Whether to remove the shortcut key of the quick response.</p>
            is_active: <p>Whether the quick response is active. </p>
            channels: <p>The Amazon Connect contact channels this quick response applies to. The supported contact channel types include <code>Chat</code>.</p>
            language: <p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_wisdom.errors.precondition_failed_exception.PreconditionFailedException: <p>The provided <code>revisionId</code> does not match, indicating the content has been modified since it was last read.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.update_quick_response_request.UpdateQuickResponseRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.update_quick_response_response.UpdateQuickResponseResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.update_quick_response

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.update_quick_response.async_update_quick_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.update_quick_response_request.UpdateQuickResponseRequest = {
            "knowledge_base_id": knowledge_base_id,
            "quick_response_id": quick_response_id,
        }
        if name is not None:
            input_["name"] = name
        if content is not None:
            input_["content"] = content
        if content_type is not None:
            input_["content_type"] = content_type
        if grouping_configuration is not None:
            input_["grouping_configuration"] = grouping_configuration
        if remove_grouping_configuration is not None:
            input_["remove_grouping_configuration"] = remove_grouping_configuration
        if description is not None:
            input_["description"] = description
        if remove_description is not None:
            input_["remove_description"] = remove_description
        if shortcut_key is not None:
            input_["shortcut_key"] = shortcut_key
        if remove_shortcut_key is not None:
            input_["remove_shortcut_key"] = remove_shortcut_key
        if is_active is not None:
            input_["is_active"] = is_active
        if channels is not None:
            input_["channels"] = channels
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_quick_response(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        quick_response_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
    ) -> "capo_wisdom.types.delete_quick_response_response.DeleteQuickResponseResponse":
        """<p>Deletes a quick response.</p>

        Args:
            knowledge_base_id: <p>The knowledge base from which the quick response is deleted. The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it.</p>
            quick_response_id: <p>The identifier of the quick response to delete.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.delete_quick_response_request.DeleteQuickResponseRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.delete_quick_response_response.DeleteQuickResponseResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.delete_quick_response

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.delete_quick_response.async_delete_quick_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.delete_quick_response_request.DeleteQuickResponseRequest = {
            "knowledge_base_id": knowledge_base_id,
            "quick_response_id": quick_response_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_quick_responses(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "capo_wisdom.types.list_quick_responses_response.ListQuickResponsesResponse":
        """<p>Lists information about quick response.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_wisdom.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_wisdom.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_wisdom.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_wisdom.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_wisdom.types.list_quick_responses_request.ListQuickResponsesRequest]",
        ) -> AsyncOperationResponse[
            "capo_wisdom.types.list_quick_responses_response.ListQuickResponsesResponse"
        ]:
            import capo_wisdom._operations.wisdom_service.list_quick_responses

            (
                output,
                http_response,
            ) = await capo_wisdom._operations.wisdom_service.list_quick_responses.async_list_quick_responses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_wisdom.types.list_quick_responses_request.ListQuickResponsesRequest = {
            "knowledge_base_id": knowledge_base_id
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

    async def iter_list_quick_responses(
        self,
        knowledge_base_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncWisdomClientConfig] = None,
        next_token: Optional[
            "capo_wisdom.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_wisdom.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_wisdom.types.quick_response_summary.QuickResponseSummary]":
        _token = next_token
        while True:
            _response = await self.list_quick_responses(
                knowledge_base_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("quick_response_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
