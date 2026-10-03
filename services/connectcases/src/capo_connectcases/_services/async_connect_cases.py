"""Generated from Smithy shape ``com.amazonaws.connectcases#AmazonConnectCases``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_connectcases._auth._signers
import capo_connectcases._auth._sigv4
from capo_connectcases._auth._identity import Credentials
from capo_connectcases._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_connectcases._auth._zapros_handler import AuthMiddleware
from capo_connectcases._pagination import resolve_path as _resolve_path
from capo_connectcases._resources.amazon_connect_cases.case import AsyncCase
from capo_connectcases._resources.amazon_connect_cases.case_rule import AsyncCaseRule
from capo_connectcases._resources.amazon_connect_cases.domain import AsyncDomain
from capo_connectcases._resources.amazon_connect_cases.field import AsyncField
from capo_connectcases._resources.amazon_connect_cases.layout import AsyncLayout
from capo_connectcases._resources.amazon_connect_cases.template import AsyncTemplate
from capo_connectcases._services._aws_config import aaws_config
from capo_connectcases._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_connectcases.types.arn
    import capo_connectcases.types.batch_get_case_rule_request
    import capo_connectcases.types.batch_get_case_rule_response
    import capo_connectcases.types.batch_get_field_identifier_list
    import capo_connectcases.types.batch_get_field_request
    import capo_connectcases.types.batch_get_field_response
    import capo_connectcases.types.batch_put_field_options_request
    import capo_connectcases.types.batch_put_field_options_response
    import capo_connectcases.types.case_filter
    import capo_connectcases.types.case_id
    import capo_connectcases.types.case_rule_description
    import capo_connectcases.types.case_rule_details
    import capo_connectcases.types.case_rule_id
    import capo_connectcases.types.case_rule_identifier_list
    import capo_connectcases.types.case_rule_name
    import capo_connectcases.types.case_rule_summary
    import capo_connectcases.types.contact_arn
    import capo_connectcases.types.create_case_request
    import capo_connectcases.types.create_case_response
    import capo_connectcases.types.create_case_rule_request
    import capo_connectcases.types.create_case_rule_response
    import capo_connectcases.types.create_domain_request
    import capo_connectcases.types.create_domain_response
    import capo_connectcases.types.create_field_request
    import capo_connectcases.types.create_field_response
    import capo_connectcases.types.create_layout_request
    import capo_connectcases.types.create_layout_response
    import capo_connectcases.types.create_related_item_request
    import capo_connectcases.types.create_related_item_response
    import capo_connectcases.types.create_template_request
    import capo_connectcases.types.create_template_response
    import capo_connectcases.types.delete_case_request
    import capo_connectcases.types.delete_case_response
    import capo_connectcases.types.delete_case_rule_request
    import capo_connectcases.types.delete_case_rule_response
    import capo_connectcases.types.delete_domain_request
    import capo_connectcases.types.delete_domain_response
    import capo_connectcases.types.delete_field_request
    import capo_connectcases.types.delete_field_response
    import capo_connectcases.types.delete_layout_request
    import capo_connectcases.types.delete_layout_response
    import capo_connectcases.types.delete_related_item_request
    import capo_connectcases.types.delete_related_item_response
    import capo_connectcases.types.delete_template_request
    import capo_connectcases.types.delete_template_response
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.domain_name
    import capo_connectcases.types.event_bridge_configuration
    import capo_connectcases.types.field_attributes
    import capo_connectcases.types.field_description
    import capo_connectcases.types.field_id
    import capo_connectcases.types.field_identifier_list
    import capo_connectcases.types.field_name
    import capo_connectcases.types.field_options_list
    import capo_connectcases.types.field_type
    import capo_connectcases.types.field_value_list
    import capo_connectcases.types.get_case_audit_events_request
    import capo_connectcases.types.get_case_audit_events_response
    import capo_connectcases.types.get_case_event_configuration_request
    import capo_connectcases.types.get_case_event_configuration_response
    import capo_connectcases.types.get_case_request
    import capo_connectcases.types.get_case_response
    import capo_connectcases.types.get_domain_request
    import capo_connectcases.types.get_domain_response
    import capo_connectcases.types.get_layout_request
    import capo_connectcases.types.get_layout_response
    import capo_connectcases.types.get_template_request
    import capo_connectcases.types.get_template_response
    import capo_connectcases.types.layout_configuration
    import capo_connectcases.types.layout_content
    import capo_connectcases.types.layout_id
    import capo_connectcases.types.layout_name
    import capo_connectcases.types.list_case_rules_request
    import capo_connectcases.types.list_case_rules_response
    import capo_connectcases.types.list_cases_for_contact_request
    import capo_connectcases.types.list_cases_for_contact_response
    import capo_connectcases.types.list_domains_request
    import capo_connectcases.types.list_domains_response
    import capo_connectcases.types.list_field_options_request
    import capo_connectcases.types.list_field_options_response
    import capo_connectcases.types.list_fields_request
    import capo_connectcases.types.list_fields_response
    import capo_connectcases.types.list_layouts_request
    import capo_connectcases.types.list_layouts_response
    import capo_connectcases.types.list_tags_for_resource_request
    import capo_connectcases.types.list_tags_for_resource_response
    import capo_connectcases.types.list_templates_request
    import capo_connectcases.types.list_templates_response
    import capo_connectcases.types.max_results
    import capo_connectcases.types.mutable_tags
    import capo_connectcases.types.next_token
    import capo_connectcases.types.put_case_event_configuration_request
    import capo_connectcases.types.put_case_event_configuration_response
    import capo_connectcases.types.related_item_filter_list
    import capo_connectcases.types.related_item_id
    import capo_connectcases.types.related_item_input_content
    import capo_connectcases.types.related_item_type
    import capo_connectcases.types.related_item_update_content
    import capo_connectcases.types.required_field_list
    import capo_connectcases.types.search_all_related_items_request
    import capo_connectcases.types.search_all_related_items_response
    import capo_connectcases.types.search_all_related_items_response_item
    import capo_connectcases.types.search_all_related_items_sort_list
    import capo_connectcases.types.search_cases_request
    import capo_connectcases.types.search_cases_response
    import capo_connectcases.types.search_cases_response_item
    import capo_connectcases.types.search_related_items_request
    import capo_connectcases.types.search_related_items_response
    import capo_connectcases.types.search_related_items_response_item
    import capo_connectcases.types.sort_list
    import capo_connectcases.types.tag_key_list
    import capo_connectcases.types.tag_propagation_configuration_list
    import capo_connectcases.types.tag_resource_request
    import capo_connectcases.types.tags
    import capo_connectcases.types.template_case_rule_list
    import capo_connectcases.types.template_description
    import capo_connectcases.types.template_id
    import capo_connectcases.types.template_name
    import capo_connectcases.types.template_status
    import capo_connectcases.types.template_status_filters
    import capo_connectcases.types.untag_resource_request
    import capo_connectcases.types.update_case_request
    import capo_connectcases.types.update_case_response
    import capo_connectcases.types.update_case_rule_request
    import capo_connectcases.types.update_case_rule_response
    import capo_connectcases.types.update_field_request
    import capo_connectcases.types.update_field_response
    import capo_connectcases.types.update_layout_request
    import capo_connectcases.types.update_layout_response
    import capo_connectcases.types.update_related_item_request
    import capo_connectcases.types.update_related_item_response
    import capo_connectcases.types.update_template_request
    import capo_connectcases.types.update_template_response
    import capo_connectcases.types.user_union
    import capo_connectcases.types.values_list


class AsyncConnectCasesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncConnectCasesClient:
    """A client for the ``ConnectCases`` service.

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
        self._config = AsyncConnectCasesClientConfig(
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
        self.case = AsyncCase(self)
        self.case_rule = AsyncCaseRule(self)
        self.domain = AsyncDomain(self)
        self.field = AsyncField(self)
        self.layout = AsyncLayout(self)
        self.template = AsyncTemplate(self)

    def operation_options(
        self, config_overrides: Optional[AsyncConnectCasesClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncConnectCasesClientConfig = config_overrides or {}
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
        arn: "capo_connectcases.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for a resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN)</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
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
        arn: "capo_connectcases.types.arn.Arn",
        tags: "capo_connectcases.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> None:
        """<p>Adds tags to a resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN)</p>
            tags: <p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcases._operations.amazon_connect_cases.tag_resource

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.tag_resource_request.TagResourceRequest = {
            "arn": arn,
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
        arn: "capo_connectcases.types.arn.Arn",
        tag_keys: "capo_connectcases.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> None:
        """<p>Untags a resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN)</p>
            tag_keys: <p>List of tag keys.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_connectcases._operations.amazon_connect_cases.untag_resource

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.untag_resource_request.UntagResourceRequest = {
            "arn": arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_case(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        fields: "capo_connectcases.types.field_value_list.FieldValueList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        client_token: Optional[str] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
        tags: Optional["capo_connectcases.types.mutable_tags.MutableTags"] = None,
    ) -> "capo_connectcases.types.create_case_response.CreateCaseResponse":
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the User ARN resource that you provide</p> </note> <p>Creates a case in the specified Cases domain. Case system and custom fields are taken as an array id/value pairs with a declared data types.</p> <p>When creating a case from a template that has tag propagation configurations, the specified tags are automatically applied to the case.</p> <p>The following fields are required when creating a case:</p> <ul> <li> <p> <code>customer_id</code> - You must provide the full customer profile ARN in this format: <code>arn:aws:profile:your_AWS_Region:your_AWS_account ID:domains/your_profiles_domain_name/profiles/profile_ID</code> </p> </li> <li> <p> <code>title</code> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier of a template.</p>
            fields: <p>An array of objects with field ID (matching ListFields/DescribeField) and value union data.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_case_request.CreateCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_case_response.CreateCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_case

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_case.async_create_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.create_case_request.CreateCaseRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
            "fields": fields,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if performed_by is not None:
            input_["performed_by"] = performed_by
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_case(
        self,
        case_id: "capo_connectcases.types.case_id.CaseId",
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        fields: "capo_connectcases.types.field_identifier_list.FieldIdentifierList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.get_case_response.GetCaseResponse":
        """<p>Returns information about a specific case if it exists. </p>

        Args:
            case_id: <p>A unique identifier of the case.</p>
            domain_id: <p>The unique identifier of the Cases domain. </p>
            fields: <p>A list of unique field identifiers. </p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_case_request.GetCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_case_response.GetCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_case

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_case.async_get_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.get_case_request.GetCaseRequest = {
            "case_id": case_id,
            "domain_id": domain_id,
            "fields": fields,
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

    async def iter_get_case(
        self,
        case_id: "capo_connectcases.types.case_id.CaseId",
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        fields: "capo_connectcases.types.field_identifier_list.FieldIdentifierList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_connectcases.types.get_case_response.GetCaseResponse]":
        _token = next_token
        while True:
            _response = await self.get_case(
                case_id,
                domain_id,
                fields,
                config_overrides=config_overrides,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_case(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        fields: "capo_connectcases.types.field_value_list.FieldValueList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
    ) -> "capo_connectcases.types.update_case_response.UpdateCaseResponse":
        """<note> <p>If you provide a value for <code>PerformedBy.UserArn</code> you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">connect:DescribeUser</a> permission on the User ARN resource that you provide</p> </note> <p>Updates the values of fields on a case. Fields to be updated are received as an array of id/value pairs identical to the <code>CreateCase</code> input .</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>A unique identifier of the case.</p>
            fields: <p>An array of objects with <code>fieldId</code> (matching ListFields/DescribeField) and value union data, structured identical to <code>CreateCase</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.update_case_request.UpdateCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.update_case_response.UpdateCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_case

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.update_case.async_update_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.update_case_request.UpdateCaseRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
            "fields": fields,
        }
        if performed_by is not None:
            input_["performed_by"] = performed_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_case(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_case_response.DeleteCaseResponse":
        """<p> The DeleteCase API permanently deletes a case and all its associated resources from the cases data store. After a successful deletion, you cannot:</p> <ul> <li> <p>Retrieve related items</p> </li> <li> <p>Access audit history</p> </li> <li> <p>Perform any operations that require the CaseID</p> </li> </ul> <important> <p>This action is irreversible. After you delete a case, you cannot recover its data.</p> </important>

        Args:
            domain_id: <p>A unique identifier of the Cases domain.</p>
            case_id: <p>A unique identifier of the case.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.delete_case_request.DeleteCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_case_response.DeleteCaseResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_case

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_case.async_delete_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_case_request.DeleteCaseRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_case_audit_events(
        self,
        case_id: "capo_connectcases.types.case_id.CaseId",
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse":
        """<p>Returns the audit history about a specific case if it exists.</p>

        Args:
            case_id: <p>A unique identifier of the case.</p>
            domain_id: <p>The unique identifier of the Cases domain.</p>
            max_results: <p>The maximum number of audit events to return. When no value is provided, 25 is the default.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_case_audit_events_request.GetCaseAuditEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_case_audit_events

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_case_audit_events.async_get_case_audit_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.get_case_audit_events_request.GetCaseAuditEventsRequest = {
            "case_id": case_id,
            "domain_id": domain_id,
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

    async def iter_get_case_audit_events(
        self,
        case_id: "capo_connectcases.types.case_id.CaseId",
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_connectcases.types.get_case_audit_events_response.GetCaseAuditEventsResponse]":
        _token = next_token
        while True:
            _response = await self.get_case_audit_events(
                case_id,
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_cases_for_contact(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        contact_arn: "capo_connectcases.types.contact_arn.ContactArn",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse":
        """<p>Lists cases for a given contact.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            contact_arn: <p>A unique identifier of a contact in Amazon Connect.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_cases_for_contact_request.ListCasesForContactRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_cases_for_contact

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_cases_for_contact.async_list_cases_for_contact(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.list_cases_for_contact_request.ListCasesForContactRequest = {
            "domain_id": domain_id,
            "contact_arn": contact_arn,
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

    async def iter_list_cases_for_contact(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        contact_arn: "capo_connectcases.types.contact_arn.ContactArn",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_connectcases.types.list_cases_for_contact_response.ListCasesForContactResponse]":
        _token = next_token
        while True:
            _response = await self.list_cases_for_contact(
                domain_id,
                contact_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_cases(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        search_term: Optional[str] = None,
        filter: Optional["capo_connectcases.types.case_filter.CaseFilter"] = None,
        sorts: Optional["capo_connectcases.types.sort_list.SortList"] = None,
        fields: Optional[
            "capo_connectcases.types.field_identifier_list.FieldIdentifierList"
        ] = None,
    ) -> "capo_connectcases.types.search_cases_response.SearchCasesResponse":
        """<p>Searches for cases within their associated Cases domain. Search results are returned as a paginated list of abridged case documents.</p> <note> <p>For <code>customer_id</code> you must provide the full customer profile ARN in this format: <code> arn:aws:profile:your AWS Region:your AWS account ID:domains/profiles domain name/profiles/profile ID</code>. </p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of cases to return. When no value is provided, 25 is the default.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            search_term: <p>A word or phrase used to perform a quick search.</p>
            filter: <p>A list of filter objects.</p>
            sorts: <p>A list of sorts where each sort specifies a field and their sort order to be applied to the results. </p>
            fields: <p>The list of field identifiers to be returned as part of the response.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.search_cases_request.SearchCasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.search_cases_response.SearchCasesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.search_cases

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.search_cases.async_search_cases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.search_cases_request.SearchCasesRequest = {
            "domain_id": domain_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if search_term is not None:
            input_["search_term"] = search_term
        if filter is not None:
            input_["filter"] = filter
        if sorts is not None:
            input_["sorts"] = sorts
        if fields is not None:
            input_["fields"] = fields

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_cases(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        search_term: Optional[str] = None,
        filter: Optional["capo_connectcases.types.case_filter.CaseFilter"] = None,
        sorts: Optional["capo_connectcases.types.sort_list.SortList"] = None,
        fields: Optional[
            "capo_connectcases.types.field_identifier_list.FieldIdentifierList"
        ] = None,
    ) -> "AsyncIterator[capo_connectcases.types.search_cases_response_item.SearchCasesResponseItem]":
        _token = next_token
        while True:
            _response = await self.search_cases(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                search_term=search_term,
                filter=filter,
                sorts=sorts,
                fields=fields,
            )
            _page = _resolve_path(_response, ("cases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_related_item(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        type: "capo_connectcases.types.related_item_type.RelatedItemType",
        content: "capo_connectcases.types.related_item_input_content.RelatedItemInputContent",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
    ) -> (
        "capo_connectcases.types.create_related_item_response.CreateRelatedItemResponse"
    ):
        """<p>Creates a related item (comments, tasks, and contacts) and associates it with a case.</p> <p>There's a quota for the number of fields allowed in a Custom type related item. See <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#cases-quotas">Amazon Connect Cases quotas</a>.</p> <p> <b>Use cases</b> </p> <p>Following are examples of related items that you may want to associate with a case:</p> <ul> <li> <p>Related contacts, such as calls, chats, emails tasks</p> </li> <li> <p>Comments, for agent notes</p> </li> <li> <p>SLAs, to capture target resolution goals</p> </li> <li> <p>Cases, to capture related Amazon Connect Cases</p> </li> <li> <p>Files, such as policy documentation or customer-provided attachments</p> </li> <li> <p>Custom related items, which provide flexibility for you to define related items that such as bookings, orders, products, notices, and more</p> </li> </ul> <p> <b>Important things to know</b> </p> <ul> <li> <p>If you are associating a contact to a case by passing in <code>Contact</code> for a <code>type</code>, you must have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html">DescribeContact</a> permission on the ARN of the contact that you provide in <code>content.contact.contactArn</code>.</p> </li> <li> <p>A Related Item is a resource that is associated with a case. It may or may not have an external identifier linking it to an external resource (for example, a <code>contactArn</code>). All Related Items have their own internal identifier, the <code>relatedItemArn</code>. Examples of related items include <code>comments</code> and <code>contacts</code>.</p> </li> <li> <p>If you provide a value for <code>performedBy.userArn</code> you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">DescribeUser</a> permission on the ARN of the user that you provide.</p> </li> <li> <p>The <code>type</code> field is reserved for internal use only.</p> </li> </ul> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Amazon Connect endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>A unique identifier of the case.</p>
            type: <p>The type of a related item.</p>
            content: <p>The content of a related item to be created.</p>
            performed_by: <p>Represents the creator of the related item.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_related_item_request.CreateRelatedItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_related_item_response.CreateRelatedItemResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_related_item

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_related_item.async_create_related_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.create_related_item_request.CreateRelatedItemRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
            "type": type,
            "content": content,
        }
        if performed_by is not None:
            input_["performed_by"] = performed_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_related_item(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        related_item_id: "capo_connectcases.types.related_item_id.RelatedItemId",
        content: "capo_connectcases.types.related_item_update_content.RelatedItemUpdateContent",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        performed_by: Optional["capo_connectcases.types.user_union.UserUnion"] = None,
    ) -> (
        "capo_connectcases.types.update_related_item_response.UpdateRelatedItemResponse"
    ):
        """<p>Updates the content of a related item associated with a case. The following related item types are supported:</p> <ul> <li> <p> <b>Comment</b> - Update the text content of an existing comment</p> </li> <li> <p> <b>Custom</b> - Update the fields of a custom related item. You can add, modify, and remove fields from a custom related item. There's a quota for the number of fields allowed in a Custom type related item. See <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#cases-quotas">Amazon Connect Cases quotas</a>.</p> </li> </ul> <p> <b>Important things to know</b> </p> <ul> <li> <p>When updating a Custom related item, all existing and new fields, and their associated values should be included in the request. Fields not included as part of this request will be removed.</p> </li> <li> <p>If you provide a value for <code>performedBy.userArn</code> you must also have <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html">DescribeUser</a> permission on the ARN of the user that you provide.</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html#system-case-fields">System case fields</a> cannot be used in a custom related item.</p> </li> </ul> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Amazon Connect endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>A unique identifier of the case.</p>
            related_item_id: <p>Unique identifier of a related item.</p>
            content: <p>The content of a related item to be updated.</p>
            performed_by: <p>Represents the user who performed the update of the related item.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.update_related_item_request.UpdateRelatedItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.update_related_item_response.UpdateRelatedItemResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_related_item

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.update_related_item.async_update_related_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.update_related_item_request.UpdateRelatedItemRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
            "related_item_id": related_item_id,
            "content": content,
        }
        if performed_by is not None:
            input_["performed_by"] = performed_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_related_item(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        related_item_id: "capo_connectcases.types.related_item_id.RelatedItemId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> (
        "capo_connectcases.types.delete_related_item_response.DeleteRelatedItemResponse"
    ):
        """<p>Deletes the related item resource under a case.</p> <note> <p>This API cannot be used on a FILE type related attachment. To delete this type of file, use the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteAttachedFile.html">DeleteAttachedFile</a> API</p> </note>

        Args:
            domain_id: <p>A unique identifier of the Cases domain.</p>
            case_id: <p>A unique identifier of the case.</p>
            related_item_id: <p>A unique identifier of a related item.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.delete_related_item_request.DeleteRelatedItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_related_item_response.DeleteRelatedItemResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_related_item

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_related_item.async_delete_related_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_related_item_request.DeleteRelatedItemRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
            "related_item_id": related_item_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_related_items(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_connectcases.types.related_item_filter_list.RelatedItemFilterList"
        ] = None,
    ) -> "capo_connectcases.types.search_related_items_response.SearchRelatedItemsResponse":
        """<p>Searches for related items that are associated with a case.</p> <note> <p>If no filters are provided, this returns all related items associated with a case.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            case_id: <p>A unique identifier of the case.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filters: <p>The list of types of related items and their parameters to use for filtering.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.search_related_items_request.SearchRelatedItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.search_related_items_response.SearchRelatedItemsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.search_related_items

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.search_related_items.async_search_related_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.search_related_items_request.SearchRelatedItemsRequest = {
            "domain_id": domain_id,
            "case_id": case_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_related_items(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_id: "capo_connectcases.types.case_id.CaseId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_connectcases.types.related_item_filter_list.RelatedItemFilterList"
        ] = None,
    ) -> "AsyncIterator[capo_connectcases.types.search_related_items_response_item.SearchRelatedItemsResponseItem]":
        _token = next_token
        while True:
            _response = await self.search_related_items(
                domain_id,
                case_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("related_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_case_rule(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        name: "capo_connectcases.types.case_rule_name.CaseRuleName",
        rule: "capo_connectcases.types.case_rule_details.CaseRuleDetails",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        description: Optional[
            "capo_connectcases.types.case_rule_description.CaseRuleDescription"
        ] = None,
    ) -> "capo_connectcases.types.create_case_rule_response.CreateCaseRuleResponse":
        """<p>Creates a new case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            name: <p>Name of the case rule.</p>
            description: <p>The description of a case rule.</p>
            rule: <p>Represents what rule type should take place, under what conditions.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_case_rule_request.CreateCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_case_rule_response.CreateCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_case_rule

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_case_rule.async_create_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.create_case_rule_request.CreateCaseRuleRequest = {
            "domain_id": domain_id,
            "name": name,
            "rule": rule,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_case_rule(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        name: Optional["capo_connectcases.types.case_rule_name.CaseRuleName"] = None,
        description: Optional[
            "capo_connectcases.types.case_rule_description.CaseRuleDescription"
        ] = None,
        rule: Optional[
            "capo_connectcases.types.case_rule_details.CaseRuleDetails"
        ] = None,
    ) -> "capo_connectcases.types.update_case_rule_response.UpdateCaseRuleResponse":
        """<p>Updates a case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rule_id: <p>Unique identifier of a case rule.</p>
            name: <p>Name of the case rule.</p>
            description: <p>Description of a case rule.</p>
            rule: <p>Represents what rule type should take place, under what conditions.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.update_case_rule_request.UpdateCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.update_case_rule_response.UpdateCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_case_rule

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.update_case_rule.async_update_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.update_case_rule_request.UpdateCaseRuleRequest = {
            "domain_id": domain_id,
            "case_rule_id": case_rule_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if rule is not None:
            input_["rule"] = rule

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_case_rule(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_rule_id: "capo_connectcases.types.case_rule_id.CaseRuleId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_case_rule_response.DeleteCaseRuleResponse":
        """<p>Deletes a case rule. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rule_id: <p>Unique identifier of a case rule.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.delete_case_rule_request.DeleteCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_case_rule_response.DeleteCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_case_rule

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_case_rule.async_delete_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_case_rule_request.DeleteCaseRuleRequest = {
            "domain_id": domain_id,
            "case_rule_id": case_rule_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_case_rules(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_case_rules_response.ListCaseRulesResponse":
        """<p>Lists all case rules in a Cases domain. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_case_rules_request.ListCaseRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_case_rules_response.ListCaseRulesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_case_rules

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_case_rules.async_list_case_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.list_case_rules_request.ListCaseRulesRequest = {
            "domain_id": domain_id
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

    async def iter_list_case_rules(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_connectcases.types.case_rule_summary.CaseRuleSummary]":
        _token = next_token
        while True:
            _response = await self.list_case_rules(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("case_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_get_case_rule(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        case_rules: "capo_connectcases.types.case_rule_identifier_list.CaseRuleIdentifierList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> (
        "capo_connectcases.types.batch_get_case_rule_response.BatchGetCaseRuleResponse"
    ):
        """<p>Gets a batch of case rules. In the Amazon Connect admin website, case rules are known as <i>case field conditions</i>. For more information about case field conditions, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">Add case field conditions to a case template</a>.</p>

        Args:
            domain_id: <p>Unique identifier of a Cases domain.</p>
            case_rules: <p>A list of case rule identifiers.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.batch_get_case_rule_request.BatchGetCaseRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.batch_get_case_rule_response.BatchGetCaseRuleResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_get_case_rule

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.batch_get_case_rule.async_batch_get_case_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.batch_get_case_rule_request.BatchGetCaseRuleRequest = {
            "domain_id": domain_id,
            "case_rules": case_rules,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_domain(
        self,
        name: "capo_connectcases.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a domain, which is a container for all case data, such as cases, fields, templates and layouts. Each Amazon Connect instance can be associated with only one Cases domain.</p> <important> <p>This will not associate your connect instance to Cases domain. Instead, use the Amazon Connect <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html">CreateIntegrationAssociation</a> API. You need specific IAM permissions to successfully associate the Cases domain. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/required-permissions-iam-cases.html#onboard-cases-iam">Onboard to Cases</a>.</p> </important>

        Args:
            name: <p>The name for your Cases domain. It must be unique for your Amazon Web Services account.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_domain_request.CreateDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_domain_response.CreateDomainResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_domain

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.create_domain_request.CreateDomainRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_domain_response.GetDomainResponse":
        """<p>Returns information about a specific domain if it exists. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_domain_request.GetDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_domain_response.GetDomainResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_domain

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_domain.async_get_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.get_domain_request.GetDomainRequest = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_domain(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_domain_response.DeleteDomainResponse":
        """<p>Deletes a Cases domain.</p> <note> <p>After deleting your domain you must disassociate the deleted domain from your Amazon Connect instance with another API call before being able to use Cases again with this Amazon Connect instance. See <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteIntegrationAssociation.html">DeleteIntegrationAssociation</a>.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.delete_domain_request.DeleteDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_domain

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_domain_request.DeleteDomainRequest = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_domains(
        self,
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_domains_response.ListDomainsResponse":
        """<p>Lists all cases domains in the Amazon Web Services account. Each list item is a condensed summary object of the domain.</p>

        Args:
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_domains_request.ListDomainsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_domains_response.ListDomainsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_domains

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.list_domains_request.ListDomainsRequest = {}
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

    async def iter_list_domains(
        self,
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_connectcases.types.list_domains_response.ListDomainsResponse]":
        _token = next_token
        while True:
            _response = await self.list_domains(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_case_event_configuration(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_case_event_configuration_response.GetCaseEventConfigurationResponse":
        """<p>Returns the case event publishing configuration.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_case_event_configuration_request.GetCaseEventConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_case_event_configuration_response.GetCaseEventConfigurationResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_case_event_configuration

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_case_event_configuration.async_get_case_event_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.get_case_event_configuration_request.GetCaseEventConfigurationRequest = {
            "domain_id": domain_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_case_event_configuration(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        event_bridge: "capo_connectcases.types.event_bridge_configuration.EventBridgeConfiguration",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.put_case_event_configuration_response.PutCaseEventConfigurationResponse":
        """<p>Adds case event publishing configuration. For a complete list of fields you can add to the event message, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html">Create case fields</a> in the <i>Amazon Connect Administrator Guide</i> </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            event_bridge: <p>Configuration to enable EventBridge case event delivery and determine what data is delivered.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.put_case_event_configuration_request.PutCaseEventConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.put_case_event_configuration_response.PutCaseEventConfigurationResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.put_case_event_configuration

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.put_case_event_configuration.async_put_case_event_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.put_case_event_configuration_request.PutCaseEventConfigurationRequest = {
            "domain_id": domain_id,
            "event_bridge": event_bridge,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_all_related_items(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_connectcases.types.related_item_filter_list.RelatedItemFilterList"
        ] = None,
        sorts: Optional[
            "capo_connectcases.types.search_all_related_items_sort_list.SearchAllRelatedItemsSortList"
        ] = None,
    ) -> "capo_connectcases.types.search_all_related_items_response.SearchAllRelatedItemsResponse":
        """<p>Searches for related items across all cases within a domain. This is a global search operation that returns related items from multiple cases, unlike the case-specific <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchRelatedItems.html">SearchRelatedItems</a> API.</p> <p> <b>Use cases</b> </p> <p>Following are common uses cases for this API:</p> <ul> <li> <p>Find cases with similar issues across the domain. For example, search for all cases containing comments about "product defect" to identify patterns and existing solutions.</p> </li> <li> <p>Locate all cases associated with specific contacts or orders. For example, find all cases linked to a contactArn to understand the complete customer journey. </p> </li> <li> <p>Monitor SLA compliance across cases. For example, search for all cases with "Active" SLA status to prioritize remediation efforts.</p> </li> </ul> <p> <b>Important things to know</b> </p> <ul> <li> <p>This API returns case identifiers, not complete case objects. To retrieve full case details, you must make additional calls to the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCase.html">GetCase</a> API for each returned case ID. </p> </li> <li> <p>This API searches across related items content, not case fields. Use the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_SearchCases.html">SearchCases</a> API to search within case field values.</p> </li> </ul> <p> <b>Endpoints</b>: See <a href="https://docs.aws.amazon.com/general/latest/gr/connect_region.html">Amazon Connect endpoints and quotas</a>.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filters: <p>The list of types of related items and their parameters to use for filtering. The filters work as an OR condition: caller gets back related items that match any of the specified filter types.</p>
            sorts: <p>A structured set of sort terms to specify the order in which related items should be returned. Supports sorting by association time or case ID. The sorts work in the order specified: first sort term takes precedence over subsequent terms.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.search_all_related_items_request.SearchAllRelatedItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.search_all_related_items_response.SearchAllRelatedItemsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.search_all_related_items

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.search_all_related_items.async_search_all_related_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.search_all_related_items_request.SearchAllRelatedItemsRequest = {
            "domain_id": domain_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters
        if sorts is not None:
            input_["sorts"] = sorts

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_all_related_items(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_connectcases.types.related_item_filter_list.RelatedItemFilterList"
        ] = None,
        sorts: Optional[
            "capo_connectcases.types.search_all_related_items_sort_list.SearchAllRelatedItemsSortList"
        ] = None,
    ) -> "AsyncIterator[capo_connectcases.types.search_all_related_items_response_item.SearchAllRelatedItemsResponseItem]":
        _token = next_token
        while True:
            _response = await self.search_all_related_items(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
                sorts=sorts,
            )
            _page = _resolve_path(_response, ("related_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_field(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        name: "capo_connectcases.types.field_name.FieldName",
        type: "capo_connectcases.types.field_type.FieldType",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        description: Optional[
            "capo_connectcases.types.field_description.FieldDescription"
        ] = None,
        attributes: Optional[
            "capo_connectcases.types.field_attributes.FieldAttributes"
        ] = None,
    ) -> "capo_connectcases.types.create_field_response.CreateFieldResponse":
        """<p>Creates a field in the Cases domain. This field is used to define the case object model (that is, defines what data can be captured on cases) in a Cases domain. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            name: <p>The name of the field.</p>
            type: <p>Defines the data type, some system constraints, and default display of the field.</p>
            description: <p>The description of the field.</p>
            attributes: <p>Union of field attributes.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_field_request.CreateFieldRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_field_response.CreateFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_field

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_field.async_create_field(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.create_field_request.CreateFieldRequest = {
            "domain_id": domain_id,
            "name": name,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_field(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        field_id: "capo_connectcases.types.field_id.FieldId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        name: Optional["capo_connectcases.types.field_name.FieldName"] = None,
        description: Optional[
            "capo_connectcases.types.field_description.FieldDescription"
        ] = None,
        attributes: Optional[
            "capo_connectcases.types.field_attributes.FieldAttributes"
        ] = None,
    ) -> "capo_connectcases.types.update_field_response.UpdateFieldResponse":
        """<p>Updates the properties of an existing field. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            field_id: <p>The unique identifier of a field.</p>
            name: <p>The name of the field.</p>
            description: <p>The description of a field.</p>
            attributes: <p>Union of field attributes.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.update_field_request.UpdateFieldRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.update_field_response.UpdateFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_field

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.update_field.async_update_field(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.update_field_request.UpdateFieldRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_field(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        field_id: "capo_connectcases.types.field_id.FieldId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_field_response.DeleteFieldResponse":
        """<p>Deletes a field from a cases template.</p> <p>After a field is deleted:</p> <ul> <li> <p>You can still retrieve the field by calling <code>BatchGetField</code>.</p> </li> <li> <p>You cannot update a deleted field by calling <code>UpdateField</code>; it throws a <code>ValidationException</code>.</p> </li> <li> <p>Deleted fields are not included in the <code>ListFields</code> response.</p> </li> <li> <p>Calling <code>CreateCase</code> with a deleted field throws a <code>ValidationException</code> denoting which field identifiers in the request have been deleted.</p> </li> <li> <p>Calling <code>GetCase</code> with a deleted field identifier returns the deleted field's value if one exists.</p> </li> <li> <p>Calling <code>UpdateCase</code> with a deleted field ID throws a <code>ValidationException</code> if the case does not already contain a value for the deleted field. Otherwise it succeeds, allowing you to update or remove (using <code>emptyValue: {}</code>) the field's value from the case.</p> </li> <li> <p> <code>GetTemplate</code> does not return field IDs for deleted fields.</p> </li> <li> <p> <code>GetLayout</code> does not return field IDs for deleted fields.</p> </li> <li> <p>Calling <code>SearchCases</code> with the deleted field ID as a filter returns any cases that have a value for the deleted field that matches the filter criteria.</p> </li> <li> <p>Calling <code>SearchCases</code> with a <code>searchTerm</code> value that matches a deleted field's value on a case returns the case in the response.</p> </li> <li> <p>Calling <code>BatchPutFieldOptions</code> with a deleted field ID throw a <code>ValidationException</code>.</p> </li> <li> <p>Calling <code>GetCaseEventConfiguration</code> does not return field IDs for deleted fields.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain.</p>
            field_id: <p>Unique identifier of the field.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.delete_field_request.DeleteFieldRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_field_response.DeleteFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_field

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_field.async_delete_field(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_field_request.DeleteFieldRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_fields(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_fields_response.ListFieldsResponse":
        """<p>Lists all fields in a Cases domain.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_fields_request.ListFieldsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_fields_response.ListFieldsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_fields

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_fields.async_list_fields(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.list_fields_request.ListFieldsRequest = {
            "domain_id": domain_id
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

    async def iter_list_fields(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> (
        "AsyncIterator[capo_connectcases.types.list_fields_response.ListFieldsResponse]"
    ):
        _token = next_token
        while True:
            _response = await self.list_fields(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_put_field_options(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        field_id: "capo_connectcases.types.field_id.FieldId",
        options: "capo_connectcases.types.field_options_list.FieldOptionsList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.batch_put_field_options_response.BatchPutFieldOptionsResponse":
        """<p>Creates and updates a set of field options for a single select field in a Cases domain.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            field_id: <p>The unique identifier of a field.</p>
            options: <p>A list of <code>FieldOption</code> objects.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.batch_put_field_options_request.BatchPutFieldOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.batch_put_field_options_response.BatchPutFieldOptionsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_put_field_options

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.batch_put_field_options.async_batch_put_field_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.batch_put_field_options_request.BatchPutFieldOptionsRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
            "options": options,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_field_options(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        field_id: "capo_connectcases.types.field_id.FieldId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        values: Optional["capo_connectcases.types.values_list.ValuesList"] = None,
    ) -> "capo_connectcases.types.list_field_options_response.ListFieldOptionsResponse":
        """<p>Lists all of the field options for a field identifier in the domain. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            field_id: <p>The unique identifier of a field.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            values: <p>A list of <code>FieldOption</code> values to filter on for <code>ListFieldOptions</code>.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_field_options_request.ListFieldOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_field_options_response.ListFieldOptionsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_field_options

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_field_options.async_list_field_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.list_field_options_request.ListFieldOptionsRequest = {
            "domain_id": domain_id,
            "field_id": field_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if values is not None:
            input_["values"] = values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_field_options(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        field_id: "capo_connectcases.types.field_id.FieldId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        values: Optional["capo_connectcases.types.values_list.ValuesList"] = None,
    ) -> "AsyncIterator[capo_connectcases.types.list_field_options_response.ListFieldOptionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_field_options(
                domain_id,
                field_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                values=values,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_get_field(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        fields: "capo_connectcases.types.batch_get_field_identifier_list.BatchGetFieldIdentifierList",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.batch_get_field_response.BatchGetFieldResponse":
        """<p>Returns the description for the list of fields in the request parameters. </p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            fields: <p>A list of unique field identifiers. </p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.batch_get_field_request.BatchGetFieldRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.batch_get_field_response.BatchGetFieldResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.batch_get_field

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.batch_get_field.async_batch_get_field(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.batch_get_field_request.BatchGetFieldRequest = {
            "domain_id": domain_id,
            "fields": fields,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_layout(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        name: "capo_connectcases.types.layout_name.LayoutName",
        content: "capo_connectcases.types.layout_content.LayoutContent",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.create_layout_response.CreateLayoutResponse":
        """<p>Creates a layout in the Cases domain. Layouts define the following configuration in the top section and More Info tab of the Cases user interface:</p> <ul> <li> <p>Fields to display to the users</p> </li> <li> <p>Field ordering</p> </li> </ul> <note> <p>Title and Status fields cannot be part of layouts since they are not configurable.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            name: <p>The name of the layout. It must be unique for the Cases domain.</p>
            content: <p>Information about which fields will be present in the layout, and information about the order of the fields.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_layout_request.CreateLayoutRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_layout_response.CreateLayoutResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_layout

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_layout.async_create_layout(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.create_layout_request.CreateLayoutRequest = {
            "domain_id": domain_id,
            "name": name,
            "content": content,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_layout(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        layout_id: "capo_connectcases.types.layout_id.LayoutId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_layout_response.GetLayoutResponse":
        """<p>Returns the details for the requested layout.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            layout_id: <p>The unique identifier of the layout.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_layout_request.GetLayoutRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_layout_response.GetLayoutResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_layout

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_layout.async_get_layout(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.get_layout_request.GetLayoutRequest = {
            "domain_id": domain_id,
            "layout_id": layout_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_layout(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        layout_id: "capo_connectcases.types.layout_id.LayoutId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        name: Optional["capo_connectcases.types.layout_name.LayoutName"] = None,
        content: Optional[
            "capo_connectcases.types.layout_content.LayoutContent"
        ] = None,
    ) -> "capo_connectcases.types.update_layout_response.UpdateLayoutResponse":
        """<p>Updates the attributes of an existing layout.</p> <p>If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.</p> <p>A <code>ValidationException</code> is returned when you add non-existent <code>fieldIds</code> to a layout.</p> <note> <p>Title and Status fields cannot be part of layouts because they are not configurable.</p> </note>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            layout_id: <p>The unique identifier of the layout.</p>
            name: <p>The name of the layout. It must be unique per domain.</p>
            content: <p>Information about which fields will be present in the layout, the order of the fields.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.update_layout_request.UpdateLayoutRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.update_layout_response.UpdateLayoutResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_layout

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.update_layout.async_update_layout(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.update_layout_request.UpdateLayoutRequest = {
            "domain_id": domain_id,
            "layout_id": layout_id,
        }
        if name is not None:
            input_["name"] = name
        if content is not None:
            input_["content"] = content

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_layout(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        layout_id: "capo_connectcases.types.layout_id.LayoutId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_layout_response.DeleteLayoutResponse":
        """<p>Deletes a layout from a cases template. You can delete up to 100 layouts per domain.</p> <p>After a layout is deleted:</p> <ul> <li> <p>You can still retrieve the layout by calling <code>GetLayout</code>.</p> </li> <li> <p>You cannot update a deleted layout by calling <code>UpdateLayout</code>; it throws a <code>ValidationException</code>.</p> </li> <li> <p>Deleted layouts are not included in the <code>ListLayouts</code> response.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain.</p>
            layout_id: <p>The unique identifier of the layout.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.delete_layout_request.DeleteLayoutRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_layout_response.DeleteLayoutResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_layout

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_layout.async_delete_layout(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_layout_request.DeleteLayoutRequest = {
            "domain_id": domain_id,
            "layout_id": layout_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_layouts(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "capo_connectcases.types.list_layouts_response.ListLayoutsResponse":
        """<p>Lists all layouts in the given cases domain. Each list item is a condensed summary object of the layout.</p>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_layouts_request.ListLayoutsRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_layouts_response.ListLayoutsResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_layouts

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_layouts.async_list_layouts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.list_layouts_request.ListLayoutsRequest = {
            "domain_id": domain_id
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

    async def iter_list_layouts(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_connectcases.types.list_layouts_response.ListLayoutsResponse]":
        _token = next_token
        while True:
            _response = await self.list_layouts(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_template(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        name: "capo_connectcases.types.template_name.TemplateName",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        description: Optional[
            "capo_connectcases.types.template_description.TemplateDescription"
        ] = None,
        layout_configuration: Optional[
            "capo_connectcases.types.layout_configuration.LayoutConfiguration"
        ] = None,
        required_fields: Optional[
            "capo_connectcases.types.required_field_list.RequiredFieldList"
        ] = None,
        status: Optional[
            "capo_connectcases.types.template_status.TemplateStatus"
        ] = None,
        rules: Optional[
            "capo_connectcases.types.template_case_rule_list.TemplateCaseRuleList"
        ] = None,
        tag_propagation_configurations: Optional[
            "capo_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
        ] = None,
    ) -> "capo_connectcases.types.create_template_response.CreateTemplateResponse":
        """<p>Creates a template in the Cases domain. This template is used to define the case object model (that is, to define what data can be captured on cases) in a Cases domain. A template must have a unique name within a domain, and it must reference existing field IDs and layout IDs. Additionally, multiple fields with same IDs are not allowed within the same Template. A template can be either Active or Inactive, as indicated by its status. Inactive templates cannot be used to create cases.</p> <p> Other template APIs are: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html">GetTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html">ListTemplates</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html">UpdateTemplate</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            name: <p>A name for the template. It must be unique per domain.</p>
            description: <p>A brief description of the template.</p>
            layout_configuration: <p>Configuration of layouts associated to the template.</p>
            required_fields: <p>A list of fields that must contain a value for a case to be successfully created with this template.</p>
            status: <p>The status of the template.</p>
            rules: <p>A list of case rules (also known as <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">case field conditions</a>) on a template. </p>
            tag_propagation_configurations: <p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.create_template_request.CreateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.create_template_response.CreateTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.create_template

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.create_template.async_create_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.create_template_request.CreateTemplateRequest = {
            "domain_id": domain_id,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if layout_configuration is not None:
            input_["layout_configuration"] = layout_configuration
        if required_fields is not None:
            input_["required_fields"] = required_fields
        if status is not None:
            input_["status"] = status
        if rules is not None:
            input_["rules"] = rules
        if tag_propagation_configurations is not None:
            input_["tag_propagation_configurations"] = tag_propagation_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_template(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.get_template_response.GetTemplateResponse":
        """<p>Returns the details for the requested template. Other template APIs are: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html">CreateTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html">ListTemplates</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html">UpdateTemplate</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier of a template.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.get_template_request.GetTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.get_template_response.GetTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.get_template

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.get_template.async_get_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.get_template_request.GetTemplateRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_template(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        name: Optional["capo_connectcases.types.template_name.TemplateName"] = None,
        description: Optional[
            "capo_connectcases.types.template_description.TemplateDescription"
        ] = None,
        layout_configuration: Optional[
            "capo_connectcases.types.layout_configuration.LayoutConfiguration"
        ] = None,
        required_fields: Optional[
            "capo_connectcases.types.required_field_list.RequiredFieldList"
        ] = None,
        status: Optional[
            "capo_connectcases.types.template_status.TemplateStatus"
        ] = None,
        rules: Optional[
            "capo_connectcases.types.template_case_rule_list.TemplateCaseRuleList"
        ] = None,
        tag_propagation_configurations: Optional[
            "capo_connectcases.types.tag_propagation_configuration_list.TagPropagationConfigurationList"
        ] = None,
    ) -> "capo_connectcases.types.update_template_response.UpdateTemplateResponse":
        """<p>Updates the attributes of an existing template. The template attributes that can be modified include <code>name</code>, <code>description</code>, <code>layoutConfiguration</code>, <code>requiredFields</code>, and <code>status</code>. At least one of these attributes must not be null. If a null value is provided for a given attribute, that attribute is ignored and its current value is preserved.</p> <p>Other template APIs are:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html">CreateTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html">GetTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html">ListTemplates</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            template_id: <p>A unique identifier for the template.</p>
            name: <p>The name of the template. It must be unique per domain.</p>
            description: <p>A brief description of the template.</p>
            layout_configuration: <p>Configuration of layouts associated to the template.</p>
            required_fields: <p>A list of fields that must contain a value for a case to be successfully created with this template.</p>
            status: <p>The status of the template.</p>
            rules: <p>A list of case rules (also known as <a href="https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html">case field conditions</a>) on a template.</p>
            tag_propagation_configurations: <p>Defines tag propagation configuration for resources created within a domain. Tags specified here will be automatically applied to resources being created for the specified resource type.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded. For a list of service quotas, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Amazon Connect Service Quotas</a> in the <i>Amazon Connect Administrator Guide</i>.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.update_template_request.UpdateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.update_template_response.UpdateTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.update_template

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.update_template.async_update_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.update_template_request.UpdateTemplateRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if layout_configuration is not None:
            input_["layout_configuration"] = layout_configuration
        if required_fields is not None:
            input_["required_fields"] = required_fields
        if status is not None:
            input_["status"] = status
        if rules is not None:
            input_["rules"] = rules
        if tag_propagation_configurations is not None:
            input_["tag_propagation_configurations"] = tag_propagation_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_template(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        template_id: "capo_connectcases.types.template_id.TemplateId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
    ) -> "capo_connectcases.types.delete_template_response.DeleteTemplateResponse":
        """<p>Deletes a cases template. You can delete up to 100 templates per domain.</p> <p>After a cases template is deleted:</p> <ul> <li> <p>You can still retrieve the template by calling <code>GetTemplate</code>.</p> </li> <li> <p>You cannot update the template. </p> </li> <li> <p>You cannot create a case by using the deleted template.</p> </li> <li> <p>Deleted templates are not included in the <code>ListTemplates</code> response.</p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain.</p>
            template_id: <p>A unique identifier of a template.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.delete_template_request.DeleteTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.delete_template_response.DeleteTemplateResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.delete_template

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.delete_template.async_delete_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.delete_template_request.DeleteTemplateRequest = {
            "domain_id": domain_id,
            "template_id": template_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_templates(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        status: Optional[
            "capo_connectcases.types.template_status_filters.TemplateStatusFilters"
        ] = None,
    ) -> "capo_connectcases.types.list_templates_response.ListTemplatesResponse":
        """<p>Lists all of the templates in a Cases domain. Each list item is a condensed summary object of the template. </p> <p> Other template APIs are: </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateTemplate.html">CreateTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html">DeleteTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html">GetTemplate</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html">UpdateTemplate</a> </p> </li> </ul>

        Args:
            domain_id: <p>The unique identifier of the Cases domain. </p>
            max_results: <p>The maximum number of results to return per page.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            status: <p>A list of status values to filter on.</p>

        Raises:
            capo_connectcases.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_connectcases.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_connectcases.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same Amazon Web Services Region as your request, and try your request again.</p>
            capo_connectcases.errors.throttling_exception.ThrottlingException: <p>The rate has been exceeded for this API. Please try again after a few minutes.</p>
            capo_connectcases.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_connectcases.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_connectcases.types.list_templates_request.ListTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_connectcases.types.list_templates_response.ListTemplatesResponse"
        ]:
            import capo_connectcases._operations.amazon_connect_cases.list_templates

            (
                output,
                http_response,
            ) = await capo_connectcases._operations.amazon_connect_cases.list_templates.async_list_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_connectcases.types.list_templates_request.ListTemplatesRequest = {
            "domain_id": domain_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_templates(
        self,
        domain_id: "capo_connectcases.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncConnectCasesClientConfig] = None,
        max_results: Optional["capo_connectcases.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_connectcases.types.next_token.NextToken"] = None,
        status: Optional[
            "capo_connectcases.types.template_status_filters.TemplateStatusFilters"
        ] = None,
    ) -> "AsyncIterator[capo_connectcases.types.list_templates_response.ListTemplatesResponse]":
        _token = next_token
        while True:
            _response = await self.list_templates(
                domain_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
