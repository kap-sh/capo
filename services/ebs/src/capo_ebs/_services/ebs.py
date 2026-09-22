"""Generated from Smithy shape ``com.amazonaws.ebs#Ebs``."""

import uuid
import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_ebs._auth._signers
import capo_ebs._auth._sigv4
from capo_ebs._auth._identity import Credentials
from capo_ebs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ebs._auth._zapros_handler import AuthMiddleware
from capo_ebs._body import Body, closing_bodies
from capo_ebs._iter import ensure_sync_iterator
from capo_ebs._pagination import resolve_path as _resolve_path
from capo_ebs._services._aws_config import aws_config
from capo_ebs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_ebs.types.block_data
    import capo_ebs.types.block_index
    import capo_ebs.types.block_token
    import capo_ebs.types.boolean
    import capo_ebs.types.changed_blocks_count
    import capo_ebs.types.checksum
    import capo_ebs.types.checksum_aggregation_method
    import capo_ebs.types.checksum_algorithm
    import capo_ebs.types.complete_snapshot_request
    import capo_ebs.types.complete_snapshot_response
    import capo_ebs.types.data_length
    import capo_ebs.types.description
    import capo_ebs.types.get_snapshot_block_request
    import capo_ebs.types.get_snapshot_block_response
    import capo_ebs.types.idempotency_token
    import capo_ebs.types.kms_key_arn
    import capo_ebs.types.list_changed_blocks_request
    import capo_ebs.types.list_changed_blocks_response
    import capo_ebs.types.list_snapshot_blocks_request
    import capo_ebs.types.list_snapshot_blocks_response
    import capo_ebs.types.max_results
    import capo_ebs.types.page_token
    import capo_ebs.types.progress
    import capo_ebs.types.put_snapshot_block_request
    import capo_ebs.types.put_snapshot_block_response
    import capo_ebs.types.snapshot_id
    import capo_ebs.types.start_snapshot_request
    import capo_ebs.types.start_snapshot_response
    import capo_ebs.types.tags
    import capo_ebs.types.timeout
    import capo_ebs.types.volume_size


class EBSClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class EBSClient:
    """A client for the ``EBS`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = EBSClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[EBSClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: EBSClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def complete_snapshot(
        self,
        snapshot_id: "capo_ebs.types.snapshot_id.SnapshotId",
        changed_blocks_count: "capo_ebs.types.changed_blocks_count.ChangedBlocksCount",
        *,
        config_overrides: Optional[EBSClientConfig] = None,
        checksum: Optional["capo_ebs.types.checksum.Checksum"] = None,
        checksum_algorithm: Optional[
            "capo_ebs.types.checksum_algorithm.ChecksumAlgorithm"
        ] = None,
        checksum_aggregation_method: Optional[
            "capo_ebs.types.checksum_aggregation_method.ChecksumAggregationMethod"
        ] = None,
    ) -> "capo_ebs.types.complete_snapshot_response.CompleteSnapshotResponse":
        r"""<p>Seals and completes the snapshot after all of the required blocks of data have been written to it. Completing the snapshot changes the status to <code>completed</code>. You cannot write new blocks to a snapshot after it has been completed.</p> <note> <p>You should always retry requests that receive server (<code>5xx</code>) error responses, and <code>ThrottlingException</code> and <code>RequestThrottledException</code> client error responses. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </note>

        Args:
            snapshot_id: <p>The ID of the snapshot.</p>
            changed_blocks_count: <p>The number of blocks that were written to the snapshot.</p>
            checksum: <p>An aggregated Base-64 SHA256 checksum based on the checksums of each written block.</p> <p>To generate the aggregated checksum using the linear aggregation method, arrange the checksums for each written block in ascending order of their block index, concatenate them to form a single string, and then generate the checksum on the entire string using the SHA256 algorithm.</p>
            checksum_algorithm: <p>The algorithm used to generate the checksum. Currently, the only supported algorithm is <code>SHA256</code>.</p>
            checksum_aggregation_method: <p>The aggregation method used to generate the checksum. Currently, the only supported aggregation method is <code>LINEAR</code>.</p>

        Raises:
            capo_ebs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ebs.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.request_throttled_exception.RequestThrottledException: <p>The number of API requests has exceeded the maximum allowed API request throttling limit for the snapshot. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_ebs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your current service quotas do not allow you to perform this action.</p>
            capo_ebs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints of the EBS direct APIs.</p>
            capo_ebs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ebs.types.complete_snapshot_request.CompleteSnapshotRequest]",
        ) -> OperationResponse[
            "capo_ebs.types.complete_snapshot_response.CompleteSnapshotResponse"
        ]:
            import capo_ebs._operations.ebs.complete_snapshot

            output, http_response = (
                capo_ebs._operations.ebs.complete_snapshot.complete_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ebs.types.complete_snapshot_request.CompleteSnapshotRequest = {
            "snapshot_id": snapshot_id,
            "changed_blocks_count": changed_blocks_count,
        }
        if checksum is not None:
            input_["checksum"] = checksum
        if checksum_algorithm is not None:
            input_["checksum_algorithm"] = checksum_algorithm
        if checksum_aggregation_method is not None:
            input_["checksum_aggregation_method"] = checksum_aggregation_method

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def get_snapshot_block(
        self,
        snapshot_id: "capo_ebs.types.snapshot_id.SnapshotId",
        block_index: "capo_ebs.types.block_index.BlockIndex",
        block_token: "capo_ebs.types.block_token.BlockToken",
        *,
        config_overrides: Optional[EBSClientConfig] = None,
    ) -> (
        "Generator[capo_ebs.types.get_snapshot_block_response.GetSnapshotBlockResponse]"
    ):
        r"""<p>Returns the data in a block in an Amazon Elastic Block Store snapshot.</p> <note> <p>You should always retry requests that receive server (<code>5xx</code>) error responses, and <code>ThrottlingException</code> and <code>RequestThrottledException</code> client error responses. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </note>

        Args:
            snapshot_id: <p>The ID of the snapshot containing the block from which to get data.</p> <important> <p>If the specified snapshot is encrypted, you must have permission to use the KMS key that was used to encrypt the snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapis-using-encryption.html\"> Using encryption</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </important>
            block_index: <p>The block index of the block in which to read the data. A block index is a logical index in units of <code>512</code> KiB blocks. To identify the block index, divide the logical offset of the data in the logical volume by the block size (logical offset of data/<code>524288</code>). The logical offset of the data must be <code>512</code> KiB aligned.</p>
            block_token: <p>The block token of the block from which to get data. You can obtain the <code>BlockToken</code> by running the <code>ListChangedBlocks</code> or <code>ListSnapshotBlocks</code> operations.</p>

        Raises:
            capo_ebs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ebs.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.request_throttled_exception.RequestThrottledException: <p>The number of API requests has exceeded the maximum allowed API request throttling limit for the snapshot. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_ebs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your current service quotas do not allow you to perform this action.</p>
            capo_ebs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints of the EBS direct APIs.</p>
            capo_ebs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ebs.types.get_snapshot_block_request.GetSnapshotBlockRequest]",
        ) -> OperationResponse[
            "capo_ebs.types.get_snapshot_block_response.GetSnapshotBlockResponse"
        ]:
            import capo_ebs._operations.ebs.get_snapshot_block

            output, http_response = (
                capo_ebs._operations.ebs.get_snapshot_block.get_snapshot_block(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ebs.types.get_snapshot_block_request.GetSnapshotBlockRequest = {
            "snapshot_id": snapshot_id,
            "block_index": block_index,
            "block_token": block_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def list_changed_blocks(
        self,
        second_snapshot_id: "capo_ebs.types.snapshot_id.SnapshotId",
        *,
        config_overrides: Optional[EBSClientConfig] = None,
        first_snapshot_id: Optional["capo_ebs.types.snapshot_id.SnapshotId"] = None,
        next_token: Optional["capo_ebs.types.page_token.PageToken"] = None,
        max_results: Optional["capo_ebs.types.max_results.MaxResults"] = None,
        starting_block_index: Optional["capo_ebs.types.block_index.BlockIndex"] = None,
    ) -> "capo_ebs.types.list_changed_blocks_response.ListChangedBlocksResponse":
        r"""<p>Returns information about the blocks that are different between two Amazon Elastic Block Store snapshots of the same volume/snapshot lineage.</p> <note> <p>You should always retry requests that receive server (<code>5xx</code>) error responses, and <code>ThrottlingException</code> and <code>RequestThrottledException</code> client error responses. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </note>

        Args:
            first_snapshot_id: <p>The ID of the first snapshot to use for the comparison.</p> <important> <p>The <code>FirstSnapshotID</code> parameter must be specified with a <code>SecondSnapshotId</code> parameter; otherwise, an error occurs.</p> </important>
            second_snapshot_id: <p>The ID of the second snapshot to use for the comparison.</p> <important> <p>The <code>SecondSnapshotId</code> parameter must be specified with a <code>FirstSnapshotID</code> parameter; otherwise, an error occurs.</p> </important>
            next_token: <p>The token to request the next page of results.</p> <p>If you specify <b>NextToken</b>, then <b>StartingBlockIndex</b> is ignored.</p>
            max_results: <p>The maximum number of blocks to be returned by the request.</p> <p>Even if additional blocks can be retrieved from the snapshot, the request can return less blocks than <b>MaxResults</b> or an empty array of blocks.</p> <p>To retrieve the next set of blocks from the snapshot, make another request with the returned <b>NextToken</b> value. The value of <b>NextToken</b> is <code>null</code> when there are no more blocks to return.</p>
            starting_block_index: <p>The block index from which the comparison should start.</p> <p>The list in the response will start from this block index or the next valid block index in the snapshots.</p> <p>If you specify <b>NextToken</b>, then <b>StartingBlockIndex</b> is ignored.</p>

        Raises:
            capo_ebs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ebs.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.request_throttled_exception.RequestThrottledException: <p>The number of API requests has exceeded the maximum allowed API request throttling limit for the snapshot. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_ebs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your current service quotas do not allow you to perform this action.</p>
            capo_ebs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints of the EBS direct APIs.</p>
            capo_ebs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ebs.types.list_changed_blocks_request.ListChangedBlocksRequest]",
        ) -> OperationResponse[
            "capo_ebs.types.list_changed_blocks_response.ListChangedBlocksResponse"
        ]:
            import capo_ebs._operations.ebs.list_changed_blocks

            output, http_response = (
                capo_ebs._operations.ebs.list_changed_blocks.list_changed_blocks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ebs.types.list_changed_blocks_request.ListChangedBlocksRequest = {
            "second_snapshot_id": second_snapshot_id
        }
        if first_snapshot_id is not None:
            input_["first_snapshot_id"] = first_snapshot_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if starting_block_index is not None:
            input_["starting_block_index"] = starting_block_index

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_changed_blocks(
        self,
        second_snapshot_id: "capo_ebs.types.snapshot_id.SnapshotId",
        *,
        config_overrides: Optional[EBSClientConfig] = None,
        first_snapshot_id: Optional["capo_ebs.types.snapshot_id.SnapshotId"] = None,
        next_token: Optional["capo_ebs.types.page_token.PageToken"] = None,
        max_results: Optional["capo_ebs.types.max_results.MaxResults"] = None,
        starting_block_index: Optional["capo_ebs.types.block_index.BlockIndex"] = None,
    ) -> "Iterator[capo_ebs.types.list_changed_blocks_response.ListChangedBlocksResponse]":
        _token = next_token
        while True:
            _response = self.list_changed_blocks(
                second_snapshot_id,
                config_overrides=config_overrides,
                first_snapshot_id=first_snapshot_id,
                next_token=_token,
                max_results=max_results,
                starting_block_index=starting_block_index,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_snapshot_blocks(
        self,
        snapshot_id: "capo_ebs.types.snapshot_id.SnapshotId",
        *,
        config_overrides: Optional[EBSClientConfig] = None,
        next_token: Optional["capo_ebs.types.page_token.PageToken"] = None,
        max_results: Optional["capo_ebs.types.max_results.MaxResults"] = None,
        starting_block_index: Optional["capo_ebs.types.block_index.BlockIndex"] = None,
    ) -> "capo_ebs.types.list_snapshot_blocks_response.ListSnapshotBlocksResponse":
        r"""<p>Returns information about the blocks in an Amazon Elastic Block Store snapshot.</p> <note> <p>You should always retry requests that receive server (<code>5xx</code>) error responses, and <code>ThrottlingException</code> and <code>RequestThrottledException</code> client error responses. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </note>

        Args:
            snapshot_id: <p>The ID of the snapshot from which to get block indexes and block tokens.</p>
            next_token: <p>The token to request the next page of results.</p> <p>If you specify <b>NextToken</b>, then <b>StartingBlockIndex</b> is ignored.</p>
            max_results: <p>The maximum number of blocks to be returned by the request.</p> <p>Even if additional blocks can be retrieved from the snapshot, the request can return less blocks than <b>MaxResults</b> or an empty array of blocks.</p> <p>To retrieve the next set of blocks from the snapshot, make another request with the returned <b>NextToken</b> value. The value of <b>NextToken</b> is <code>null</code> when there are no more blocks to return.</p>
            starting_block_index: <p>The block index from which the list should start. The list in the response will start from this block index or the next valid block index in the snapshot.</p> <p>If you specify <b>NextToken</b>, then <b>StartingBlockIndex</b> is ignored.</p>

        Raises:
            capo_ebs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ebs.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.request_throttled_exception.RequestThrottledException: <p>The number of API requests has exceeded the maximum allowed API request throttling limit for the snapshot. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_ebs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your current service quotas do not allow you to perform this action.</p>
            capo_ebs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints of the EBS direct APIs.</p>
            capo_ebs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ebs.types.list_snapshot_blocks_request.ListSnapshotBlocksRequest]",
        ) -> OperationResponse[
            "capo_ebs.types.list_snapshot_blocks_response.ListSnapshotBlocksResponse"
        ]:
            import capo_ebs._operations.ebs.list_snapshot_blocks

            output, http_response = (
                capo_ebs._operations.ebs.list_snapshot_blocks.list_snapshot_blocks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ebs.types.list_snapshot_blocks_request.ListSnapshotBlocksRequest = {
            "snapshot_id": snapshot_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if starting_block_index is not None:
            input_["starting_block_index"] = starting_block_index

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_snapshot_blocks(
        self,
        snapshot_id: "capo_ebs.types.snapshot_id.SnapshotId",
        *,
        config_overrides: Optional[EBSClientConfig] = None,
        next_token: Optional["capo_ebs.types.page_token.PageToken"] = None,
        max_results: Optional["capo_ebs.types.max_results.MaxResults"] = None,
        starting_block_index: Optional["capo_ebs.types.block_index.BlockIndex"] = None,
    ) -> "Iterator[capo_ebs.types.list_snapshot_blocks_response.ListSnapshotBlocksResponse]":
        _token = next_token
        while True:
            _response = self.list_snapshot_blocks(
                snapshot_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                starting_block_index=starting_block_index,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_snapshot_block(
        self,
        snapshot_id: "capo_ebs.types.snapshot_id.SnapshotId",
        block_index: "capo_ebs.types.block_index.BlockIndex",
        block_data: Body[Iterator[bytes]] | Iterator[bytes] | bytes,
        data_length: "capo_ebs.types.data_length.DataLength",
        checksum: "capo_ebs.types.checksum.Checksum",
        checksum_algorithm: "capo_ebs.types.checksum_algorithm.ChecksumAlgorithm",
        *,
        config_overrides: Optional[EBSClientConfig] = None,
        progress: Optional["capo_ebs.types.progress.Progress"] = None,
    ) -> "capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse":
        r"""<p>Writes a block of data to a snapshot. If the specified block contains data, the existing data is overwritten. The target snapshot must be in the <code>pending</code> state.</p> <p>Data written to a snapshot must be aligned with 512-KiB sectors.</p> <note> <p>You should always retry requests that receive server (<code>5xx</code>) error responses, and <code>ThrottlingException</code> and <code>RequestThrottledException</code> client error responses. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </note>

        Args:
            snapshot_id: <p>The ID of the snapshot.</p> <important> <p>If the specified snapshot is encrypted, you must have permission to use the KMS key that was used to encrypt the snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapis-using-encryption.html\"> Using encryption</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>..</p> </important>
            block_index: <p>The block index of the block in which to write the data. A block index is a logical index in units of <code>512</code> KiB blocks. To identify the block index, divide the logical offset of the data in the logical volume by the block size (logical offset of data/<code>524288</code>). The logical offset of the data must be <code>512</code> KiB aligned.</p>
            block_data: <p>The data to write to the block.</p> <p>The block data is not signed as part of the Signature Version 4 signing process. As a result, you must generate and provide a Base64-encoded SHA256 checksum for the block data using the <b>x-amz-Checksum</b> header. Also, you must specify the checksum algorithm using the <b>x-amz-Checksum-Algorithm</b> header. The checksum that you provide is part of the Signature Version 4 signing process. It is validated against a checksum generated by Amazon EBS to ensure the validity and authenticity of the data. If the checksums do not correspond, the request fails. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-accessing-snapshot.html#ebsapis-using-checksums\"> Using checksums with the EBS direct APIs</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>
            data_length: <p>The size of the data to write to the block, in bytes. Currently, the only supported size is <code>524288</code> bytes.</p> <p>Valid values: <code>524288</code> </p>
            progress: <p>The progress of the write process, as a percentage.</p>
            checksum: <p>A Base64-encoded SHA256 checksum of the data. Only SHA256 checksums are supported.</p>
            checksum_algorithm: <p>The algorithm used to generate the checksum. Currently, the only supported algorithm is <code>SHA256</code>.</p>

        Raises:
            capo_ebs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ebs.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.request_throttled_exception.RequestThrottledException: <p>The number of API requests has exceeded the maximum allowed API request throttling limit for the snapshot. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_ebs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your current service quotas do not allow you to perform this action.</p>
            capo_ebs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints of the EBS direct APIs.</p>
            capo_ebs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ebs.types.put_snapshot_block_request.PutSnapshotBlockRequest]",
        ) -> OperationResponse[
            "capo_ebs.types.put_snapshot_block_response.PutSnapshotBlockResponse"
        ]:
            import capo_ebs._operations.ebs.put_snapshot_block

            output, http_response = (
                capo_ebs._operations.ebs.put_snapshot_block.put_snapshot_block(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ebs.types.put_snapshot_block_request.PutSnapshotBlockRequest = {
            "snapshot_id": snapshot_id,
            "block_index": block_index,
            "block_data": ensure_sync_iterator(block_data),
            "data_length": data_length,
            "checksum": checksum,
            "checksum_algorithm": checksum_algorithm,
        }
        if progress is not None:
            input_["progress"] = progress

        with closing_bodies(input_):
            response = execute_pipeline(
                OperationRequest(input=input_, options=options_),
                handler=_handler,
                interceptors=list(interceptors_),
            )
            response.response.close()
            return response.output

    def start_snapshot(
        self,
        volume_size: "capo_ebs.types.volume_size.VolumeSize",
        *,
        config_overrides: Optional[EBSClientConfig] = None,
        parent_snapshot_id: Optional["capo_ebs.types.snapshot_id.SnapshotId"] = None,
        tags: Optional["capo_ebs.types.tags.Tags"] = None,
        description: Optional["capo_ebs.types.description.Description"] = None,
        client_token: Optional[
            "capo_ebs.types.idempotency_token.IdempotencyToken"
        ] = None,
        encrypted: Optional["capo_ebs.types.boolean.Boolean"] = None,
        kms_key_arn: Optional["capo_ebs.types.kms_key_arn.KmsKeyArn"] = None,
        timeout: Optional["capo_ebs.types.timeout.Timeout"] = None,
    ) -> "capo_ebs.types.start_snapshot_response.StartSnapshotResponse":
        r"""<p>Creates a new Amazon EBS snapshot. The new snapshot enters the <code>pending</code> state after the request completes. </p> <p>After creating the snapshot, use <a href=\"https://docs.aws.amazon.com/ebs/latest/APIReference/API_PutSnapshotBlock.html\"> PutSnapshotBlock</a> to write blocks of data to the snapshot.</p> <note> <p>You should always retry requests that receive server (<code>5xx</code>) error responses, and <code>ThrottlingException</code> and <code>RequestThrottledException</code> client error responses. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </note>

        Args:
            volume_size: <p>The size of the volume, in GiB. The maximum size is <code>65536</code> GiB (64 TiB).</p>
            parent_snapshot_id: <p>The ID of the parent snapshot. If there is no parent snapshot, or if you are creating the first snapshot for an on-premises volume, omit this parameter.</p> <p>You can't specify <b>ParentSnapshotId</b> and <b>Encrypted</b> in the same request. If you specify both parameters, the request fails with <code>ValidationException</code>.</p> <p>The encryption status of the snapshot depends on the values that you specify for <b>Encrypted</b>, <b>KmsKeyArn</b>, and <b>ParentSnapshotId</b>, and whether your Amazon Web Services account is enabled for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default\"> encryption by default</a>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapis-using-encryption.html\"> Using encryption</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> <important> <p>If you specify an encrypted parent snapshot, you must have permission to use the KMS key that was used to encrypt the parent snapshot. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapi-permissions.html#ebsapi-kms-permissions\"> Permissions to use Key Management Service keys</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </important>
            tags: <p>The tags to apply to the snapshot.</p>
            description: <p>A description for the snapshot.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully. The subsequent retries with the same client token return the result from the original successful request and they have no additional effect.</p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-direct-api-idempotency.html\"> Idempotency for StartSnapshot API</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>
            encrypted: <p>Indicates whether to encrypt the snapshot.</p> <p>You can't specify <b>Encrypted</b> and <b> ParentSnapshotId</b> in the same request. If you specify both parameters, the request fails with <code>ValidationException</code>.</p> <p>The encryption status of the snapshot depends on the values that you specify for <b>Encrypted</b>, <b>KmsKeyArn</b>, and <b>ParentSnapshotId</b>, and whether your Amazon Web Services account is enabled for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default\"> encryption by default</a>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapis-using-encryption.html\"> Using encryption</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> <important> <p>To create an encrypted snapshot, you must have permission to use the KMS key. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapi-permissions.html#ebsapi-kms-permissions\"> Permissions to use Key Management Service keys</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </important>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the Key Management Service (KMS) key to be used to encrypt the snapshot.</p> <p>The encryption status of the snapshot depends on the values that you specify for <b>Encrypted</b>, <b>KmsKeyArn</b>, and <b>ParentSnapshotId</b>, and whether your Amazon Web Services account is enabled for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default\"> encryption by default</a>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapis-using-encryption.html\"> Using encryption</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> <important> <p>To create an encrypted snapshot, you must have permission to use the KMS key. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapi-permissions.html#ebsapi-kms-permissions\"> Permissions to use Key Management Service keys</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p> </important>
            timeout: <p>The amount of time (in minutes) after which the snapshot is automatically cancelled if:</p> <ul> <li> <p>No blocks are written to the snapshot.</p> </li> <li> <p>The snapshot is not completed after writing the last block of data.</p> </li> </ul> <p>If no value is specified, the timeout defaults to <code>60</code> minutes.</p>

        Raises:
            capo_ebs.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ebs.errors.concurrent_limit_exceeded_exception.ConcurrentLimitExceededException: <p>You have reached the limit for concurrent API requests. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-accessing-snapshot.html#ebsapi-performance\">Optimizing performance of the EBS direct APIs</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>
            capo_ebs.errors.conflict_exception.ConflictException: <p>The request uses the same client token as a previous, but non-identical request.</p>
            capo_ebs.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.request_throttled_exception.RequestThrottledException: <p>The number of API requests has exceeded the maximum allowed API request throttling limit for the snapshot. For more information see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html\">Error retries</a>.</p>
            capo_ebs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_ebs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your current service quotas do not allow you to perform this action.</p>
            capo_ebs.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints of the EBS direct APIs.</p>
            capo_ebs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_ebs.types.start_snapshot_request.StartSnapshotRequest]",
        ) -> OperationResponse[
            "capo_ebs.types.start_snapshot_response.StartSnapshotResponse"
        ]:
            import capo_ebs._operations.ebs.start_snapshot

            output, http_response = (
                capo_ebs._operations.ebs.start_snapshot.start_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ebs.types.start_snapshot_request.StartSnapshotRequest = {
            "volume_size": volume_size
        }
        if parent_snapshot_id is not None:
            input_["parent_snapshot_id"] = parent_snapshot_id
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if encrypted is not None:
            input_["encrypted"] = encrypted
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if timeout is not None:
            input_["timeout"] = timeout

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
