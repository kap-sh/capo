"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#DynamoDBStreams_20120810``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_dynamodb_streams._auth._signers
import capo_dynamodb_streams._auth._sigv4
from capo_dynamodb_streams._auth._identity import Credentials
from capo_dynamodb_streams._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_dynamodb_streams._auth._zapros_handler import AuthMiddleware
from capo_dynamodb_streams._services._aws_config import aws_config
from capo_dynamodb_streams._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.describe_stream_input
    import capo_dynamodb_streams.types.describe_stream_output
    import capo_dynamodb_streams.types.get_records_input
    import capo_dynamodb_streams.types.get_records_output
    import capo_dynamodb_streams.types.get_shard_iterator_input
    import capo_dynamodb_streams.types.get_shard_iterator_output
    import capo_dynamodb_streams.types.list_streams_input
    import capo_dynamodb_streams.types.list_streams_output
    import capo_dynamodb_streams.types.positive_integer_object
    import capo_dynamodb_streams.types.sequence_number
    import capo_dynamodb_streams.types.shard_filter
    import capo_dynamodb_streams.types.shard_id
    import capo_dynamodb_streams.types.shard_iterator
    import capo_dynamodb_streams.types.shard_iterator_type
    import capo_dynamodb_streams.types.stream_arn
    import capo_dynamodb_streams.types.table_name


class DynamoDBStreamsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class DynamoDBStreamsClient:
    """A client for the ``DynamoDBStreams`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = DynamoDBStreamsClientConfig(
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
        self, config_overrides: Optional[DynamoDBStreamsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DynamoDBStreamsClientConfig = config_overrides or {}
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

    def describe_stream(
        self,
        stream_arn: "capo_dynamodb_streams.types.stream_arn.StreamArn",
        *,
        config_overrides: Optional[DynamoDBStreamsClientConfig] = None,
        limit: Optional[
            "capo_dynamodb_streams.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        exclusive_start_shard_id: Optional[
            "capo_dynamodb_streams.types.shard_id.ShardId"
        ] = None,
        shard_filter: Optional[
            "capo_dynamodb_streams.types.shard_filter.ShardFilter"
        ] = None,
    ) -> "capo_dynamodb_streams.types.describe_stream_output.DescribeStreamOutput":
        """<p>Returns information about a stream, including the current status of the stream, its Amazon Resource Name (ARN), the composition of its shards, and its corresponding DynamoDB table.</p> <note> <p>You can call <code>DescribeStream</code> at a maximum rate of 10 times per second.</p> </note> <p>Each shard in the stream has a <code>SequenceNumberRange</code> associated with it. If the <code>SequenceNumberRange</code> has a <code>StartingSequenceNumber</code> but no <code>EndingSequenceNumber</code>, then the shard is still open (able to receive more stream records). If both <code>StartingSequenceNumber</code> and <code>EndingSequenceNumber</code> are present, then that shard is closed and can no longer receive more data.</p>

        Args:
            stream_arn: <p>The Amazon Resource Name (ARN) for the stream.</p>
            limit: <p>The maximum number of shard objects to return. The upper limit is 100.</p>
            exclusive_start_shard_id: <p>The shard ID of the first item that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedShardId</code> in the previous operation. </p>
            shard_filter: <p>This optional field contains the filter definition for the <code>DescribeStream</code> API.</p>

        Raises:
            capo_dynamodb_streams.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb_streams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb_streams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb_streams.types.describe_stream_input.DescribeStreamInput]",
        ) -> OperationResponse[
            "capo_dynamodb_streams.types.describe_stream_output.DescribeStreamOutput"
        ]:
            import capo_dynamodb_streams._operations.dynamo_db_streams_20120810.describe_stream

            output, http_response = (
                capo_dynamodb_streams._operations.dynamo_db_streams_20120810.describe_stream.describe_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb_streams.types.describe_stream_input.DescribeStreamInput = {
            "stream_arn": stream_arn
        }
        if limit is not None:
            input_["limit"] = limit
        if exclusive_start_shard_id is not None:
            input_["exclusive_start_shard_id"] = exclusive_start_shard_id
        if shard_filter is not None:
            input_["shard_filter"] = shard_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_records(
        self,
        shard_iterator: "capo_dynamodb_streams.types.shard_iterator.ShardIterator",
        *,
        config_overrides: Optional[DynamoDBStreamsClientConfig] = None,
        limit: Optional[
            "capo_dynamodb_streams.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
    ) -> "capo_dynamodb_streams.types.get_records_output.GetRecordsOutput":
        """<p>Retrieves the stream records from a given shard.</p> <p>Specify a shard iterator using the <code>ShardIterator</code> parameter. The shard iterator specifies the position in the shard from which you want to start reading stream records sequentially. If there are no stream records available in the portion of the shard that the iterator points to, <code>GetRecords</code> returns an empty list. Note that it might take multiple calls to get to a portion of the shard that contains stream records.</p> <note> <p> <code>GetRecords</code> can retrieve a maximum of 1 MB of data or 1000 stream records, whichever comes first.</p> </note>

        Args:
            shard_iterator: <p>A shard iterator that was retrieved from a previous GetShardIterator operation. This iterator can be used to access the stream records in this shard.</p>
            limit: <p>The maximum number of records to return from the shard. The upper limit is 1000.</p>

        Raises:
            capo_dynamodb_streams.errors.expired_iterator_exception.ExpiredIteratorException: <p>The shard iterator has expired and can no longer be used to retrieve stream records. A shard iterator expires 15 minutes after it is retrieved using the <code>GetShardIterator</code> action.</p>
            capo_dynamodb_streams.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb_streams.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb_streams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb_streams.errors.trimmed_data_access_exception.TrimmedDataAccessException: <p>The operation attempted to read past the oldest stream record in a shard.</p> <p>In DynamoDB Streams, there is a 24 hour limit on data retention. Stream records whose age exceeds this limit are subject to removal (trimming) from the stream. You might receive a TrimmedDataAccessException if:</p> <ul> <li> <p>You request a shard iterator with a sequence number older than the trim point (24 hours).</p> </li> <li> <p>You obtain a shard iterator, but before you use the iterator in a <code>GetRecords</code> request, a stream record in the shard exceeds the 24 hour period and is trimmed. This causes the iterator to access a record that no longer exists.</p> </li> </ul>
            capo_dynamodb_streams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb_streams.types.get_records_input.GetRecordsInput]",
        ) -> OperationResponse[
            "capo_dynamodb_streams.types.get_records_output.GetRecordsOutput"
        ]:
            import capo_dynamodb_streams._operations.dynamo_db_streams_20120810.get_records

            output, http_response = (
                capo_dynamodb_streams._operations.dynamo_db_streams_20120810.get_records.get_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb_streams.types.get_records_input.GetRecordsInput = {
            "shard_iterator": shard_iterator
        }
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_shard_iterator(
        self,
        stream_arn: "capo_dynamodb_streams.types.stream_arn.StreamArn",
        shard_id: "capo_dynamodb_streams.types.shard_id.ShardId",
        shard_iterator_type: "capo_dynamodb_streams.types.shard_iterator_type.ShardIteratorType",
        *,
        config_overrides: Optional[DynamoDBStreamsClientConfig] = None,
        sequence_number: Optional[
            "capo_dynamodb_streams.types.sequence_number.SequenceNumber"
        ] = None,
    ) -> "capo_dynamodb_streams.types.get_shard_iterator_output.GetShardIteratorOutput":
        """<p>Returns a shard iterator. A shard iterator provides information about how to retrieve the stream records from within a shard. Use the shard iterator in a subsequent <code>GetRecords</code> request to read the stream records from the shard.</p> <note> <p>A shard iterator expires 15 minutes after it is returned to the requester.</p> </note>

        Args:
            stream_arn: <p>The Amazon Resource Name (ARN) for the stream.</p>
            shard_id: <p>The identifier of the shard. The iterator will be returned for this shard ID.</p>
            shard_iterator_type: <p>Determines how the shard iterator is used to start reading stream records from the shard:</p> <ul> <li> <p> <code>AT_SEQUENCE_NUMBER</code> - Start reading exactly from the position denoted by a specific sequence number.</p> </li> <li> <p> <code>AFTER_SEQUENCE_NUMBER</code> - Start reading right after the position denoted by a specific sequence number.</p> </li> <li> <p> <code>TRIM_HORIZON</code> - Start reading at the last (untrimmed) stream record, which is the oldest record in the shard. In DynamoDB Streams, there is a 24 hour limit on data retention. Stream records whose age exceeds this limit are subject to removal (trimming) from the stream.</p> </li> <li> <p> <code>LATEST</code> - Start reading just after the most recent stream record in the shard, so that you always read the most recent data in the shard.</p> </li> </ul>
            sequence_number: <p>The sequence number of a stream record in the shard from which to start reading.</p>

        Raises:
            capo_dynamodb_streams.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb_streams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb_streams.errors.trimmed_data_access_exception.TrimmedDataAccessException: <p>The operation attempted to read past the oldest stream record in a shard.</p> <p>In DynamoDB Streams, there is a 24 hour limit on data retention. Stream records whose age exceeds this limit are subject to removal (trimming) from the stream. You might receive a TrimmedDataAccessException if:</p> <ul> <li> <p>You request a shard iterator with a sequence number older than the trim point (24 hours).</p> </li> <li> <p>You obtain a shard iterator, but before you use the iterator in a <code>GetRecords</code> request, a stream record in the shard exceeds the 24 hour period and is trimmed. This causes the iterator to access a record that no longer exists.</p> </li> </ul>
            capo_dynamodb_streams.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To obtain a shard iterator for the provided stream ARN and shard ID
            The following example returns a shard iterator for the provided stream ARN and shard ID.

            >>> client.get_shard_iterator(stream_arn='arn:aws:dynamodb:us-west-2:111122223333:table/Forum/stream/2015-05-20T20:51:10.252', shard_id='00000001414576573621-f55eea83', shard_iterator_type='TRIM_HORIZON')
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb_streams.types.get_shard_iterator_input.GetShardIteratorInput]",
        ) -> OperationResponse[
            "capo_dynamodb_streams.types.get_shard_iterator_output.GetShardIteratorOutput"
        ]:
            import capo_dynamodb_streams._operations.dynamo_db_streams_20120810.get_shard_iterator

            output, http_response = (
                capo_dynamodb_streams._operations.dynamo_db_streams_20120810.get_shard_iterator.get_shard_iterator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb_streams.types.get_shard_iterator_input.GetShardIteratorInput = {
            "stream_arn": stream_arn,
            "shard_id": shard_id,
            "shard_iterator_type": shard_iterator_type,
        }
        if sequence_number is not None:
            input_["sequence_number"] = sequence_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_streams(
        self,
        *,
        config_overrides: Optional[DynamoDBStreamsClientConfig] = None,
        table_name: Optional["capo_dynamodb_streams.types.table_name.TableName"] = None,
        limit: Optional[
            "capo_dynamodb_streams.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        exclusive_start_stream_arn: Optional[
            "capo_dynamodb_streams.types.stream_arn.StreamArn"
        ] = None,
    ) -> "capo_dynamodb_streams.types.list_streams_output.ListStreamsOutput":
        """<p>Returns an array of stream ARNs associated with the current account and endpoint. If the <code>TableName</code> parameter is present, then <code>ListStreams</code> will return only the streams ARNs for that table.</p> <note> <p>You can call <code>ListStreams</code> at a maximum rate of 5 times per second.</p> </note>

        Args:
            table_name: <p>If this parameter is provided, then only the streams associated with this table name are returned.</p>
            limit: <p>The maximum number of streams to return. The upper limit is 100.</p>
            exclusive_start_stream_arn: <p>The ARN (Amazon Resource Name) of the first item that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedStreamArn</code> in the previous operation. </p>

        Raises:
            capo_dynamodb_streams.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb_streams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb_streams.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list all of the stream ARNs
            The following example lists all of the stream ARNs.

            >>> client.list_streams()
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb_streams.types.list_streams_input.ListStreamsInput]",
        ) -> OperationResponse[
            "capo_dynamodb_streams.types.list_streams_output.ListStreamsOutput"
        ]:
            import capo_dynamodb_streams._operations.dynamo_db_streams_20120810.list_streams

            output, http_response = (
                capo_dynamodb_streams._operations.dynamo_db_streams_20120810.list_streams.list_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb_streams.types.list_streams_input.ListStreamsInput = {}
        if table_name is not None:
            input_["table_name"] = table_name
        if limit is not None:
            input_["limit"] = limit
        if exclusive_start_stream_arn is not None:
            input_["exclusive_start_stream_arn"] = exclusive_start_stream_arn

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
