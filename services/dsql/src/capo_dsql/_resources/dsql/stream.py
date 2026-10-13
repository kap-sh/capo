from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_dsql._auth._signers
import capo_dsql._auth._sigv4
from capo_dsql._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_dsql.types.client_token
    import capo_dsql.types.cluster_id
    import capo_dsql.types.create_stream_input
    import capo_dsql.types.create_stream_output
    import capo_dsql.types.delete_stream_input
    import capo_dsql.types.delete_stream_output
    import capo_dsql.types.get_stream_input
    import capo_dsql.types.get_stream_output
    import capo_dsql.types.list_streams_input
    import capo_dsql.types.list_streams_output
    import capo_dsql.types.max_results
    import capo_dsql.types.next_token
    import capo_dsql.types.stream_format
    import capo_dsql.types.stream_id
    import capo_dsql.types.stream_ordering
    import capo_dsql.types.stream_summary
    import capo_dsql.types.tag_map
    import capo_dsql.types.target_definition
    from capo_dsql._services.async_dsql import AsyncDSQLClient, AsyncDSQLClientConfig
    from capo_dsql._services.dsql import DSQLClient, DSQLClientConfig


class Stream:
    def __init__(self, service: DSQLClient) -> None:
        self._service = service

    def create(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        target_definition: "capo_dsql.types.target_definition.TargetDefinition",
        ordering: "capo_dsql.types.stream_ordering.StreamOrdering",
        format: "capo_dsql.types.stream_format.StreamFormat",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        tags: Optional["capo_dsql.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
    ) -> "capo_dsql.types.create_stream_output.CreateStreamOutput":
        """<p>Creates a new change data capture (CDC) stream for a cluster. The stream captures database changes and delivers them to the specified target destination.</p> <p> <b>Required permissions</b> </p> <dl> <dt>dsql:CreateStream</dt> <dd> <p>Permission to create a new stream.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/cluster-id</code> </p> </dd> <dt>iam:PassRole</dt> <dd> <p>Permission to pass the IAM role specified in the target definition to the service.</p> <p>Resources: ARN of the IAM role specified in <code>targetDefinition.kinesis.roleArn</code> </p> </dd> <dt>kms:Decrypt</dt> <dd> <p>Required when the cluster uses a customer managed KMS key (CMK). Permission to decrypt data using the cluster's CMK.</p> <p>Resources: ARN of the KMS key used by the cluster</p> </dd> </dl>

        Args:
            cluster_identifier: <p>The ID of the cluster for which to create the stream.</p>
            target_definition: <p>The target destination configuration for the stream. Contains Kinesis stream configuration including stream ARN and IAM role ARN.</p>
            ordering: <p>The ordering mode for the stream. Determines how change events are ordered when delivered to the target.</p>
            format: <p>The format of the stream records.</p>
            tags: <p>A map of key and value pairs to use to tag your stream.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.create_stream_input.CreateStreamInput]",
        ) -> OperationResponse[
            "capo_dsql.types.create_stream_output.CreateStreamOutput"
        ]:
            import capo_dsql._operations.dsql.create_stream

            output, http_response = (
                capo_dsql._operations.dsql.create_stream.create_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateStream")
        )
        input_: capo_dsql.types.create_stream_input.CreateStreamInput = {
            "cluster_identifier": cluster_identifier,
            "target_definition": target_definition,
            "ordering": ordering,
            "format": format,
        }
        if tags is not None:
            input_["tags"] = tags
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

    def read(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        stream_identifier: "capo_dsql.types.stream_id.StreamId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
    ) -> "capo_dsql.types.get_stream_output.GetStreamOutput":
        """<p>Retrieves information about a stream.</p>

        Args:
            cluster_identifier: <p>The ID of the cluster containing the stream to retrieve.</p>
            stream_identifier: <p>The ID of the stream to retrieve.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.get_stream_input.GetStreamInput]",
        ) -> OperationResponse["capo_dsql.types.get_stream_output.GetStreamOutput"]:
            import capo_dsql._operations.dsql.get_stream

            output, http_response = capo_dsql._operations.dsql.get_stream.get_stream(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetStream")
        )
        input_: capo_dsql.types.get_stream_input.GetStreamInput = {
            "cluster_identifier": cluster_identifier,
            "stream_identifier": stream_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        stream_identifier: "capo_dsql.types.stream_id.StreamId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
    ) -> "capo_dsql.types.delete_stream_output.DeleteStreamOutput":
        """<p>Deletes a stream from a cluster.</p>

        Args:
            cluster_identifier: <p>The ID of the cluster containing the stream to delete.</p>
            stream_identifier: <p>The ID of the stream to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.delete_stream_input.DeleteStreamInput]",
        ) -> OperationResponse[
            "capo_dsql.types.delete_stream_output.DeleteStreamOutput"
        ]:
            import capo_dsql._operations.dsql.delete_stream

            output, http_response = (
                capo_dsql._operations.dsql.delete_stream.delete_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteStream")
        )
        input_: capo_dsql.types.delete_stream_input.DeleteStreamInput = {
            "cluster_identifier": cluster_identifier,
            "stream_identifier": stream_identifier,
        }
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

    def list(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[DSQLClientConfig] = None,
        max_results: Optional["capo_dsql.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dsql.types.next_token.NextToken"] = None,
    ) -> "capo_dsql.types.list_streams_output.ListStreamsOutput":
        """<p>Retrieves information about a list of streams for a cluster.</p>

        Args:
            cluster_identifier: <p>The ID of the cluster for which to list streams.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results. Default: 10.</p>
            next_token: <p>If your initial ListStreams operation returns a nextToken, you can include the returned nextToken in following ListStreams operations, which returns results in the next page.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dsql.types.list_streams_input.ListStreamsInput]",
        ) -> OperationResponse["capo_dsql.types.list_streams_output.ListStreamsOutput"]:
            import capo_dsql._operations.dsql.list_streams

            output, http_response = (
                capo_dsql._operations.dsql.list_streams.list_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListStreams")
        )
        input_: capo_dsql.types.list_streams_input.ListStreamsInput = {
            "cluster_identifier": cluster_identifier
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


class AsyncStream:
    def __init__(self, service: AsyncDSQLClient) -> None:
        self._service = service

    async def create(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        target_definition: "capo_dsql.types.target_definition.TargetDefinition",
        ordering: "capo_dsql.types.stream_ordering.StreamOrdering",
        format: "capo_dsql.types.stream_format.StreamFormat",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
        tags: Optional["capo_dsql.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
    ) -> "capo_dsql.types.create_stream_output.CreateStreamOutput":
        """<p>Creates a new change data capture (CDC) stream for a cluster. The stream captures database changes and delivers them to the specified target destination.</p> <p> <b>Required permissions</b> </p> <dl> <dt>dsql:CreateStream</dt> <dd> <p>Permission to create a new stream.</p> <p>Resources: <code>arn:aws:dsql:region:account-id:cluster/cluster-id</code> </p> </dd> <dt>iam:PassRole</dt> <dd> <p>Permission to pass the IAM role specified in the target definition to the service.</p> <p>Resources: ARN of the IAM role specified in <code>targetDefinition.kinesis.roleArn</code> </p> </dd> <dt>kms:Decrypt</dt> <dd> <p>Required when the cluster uses a customer managed KMS key (CMK). Permission to decrypt data using the cluster's CMK.</p> <p>Resources: ARN of the KMS key used by the cluster</p> </dd> </dl>

        Args:
            cluster_identifier: <p>The ID of the cluster for which to create the stream.</p>
            target_definition: <p>The target destination configuration for the stream. Contains Kinesis stream configuration including stream ARN and IAM role ARN.</p>
            ordering: <p>The ordering mode for the stream. Determines how change events are ordered when delivered to the target.</p>
            format: <p>The format of the stream records.</p>
            tags: <p>A map of key and value pairs to use to tag your stream.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dsql.types.create_stream_input.CreateStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_dsql.types.create_stream_output.CreateStreamOutput"
        ]:
            import capo_dsql._operations.dsql.create_stream

            (
                output,
                http_response,
            ) = await capo_dsql._operations.dsql.create_stream.async_create_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateStream")
        )
        input_: capo_dsql.types.create_stream_input.CreateStreamInput = {
            "cluster_identifier": cluster_identifier,
            "target_definition": target_definition,
            "ordering": ordering,
            "format": format,
        }
        if tags is not None:
            input_["tags"] = tags
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

    async def read(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        stream_identifier: "capo_dsql.types.stream_id.StreamId",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
    ) -> "capo_dsql.types.get_stream_output.GetStreamOutput":
        """<p>Retrieves information about a stream.</p>

        Args:
            cluster_identifier: <p>The ID of the cluster containing the stream to retrieve.</p>
            stream_identifier: <p>The ID of the stream to retrieve.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dsql.types.get_stream_input.GetStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_dsql.types.get_stream_output.GetStreamOutput"
        ]:
            import capo_dsql._operations.dsql.get_stream

            (
                output,
                http_response,
            ) = await capo_dsql._operations.dsql.get_stream.async_get_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetStream")
        )
        input_: capo_dsql.types.get_stream_input.GetStreamInput = {
            "cluster_identifier": cluster_identifier,
            "stream_identifier": stream_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        stream_identifier: "capo_dsql.types.stream_id.StreamId",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
        client_token: Optional["capo_dsql.types.client_token.ClientToken"] = None,
    ) -> "capo_dsql.types.delete_stream_output.DeleteStreamOutput":
        """<p>Deletes a stream from a cluster.</p>

        Args:
            cluster_identifier: <p>The ID of the cluster containing the stream to delete.</p>
            stream_identifier: <p>The ID of the stream to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you don't specify a client token, the Amazon Web Services SDK automatically generates one.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dsql.types.delete_stream_input.DeleteStreamInput]",
        ) -> AsyncOperationResponse[
            "capo_dsql.types.delete_stream_output.DeleteStreamOutput"
        ]:
            import capo_dsql._operations.dsql.delete_stream

            (
                output,
                http_response,
            ) = await capo_dsql._operations.dsql.delete_stream.async_delete_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteStream")
        )
        input_: capo_dsql.types.delete_stream_input.DeleteStreamInput = {
            "cluster_identifier": cluster_identifier,
            "stream_identifier": stream_identifier,
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

    async def list(
        self,
        cluster_identifier: "capo_dsql.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[AsyncDSQLClientConfig] = None,
        max_results: Optional["capo_dsql.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_dsql.types.next_token.NextToken"] = None,
    ) -> "capo_dsql.types.list_streams_output.ListStreamsOutput":
        """<p>Retrieves information about a list of streams for a cluster.</p>

        Args:
            cluster_identifier: <p>The ID of the cluster for which to list streams.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results. Default: 10.</p>
            next_token: <p>If your initial ListStreams operation returns a nextToken, you can include the returned nextToken in following ListStreams operations, which returns results in the next page.</p>

        Raises:
            capo_dsql.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_dsql.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_dsql.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_dsql.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_dsql.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_dsql.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_dsql.types.list_streams_input.ListStreamsInput]",
        ) -> AsyncOperationResponse[
            "capo_dsql.types.list_streams_output.ListStreamsOutput"
        ]:
            import capo_dsql._operations.dsql.list_streams

            (
                output,
                http_response,
            ) = await capo_dsql._operations.dsql.list_streams.async_list_streams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListStreams")
        )
        input_: capo_dsql.types.list_streams_input.ListStreamsInput = {
            "cluster_identifier": cluster_identifier
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
