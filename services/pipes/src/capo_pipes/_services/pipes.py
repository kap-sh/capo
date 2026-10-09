"""Generated from Smithy shape ``com.amazonaws.pipes#Pipes``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_pipes._auth._signers
import capo_pipes._auth._sigv4
from capo_pipes._auth._identity import Credentials
from capo_pipes._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pipes._auth._zapros_handler import AuthMiddleware
from capo_pipes._pagination import resolve_path as _resolve_path
from capo_pipes._resources.pipes.pipe_resource import PipeResource
from capo_pipes._services._aws_config import aws_config
from capo_pipes._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_pipes.types.arn
    import capo_pipes.types.arn_or_url
    import capo_pipes.types.create_pipe_request
    import capo_pipes.types.create_pipe_response
    import capo_pipes.types.delete_pipe_request
    import capo_pipes.types.delete_pipe_response
    import capo_pipes.types.describe_pipe_request
    import capo_pipes.types.describe_pipe_response
    import capo_pipes.types.kms_key_identifier
    import capo_pipes.types.limit_max100
    import capo_pipes.types.list_pipes_request
    import capo_pipes.types.list_pipes_response
    import capo_pipes.types.list_tags_for_resource_request
    import capo_pipes.types.list_tags_for_resource_response
    import capo_pipes.types.next_token
    import capo_pipes.types.optional_arn
    import capo_pipes.types.pipe
    import capo_pipes.types.pipe_arn
    import capo_pipes.types.pipe_description
    import capo_pipes.types.pipe_enrichment_parameters
    import capo_pipes.types.pipe_log_configuration_parameters
    import capo_pipes.types.pipe_name
    import capo_pipes.types.pipe_source_parameters
    import capo_pipes.types.pipe_state
    import capo_pipes.types.pipe_target_parameters
    import capo_pipes.types.requested_pipe_state
    import capo_pipes.types.resource_arn
    import capo_pipes.types.role_arn
    import capo_pipes.types.start_pipe_request
    import capo_pipes.types.start_pipe_response
    import capo_pipes.types.stop_pipe_request
    import capo_pipes.types.stop_pipe_response
    import capo_pipes.types.tag_key_list
    import capo_pipes.types.tag_map
    import capo_pipes.types.tag_resource_request
    import capo_pipes.types.tag_resource_response
    import capo_pipes.types.untag_resource_request
    import capo_pipes.types.untag_resource_response
    import capo_pipes.types.update_pipe_request
    import capo_pipes.types.update_pipe_response
    import capo_pipes.types.update_pipe_source_parameters


class PipesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class PipesClient:
    """A client for the ``Pipes`` service.

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
        self._config = PipesClientConfig(
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
        self.pipe_resource = PipeResource(self)

    def operation_options(
        self, config_overrides: Optional[PipesClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: PipesClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_pipes.types.pipe_arn.PipeArn",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "capo_pipes.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Displays the tags associated with a pipe.</p>

        Args:
            resource_arn: <p>The ARN of the pipe for which you want to view tags.</p>

        Raises:
            capo_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            capo_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            capo_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            capo_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pipes.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_pipes.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_pipes._operations.pipes.list_tags_for_resource

            output, http_response = (
                capo_pipes._operations.pipes.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pipes.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_pipes.types.pipe_arn.PipeArn",
        tags: "capo_pipes.types.tag_map.TagMap",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "capo_pipes.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified pipe. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with a pipe that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the pipe. If you specify a tag key that is already associated with the pipe, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a pipe.</p>

        Args:
            resource_arn: <p>The ARN of the pipe.</p>
            tags: <p>The list of key-value pairs associated with the pipe.</p>

        Raises:
            capo_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            capo_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            capo_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            capo_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pipes.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_pipes.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_pipes._operations.pipes.tag_resource

            output, http_response = (
                capo_pipes._operations.pipes.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pipes.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_pipes.types.pipe_arn.PipeArn",
        tag_keys: "capo_pipes.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "capo_pipes.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified pipes.</p>

        Args:
            resource_arn: <p>The ARN of the pipe.</p>
            tag_keys: <p>The list of tag keys to remove from the pipe.</p>

        Raises:
            capo_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            capo_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            capo_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            capo_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pipes.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_pipes.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_pipes._operations.pipes.untag_resource

            output, http_response = (
                capo_pipes._operations.pipes.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pipes.types.untag_resource_request.UntagResourceRequest = {
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

    def create_pipe(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        source: "capo_pipes.types.arn_or_url.ArnOrUrl",
        target: "capo_pipes.types.arn.Arn",
        role_arn: "capo_pipes.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
        description: Optional[
            "capo_pipes.types.pipe_description.PipeDescription"
        ] = None,
        desired_state: Optional[
            "capo_pipes.types.requested_pipe_state.RequestedPipeState"
        ] = None,
        source_parameters: Optional[
            "capo_pipes.types.pipe_source_parameters.PipeSourceParameters"
        ] = None,
        enrichment: Optional["capo_pipes.types.optional_arn.OptionalArn"] = None,
        enrichment_parameters: Optional[
            "capo_pipes.types.pipe_enrichment_parameters.PipeEnrichmentParameters"
        ] = None,
        target_parameters: Optional[
            "capo_pipes.types.pipe_target_parameters.PipeTargetParameters"
        ] = None,
        tags: Optional["capo_pipes.types.tag_map.TagMap"] = None,
        log_configuration: Optional[
            "capo_pipes.types.pipe_log_configuration_parameters.PipeLogConfigurationParameters"
        ] = None,
        kms_key_identifier: Optional[
            "capo_pipes.types.kms_key_identifier.KmsKeyIdentifier"
        ] = None,
    ) -> "capo_pipes.types.create_pipe_response.CreatePipeResponse":
        """<p>Create a pipe. Amazon EventBridge Pipes connect event sources to targets and reduces the need for specialized knowledge and integration code.</p>

        Args:
            name: <p>The name of the pipe.</p>
            description: <p>A description of the pipe.</p>
            desired_state: <p>The state the pipe should be in.</p>
            source: <p>The ARN of the source resource.</p>
            source_parameters: <p>The parameters required to set up a source for your pipe.</p>
            enrichment: <p>The ARN of the enrichment resource.</p>
            enrichment_parameters: <p>The parameters required to set up enrichment on your pipe.</p>
            target: <p>The ARN of the target resource.</p>
            target_parameters: <p>The parameters required to set up a target for your pipe.</p> <p>For more information about pipe target parameters, including how to use dynamic path parameters, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html">Target parameters</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            role_arn: <p>The ARN of the role that allows the pipe to send data to the target.</p>
            tags: <p>The list of key-value pairs to associate with the pipe.</p>
            log_configuration: <p>The logging configuration settings for the pipe.</p>
            kms_key_identifier: <p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>If you do not specify a customer managed key identifier, EventBridge uses an Amazon Web Services owned key to encrypt pipe data.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html">Managing keys</a> in the <i>Key Management Service Developer Guide</i>. </p>

        Raises:
            capo_pipes.errors.conflict_exception.ConflictException: <p>An action you attempted resulted in an exception.</p>
            capo_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            capo_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            capo_pipes.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota has been exceeded.</p>
            capo_pipes.errors.throttling_exception.ThrottlingException: <p>An action was throttled.</p>
            capo_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            capo_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pipes.types.create_pipe_request.CreatePipeRequest]",
        ) -> OperationResponse[
            "capo_pipes.types.create_pipe_response.CreatePipeResponse"
        ]:
            import capo_pipes._operations.pipes.create_pipe

            output, http_response = (
                capo_pipes._operations.pipes.create_pipe.create_pipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pipes.types.create_pipe_request.CreatePipeRequest = {
            "name": name,
            "source": source,
            "target": target,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if desired_state is not None:
            input_["desired_state"] = desired_state
        if source_parameters is not None:
            input_["source_parameters"] = source_parameters
        if enrichment is not None:
            input_["enrichment"] = enrichment
        if enrichment_parameters is not None:
            input_["enrichment_parameters"] = enrichment_parameters
        if target_parameters is not None:
            input_["target_parameters"] = target_parameters
        if tags is not None:
            input_["tags"] = tags
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_pipe(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "capo_pipes.types.describe_pipe_response.DescribePipeResponse":
        """<p>Get the information about an existing pipe. For more information about pipes, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html">Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name: <p>The name of the pipe.</p>

        Raises:
            capo_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            capo_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            capo_pipes.errors.throttling_exception.ThrottlingException: <p>An action was throttled.</p>
            capo_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            capo_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pipes.types.describe_pipe_request.DescribePipeRequest]",
        ) -> OperationResponse[
            "capo_pipes.types.describe_pipe_response.DescribePipeResponse"
        ]:
            import capo_pipes._operations.pipes.describe_pipe

            output, http_response = (
                capo_pipes._operations.pipes.describe_pipe.describe_pipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pipes.types.describe_pipe_request.DescribePipeRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_pipe(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        role_arn: "capo_pipes.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
        description: Optional[
            "capo_pipes.types.pipe_description.PipeDescription"
        ] = None,
        desired_state: Optional[
            "capo_pipes.types.requested_pipe_state.RequestedPipeState"
        ] = None,
        source_parameters: Optional[
            "capo_pipes.types.update_pipe_source_parameters.UpdatePipeSourceParameters"
        ] = None,
        enrichment: Optional["capo_pipes.types.optional_arn.OptionalArn"] = None,
        enrichment_parameters: Optional[
            "capo_pipes.types.pipe_enrichment_parameters.PipeEnrichmentParameters"
        ] = None,
        target: Optional["capo_pipes.types.arn.Arn"] = None,
        target_parameters: Optional[
            "capo_pipes.types.pipe_target_parameters.PipeTargetParameters"
        ] = None,
        log_configuration: Optional[
            "capo_pipes.types.pipe_log_configuration_parameters.PipeLogConfigurationParameters"
        ] = None,
        kms_key_identifier: Optional[
            "capo_pipes.types.kms_key_identifier.KmsKeyIdentifier"
        ] = None,
    ) -> "capo_pipes.types.update_pipe_response.UpdatePipeResponse":
        """<p>Update an existing pipe. When you call <code>UpdatePipe</code>, EventBridge only the updates fields you have specified in the request; the rest remain unchanged. The exception to this is if you modify any Amazon Web Services-service specific fields in the <code>SourceParameters</code>, <code>EnrichmentParameters</code>, or <code>TargetParameters</code> objects. For example, <code>DynamoDBStreamParameters</code> or <code>EventBridgeEventBusParameters</code>. EventBridge updates the fields in these objects atomically as one and overrides existing values. This is by design, and means that if you don't specify an optional field in one of these <code>Parameters</code> objects, EventBridge sets that field to its system-default value during the update.</p> <p>For more information about pipes, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html"> Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name: <p>The name of the pipe.</p>
            description: <p>A description of the pipe.</p>
            desired_state: <p>The state the pipe should be in.</p>
            source_parameters: <p>The parameters required to set up a source for your pipe.</p>
            enrichment: <p>The ARN of the enrichment resource.</p>
            enrichment_parameters: <p>The parameters required to set up enrichment on your pipe.</p>
            target: <p>The ARN of the target resource.</p>
            target_parameters: <p>The parameters required to set up a target for your pipe.</p> <p>For more information about pipe target parameters, including how to use dynamic path parameters, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html">Target parameters</a> in the <i>Amazon EventBridge User Guide</i>.</p>
            role_arn: <p>The ARN of the role that allows the pipe to send data to the target.</p>
            log_configuration: <p>The logging configuration settings for the pipe.</p>
            kms_key_identifier: <p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>To update a pipe that is using the default Amazon Web Services owned key to use a customer managed key instead, or update a pipe that is using a customer managed key to use a different customer managed key, specify a customer managed key identifier.</p> <p>To update a pipe that is using a customer managed key to use the default Amazon Web Services owned key, specify an empty string.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html">Managing keys</a> in the <i>Key Management Service Developer Guide</i>. </p>

        Raises:
            capo_pipes.errors.conflict_exception.ConflictException: <p>An action you attempted resulted in an exception.</p>
            capo_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            capo_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            capo_pipes.errors.throttling_exception.ThrottlingException: <p>An action was throttled.</p>
            capo_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            capo_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pipes.types.update_pipe_request.UpdatePipeRequest]",
        ) -> OperationResponse[
            "capo_pipes.types.update_pipe_response.UpdatePipeResponse"
        ]:
            import capo_pipes._operations.pipes.update_pipe

            output, http_response = (
                capo_pipes._operations.pipes.update_pipe.update_pipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pipes.types.update_pipe_request.UpdatePipeRequest = {
            "name": name,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if desired_state is not None:
            input_["desired_state"] = desired_state
        if source_parameters is not None:
            input_["source_parameters"] = source_parameters
        if enrichment is not None:
            input_["enrichment"] = enrichment
        if enrichment_parameters is not None:
            input_["enrichment_parameters"] = enrichment_parameters
        if target is not None:
            input_["target"] = target
        if target_parameters is not None:
            input_["target_parameters"] = target_parameters
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_pipe(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "capo_pipes.types.delete_pipe_response.DeletePipeResponse":
        """<p>Delete an existing pipe. For more information about pipes, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html">Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name: <p>The name of the pipe.</p>

        Raises:
            capo_pipes.errors.conflict_exception.ConflictException: <p>An action you attempted resulted in an exception.</p>
            capo_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            capo_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            capo_pipes.errors.throttling_exception.ThrottlingException: <p>An action was throttled.</p>
            capo_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            capo_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pipes.types.delete_pipe_request.DeletePipeRequest]",
        ) -> OperationResponse[
            "capo_pipes.types.delete_pipe_response.DeletePipeResponse"
        ]:
            import capo_pipes._operations.pipes.delete_pipe

            output, http_response = (
                capo_pipes._operations.pipes.delete_pipe.delete_pipe(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pipes.types.delete_pipe_request.DeletePipeRequest = {"name": name}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_pipes(
        self,
        *,
        config_overrides: Optional[PipesClientConfig] = None,
        name_prefix: Optional["capo_pipes.types.pipe_name.PipeName"] = None,
        desired_state: Optional[
            "capo_pipes.types.requested_pipe_state.RequestedPipeState"
        ] = None,
        current_state: Optional["capo_pipes.types.pipe_state.PipeState"] = None,
        source_prefix: Optional["capo_pipes.types.resource_arn.ResourceArn"] = None,
        target_prefix: Optional["capo_pipes.types.resource_arn.ResourceArn"] = None,
        next_token: Optional["capo_pipes.types.next_token.NextToken"] = None,
        limit: Optional["capo_pipes.types.limit_max100.LimitMax100"] = None,
    ) -> "capo_pipes.types.list_pipes_response.ListPipesResponse":
        """<p>Get the pipes associated with this account. For more information about pipes, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html">Amazon EventBridge Pipes</a> in the Amazon EventBridge User Guide.</p>

        Args:
            name_prefix: <p>A value that will return a subset of the pipes associated with this account. For example, <code>"NamePrefix": "ABC"</code> will return all endpoints with "ABC" in the name.</p>
            desired_state: <p>The state the pipe should be in.</p>
            current_state: <p>The state the pipe is in.</p>
            source_prefix: <p>The prefix matching the pipe source.</p>
            target_prefix: <p>The prefix matching the pipe target.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>
            limit: <p>The maximum number of pipes to include in the response.</p>

        Raises:
            capo_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            capo_pipes.errors.throttling_exception.ThrottlingException: <p>An action was throttled.</p>
            capo_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            capo_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pipes.types.list_pipes_request.ListPipesRequest]",
        ) -> OperationResponse[
            "capo_pipes.types.list_pipes_response.ListPipesResponse"
        ]:
            import capo_pipes._operations.pipes.list_pipes

            output, http_response = capo_pipes._operations.pipes.list_pipes.list_pipes(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pipes.types.list_pipes_request.ListPipesRequest = {}
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if desired_state is not None:
            input_["desired_state"] = desired_state
        if current_state is not None:
            input_["current_state"] = current_state
        if source_prefix is not None:
            input_["source_prefix"] = source_prefix
        if target_prefix is not None:
            input_["target_prefix"] = target_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_pipes(
        self,
        *,
        config_overrides: Optional[PipesClientConfig] = None,
        name_prefix: Optional["capo_pipes.types.pipe_name.PipeName"] = None,
        desired_state: Optional[
            "capo_pipes.types.requested_pipe_state.RequestedPipeState"
        ] = None,
        current_state: Optional["capo_pipes.types.pipe_state.PipeState"] = None,
        source_prefix: Optional["capo_pipes.types.resource_arn.ResourceArn"] = None,
        target_prefix: Optional["capo_pipes.types.resource_arn.ResourceArn"] = None,
        next_token: Optional["capo_pipes.types.next_token.NextToken"] = None,
        limit: Optional["capo_pipes.types.limit_max100.LimitMax100"] = None,
    ) -> "Iterator[capo_pipes.types.pipe.Pipe]":
        _token = next_token
        while True:
            _response = self.list_pipes(
                config_overrides=config_overrides,
                name_prefix=name_prefix,
                desired_state=desired_state,
                current_state=current_state,
                source_prefix=source_prefix,
                target_prefix=target_prefix,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("pipes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_pipe(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "capo_pipes.types.start_pipe_response.StartPipeResponse":
        """<p>Start an existing pipe.</p>

        Args:
            name: <p>The name of the pipe.</p>

        Raises:
            capo_pipes.errors.conflict_exception.ConflictException: <p>An action you attempted resulted in an exception.</p>
            capo_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            capo_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            capo_pipes.errors.throttling_exception.ThrottlingException: <p>An action was throttled.</p>
            capo_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            capo_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pipes.types.start_pipe_request.StartPipeRequest]",
        ) -> OperationResponse[
            "capo_pipes.types.start_pipe_response.StartPipeResponse"
        ]:
            import capo_pipes._operations.pipes.start_pipe

            output, http_response = capo_pipes._operations.pipes.start_pipe.start_pipe(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pipes.types.start_pipe_request.StartPipeRequest = {"name": name}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_pipe(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[PipesClientConfig] = None,
    ) -> "capo_pipes.types.stop_pipe_response.StopPipeResponse":
        """<p>Stop an existing pipe.</p>

        Args:
            name: <p>The name of the pipe.</p>

        Raises:
            capo_pipes.errors.conflict_exception.ConflictException: <p>An action you attempted resulted in an exception.</p>
            capo_pipes.errors.internal_exception.InternalException: <p>This exception occurs due to unexpected causes.</p>
            capo_pipes.errors.not_found_exception.NotFoundException: <p>An entity that you specified does not exist.</p>
            capo_pipes.errors.throttling_exception.ThrottlingException: <p>An action was throttled.</p>
            capo_pipes.errors.validation_exception.ValidationException: <p>Indicates that an error has occurred while performing a validate operation.</p>
            capo_pipes.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pipes.types.stop_pipe_request.StopPipeRequest]",
        ) -> OperationResponse["capo_pipes.types.stop_pipe_response.StopPipeResponse"]:
            import capo_pipes._operations.pipes.stop_pipe

            output, http_response = capo_pipes._operations.pipes.stop_pipe.stop_pipe(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pipes.types.stop_pipe_request.StopPipeRequest = {"name": name}

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
