from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_pipes._auth._signers
import capo_pipes._auth._sigv4
from capo_pipes._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
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
    import capo_pipes.types.next_token
    import capo_pipes.types.optional_arn
    import capo_pipes.types.pipe
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
    import capo_pipes.types.tag_map
    import capo_pipes.types.update_pipe_request
    import capo_pipes.types.update_pipe_response
    import capo_pipes.types.update_pipe_source_parameters
    from capo_pipes._services.async_pipes import (
        AsyncPipesClient,
        AsyncPipesClientConfig,
    )
    from capo_pipes._services.pipes import PipesClient, PipesClientConfig


class PipeResource:
    def __init__(self, service: PipesClient) -> None:
        self._service = service

    def put(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def update(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pipes.types.delete_pipe_request.DeletePipeRequest = {"name": name}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pipes.types.stop_pipe_request.StopPipeRequest = {"name": name}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPipeResource:
    def __init__(self, service: AsyncPipesClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        source: "capo_pipes.types.arn_or_url.ArnOrUrl",
        target: "capo_pipes.types.arn.Arn",
        role_arn: "capo_pipes.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_pipes.types.create_pipe_request.CreatePipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pipes.types.create_pipe_response.CreatePipeResponse"
        ]:
            import capo_pipes._operations.pipes.create_pipe

            (
                output,
                http_response,
            ) = await capo_pipes._operations.pipes.create_pipe.async_create_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_pipes.types.describe_pipe_request.DescribePipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pipes.types.describe_pipe_response.DescribePipeResponse"
        ]:
            import capo_pipes._operations.pipes.describe_pipe

            (
                output,
                http_response,
            ) = await capo_pipes._operations.pipes.describe_pipe.async_describe_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pipes.types.describe_pipe_request.DescribePipeRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        role_arn: "capo_pipes.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_pipes.types.update_pipe_request.UpdatePipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pipes.types.update_pipe_response.UpdatePipeResponse"
        ]:
            import capo_pipes._operations.pipes.update_pipe

            (
                output,
                http_response,
            ) = await capo_pipes._operations.pipes.update_pipe.async_update_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_pipes.types.delete_pipe_request.DeletePipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pipes.types.delete_pipe_response.DeletePipeResponse"
        ]:
            import capo_pipes._operations.pipes.delete_pipe

            (
                output,
                http_response,
            ) = await capo_pipes._operations.pipes.delete_pipe.async_delete_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pipes.types.delete_pipe_request.DeletePipeRequest = {"name": name}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_pipes.types.list_pipes_request.ListPipesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pipes.types.list_pipes_response.ListPipesResponse"
        ]:
            import capo_pipes._operations.pipes.list_pipes

            (
                output,
                http_response,
            ) = await capo_pipes._operations.pipes.list_pipes.async_list_pipes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_pipe(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_pipes.types.start_pipe_request.StartPipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pipes.types.start_pipe_response.StartPipeResponse"
        ]:
            import capo_pipes._operations.pipes.start_pipe

            (
                output,
                http_response,
            ) = await capo_pipes._operations.pipes.start_pipe.async_start_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pipes.types.start_pipe_request.StartPipeRequest = {"name": name}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_pipe(
        self,
        name: "capo_pipes.types.pipe_name.PipeName",
        *,
        config_overrides: Optional[AsyncPipesClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_pipes.types.stop_pipe_request.StopPipeRequest]",
        ) -> AsyncOperationResponse[
            "capo_pipes.types.stop_pipe_response.StopPipeResponse"
        ]:
            import capo_pipes._operations.pipes.stop_pipe

            (
                output,
                http_response,
            ) = await capo_pipes._operations.pipes.stop_pipe.async_stop_pipe(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pipes.types.stop_pipe_request.StopPipeRequest = {"name": name}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
