"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#CloudApiService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_cloudcontrol._auth._signers
import capo_cloudcontrol._auth._sigv4
from capo_cloudcontrol._auth._identity import Credentials
from capo_cloudcontrol._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloudcontrol._auth._zapros_handler import AuthMiddleware
from capo_cloudcontrol._pagination import resolve_path as _resolve_path
from capo_cloudcontrol._services._aws_config import aaws_config
from capo_cloudcontrol._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_cloudcontrol.types.cancel_resource_request_input
    import capo_cloudcontrol.types.cancel_resource_request_output
    import capo_cloudcontrol.types.client_token
    import capo_cloudcontrol.types.create_resource_input
    import capo_cloudcontrol.types.create_resource_output
    import capo_cloudcontrol.types.delete_resource_input
    import capo_cloudcontrol.types.delete_resource_output
    import capo_cloudcontrol.types.get_resource_input
    import capo_cloudcontrol.types.get_resource_output
    import capo_cloudcontrol.types.get_resource_request_status_input
    import capo_cloudcontrol.types.get_resource_request_status_output
    import capo_cloudcontrol.types.handler_next_token
    import capo_cloudcontrol.types.identifier
    import capo_cloudcontrol.types.list_resource_requests_input
    import capo_cloudcontrol.types.list_resource_requests_output
    import capo_cloudcontrol.types.list_resources_input
    import capo_cloudcontrol.types.list_resources_output
    import capo_cloudcontrol.types.max_results
    import capo_cloudcontrol.types.next_token
    import capo_cloudcontrol.types.patch_document
    import capo_cloudcontrol.types.progress_event
    import capo_cloudcontrol.types.properties
    import capo_cloudcontrol.types.request_token
    import capo_cloudcontrol.types.resource_description
    import capo_cloudcontrol.types.resource_request_status_filter
    import capo_cloudcontrol.types.role_arn
    import capo_cloudcontrol.types.type_name
    import capo_cloudcontrol.types.type_version_id
    import capo_cloudcontrol.types.update_resource_input
    import capo_cloudcontrol.types.update_resource_output


class AsyncCloudControlClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncCloudControlClient:
    """A client for the ``CloudControl`` service.

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
        self._config = AsyncCloudControlClientConfig(
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
        self, config_overrides: Optional[AsyncCloudControlClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCloudControlClientConfig = config_overrides or {}
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

    async def cancel_resource_request(
        self,
        request_token: "capo_cloudcontrol.types.request_token.RequestToken",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
    ) -> "capo_cloudcontrol.types.cancel_resource_request_output.CancelResourceRequestOutput":
        """<p>Cancels the specified resource operation request. For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-cancel">Canceling resource operation requests</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>Only resource operations requests with a status of <code>PENDING</code> or <code>IN_PROGRESS</code> can be canceled.</p>

        Args:
            request_token: <p>The <code>RequestToken</code> of the <code>ProgressEvent</code> object returned by the resource operation request.</p>

        Raises:
            capo_cloudcontrol.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource is currently being modified by another operation.</p>
            capo_cloudcontrol.errors.request_token_not_found_exception.RequestTokenNotFoundException: <p>A resource operation with the specified request token can't be found.</p>
            capo_cloudcontrol.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudcontrol.types.cancel_resource_request_input.CancelResourceRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudcontrol.types.cancel_resource_request_output.CancelResourceRequestOutput"
        ]:
            import capo_cloudcontrol._operations.cloud_api_service.cancel_resource_request

            (
                output,
                http_response,
            ) = await capo_cloudcontrol._operations.cloud_api_service.cancel_resource_request.async_cancel_resource_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudcontrol.types.cancel_resource_request_input.CancelResourceRequestInput = {
            "request_token": request_token
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_resource(
        self,
        type_name: "capo_cloudcontrol.types.type_name.TypeName",
        desired_state: "capo_cloudcontrol.types.properties.Properties",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "capo_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["capo_cloudcontrol.types.role_arn.RoleArn"] = None,
        client_token: Optional[
            "capo_cloudcontrol.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudcontrol.types.create_resource_output.CreateResourceOutput":
        """<p>Creates the specified resource. For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-create.html">Creating a resource</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>After you have initiated a resource creation request, you can monitor the progress of your request by calling <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html">GetResourceRequestStatus</a> using the <code>RequestToken</code> of the <code>ProgressEvent</code> type returned by <code>CreateResource</code>.</p>

        Args:
            type_name: <p>The name of the resource type.</p>
            type_version_id: <p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers">handlers</a> </code> section of the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            client_token: <p>A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately distinguish between request retries and new resource requests. You might retry a resource request to ensure that it was successfully received.</p> <p>A client token is valid for 36 hours once used. After that, a resource request with the same client token is treated as a new request.</p> <p>If you do not specify a client token, one is generated for inclusion in the request.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-idempotency">Ensuring resource operation requests are unique</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            desired_state: <p>Structured data format representing the desired state of the resource, consisting of that resource's properties and their desired values.</p> <note> <p>Cloud Control API currently supports JSON as a structured data format.</p> </note> <p>Specify the desired state as one of the following:</p> <ul> <li> <p>A JSON blob</p> </li> <li> <p>A local path containing the desired state in JSON data format</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-create.html#resource-operations-create-desiredstate">Composing the desired state of the resource</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>For more information about the properties of a specific resource, refer to the related topic for the resource in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Resource and property types reference</a> in the <i>CloudFormation Users Guide</i>.</p>

        Raises:
            capo_cloudcontrol.errors.already_exists_exception.AlreadyExistsException: <p>The resource with the name requested already exists.</p>
            capo_cloudcontrol.errors.client_token_conflict_exception.ClientTokenConflictException: <p>The specified client token has already been used in another resource request.</p> <p>It's best practice for client tokens to be unique for each resource operation request. However, client token expire after 36 hours.</p>
            capo_cloudcontrol.errors.concurrent_operation_exception.ConcurrentOperationException: <p>Another resource operation is currently being performed on this resource.</p>
            capo_cloudcontrol.errors.general_service_exception.GeneralServiceException: <p>The resource handler has returned that the downstream service generated an error that doesn't map to any other handler error code.</p>
            capo_cloudcontrol.errors.handler_failure_exception.HandlerFailureException: <p>The resource handler has failed without a returning a more specific error code. This can include timeouts.</p>
            capo_cloudcontrol.errors.handler_internal_failure_exception.HandlerInternalFailureException: <p>The resource handler has returned that an unexpected error occurred within the resource handler.</p>
            capo_cloudcontrol.errors.invalid_credentials_exception.InvalidCredentialsException: <p>The resource handler has returned that the credentials provided by the user are invalid.</p>
            capo_cloudcontrol.errors.invalid_request_exception.InvalidRequestException: <p>The resource handler has returned that invalid input from the user has generated a generic exception.</p>
            capo_cloudcontrol.errors.network_failure_exception.NetworkFailureException: <p>The resource handler has returned that the request couldn't be completed due to networking issues, such as a failure to receive a response from the server.</p>
            capo_cloudcontrol.errors.not_stabilized_exception.NotStabilizedException: <p>The resource handler has returned that the downstream resource failed to complete all of its ready-state checks.</p>
            capo_cloudcontrol.errors.not_updatable_exception.NotUpdatableException: <p>One or more properties included in this resource operation are defined as create-only, and therefore can't be updated.</p>
            capo_cloudcontrol.errors.private_type_exception.PrivateTypeException: <p>Cloud Control API hasn't received a valid response from the resource handler, due to a configuration error. This includes issues such as the resource handler returning an invalid response, or timing out.</p>
            capo_cloudcontrol.errors.resource_conflict_exception.ResourceConflictException: <p>The resource is temporarily unavailable to be acted upon. For example, if the resource is currently undergoing an operation and can't be acted upon until that operation is finished.</p>
            capo_cloudcontrol.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource with the specified identifier can't be found.</p>
            capo_cloudcontrol.errors.service_internal_error_exception.ServiceInternalErrorException: <p>The resource handler has returned that the downstream service returned an internal error, typically with a <code>5XX HTTP</code> status code.</p>
            capo_cloudcontrol.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The resource handler has returned that a non-transient resource limit was reached on the service side.</p>
            capo_cloudcontrol.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cloudcontrol.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudcontrol.errors.unsupported_action_exception.UnsupportedActionException: <p>The specified resource doesn't support this resource operation.</p>
            capo_cloudcontrol.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudcontrol.types.create_resource_input.CreateResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudcontrol.types.create_resource_output.CreateResourceOutput"
        ]:
            import capo_cloudcontrol._operations.cloud_api_service.create_resource

            (
                output,
                http_response,
            ) = await capo_cloudcontrol._operations.cloud_api_service.create_resource.async_create_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudcontrol.types.create_resource_input.CreateResourceInput = {
            "type_name": type_name,
            "desired_state": desired_state,
        }
        if type_version_id is not None:
            input_["type_version_id"] = type_version_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
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

    async def delete_resource(
        self,
        type_name: "capo_cloudcontrol.types.type_name.TypeName",
        identifier: "capo_cloudcontrol.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "capo_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["capo_cloudcontrol.types.role_arn.RoleArn"] = None,
        client_token: Optional[
            "capo_cloudcontrol.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudcontrol.types.delete_resource_output.DeleteResourceOutput":
        """<p>Deletes the specified resource. For details, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-delete.html">Deleting a resource</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>After you have initiated a resource deletion request, you can monitor the progress of your request by calling <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html">GetResourceRequestStatus</a> using the <code>RequestToken</code> of the <code>ProgressEvent</code> returned by <code>DeleteResource</code>.</p>

        Args:
            type_name: <p>The name of the resource type.</p>
            type_version_id: <p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers">handlers</a> </code> section of the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            client_token: <p>A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately distinguish between request retries and new resource requests. You might retry a resource request to ensure that it was successfully received.</p> <p>A client token is valid for 36 hours once used. After that, a resource request with the same client token is treated as a new request.</p> <p>If you do not specify a client token, one is generated for inclusion in the request.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-idempotency">Ensuring resource operation requests are unique</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            identifier: <p>The identifier for the resource.</p> <p>You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Primary identifiers can be specified as a string or JSON; secondary identifiers must be specified as JSON.</p> <p>For compound primary identifiers (that is, one that consists of multiple resource properties strung together), to specify the primary identifier as a string, list the property values <i>in the order they are specified</i> in the primary identifier definition, separated by <code>|</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html">Identifying resources</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>

        Raises:
            capo_cloudcontrol.errors.already_exists_exception.AlreadyExistsException: <p>The resource with the name requested already exists.</p>
            capo_cloudcontrol.errors.client_token_conflict_exception.ClientTokenConflictException: <p>The specified client token has already been used in another resource request.</p> <p>It's best practice for client tokens to be unique for each resource operation request. However, client token expire after 36 hours.</p>
            capo_cloudcontrol.errors.concurrent_operation_exception.ConcurrentOperationException: <p>Another resource operation is currently being performed on this resource.</p>
            capo_cloudcontrol.errors.general_service_exception.GeneralServiceException: <p>The resource handler has returned that the downstream service generated an error that doesn't map to any other handler error code.</p>
            capo_cloudcontrol.errors.handler_failure_exception.HandlerFailureException: <p>The resource handler has failed without a returning a more specific error code. This can include timeouts.</p>
            capo_cloudcontrol.errors.handler_internal_failure_exception.HandlerInternalFailureException: <p>The resource handler has returned that an unexpected error occurred within the resource handler.</p>
            capo_cloudcontrol.errors.invalid_credentials_exception.InvalidCredentialsException: <p>The resource handler has returned that the credentials provided by the user are invalid.</p>
            capo_cloudcontrol.errors.invalid_request_exception.InvalidRequestException: <p>The resource handler has returned that invalid input from the user has generated a generic exception.</p>
            capo_cloudcontrol.errors.network_failure_exception.NetworkFailureException: <p>The resource handler has returned that the request couldn't be completed due to networking issues, such as a failure to receive a response from the server.</p>
            capo_cloudcontrol.errors.not_stabilized_exception.NotStabilizedException: <p>The resource handler has returned that the downstream resource failed to complete all of its ready-state checks.</p>
            capo_cloudcontrol.errors.not_updatable_exception.NotUpdatableException: <p>One or more properties included in this resource operation are defined as create-only, and therefore can't be updated.</p>
            capo_cloudcontrol.errors.private_type_exception.PrivateTypeException: <p>Cloud Control API hasn't received a valid response from the resource handler, due to a configuration error. This includes issues such as the resource handler returning an invalid response, or timing out.</p>
            capo_cloudcontrol.errors.resource_conflict_exception.ResourceConflictException: <p>The resource is temporarily unavailable to be acted upon. For example, if the resource is currently undergoing an operation and can't be acted upon until that operation is finished.</p>
            capo_cloudcontrol.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource with the specified identifier can't be found.</p>
            capo_cloudcontrol.errors.service_internal_error_exception.ServiceInternalErrorException: <p>The resource handler has returned that the downstream service returned an internal error, typically with a <code>5XX HTTP</code> status code.</p>
            capo_cloudcontrol.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The resource handler has returned that a non-transient resource limit was reached on the service side.</p>
            capo_cloudcontrol.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cloudcontrol.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudcontrol.errors.unsupported_action_exception.UnsupportedActionException: <p>The specified resource doesn't support this resource operation.</p>
            capo_cloudcontrol.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudcontrol.types.delete_resource_input.DeleteResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudcontrol.types.delete_resource_output.DeleteResourceOutput"
        ]:
            import capo_cloudcontrol._operations.cloud_api_service.delete_resource

            (
                output,
                http_response,
            ) = await capo_cloudcontrol._operations.cloud_api_service.delete_resource.async_delete_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudcontrol.types.delete_resource_input.DeleteResourceInput = {
            "type_name": type_name,
            "identifier": identifier,
        }
        if type_version_id is not None:
            input_["type_version_id"] = type_version_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
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

    async def get_resource(
        self,
        type_name: "capo_cloudcontrol.types.type_name.TypeName",
        identifier: "capo_cloudcontrol.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "capo_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["capo_cloudcontrol.types.role_arn.RoleArn"] = None,
    ) -> "capo_cloudcontrol.types.get_resource_output.GetResourceOutput":
        """<p>Returns information about the current state of the specified resource. For details, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-read.html">Reading a resource's current state</a>.</p> <p>You can use this action to return information about an existing resource in your account and Amazon Web Services Region, whether those resources were provisioned using Cloud Control API.</p>

        Args:
            type_name: <p>The name of the resource type.</p>
            type_version_id: <p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers">handlers</a> </code> section of the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            identifier: <p>The identifier for the resource.</p> <p>You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Primary identifiers can be specified as a string or JSON; secondary identifiers must be specified as JSON.</p> <p>For compound primary identifiers (that is, one that consists of multiple resource properties strung together), to specify the primary identifier as a string, list the property values <i>in the order they are specified</i> in the primary identifier definition, separated by <code>|</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html">Identifying resources</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>

        Raises:
            capo_cloudcontrol.errors.already_exists_exception.AlreadyExistsException: <p>The resource with the name requested already exists.</p>
            capo_cloudcontrol.errors.general_service_exception.GeneralServiceException: <p>The resource handler has returned that the downstream service generated an error that doesn't map to any other handler error code.</p>
            capo_cloudcontrol.errors.handler_failure_exception.HandlerFailureException: <p>The resource handler has failed without a returning a more specific error code. This can include timeouts.</p>
            capo_cloudcontrol.errors.handler_internal_failure_exception.HandlerInternalFailureException: <p>The resource handler has returned that an unexpected error occurred within the resource handler.</p>
            capo_cloudcontrol.errors.invalid_credentials_exception.InvalidCredentialsException: <p>The resource handler has returned that the credentials provided by the user are invalid.</p>
            capo_cloudcontrol.errors.invalid_request_exception.InvalidRequestException: <p>The resource handler has returned that invalid input from the user has generated a generic exception.</p>
            capo_cloudcontrol.errors.network_failure_exception.NetworkFailureException: <p>The resource handler has returned that the request couldn't be completed due to networking issues, such as a failure to receive a response from the server.</p>
            capo_cloudcontrol.errors.not_stabilized_exception.NotStabilizedException: <p>The resource handler has returned that the downstream resource failed to complete all of its ready-state checks.</p>
            capo_cloudcontrol.errors.not_updatable_exception.NotUpdatableException: <p>One or more properties included in this resource operation are defined as create-only, and therefore can't be updated.</p>
            capo_cloudcontrol.errors.private_type_exception.PrivateTypeException: <p>Cloud Control API hasn't received a valid response from the resource handler, due to a configuration error. This includes issues such as the resource handler returning an invalid response, or timing out.</p>
            capo_cloudcontrol.errors.resource_conflict_exception.ResourceConflictException: <p>The resource is temporarily unavailable to be acted upon. For example, if the resource is currently undergoing an operation and can't be acted upon until that operation is finished.</p>
            capo_cloudcontrol.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource with the specified identifier can't be found.</p>
            capo_cloudcontrol.errors.service_internal_error_exception.ServiceInternalErrorException: <p>The resource handler has returned that the downstream service returned an internal error, typically with a <code>5XX HTTP</code> status code.</p>
            capo_cloudcontrol.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The resource handler has returned that a non-transient resource limit was reached on the service side.</p>
            capo_cloudcontrol.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cloudcontrol.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudcontrol.errors.unsupported_action_exception.UnsupportedActionException: <p>The specified resource doesn't support this resource operation.</p>
            capo_cloudcontrol.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudcontrol.types.get_resource_input.GetResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudcontrol.types.get_resource_output.GetResourceOutput"
        ]:
            import capo_cloudcontrol._operations.cloud_api_service.get_resource

            (
                output,
                http_response,
            ) = await capo_cloudcontrol._operations.cloud_api_service.get_resource.async_get_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudcontrol.types.get_resource_input.GetResourceInput = {
            "type_name": type_name,
            "identifier": identifier,
        }
        if type_version_id is not None:
            input_["type_version_id"] = type_version_id
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_request_status(
        self,
        request_token: "capo_cloudcontrol.types.request_token.RequestToken",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
    ) -> "capo_cloudcontrol.types.get_resource_request_status_output.GetResourceRequestStatusOutput":
        """<p>Returns the current status of a resource operation request. For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-track">Tracking the progress of resource operation requests</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>

        Args:
            request_token: <p>A unique token used to track the progress of the resource operation request.</p> <p>Request tokens are included in the <code>ProgressEvent</code> type returned by a resource operation request.</p>

        Raises:
            capo_cloudcontrol.errors.request_token_not_found_exception.RequestTokenNotFoundException: <p>A resource operation with the specified request token can't be found.</p>
            capo_cloudcontrol.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudcontrol.types.get_resource_request_status_input.GetResourceRequestStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudcontrol.types.get_resource_request_status_output.GetResourceRequestStatusOutput"
        ]:
            import capo_cloudcontrol._operations.cloud_api_service.get_resource_request_status

            (
                output,
                http_response,
            ) = await capo_cloudcontrol._operations.cloud_api_service.get_resource_request_status.async_get_resource_request_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudcontrol.types.get_resource_request_status_input.GetResourceRequestStatusInput = {
            "request_token": request_token
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_resource_requests(
        self,
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        max_results: Optional["capo_cloudcontrol.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_cloudcontrol.types.next_token.NextToken"] = None,
        resource_request_status_filter: Optional[
            "capo_cloudcontrol.types.resource_request_status_filter.ResourceRequestStatusFilter"
        ] = None,
    ) -> "capo_cloudcontrol.types.list_resource_requests_output.ListResourceRequestsOutput":
        """<p>Returns existing resource operation requests. This includes requests of all status types. For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-list">Listing active resource operation requests</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <note> <p>Resource operation requests expire after 7 days.</p> </note>

        Args:
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p> <p>The default is <code>20</code>.</p>
            next_token: <p>If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.</p>
            resource_request_status_filter: <p>The filter criteria to apply to the requests returned.</p>

        Raises:
            capo_cloudcontrol.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudcontrol.types.list_resource_requests_input.ListResourceRequestsInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudcontrol.types.list_resource_requests_output.ListResourceRequestsOutput"
        ]:
            import capo_cloudcontrol._operations.cloud_api_service.list_resource_requests

            (
                output,
                http_response,
            ) = await capo_cloudcontrol._operations.cloud_api_service.list_resource_requests.async_list_resource_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudcontrol.types.list_resource_requests_input.ListResourceRequestsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_request_status_filter is not None:
            input_["resource_request_status_filter"] = resource_request_status_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resource_requests(
        self,
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        max_results: Optional["capo_cloudcontrol.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_cloudcontrol.types.next_token.NextToken"] = None,
        resource_request_status_filter: Optional[
            "capo_cloudcontrol.types.resource_request_status_filter.ResourceRequestStatusFilter"
        ] = None,
    ) -> "AsyncIterator[capo_cloudcontrol.types.progress_event.ProgressEvent]":
        _token = next_token
        while True:
            _response = await self.list_resource_requests(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                resource_request_status_filter=resource_request_status_filter,
            )
            _page = _resolve_path(_response, ("resource_request_status_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resources(
        self,
        type_name: "capo_cloudcontrol.types.type_name.TypeName",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "capo_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["capo_cloudcontrol.types.role_arn.RoleArn"] = None,
        next_token: Optional[
            "capo_cloudcontrol.types.handler_next_token.HandlerNextToken"
        ] = None,
        max_results: Optional["capo_cloudcontrol.types.max_results.MaxResults"] = None,
        resource_model: Optional[
            "capo_cloudcontrol.types.properties.Properties"
        ] = None,
    ) -> "capo_cloudcontrol.types.list_resources_output.ListResourcesOutput":
        """<p>Returns information about the specified resources. For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-list.html">Discovering resources</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>You can use this action to return information about existing resources in your account and Amazon Web Services Region, whether those resources were provisioned using Cloud Control API.</p>

        Args:
            type_name: <p>The name of the resource type.</p>
            type_version_id: <p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers">handlers</a> </code> section of the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            next_token: <p>If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.</p>
            max_results: <p>Reserved.</p>
            resource_model: <p>The resource model to use to select the resources to return.</p>

        Raises:
            capo_cloudcontrol.errors.already_exists_exception.AlreadyExistsException: <p>The resource with the name requested already exists.</p>
            capo_cloudcontrol.errors.general_service_exception.GeneralServiceException: <p>The resource handler has returned that the downstream service generated an error that doesn't map to any other handler error code.</p>
            capo_cloudcontrol.errors.handler_failure_exception.HandlerFailureException: <p>The resource handler has failed without a returning a more specific error code. This can include timeouts.</p>
            capo_cloudcontrol.errors.handler_internal_failure_exception.HandlerInternalFailureException: <p>The resource handler has returned that an unexpected error occurred within the resource handler.</p>
            capo_cloudcontrol.errors.invalid_credentials_exception.InvalidCredentialsException: <p>The resource handler has returned that the credentials provided by the user are invalid.</p>
            capo_cloudcontrol.errors.invalid_request_exception.InvalidRequestException: <p>The resource handler has returned that invalid input from the user has generated a generic exception.</p>
            capo_cloudcontrol.errors.network_failure_exception.NetworkFailureException: <p>The resource handler has returned that the request couldn't be completed due to networking issues, such as a failure to receive a response from the server.</p>
            capo_cloudcontrol.errors.not_stabilized_exception.NotStabilizedException: <p>The resource handler has returned that the downstream resource failed to complete all of its ready-state checks.</p>
            capo_cloudcontrol.errors.not_updatable_exception.NotUpdatableException: <p>One or more properties included in this resource operation are defined as create-only, and therefore can't be updated.</p>
            capo_cloudcontrol.errors.private_type_exception.PrivateTypeException: <p>Cloud Control API hasn't received a valid response from the resource handler, due to a configuration error. This includes issues such as the resource handler returning an invalid response, or timing out.</p>
            capo_cloudcontrol.errors.resource_conflict_exception.ResourceConflictException: <p>The resource is temporarily unavailable to be acted upon. For example, if the resource is currently undergoing an operation and can't be acted upon until that operation is finished.</p>
            capo_cloudcontrol.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource with the specified identifier can't be found.</p>
            capo_cloudcontrol.errors.service_internal_error_exception.ServiceInternalErrorException: <p>The resource handler has returned that the downstream service returned an internal error, typically with a <code>5XX HTTP</code> status code.</p>
            capo_cloudcontrol.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The resource handler has returned that a non-transient resource limit was reached on the service side.</p>
            capo_cloudcontrol.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cloudcontrol.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudcontrol.errors.unsupported_action_exception.UnsupportedActionException: <p>The specified resource doesn't support this resource operation.</p>
            capo_cloudcontrol.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudcontrol.types.list_resources_input.ListResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudcontrol.types.list_resources_output.ListResourcesOutput"
        ]:
            import capo_cloudcontrol._operations.cloud_api_service.list_resources

            (
                output,
                http_response,
            ) = await capo_cloudcontrol._operations.cloud_api_service.list_resources.async_list_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudcontrol.types.list_resources_input.ListResourcesInput = {
            "type_name": type_name
        }
        if type_version_id is not None:
            input_["type_version_id"] = type_version_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resource_model is not None:
            input_["resource_model"] = resource_model

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resources(
        self,
        type_name: "capo_cloudcontrol.types.type_name.TypeName",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "capo_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["capo_cloudcontrol.types.role_arn.RoleArn"] = None,
        next_token: Optional[
            "capo_cloudcontrol.types.handler_next_token.HandlerNextToken"
        ] = None,
        max_results: Optional["capo_cloudcontrol.types.max_results.MaxResults"] = None,
        resource_model: Optional[
            "capo_cloudcontrol.types.properties.Properties"
        ] = None,
    ) -> "AsyncIterator[capo_cloudcontrol.types.resource_description.ResourceDescription]":
        _token = next_token
        while True:
            _response = await self.list_resources(
                type_name,
                config_overrides=config_overrides,
                type_version_id=type_version_id,
                role_arn=role_arn,
                next_token=_token,
                max_results=max_results,
                resource_model=resource_model,
            )
            _page = _resolve_path(_response, ("resource_descriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_resource(
        self,
        type_name: "capo_cloudcontrol.types.type_name.TypeName",
        identifier: "capo_cloudcontrol.types.identifier.Identifier",
        patch_document: "capo_cloudcontrol.types.patch_document.PatchDocument",
        *,
        config_overrides: Optional[AsyncCloudControlClientConfig] = None,
        type_version_id: Optional[
            "capo_cloudcontrol.types.type_version_id.TypeVersionId"
        ] = None,
        role_arn: Optional["capo_cloudcontrol.types.role_arn.RoleArn"] = None,
        client_token: Optional[
            "capo_cloudcontrol.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_cloudcontrol.types.update_resource_output.UpdateResourceOutput":
        """<p>Updates the specified property values in the resource.</p> <p>You specify your resource property updates as a list of patch operations contained in a JSON patch document that adheres to the <a href="https://datatracker.ietf.org/doc/html/rfc6902"> <i>RFC 6902 - JavaScript Object Notation (JSON) Patch</i> </a> standard.</p> <p>For details on how Cloud Control API performs resource update operations, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-update.html">Updating a resource</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p> <p>After you have initiated a resource update request, you can monitor the progress of your request by calling <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html">GetResourceRequestStatus</a> using the <code>RequestToken</code> of the <code>ProgressEvent</code> returned by <code>UpdateResource</code>.</p> <p>For more information about the properties of a specific resource, refer to the related topic for the resource in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Resource and property types reference</a> in the <i>CloudFormation Users Guide</i>.</p>

        Args:
            type_name: <p>The name of the resource type.</p>
            type_version_id: <p>For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the <code> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers">handlers</a> </code> section of the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">resource type definition schema</a>.</p> <p>If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions">Specifying credentials</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            client_token: <p>A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately distinguish between request retries and new resource requests. You might retry a resource request to ensure that it was successfully received.</p> <p>A client token is valid for 36 hours once used. After that, a resource request with the same client token is treated as a new request.</p> <p>If you do not specify a client token, one is generated for inclusion in the request.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-idempotency">Ensuring resource operation requests are unique</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            identifier: <p>The identifier for the resource.</p> <p>You can specify the primary identifier, or any secondary identifier defined for the resource type in its resource schema. You can only specify one identifier. Primary identifiers can be specified as a string or JSON; secondary identifiers must be specified as JSON.</p> <p>For compound primary identifiers (that is, one that consists of multiple resource properties strung together), to specify the primary identifier as a string, list the property values <i>in the order they are specified</i> in the primary identifier definition, separated by <code>|</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html">Identifying resources</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>
            patch_document: <p>A JavaScript Object Notation (JSON) document listing the patch operations that represent the updates to apply to the current resource properties. For details, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-update.html#resource-operations-update-patch">Composing the patch document</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>

        Raises:
            capo_cloudcontrol.errors.already_exists_exception.AlreadyExistsException: <p>The resource with the name requested already exists.</p>
            capo_cloudcontrol.errors.client_token_conflict_exception.ClientTokenConflictException: <p>The specified client token has already been used in another resource request.</p> <p>It's best practice for client tokens to be unique for each resource operation request. However, client token expire after 36 hours.</p>
            capo_cloudcontrol.errors.concurrent_operation_exception.ConcurrentOperationException: <p>Another resource operation is currently being performed on this resource.</p>
            capo_cloudcontrol.errors.general_service_exception.GeneralServiceException: <p>The resource handler has returned that the downstream service generated an error that doesn't map to any other handler error code.</p>
            capo_cloudcontrol.errors.handler_failure_exception.HandlerFailureException: <p>The resource handler has failed without a returning a more specific error code. This can include timeouts.</p>
            capo_cloudcontrol.errors.handler_internal_failure_exception.HandlerInternalFailureException: <p>The resource handler has returned that an unexpected error occurred within the resource handler.</p>
            capo_cloudcontrol.errors.invalid_credentials_exception.InvalidCredentialsException: <p>The resource handler has returned that the credentials provided by the user are invalid.</p>
            capo_cloudcontrol.errors.invalid_request_exception.InvalidRequestException: <p>The resource handler has returned that invalid input from the user has generated a generic exception.</p>
            capo_cloudcontrol.errors.network_failure_exception.NetworkFailureException: <p>The resource handler has returned that the request couldn't be completed due to networking issues, such as a failure to receive a response from the server.</p>
            capo_cloudcontrol.errors.not_stabilized_exception.NotStabilizedException: <p>The resource handler has returned that the downstream resource failed to complete all of its ready-state checks.</p>
            capo_cloudcontrol.errors.not_updatable_exception.NotUpdatableException: <p>One or more properties included in this resource operation are defined as create-only, and therefore can't be updated.</p>
            capo_cloudcontrol.errors.private_type_exception.PrivateTypeException: <p>Cloud Control API hasn't received a valid response from the resource handler, due to a configuration error. This includes issues such as the resource handler returning an invalid response, or timing out.</p>
            capo_cloudcontrol.errors.resource_conflict_exception.ResourceConflictException: <p>The resource is temporarily unavailable to be acted upon. For example, if the resource is currently undergoing an operation and can't be acted upon until that operation is finished.</p>
            capo_cloudcontrol.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource with the specified identifier can't be found.</p>
            capo_cloudcontrol.errors.service_internal_error_exception.ServiceInternalErrorException: <p>The resource handler has returned that the downstream service returned an internal error, typically with a <code>5XX HTTP</code> status code.</p>
            capo_cloudcontrol.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The resource handler has returned that a non-transient resource limit was reached on the service side.</p>
            capo_cloudcontrol.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cloudcontrol.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudcontrol.errors.unsupported_action_exception.UnsupportedActionException: <p>The specified resource doesn't support this resource operation.</p>
            capo_cloudcontrol.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cloudcontrol.types.update_resource_input.UpdateResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_cloudcontrol.types.update_resource_output.UpdateResourceOutput"
        ]:
            import capo_cloudcontrol._operations.cloud_api_service.update_resource

            (
                output,
                http_response,
            ) = await capo_cloudcontrol._operations.cloud_api_service.update_resource.async_update_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudcontrol.types.update_resource_input.UpdateResourceInput = {
            "type_name": type_name,
            "identifier": identifier,
            "patch_document": patch_document,
        }
        if type_version_id is not None:
            input_["type_version_id"] = type_version_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
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
