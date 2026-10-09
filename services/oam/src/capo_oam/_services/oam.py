"""Generated from Smithy shape ``com.amazonaws.oam#oamservice``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_oam._auth._signers
import capo_oam._auth._sigv4
from capo_oam._auth._identity import Credentials
from capo_oam._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_oam._auth._zapros_handler import AuthMiddleware
from capo_oam._pagination import resolve_path as _resolve_path
from capo_oam._services._aws_config import aws_config
from capo_oam._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_oam.types.arn
    import capo_oam.types.create_link_input
    import capo_oam.types.create_link_output
    import capo_oam.types.create_sink_input
    import capo_oam.types.create_sink_output
    import capo_oam.types.delete_link_input
    import capo_oam.types.delete_link_output
    import capo_oam.types.delete_sink_input
    import capo_oam.types.delete_sink_output
    import capo_oam.types.get_link_input
    import capo_oam.types.get_link_output
    import capo_oam.types.get_sink_input
    import capo_oam.types.get_sink_output
    import capo_oam.types.get_sink_policy_input
    import capo_oam.types.get_sink_policy_output
    import capo_oam.types.include_tags
    import capo_oam.types.label_template
    import capo_oam.types.link_configuration
    import capo_oam.types.list_attached_links_input
    import capo_oam.types.list_attached_links_item
    import capo_oam.types.list_attached_links_max_results
    import capo_oam.types.list_attached_links_output
    import capo_oam.types.list_links_input
    import capo_oam.types.list_links_item
    import capo_oam.types.list_links_max_results
    import capo_oam.types.list_links_output
    import capo_oam.types.list_sinks_input
    import capo_oam.types.list_sinks_item
    import capo_oam.types.list_sinks_max_results
    import capo_oam.types.list_sinks_output
    import capo_oam.types.list_tags_for_resource_input
    import capo_oam.types.list_tags_for_resource_output
    import capo_oam.types.next_token
    import capo_oam.types.put_sink_policy_input
    import capo_oam.types.put_sink_policy_output
    import capo_oam.types.resource_identifier
    import capo_oam.types.resource_types_input
    import capo_oam.types.sink_name
    import capo_oam.types.sink_policy
    import capo_oam.types.tag_keys
    import capo_oam.types.tag_map_input
    import capo_oam.types.tag_resource_input
    import capo_oam.types.tag_resource_output
    import capo_oam.types.untag_resource_input
    import capo_oam.types.untag_resource_output
    import capo_oam.types.update_link_input
    import capo_oam.types.update_link_output


class OAMClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class OAMClient:
    """A client for the ``OAM`` service.

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
        self._config = OAMClientConfig(
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
        self, config_overrides: Optional[OAMClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: OAMClientConfig = config_overrides or {}
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

    def create_link(
        self,
        label_template: "capo_oam.types.label_template.LabelTemplate",
        resource_types: "capo_oam.types.resource_types_input.ResourceTypesInput",
        sink_identifier: "capo_oam.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        tags: Optional["capo_oam.types.tag_map_input.TagMapInput"] = None,
        link_configuration: Optional[
            "capo_oam.types.link_configuration.LinkConfiguration"
        ] = None,
    ) -> "capo_oam.types.create_link_output.CreateLinkOutput":
        """<p>Creates a link between a source account and a sink that you have created in a monitoring account. After the link is created, data is sent from the source account to the monitoring account. When you create a link, you can optionally specify filters that specify which metric namespaces and which log groups are shared from the source account to the monitoring account.</p> <p>Before you create a link, you must create a sink in the monitoring account and create a sink policy in that account. The sink policy must permit the source account to link to it. You can grant permission to source accounts by granting permission to an entire organization or to individual accounts.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html">CreateSink</a> and <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html">PutSinkPolicy</a>.</p> <p>Each monitoring account can be linked to as many as 100,000 source accounts.</p> <p>Each source account can be linked to as many as five monitoring accounts.</p>

        Args:
            label_template: <p>Specify a friendly human-readable name to use to identify this source account when you are viewing data from it in the monitoring account.</p> <p>You can use a custom label or use the following variables:</p> <ul> <li> <p> <code>$AccountName</code> is the name of the account</p> </li> <li> <p> <code>$AccountEmail</code> is the globally unique email address of the account</p> </li> <li> <p> <code>$AccountEmailNoDomain</code> is the email address of the account without the domain name</p> </li> </ul> <note> <p>In the Amazon Web Services GovCloud (US-East) and Amazon Web Services GovCloud (US-West) Regions, the only supported option is to use custom labels, and the <code>$AccountName</code>, <code>$AccountEmail</code>, and <code>$AccountEmailNoDomain</code> variables all resolve as <i>account-id</i> instead of the specified variable.</p> </note>
            resource_types: <p>An array of strings that define which types of data that the source account shares with the monitoring account.</p>
            sink_identifier: <p>The ARN of the sink to use to create this link. You can use <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html">ListSinks</a> to find the ARNs of sinks.</p> <p>For more information about sinks, see <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html">CreateSink</a>.</p>
            tags: <p>Assigns one or more tags (key-value pairs) to the link. </p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>For more information about using tags to control access, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html">Controlling access to Amazon Web Services resources using tags</a>.</p>
            link_configuration: <p>Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.</p>

        Raises:
            capo_oam.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>A required parameter is missing from the request.</p>
            capo_oam.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.create_link_input.CreateLinkInput]",
        ) -> OperationResponse["capo_oam.types.create_link_output.CreateLinkOutput"]:
            import capo_oam._operations.oamservice.create_link

            output, http_response = (
                capo_oam._operations.oamservice.create_link.create_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.create_link_input.CreateLinkInput = {
            "label_template": label_template,
            "resource_types": resource_types,
            "sink_identifier": sink_identifier,
        }
        if tags is not None:
            input_["tags"] = tags
        if link_configuration is not None:
            input_["link_configuration"] = link_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_sink(
        self,
        name: "capo_oam.types.sink_name.SinkName",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        tags: Optional["capo_oam.types.tag_map_input.TagMapInput"] = None,
    ) -> "capo_oam.types.create_sink_output.CreateSinkOutput":
        """<p>Use this to create a <i>sink</i> in the current account, so that it can be used as a monitoring account in CloudWatch cross-account observability. A sink is a resource that represents an attachment point in a monitoring account. Source accounts can link to the sink to send observability data.</p> <p>After you create a sink, you must create a sink policy that allows source accounts to attach to it. For more information, see <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html">PutSinkPolicy</a>.</p> <p>Each account can contain one sink per Region. If you delete a sink, you can then create a new one in that Region.</p>

        Args:
            name: <p>A name for the sink.</p>
            tags: <p>Assigns one or more tags (key-value pairs) to the link. </p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>For more information about using tags to control access, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html">Controlling access to Amazon Web Services resources using tags</a>.</p>

        Raises:
            capo_oam.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>A required parameter is missing from the request.</p>
            capo_oam.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.create_sink_input.CreateSinkInput]",
        ) -> OperationResponse["capo_oam.types.create_sink_output.CreateSinkOutput"]:
            import capo_oam._operations.oamservice.create_sink

            output, http_response = (
                capo_oam._operations.oamservice.create_sink.create_sink(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.create_sink_input.CreateSinkInput = {"name": name}
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_link(
        self,
        identifier: "capo_oam.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
    ) -> "capo_oam.types.delete_link_output.DeleteLinkOutput":
        """<p>Deletes a link between a monitoring account sink and a source account. You must run this operation in the source account.</p>

        Args:
            identifier: <p>The ARN of the link to delete.</p>

        Raises:
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>A required parameter is missing from the request.</p>
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.delete_link_input.DeleteLinkInput]",
        ) -> OperationResponse["capo_oam.types.delete_link_output.DeleteLinkOutput"]:
            import capo_oam._operations.oamservice.delete_link

            output, http_response = (
                capo_oam._operations.oamservice.delete_link.delete_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.delete_link_input.DeleteLinkInput = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_sink(
        self,
        identifier: "capo_oam.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
    ) -> "capo_oam.types.delete_sink_output.DeleteSinkOutput":
        """<p>Deletes a sink. You must delete all links to a sink before you can delete that sink.</p>

        Args:
            identifier: <p>The ARN of the sink to delete.</p>

        Raises:
            capo_oam.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>A required parameter is missing from the request.</p>
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.delete_sink_input.DeleteSinkInput]",
        ) -> OperationResponse["capo_oam.types.delete_sink_output.DeleteSinkOutput"]:
            import capo_oam._operations.oamservice.delete_sink

            output, http_response = (
                capo_oam._operations.oamservice.delete_sink.delete_sink(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.delete_sink_input.DeleteSinkInput = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_link(
        self,
        identifier: "capo_oam.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        include_tags: Optional["capo_oam.types.include_tags.IncludeTags"] = None,
    ) -> "capo_oam.types.get_link_output.GetLinkOutput":
        """<p>Returns complete information about one link.</p> <p>To use this operation, provide the link ARN. To retrieve a list of link ARNs, use <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html">ListLinks</a>.</p>

        Args:
            identifier: <p>The ARN of the link to retrieve information for.</p>
            include_tags: <p>Specifies whether to include the tags associated with the link in the response. When <code>IncludeTags</code> is set to <code>true</code> and the caller has the required permission, <code>oam:ListTagsForResource</code>, the API will return the tags for the specified resource. If the caller doesn't have the required permission, <code>oam:ListTagsForResource</code>, the API will raise an exception.</p> <p>The default value is <code>false</code>.</p>

        Raises:
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>A required parameter is missing from the request.</p>
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.get_link_input.GetLinkInput]",
        ) -> OperationResponse["capo_oam.types.get_link_output.GetLinkOutput"]:
            import capo_oam._operations.oamservice.get_link

            output, http_response = capo_oam._operations.oamservice.get_link.get_link(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.get_link_input.GetLinkInput = {"identifier": identifier}
        if include_tags is not None:
            input_["include_tags"] = include_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sink(
        self,
        identifier: "capo_oam.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        include_tags: Optional["capo_oam.types.include_tags.IncludeTags"] = None,
    ) -> "capo_oam.types.get_sink_output.GetSinkOutput":
        """<p>Returns complete information about one monitoring account sink.</p> <p>To use this operation, provide the sink ARN. To retrieve a list of sink ARNs, use <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html">ListSinks</a>.</p>

        Args:
            identifier: <p>The ARN of the sink to retrieve information for.</p>
            include_tags: <p>Specifies whether to include the tags associated with the sink in the response. When <code>IncludeTags</code> is set to <code>true</code> and the caller has the required permission, <code>oam:ListTagsForResource</code>, the API will return the tags for the specified resource. If the caller doesn't have the required permission, <code>oam:ListTagsForResource</code>, the API will raise an exception.</p> <p>The default value is <code>false</code>.</p>

        Raises:
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>A required parameter is missing from the request.</p>
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.get_sink_input.GetSinkInput]",
        ) -> OperationResponse["capo_oam.types.get_sink_output.GetSinkOutput"]:
            import capo_oam._operations.oamservice.get_sink

            output, http_response = capo_oam._operations.oamservice.get_sink.get_sink(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.get_sink_input.GetSinkInput = {"identifier": identifier}
        if include_tags is not None:
            input_["include_tags"] = include_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sink_policy(
        self,
        sink_identifier: "capo_oam.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
    ) -> "capo_oam.types.get_sink_policy_output.GetSinkPolicyOutput":
        """<p>Returns the current sink policy attached to this sink. The sink policy specifies what accounts can attach to this sink as source accounts, and what types of data they can share.</p>

        Args:
            sink_identifier: <p>The ARN of the sink to retrieve the policy of.</p>

        Raises:
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>A required parameter is missing from the request.</p>
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.get_sink_policy_input.GetSinkPolicyInput]",
        ) -> OperationResponse[
            "capo_oam.types.get_sink_policy_output.GetSinkPolicyOutput"
        ]:
            import capo_oam._operations.oamservice.get_sink_policy

            output, http_response = (
                capo_oam._operations.oamservice.get_sink_policy.get_sink_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.get_sink_policy_input.GetSinkPolicyInput = {
            "sink_identifier": sink_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_attached_links(
        self,
        sink_identifier: "capo_oam.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        max_results: Optional[
            "capo_oam.types.list_attached_links_max_results.ListAttachedLinksMaxResults"
        ] = None,
        next_token: Optional["capo_oam.types.next_token.NextToken"] = None,
    ) -> "capo_oam.types.list_attached_links_output.ListAttachedLinksOutput":
        """<p>Returns a list of source account links that are linked to this monitoring account sink.</p> <p>To use this operation, provide the sink ARN. To retrieve a list of sink ARNs, use <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html">ListSinks</a>.</p> <p>To find a list of links for one source account, use <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListLinks.html">ListLinks</a>.</p>

        Args:
            max_results: <p>Limits the number of returned links to the specified number.</p>
            next_token: <p>The token for the next set of items to return. You received this token from a previous call.</p>
            sink_identifier: <p>The ARN of the sink that you want to retrieve links for.</p>

        Raises:
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>A required parameter is missing from the request.</p>
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.list_attached_links_input.ListAttachedLinksInput]",
        ) -> OperationResponse[
            "capo_oam.types.list_attached_links_output.ListAttachedLinksOutput"
        ]:
            import capo_oam._operations.oamservice.list_attached_links

            output, http_response = (
                capo_oam._operations.oamservice.list_attached_links.list_attached_links(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.list_attached_links_input.ListAttachedLinksInput = {
            "sink_identifier": sink_identifier
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

    def iter_list_attached_links(
        self,
        sink_identifier: "capo_oam.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        max_results: Optional[
            "capo_oam.types.list_attached_links_max_results.ListAttachedLinksMaxResults"
        ] = None,
        next_token: Optional["capo_oam.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_oam.types.list_attached_links_item.ListAttachedLinksItem]":
        _token = next_token
        while True:
            _response = self.list_attached_links(
                sink_identifier,
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

    def list_links(
        self,
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        max_results: Optional[
            "capo_oam.types.list_links_max_results.ListLinksMaxResults"
        ] = None,
        next_token: Optional["capo_oam.types.next_token.NextToken"] = None,
    ) -> "capo_oam.types.list_links_output.ListLinksOutput":
        """<p>Use this operation in a source account to return a list of links to monitoring account sinks that this source account has.</p> <p>To find a list of links for one monitoring account sink, use <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListAttachedLinks.html">ListAttachedLinks</a> from within the monitoring account.</p>

        Args:
            max_results: <p>Limits the number of returned links to the specified number.</p>
            next_token: <p>The token for the next set of items to return. You received this token from a previous call.</p>

        Raises:
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.list_links_input.ListLinksInput]",
        ) -> OperationResponse["capo_oam.types.list_links_output.ListLinksOutput"]:
            import capo_oam._operations.oamservice.list_links

            output, http_response = (
                capo_oam._operations.oamservice.list_links.list_links(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.list_links_input.ListLinksInput = {}
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

    def iter_list_links(
        self,
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        max_results: Optional[
            "capo_oam.types.list_links_max_results.ListLinksMaxResults"
        ] = None,
        next_token: Optional["capo_oam.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_oam.types.list_links_item.ListLinksItem]":
        _token = next_token
        while True:
            _response = self.list_links(
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

    def list_sinks(
        self,
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        max_results: Optional[
            "capo_oam.types.list_sinks_max_results.ListSinksMaxResults"
        ] = None,
        next_token: Optional["capo_oam.types.next_token.NextToken"] = None,
    ) -> "capo_oam.types.list_sinks_output.ListSinksOutput":
        """<p>Use this operation in a monitoring account to return the list of sinks created in that account.</p>

        Args:
            max_results: <p>Limits the number of returned links to the specified number.</p>
            next_token: <p>The token for the next set of items to return. You received this token from a previous call.</p>

        Raises:
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.list_sinks_input.ListSinksInput]",
        ) -> OperationResponse["capo_oam.types.list_sinks_output.ListSinksOutput"]:
            import capo_oam._operations.oamservice.list_sinks

            output, http_response = (
                capo_oam._operations.oamservice.list_sinks.list_sinks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.list_sinks_input.ListSinksInput = {}
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

    def iter_list_sinks(
        self,
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        max_results: Optional[
            "capo_oam.types.list_sinks_max_results.ListSinksMaxResults"
        ] = None,
        next_token: Optional["capo_oam.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_oam.types.list_sinks_item.ListSinksItem]":
        _token = next_token
        while True:
            _response = self.list_sinks(
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
        resource_arn: "capo_oam.types.arn.Arn",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
    ) -> "capo_oam.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Displays the tags associated with a resource. Both sinks and links support tagging.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you want to view tags for.</p> <p>The ARN format of a sink is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:sink/<i>sink-id</i> </code> </p> <p>The ARN format of a link is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:link/<i>link-id</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html">CloudWatch Logs resources and operations</a>.</p> <important> <p>Unlike tagging permissions in other Amazon Web Services services, to retrieve the list of tags for links or sinks you must have the <code>oam:RequestTag</code> permission. The <code>aws:ReguestTag</code> permission does not allow you to tag and untag links and sinks.</p> </important>

        Raises:
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_oam.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_oam._operations.oamservice.list_tags_for_resource

            output, http_response = (
                capo_oam._operations.oamservice.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_sink_policy(
        self,
        sink_identifier: "capo_oam.types.resource_identifier.ResourceIdentifier",
        policy: "capo_oam.types.sink_policy.SinkPolicy",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
    ) -> "capo_oam.types.put_sink_policy_output.PutSinkPolicyOutput":
        """<p>Creates or updates the resource policy that grants permissions to source accounts to link to the monitoring account sink. When you create a sink policy, you can grant permissions to all accounts in an organization or to individual accounts.</p> <p>You can also use a sink policy to limit the types of data that is shared. The six types of services with their respective resource types that you can allow or deny are:</p> <ul> <li> <p> <b>Metrics</b> - Specify with <code>AWS::CloudWatch::Metric</code> </p> </li> <li> <p> <b>Log groups</b> - Specify with <code>AWS::Logs::LogGroup</code> </p> </li> <li> <p> <b>Traces</b> - Specify with <code>AWS::XRay::Trace</code> </p> </li> <li> <p> <b>Application Insights - Applications</b> - Specify with <code>AWS::ApplicationInsights::Application</code> </p> </li> <li> <p> <b>Internet Monitor</b> - Specify with <code>AWS::InternetMonitor::Monitor</code> </p> </li> <li> <p> <b>Application Signals</b> - Specify with <code>AWS::ApplicationSignals::Service</code> and <code>AWS::ApplicationSignals::ServiceLevelObjective</code> </p> </li> </ul> <p>See the examples in this section to see how to specify permitted source accounts and data types.</p>

        Args:
            sink_identifier: <p>The ARN of the sink to attach this policy to.</p>
            policy: <p>The JSON policy to use. If you are updating an existing policy, the entire existing policy is replaced by what you specify here.</p> <p>The policy must be in JSON string format with quotation marks escaped and no newlines.</p> <p>For examples of different types of policies, see the <b>Examples</b> section on this page.</p>

        Raises:
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>A required parameter is missing from the request.</p>
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.put_sink_policy_input.PutSinkPolicyInput]",
        ) -> OperationResponse[
            "capo_oam.types.put_sink_policy_output.PutSinkPolicyOutput"
        ]:
            import capo_oam._operations.oamservice.put_sink_policy

            output, http_response = (
                capo_oam._operations.oamservice.put_sink_policy.put_sink_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.put_sink_policy_input.PutSinkPolicyInput = {
            "sink_identifier": sink_identifier,
            "policy": policy,
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
        resource_arn: "capo_oam.types.arn.Arn",
        tags: "capo_oam.types.tag_map_input.TagMapInput",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
    ) -> "capo_oam.types.tag_resource_output.TagResourceOutput":
        """<p>Assigns one or more tags (key-value pairs) to the specified resource. Both sinks and links can be tagged. </p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with a resource that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a resource.</p> <important> <p>Unlike tagging permissions in other Amazon Web Services services, to tag or untag links and sinks you must have the <code>oam:ResourceTag</code> permission. The <code>iam:ResourceTag</code> permission does not allow you to tag and untag links and sinks.</p> </important>

        Args:
            resource_arn: <p>The ARN of the resource that you're adding tags to.</p> <p>The ARN format of a sink is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:sink/<i>sink-id</i> </code> </p> <p>The ARN format of a link is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:link/<i>link-id</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html">CloudWatch Logs resources and operations</a>.</p>
            tags: <p>The list of key-value pairs to associate with the resource.</p>

        Raises:
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.too_many_tags_exception.TooManyTagsException: <p>A resource can have no more than 50 tags.</p>
            capo_oam.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse["capo_oam.types.tag_resource_output.TagResourceOutput"]:
            import capo_oam._operations.oamservice.tag_resource

            output, http_response = (
                capo_oam._operations.oamservice.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_oam.types.arn.Arn",
        tag_keys: "capo_oam.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
    ) -> "capo_oam.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tags from the specified resource.</p> <important> <p>Unlike tagging permissions in other Amazon Web Services services, to tag or untag links and sinks you must have the <code>oam:ResourceTag</code> permission. The <code>iam:TagResource</code> permission does not allow you to tag and untag links and sinks.</p> </important>

        Args:
            resource_arn: <p>The ARN of the resource that you're removing tags from.</p> <p>The ARN format of a sink is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:sink/<i>sink-id</i> </code> </p> <p>The ARN format of a link is <code>arn:aws:oam:<i>Region</i>:<i>account-id</i>:link/<i>link-id</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html">CloudWatch Logs resources and operations</a>.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_oam.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_oam._operations.oamservice.untag_resource

            output, http_response = (
                capo_oam._operations.oamservice.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.untag_resource_input.UntagResourceInput = {
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

    def update_link(
        self,
        identifier: "capo_oam.types.resource_identifier.ResourceIdentifier",
        resource_types: "capo_oam.types.resource_types_input.ResourceTypesInput",
        *,
        config_overrides: Optional[OAMClientConfig] = None,
        link_configuration: Optional[
            "capo_oam.types.link_configuration.LinkConfiguration"
        ] = None,
        include_tags: Optional["capo_oam.types.include_tags.IncludeTags"] = None,
    ) -> "capo_oam.types.update_link_output.UpdateLinkOutput":
        """<p>Use this operation to change what types of data are shared from a source account to its linked monitoring account sink. You can't change the sink or change the monitoring account with this operation.</p> <p>When you update a link, you can optionally specify filters that specify which metric namespaces and which log groups are shared from the source account to the monitoring account.</p> <p>To update the list of tags associated with the sink, use <a href="https://docs.aws.amazon.com/OAM/latest/APIReference/API_TagResource.html">TagResource</a>.</p>

        Args:
            identifier: <p>The ARN of the link that you want to update.</p>
            resource_types: <p>An array of strings that define which types of data that the source account will send to the monitoring account.</p> <p>Your input here replaces the current set of data types that are shared.</p>
            link_configuration: <p>Use this structure to filter which metric namespaces and which log groups are to be shared from the source account to the monitoring account.</p>
            include_tags: <p>Specifies whether to include the tags associated with the link in the response after the update operation. When <code>IncludeTags</code> is set to <code>true</code> and the caller has the required permission, <code>oam:ListTagsForResource</code>, the API will return the tags for the specified resource. If the caller doesn't have the required permission, <code>oam:ListTagsForResource</code>, the API will raise an exception. </p> <p>The default value is <code>false</code>.</p>

        Raises:
            capo_oam.errors.internal_service_fault.InternalServiceFault: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_oam.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_oam.errors.missing_required_parameter_exception.MissingRequiredParameterException: <p>A required parameter is missing from the request.</p>
            capo_oam.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_oam.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_oam.types.update_link_input.UpdateLinkInput]",
        ) -> OperationResponse["capo_oam.types.update_link_output.UpdateLinkOutput"]:
            import capo_oam._operations.oamservice.update_link

            output, http_response = (
                capo_oam._operations.oamservice.update_link.update_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_oam.types.update_link_input.UpdateLinkInput = {
            "identifier": identifier,
            "resource_types": resource_types,
        }
        if link_configuration is not None:
            input_["link_configuration"] = link_configuration
        if include_tags is not None:
            input_["include_tags"] = include_tags

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
