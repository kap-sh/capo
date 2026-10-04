"""Generated from Smithy shape ``com.amazonaws.dynamodb#DynamoDB_20120810``."""

import time
import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_dynamodb._auth._signers
import capo_dynamodb._auth._sigv4
from capo_dynamodb._auth._identity import Credentials
from capo_dynamodb._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_dynamodb._auth._zapros_handler import AuthMiddleware
from capo_dynamodb._pagination import resolve_path as _resolve_path
from capo_dynamodb._services._aws_config import aws_config
from capo_dynamodb._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)
from capo_dynamodb.errors import ServiceError, WaiterTimeoutError

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_definitions
    import capo_dynamodb.types.attribute_map
    import capo_dynamodb.types.attribute_name_list
    import capo_dynamodb.types.attribute_updates
    import capo_dynamodb.types.auto_scaling_settings_update
    import capo_dynamodb.types.backup_arn
    import capo_dynamodb.types.backup_name
    import capo_dynamodb.types.backup_type_filter
    import capo_dynamodb.types.backups_input_limit
    import capo_dynamodb.types.batch_execute_statement_input
    import capo_dynamodb.types.batch_execute_statement_output
    import capo_dynamodb.types.batch_get_item_input
    import capo_dynamodb.types.batch_get_item_output
    import capo_dynamodb.types.batch_get_request_map
    import capo_dynamodb.types.batch_write_item_input
    import capo_dynamodb.types.batch_write_item_output
    import capo_dynamodb.types.batch_write_item_request_map
    import capo_dynamodb.types.billing_mode
    import capo_dynamodb.types.boolean_object
    import capo_dynamodb.types.client_request_token
    import capo_dynamodb.types.client_token
    import capo_dynamodb.types.condition_expression
    import capo_dynamodb.types.conditional_operator
    import capo_dynamodb.types.confirm_remove_self_resource_access
    import capo_dynamodb.types.consistent_read
    import capo_dynamodb.types.contributor_insights_action
    import capo_dynamodb.types.contributor_insights_mode
    import capo_dynamodb.types.create_backup_input
    import capo_dynamodb.types.create_backup_output
    import capo_dynamodb.types.create_global_table_input
    import capo_dynamodb.types.create_global_table_output
    import capo_dynamodb.types.create_table_input
    import capo_dynamodb.types.create_table_output
    import capo_dynamodb.types.date
    import capo_dynamodb.types.delete_backup_input
    import capo_dynamodb.types.delete_backup_output
    import capo_dynamodb.types.delete_item_input
    import capo_dynamodb.types.delete_item_output
    import capo_dynamodb.types.delete_resource_policy_input
    import capo_dynamodb.types.delete_resource_policy_output
    import capo_dynamodb.types.delete_table_input
    import capo_dynamodb.types.delete_table_output
    import capo_dynamodb.types.deletion_protection_enabled
    import capo_dynamodb.types.describe_backup_input
    import capo_dynamodb.types.describe_backup_output
    import capo_dynamodb.types.describe_continuous_backups_input
    import capo_dynamodb.types.describe_continuous_backups_output
    import capo_dynamodb.types.describe_contributor_insights_input
    import capo_dynamodb.types.describe_contributor_insights_output
    import capo_dynamodb.types.describe_endpoints_request
    import capo_dynamodb.types.describe_endpoints_response
    import capo_dynamodb.types.describe_export_input
    import capo_dynamodb.types.describe_export_output
    import capo_dynamodb.types.describe_global_table_input
    import capo_dynamodb.types.describe_global_table_output
    import capo_dynamodb.types.describe_global_table_settings_input
    import capo_dynamodb.types.describe_global_table_settings_output
    import capo_dynamodb.types.describe_import_input
    import capo_dynamodb.types.describe_import_output
    import capo_dynamodb.types.describe_kinesis_streaming_destination_input
    import capo_dynamodb.types.describe_kinesis_streaming_destination_output
    import capo_dynamodb.types.describe_limits_input
    import capo_dynamodb.types.describe_limits_output
    import capo_dynamodb.types.describe_table_input
    import capo_dynamodb.types.describe_table_output
    import capo_dynamodb.types.describe_table_replica_auto_scaling_input
    import capo_dynamodb.types.describe_table_replica_auto_scaling_output
    import capo_dynamodb.types.describe_time_to_live_input
    import capo_dynamodb.types.describe_time_to_live_output
    import capo_dynamodb.types.enable_kinesis_streaming_configuration
    import capo_dynamodb.types.execute_statement_input
    import capo_dynamodb.types.execute_statement_output
    import capo_dynamodb.types.execute_transaction_input
    import capo_dynamodb.types.execute_transaction_output
    import capo_dynamodb.types.expected_attribute_map
    import capo_dynamodb.types.export_arn
    import capo_dynamodb.types.export_format
    import capo_dynamodb.types.export_next_token
    import capo_dynamodb.types.export_table_to_point_in_time_input
    import capo_dynamodb.types.export_table_to_point_in_time_output
    import capo_dynamodb.types.export_time
    import capo_dynamodb.types.export_type
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.expression_attribute_value_map
    import capo_dynamodb.types.filter_condition_map
    import capo_dynamodb.types.filter_specification
    import capo_dynamodb.types.get_item_input
    import capo_dynamodb.types.get_item_output
    import capo_dynamodb.types.get_resource_policy_input
    import capo_dynamodb.types.get_resource_policy_output
    import capo_dynamodb.types.global_secondary_index_auto_scaling_update_list
    import capo_dynamodb.types.global_secondary_index_list
    import capo_dynamodb.types.global_secondary_index_update_list
    import capo_dynamodb.types.global_table_global_secondary_index_settings_update_list
    import capo_dynamodb.types.global_table_settings_replication_mode
    import capo_dynamodb.types.global_table_witness_group_update_list
    import capo_dynamodb.types.import_arn
    import capo_dynamodb.types.import_next_token
    import capo_dynamodb.types.import_table_input
    import capo_dynamodb.types.import_table_output
    import capo_dynamodb.types.incremental_export_specification
    import capo_dynamodb.types.index_name
    import capo_dynamodb.types.input_compression_type
    import capo_dynamodb.types.input_format
    import capo_dynamodb.types.input_format_options
    import capo_dynamodb.types.key
    import capo_dynamodb.types.key_conditions
    import capo_dynamodb.types.key_expression
    import capo_dynamodb.types.key_schema
    import capo_dynamodb.types.kinesis_streaming_destination_input
    import capo_dynamodb.types.kinesis_streaming_destination_output
    import capo_dynamodb.types.list_backups_input
    import capo_dynamodb.types.list_backups_output
    import capo_dynamodb.types.list_contributor_insights_input
    import capo_dynamodb.types.list_contributor_insights_limit
    import capo_dynamodb.types.list_contributor_insights_output
    import capo_dynamodb.types.list_exports_input
    import capo_dynamodb.types.list_exports_max_limit
    import capo_dynamodb.types.list_exports_output
    import capo_dynamodb.types.list_global_tables_input
    import capo_dynamodb.types.list_global_tables_output
    import capo_dynamodb.types.list_imports_input
    import capo_dynamodb.types.list_imports_max_limit
    import capo_dynamodb.types.list_imports_output
    import capo_dynamodb.types.list_tables_input
    import capo_dynamodb.types.list_tables_input_limit
    import capo_dynamodb.types.list_tables_output
    import capo_dynamodb.types.list_tags_of_resource_input
    import capo_dynamodb.types.list_tags_of_resource_output
    import capo_dynamodb.types.local_secondary_index_list
    import capo_dynamodb.types.multi_region_consistency
    import capo_dynamodb.types.next_token_string
    import capo_dynamodb.types.on_demand_throughput
    import capo_dynamodb.types.parameterized_statements
    import capo_dynamodb.types.parti_ql_batch_request
    import capo_dynamodb.types.parti_ql_next_token
    import capo_dynamodb.types.parti_ql_statement
    import capo_dynamodb.types.point_in_time_recovery_specification
    import capo_dynamodb.types.policy_revision_id
    import capo_dynamodb.types.positive_integer_object
    import capo_dynamodb.types.positive_long_object
    import capo_dynamodb.types.prepared_statement_parameters
    import capo_dynamodb.types.projection_expression
    import capo_dynamodb.types.provisioned_throughput
    import capo_dynamodb.types.put_item_input
    import capo_dynamodb.types.put_item_input_attribute_map
    import capo_dynamodb.types.put_item_output
    import capo_dynamodb.types.put_resource_policy_input
    import capo_dynamodb.types.put_resource_policy_output
    import capo_dynamodb.types.query_input
    import capo_dynamodb.types.query_output
    import capo_dynamodb.types.region_name
    import capo_dynamodb.types.replica_auto_scaling_update_list
    import capo_dynamodb.types.replica_list
    import capo_dynamodb.types.replica_settings_update_list
    import capo_dynamodb.types.replica_update_list
    import capo_dynamodb.types.replication_group_update_list
    import capo_dynamodb.types.resource_arn_string
    import capo_dynamodb.types.resource_policy
    import capo_dynamodb.types.restore_table_from_backup_input
    import capo_dynamodb.types.restore_table_from_backup_output
    import capo_dynamodb.types.restore_table_to_point_in_time_input
    import capo_dynamodb.types.restore_table_to_point_in_time_output
    import capo_dynamodb.types.return_consumed_capacity
    import capo_dynamodb.types.return_item_collection_metrics
    import capo_dynamodb.types.return_value
    import capo_dynamodb.types.return_values_on_condition_check_failure
    import capo_dynamodb.types.s3_bucket
    import capo_dynamodb.types.s3_bucket_owner
    import capo_dynamodb.types.s3_bucket_source
    import capo_dynamodb.types.s3_prefix
    import capo_dynamodb.types.s3_sse_algorithm
    import capo_dynamodb.types.s3_sse_kms_key_id
    import capo_dynamodb.types.scan_input
    import capo_dynamodb.types.scan_output
    import capo_dynamodb.types.scan_segment
    import capo_dynamodb.types.scan_total_segments
    import capo_dynamodb.types.search_vector_list
    import capo_dynamodb.types.search_vectors_input
    import capo_dynamodb.types.search_vectors_output
    import capo_dynamodb.types.select
    import capo_dynamodb.types.sse_specification
    import capo_dynamodb.types.stream_arn
    import capo_dynamodb.types.stream_specification
    import capo_dynamodb.types.string
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.table_class
    import capo_dynamodb.types.table_creation_parameters
    import capo_dynamodb.types.table_name
    import capo_dynamodb.types.tag_key_list
    import capo_dynamodb.types.tag_list
    import capo_dynamodb.types.tag_resource_input
    import capo_dynamodb.types.time_range_lower_bound
    import capo_dynamodb.types.time_range_upper_bound
    import capo_dynamodb.types.time_to_live_specification
    import capo_dynamodb.types.top_k_integer
    import capo_dynamodb.types.transact_get_item_list
    import capo_dynamodb.types.transact_get_items_input
    import capo_dynamodb.types.transact_get_items_output
    import capo_dynamodb.types.transact_write_item_list
    import capo_dynamodb.types.transact_write_items_input
    import capo_dynamodb.types.transact_write_items_output
    import capo_dynamodb.types.untag_resource_input
    import capo_dynamodb.types.update_continuous_backups_input
    import capo_dynamodb.types.update_continuous_backups_output
    import capo_dynamodb.types.update_contributor_insights_input
    import capo_dynamodb.types.update_contributor_insights_output
    import capo_dynamodb.types.update_expression
    import capo_dynamodb.types.update_global_table_input
    import capo_dynamodb.types.update_global_table_output
    import capo_dynamodb.types.update_global_table_settings_input
    import capo_dynamodb.types.update_global_table_settings_output
    import capo_dynamodb.types.update_item_input
    import capo_dynamodb.types.update_item_output
    import capo_dynamodb.types.update_kinesis_streaming_configuration
    import capo_dynamodb.types.update_kinesis_streaming_destination_input
    import capo_dynamodb.types.update_kinesis_streaming_destination_output
    import capo_dynamodb.types.update_table_input
    import capo_dynamodb.types.update_table_output
    import capo_dynamodb.types.update_table_replica_auto_scaling_input
    import capo_dynamodb.types.update_table_replica_auto_scaling_output
    import capo_dynamodb.types.update_time_to_live_input
    import capo_dynamodb.types.update_time_to_live_output
    import capo_dynamodb.types.vector_index_list
    import capo_dynamodb.types.vector_index_update_list
    import capo_dynamodb.types.warm_throughput


class DynamoDBClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    account_id: str | None
    account_id_endpoint_mode: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class DynamoDBClient:
    """A client for the ``DynamoDB`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        account_id: The value of the ``AWS::Auth::AccountId`` endpoint parameter.
        account_id_endpoint_mode: The value of the ``AWS::Auth::AccountIdEndpointMode`` endpoint parameter.
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
        account_id: str | None = None,
        account_id_endpoint_mode: str | None = None,
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
        self._config = DynamoDBClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "account_id": account_id,
                "account_id_endpoint_mode": account_id_endpoint_mode,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[DynamoDBClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: DynamoDBClientConfig = config_overrides or {}
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
            account_id=overrides.get("account_id", self._config.get("account_id")),
            account_id_endpoint_mode=overrides.get(
                "account_id_endpoint_mode", self._config.get("account_id_endpoint_mode")
            ),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def batch_execute_statement(
        self,
        statements: "capo_dynamodb.types.parti_ql_batch_request.PartiQLBatchRequest",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
    ) -> (
        "capo_dynamodb.types.batch_execute_statement_output.BatchExecuteStatementOutput"
    ):
        """<p>This operation allows you to perform batch reads or writes on data stored in DynamoDB, using PartiQL. Each read statement in a <code>BatchExecuteStatement</code> must specify an equality condition on all key attributes. This enforces that each <code>SELECT</code> statement in a batch returns at most a single item. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.multiplestatements.batching.html">Running batch operations with PartiQL for DynamoDB </a>.</p> <note> <p>The entire batch must consist of either read statements or write statements, you cannot mix both in one batch.</p> </note> <important> <p>A HTTP 200 response does not mean that all statements in the BatchExecuteStatement succeeded. Error details for individual statements can be found under the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchStatementResponse.html#DDB-Type-BatchStatementResponse-Error">Error</a> field of the <code>BatchStatementResponse</code> for each statement.</p> </important>

        Args:
            statements: <p>The list of PartiQL statements representing the batch to run.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.batch_execute_statement_input.BatchExecuteStatementInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.batch_execute_statement_output.BatchExecuteStatementOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.batch_execute_statement

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.batch_execute_statement.batch_execute_statement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.batch_execute_statement_input.BatchExecuteStatementInput = {
            "statements": statements
        }
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_item(
        self,
        request_items: "capo_dynamodb.types.batch_get_request_map.BatchGetRequestMap",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
    ) -> "capo_dynamodb.types.batch_get_item_output.BatchGetItemOutput":
        """<p>The <code>BatchGetItem</code> operation returns the attributes of one or more items from one or more tables. You identify requested items by primary key.</p> <p>A single operation can retrieve up to 16 MB of data, which can contain as many as 100 items. <code>BatchGetItem</code> returns a partial result if the response size limit is exceeded, the table's provisioned throughput is exceeded, more than 1MB per partition is requested, or an internal processing failure occurs. If a partial result is returned, the operation returns a value for <code>UnprocessedKeys</code>. You can use this value to retry the operation starting with the next item to get.</p> <important> <p>If you request more than 100 items, <code>BatchGetItem</code> returns a <code>ValidationException</code> with the message "Too many items requested for the BatchGetItem call."</p> </important> <p>For example, if you ask to retrieve 100 items, but each individual item is 300 KB in size, the system returns 52 items (so as not to exceed the 16 MB limit). It also returns an appropriate <code>UnprocessedKeys</code> value so you can get the next page of results. If desired, your application can include its own logic to assemble the pages of results into one dataset.</p> <p>If <i>none</i> of the items can be processed due to insufficient provisioned throughput on all of the tables in the request, then <code>BatchGetItem</code> returns a <code>ProvisionedThroughputExceededException</code>. If <i>at least one</i> of the items is successfully processed, then <code>BatchGetItem</code> completes successfully, while returning the keys of the unread items in <code>UnprocessedKeys</code>.</p> <important> <p>If DynamoDB returns any unprocessed items, you should retry the batch operation on those items. However, <i>we strongly recommend that you use an exponential backoff algorithm</i>. If you retry the batch operation immediately, the underlying read or write requests can still fail due to throttling on the individual tables. If you delay the batch operation using exponential backoff, the individual requests in the batch are much more likely to succeed.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ErrorHandling.html#BatchOperations">Batch Operations and Error Handling</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> </important> <p>By default, <code>BatchGetItem</code> performs eventually consistent reads on every table in the request. If you want strongly consistent reads instead, you can set <code>ConsistentRead</code> to <code>true</code> for any or all tables.</p> <p>In order to minimize response latency, <code>BatchGetItem</code> may retrieve items in parallel.</p> <p>When designing your application, keep in mind that DynamoDB does not return items in any particular order. To help parse the response by item, include the primary key values for the items in your request in the <code>ProjectionExpression</code> parameter.</p> <p>If a requested item does not exist, it is not returned in the result. Requests for nonexistent items consume the minimum read capacity units according to the type of read. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#CapacityUnitCalculations">Working with Tables</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <note> <p> <code>BatchGetItem</code> will result in a <code>ValidationException</code> if the same key is specified multiple times.</p> </note>

        Args:
            request_items: <p>A map of one or more table names or table ARNs and, for each table, a map that describes one or more items to retrieve from that table. Each table name or ARN can be used only once per <code>BatchGetItem</code> request.</p> <p>Each element in the map of items to retrieve consists of the following:</p> <ul> <li> <p> <code>ConsistentRead</code> - If <code>true</code>, a strongly consistent read is used; if <code>false</code> (the default), an eventually consistent read is used.</p> </li> <li> <p> <code>ExpressionAttributeNames</code> - One or more substitution tokens for attribute names in the <code>ProjectionExpression</code> parameter. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information about expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Accessing Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> </li> <li> <p> <code>Keys</code> - An array of primary key attribute values that define specific items in the table. For each primary key, you must provide <i>all</i> of the key attributes. For example, with a simple primary key, you only need to provide the partition key value. For a composite key, you must provide <i>both</i> the partition key value and the sort key value.</p> </li> <li> <p> <code>ProjectionExpression</code> - A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.</p> <p>If no attribute names are specified, then all attributes are returned. If any of the requested attributes are not found, they do not appear in the result.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Accessing Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> </li> <li> <p> <code>AttributesToGet</code> - This is a legacy parameter. Use <code>ProjectionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html">AttributesToGet</a> in the <i>Amazon DynamoDB Developer Guide</i>. </p> </li> </ul>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve multiple items from a table
            This example reads multiple items from the Music table using a batch of three GetItem requests.  Only the AlbumTitle attribute is returned.

            >>> client.batch_get_item(request_items={'Music': {'Keys': [{'Artist': {'S': 'No One You Know'}, 'SongTitle': {'S': 'Call Me Today'}}, {'Artist': {'S': 'Acme Band'}, 'SongTitle': {'S': 'Happy Day'}}, {'Artist': {'S': 'No One You Know'}, 'SongTitle': {'S': 'Scared of My Shadow'}}], 'ProjectionExpression': 'AlbumTitle'}})
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.batch_get_item_input.BatchGetItemInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.batch_get_item_output.BatchGetItemOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.batch_get_item

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.batch_get_item.batch_get_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.batch_get_item_input.BatchGetItemInput = {
            "request_items": request_items
        }
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_write_item(
        self,
        request_items: "capo_dynamodb.types.batch_write_item_request_map.BatchWriteItemRequestMap",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        return_item_collection_metrics: Optional[
            "capo_dynamodb.types.return_item_collection_metrics.ReturnItemCollectionMetrics"
        ] = None,
    ) -> "capo_dynamodb.types.batch_write_item_output.BatchWriteItemOutput":
        """<p>The <code>BatchWriteItem</code> operation puts or deletes multiple items in one or more tables. A single call to <code>BatchWriteItem</code> can transmit up to 16MB of data over the network, consisting of up to 25 item put or delete operations. While individual items can be up to 400 KB once stored, it's important to note that an item's representation might be greater than 400KB while being sent in DynamoDB's JSON format for the API call. For more details on this distinction, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html">Naming Rules and Data Types</a>.</p> <note> <p> <code>BatchWriteItem</code> cannot update items. If you perform a <code>BatchWriteItem</code> operation on an existing item, that item's values will be overwritten by the operation and it will appear like it was updated. To update items, we recommend you use the <code>UpdateItem</code> action.</p> </note> <p>The individual <code>PutItem</code> and <code>DeleteItem</code> operations specified in <code>BatchWriteItem</code> are atomic; however <code>BatchWriteItem</code> as a whole is not. If any requested operations fail because the table's provisioned throughput is exceeded or an internal processing failure occurs, the failed operations are returned in the <code>UnprocessedItems</code> response parameter. You can investigate and optionally resend the requests. Typically, you would call <code>BatchWriteItem</code> in a loop. Each iteration would check for unprocessed items and submit a new <code>BatchWriteItem</code> request with those unprocessed items until all items have been processed.</p> <p>If <code>BatchWriteItem</code> cannot process any items due to throttling (for example, insufficient provisioned throughput on the tables in the request, or partition-level or account-level limits), it returns a <code>ProvisionedThroughputExceededException</code> or a <code>ThrottlingException</code>. Both indicate that the request was throttled; check the <code>ThrottlingReason</code> field in the returned exception for details.</p> <important> <p>If DynamoDB returns any unprocessed items, you should retry the batch operation on those items. However, <i>we strongly recommend that you use an exponential backoff algorithm</i>. If you retry the batch operation immediately, the underlying read or write requests can still fail due to throttling on the individual tables. If you delay the batch operation using exponential backoff, the individual requests in the batch are much more likely to succeed.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ErrorHandling.html#Programming.Errors.BatchOperations">Batch Operations and Error Handling</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> </important> <p>With <code>BatchWriteItem</code>, you can efficiently write or delete large amounts of data, such as from Amazon EMR, or copy data from another database into DynamoDB. In order to improve performance with these large-scale operations, <code>BatchWriteItem</code> does not behave in the same way as individual <code>PutItem</code> and <code>DeleteItem</code> calls would. For example, you cannot specify conditions on individual put and delete requests, and <code>BatchWriteItem</code> does not return deleted items in the response.</p> <p>If you use a programming language that supports concurrency, you can use threads to write items in parallel. Your application must include the necessary logic to manage the threads. With languages that don't support threading, you must update or delete the specified items one at a time. In both situations, <code>BatchWriteItem</code> performs the specified put and delete operations in parallel, giving you the power of the thread pool approach without having to introduce complexity into your application.</p> <p>Parallel processing reduces latency, but each specified put and delete request consumes the same number of write capacity units whether it is processed in parallel or not. Delete operations on nonexistent items consume one write capacity unit.</p> <p>If one or more of the following is true, DynamoDB rejects the entire batch write operation:</p> <ul> <li> <p>One or more tables specified in the <code>BatchWriteItem</code> request does not exist.</p> </li> <li> <p>Primary key attributes specified on an item in the request do not match those in the corresponding table's primary key schema.</p> </li> <li> <p>You try to perform multiple operations on the same item in the same <code>BatchWriteItem</code> request. For example, you cannot put and delete the same item in the same <code>BatchWriteItem</code> request. </p> </li> <li> <p> Your request contains at least two items with identical hash and range keys (which essentially is two put operations). </p> </li> <li> <p>There are more than 25 requests in the batch.</p> </li> <li> <p>Any individual item in a batch exceeds 400 KB.</p> </li> <li> <p>The total request size exceeds 16 MB.</p> </li> <li> <p>Any individual items with keys exceeding the key length limits. For a partition key, the limit is 2048 bytes and for a sort key, the limit is 1024 bytes.</p> </li> </ul>

        Args:
            request_items: <p>A map of one or more table names or table ARNs and, for each table, a list of operations to be performed (<code>DeleteRequest</code> or <code>PutRequest</code>). Each element in the map consists of the following:</p> <ul> <li> <p> <code>DeleteRequest</code> - Perform a <code>DeleteItem</code> operation on the specified item. The item to be deleted is identified by a <code>Key</code> subelement:</p> <ul> <li> <p> <code>Key</code> - A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value. For each primary key, you must provide <i>all</i> of the key attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for <i>both</i> the partition key and the sort key.</p> </li> </ul> </li> <li> <p> <code>PutRequest</code> - Perform a <code>PutItem</code> operation on the specified item. The item to be put is identified by an <code>Item</code> subelement:</p> <ul> <li> <p> <code>Item</code> - A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values are rejected with a <code>ValidationException</code> exception.</p> <p>If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table's attribute definition.</p> </li> </ul> </li> </ul>
            return_item_collection_metrics: <p>Determines whether item collection metrics are returned. If set to <code>SIZE</code>, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to <code>NONE</code> (the default), no statistics are returned.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.item_collection_size_limit_exceeded_exception.ItemCollectionSizeLimitExceededException: <p>An item collection is too large. This exception is only returned for tables that have one or more local secondary indexes.</p>
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.replicated_write_conflict_exception.ReplicatedWriteConflictException: <p>The request was rejected because one or more items in the request are being modified by a request in another Region. </p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add multiple items to a table
            This example adds three new items to the Music table using a batch of three PutItem requests.

            >>> client.batch_write_item(request_items={'Music': [{'PutRequest': {'Item': {'AlbumTitle': {'S': 'Somewhat Famous'}, 'SongTitle': {'S': 'Call Me Today'}, 'Artist': {'S': 'No One You Know'}}}}, {'PutRequest': {'Item': {'AlbumTitle': {'S': 'Songs About Life'}, 'SongTitle': {'S': 'Happy Day'}, 'Artist': {'S': 'Acme Band'}}}}, {'PutRequest': {'Item': {'AlbumTitle': {'S': 'Blue Sky Blues'}, 'SongTitle': {'S': 'Scared of My Shadow'}, 'Artist': {'S': 'No One You Know'}}}}]})
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.batch_write_item_input.BatchWriteItemInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.batch_write_item_output.BatchWriteItemOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.batch_write_item

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.batch_write_item.batch_write_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.batch_write_item_input.BatchWriteItemInput = {
            "request_items": request_items
        }
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity
        if return_item_collection_metrics is not None:
            input_["return_item_collection_metrics"] = return_item_collection_metrics

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backup(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        backup_name: "capo_dynamodb.types.backup_name.BackupName",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.create_backup_output.CreateBackupOutput":
        """<p>Creates a backup for an existing table.</p> <p> Each time you create an on-demand backup, the entire table data is backed up. There is no limit to the number of on-demand backups that can be taken. </p> <p> When you create an on-demand backup, a time marker of the request is cataloged, and the backup is created asynchronously, by applying all changes until the time of the request to the last full table snapshot. Backup requests are processed instantaneously and become available for restore within minutes. </p> <p>You can call <code>CreateBackup</code> at a maximum rate of 50 times per second.</p> <p>All backups in DynamoDB work without consuming any provisioned throughput on the table.</p> <p> If you submit a backup request on 2018-12-14 at 14:25:00, the backup is guaranteed to contain all data committed to the table up to 14:24:00, and data committed after 14:26:00 will not be. The backup might contain data modifications made between 14:24:00 and 14:26:00. On-demand backup does not support causal consistency. </p> <p> Along with data, the following are also included on the backups: </p> <ul> <li> <p>Global secondary indexes (GSIs)</p> </li> <li> <p>Local secondary indexes (LSIs)</p> </li> <li> <p>Streams</p> </li> <li> <p>Provisioned read and write capacity</p> </li> </ul>

        Args:
            table_name: <p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            backup_name: <p>Specified name for the backup.</p>

        Raises:
            capo_dynamodb.errors.backup_in_use_exception.BackupInUseException: <p>There is another ongoing conflicting backup control plane operation on the table. The backup is either being created, deleted or restored to a table.</p>
            capo_dynamodb.errors.continuous_backups_unavailable_exception.ContinuousBackupsUnavailableException: <p>Backups have not yet been enabled for this table.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.table_in_use_exception.TableInUseException: <p>A target table with the specified name is either being created or deleted. </p>
            capo_dynamodb.errors.table_not_found_exception.TableNotFoundException: <p>A source table with the name <code>TableName</code> does not currently exist within the subscriber's account or the subscriber is operating in the wrong Amazon Web Services Region.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.create_backup_input.CreateBackupInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.create_backup_output.CreateBackupOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.create_backup

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.create_backup.create_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.create_backup_input.CreateBackupInput = {
            "table_name": table_name,
            "backup_name": backup_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_global_table(
        self,
        global_table_name: "capo_dynamodb.types.table_name.TableName",
        replication_group: "capo_dynamodb.types.replica_list.ReplicaList",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.create_global_table_output.CreateGlobalTableOutput":
        """<p>Creates a global table from an existing table. A global table creates a replication relationship between two or more DynamoDB tables with the same table name in the provided Regions. </p> <important> <p>This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html">Global Tables version 2019.11.21 (Current)</a> when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).</p> <p>To determine which version you're using, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html">Determining the global table version you are using</a>. To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html">Upgrading global tables</a>.</p> </important> <p>If you want to add a new replica table to a global table, each of the following conditions must be true:</p> <ul> <li> <p>The table must have the same primary key as all of the other replicas.</p> </li> <li> <p>The table must have the same name as all of the other replicas.</p> </li> <li> <p>The table must have DynamoDB Streams enabled, with the stream containing both the new and the old images of the item.</p> </li> <li> <p>None of the replica tables in the global table can contain any data.</p> </li> </ul> <p> If global secondary indexes are specified, then the following conditions must also be met: </p> <ul> <li> <p> The global secondary indexes must have the same name. </p> </li> <li> <p> The global secondary indexes must have the same hash key and sort key (if present). </p> </li> </ul> <p> If local secondary indexes are specified, then the following conditions must also be met: </p> <ul> <li> <p> The local secondary indexes must have the same name. </p> </li> <li> <p> The local secondary indexes must have the same hash key and sort key (if present). </p> </li> </ul> <important> <p> Write capacity settings should be set consistently across your replica tables and secondary indexes. DynamoDB strongly recommends enabling auto scaling to manage the write capacity settings for all of your global tables replicas and indexes. </p> <p> If you prefer to manage write capacity settings manually, you should provision equal replicated write capacity units to your replica tables. You should also provision equal replicated write capacity units to matching secondary indexes across your global table. </p> </important>

        Args:
            global_table_name: <p>The global table name.</p>
            replication_group: <p>The Regions where the global table needs to be created.</p>

        Raises:
            capo_dynamodb.errors.global_table_already_exists_exception.GlobalTableAlreadyExistsException: <p>The specified global table already exists.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.table_not_found_exception.TableNotFoundException: <p>A source table with the name <code>TableName</code> does not currently exist within the subscriber's account or the subscriber is operating in the wrong Amazon Web Services Region.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.create_global_table_input.CreateGlobalTableInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.create_global_table_output.CreateGlobalTableOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.create_global_table

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.create_global_table.create_global_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.create_global_table_input.CreateGlobalTableInput = {
            "global_table_name": global_table_name,
            "replication_group": replication_group,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_table(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        attribute_definitions: Optional[
            "capo_dynamodb.types.attribute_definitions.AttributeDefinitions"
        ] = None,
        key_schema: Optional["capo_dynamodb.types.key_schema.KeySchema"] = None,
        local_secondary_indexes: Optional[
            "capo_dynamodb.types.local_secondary_index_list.LocalSecondaryIndexList"
        ] = None,
        global_secondary_indexes: Optional[
            "capo_dynamodb.types.global_secondary_index_list.GlobalSecondaryIndexList"
        ] = None,
        billing_mode: Optional["capo_dynamodb.types.billing_mode.BillingMode"] = None,
        provisioned_throughput: Optional[
            "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
        ] = None,
        stream_specification: Optional[
            "capo_dynamodb.types.stream_specification.StreamSpecification"
        ] = None,
        sse_specification: Optional[
            "capo_dynamodb.types.sse_specification.SSESpecification"
        ] = None,
        tags: Optional["capo_dynamodb.types.tag_list.TagList"] = None,
        table_class: Optional["capo_dynamodb.types.table_class.TableClass"] = None,
        deletion_protection_enabled: Optional[
            "capo_dynamodb.types.deletion_protection_enabled.DeletionProtectionEnabled"
        ] = None,
        warm_throughput: Optional[
            "capo_dynamodb.types.warm_throughput.WarmThroughput"
        ] = None,
        resource_policy: Optional[
            "capo_dynamodb.types.resource_policy.ResourcePolicy"
        ] = None,
        on_demand_throughput: Optional[
            "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
        ] = None,
        global_table_source_arn: Optional[
            "capo_dynamodb.types.table_arn.TableArn"
        ] = None,
        global_table_settings_replication_mode: Optional[
            "capo_dynamodb.types.global_table_settings_replication_mode.GlobalTableSettingsReplicationMode"
        ] = None,
        vector_indexes: Optional[
            "capo_dynamodb.types.vector_index_list.VectorIndexList"
        ] = None,
    ) -> "capo_dynamodb.types.create_table_output.CreateTableOutput":
        """<p>The <code>CreateTable</code> operation adds a new table to your account. In an Amazon Web Services account, table names must be unique within each Region. That is, you can have two tables with same name if you create the tables in different Regions.</p> <p> <code>CreateTable</code> is an asynchronous operation. Upon receiving a <code>CreateTable</code> request, DynamoDB immediately returns a response with a <code>TableStatus</code> of <code>CREATING</code>. After the table is created, DynamoDB sets the <code>TableStatus</code> to <code>ACTIVE</code>. You can perform read and write operations only on an <code>ACTIVE</code> table. </p> <p>You can optionally define secondary indexes on the new table, as part of the <code>CreateTable</code> operation. If you want to create multiple tables with secondary indexes on them, you must create the tables sequentially. Only one table with secondary indexes can be in the <code>CREATING</code> state at any given time.</p> <p>You can use the <code>DescribeTable</code> action to check the table status.</p>

        Args:
            attribute_definitions: <p>An array of attributes that describe the key schema for the table and indexes.</p>
            table_name: <p>The name of the table to create. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            key_schema: <p>Specifies the attributes that make up the primary key for a table or an index. The attributes in <code>KeySchema</code> must also be defined in the <code>AttributeDefinitions</code> array. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DataModel.html">Data Model</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>Each <code>KeySchemaElement</code> in the array is composed of:</p> <ul> <li> <p> <code>AttributeName</code> - The name of this key attribute.</p> </li> <li> <p> <code>KeyType</code> - The role that the key attribute will assume:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term "hash attribute" derives from the DynamoDB usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note> <p>For a simple primary key (partition key), you must provide exactly one element with a <code>KeyType</code> of <code>HASH</code>.</p> <p>For a composite primary key (partition key and sort key), you must provide exactly two elements, in this order: The first element must have a <code>KeyType</code> of <code>HASH</code>, and the second element must have a <code>KeyType</code> of <code>RANGE</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html#WorkingWithTables.primary.key">Working with Tables</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            local_secondary_indexes: <p>One or more local secondary indexes (the maximum is 5) to be created on the table. Each index is scoped to a given partition key value. There is a 10 GB size limit per partition key value; otherwise, the size of a local secondary index is unconstrained.</p> <p>Each local secondary index in the array includes the following:</p> <ul> <li> <p> <code>IndexName</code> - The name of the local secondary index. Must be unique only for this table.</p> <p></p> </li> <li> <p> <code>KeySchema</code> - Specifies the key schema for the local secondary index. The key schema must begin with the same partition key as the table.</p> </li> <li> <p> <code>Projection</code> - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:</p> <ul> <li> <p> <code>ProjectionType</code> - One of the following:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the index and primary keys are projected into the index.</p> </li> <li> <p> <code>INCLUDE</code> - Only the specified table attributes are projected into the index. The list of projected attributes is in <code>NonKeyAttributes</code>.</p> </li> <li> <p> <code>ALL</code> - All of the table attributes are projected into the index.</p> </li> </ul> </li> <li> <p> <code>NonKeyAttributes</code> - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in <code>NonKeyAttributes</code>, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of <code>INCLUDE</code>. You still can specify the ProjectionType of <code>ALL</code> to project all attributes from the source table, even if the table has more than 100 attributes.</p> </li> </ul> </li> </ul>
            global_secondary_indexes: <p>One or more global secondary indexes (the maximum is 20) to be created on the table. Each global secondary index in the array includes the following:</p> <ul> <li> <p> <code>IndexName</code> - The name of the global secondary index. Must be unique only for this table.</p> <p></p> </li> <li> <p> <code>KeySchema</code> - Specifies the key schema for the global secondary index. Each global secondary index supports up to 4 partition keys and up to 4 sort keys.</p> </li> <li> <p> <code>Projection</code> - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of:</p> <ul> <li> <p> <code>ProjectionType</code> - One of the following:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the index and primary keys are projected into the index.</p> </li> <li> <p> <code>INCLUDE</code> - Only the specified table attributes are projected into the index. The list of projected attributes is in <code>NonKeyAttributes</code>.</p> </li> <li> <p> <code>ALL</code> - All of the table attributes are projected into the index.</p> </li> </ul> </li> <li> <p> <code>NonKeyAttributes</code> - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in <code>NonKeyAttributes</code>, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. This limit only applies when you specify the ProjectionType of <code>INCLUDE</code>. You still can specify the ProjectionType of <code>ALL</code> to project all attributes from the source table, even if the table has more than 100 attributes.</p> </li> </ul> </li> <li> <p> <code>ProvisionedThroughput</code> - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units.</p> </li> </ul>
            billing_mode: <p>Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.</p> <ul> <li> <p> <code>PAY_PER_REQUEST</code> - We recommend using <code>PAY_PER_REQUEST</code> for most DynamoDB workloads. <code>PAY_PER_REQUEST</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html">On-demand capacity mode</a>. </p> </li> <li> <p> <code>PROVISIONED</code> - We recommend using <code>PROVISIONED</code> for steady workloads with predictable growth where capacity requirements can be reliably forecasted. <code>PROVISIONED</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html">Provisioned capacity mode</a>.</p> </li> </ul>
            provisioned_throughput: <p>Represents the provisioned throughput settings for a specified table or index. The settings can be modified using the <code>UpdateTable</code> operation.</p> <p> If you set BillingMode as <code>PROVISIONED</code>, you must specify this property. If you set BillingMode as <code>PAY_PER_REQUEST</code>, you cannot specify this property.</p> <p>For current minimum and maximum provisioned throughput values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html">Service, Account, and Table Quotas</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            stream_specification: <p>The settings for DynamoDB Streams on the table. These settings consist of:</p> <ul> <li> <p> <code>StreamEnabled</code> - Indicates whether DynamoDB Streams is to be enabled (true) or disabled (false).</p> </li> <li> <p> <code>StreamViewType</code> - When an item in the table is modified, <code>StreamViewType</code> determines what information is written to the table's stream. Valid values for <code>StreamViewType</code> are:</p> <ul> <li> <p> <code>KEYS_ONLY</code> - Only the key attributes of the modified item are written to the stream.</p> </li> <li> <p> <code>NEW_IMAGE</code> - The entire item, as it appears after it was modified, is written to the stream.</p> </li> <li> <p> <code>OLD_IMAGE</code> - The entire item, as it appeared before it was modified, is written to the stream.</p> </li> <li> <p> <code>NEW_AND_OLD_IMAGES</code> - Both the new and the old item images of the item are written to the stream.</p> </li> </ul> </li> </ul>
            sse_specification: <p>Represents the settings used to enable server-side encryption.</p>
            tags: <p>A list of key-value pairs to label the table. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html">Tagging for DynamoDB</a>.</p>
            table_class: <p>The table class of the new table. Valid values are <code>STANDARD</code> and <code>STANDARD_INFREQUENT_ACCESS</code>.</p>
            deletion_protection_enabled: <p>Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table.</p>
            warm_throughput: <p>Represents the warm throughput (in read units per second and write units per second) for creating a table.</p>
            resource_policy: <p>An Amazon Web Services resource-based policy document in JSON format that will be attached to the table.</p> <p>When you attach a resource-based policy while creating a table, the policy application is <i>strongly consistent</i>.</p> <p>The maximum size supported for a resource-based policy document is 20 KB. DynamoDB counts whitespaces when calculating the size of a policy against this limit. For a full list of all considerations that apply for resource-based policies, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-considerations.html">Resource-based policy considerations</a>.</p> <note> <p>You need to specify the <code>CreateTable</code> and <code>PutResourcePolicy</code> IAM actions for authorizing a user to create a table with a resource-based policy.</p> </note>
            on_demand_throughput: <p>Sets the maximum number of read and write units for the specified table in on-demand capacity mode. If you use this parameter, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both.</p>
            global_table_source_arn: <p>The Amazon Resource Name (ARN) of the source table used for the creation of a multi-account global table.</p>
            global_table_settings_replication_mode: <p>Controls the settings synchronization mode for the global table. For multi-account global tables, this parameter is required and the only supported value is ENABLED. For same-account global tables, this parameter is set to ENABLED_WITH_OVERRIDES. </p>
            vector_indexes: <p>One or more vector indexes to be created on the table. Each vector index enables similarity search on a vector attribute. Each element in the list consists of:</p> <ul> <li> <p> <code>IndexName</code> - The name of the vector index. Must be unique within the table.</p> </li> <li> <p> <code>VectorAttribute</code> - The attribute that contains vector embeddings. If multiple vector indexes reference the same attribute, they must all use the same number of dimensions.</p> </li> <li> <p> <code>Dimensions</code> - The number of dimensions in each vector.</p> </li> <li> <p> <code>DistanceFunction</code> - The distance function used to calculate similarity. Valid values: <code>COSINE</code>, <code>EUCLIDEAN</code>, <code>DOT_PRODUCT</code>.</p> </li> <li> <p> <code>Projection</code> - Specifies attributes that are copied (projected) from the table into the vector index. The total number of projected non-key attributes is shared across the vector attribute (counts as 1) and <code>INLINE_FILTER</code> search schema elements (each counts as 1). <code>HASH</code> search schema elements do not count toward this limit.</p> </li> <li> <p> <code>SearchSchema</code> - (Optional) Defines the partition key (<code>HASH</code>) and inline filter (<code>INLINE_FILTER</code>) attributes for the vector index.</p> </li> </ul>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.create_table_input.CreateTableInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.create_table_output.CreateTableOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.create_table

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.create_table.create_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.create_table_input.CreateTableInput = {
            "table_name": table_name
        }
        if attribute_definitions is not None:
            input_["attribute_definitions"] = attribute_definitions
        if key_schema is not None:
            input_["key_schema"] = key_schema
        if local_secondary_indexes is not None:
            input_["local_secondary_indexes"] = local_secondary_indexes
        if global_secondary_indexes is not None:
            input_["global_secondary_indexes"] = global_secondary_indexes
        if billing_mode is not None:
            input_["billing_mode"] = billing_mode
        if provisioned_throughput is not None:
            input_["provisioned_throughput"] = provisioned_throughput
        if stream_specification is not None:
            input_["stream_specification"] = stream_specification
        if sse_specification is not None:
            input_["sse_specification"] = sse_specification
        if tags is not None:
            input_["tags"] = tags
        if table_class is not None:
            input_["table_class"] = table_class
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if warm_throughput is not None:
            input_["warm_throughput"] = warm_throughput
        if resource_policy is not None:
            input_["resource_policy"] = resource_policy
        if on_demand_throughput is not None:
            input_["on_demand_throughput"] = on_demand_throughput
        if global_table_source_arn is not None:
            input_["global_table_source_arn"] = global_table_source_arn
        if global_table_settings_replication_mode is not None:
            input_["global_table_settings_replication_mode"] = (
                global_table_settings_replication_mode
            )
        if vector_indexes is not None:
            input_["vector_indexes"] = vector_indexes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backup(
        self,
        backup_arn: "capo_dynamodb.types.backup_arn.BackupArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.delete_backup_output.DeleteBackupOutput":
        """<p>Deletes an existing backup of a table.</p> <p>You can call <code>DeleteBackup</code> at a maximum rate of 10 times per second.</p>

        Args:
            backup_arn: <p>The ARN associated with the backup.</p>

        Raises:
            capo_dynamodb.errors.backup_in_use_exception.BackupInUseException: <p>There is another ongoing conflicting backup control plane operation on the table. The backup is either being created, deleted or restored to a table.</p>
            capo_dynamodb.errors.backup_not_found_exception.BackupNotFoundException: <p>Backup not found for the given BackupARN. </p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.delete_backup_input.DeleteBackupInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.delete_backup_output.DeleteBackupOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.delete_backup

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.delete_backup.delete_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.delete_backup_input.DeleteBackupInput = {
            "backup_arn": backup_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_item(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        key: "capo_dynamodb.types.key.Key",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        expected: Optional[
            "capo_dynamodb.types.expected_attribute_map.ExpectedAttributeMap"
        ] = None,
        conditional_operator: Optional[
            "capo_dynamodb.types.conditional_operator.ConditionalOperator"
        ] = None,
        return_values: Optional["capo_dynamodb.types.return_value.ReturnValue"] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        return_item_collection_metrics: Optional[
            "capo_dynamodb.types.return_item_collection_metrics.ReturnItemCollectionMetrics"
        ] = None,
        condition_expression: Optional[
            "capo_dynamodb.types.condition_expression.ConditionExpression"
        ] = None,
        expression_attribute_names: Optional[
            "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
        ] = None,
        expression_attribute_values: Optional[
            "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
        ] = None,
        return_values_on_condition_check_failure: Optional[
            "capo_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
        ] = None,
    ) -> "capo_dynamodb.types.delete_item_output.DeleteItemOutput":
        """<p>Deletes a single item in a table by primary key. You can perform a conditional delete operation that deletes the item if it exists, or if it has an expected attribute value.</p> <p>In addition to deleting an item, you can also return the item's attribute values in the same operation, using the <code>ReturnValues</code> parameter.</p> <p>Unless you specify conditions, the <code>DeleteItem</code> is an idempotent operation; running it multiple times on the same item or attribute does <i>not</i> result in an error response.</p> <p>Conditional deletes are useful for deleting items only if specific conditions are met. If those conditions are met, DynamoDB performs the delete. Otherwise, the item is not deleted.</p>

        Args:
            table_name: <p>The name of the table from which to delete the item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            key: <p>A map of attribute names to <code>AttributeValue</code> objects, representing the primary key of the item to delete.</p> <p>For the primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.</p>
            expected: <p>This is a legacy parameter. Use <code>ConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Expected.html">Expected</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            conditional_operator: <p>This is a legacy parameter. Use <code>ConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html">ConditionalOperator</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            return_values: <p>Use <code>ReturnValues</code> if you want to get the item attributes as they appeared before they were deleted. For <code>DeleteItem</code>, the valid values are:</p> <ul> <li> <p> <code>NONE</code> - If <code>ReturnValues</code> is not specified, or if its value is <code>NONE</code>, then nothing is returned. (This setting is the default for <code>ReturnValues</code>.)</p> </li> <li> <p> <code>ALL_OLD</code> - The content of the old item is returned.</p> </li> </ul> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p> <note> <p>The <code>ReturnValues</code> parameter is used by several DynamoDB operations; however, <code>DeleteItem</code> does not recognize any values other than <code>NONE</code> or <code>ALL_OLD</code>.</p> </note>
            return_item_collection_metrics: <p>Determines whether item collection metrics are returned. If set to <code>SIZE</code>, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to <code>NONE</code> (the default), no statistics are returned.</p>
            condition_expression: <p>A condition that must be satisfied in order for a conditional <code>DeleteItem</code> to succeed.</p> <p>An expression can contain any of the following:</p> <ul> <li> <p>Functions: <code>attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size</code> </p> <p>These function names are case-sensitive.</p> </li> <li> <p>Comparison operators: <code>= | <> | < | > | <= | >= | BETWEEN | IN </code> </p> </li> <li> <p> Logical operators: <code>AND | OR | NOT</code> </p> </li> </ul> <p>For more information about condition expressions, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Condition Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_names: <p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information on expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_values: <p>One or more values that can be substituted in an expression.</p> <p>Use the <b>:</b> (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the <i>ProductStatus</i> attribute was one of the following: </p> <p> <code>Available | Backordered | Discontinued</code> </p> <p>You would first need to specify <code>ExpressionAttributeValues</code> as follows:</p> <p> <code>{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }</code> </p> <p>You could then use these values in an expression, such as this:</p> <p> <code>ProductStatus IN (:avail, :back, :disc)</code> </p> <p>For more information on expression attribute values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Condition Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            return_values_on_condition_check_failure: <p>An optional parameter that returns the item attributes for a <code>DeleteItem</code> operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>

        Raises:
            capo_dynamodb.errors.conditional_check_failed_exception.ConditionalCheckFailedException: <p>A condition specified in the operation failed to be evaluated.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.item_collection_size_limit_exceeded_exception.ItemCollectionSizeLimitExceededException: <p>An item collection is too large. This exception is only returned for tables that have one or more local secondary indexes.</p>
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.replicated_write_conflict_exception.ReplicatedWriteConflictException: <p>The request was rejected because one or more items in the request are being modified by a request in another Region. </p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.transaction_conflict_exception.TransactionConflictException: <p>Operation was rejected because there is an ongoing transaction for the item.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an item
            This example deletes an item from the Music table.

            >>> client.delete_item(table_name='Music', key={'Artist': {'S': 'No One You Know'}, 'SongTitle': {'S': 'Scared of My Shadow'}})
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.delete_item_input.DeleteItemInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.delete_item_output.DeleteItemOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.delete_item

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.delete_item.delete_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.delete_item_input.DeleteItemInput = {
            "table_name": table_name,
            "key": key,
        }
        if expected is not None:
            input_["expected"] = expected
        if conditional_operator is not None:
            input_["conditional_operator"] = conditional_operator
        if return_values is not None:
            input_["return_values"] = return_values
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity
        if return_item_collection_metrics is not None:
            input_["return_item_collection_metrics"] = return_item_collection_metrics
        if condition_expression is not None:
            input_["condition_expression"] = condition_expression
        if expression_attribute_names is not None:
            input_["expression_attribute_names"] = expression_attribute_names
        if expression_attribute_values is not None:
            input_["expression_attribute_values"] = expression_attribute_values
        if return_values_on_condition_check_failure is not None:
            input_["return_values_on_condition_check_failure"] = (
                return_values_on_condition_check_failure
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        resource_arn: "capo_dynamodb.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        expected_revision_id: Optional[
            "capo_dynamodb.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "capo_dynamodb.types.delete_resource_policy_output.DeleteResourcePolicyOutput":
        """<p>Deletes the resource-based policy attached to the resource, which can be a table or stream.</p> <p> <code>DeleteResourcePolicy</code> is an idempotent operation; running it multiple times on the same resource <i>doesn't</i> result in an error response, unless you specify an <code>ExpectedRevisionId</code>, which will then return a <code>PolicyNotFoundException</code>.</p> <important> <p>To make sure that you don't inadvertently lock yourself out of your own resources, the root principal in your Amazon Web Services account can perform <code>DeleteResourcePolicy</code> requests, even if your resource-based policy explicitly denies the root principal's access. </p> </important> <note> <p> <code>DeleteResourcePolicy</code> is an asynchronous operation. If you issue a <code>GetResourcePolicy</code> request immediately after running the <code>DeleteResourcePolicy</code> request, DynamoDB might still return the deleted policy. This is because the policy for your resource might not have been deleted yet. Wait for a few seconds, and then try the <code>GetResourcePolicy</code> request again.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the DynamoDB resource from which the policy will be removed. The resources you can specify include tables and streams. If you remove the policy of a table, it will also remove the permissions for the table's indexes defined in that policy document. This is because index permissions are defined in the table's policy.</p>
            expected_revision_id: <p>A string value that you can use to conditionally delete your policy. When you provide an expected revision ID, if the revision ID of the existing policy on the resource doesn't match or if there's no policy attached to the resource, the request will fail and return a <code>PolicyNotFoundException</code>.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.policy_not_found_exception.PolicyNotFoundException: <p>The operation tried to access a nonexistent resource-based policy.</p> <p>If you specified an <code>ExpectedRevisionId</code>, it's possible that a policy is present for the resource but its revision ID didn't match the expected value.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.delete_resource_policy_input.DeleteResourcePolicyInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.delete_resource_policy_output.DeleteResourcePolicyOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.delete_resource_policy

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.delete_resource_policy_input.DeleteResourcePolicyInput = {
            "resource_arn": resource_arn
        }
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_table(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.delete_table_output.DeleteTableOutput":
        """<p>The <code>DeleteTable</code> operation deletes a table and all of its items. After a <code>DeleteTable</code> request, the specified table is in the <code>DELETING</code> state until DynamoDB completes the deletion. If the table is in the <code>ACTIVE</code> state, you can delete it. If a table is in <code>CREATING</code> or <code>UPDATING</code> states, then DynamoDB returns a <code>ResourceInUseException</code>. If the specified table does not exist, DynamoDB returns a <code>ResourceNotFoundException</code>. If table is already in the <code>DELETING</code> state, no error is returned. </p> <note> <p>DynamoDB might continue to accept data read and write operations, such as <code>GetItem</code> and <code>PutItem</code>, on a table in the <code>DELETING</code> state until the table deletion is complete. For the full list of table states, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableDescription.html#DDB-Type-TableDescription-TableStatus">TableStatus</a>.</p> </note> <p>When you delete a table, any indexes on that table are also deleted.</p> <p>If you have DynamoDB Streams enabled on the table, then the corresponding stream on that table goes into the <code>DISABLED</code> state, and the stream is automatically deleted after 24 hours.</p> <p>Use the <code>DescribeTable</code> action to check the status of the table. </p>

        Args:
            table_name: <p>The name of the table to delete. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a table
            This example deletes the Music table.

            >>> client.delete_table(table_name='Music')
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.delete_table_input.DeleteTableInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.delete_table_output.DeleteTableOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.delete_table

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.delete_table.delete_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.delete_table_input.DeleteTableInput = {
            "table_name": table_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_backup(
        self,
        backup_arn: "capo_dynamodb.types.backup_arn.BackupArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.describe_backup_output.DescribeBackupOutput":
        """<p>Describes an existing backup of a table.</p> <p>You can call <code>DescribeBackup</code> at a maximum rate of 10 times per second.</p>

        Args:
            backup_arn: <p>The Amazon Resource Name (ARN) associated with the backup.</p>

        Raises:
            capo_dynamodb.errors.backup_not_found_exception.BackupNotFoundException: <p>Backup not found for the given BackupARN. </p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_backup_input.DescribeBackupInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_backup_output.DescribeBackupOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_backup

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_backup.describe_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_backup_input.DescribeBackupInput = {
            "backup_arn": backup_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_continuous_backups(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.describe_continuous_backups_output.DescribeContinuousBackupsOutput":
        """<p>Checks the status of continuous backups and point in time recovery on the specified table. Continuous backups are <code>ENABLED</code> on all tables at table creation. If point in time recovery is enabled, <code>PointInTimeRecoveryStatus</code> will be set to ENABLED.</p> <p> After continuous backups and point in time recovery are enabled, you can restore to any point in time within <code>EarliestRestorableDateTime</code> and <code>LatestRestorableDateTime</code>. </p> <p> <code>LatestRestorableDateTime</code> is typically 5 minutes before the current time. You can restore your table to any point in time in the last 35 days. You can set the recovery period to any value between 1 and 35 days. </p> <p>You can call <code>DescribeContinuousBackups</code> at a maximum rate of 10 times per second.</p>

        Args:
            table_name: <p>Name of the table for which the customer wants to check the continuous backups and point in time recovery settings.</p> <p>You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.table_not_found_exception.TableNotFoundException: <p>A source table with the name <code>TableName</code> does not currently exist within the subscriber's account or the subscriber is operating in the wrong Amazon Web Services Region.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_continuous_backups_input.DescribeContinuousBackupsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_continuous_backups_output.DescribeContinuousBackupsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_continuous_backups

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_continuous_backups.describe_continuous_backups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_continuous_backups_input.DescribeContinuousBackupsInput = {
            "table_name": table_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_contributor_insights(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        index_name: Optional["capo_dynamodb.types.index_name.IndexName"] = None,
    ) -> "capo_dynamodb.types.describe_contributor_insights_output.DescribeContributorInsightsOutput":
        """<p>Returns information about contributor insights for a given table or global secondary index.</p>

        Args:
            table_name: <p>The name of the table to describe. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            index_name: <p>The name of the global secondary index to describe, if applicable.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_contributor_insights_input.DescribeContributorInsightsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_contributor_insights_output.DescribeContributorInsightsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_contributor_insights

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_contributor_insights.describe_contributor_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_contributor_insights_input.DescribeContributorInsightsInput = {
            "table_name": table_name
        }
        if index_name is not None:
            input_["index_name"] = index_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_endpoints(
        self, *, config_overrides: Optional[DynamoDBClientConfig] = None
    ) -> "capo_dynamodb.types.describe_endpoints_response.DescribeEndpointsResponse":
        """<p>Returns the regional endpoint information. For more information on policy permissions, please see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/inter-network-traffic-privacy.html#inter-network-traffic-DescribeEndpoints">Internetwork traffic privacy</a>.</p>

        Raises:
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_endpoints_request.DescribeEndpointsRequest]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_endpoints_response.DescribeEndpointsResponse"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_endpoints

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_endpoints.describe_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_endpoints_request.DescribeEndpointsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_export(
        self,
        export_arn: "capo_dynamodb.types.export_arn.ExportArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.describe_export_output.DescribeExportOutput":
        """<p>Describes an existing table export.</p>

        Args:
            export_arn: <p>The Amazon Resource Name (ARN) associated with the export.</p>

        Raises:
            capo_dynamodb.errors.export_not_found_exception.ExportNotFoundException: <p>The specified export was not found.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_export_input.DescribeExportInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_export_output.DescribeExportOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_export

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_export.describe_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_export_input.DescribeExportInput = {
            "export_arn": export_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_global_table(
        self,
        global_table_name: "capo_dynamodb.types.table_name.TableName",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.describe_global_table_output.DescribeGlobalTableOutput":
        """<p>Returns information about the specified global table.</p> <important> <p>This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html">Global Tables version 2019.11.21 (Current)</a> when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).</p> <p>To determine which version you're using, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html">Determining the global table version you are using</a>. To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html">Upgrading global tables</a>.</p> </important>

        Args:
            global_table_name: <p>The name of the global table.</p>

        Raises:
            capo_dynamodb.errors.global_table_not_found_exception.GlobalTableNotFoundException: <p>The specified global table does not exist.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_global_table_input.DescribeGlobalTableInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_global_table_output.DescribeGlobalTableOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_global_table

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_global_table.describe_global_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_global_table_input.DescribeGlobalTableInput = {
            "global_table_name": global_table_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_global_table_settings(
        self,
        global_table_name: "capo_dynamodb.types.table_name.TableName",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.describe_global_table_settings_output.DescribeGlobalTableSettingsOutput":
        """<p>Describes Region-specific settings for a global table.</p> <important> <p>This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html">Global Tables version 2019.11.21 (Current)</a> when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).</p> <p>To determine which version you're using, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html">Determining the global table version you are using</a>. To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html">Upgrading global tables</a>.</p> </important>

        Args:
            global_table_name: <p>The name of the global table to describe.</p>

        Raises:
            capo_dynamodb.errors.global_table_not_found_exception.GlobalTableNotFoundException: <p>The specified global table does not exist.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_global_table_settings_input.DescribeGlobalTableSettingsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_global_table_settings_output.DescribeGlobalTableSettingsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_global_table_settings

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_global_table_settings.describe_global_table_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_global_table_settings_input.DescribeGlobalTableSettingsInput = {
            "global_table_name": global_table_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_import(
        self,
        import_arn: "capo_dynamodb.types.import_arn.ImportArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.describe_import_output.DescribeImportOutput":
        """<p> Represents the properties of the import. </p>

        Args:
            import_arn: <p> The Amazon Resource Name (ARN) associated with the table you're importing to. </p>

        Raises:
            capo_dynamodb.errors.import_not_found_exception.ImportNotFoundException: <p> The specified import was not found. </p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_import_input.DescribeImportInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_import_output.DescribeImportOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_import

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_import.describe_import(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_import_input.DescribeImportInput = {
            "import_arn": import_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_kinesis_streaming_destination(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.describe_kinesis_streaming_destination_output.DescribeKinesisStreamingDestinationOutput":
        """<p>Returns information about the status of Kinesis streaming.</p>

        Args:
            table_name: <p>The name of the table being described. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_kinesis_streaming_destination_input.DescribeKinesisStreamingDestinationInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_kinesis_streaming_destination_output.DescribeKinesisStreamingDestinationOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_kinesis_streaming_destination

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_kinesis_streaming_destination.describe_kinesis_streaming_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_kinesis_streaming_destination_input.DescribeKinesisStreamingDestinationInput = {
            "table_name": table_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_limits(
        self, *, config_overrides: Optional[DynamoDBClientConfig] = None
    ) -> "capo_dynamodb.types.describe_limits_output.DescribeLimitsOutput":
        """<p>Returns the current provisioned-capacity quotas for your Amazon Web Services account in a Region, both for the Region as a whole and for any one DynamoDB table that you create there.</p> <p>When you establish an Amazon Web Services account, the account has initial quotas on the maximum read capacity units and write capacity units that you can provision across all of your DynamoDB tables in a given Region. Also, there are per-table quotas that apply when you create a table there. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html">Service, Account, and Table Quotas</a> page in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>Although you can increase these quotas by filing a case at <a href="https://console.aws.amazon.com/support/home#/">Amazon Web Services Support Center</a>, obtaining the increase is not instantaneous. The <code>DescribeLimits</code> action lets you write code to compare the capacity you are currently using to those quotas imposed by your account so that you have enough time to apply for an increase before you hit a quota.</p> <p>For example, you could use one of the Amazon Web Services SDKs to do the following:</p> <ol> <li> <p>Call <code>DescribeLimits</code> for a particular Region to obtain your current account quotas on provisioned capacity there.</p> </li> <li> <p>Create a variable to hold the aggregate read capacity units provisioned for all your tables in that Region, and one to hold the aggregate write capacity units. Zero them both.</p> </li> <li> <p>Call <code>ListTables</code> to obtain a list of all your DynamoDB tables.</p> </li> <li> <p>For each table name listed by <code>ListTables</code>, do the following:</p> <ul> <li> <p>Call <code>DescribeTable</code> with the table name.</p> </li> <li> <p>Use the data returned by <code>DescribeTable</code> to add the read capacity units and write capacity units provisioned for the table itself to your variables.</p> </li> <li> <p>If the table has one or more global secondary indexes (GSIs), loop over these GSIs and add their provisioned capacity values to your variables as well.</p> </li> </ul> </li> <li> <p>Report the account quotas for that Region returned by <code>DescribeLimits</code>, along with the total current provisioned capacity levels you have calculated.</p> </li> </ol> <p>This will let you see whether you are getting close to your account-level quotas.</p> <p>The per-table quotas apply only when you are creating a new table. They restrict the sum of the provisioned capacity of the new table itself and all its global secondary indexes.</p> <p>For existing tables and their GSIs, DynamoDB doesn't let you increase provisioned capacity extremely rapidly, but the only quota that applies is that the aggregate provisioned capacity over all your tables and GSIs cannot exceed either of the per-account quotas.</p> <note> <p> <code>DescribeLimits</code> should only be called periodically. You can expect throttling errors if you call it more than once in a minute.</p> </note> <p>The <code>DescribeLimits</code> Request element has no content.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To determine capacity limits per table and account, in the current AWS region
            The following example returns the maximum read and write capacity units per table, and for the AWS account, in the current AWS region.

            >>> client.describe_limits()
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_limits_input.DescribeLimitsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_limits_output.DescribeLimitsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_limits

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_limits.describe_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_limits_input.DescribeLimitsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_table(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.describe_table_output.DescribeTableOutput":
        """<p>Returns information about the table, including the current status of the table, when it was created, the primary key schema, and any indexes on the table.</p> <note> <p>If you issue a <code>DescribeTable</code> request immediately after a <code>CreateTable</code> request, DynamoDB might return a <code>ResourceNotFoundException</code>. This is because <code>DescribeTable</code> uses an eventually consistent query, and the metadata for your table might not be available at that moment. Wait for a few seconds, and then try the <code>DescribeTable</code> request again.</p> </note>

        Args:
            table_name: <p>The name of the table to describe. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_table_input.DescribeTableInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_table_output.DescribeTableOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_table

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_table.describe_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_table_input.DescribeTableInput = {
            "table_name": table_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def wait_until_table_not_exists(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        max_wait_time: float,
        min_delay: float = 20,
        max_delay: float = 120,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> ServiceError:
        """Wait for table_not_exists.

        Args:
            table_name: <p>The name of the table to describe. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_dynamodb.types.describe_table_output.DescribeTableOutput | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = self.describe_table(  # noqa: F841
                    table_name, config_overrides=config_overrides
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("table_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            time.sleep(delay)
            attempt += 1

    def describe_table_replica_auto_scaling(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.describe_table_replica_auto_scaling_output.DescribeTableReplicaAutoScalingOutput":
        """<p>Describes auto scaling settings across replicas of the global table at once.</p>

        Args:
            table_name: <p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_table_replica_auto_scaling_input.DescribeTableReplicaAutoScalingInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_table_replica_auto_scaling_output.DescribeTableReplicaAutoScalingOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_table_replica_auto_scaling

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_table_replica_auto_scaling.describe_table_replica_auto_scaling(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_table_replica_auto_scaling_input.DescribeTableReplicaAutoScalingInput = {
            "table_name": table_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_time_to_live(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.describe_time_to_live_output.DescribeTimeToLiveOutput":
        """<p>Gives a description of the Time to Live (TTL) status on the specified table. </p>

        Args:
            table_name: <p>The name of the table to be described. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.describe_time_to_live_input.DescribeTimeToLiveInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.describe_time_to_live_output.DescribeTimeToLiveOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.describe_time_to_live

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.describe_time_to_live.describe_time_to_live(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.describe_time_to_live_input.DescribeTimeToLiveInput = {
            "table_name": table_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_kinesis_streaming_destination(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        stream_arn: "capo_dynamodb.types.stream_arn.StreamArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        enable_kinesis_streaming_configuration: Optional[
            "capo_dynamodb.types.enable_kinesis_streaming_configuration.EnableKinesisStreamingConfiguration"
        ] = None,
    ) -> "capo_dynamodb.types.kinesis_streaming_destination_output.KinesisStreamingDestinationOutput":
        """<p>Stops replication from the DynamoDB table to the Kinesis data stream. This is done without deleting either of the resources.</p>

        Args:
            table_name: <p>The name of the DynamoDB table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            stream_arn: <p>The ARN for a Kinesis data stream.</p>
            enable_kinesis_streaming_configuration: <p>The source for the Kinesis streaming information that is being enabled.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.kinesis_streaming_destination_input.KinesisStreamingDestinationInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.kinesis_streaming_destination_output.KinesisStreamingDestinationOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.disable_kinesis_streaming_destination

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.disable_kinesis_streaming_destination.disable_kinesis_streaming_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.kinesis_streaming_destination_input.KinesisStreamingDestinationInput = {
            "table_name": table_name,
            "stream_arn": stream_arn,
        }
        if enable_kinesis_streaming_configuration is not None:
            input_["enable_kinesis_streaming_configuration"] = (
                enable_kinesis_streaming_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_kinesis_streaming_destination(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        stream_arn: "capo_dynamodb.types.stream_arn.StreamArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        enable_kinesis_streaming_configuration: Optional[
            "capo_dynamodb.types.enable_kinesis_streaming_configuration.EnableKinesisStreamingConfiguration"
        ] = None,
    ) -> "capo_dynamodb.types.kinesis_streaming_destination_output.KinesisStreamingDestinationOutput":
        """<p>Starts table data replication to the specified Kinesis data stream at a timestamp chosen during the enable workflow. If this operation doesn't return results immediately, use DescribeKinesisStreamingDestination to check if streaming to the Kinesis data stream is ACTIVE.</p>

        Args:
            table_name: <p>The name of the DynamoDB table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            stream_arn: <p>The ARN for a Kinesis data stream.</p>
            enable_kinesis_streaming_configuration: <p>The source for the Kinesis streaming information that is being enabled.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.kinesis_streaming_destination_input.KinesisStreamingDestinationInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.kinesis_streaming_destination_output.KinesisStreamingDestinationOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.enable_kinesis_streaming_destination

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.enable_kinesis_streaming_destination.enable_kinesis_streaming_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.kinesis_streaming_destination_input.KinesisStreamingDestinationInput = {
            "table_name": table_name,
            "stream_arn": stream_arn,
        }
        if enable_kinesis_streaming_configuration is not None:
            input_["enable_kinesis_streaming_configuration"] = (
                enable_kinesis_streaming_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def execute_statement(
        self,
        statement: "capo_dynamodb.types.parti_ql_statement.PartiQLStatement",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        parameters: Optional[
            "capo_dynamodb.types.prepared_statement_parameters.PreparedStatementParameters"
        ] = None,
        consistent_read: Optional[
            "capo_dynamodb.types.consistent_read.ConsistentRead"
        ] = None,
        next_token: Optional[
            "capo_dynamodb.types.parti_ql_next_token.PartiQLNextToken"
        ] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        limit: Optional[
            "capo_dynamodb.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        return_values_on_condition_check_failure: Optional[
            "capo_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
        ] = None,
    ) -> "capo_dynamodb.types.execute_statement_output.ExecuteStatementOutput":
        """<p>This operation allows you to perform reads and singleton writes on data stored in DynamoDB, using PartiQL.</p> <p>For PartiQL reads (<code>SELECT</code> statement), if the total number of processed items exceeds the maximum dataset size limit of 1 MB, the read stops and results are returned to the user as a <code>LastEvaluatedKey</code> value to continue the read in a subsequent operation. If the filter criteria in <code>WHERE</code> clause does not match any data, the read will return an empty result set.</p> <p>A single <code>SELECT</code> statement response can return up to the maximum number of items (if using the Limit parameter) or a maximum of 1 MB of data (and then apply any filtering to the results using <code>WHERE</code> clause). If <code>LastEvaluatedKey</code> is present in the response, you need to paginate the result set. If <code>NextToken</code> is present, you need to paginate the result set and include <code>NextToken</code>.</p>

        Args:
            statement: <p>The PartiQL statement representing the operation to run.</p>
            parameters: <p>The parameters for the PartiQL statement, if any.</p>
            consistent_read: <p>The consistency of a read operation. If set to <code>true</code>, then a strongly consistent read is used; otherwise, an eventually consistent read is used.</p>
            next_token: <p>Set this value to get remaining results, if <code>NextToken</code> was returned in the statement response.</p>
            limit: <p>The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, along with a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation so you can pick up where you left off. Also, if the processed dataset size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation to continue the operation. </p>
            return_values_on_condition_check_failure: <p>An optional parameter that returns the item attributes for an <code>ExecuteStatement</code> operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>

        Raises:
            capo_dynamodb.errors.conditional_check_failed_exception.ConditionalCheckFailedException: <p>A condition specified in the operation failed to be evaluated.</p>
            capo_dynamodb.errors.duplicate_item_exception.DuplicateItemException: <p> There was an attempt to insert an item with the same primary key as an item that already exists in the DynamoDB table.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.item_collection_size_limit_exceeded_exception.ItemCollectionSizeLimitExceededException: <p>An item collection is too large. This exception is only returned for tables that have one or more local secondary indexes.</p>
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.transaction_conflict_exception.TransactionConflictException: <p>Operation was rejected because there is an ongoing transaction for the item.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.execute_statement_input.ExecuteStatementInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.execute_statement_output.ExecuteStatementOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.execute_statement

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.execute_statement.execute_statement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.execute_statement_input.ExecuteStatementInput = {
            "statement": statement
        }
        if parameters is not None:
            input_["parameters"] = parameters
        if consistent_read is not None:
            input_["consistent_read"] = consistent_read
        if next_token is not None:
            input_["next_token"] = next_token
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity
        if limit is not None:
            input_["limit"] = limit
        if return_values_on_condition_check_failure is not None:
            input_["return_values_on_condition_check_failure"] = (
                return_values_on_condition_check_failure
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def execute_transaction(
        self,
        transact_statements: "capo_dynamodb.types.parameterized_statements.ParameterizedStatements",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        client_request_token: Optional[
            "capo_dynamodb.types.client_request_token.ClientRequestToken"
        ] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
    ) -> "capo_dynamodb.types.execute_transaction_output.ExecuteTransactionOutput":
        """<p>This operation allows you to perform transactional reads or writes on data stored in DynamoDB, using PartiQL.</p> <note> <p>The entire transaction must consist of either read statements or write statements, you cannot mix both in one transaction. The EXISTS function is an exception and can be used to check the condition of specific attributes of the item in a similar manner to <code>ConditionCheck</code> in the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transaction-apis.html#transaction-apis-txwriteitems">TransactWriteItems</a> API.</p> </note>

        Args:
            transact_statements: <p>The list of PartiQL statements representing the transaction to run.</p>
            client_request_token: <p>Set this value to get remaining results, if <code>NextToken</code> was returned in the statement response.</p>
            return_consumed_capacity: <p>Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactGetItems.html">TransactGetItems</a> and <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html">TransactWriteItems</a>.</p>

        Raises:
            capo_dynamodb.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>DynamoDB rejected the request because you retried a request with a different payload but with an idempotent token that was already used.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.transaction_canceled_exception.TransactionCanceledException: <p>The entire transaction request was canceled.</p> <p>DynamoDB cancels a <code>TransactWriteItems</code> request under the following circumstances:</p> <ul> <li> <p>A condition in one of the condition expressions is not met.</p> </li> <li> <p>A table in the <code>TransactWriteItems</code> request is in a different account or region.</p> </li> <li> <p>More than one action in the <code>TransactWriteItems</code> operation targets the same item.</p> </li> <li> <p>There is insufficient provisioned capacity for the transaction to be completed.</p> </li> <li> <p>An item size becomes too large (larger than 400 KB), or a local secondary index (LSI) becomes too large, or a similar validation error occurs because of changes made by the transaction.</p> </li> <li> <p>There is a user error, such as an invalid data format.</p> </li> <li> <p> There is an ongoing <code>TransactWriteItems</code> operation that conflicts with a concurrent <code>TransactWriteItems</code> request. In this case the <code>TransactWriteItems</code> operation fails with a <code>TransactionCanceledException</code>. </p> </li> </ul> <p>DynamoDB cancels a <code>TransactGetItems</code> request under the following circumstances:</p> <ul> <li> <p>There is an ongoing <code>TransactGetItems</code> operation that conflicts with a concurrent <code>PutItem</code>, <code>UpdateItem</code>, <code>DeleteItem</code> or <code>TransactWriteItems</code> request. In this case the <code>TransactGetItems</code> operation fails with a <code>TransactionCanceledException</code>.</p> </li> <li> <p>A table in the <code>TransactGetItems</code> request is in a different account or region.</p> </li> <li> <p>There is insufficient provisioned capacity for the transaction to be completed.</p> </li> <li> <p>There is a user error, such as an invalid data format.</p> </li> </ul> <note> <p>DynamoDB lists the cancellation reasons on the <code>CancellationReasons</code> property. Transaction cancellation reasons are ordered in the order of requested items, if an item has no error it will have <code>None</code> code and <code>Null</code> message. The <code>None</code> code is returned as the literal string <code>"None"</code>, not a null or absent value; the message field is omitted entirely for an item that has no error. This is important to note when using an SDK that surfaces the code as an optional or nullable type.</p> </note> <p>Cancellation reason codes and possible error messages:</p> <ul> <li> <p>No Errors:</p> <ul> <li> <p>Code: <code>None</code> </p> </li> <li> <p>Message: <code>null</code> </p> </li> </ul> </li> <li> <p>Conditional Check Failed:</p> <ul> <li> <p>Code: <code>ConditionalCheckFailed</code> </p> </li> <li> <p>Message: The conditional request failed. </p> </li> </ul> </li> <li> <p>Item Collection Size Limit Exceeded:</p> <ul> <li> <p>Code: <code>ItemCollectionSizeLimitExceeded</code> </p> </li> <li> <p>Message: Collection size exceeded.</p> </li> </ul> </li> <li> <p>Transaction Conflict:</p> <ul> <li> <p>Code: <code>TransactionConflict</code> </p> </li> <li> <p>Message: Transaction is ongoing for the item.</p> </li> </ul> </li> <li> <p>Provisioned Throughput Exceeded:</p> <ul> <li> <p>Code: <code>ProvisionedThroughputExceeded</code> </p> </li> <li> <p>Messages:</p> <ul> <li> <p>The level of configured provisioned throughput for the table was exceeded. Consider increasing your provisioning level with the UpdateTable API.</p> <note> <p>This Message is received when provisioned throughput is exceeded is on a provisioned DynamoDB table.</p> </note> </li> <li> <p>The level of configured provisioned throughput for one or more global secondary indexes of the table was exceeded. Consider increasing your provisioning level for the under-provisioned global secondary indexes with the UpdateTable API.</p> <note> <p>This message is returned when provisioned throughput is exceeded is on a provisioned GSI.</p> </note> </li> </ul> </li> </ul> </li> <li> <p>Throttling Error:</p> <ul> <li> <p>Code: <code>ThrottlingError</code> </p> </li> <li> <p>Messages: </p> <ul> <li> <p>Throughput exceeds the current capacity of your table or index. DynamoDB is automatically scaling your table or index so please try again shortly. If exceptions persist, check if you have a hot key: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html.</p> <note> <p>This message is returned when writes get throttled on an On-Demand table as DynamoDB is automatically scaling the table.</p> </note> </li> <li> <p>Throughput exceeds the current capacity for one or more global secondary indexes. DynamoDB is automatically scaling your index so please try again shortly.</p> <note> <p>This message is returned when writes get throttled on an On-Demand GSI as DynamoDB is automatically scaling the GSI.</p> </note> </li> </ul> </li> </ul> </li> <li> <p>Validation Error:</p> <ul> <li> <p>Code: <code>ValidationError</code> </p> </li> <li> <p>Messages: </p> <ul> <li> <p>One or more parameter values were invalid.</p> </li> <li> <p>The update expression attempted to update the secondary index key beyond allowed size limits.</p> </li> <li> <p>The update expression attempted to update the secondary index key to unsupported type.</p> </li> <li> <p>An operand in the update expression has an incorrect data type.</p> </li> <li> <p>Item size to update has exceeded the maximum allowed size.</p> </li> <li> <p>Number overflow. Attempting to store a number with magnitude larger than supported range.</p> </li> <li> <p>Type mismatch for attribute to update.</p> </li> <li> <p>Nesting Levels have exceeded supported limits.</p> </li> <li> <p>The document path provided in the update expression is invalid for update.</p> </li> <li> <p>The provided expression refers to an attribute that does not exist in the item.</p> </li> </ul> </li> </ul> </li> </ul>
            capo_dynamodb.errors.transaction_in_progress_exception.TransactionInProgressException: <p>The transaction with the given request token is already in progress.</p> <p> Recommended Settings </p> <note> <p> This is a general recommendation for handling the <code>TransactionInProgressException</code>. These settings help ensure that the client retries will trigger completion of the ongoing <code>TransactWriteItems</code> request. </p> </note> <ul> <li> <p> Set <code>clientExecutionTimeout</code> to a value that allows at least one retry to be processed after 5 seconds have elapsed since the first attempt for the <code>TransactWriteItems</code> operation. </p> </li> <li> <p> Set <code>socketTimeout</code> to a value a little lower than the <code>requestTimeout</code> setting. </p> </li> <li> <p> <code>requestTimeout</code> should be set based on the time taken for the individual retries of a single HTTP request for your use case, but setting it to 1 second or higher should work well to reduce chances of retries and <code>TransactionInProgressException</code> errors. </p> </li> <li> <p> Use exponential backoff when retrying and tune backoff if needed. </p> </li> </ul> <p> Assuming <a href="https://github.com/aws/aws-sdk-java/blob/fd409dee8ae23fb8953e0bb4dbde65536a7e0514/aws-java-sdk-core/src/main/java/com/amazonaws/retry/PredefinedRetryPolicies.java#L97">default retry policy</a>, example timeout settings based on the guidelines above are as follows: </p> <p>Example timeline:</p> <ul> <li> <p>0-1000 first attempt</p> </li> <li> <p>1000-1500 first sleep/delay (default retry policy uses 500 ms as base delay for 4xx errors)</p> </li> <li> <p>1500-2500 second attempt</p> </li> <li> <p>2500-3500 second sleep/delay (500 * 2, exponential backoff)</p> </li> <li> <p>3500-4500 third attempt</p> </li> <li> <p>4500-6500 third sleep/delay (500 * 2^2)</p> </li> <li> <p>6500-7500 fourth attempt (this can trigger inline recovery since 5 seconds have elapsed since the first attempt reached TC)</p> </li> </ul>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.execute_transaction_input.ExecuteTransactionInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.execute_transaction_output.ExecuteTransactionOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.execute_transaction

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.execute_transaction.execute_transaction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.execute_transaction_input.ExecuteTransactionInput = {
            "transact_statements": transact_statements
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_table_to_point_in_time(
        self,
        table_arn: "capo_dynamodb.types.table_arn.TableArn",
        s3_bucket: "capo_dynamodb.types.s3_bucket.S3Bucket",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        export_time: Optional["capo_dynamodb.types.export_time.ExportTime"] = None,
        client_token: Optional["capo_dynamodb.types.client_token.ClientToken"] = None,
        s3_bucket_owner: Optional[
            "capo_dynamodb.types.s3_bucket_owner.S3BucketOwner"
        ] = None,
        s3_prefix: Optional["capo_dynamodb.types.s3_prefix.S3Prefix"] = None,
        s3_sse_algorithm: Optional[
            "capo_dynamodb.types.s3_sse_algorithm.S3SseAlgorithm"
        ] = None,
        s3_sse_kms_key_id: Optional[
            "capo_dynamodb.types.s3_sse_kms_key_id.S3SseKmsKeyId"
        ] = None,
        export_format: Optional[
            "capo_dynamodb.types.export_format.ExportFormat"
        ] = None,
        export_type: Optional["capo_dynamodb.types.export_type.ExportType"] = None,
        incremental_export_specification: Optional[
            "capo_dynamodb.types.incremental_export_specification.IncrementalExportSpecification"
        ] = None,
        filter_specification: Optional[
            "capo_dynamodb.types.filter_specification.FilterSpecification"
        ] = None,
    ) -> "capo_dynamodb.types.export_table_to_point_in_time_output.ExportTableToPointInTimeOutput":
        """<p>Exports table data to an S3 bucket. The table must have point in time recovery enabled, and you can export data from any time within the point in time recovery window.</p>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) associated with the table to export.</p>
            export_time: <p>Time in the past from which to export table data, counted in seconds from the start of the Unix epoch. The table export will be a snapshot of the table's state at this point in time.</p>
            client_token: <p>Providing a <code>ClientToken</code> makes the call to <code>ExportTableToPointInTimeInput</code> idempotent, meaning that multiple identical calls have the same effect as one single call.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After 8 hours, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 8 hours, or the result might not be idempotent.</p> <p>If you submit a request with the same client token but a change in other parameters within the 8-hour idempotency window, DynamoDB returns an <code>ExportConflictException</code>.</p>
            s3_bucket: <p>The name of the Amazon S3 bucket to export the snapshot to.</p>
            s3_bucket_owner: <p>The ID of the Amazon Web Services account that owns the bucket the export will be stored in.</p> <note> <p>S3BucketOwner is a required parameter when exporting to a S3 bucket in another account.</p> </note>
            s3_prefix: <p>The Amazon S3 bucket prefix to use as the file name and path of the exported snapshot.</p>
            s3_sse_algorithm: <p>Type of encryption used on the bucket where export data will be stored. Valid values for <code>S3SseAlgorithm</code> are:</p> <ul> <li> <p> <code>AES256</code> - server-side encryption with Amazon S3 managed keys</p> </li> <li> <p> <code>KMS</code> - server-side encryption with KMS managed keys</p> </li> </ul>
            s3_sse_kms_key_id: <p>The ID of the KMS managed key used to encrypt the S3 bucket where export data will be stored (if applicable).</p>
            export_format: <p>The format for the exported data. Valid values for <code>ExportFormat</code> are <code>DYNAMODB_JSON</code> or <code>ION</code>.</p>
            export_type: <p>Choice of whether to execute as a full export or incremental export. Valid values are FULL_EXPORT or INCREMENTAL_EXPORT. The default value is FULL_EXPORT. If INCREMENTAL_EXPORT is provided, the IncrementalExportSpecification must also be used.</p>
            incremental_export_specification: <p>Optional object containing the parameters specific to an incremental export.</p>
            filter_specification: <p>The criteria used to filter which items are included in the point-in-time export. When you specify this parameter, only items that match the key conditions and filter expressions are exported.</p>

        Raises:
            capo_dynamodb.errors.export_conflict_exception.ExportConflictException: <p>There was a conflict when writing to the specified S3 bucket.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_export_time_exception.InvalidExportTimeException: <p>The specified <code>ExportTime</code> is outside of the point in time recovery window.</p>
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.point_in_time_recovery_unavailable_exception.PointInTimeRecoveryUnavailableException: <p>Point in time recovery has not yet been enabled for this source table.</p>
            capo_dynamodb.errors.table_not_found_exception.TableNotFoundException: <p>A source table with the name <code>TableName</code> does not currently exist within the subscriber's account or the subscriber is operating in the wrong Amazon Web Services Region.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.export_table_to_point_in_time_input.ExportTableToPointInTimeInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.export_table_to_point_in_time_output.ExportTableToPointInTimeOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.export_table_to_point_in_time

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.export_table_to_point_in_time.export_table_to_point_in_time(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.export_table_to_point_in_time_input.ExportTableToPointInTimeInput = {
            "table_arn": table_arn,
            "s3_bucket": s3_bucket,
        }
        if export_time is not None:
            input_["export_time"] = export_time
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if s3_bucket_owner is not None:
            input_["s3_bucket_owner"] = s3_bucket_owner
        if s3_prefix is not None:
            input_["s3_prefix"] = s3_prefix
        if s3_sse_algorithm is not None:
            input_["s3_sse_algorithm"] = s3_sse_algorithm
        if s3_sse_kms_key_id is not None:
            input_["s3_sse_kms_key_id"] = s3_sse_kms_key_id
        if export_format is not None:
            input_["export_format"] = export_format
        if export_type is not None:
            input_["export_type"] = export_type
        if incremental_export_specification is not None:
            input_["incremental_export_specification"] = (
                incremental_export_specification
            )
        if filter_specification is not None:
            input_["filter_specification"] = filter_specification

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_item(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        key: "capo_dynamodb.types.key.Key",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        attributes_to_get: Optional[
            "capo_dynamodb.types.attribute_name_list.AttributeNameList"
        ] = None,
        consistent_read: Optional[
            "capo_dynamodb.types.consistent_read.ConsistentRead"
        ] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        projection_expression: Optional[
            "capo_dynamodb.types.projection_expression.ProjectionExpression"
        ] = None,
        expression_attribute_names: Optional[
            "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
        ] = None,
    ) -> "capo_dynamodb.types.get_item_output.GetItemOutput":
        """<p>The <code>GetItem</code> operation returns a set of attributes for the item with the given primary key. If there is no matching item, <code>GetItem</code> does not return any data and there will be no <code>Item</code> element in the response.</p> <p> <code>GetItem</code> provides an eventually consistent read by default. If your application requires a strongly consistent read, set <code>ConsistentRead</code> to <code>true</code>. Although a strongly consistent read might take more time than an eventually consistent read, it always returns the last updated value.</p>

        Args:
            table_name: <p>The name of the table containing the requested item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            key: <p>A map of attribute names to <code>AttributeValue</code> objects, representing the primary key of the item to retrieve.</p> <p>For the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.</p>
            attributes_to_get: <p>This is a legacy parameter. Use <code>ProjectionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html">AttributesToGet</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            consistent_read: <p>Determines the read consistency model: If set to <code>true</code>, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.</p>
            projection_expression: <p>A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.</p> <p>If no attribute names are specified, then all attributes are returned. If any of the requested attributes are not found, they do not appear in the result.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_names: <p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information on expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To read an item from a table
            This example retrieves an item from the Music table. The table has a partition key and a sort key (Artist and SongTitle), so you must specify both of these attributes.

            >>> client.get_item(table_name='Music', key={'Artist': {'S': 'Acme Band'}, 'SongTitle': {'S': 'Happy Day'}})
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.get_item_input.GetItemInput]",
        ) -> OperationResponse["capo_dynamodb.types.get_item_output.GetItemOutput"]:
            import capo_dynamodb._operations.dynamo_db_20120810.get_item

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.get_item.get_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.get_item_input.GetItemInput = {
            "table_name": table_name,
            "key": key,
        }
        if attributes_to_get is not None:
            input_["attributes_to_get"] = attributes_to_get
        if consistent_read is not None:
            input_["consistent_read"] = consistent_read
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity
        if projection_expression is not None:
            input_["projection_expression"] = projection_expression
        if expression_attribute_names is not None:
            input_["expression_attribute_names"] = expression_attribute_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "capo_dynamodb.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.get_resource_policy_output.GetResourcePolicyOutput":
        """<p>Returns the resource-based policy document attached to the resource, which can be a table or stream, in JSON format.</p> <p> <code>GetResourcePolicy</code> follows an <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html"> <i>eventually consistent</i> </a> model. The following list describes the outcomes when you issue the <code>GetResourcePolicy</code> request immediately after issuing another request:</p> <ul> <li> <p>If you issue a <code>GetResourcePolicy</code> request immediately after a <code>PutResourcePolicy</code> request, DynamoDB might return a <code>PolicyNotFoundException</code>.</p> </li> <li> <p>If you issue a <code>GetResourcePolicy</code>request immediately after a <code>DeleteResourcePolicy</code> request, DynamoDB might return the policy that was present before the deletion request.</p> </li> <li> <p>If you issue a <code>GetResourcePolicy</code> request immediately after a <code>CreateTable</code> request, which includes a resource-based policy, DynamoDB might return a <code>ResourceNotFoundException</code> or a <code>PolicyNotFoundException</code>.</p> </li> </ul> <p>Because <code>GetResourcePolicy</code> uses an <i>eventually consistent</i> query, the metadata for your policy or table might not be available at that moment. Wait for a few seconds, and then retry the <code>GetResourcePolicy</code> request.</p> <p>After a <code>GetResourcePolicy</code> request returns a policy created using the <code>PutResourcePolicy</code> request, the policy will be applied in the authorization of requests to the resource. Because this process is eventually consistent, it will take some time to apply the policy to all requests to a resource. Policies that you attach while creating a table using the <code>CreateTable</code> request will always be applied to all requests for that table.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the DynamoDB resource to which the policy is attached. The resources you can specify include tables and streams.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.policy_not_found_exception.PolicyNotFoundException: <p>The operation tried to access a nonexistent resource-based policy.</p> <p>If you specified an <code>ExpectedRevisionId</code>, it's possible that a policy is present for the resource but its revision ID didn't match the expected value.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.get_resource_policy_input.GetResourcePolicyInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.get_resource_policy_output.GetResourcePolicyOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.get_resource_policy

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.get_resource_policy_input.GetResourcePolicyInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_table(
        self,
        s3_bucket_source: "capo_dynamodb.types.s3_bucket_source.S3BucketSource",
        input_format: "capo_dynamodb.types.input_format.InputFormat",
        table_creation_parameters: "capo_dynamodb.types.table_creation_parameters.TableCreationParameters",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        client_token: Optional["capo_dynamodb.types.client_token.ClientToken"] = None,
        input_format_options: Optional[
            "capo_dynamodb.types.input_format_options.InputFormatOptions"
        ] = None,
        input_compression_type: Optional[
            "capo_dynamodb.types.input_compression_type.InputCompressionType"
        ] = None,
    ) -> "capo_dynamodb.types.import_table_output.ImportTableOutput":
        """<p> Imports table data from an S3 bucket. </p>

        Args:
            client_token: <p>Providing a <code>ClientToken</code> makes the call to <code>ImportTableInput</code> idempotent, meaning that multiple identical calls have the same effect as one single call.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After 8 hours, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 8 hours, or the result might not be idempotent.</p> <p>If you submit a request with the same client token but a change in other parameters within the 8-hour idempotency window, DynamoDB returns an <code>IdempotentParameterMismatch</code> exception.</p>
            s3_bucket_source: <p> The S3 bucket that provides the source for the import. </p>
            input_format: <p> The format of the source data. Valid values for <code>ImportFormat</code> are <code>CSV</code>, <code>DYNAMODB_JSON</code> or <code>ION</code>. </p>
            input_format_options: <p> Additional properties that specify how the input is formatted, </p>
            input_compression_type: <p> Type of compression to be used on the input coming from the imported table. </p>
            table_creation_parameters: <p>Parameters for the table to import the data into. </p>

        Raises:
            capo_dynamodb.errors.import_conflict_exception.ImportConflictException: <p> There was a conflict when importing from the specified S3 source. This can occur when the current import conflicts with a previous import request that had the same client token. </p>
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.import_table_input.ImportTableInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.import_table_output.ImportTableOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.import_table

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.import_table.import_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.import_table_input.ImportTableInput = {
            "s3_bucket_source": s3_bucket_source,
            "input_format": input_format,
            "table_creation_parameters": table_creation_parameters,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if input_format_options is not None:
            input_["input_format_options"] = input_format_options
        if input_compression_type is not None:
            input_["input_compression_type"] = input_compression_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_backups(
        self,
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        table_name: Optional["capo_dynamodb.types.table_arn.TableArn"] = None,
        limit: Optional[
            "capo_dynamodb.types.backups_input_limit.BackupsInputLimit"
        ] = None,
        time_range_lower_bound: Optional[
            "capo_dynamodb.types.time_range_lower_bound.TimeRangeLowerBound"
        ] = None,
        time_range_upper_bound: Optional[
            "capo_dynamodb.types.time_range_upper_bound.TimeRangeUpperBound"
        ] = None,
        exclusive_start_backup_arn: Optional[
            "capo_dynamodb.types.backup_arn.BackupArn"
        ] = None,
        backup_type: Optional[
            "capo_dynamodb.types.backup_type_filter.BackupTypeFilter"
        ] = None,
    ) -> "capo_dynamodb.types.list_backups_output.ListBackupsOutput":
        """<p>List DynamoDB backups that are associated with an Amazon Web Services account and weren't made with Amazon Web Services Backup. To list these backups for a given table, specify <code>TableName</code>. <code>ListBackups</code> returns a paginated list of results with at most 1 MB worth of items in a page. You can also specify a maximum number of entries to be returned in a page.</p> <p>In the request, start time is inclusive, but end time is exclusive. Note that these boundaries are for the time at which the original backup was requested.</p> <p>You can call <code>ListBackups</code> a maximum of five times per second.</p> <p>If you want to retrieve the complete list of backups made with Amazon Web Services Backup, use the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ListBackupJobs.html">Amazon Web Services Backup list API.</a> </p>

        Args:
            table_name: <p>Lists the backups from the table specified in <code>TableName</code>. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            limit: <p>Maximum number of backups to return at once.</p>
            time_range_lower_bound: <p>Only backups created after this time are listed. <code>TimeRangeLowerBound</code> is inclusive.</p>
            time_range_upper_bound: <p>Only backups created before this time are listed. <code>TimeRangeUpperBound</code> is exclusive. </p>
            exclusive_start_backup_arn: <p> <code>LastEvaluatedBackupArn</code> is the Amazon Resource Name (ARN) of the backup last evaluated when the current page of results was returned, inclusive of the current page of results. This value may be specified as the <code>ExclusiveStartBackupArn</code> of a new <code>ListBackups</code> operation in order to fetch the next page of results. </p>
            backup_type: <p>The backups from the table specified by <code>BackupType</code> are listed.</p> <p>Where <code>BackupType</code> can be:</p> <ul> <li> <p> <code>USER</code> - On-demand backup created by you. (The default setting if no other backup types are specified.)</p> </li> <li> <p> <code>SYSTEM</code> - On-demand backup automatically created by DynamoDB.</p> </li> <li> <p> <code>ALL</code> - All types of on-demand backups (USER and SYSTEM).</p> </li> </ul>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.list_backups_input.ListBackupsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.list_backups_output.ListBackupsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.list_backups

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.list_backups.list_backups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.list_backups_input.ListBackupsInput = {}
        if table_name is not None:
            input_["table_name"] = table_name
        if limit is not None:
            input_["limit"] = limit
        if time_range_lower_bound is not None:
            input_["time_range_lower_bound"] = time_range_lower_bound
        if time_range_upper_bound is not None:
            input_["time_range_upper_bound"] = time_range_upper_bound
        if exclusive_start_backup_arn is not None:
            input_["exclusive_start_backup_arn"] = exclusive_start_backup_arn
        if backup_type is not None:
            input_["backup_type"] = backup_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_contributor_insights(
        self,
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        table_name: Optional["capo_dynamodb.types.table_arn.TableArn"] = None,
        next_token: Optional[
            "capo_dynamodb.types.next_token_string.NextTokenString"
        ] = None,
        max_results: Optional[
            "capo_dynamodb.types.list_contributor_insights_limit.ListContributorInsightsLimit"
        ] = None,
    ) -> "capo_dynamodb.types.list_contributor_insights_output.ListContributorInsightsOutput":
        """<p>Returns a list of ContributorInsightsSummary for a table and all its global secondary indexes.</p>

        Args:
            table_name: <p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            next_token: <p>A token to for the desired page, if there is one.</p>
            max_results: <p>Maximum number of results to return per page.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.list_contributor_insights_input.ListContributorInsightsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.list_contributor_insights_output.ListContributorInsightsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.list_contributor_insights

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.list_contributor_insights.list_contributor_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.list_contributor_insights_input.ListContributorInsightsInput = {}
        if table_name is not None:
            input_["table_name"] = table_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_contributor_insights(
        self,
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        table_name: Optional["capo_dynamodb.types.table_arn.TableArn"] = None,
        next_token: Optional[
            "capo_dynamodb.types.next_token_string.NextTokenString"
        ] = None,
        max_results: Optional[
            "capo_dynamodb.types.list_contributor_insights_limit.ListContributorInsightsLimit"
        ] = None,
    ) -> "Iterator[capo_dynamodb.types.list_contributor_insights_output.ListContributorInsightsOutput]":
        _token = next_token
        while True:
            _response = self.list_contributor_insights(
                config_overrides=config_overrides,
                table_name=table_name,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_exports(
        self,
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        table_arn: Optional["capo_dynamodb.types.table_arn.TableArn"] = None,
        max_results: Optional[
            "capo_dynamodb.types.list_exports_max_limit.ListExportsMaxLimit"
        ] = None,
        next_token: Optional[
            "capo_dynamodb.types.export_next_token.ExportNextToken"
        ] = None,
    ) -> "capo_dynamodb.types.list_exports_output.ListExportsOutput":
        """<p>Lists completed exports within the past 90 days, in reverse alphanumeric order of <code>ExportArn</code>.</p>

        Args:
            table_arn: <p>The Amazon Resource Name (ARN) associated with the exported table.</p>
            max_results: <p>Maximum number of results to return per page.</p>
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to <code>ListExports</code>. When provided in this manner, the API fetches the next page of results.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.list_exports_input.ListExportsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.list_exports_output.ListExportsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.list_exports

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.list_exports.list_exports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.list_exports_input.ListExportsInput = {}
        if table_arn is not None:
            input_["table_arn"] = table_arn
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

    def iter_list_exports(
        self,
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        table_arn: Optional["capo_dynamodb.types.table_arn.TableArn"] = None,
        max_results: Optional[
            "capo_dynamodb.types.list_exports_max_limit.ListExportsMaxLimit"
        ] = None,
        next_token: Optional[
            "capo_dynamodb.types.export_next_token.ExportNextToken"
        ] = None,
    ) -> "Iterator[capo_dynamodb.types.list_exports_output.ListExportsOutput]":
        _token = next_token
        while True:
            _response = self.list_exports(
                config_overrides=config_overrides,
                table_arn=table_arn,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_global_tables(
        self,
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        exclusive_start_global_table_name: Optional[
            "capo_dynamodb.types.table_name.TableName"
        ] = None,
        limit: Optional[
            "capo_dynamodb.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        region_name: Optional["capo_dynamodb.types.region_name.RegionName"] = None,
    ) -> "capo_dynamodb.types.list_global_tables_output.ListGlobalTablesOutput":
        """<p>Lists all global tables that have a replica in the specified Region.</p> <important> <p>This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html">Global Tables version 2019.11.21 (Current)</a> when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).</p> <p>To determine which version you're using, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html">Determining the global table version you are using</a>. To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html">Upgrading global tables</a>.</p> </important>

        Args:
            exclusive_start_global_table_name: <p>The first global table name that this operation will evaluate.</p>
            limit: <p>The maximum number of table names to return, if the parameter is not specified DynamoDB defaults to 100.</p> <p>If the number of global tables DynamoDB finds reaches this limit, it stops the operation and returns the table names collected up to that point, with a table name in the <code>LastEvaluatedGlobalTableName</code> to apply in a subsequent operation to the <code>ExclusiveStartGlobalTableName</code> parameter.</p>
            region_name: <p>Lists the global tables in a specific Region.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.list_global_tables_input.ListGlobalTablesInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.list_global_tables_output.ListGlobalTablesOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.list_global_tables

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.list_global_tables.list_global_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.list_global_tables_input.ListGlobalTablesInput = {}
        if exclusive_start_global_table_name is not None:
            input_["exclusive_start_global_table_name"] = (
                exclusive_start_global_table_name
            )
        if limit is not None:
            input_["limit"] = limit
        if region_name is not None:
            input_["region_name"] = region_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_imports(
        self,
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        table_arn: Optional["capo_dynamodb.types.table_arn.TableArn"] = None,
        page_size: Optional[
            "capo_dynamodb.types.list_imports_max_limit.ListImportsMaxLimit"
        ] = None,
        next_token: Optional[
            "capo_dynamodb.types.import_next_token.ImportNextToken"
        ] = None,
    ) -> "capo_dynamodb.types.list_imports_output.ListImportsOutput":
        """<p> Lists completed imports within the past 90 days. </p>

        Args:
            table_arn: <p> The Amazon Resource Name (ARN) associated with the table that was imported to. </p>
            page_size: <p> The number of <code>ImportSummary </code>objects returned in a single page. </p>
            next_token: <p> An optional string that, if supplied, must be copied from the output of a previous call to <code>ListImports</code>. When provided in this manner, the API fetches the next page of results. </p>

        Raises:
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.list_imports_input.ListImportsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.list_imports_output.ListImportsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.list_imports

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.list_imports.list_imports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.list_imports_input.ListImportsInput = {}
        if table_arn is not None:
            input_["table_arn"] = table_arn
        if page_size is not None:
            input_["page_size"] = page_size
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_imports(
        self,
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        table_arn: Optional["capo_dynamodb.types.table_arn.TableArn"] = None,
        page_size: Optional[
            "capo_dynamodb.types.list_imports_max_limit.ListImportsMaxLimit"
        ] = None,
        next_token: Optional[
            "capo_dynamodb.types.import_next_token.ImportNextToken"
        ] = None,
    ) -> "Iterator[capo_dynamodb.types.list_imports_output.ListImportsOutput]":
        _token = next_token
        while True:
            _response = self.list_imports(
                config_overrides=config_overrides,
                table_arn=table_arn,
                page_size=page_size,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tables(
        self,
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        exclusive_start_table_name: Optional[
            "capo_dynamodb.types.table_name.TableName"
        ] = None,
        limit: Optional[
            "capo_dynamodb.types.list_tables_input_limit.ListTablesInputLimit"
        ] = None,
    ) -> "capo_dynamodb.types.list_tables_output.ListTablesOutput":
        """<p>Returns an array of table names associated with the current account and endpoint. The output from <code>ListTables</code> is paginated, with each page returning a maximum of 100 table names.</p>

        Args:
            exclusive_start_table_name: <p>The first table name that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedTableName</code> in a previous operation, so that you can obtain the next page of results.</p>
            limit: <p>A maximum number of table names to return. If this parameter is not specified, the limit is 100.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list tables
            This example lists all of the tables associated with the current AWS account and endpoint.

            >>> client.list_tables()
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.list_tables_input.ListTablesInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.list_tables_output.ListTablesOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.list_tables

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.list_tables.list_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.list_tables_input.ListTablesInput = {}
        if exclusive_start_table_name is not None:
            input_["exclusive_start_table_name"] = exclusive_start_table_name
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_tables(
        self,
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        exclusive_start_table_name: Optional[
            "capo_dynamodb.types.table_name.TableName"
        ] = None,
        limit: Optional[
            "capo_dynamodb.types.list_tables_input_limit.ListTablesInputLimit"
        ] = None,
    ) -> "Iterator[capo_dynamodb.types.table_name.TableName]":
        _token = exclusive_start_table_name
        while True:
            _response = self.list_tables(
                config_overrides=config_overrides,
                exclusive_start_table_name=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("table_names",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("last_evaluated_table_name",))
            if not _token:
                break

    def list_tags_of_resource(
        self,
        resource_arn: "capo_dynamodb.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        next_token: Optional[
            "capo_dynamodb.types.next_token_string.NextTokenString"
        ] = None,
    ) -> "capo_dynamodb.types.list_tags_of_resource_output.ListTagsOfResourceOutput":
        """<p>List all tags on an Amazon DynamoDB resource. You can call ListTagsOfResource up to 10 times per second, per account.</p> <p>For an overview on tagging DynamoDB resources, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html">Tagging for DynamoDB</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The Amazon DynamoDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).</p>
            next_token: <p>An optional string that, if supplied, must be copied from the output of a previous call to ListTagOfResource. When provided in this manner, this API fetches the next page of results.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.list_tags_of_resource_input.ListTagsOfResourceInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.list_tags_of_resource_output.ListTagsOfResourceOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.list_tags_of_resource

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.list_tags_of_resource.list_tags_of_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.list_tags_of_resource_input.ListTagsOfResourceInput = {
            "resource_arn": resource_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_item(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        item: "capo_dynamodb.types.put_item_input_attribute_map.PutItemInputAttributeMap",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        expected: Optional[
            "capo_dynamodb.types.expected_attribute_map.ExpectedAttributeMap"
        ] = None,
        return_values: Optional["capo_dynamodb.types.return_value.ReturnValue"] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        return_item_collection_metrics: Optional[
            "capo_dynamodb.types.return_item_collection_metrics.ReturnItemCollectionMetrics"
        ] = None,
        conditional_operator: Optional[
            "capo_dynamodb.types.conditional_operator.ConditionalOperator"
        ] = None,
        condition_expression: Optional[
            "capo_dynamodb.types.condition_expression.ConditionExpression"
        ] = None,
        expression_attribute_names: Optional[
            "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
        ] = None,
        expression_attribute_values: Optional[
            "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
        ] = None,
        return_values_on_condition_check_failure: Optional[
            "capo_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
        ] = None,
    ) -> "capo_dynamodb.types.put_item_output.PutItemOutput":
        """<p>Creates a new item, or replaces an old item with a new item. If an item that has the same primary key as the new item already exists in the specified table, the new item completely replaces the existing item. You can perform a conditional put operation (add a new item if one with the specified primary key doesn't exist), or replace an existing item if it has certain attribute values. You can return the item's attribute values in the same operation, using the <code>ReturnValues</code> parameter.</p> <p>When you add an item, the primary key attributes are the only required attributes. </p> <p>Empty String and Binary attribute values are allowed. Attribute values of type String and Binary must have a length greater than zero if the attribute is used as a key attribute for a table or index. Set type attributes cannot be empty. </p> <p>Invalid Requests with empty values will be rejected with a <code>ValidationException</code> exception.</p> <note> <p>To prevent a new item from replacing an existing item, use a conditional expression that contains the <code>attribute_not_exists</code> function with the name of the attribute being used as the partition key for the table. Since every record must contain that attribute, the <code>attribute_not_exists</code> function will only succeed if no matching item exists.</p> </note> <note> <p>To determine whether <code>PutItem</code> overwrote an existing item, use <code>ReturnValues</code> set to <code>ALL_OLD</code>. If the response includes the <code>Attributes</code> element, an existing item was overwritten.</p> </note> <p>For more information about <code>PutItem</code>, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html">Working with Items</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>

        Args:
            table_name: <p>The name of the table to contain the item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            item: <p>A map of attribute name/value pairs, one for each attribute. Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.</p> <p>You must provide all of the attributes for the primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide both values for both the partition key and the sort key.</p> <p>If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table's attribute definition.</p> <p>If the table has vector indexes, the following validations apply to write operations. A violation of any of these constraints results in a <code>ValidationException</code>:</p> <ul> <li> <p>The vector attribute must be a list of numbers with dimensions matching the index configuration.</p> </li> <li> <p>Vector values must fit in 32-bit IEEE-754 floating point format (f32).</p> </li> <li> <p>Partition key and inline filter attributes defined in the search schema must have data types matching the index schema definition.</p> </li> </ul> <p>Empty String and Binary attribute values are allowed. Attribute values of type String and Binary must have a length greater than zero if the attribute is used as a key attribute for a table or index.</p> <p>For more information about primary keys, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey">Primary Key</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>Each element in the <code>Item</code> map is an <code>AttributeValue</code> object.</p>
            expected: <p>This is a legacy parameter. Use <code>ConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Expected.html">Expected</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            return_values: <p>Use <code>ReturnValues</code> if you want to get the item attributes as they appeared before they were updated with the <code>PutItem</code> request. For <code>PutItem</code>, the valid values are:</p> <ul> <li> <p> <code>NONE</code> - If <code>ReturnValues</code> is not specified, or if its value is <code>NONE</code>, then nothing is returned. (This setting is the default for <code>ReturnValues</code>.)</p> </li> <li> <p> <code>ALL_OLD</code> - If <code>PutItem</code> overwrote an attribute name-value pair, then the content of the old item is returned.</p> </li> </ul> <p>The values returned are strongly consistent.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p> <note> <p>The <code>ReturnValues</code> parameter is used by several DynamoDB operations; however, <code>PutItem</code> does not recognize any values other than <code>NONE</code> or <code>ALL_OLD</code>.</p> </note>
            return_item_collection_metrics: <p>Determines whether item collection metrics are returned. If set to <code>SIZE</code>, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to <code>NONE</code> (the default), no statistics are returned.</p>
            conditional_operator: <p>This is a legacy parameter. Use <code>ConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html">ConditionalOperator</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            condition_expression: <p>A condition that must be satisfied in order for a conditional <code>PutItem</code> operation to succeed.</p> <p>An expression can contain any of the following:</p> <ul> <li> <p>Functions: <code>attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size</code> </p> <p>These function names are case-sensitive.</p> </li> <li> <p>Comparison operators: <code>= | <> | < | > | <= | >= | BETWEEN | IN </code> </p> </li> <li> <p> Logical operators: <code>AND | OR | NOT</code> </p> </li> </ul> <p>For more information on condition expressions, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Condition Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_names: <p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information on expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_values: <p>One or more values that can be substituted in an expression.</p> <p>Use the <b>:</b> (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the <i>ProductStatus</i> attribute was one of the following: </p> <p> <code>Available | Backordered | Discontinued</code> </p> <p>You would first need to specify <code>ExpressionAttributeValues</code> as follows:</p> <p> <code>{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }</code> </p> <p>You could then use these values in an expression, such as this:</p> <p> <code>ProductStatus IN (:avail, :back, :disc)</code> </p> <p>For more information on expression attribute values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Condition Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            return_values_on_condition_check_failure: <p>An optional parameter that returns the item attributes for a <code>PutItem</code> operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>

        Raises:
            capo_dynamodb.errors.conditional_check_failed_exception.ConditionalCheckFailedException: <p>A condition specified in the operation failed to be evaluated.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.item_collection_size_limit_exceeded_exception.ItemCollectionSizeLimitExceededException: <p>An item collection is too large. This exception is only returned for tables that have one or more local secondary indexes.</p>
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.replicated_write_conflict_exception.ReplicatedWriteConflictException: <p>The request was rejected because one or more items in the request are being modified by a request in another Region. </p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.transaction_conflict_exception.TransactionConflictException: <p>Operation was rejected because there is an ongoing transaction for the item.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add an item to a table
            This example adds a new item to the Music table.

            >>> client.put_item(table_name='Music', item={'AlbumTitle': {'S': 'Somewhat Famous'}, 'SongTitle': {'S': 'Call Me Today'}, 'Artist': {'S': 'No One You Know'}}, return_consumed_capacity='TOTAL')
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.put_item_input.PutItemInput]",
        ) -> OperationResponse["capo_dynamodb.types.put_item_output.PutItemOutput"]:
            import capo_dynamodb._operations.dynamo_db_20120810.put_item

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.put_item.put_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.put_item_input.PutItemInput = {
            "table_name": table_name,
            "item": item,
        }
        if expected is not None:
            input_["expected"] = expected
        if return_values is not None:
            input_["return_values"] = return_values
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity
        if return_item_collection_metrics is not None:
            input_["return_item_collection_metrics"] = return_item_collection_metrics
        if conditional_operator is not None:
            input_["conditional_operator"] = conditional_operator
        if condition_expression is not None:
            input_["condition_expression"] = condition_expression
        if expression_attribute_names is not None:
            input_["expression_attribute_names"] = expression_attribute_names
        if expression_attribute_values is not None:
            input_["expression_attribute_values"] = expression_attribute_values
        if return_values_on_condition_check_failure is not None:
            input_["return_values_on_condition_check_failure"] = (
                return_values_on_condition_check_failure
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "capo_dynamodb.types.resource_arn_string.ResourceArnString",
        policy: "capo_dynamodb.types.resource_policy.ResourcePolicy",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        expected_revision_id: Optional[
            "capo_dynamodb.types.policy_revision_id.PolicyRevisionId"
        ] = None,
        confirm_remove_self_resource_access: Optional[
            "capo_dynamodb.types.confirm_remove_self_resource_access.ConfirmRemoveSelfResourceAccess"
        ] = None,
    ) -> "capo_dynamodb.types.put_resource_policy_output.PutResourcePolicyOutput":
        """<p>Attaches a resource-based policy document to the resource, which can be a table or stream. When you attach a resource-based policy using this API, the policy application is <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html"> <i>eventually consistent</i> </a>.</p> <p> <code>PutResourcePolicy</code> is an idempotent operation; running it multiple times on the same resource using the same policy document will return the same revision ID. If you specify an <code>ExpectedRevisionId</code> that doesn't match the current policy's <code>RevisionId</code>, the <code>PolicyNotFoundException</code> will be returned.</p> <note> <p> <code>PutResourcePolicy</code> is an asynchronous operation. If you issue a <code>GetResourcePolicy</code> request immediately after a <code>PutResourcePolicy</code> request, DynamoDB might return your previous policy, if there was one, or return the <code>PolicyNotFoundException</code>. This is because <code>GetResourcePolicy</code> uses an eventually consistent query, and the metadata for your policy or table might not be available at that moment. Wait for a few seconds, and then try the <code>GetResourcePolicy</code> request again.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the DynamoDB resource to which the policy will be attached. The resources you can specify include tables and streams.</p> <p>You can control index permissions using the base table's policy. To specify the same permission level for your table and its indexes, you can provide both the table and index Amazon Resource Name (ARN)s in the <code>Resource</code> field of a given <code>Statement</code> in your policy document. Alternatively, to specify different permissions for your table, indexes, or both, you can define multiple <code>Statement</code> fields in your policy document.</p>
            policy: <p>An Amazon Web Services resource-based policy document in JSON format.</p> <ul> <li> <p>The maximum size supported for a resource-based policy document is 20 KB. DynamoDB counts whitespaces when calculating the size of a policy against this limit.</p> </li> <li> <p>Within a resource-based policy, if the action for a DynamoDB service-linked role (SLR) to replicate data for a global table is denied, adding or deleting a replica will fail with an error.</p> </li> </ul> <p>For a full list of all considerations that apply while attaching a resource-based policy, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-considerations.html">Resource-based policy considerations</a>.</p>
            expected_revision_id: <p>A string value that you can use to conditionally update your policy. You can provide the revision ID of your existing policy to make mutating requests against that policy.</p> <note> <p>When you provide an expected revision ID, if the revision ID of the existing policy on the resource doesn't match or if there's no policy attached to the resource, your request will be rejected with a <code>PolicyNotFoundException</code>.</p> </note> <p>To conditionally attach a policy when no policy exists for the resource, specify <code>NO_POLICY</code> for the revision ID.</p>
            confirm_remove_self_resource_access: <p>Set this parameter to <code>true</code> to confirm that you want to remove your permissions to change the policy of this resource in the future.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.policy_not_found_exception.PolicyNotFoundException: <p>The operation tried to access a nonexistent resource-based policy.</p> <p>If you specified an <code>ExpectedRevisionId</code>, it's possible that a policy is present for the resource but its revision ID didn't match the expected value.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.put_resource_policy_input.PutResourcePolicyInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.put_resource_policy_output.PutResourcePolicyOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.put_resource_policy

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.put_resource_policy_input.PutResourcePolicyInput = {
            "resource_arn": resource_arn,
            "policy": policy,
        }
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id
        if confirm_remove_self_resource_access is not None:
            input_["confirm_remove_self_resource_access"] = (
                confirm_remove_self_resource_access
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def query(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        index_name: Optional["capo_dynamodb.types.index_name.IndexName"] = None,
        select: Optional["capo_dynamodb.types.select.Select"] = None,
        attributes_to_get: Optional[
            "capo_dynamodb.types.attribute_name_list.AttributeNameList"
        ] = None,
        limit: Optional[
            "capo_dynamodb.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        consistent_read: Optional[
            "capo_dynamodb.types.consistent_read.ConsistentRead"
        ] = None,
        key_conditions: Optional[
            "capo_dynamodb.types.key_conditions.KeyConditions"
        ] = None,
        query_filter: Optional[
            "capo_dynamodb.types.filter_condition_map.FilterConditionMap"
        ] = None,
        conditional_operator: Optional[
            "capo_dynamodb.types.conditional_operator.ConditionalOperator"
        ] = None,
        scan_index_forward: Optional[
            "capo_dynamodb.types.boolean_object.BooleanObject"
        ] = None,
        exclusive_start_key: Optional["capo_dynamodb.types.key.Key"] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        projection_expression: Optional[
            "capo_dynamodb.types.projection_expression.ProjectionExpression"
        ] = None,
        filter_expression: Optional[
            "capo_dynamodb.types.condition_expression.ConditionExpression"
        ] = None,
        key_condition_expression: Optional[
            "capo_dynamodb.types.key_expression.KeyExpression"
        ] = None,
        expression_attribute_names: Optional[
            "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
        ] = None,
        expression_attribute_values: Optional[
            "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
        ] = None,
    ) -> "capo_dynamodb.types.query_output.QueryOutput":
        """<p>You must provide the name of the partition key attribute and a single value for that attribute. <code>Query</code> returns all items with that partition key value. Optionally, you can provide a sort key attribute and use a comparison operator to refine the search results.</p> <p>Use the <code>KeyConditionExpression</code> parameter to provide a specific value for the partition key. The <code>Query</code> operation will return all of the items from the table or index with that partition key value. You can optionally narrow the scope of the <code>Query</code> operation by specifying a sort key value and a comparison operator in <code>KeyConditionExpression</code>. To further refine the <code>Query</code> results, you can optionally provide a <code>FilterExpression</code>. A <code>FilterExpression</code> determines which items within the results should be returned to you. All of the other results are discarded. </p> <p> A <code>Query</code> operation always returns a result set. If no matching items are found, the result set will be empty. Queries that do not return results consume the minimum number of read capacity units for that type of read operation. </p> <note> <p> DynamoDB calculates the number of read capacity units consumed based on item size, not on the amount of data that is returned to an application. The number of capacity units consumed will be the same whether you request all of the attributes (the default behavior) or just some of them (using a projection expression). The number will also be the same whether or not you use a <code>FilterExpression</code>. </p> </note> <p> <code>Query</code> results are always sorted by the sort key value. If the data type of the sort key is Number, the results are returned in numeric order; otherwise, the results are returned in order of UTF-8 bytes. By default, the sort order is ascending. To reverse the order, set the <code>ScanIndexForward</code> parameter to false. </p> <p> A single <code>Query</code> operation will read up to the maximum number of items set (if using the <code>Limit</code> parameter) or a maximum of 1 MB of data and then apply any filtering to the results using <code>FilterExpression</code>. If <code>LastEvaluatedKey</code> is present in the response, you will need to paginate the result set. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html#Query.Pagination">Paginating the Results</a> in the <i>Amazon DynamoDB Developer Guide</i>. </p> <p> <code>FilterExpression</code> is applied after a <code>Query</code> finishes, but before the results are returned. A <code>FilterExpression</code> cannot contain partition key or sort key attributes. You need to specify those attributes in the <code>KeyConditionExpression</code>. </p> <note> <p> A <code>Query</code> operation can return an empty result set and a <code>LastEvaluatedKey</code> if all the items read for the page of results are filtered out. </p> </note> <p>You can query a table, a local secondary index, or a global secondary index. For a query on a table or on a local secondary index, you can set the <code>ConsistentRead</code> parameter to <code>true</code> and obtain a strongly consistent result. Global secondary indexes support eventually consistent reads only, so do not specify <code>ConsistentRead</code> when querying a global secondary index.</p>

        Args:
            table_name: <p>The name of the table containing the requested items. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            index_name: <p>The name of an index to query. This index can be any local secondary index or global secondary index on the table. Note that if you use the <code>IndexName</code> parameter, you must also provide <code>TableName.</code> </p>
            select: <p>The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.</p> <ul> <li> <p> <code>ALL_ATTRIBUTES</code> - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index, DynamoDB fetches the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.</p> </li> <li> <p> <code>ALL_PROJECTED_ATTRIBUTES</code> - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying <code>ALL_ATTRIBUTES</code>.</p> </li> <li> <p> <code>COUNT</code> - Returns the number of matching items, rather than the matching items themselves. Note that this uses the same quantity of read capacity units as getting the items, and is subject to the same item size calculations.</p> </li> <li> <p> <code>SPECIFIC_ATTRIBUTES</code> - Returns only the attributes listed in <code>ProjectionExpression</code>. This return value is equivalent to specifying <code>ProjectionExpression</code> without specifying any value for <code>Select</code>.</p> <p>If you query or scan a local secondary index and request only attributes that are projected into that index, the operation will read only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB fetches each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency.</p> <p>If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table.</p> </li> </ul> <p>If neither <code>Select</code> nor <code>ProjectionExpression</code> are specified, DynamoDB defaults to <code>ALL_ATTRIBUTES</code> when accessing a table, and <code>ALL_PROJECTED_ATTRIBUTES</code> when accessing an index. You cannot use both <code>Select</code> and <code>ProjectionExpression</code> together in a single request, unless the value for <code>Select</code> is <code>SPECIFIC_ATTRIBUTES</code>. (This usage is equivalent to specifying <code>ProjectionExpression</code> without any value for <code>Select</code>.)</p> <note> <p>If you use the <code>ProjectionExpression</code> parameter, then the value for <code>Select</code> can only be <code>SPECIFIC_ATTRIBUTES</code>. Any other value for <code>Select</code> will return an error.</p> </note>
            attributes_to_get: <p>This is a legacy parameter. Use <code>ProjectionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html">AttributesToGet</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            limit: <p>The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation, so that you can pick up where you left off. Also, if the processed dataset size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation to continue the operation. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html">Query and Scan</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            consistent_read: <p>Determines the read consistency model: If set to <code>true</code>, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.</p> <p>Strongly consistent reads are not supported on global secondary indexes. If you query a global secondary index with <code>ConsistentRead</code> set to <code>true</code>, you will receive a <code>ValidationException</code>.</p>
            key_conditions: <p>This is a legacy parameter. Use <code>KeyConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.KeyConditions.html">KeyConditions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            query_filter: <p>This is a legacy parameter. Use <code>FilterExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.QueryFilter.html">QueryFilter</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            conditional_operator: <p>This is a legacy parameter. Use <code>FilterExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html">ConditionalOperator</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            scan_index_forward: <p>Specifies the order for index traversal: If <code>true</code> (default), the traversal is performed in ascending order; if <code>false</code>, the traversal is performed in descending order. </p> <p>Items with the same partition key value are stored in sorted order by sort key. If the sort key data type is Number, the results are stored in numeric order. For type String, the results are stored in order of UTF-8 bytes. For type Binary, DynamoDB treats each byte of the binary data as unsigned.</p> <p>If <code>ScanIndexForward</code> is <code>true</code>, DynamoDB returns the results in the order in which they are stored (by sort key value). This is the default behavior. If <code>ScanIndexForward</code> is <code>false</code>, DynamoDB reads the results in reverse order by sort key value, and then returns the results to the client.</p>
            exclusive_start_key: <p>The primary key of the first item that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedKey</code> in the previous operation.</p> <p>The data type for <code>ExclusiveStartKey</code> must be String, Number, or Binary. No set data types are allowed.</p>
            projection_expression: <p>A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.</p> <p>If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Accessing Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            filter_expression: <p>A string that contains conditions that DynamoDB applies after the <code>Query</code> operation, but before the data is returned to you. Items that do not satisfy the <code>FilterExpression</code> criteria are not returned.</p> <p>A <code>FilterExpression</code> does not allow key attributes. You cannot define a filter expression based on a partition key or a sort key.</p> <note> <p>A <code>FilterExpression</code> is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.FilterExpression.html">Filter Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            key_condition_expression: <p>The condition that specifies the key values for items to be retrieved by the <code>Query</code> action.</p> <p>The condition must perform an equality test on a single partition key value.</p> <p>The condition can optionally perform one of several comparison tests on a single sort key value. This allows <code>Query</code> to retrieve one item with a given partition key value and sort key value, or several items that have the same partition key value but different sort key values.</p> <p>The partition key equality test is required, and must be specified in the following format:</p> <p> <code>partitionKeyName</code> <i>=</i> <code>:partitionkeyval</code> </p> <p>If you also want to provide a condition for the sort key, it must be combined using <code>AND</code> with the condition for the sort key. Following is an example, using the <b>=</b> comparison operator for the sort key:</p> <p> <code>partitionKeyName</code> <code>=</code> <code>:partitionkeyval</code> <code>AND</code> <code>sortKeyName</code> <code>=</code> <code>:sortkeyval</code> </p> <p>Valid comparisons for the sort key condition are as follows:</p> <ul> <li> <p> <code>sortKeyName</code> <code>=</code> <code>:sortkeyval</code> - true if the sort key value is equal to <code>:sortkeyval</code>.</p> </li> <li> <p> <code>sortKeyName</code> <code><</code> <code>:sortkeyval</code> - true if the sort key value is less than <code>:sortkeyval</code>.</p> </li> <li> <p> <code>sortKeyName</code> <code><=</code> <code>:sortkeyval</code> - true if the sort key value is less than or equal to <code>:sortkeyval</code>.</p> </li> <li> <p> <code>sortKeyName</code> <code>></code> <code>:sortkeyval</code> - true if the sort key value is greater than <code>:sortkeyval</code>.</p> </li> <li> <p> <code>sortKeyName</code> <code>>= </code> <code>:sortkeyval</code> - true if the sort key value is greater than or equal to <code>:sortkeyval</code>.</p> </li> <li> <p> <code>sortKeyName</code> <code>BETWEEN</code> <code>:sortkeyval1</code> <code>AND</code> <code>:sortkeyval2</code> - true if the sort key value is greater than or equal to <code>:sortkeyval1</code>, and less than or equal to <code>:sortkeyval2</code>.</p> </li> <li> <p> <code>begins_with (</code> <code>sortKeyName</code>, <code>:sortkeyval</code> <code>)</code> - true if the sort key value begins with a particular operand. (You cannot use this function with a sort key that is of type Number.) Note that the function name <code>begins_with</code> is case-sensitive.</p> </li> </ul> <p>Use the <code>ExpressionAttributeValues</code> parameter to replace tokens such as <code>:partitionval</code> and <code>:sortval</code> with actual values at runtime.</p> <p>You can optionally use the <code>ExpressionAttributeNames</code> parameter to replace the names of the partition key and sort key with placeholder tokens. This option might be necessary if an attribute name conflicts with a DynamoDB reserved word. For example, the following <code>KeyConditionExpression</code> parameter causes an error because <i>Size</i> is a reserved word:</p> <ul> <li> <p> <code>Size = :myval</code> </p> </li> </ul> <p>To work around this, define a placeholder (such a <code>#S</code>) to represent the attribute name <i>Size</i>. <code>KeyConditionExpression</code> then is as follows:</p> <ul> <li> <p> <code>#S = :myval</code> </p> </li> </ul> <p>For a list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>For more information on <code>ExpressionAttributeNames</code> and <code>ExpressionAttributeValues</code>, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ExpressionPlaceholders.html">Using Placeholders for Attribute Names and Values</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_names: <p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information on expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_values: <p>One or more values that can be substituted in an expression.</p> <p>Use the <b>:</b> (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the <i>ProductStatus</i> attribute was one of the following: </p> <p> <code>Available | Backordered | Discontinued</code> </p> <p>You would first need to specify <code>ExpressionAttributeValues</code> as follows:</p> <p> <code>{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }</code> </p> <p>You could then use these values in an expression, such as this:</p> <p> <code>ProductStatus IN (:avail, :back, :disc)</code> </p> <p>For more information on expression attribute values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Specifying Conditions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To query an item
            This example queries items in the Music table. The table has a partition key and sort key (Artist and SongTitle), but this query only specifies the partition key value. It returns song titles by the artist named "No One You Know".

            >>> client.query(table_name='Music', projection_expression='SongTitle', key_condition_expression='Artist = :v1', expression_attribute_values={':v1': {'S': 'No One You Know'}})
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.query_input.QueryInput]",
        ) -> OperationResponse["capo_dynamodb.types.query_output.QueryOutput"]:
            import capo_dynamodb._operations.dynamo_db_20120810.query

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.query.query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.query_input.QueryInput = {"table_name": table_name}
        if index_name is not None:
            input_["index_name"] = index_name
        if select is not None:
            input_["select"] = select
        if attributes_to_get is not None:
            input_["attributes_to_get"] = attributes_to_get
        if limit is not None:
            input_["limit"] = limit
        if consistent_read is not None:
            input_["consistent_read"] = consistent_read
        if key_conditions is not None:
            input_["key_conditions"] = key_conditions
        if query_filter is not None:
            input_["query_filter"] = query_filter
        if conditional_operator is not None:
            input_["conditional_operator"] = conditional_operator
        if scan_index_forward is not None:
            input_["scan_index_forward"] = scan_index_forward
        if exclusive_start_key is not None:
            input_["exclusive_start_key"] = exclusive_start_key
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity
        if projection_expression is not None:
            input_["projection_expression"] = projection_expression
        if filter_expression is not None:
            input_["filter_expression"] = filter_expression
        if key_condition_expression is not None:
            input_["key_condition_expression"] = key_condition_expression
        if expression_attribute_names is not None:
            input_["expression_attribute_names"] = expression_attribute_names
        if expression_attribute_values is not None:
            input_["expression_attribute_values"] = expression_attribute_values

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_query(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        index_name: Optional["capo_dynamodb.types.index_name.IndexName"] = None,
        select: Optional["capo_dynamodb.types.select.Select"] = None,
        attributes_to_get: Optional[
            "capo_dynamodb.types.attribute_name_list.AttributeNameList"
        ] = None,
        limit: Optional[
            "capo_dynamodb.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        consistent_read: Optional[
            "capo_dynamodb.types.consistent_read.ConsistentRead"
        ] = None,
        key_conditions: Optional[
            "capo_dynamodb.types.key_conditions.KeyConditions"
        ] = None,
        query_filter: Optional[
            "capo_dynamodb.types.filter_condition_map.FilterConditionMap"
        ] = None,
        conditional_operator: Optional[
            "capo_dynamodb.types.conditional_operator.ConditionalOperator"
        ] = None,
        scan_index_forward: Optional[
            "capo_dynamodb.types.boolean_object.BooleanObject"
        ] = None,
        exclusive_start_key: Optional["capo_dynamodb.types.key.Key"] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        projection_expression: Optional[
            "capo_dynamodb.types.projection_expression.ProjectionExpression"
        ] = None,
        filter_expression: Optional[
            "capo_dynamodb.types.condition_expression.ConditionExpression"
        ] = None,
        key_condition_expression: Optional[
            "capo_dynamodb.types.key_expression.KeyExpression"
        ] = None,
        expression_attribute_names: Optional[
            "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
        ] = None,
        expression_attribute_values: Optional[
            "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
        ] = None,
    ) -> "Iterator[capo_dynamodb.types.attribute_map.AttributeMap]":
        _token = exclusive_start_key
        while True:
            _response = self.query(
                table_name,
                config_overrides=config_overrides,
                index_name=index_name,
                select=select,
                attributes_to_get=attributes_to_get,
                limit=limit,
                consistent_read=consistent_read,
                key_conditions=key_conditions,
                query_filter=query_filter,
                conditional_operator=conditional_operator,
                scan_index_forward=scan_index_forward,
                exclusive_start_key=_token,
                return_consumed_capacity=return_consumed_capacity,
                projection_expression=projection_expression,
                filter_expression=filter_expression,
                key_condition_expression=key_condition_expression,
                expression_attribute_names=expression_attribute_names,
                expression_attribute_values=expression_attribute_values,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("last_evaluated_key",))
            if not _token:
                break

    def restore_table_from_backup(
        self,
        target_table_name: "capo_dynamodb.types.table_name.TableName",
        backup_arn: "capo_dynamodb.types.backup_arn.BackupArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        billing_mode_override: Optional[
            "capo_dynamodb.types.billing_mode.BillingMode"
        ] = None,
        global_secondary_index_override: Optional[
            "capo_dynamodb.types.global_secondary_index_list.GlobalSecondaryIndexList"
        ] = None,
        local_secondary_index_override: Optional[
            "capo_dynamodb.types.local_secondary_index_list.LocalSecondaryIndexList"
        ] = None,
        provisioned_throughput_override: Optional[
            "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
        ] = None,
        on_demand_throughput_override: Optional[
            "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
        ] = None,
        sse_specification_override: Optional[
            "capo_dynamodb.types.sse_specification.SSESpecification"
        ] = None,
        vector_index_override: Optional[
            "capo_dynamodb.types.vector_index_list.VectorIndexList"
        ] = None,
    ) -> "capo_dynamodb.types.restore_table_from_backup_output.RestoreTableFromBackupOutput":
        """<p>Creates a new table from an existing backup. Any number of users can execute up to 50 concurrent restores (any type of restore) in a given account. </p> <p>You can call <code>RestoreTableFromBackup</code> at a maximum rate of 10 times per second.</p> <p>You must manually set up the following on the restored table:</p> <ul> <li> <p>Auto scaling policies</p> </li> <li> <p>IAM policies</p> </li> <li> <p>Amazon CloudWatch metrics and alarms</p> </li> <li> <p>Tags</p> </li> <li> <p>Stream settings</p> </li> <li> <p>Time to Live (TTL) settings</p> </li> </ul>

        Args:
            target_table_name: <p>The name of the new table to which the backup must be restored.</p>
            backup_arn: <p>The Amazon Resource Name (ARN) associated with the backup.</p>
            billing_mode_override: <p>The billing mode of the restored table.</p>
            global_secondary_index_override: <p>List of global secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.</p>
            local_secondary_index_override: <p>List of local secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.</p>
            provisioned_throughput_override: <p>Provisioned throughput settings for the restored table.</p>
            sse_specification_override: <p>The new server-side encryption settings for the restored table.</p>
            vector_index_override: <p>The vector indexes for the restored table. If not specified, all vector indexes from the backup are restored. The indexes provided must match existing vector indexes from the backup. You can choose to exclude some or all of the vector indexes at the time of restore.</p>

        Raises:
            capo_dynamodb.errors.backup_in_use_exception.BackupInUseException: <p>There is another ongoing conflicting backup control plane operation on the table. The backup is either being created, deleted or restored to a table.</p>
            capo_dynamodb.errors.backup_not_found_exception.BackupNotFoundException: <p>Backup not found for the given BackupARN. </p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.table_already_exists_exception.TableAlreadyExistsException: <p>A target table with the specified name already exists. </p>
            capo_dynamodb.errors.table_in_use_exception.TableInUseException: <p>A target table with the specified name is either being created or deleted. </p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.restore_table_from_backup_input.RestoreTableFromBackupInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.restore_table_from_backup_output.RestoreTableFromBackupOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.restore_table_from_backup

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.restore_table_from_backup.restore_table_from_backup(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.restore_table_from_backup_input.RestoreTableFromBackupInput = {
            "target_table_name": target_table_name,
            "backup_arn": backup_arn,
        }
        if billing_mode_override is not None:
            input_["billing_mode_override"] = billing_mode_override
        if global_secondary_index_override is not None:
            input_["global_secondary_index_override"] = global_secondary_index_override
        if local_secondary_index_override is not None:
            input_["local_secondary_index_override"] = local_secondary_index_override
        if provisioned_throughput_override is not None:
            input_["provisioned_throughput_override"] = provisioned_throughput_override
        if on_demand_throughput_override is not None:
            input_["on_demand_throughput_override"] = on_demand_throughput_override
        if sse_specification_override is not None:
            input_["sse_specification_override"] = sse_specification_override
        if vector_index_override is not None:
            input_["vector_index_override"] = vector_index_override

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_table_to_point_in_time(
        self,
        target_table_name: "capo_dynamodb.types.table_name.TableName",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        source_table_arn: Optional["capo_dynamodb.types.table_arn.TableArn"] = None,
        source_table_name: Optional["capo_dynamodb.types.table_name.TableName"] = None,
        use_latest_restorable_time: Optional[
            "capo_dynamodb.types.boolean_object.BooleanObject"
        ] = None,
        restore_date_time: Optional["capo_dynamodb.types.date.Date"] = None,
        billing_mode_override: Optional[
            "capo_dynamodb.types.billing_mode.BillingMode"
        ] = None,
        global_secondary_index_override: Optional[
            "capo_dynamodb.types.global_secondary_index_list.GlobalSecondaryIndexList"
        ] = None,
        local_secondary_index_override: Optional[
            "capo_dynamodb.types.local_secondary_index_list.LocalSecondaryIndexList"
        ] = None,
        provisioned_throughput_override: Optional[
            "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
        ] = None,
        on_demand_throughput_override: Optional[
            "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
        ] = None,
        sse_specification_override: Optional[
            "capo_dynamodb.types.sse_specification.SSESpecification"
        ] = None,
        vector_index_override: Optional[
            "capo_dynamodb.types.vector_index_list.VectorIndexList"
        ] = None,
    ) -> "capo_dynamodb.types.restore_table_to_point_in_time_output.RestoreTableToPointInTimeOutput":
        """<p>Restores the specified table to the specified point in time within <code>EarliestRestorableDateTime</code> and <code>LatestRestorableDateTime</code>. You can restore your table to any point in time in the last 35 days. You can set the recovery period to any value between 1 and 35 days. Any number of users can execute up to 50 concurrent restores (any type of restore) in a given account. </p> <p>When you restore using point in time recovery, DynamoDB restores your table data to the state based on the selected date and time (day:hour:minute:second) to a new table. </p> <p>Along with data, the following are also included on the new restored table using point in time recovery: </p> <ul> <li> <p>Global secondary indexes (GSIs)</p> </li> <li> <p>Local secondary indexes (LSIs)</p> </li> <li> <p>Provisioned read and write capacity</p> </li> <li> <p>Encryption settings</p> <important> <p> All these settings come from the current settings of the source table at the time of restore. </p> </important> </li> </ul> <p>You must manually set up the following on the restored table:</p> <ul> <li> <p>Auto scaling policies</p> </li> <li> <p>IAM policies</p> </li> <li> <p>Amazon CloudWatch metrics and alarms</p> </li> <li> <p>Tags</p> </li> <li> <p>Stream settings</p> </li> <li> <p>Time to Live (TTL) settings</p> </li> <li> <p>Point in time recovery settings</p> </li> </ul>

        Args:
            source_table_arn: <p>The DynamoDB table that will be restored. This value is an Amazon Resource Name (ARN).</p>
            source_table_name: <p>Name of the source table that is being restored.</p>
            target_table_name: <p>The name of the new table to which it must be restored to.</p>
            use_latest_restorable_time: <p>Restore the table to the latest possible time. <code>LatestRestorableDateTime</code> is typically 5 minutes before the current time. </p>
            restore_date_time: <p>Time in the past to restore the table to.</p>
            billing_mode_override: <p>The billing mode of the restored table.</p>
            global_secondary_index_override: <p>List of global secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.</p> <p>The <code>WarmThroughput</code> setting is not supported on global secondary indexes when you use <code>RestoreTableToPointInTime</code>. Although <code>WarmThroughput</code> appears in the shared index definition, including it in a <code>GlobalSecondaryIndexOverride</code> entry causes the request to fail with a validation error.</p>
            local_secondary_index_override: <p>List of local secondary indexes for the restored table. The indexes provided should match existing secondary indexes. You can choose to exclude some or all of the indexes at the time of restore.</p>
            provisioned_throughput_override: <p>Provisioned throughput settings for the restored table.</p>
            sse_specification_override: <p>The new server-side encryption settings for the restored table.</p>
            vector_index_override: <p>The vector indexes for the restored table. If not specified, all vector indexes from the source table are restored. The indexes provided must match existing vector indexes from the source table. You can choose to exclude some or all of the vector indexes at the time of restore.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.invalid_restore_time_exception.InvalidRestoreTimeException: <p>An invalid restore time was specified. RestoreDateTime must be between EarliestRestorableDateTime and LatestRestorableDateTime.</p>
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.point_in_time_recovery_unavailable_exception.PointInTimeRecoveryUnavailableException: <p>Point in time recovery has not yet been enabled for this source table.</p>
            capo_dynamodb.errors.table_already_exists_exception.TableAlreadyExistsException: <p>A target table with the specified name already exists. </p>
            capo_dynamodb.errors.table_in_use_exception.TableInUseException: <p>A target table with the specified name is either being created or deleted. </p>
            capo_dynamodb.errors.table_not_found_exception.TableNotFoundException: <p>A source table with the name <code>TableName</code> does not currently exist within the subscriber's account or the subscriber is operating in the wrong Amazon Web Services Region.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.restore_table_to_point_in_time_input.RestoreTableToPointInTimeInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.restore_table_to_point_in_time_output.RestoreTableToPointInTimeOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.restore_table_to_point_in_time

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.restore_table_to_point_in_time.restore_table_to_point_in_time(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.restore_table_to_point_in_time_input.RestoreTableToPointInTimeInput = {
            "target_table_name": target_table_name
        }
        if source_table_arn is not None:
            input_["source_table_arn"] = source_table_arn
        if source_table_name is not None:
            input_["source_table_name"] = source_table_name
        if use_latest_restorable_time is not None:
            input_["use_latest_restorable_time"] = use_latest_restorable_time
        if restore_date_time is not None:
            input_["restore_date_time"] = restore_date_time
        if billing_mode_override is not None:
            input_["billing_mode_override"] = billing_mode_override
        if global_secondary_index_override is not None:
            input_["global_secondary_index_override"] = global_secondary_index_override
        if local_secondary_index_override is not None:
            input_["local_secondary_index_override"] = local_secondary_index_override
        if provisioned_throughput_override is not None:
            input_["provisioned_throughput_override"] = provisioned_throughput_override
        if on_demand_throughput_override is not None:
            input_["on_demand_throughput_override"] = on_demand_throughput_override
        if sse_specification_override is not None:
            input_["sse_specification_override"] = sse_specification_override
        if vector_index_override is not None:
            input_["vector_index_override"] = vector_index_override

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def scan(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        index_name: Optional["capo_dynamodb.types.index_name.IndexName"] = None,
        attributes_to_get: Optional[
            "capo_dynamodb.types.attribute_name_list.AttributeNameList"
        ] = None,
        limit: Optional[
            "capo_dynamodb.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        select: Optional["capo_dynamodb.types.select.Select"] = None,
        scan_filter: Optional[
            "capo_dynamodb.types.filter_condition_map.FilterConditionMap"
        ] = None,
        conditional_operator: Optional[
            "capo_dynamodb.types.conditional_operator.ConditionalOperator"
        ] = None,
        exclusive_start_key: Optional["capo_dynamodb.types.key.Key"] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        total_segments: Optional[
            "capo_dynamodb.types.scan_total_segments.ScanTotalSegments"
        ] = None,
        segment: Optional["capo_dynamodb.types.scan_segment.ScanSegment"] = None,
        projection_expression: Optional[
            "capo_dynamodb.types.projection_expression.ProjectionExpression"
        ] = None,
        filter_expression: Optional[
            "capo_dynamodb.types.condition_expression.ConditionExpression"
        ] = None,
        expression_attribute_names: Optional[
            "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
        ] = None,
        expression_attribute_values: Optional[
            "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
        ] = None,
        consistent_read: Optional[
            "capo_dynamodb.types.consistent_read.ConsistentRead"
        ] = None,
    ) -> "capo_dynamodb.types.scan_output.ScanOutput":
        """<p>The <code>Scan</code> operation returns one or more items and item attributes by accessing every item in a table or a secondary index. To have DynamoDB return fewer items, you can provide a <code>FilterExpression</code> operation.</p> <p>If the total size of scanned items exceeds the maximum dataset size limit of 1 MB, the scan completes and results are returned to the user. The <code>LastEvaluatedKey</code> value is also returned and the requestor can use the <code>LastEvaluatedKey</code> to continue the scan in a subsequent operation. Each scan response also includes number of items that were scanned (ScannedCount) as part of the request. If using a <code>FilterExpression</code>, a scan result can result in no items meeting the criteria and the <code>Count</code> will result in zero. If you did not use a <code>FilterExpression</code> in the scan request, then <code>Count</code> is the same as <code>ScannedCount</code>.</p> <note> <p> <code>Count</code> and <code>ScannedCount</code> only return the count of items specific to a single scan request and, unless the table is less than 1MB, do not represent the total number of items in the table. </p> </note> <p>A single <code>Scan</code> operation first reads up to the maximum number of items set (if using the <code>Limit</code> parameter) or a maximum of 1 MB of data and then applies any filtering to the results if a <code>FilterExpression</code> is provided. If <code>LastEvaluatedKey</code> is present in the response, pagination is required to complete the full table scan. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html#Scan.Pagination">Paginating the Results</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p> <code>Scan</code> operations proceed sequentially; however, for faster performance on a large table or secondary index, applications can request a parallel <code>Scan</code> operation by providing the <code>Segment</code> and <code>TotalSegments</code> parameters. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html#Scan.ParallelScan">Parallel Scan</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>By default, a <code>Scan</code> uses eventually consistent reads when accessing the items in a table. Therefore, the results from an eventually consistent <code>Scan</code> may not include the latest item changes at the time the scan iterates through each item in the table. If you require a strongly consistent read of each item as the scan iterates through the items in the table, you can set the <code>ConsistentRead</code> parameter to true. Strong consistency only relates to the consistency of the read at the item level.</p> <note> <p> DynamoDB does not provide snapshot isolation for a scan operation when the <code>ConsistentRead</code> parameter is set to true. Thus, a DynamoDB scan operation does not guarantee that all reads in a scan see a consistent snapshot of the table when the scan operation was requested. </p> </note>

        Args:
            table_name: <p>The name of the table containing the requested items or if you provide <code>IndexName</code>, the name of the table to which that index belongs.</p> <p>You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            index_name: <p>The name of a secondary index to scan. This index can be any local secondary index or global secondary index. Note that if you use the <code>IndexName</code> parameter, you must also provide <code>TableName</code>.</p>
            attributes_to_get: <p>This is a legacy parameter. Use <code>ProjectionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html">AttributesToGet</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            limit: <p>The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation, so that you can pick up where you left off. Also, if the processed dataset size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in <code>LastEvaluatedKey</code> to apply in a subsequent operation to continue the operation. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html">Working with Queries</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            select: <p>The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.</p> <ul> <li> <p> <code>ALL_ATTRIBUTES</code> - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index, DynamoDB fetches the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.</p> </li> <li> <p> <code>ALL_PROJECTED_ATTRIBUTES</code> - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying <code>ALL_ATTRIBUTES</code>.</p> </li> <li> <p> <code>COUNT</code> - Returns the number of matching items, rather than the matching items themselves. Note that this uses the same quantity of read capacity units as getting the items, and is subject to the same item size calculations.</p> </li> <li> <p> <code>SPECIFIC_ATTRIBUTES</code> - Returns only the attributes listed in <code>ProjectionExpression</code>. This return value is equivalent to specifying <code>ProjectionExpression</code> without specifying any value for <code>Select</code>.</p> <p>If you query or scan a local secondary index and request only attributes that are projected into that index, the operation reads only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB fetches each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency.</p> <p>If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table.</p> </li> </ul> <p>If neither <code>Select</code> nor <code>ProjectionExpression</code> are specified, DynamoDB defaults to <code>ALL_ATTRIBUTES</code> when accessing a table, and <code>ALL_PROJECTED_ATTRIBUTES</code> when accessing an index. You cannot use both <code>Select</code> and <code>ProjectionExpression</code> together in a single request, unless the value for <code>Select</code> is <code>SPECIFIC_ATTRIBUTES</code>. (This usage is equivalent to specifying <code>ProjectionExpression</code> without any value for <code>Select</code>.)</p> <note> <p>If you use the <code>ProjectionExpression</code> parameter, then the value for <code>Select</code> can only be <code>SPECIFIC_ATTRIBUTES</code>. Any other value for <code>Select</code> will return an error.</p> </note>
            scan_filter: <p>This is a legacy parameter. Use <code>FilterExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ScanFilter.html">ScanFilter</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            conditional_operator: <p>This is a legacy parameter. Use <code>FilterExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html">ConditionalOperator</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            exclusive_start_key: <p>The primary key of the first item that this operation will evaluate. Use the value that was returned for <code>LastEvaluatedKey</code> in the previous operation.</p> <p>The data type for <code>ExclusiveStartKey</code> must be String, Number or Binary. No set data types are allowed.</p> <p>In a parallel scan, a <code>Scan</code> request that includes <code>ExclusiveStartKey</code> must specify the same segment whose previous <code>Scan</code> returned the corresponding value of <code>LastEvaluatedKey</code>.</p>
            total_segments: <p>For a parallel <code>Scan</code> request, <code>TotalSegments</code> represents the total number of segments into which the <code>Scan</code> operation will be divided. The value of <code>TotalSegments</code> corresponds to the number of application workers that will perform the parallel scan. For example, if you want to use four application threads to scan a table or an index, specify a <code>TotalSegments</code> value of 4.</p> <p>The value for <code>TotalSegments</code> must be greater than or equal to 1, and less than or equal to 1000000. If you specify a <code>TotalSegments</code> value of 1, the <code>Scan</code> operation will be sequential rather than parallel.</p> <p>If you specify <code>TotalSegments</code>, you must also specify <code>Segment</code>.</p>
            segment: <p>For a parallel <code>Scan</code> request, <code>Segment</code> identifies an individual segment to be scanned by an application worker.</p> <p>Segment IDs are zero-based, so the first segment is always 0. For example, if you want to use four application threads to scan a table or an index, then the first thread specifies a <code>Segment</code> value of 0, the second thread specifies 1, and so on.</p> <p>The value of <code>LastEvaluatedKey</code> returned from a parallel <code>Scan</code> request must be used as <code>ExclusiveStartKey</code> with the same segment ID in a subsequent <code>Scan</code> operation.</p> <p>The value for <code>Segment</code> must be greater than or equal to 0, and less than the value provided for <code>TotalSegments</code>.</p> <p>If you provide <code>Segment</code>, you must also provide <code>TotalSegments</code>.</p>
            projection_expression: <p>A string that identifies one or more attributes to retrieve from the specified table or index. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.</p> <p>If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            filter_expression: <p>A string that contains conditions that DynamoDB applies after the <code>Scan</code> operation, but before the data is returned to you. Items that do not satisfy the <code>FilterExpression</code> criteria are not returned.</p> <note> <p>A <code>FilterExpression</code> is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html#Scan.FilterExpression">Filter Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_names: <p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information on expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_values: <p>One or more values that can be substituted in an expression.</p> <p>Use the <b>:</b> (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the <code>ProductStatus</code> attribute was one of the following: </p> <p> <code>Available | Backordered | Discontinued</code> </p> <p>You would first need to specify <code>ExpressionAttributeValues</code> as follows:</p> <p> <code>{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }</code> </p> <p>You could then use these values in an expression, such as this:</p> <p> <code>ProductStatus IN (:avail, :back, :disc)</code> </p> <p>For more information on expression attribute values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Condition Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            consistent_read: <p>A Boolean value that determines the read consistency model during the scan:</p> <ul> <li> <p>If <code>ConsistentRead</code> is <code>false</code>, then the data returned from <code>Scan</code> might not contain the results from other recently completed write operations (<code>PutItem</code>, <code>UpdateItem</code>, or <code>DeleteItem</code>).</p> </li> <li> <p>If <code>ConsistentRead</code> is <code>true</code>, then all of the write operations that completed before the <code>Scan</code> began are guaranteed to be contained in the <code>Scan</code> response.</p> </li> </ul> <p>The default setting for <code>ConsistentRead</code> is <code>false</code>.</p> <p>The <code>ConsistentRead</code> parameter is not supported on global secondary indexes. If you scan a global secondary index with <code>ConsistentRead</code> set to true, you will receive a <code>ValidationException</code>.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To scan a table
            This example scans the entire Music table, and then narrows the results to songs by the artist "No One You Know". For each item, only the album title and song title are returned.

            >>> client.scan(table_name='Music', filter_expression='Artist = :a', projection_expression='#ST, #AT', expression_attribute_names={'#ST': 'SongTitle', '#AT': 'AlbumTitle'}, expression_attribute_values={':a': {'S': 'No One You Know'}})
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.scan_input.ScanInput]",
        ) -> OperationResponse["capo_dynamodb.types.scan_output.ScanOutput"]:
            import capo_dynamodb._operations.dynamo_db_20120810.scan

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.scan.scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.scan_input.ScanInput = {"table_name": table_name}
        if index_name is not None:
            input_["index_name"] = index_name
        if attributes_to_get is not None:
            input_["attributes_to_get"] = attributes_to_get
        if limit is not None:
            input_["limit"] = limit
        if select is not None:
            input_["select"] = select
        if scan_filter is not None:
            input_["scan_filter"] = scan_filter
        if conditional_operator is not None:
            input_["conditional_operator"] = conditional_operator
        if exclusive_start_key is not None:
            input_["exclusive_start_key"] = exclusive_start_key
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity
        if total_segments is not None:
            input_["total_segments"] = total_segments
        if segment is not None:
            input_["segment"] = segment
        if projection_expression is not None:
            input_["projection_expression"] = projection_expression
        if filter_expression is not None:
            input_["filter_expression"] = filter_expression
        if expression_attribute_names is not None:
            input_["expression_attribute_names"] = expression_attribute_names
        if expression_attribute_values is not None:
            input_["expression_attribute_values"] = expression_attribute_values
        if consistent_read is not None:
            input_["consistent_read"] = consistent_read

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_scan(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        index_name: Optional["capo_dynamodb.types.index_name.IndexName"] = None,
        attributes_to_get: Optional[
            "capo_dynamodb.types.attribute_name_list.AttributeNameList"
        ] = None,
        limit: Optional[
            "capo_dynamodb.types.positive_integer_object.PositiveIntegerObject"
        ] = None,
        select: Optional["capo_dynamodb.types.select.Select"] = None,
        scan_filter: Optional[
            "capo_dynamodb.types.filter_condition_map.FilterConditionMap"
        ] = None,
        conditional_operator: Optional[
            "capo_dynamodb.types.conditional_operator.ConditionalOperator"
        ] = None,
        exclusive_start_key: Optional["capo_dynamodb.types.key.Key"] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        total_segments: Optional[
            "capo_dynamodb.types.scan_total_segments.ScanTotalSegments"
        ] = None,
        segment: Optional["capo_dynamodb.types.scan_segment.ScanSegment"] = None,
        projection_expression: Optional[
            "capo_dynamodb.types.projection_expression.ProjectionExpression"
        ] = None,
        filter_expression: Optional[
            "capo_dynamodb.types.condition_expression.ConditionExpression"
        ] = None,
        expression_attribute_names: Optional[
            "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
        ] = None,
        expression_attribute_values: Optional[
            "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
        ] = None,
        consistent_read: Optional[
            "capo_dynamodb.types.consistent_read.ConsistentRead"
        ] = None,
    ) -> "Iterator[capo_dynamodb.types.attribute_map.AttributeMap]":
        _token = exclusive_start_key
        while True:
            _response = self.scan(
                table_name,
                config_overrides=config_overrides,
                index_name=index_name,
                attributes_to_get=attributes_to_get,
                limit=limit,
                select=select,
                scan_filter=scan_filter,
                conditional_operator=conditional_operator,
                exclusive_start_key=_token,
                return_consumed_capacity=return_consumed_capacity,
                total_segments=total_segments,
                segment=segment,
                projection_expression=projection_expression,
                filter_expression=filter_expression,
                expression_attribute_names=expression_attribute_names,
                expression_attribute_values=expression_attribute_values,
                consistent_read=consistent_read,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("last_evaluated_key",))
            if not _token:
                break

    def search_vectors(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        index_name: "capo_dynamodb.types.index_name.IndexName",
        search_vector: "capo_dynamodb.types.search_vector_list.SearchVectorList",
        top_k: "capo_dynamodb.types.top_k_integer.TopKInteger",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        expression_attribute_names: Optional[
            "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
        ] = None,
        expression_attribute_values: Optional[
            "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
        ] = None,
        projection_expression: Optional[
            "capo_dynamodb.types.projection_expression.ProjectionExpression"
        ] = None,
        search_condition_expression: Optional[
            "capo_dynamodb.types.string.String"
        ] = None,
    ) -> "capo_dynamodb.types.search_vectors_output.SearchVectorsOutput":
        """<p>Performs a vector similarity search on a vector index associated with an Amazon DynamoDB table, and returns the most similar items sorted by similarity score based on the distance function configured for the index.</p> <p>Score interpretation depends on the distance function:</p> <ul> <li> <p> <code>COSINE</code> - Returns the items with the <i>k smallest</i> scores. Scores range from 0 (identical) to 2 (opposite). Lower scores indicate higher similarity.</p> </li> <li> <p> <code>EUCLIDEAN</code> - Returns the items with the <i>k smallest</i> scores. Scores represent the Euclidean distance between vectors. Lower scores indicate higher similarity.</p> </li> <li> <p> <code>DOT_PRODUCT</code> - Returns the items with the <i>k highest</i> scores. Higher scores indicate higher similarity.</p> </li> </ul>

        Args:
            table_name: <p>The name or Amazon Resource Name (ARN) of the table containing the vector index.</p>
            index_name: <p>The name of the vector index to search. The index must be in the <code>ACTIVE</code> state.</p>
            expression_attribute_names: <p>One or more substitution tokens for attribute names in an expression. Use the <code>#</code> character in an expression to dereference an attribute name.</p>
            expression_attribute_values: <p>One or more values that can be substituted in an expression. Use the <code>:</code> character in an expression to dereference an attribute value.</p>
            projection_expression: <p>A string that identifies one or more attributes to retrieve from the index. Separate attribute names with commas. If not specified, the operation returns all attributes projected into the vector index.</p> <p>Only attributes projected into the vector index can be retrieved.</p>
            search_vector: <p>The search vector to compare against the indexed vectors. Each element is a 32-bit IEEE-754 floating point number, provided in DynamoDB list format.</p> <p>The number of dimensions must match the number of dimensions configured for the vector index.</p>
            search_condition_expression: <p>A condition expression used to filter the vector search results. The expression can reference attributes defined in the vector index search schema, including <code>HASH</code> and <code>INLINE_FILTER</code> key elements.</p> <p>Only the equality operator (<code>=</code>) is supported for <code>HASH</code> attributes. Comparison and range operators are supported for <code>INLINE_FILTER</code> attributes. Only top-level attributes from the search schema can be referenced.</p>
            top_k: <p>The number of most similar results to return.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To search for similar vectors
            This example searches the Products table for the top 3 items most similar to a provided vector, using the 'cosine-product-idx' vector index. The SearchConditionExpression filters results to the 'Electronics' category. The operation returns only the ProductName and Price attributes.

            >>> client.search_vectors(table_name='Products', index_name='cosine-product-idx', search_vector=[{'N': '0.12'}, {'N': '0.85'}, {'N': '0.44'}, {'N': '0.67'}], top_k=3, search_condition_expression='Category = :cat', projection_expression='ProductName, Price', expression_attribute_values={':cat': {'S': 'Electronics'}}, return_consumed_capacity='INDEXES')
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.search_vectors_input.SearchVectorsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.search_vectors_output.SearchVectorsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.search_vectors

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.search_vectors.search_vectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.search_vectors_input.SearchVectorsInput = {
            "table_name": table_name,
            "index_name": index_name,
            "search_vector": search_vector,
            "top_k": top_k,
        }
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity
        if expression_attribute_names is not None:
            input_["expression_attribute_names"] = expression_attribute_names
        if expression_attribute_values is not None:
            input_["expression_attribute_values"] = expression_attribute_values
        if projection_expression is not None:
            input_["projection_expression"] = projection_expression
        if search_condition_expression is not None:
            input_["search_condition_expression"] = search_condition_expression

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_dynamodb.types.resource_arn_string.ResourceArnString",
        tags: "capo_dynamodb.types.tag_list.TagList",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> None:
        """<p>Associate a set of tags with an Amazon DynamoDB resource. You can then activate these user-defined tags so that they appear on the Billing and Cost Management console for cost allocation tracking. You can call TagResource up to five times per second, per account. </p> <ul> <li> <p> <code>TagResource</code> is an asynchronous operation. If you issue a <a>ListTagsOfResource</a> request immediately after a <code>TagResource</code> request, DynamoDB might return your previous tag set, if there was one, or an empty tag set. This is because <code>ListTagsOfResource</code> uses an eventually consistent query, and the metadata for your tags or table might not be available at that moment. Wait for a few seconds, and then try the <code>ListTagsOfResource</code> request again.</p> </li> <li> <p>The application or removal of tags using <code>TagResource</code> and <code>UntagResource</code> APIs is eventually consistent. <code>ListTagsOfResource</code> API will only reflect the changes after a few seconds.</p> </li> </ul> <p>For an overview on tagging DynamoDB resources, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html">Tagging for DynamoDB</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>

        Args:
            resource_arn: <p>Identifies the Amazon DynamoDB resource to which tags should be added. This value is an Amazon Resource Name (ARN).</p>
            tags: <p>The tags to be assigned to the Amazon DynamoDB resource.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[None]:
            import capo_dynamodb._operations.dynamo_db_20120810.tag_resource

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.tag_resource_input.TagResourceInput = {
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

    def transact_get_items(
        self,
        transact_items: "capo_dynamodb.types.transact_get_item_list.TransactGetItemList",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
    ) -> "capo_dynamodb.types.transact_get_items_output.TransactGetItemsOutput":
        """<p> <code>TransactGetItems</code> is a synchronous operation that atomically retrieves multiple items from one or more tables (but not from indexes) in a single account and Region. A <code>TransactGetItems</code> call can contain up to 100 <code>TransactGetItem</code> objects, each of which contains a <code>Get</code> structure that specifies an item to retrieve from a table in the account and Region. A call to <code>TransactGetItems</code> cannot retrieve items from tables in more than one Amazon Web Services account or Region. The aggregate size of the items in the transaction cannot exceed 4 MB.</p> <p>DynamoDB rejects the entire <code>TransactGetItems</code> request if any of the following is true:</p> <ul> <li> <p>A conflicting operation is in the process of updating an item to be read.</p> </li> <li> <p>There is insufficient provisioned capacity for the transaction to be completed.</p> </li> <li> <p>There is a user error, such as an invalid data format.</p> </li> <li> <p>The aggregate size of the items in the transaction exceeded 4 MB.</p> </li> </ul>

        Args:
            transact_items: <p>An ordered array of up to 100 <code>TransactGetItem</code> objects, each of which contains a <code>Get</code> structure.</p>
            return_consumed_capacity: <p>A value of <code>TOTAL</code> causes consumed capacity information to be returned, and a value of <code>NONE</code> prevents that information from being returned. No other value is valid.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.transaction_canceled_exception.TransactionCanceledException: <p>The entire transaction request was canceled.</p> <p>DynamoDB cancels a <code>TransactWriteItems</code> request under the following circumstances:</p> <ul> <li> <p>A condition in one of the condition expressions is not met.</p> </li> <li> <p>A table in the <code>TransactWriteItems</code> request is in a different account or region.</p> </li> <li> <p>More than one action in the <code>TransactWriteItems</code> operation targets the same item.</p> </li> <li> <p>There is insufficient provisioned capacity for the transaction to be completed.</p> </li> <li> <p>An item size becomes too large (larger than 400 KB), or a local secondary index (LSI) becomes too large, or a similar validation error occurs because of changes made by the transaction.</p> </li> <li> <p>There is a user error, such as an invalid data format.</p> </li> <li> <p> There is an ongoing <code>TransactWriteItems</code> operation that conflicts with a concurrent <code>TransactWriteItems</code> request. In this case the <code>TransactWriteItems</code> operation fails with a <code>TransactionCanceledException</code>. </p> </li> </ul> <p>DynamoDB cancels a <code>TransactGetItems</code> request under the following circumstances:</p> <ul> <li> <p>There is an ongoing <code>TransactGetItems</code> operation that conflicts with a concurrent <code>PutItem</code>, <code>UpdateItem</code>, <code>DeleteItem</code> or <code>TransactWriteItems</code> request. In this case the <code>TransactGetItems</code> operation fails with a <code>TransactionCanceledException</code>.</p> </li> <li> <p>A table in the <code>TransactGetItems</code> request is in a different account or region.</p> </li> <li> <p>There is insufficient provisioned capacity for the transaction to be completed.</p> </li> <li> <p>There is a user error, such as an invalid data format.</p> </li> </ul> <note> <p>DynamoDB lists the cancellation reasons on the <code>CancellationReasons</code> property. Transaction cancellation reasons are ordered in the order of requested items, if an item has no error it will have <code>None</code> code and <code>Null</code> message. The <code>None</code> code is returned as the literal string <code>"None"</code>, not a null or absent value; the message field is omitted entirely for an item that has no error. This is important to note when using an SDK that surfaces the code as an optional or nullable type.</p> </note> <p>Cancellation reason codes and possible error messages:</p> <ul> <li> <p>No Errors:</p> <ul> <li> <p>Code: <code>None</code> </p> </li> <li> <p>Message: <code>null</code> </p> </li> </ul> </li> <li> <p>Conditional Check Failed:</p> <ul> <li> <p>Code: <code>ConditionalCheckFailed</code> </p> </li> <li> <p>Message: The conditional request failed. </p> </li> </ul> </li> <li> <p>Item Collection Size Limit Exceeded:</p> <ul> <li> <p>Code: <code>ItemCollectionSizeLimitExceeded</code> </p> </li> <li> <p>Message: Collection size exceeded.</p> </li> </ul> </li> <li> <p>Transaction Conflict:</p> <ul> <li> <p>Code: <code>TransactionConflict</code> </p> </li> <li> <p>Message: Transaction is ongoing for the item.</p> </li> </ul> </li> <li> <p>Provisioned Throughput Exceeded:</p> <ul> <li> <p>Code: <code>ProvisionedThroughputExceeded</code> </p> </li> <li> <p>Messages:</p> <ul> <li> <p>The level of configured provisioned throughput for the table was exceeded. Consider increasing your provisioning level with the UpdateTable API.</p> <note> <p>This Message is received when provisioned throughput is exceeded is on a provisioned DynamoDB table.</p> </note> </li> <li> <p>The level of configured provisioned throughput for one or more global secondary indexes of the table was exceeded. Consider increasing your provisioning level for the under-provisioned global secondary indexes with the UpdateTable API.</p> <note> <p>This message is returned when provisioned throughput is exceeded is on a provisioned GSI.</p> </note> </li> </ul> </li> </ul> </li> <li> <p>Throttling Error:</p> <ul> <li> <p>Code: <code>ThrottlingError</code> </p> </li> <li> <p>Messages: </p> <ul> <li> <p>Throughput exceeds the current capacity of your table or index. DynamoDB is automatically scaling your table or index so please try again shortly. If exceptions persist, check if you have a hot key: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html.</p> <note> <p>This message is returned when writes get throttled on an On-Demand table as DynamoDB is automatically scaling the table.</p> </note> </li> <li> <p>Throughput exceeds the current capacity for one or more global secondary indexes. DynamoDB is automatically scaling your index so please try again shortly.</p> <note> <p>This message is returned when writes get throttled on an On-Demand GSI as DynamoDB is automatically scaling the GSI.</p> </note> </li> </ul> </li> </ul> </li> <li> <p>Validation Error:</p> <ul> <li> <p>Code: <code>ValidationError</code> </p> </li> <li> <p>Messages: </p> <ul> <li> <p>One or more parameter values were invalid.</p> </li> <li> <p>The update expression attempted to update the secondary index key beyond allowed size limits.</p> </li> <li> <p>The update expression attempted to update the secondary index key to unsupported type.</p> </li> <li> <p>An operand in the update expression has an incorrect data type.</p> </li> <li> <p>Item size to update has exceeded the maximum allowed size.</p> </li> <li> <p>Number overflow. Attempting to store a number with magnitude larger than supported range.</p> </li> <li> <p>Type mismatch for attribute to update.</p> </li> <li> <p>Nesting Levels have exceeded supported limits.</p> </li> <li> <p>The document path provided in the update expression is invalid for update.</p> </li> <li> <p>The provided expression refers to an attribute that does not exist in the item.</p> </li> </ul> </li> </ul> </li> </ul>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.transact_get_items_input.TransactGetItemsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.transact_get_items_output.TransactGetItemsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.transact_get_items

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.transact_get_items.transact_get_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.transact_get_items_input.TransactGetItemsInput = {
            "transact_items": transact_items
        }
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def transact_write_items(
        self,
        transact_items: "capo_dynamodb.types.transact_write_item_list.TransactWriteItemList",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        return_item_collection_metrics: Optional[
            "capo_dynamodb.types.return_item_collection_metrics.ReturnItemCollectionMetrics"
        ] = None,
        client_request_token: Optional[
            "capo_dynamodb.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_dynamodb.types.transact_write_items_output.TransactWriteItemsOutput":
        """<p> <code>TransactWriteItems</code> is a synchronous write operation that groups up to 100 action requests. These actions can target items in different tables, but not in different Amazon Web Services accounts or Regions, and no two actions can target the same item. For example, you cannot both <code>ConditionCheck</code> and <code>Update</code> the same item. The aggregate size of the items in the transaction cannot exceed 4 MB.</p> <p>The actions are completed atomically so that either all of them succeed, or all of them fail. They are defined by the following objects:</p> <ul> <li> <p> <code>Put</code> — Initiates a <code>PutItem</code> operation to write a new item. This structure specifies the primary key of the item to be written, the name of the table to write it in, an optional condition expression that must be satisfied for the write to succeed, a list of the item's attributes, and a field indicating whether to retrieve the item's attributes if the condition is not met.</p> </li> <li> <p> <code>Update</code> — Initiates an <code>UpdateItem</code> operation to update an existing item. This structure specifies the primary key of the item to be updated, the name of the table where it resides, an optional condition expression that must be satisfied for the update to succeed, an expression that defines one or more attributes to be updated, and a field indicating whether to retrieve the item's attributes if the condition is not met.</p> </li> <li> <p> <code>Delete</code> — Initiates a <code>DeleteItem</code> operation to delete an existing item. This structure specifies the primary key of the item to be deleted, the name of the table where it resides, an optional condition expression that must be satisfied for the deletion to succeed, and a field indicating whether to retrieve the item's attributes if the condition is not met.</p> </li> <li> <p> <code>ConditionCheck</code> — Applies a condition to an item that is not being modified by the transaction. This structure specifies the primary key of the item to be checked, the name of the table where it resides, a condition expression that must be satisfied for the transaction to succeed, and a field indicating whether to retrieve the item's attributes if the condition is not met.</p> </li> </ul> <p>DynamoDB rejects the entire <code>TransactWriteItems</code> request if any of the following is true:</p> <ul> <li> <p>A condition in one of the condition expressions is not met.</p> </li> <li> <p>An ongoing operation is in the process of updating the same item.</p> </li> <li> <p>There is insufficient provisioned capacity for the transaction to be completed.</p> </li> <li> <p>An item size becomes too large (bigger than 400 KB), a local secondary index (LSI) becomes too large, or a similar validation error occurs because of changes made by the transaction.</p> </li> <li> <p>The aggregate size of the items in the transaction exceeds 4 MB.</p> </li> <li> <p>There is a user error, such as an invalid data format.</p> </li> </ul>

        Args:
            transact_items: <p>An ordered array of up to 100 <code>TransactWriteItem</code> objects, each of which contains a <code>ConditionCheck</code>, <code>Put</code>, <code>Update</code>, or <code>Delete</code> object. These can operate on items in different tables, but the tables must reside in the same Amazon Web Services account and Region, and no two of them can operate on the same item. </p>
            return_item_collection_metrics: <p>Determines whether item collection metrics are returned. If set to <code>SIZE</code>, the response includes statistics about item collections (if any), that were modified during the operation and are returned in the response. If set to <code>NONE</code> (the default), no statistics are returned. </p>
            client_request_token: <p>Providing a <code>ClientRequestToken</code> makes the call to <code>TransactWriteItems</code> idempotent, meaning that multiple identical calls have the same effect as one single call.</p> <p>Although multiple identical calls using the same client request token produce the same result on the server (no side effects), the responses to the calls might not be the same. If the <code>ReturnConsumedCapacity</code> parameter is set, then the initial <code>TransactWriteItems</code> call returns the amount of write capacity units consumed in making the changes. Subsequent <code>TransactWriteItems</code> calls with the same client token return the number of read capacity units consumed in reading the item.</p> <p>A client request token is valid for 10 minutes after the first request that uses it is completed. After 10 minutes, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 10 minutes, or the result might not be idempotent.</p> <p>If you submit a request with the same client token but a change in other parameters within the 10-minute idempotency window, DynamoDB returns an <code>IdempotentParameterMismatch</code> exception.</p>

        Raises:
            capo_dynamodb.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>DynamoDB rejected the request because you retried a request with a different payload but with an idempotent token that was already used.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.transaction_canceled_exception.TransactionCanceledException: <p>The entire transaction request was canceled.</p> <p>DynamoDB cancels a <code>TransactWriteItems</code> request under the following circumstances:</p> <ul> <li> <p>A condition in one of the condition expressions is not met.</p> </li> <li> <p>A table in the <code>TransactWriteItems</code> request is in a different account or region.</p> </li> <li> <p>More than one action in the <code>TransactWriteItems</code> operation targets the same item.</p> </li> <li> <p>There is insufficient provisioned capacity for the transaction to be completed.</p> </li> <li> <p>An item size becomes too large (larger than 400 KB), or a local secondary index (LSI) becomes too large, or a similar validation error occurs because of changes made by the transaction.</p> </li> <li> <p>There is a user error, such as an invalid data format.</p> </li> <li> <p> There is an ongoing <code>TransactWriteItems</code> operation that conflicts with a concurrent <code>TransactWriteItems</code> request. In this case the <code>TransactWriteItems</code> operation fails with a <code>TransactionCanceledException</code>. </p> </li> </ul> <p>DynamoDB cancels a <code>TransactGetItems</code> request under the following circumstances:</p> <ul> <li> <p>There is an ongoing <code>TransactGetItems</code> operation that conflicts with a concurrent <code>PutItem</code>, <code>UpdateItem</code>, <code>DeleteItem</code> or <code>TransactWriteItems</code> request. In this case the <code>TransactGetItems</code> operation fails with a <code>TransactionCanceledException</code>.</p> </li> <li> <p>A table in the <code>TransactGetItems</code> request is in a different account or region.</p> </li> <li> <p>There is insufficient provisioned capacity for the transaction to be completed.</p> </li> <li> <p>There is a user error, such as an invalid data format.</p> </li> </ul> <note> <p>DynamoDB lists the cancellation reasons on the <code>CancellationReasons</code> property. Transaction cancellation reasons are ordered in the order of requested items, if an item has no error it will have <code>None</code> code and <code>Null</code> message. The <code>None</code> code is returned as the literal string <code>"None"</code>, not a null or absent value; the message field is omitted entirely for an item that has no error. This is important to note when using an SDK that surfaces the code as an optional or nullable type.</p> </note> <p>Cancellation reason codes and possible error messages:</p> <ul> <li> <p>No Errors:</p> <ul> <li> <p>Code: <code>None</code> </p> </li> <li> <p>Message: <code>null</code> </p> </li> </ul> </li> <li> <p>Conditional Check Failed:</p> <ul> <li> <p>Code: <code>ConditionalCheckFailed</code> </p> </li> <li> <p>Message: The conditional request failed. </p> </li> </ul> </li> <li> <p>Item Collection Size Limit Exceeded:</p> <ul> <li> <p>Code: <code>ItemCollectionSizeLimitExceeded</code> </p> </li> <li> <p>Message: Collection size exceeded.</p> </li> </ul> </li> <li> <p>Transaction Conflict:</p> <ul> <li> <p>Code: <code>TransactionConflict</code> </p> </li> <li> <p>Message: Transaction is ongoing for the item.</p> </li> </ul> </li> <li> <p>Provisioned Throughput Exceeded:</p> <ul> <li> <p>Code: <code>ProvisionedThroughputExceeded</code> </p> </li> <li> <p>Messages:</p> <ul> <li> <p>The level of configured provisioned throughput for the table was exceeded. Consider increasing your provisioning level with the UpdateTable API.</p> <note> <p>This Message is received when provisioned throughput is exceeded is on a provisioned DynamoDB table.</p> </note> </li> <li> <p>The level of configured provisioned throughput for one or more global secondary indexes of the table was exceeded. Consider increasing your provisioning level for the under-provisioned global secondary indexes with the UpdateTable API.</p> <note> <p>This message is returned when provisioned throughput is exceeded is on a provisioned GSI.</p> </note> </li> </ul> </li> </ul> </li> <li> <p>Throttling Error:</p> <ul> <li> <p>Code: <code>ThrottlingError</code> </p> </li> <li> <p>Messages: </p> <ul> <li> <p>Throughput exceeds the current capacity of your table or index. DynamoDB is automatically scaling your table or index so please try again shortly. If exceptions persist, check if you have a hot key: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html.</p> <note> <p>This message is returned when writes get throttled on an On-Demand table as DynamoDB is automatically scaling the table.</p> </note> </li> <li> <p>Throughput exceeds the current capacity for one or more global secondary indexes. DynamoDB is automatically scaling your index so please try again shortly.</p> <note> <p>This message is returned when writes get throttled on an On-Demand GSI as DynamoDB is automatically scaling the GSI.</p> </note> </li> </ul> </li> </ul> </li> <li> <p>Validation Error:</p> <ul> <li> <p>Code: <code>ValidationError</code> </p> </li> <li> <p>Messages: </p> <ul> <li> <p>One or more parameter values were invalid.</p> </li> <li> <p>The update expression attempted to update the secondary index key beyond allowed size limits.</p> </li> <li> <p>The update expression attempted to update the secondary index key to unsupported type.</p> </li> <li> <p>An operand in the update expression has an incorrect data type.</p> </li> <li> <p>Item size to update has exceeded the maximum allowed size.</p> </li> <li> <p>Number overflow. Attempting to store a number with magnitude larger than supported range.</p> </li> <li> <p>Type mismatch for attribute to update.</p> </li> <li> <p>Nesting Levels have exceeded supported limits.</p> </li> <li> <p>The document path provided in the update expression is invalid for update.</p> </li> <li> <p>The provided expression refers to an attribute that does not exist in the item.</p> </li> </ul> </li> </ul> </li> </ul>
            capo_dynamodb.errors.transaction_in_progress_exception.TransactionInProgressException: <p>The transaction with the given request token is already in progress.</p> <p> Recommended Settings </p> <note> <p> This is a general recommendation for handling the <code>TransactionInProgressException</code>. These settings help ensure that the client retries will trigger completion of the ongoing <code>TransactWriteItems</code> request. </p> </note> <ul> <li> <p> Set <code>clientExecutionTimeout</code> to a value that allows at least one retry to be processed after 5 seconds have elapsed since the first attempt for the <code>TransactWriteItems</code> operation. </p> </li> <li> <p> Set <code>socketTimeout</code> to a value a little lower than the <code>requestTimeout</code> setting. </p> </li> <li> <p> <code>requestTimeout</code> should be set based on the time taken for the individual retries of a single HTTP request for your use case, but setting it to 1 second or higher should work well to reduce chances of retries and <code>TransactionInProgressException</code> errors. </p> </li> <li> <p> Use exponential backoff when retrying and tune backoff if needed. </p> </li> </ul> <p> Assuming <a href="https://github.com/aws/aws-sdk-java/blob/fd409dee8ae23fb8953e0bb4dbde65536a7e0514/aws-java-sdk-core/src/main/java/com/amazonaws/retry/PredefinedRetryPolicies.java#L97">default retry policy</a>, example timeout settings based on the guidelines above are as follows: </p> <p>Example timeline:</p> <ul> <li> <p>0-1000 first attempt</p> </li> <li> <p>1000-1500 first sleep/delay (default retry policy uses 500 ms as base delay for 4xx errors)</p> </li> <li> <p>1500-2500 second attempt</p> </li> <li> <p>2500-3500 second sleep/delay (500 * 2, exponential backoff)</p> </li> <li> <p>3500-4500 third attempt</p> </li> <li> <p>4500-6500 third sleep/delay (500 * 2^2)</p> </li> <li> <p>6500-7500 fourth attempt (this can trigger inline recovery since 5 seconds have elapsed since the first attempt reached TC)</p> </li> </ul>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.transact_write_items_input.TransactWriteItemsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.transact_write_items_output.TransactWriteItemsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.transact_write_items

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.transact_write_items.transact_write_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.transact_write_items_input.TransactWriteItemsInput = {
            "transact_items": transact_items
        }
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity
        if return_item_collection_metrics is not None:
            input_["return_item_collection_metrics"] = return_item_collection_metrics
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_dynamodb.types.resource_arn_string.ResourceArnString",
        tag_keys: "capo_dynamodb.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> None:
        """<p>Removes the association of tags from an Amazon DynamoDB resource. You can call <code>UntagResource</code> up to five times per second, per account. </p> <ul> <li> <p> <code>UntagResource</code> is an asynchronous operation. If you issue a <a>ListTagsOfResource</a> request immediately after an <code>UntagResource</code> request, DynamoDB might return your previous tag set, if there was one, or an empty tag set. This is because <code>ListTagsOfResource</code> uses an eventually consistent query, and the metadata for your tags or table might not be available at that moment. Wait for a few seconds, and then try the <code>ListTagsOfResource</code> request again.</p> </li> <li> <p>The application or removal of tags using <code>TagResource</code> and <code>UntagResource</code> APIs is eventually consistent. <code>ListTagsOfResource</code> API will only reflect the changes after a few seconds.</p> </li> </ul> <p>For an overview on tagging DynamoDB resources, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tagging.html">Tagging for DynamoDB</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>

        Args:
            resource_arn: <p>The DynamoDB resource that the tags will be removed from. This value is an Amazon Resource Name (ARN).</p>
            tag_keys: <p>A list of tag keys. Existing tags of the resource whose keys are members of this list will be removed from the DynamoDB resource.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[None]:
            import capo_dynamodb._operations.dynamo_db_20120810.untag_resource

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.untag_resource_input.UntagResourceInput = {
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

    def update_continuous_backups(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        point_in_time_recovery_specification: "capo_dynamodb.types.point_in_time_recovery_specification.PointInTimeRecoverySpecification",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.update_continuous_backups_output.UpdateContinuousBackupsOutput":
        """<p> <code>UpdateContinuousBackups</code> enables or disables point in time recovery for the specified table. A successful <code>UpdateContinuousBackups</code> call returns the current <code>ContinuousBackupsDescription</code>. Continuous backups are <code>ENABLED</code> on all tables at table creation. If point in time recovery is enabled, <code>PointInTimeRecoveryStatus</code> will be set to ENABLED.</p> <p> Once continuous backups and point in time recovery are enabled, you can restore to any point in time within <code>EarliestRestorableDateTime</code> and <code>LatestRestorableDateTime</code>. </p> <p> <code>LatestRestorableDateTime</code> is typically 5 minutes before the current time. You can restore your table to any point in time in the last 35 days. You can set the <code>RecoveryPeriodInDays</code> to any value between 1 and 35 days.</p>

        Args:
            table_name: <p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            point_in_time_recovery_specification: <p>Represents the settings used to enable point in time recovery.</p>

        Raises:
            capo_dynamodb.errors.continuous_backups_unavailable_exception.ContinuousBackupsUnavailableException: <p>Backups have not yet been enabled for this table.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.table_not_found_exception.TableNotFoundException: <p>A source table with the name <code>TableName</code> does not currently exist within the subscriber's account or the subscriber is operating in the wrong Amazon Web Services Region.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.update_continuous_backups_input.UpdateContinuousBackupsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.update_continuous_backups_output.UpdateContinuousBackupsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.update_continuous_backups

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.update_continuous_backups.update_continuous_backups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.update_continuous_backups_input.UpdateContinuousBackupsInput = {
            "table_name": table_name,
            "point_in_time_recovery_specification": point_in_time_recovery_specification,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_contributor_insights(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        contributor_insights_action: "capo_dynamodb.types.contributor_insights_action.ContributorInsightsAction",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        index_name: Optional["capo_dynamodb.types.index_name.IndexName"] = None,
        contributor_insights_mode: Optional[
            "capo_dynamodb.types.contributor_insights_mode.ContributorInsightsMode"
        ] = None,
    ) -> "capo_dynamodb.types.update_contributor_insights_output.UpdateContributorInsightsOutput":
        """<p>Updates the status for contributor insights for a specific table or index. CloudWatch Contributor Insights for DynamoDB graphs display the partition key and (if applicable) sort key of frequently accessed items and frequently throttled items in plaintext. If you require the use of Amazon Web Services Key Management Service (KMS) to encrypt this table’s partition key and sort key data with an Amazon Web Services managed key or customer managed key, you should not enable CloudWatch Contributor Insights for DynamoDB for this table.</p>

        Args:
            table_name: <p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            index_name: <p>The global secondary index name, if applicable.</p>
            contributor_insights_action: <p>Represents the contributor insights action.</p>
            contributor_insights_mode: <p>Specifies whether to track all access and throttled events or throttled events only for the DynamoDB table or index.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.update_contributor_insights_input.UpdateContributorInsightsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.update_contributor_insights_output.UpdateContributorInsightsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.update_contributor_insights

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.update_contributor_insights.update_contributor_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.update_contributor_insights_input.UpdateContributorInsightsInput = {
            "table_name": table_name,
            "contributor_insights_action": contributor_insights_action,
        }
        if index_name is not None:
            input_["index_name"] = index_name
        if contributor_insights_mode is not None:
            input_["contributor_insights_mode"] = contributor_insights_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_global_table(
        self,
        global_table_name: "capo_dynamodb.types.table_name.TableName",
        replica_updates: "capo_dynamodb.types.replica_update_list.ReplicaUpdateList",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.update_global_table_output.UpdateGlobalTableOutput":
        """<p>Adds or removes replicas in the specified global table. The global table must already exist to be able to use this operation. Any replica to be added must be empty, have the same name as the global table, have the same key schema, have DynamoDB Streams enabled, and have the same provisioned and maximum write capacity units.</p> <important> <p>This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html">Global Tables version 2019.11.21 (Current)</a> when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).</p> <p>To determine which version you're using, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html">Determining the global table version you are using</a>. To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html">Upgrading global tables</a>.</p> </important> <note> <p> If you are using global tables <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html">Version 2019.11.21</a> (Current) you can use <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html">UpdateTable</a> instead. </p> <p> Although you can use <code>UpdateGlobalTable</code> to add replicas and remove replicas in a single request, for simplicity we recommend that you issue separate requests for adding or removing replicas. </p> </note> <p> If global secondary indexes are specified, then the following conditions must also be met: </p> <ul> <li> <p> The global secondary indexes must have the same name. </p> </li> <li> <p> The global secondary indexes must have the same hash key and sort key (if present). </p> </li> <li> <p> The global secondary indexes must have the same provisioned and maximum write capacity units. </p> </li> </ul>

        Args:
            global_table_name: <p>The global table name.</p>
            replica_updates: <p>A list of Regions that should be added or removed from the global table.</p>

        Raises:
            capo_dynamodb.errors.global_table_not_found_exception.GlobalTableNotFoundException: <p>The specified global table does not exist.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.replica_already_exists_exception.ReplicaAlreadyExistsException: <p>The specified replica is already part of the global table.</p>
            capo_dynamodb.errors.replica_not_found_exception.ReplicaNotFoundException: <p>The specified replica is no longer part of the global table.</p>
            capo_dynamodb.errors.table_not_found_exception.TableNotFoundException: <p>A source table with the name <code>TableName</code> does not currently exist within the subscriber's account or the subscriber is operating in the wrong Amazon Web Services Region.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.update_global_table_input.UpdateGlobalTableInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.update_global_table_output.UpdateGlobalTableOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.update_global_table

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.update_global_table.update_global_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.update_global_table_input.UpdateGlobalTableInput = {
            "global_table_name": global_table_name,
            "replica_updates": replica_updates,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_global_table_settings(
        self,
        global_table_name: "capo_dynamodb.types.table_name.TableName",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        global_table_billing_mode: Optional[
            "capo_dynamodb.types.billing_mode.BillingMode"
        ] = None,
        global_table_provisioned_write_capacity_units: Optional[
            "capo_dynamodb.types.positive_long_object.PositiveLongObject"
        ] = None,
        global_table_provisioned_write_capacity_auto_scaling_settings_update: Optional[
            "capo_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
        ] = None,
        global_table_global_secondary_index_settings_update: Optional[
            "capo_dynamodb.types.global_table_global_secondary_index_settings_update_list.GlobalTableGlobalSecondaryIndexSettingsUpdateList"
        ] = None,
        replica_settings_update: Optional[
            "capo_dynamodb.types.replica_settings_update_list.ReplicaSettingsUpdateList"
        ] = None,
    ) -> "capo_dynamodb.types.update_global_table_settings_output.UpdateGlobalTableSettingsOutput":
        """<p>Updates settings for a global table.</p> <important> <p>This documentation is for version 2017.11.29 (Legacy) of global tables, which should be avoided for new global tables. Customers should use <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html">Global Tables version 2019.11.21 (Current)</a> when possible, because it provides greater flexibility, higher efficiency, and consumes less write capacity than 2017.11.29 (Legacy).</p> <p>To determine which version you're using, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.DetermineVersion.html">Determining the global table version you are using</a>. To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_upgrade.html">Upgrading global tables</a>.</p> </important>

        Args:
            global_table_name: <p>The name of the global table</p>
            global_table_billing_mode: <p>The billing mode of the global table. If <code>GlobalTableBillingMode</code> is not specified, the global table defaults to <code>PROVISIONED</code> capacity billing mode.</p> <ul> <li> <p> <code>PROVISIONED</code> - We recommend using <code>PROVISIONED</code> for predictable workloads. <code>PROVISIONED</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html">Provisioned capacity mode</a>.</p> </li> <li> <p> <code>PAY_PER_REQUEST</code> - We recommend using <code>PAY_PER_REQUEST</code> for unpredictable workloads. <code>PAY_PER_REQUEST</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html">On-demand capacity mode</a>. </p> </li> </ul>
            global_table_provisioned_write_capacity_units: <p>The maximum number of writes consumed per second before DynamoDB returns a <code>ThrottlingException.</code> </p>
            global_table_provisioned_write_capacity_auto_scaling_settings_update: <p>Auto scaling settings for managing provisioned write capacity for the global table.</p>
            global_table_global_secondary_index_settings_update: <p>Represents the settings of a global secondary index for a global table that will be modified.</p>
            replica_settings_update: <p>Represents the settings for a global table in a Region that will be modified.</p>

        Raises:
            capo_dynamodb.errors.global_table_not_found_exception.GlobalTableNotFoundException: <p>The specified global table does not exist.</p>
            capo_dynamodb.errors.index_not_found_exception.IndexNotFoundException: <p>The operation tried to access a nonexistent index.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.replica_not_found_exception.ReplicaNotFoundException: <p>The specified replica is no longer part of the global table.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.update_global_table_settings_input.UpdateGlobalTableSettingsInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.update_global_table_settings_output.UpdateGlobalTableSettingsOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.update_global_table_settings

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.update_global_table_settings.update_global_table_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.update_global_table_settings_input.UpdateGlobalTableSettingsInput = {
            "global_table_name": global_table_name
        }
        if global_table_billing_mode is not None:
            input_["global_table_billing_mode"] = global_table_billing_mode
        if global_table_provisioned_write_capacity_units is not None:
            input_["global_table_provisioned_write_capacity_units"] = (
                global_table_provisioned_write_capacity_units
            )
        if (
            global_table_provisioned_write_capacity_auto_scaling_settings_update
            is not None
        ):
            input_[
                "global_table_provisioned_write_capacity_auto_scaling_settings_update"
            ] = global_table_provisioned_write_capacity_auto_scaling_settings_update
        if global_table_global_secondary_index_settings_update is not None:
            input_["global_table_global_secondary_index_settings_update"] = (
                global_table_global_secondary_index_settings_update
            )
        if replica_settings_update is not None:
            input_["replica_settings_update"] = replica_settings_update

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_item(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        key: "capo_dynamodb.types.key.Key",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        attribute_updates: Optional[
            "capo_dynamodb.types.attribute_updates.AttributeUpdates"
        ] = None,
        expected: Optional[
            "capo_dynamodb.types.expected_attribute_map.ExpectedAttributeMap"
        ] = None,
        conditional_operator: Optional[
            "capo_dynamodb.types.conditional_operator.ConditionalOperator"
        ] = None,
        return_values: Optional["capo_dynamodb.types.return_value.ReturnValue"] = None,
        return_consumed_capacity: Optional[
            "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
        ] = None,
        return_item_collection_metrics: Optional[
            "capo_dynamodb.types.return_item_collection_metrics.ReturnItemCollectionMetrics"
        ] = None,
        update_expression: Optional[
            "capo_dynamodb.types.update_expression.UpdateExpression"
        ] = None,
        condition_expression: Optional[
            "capo_dynamodb.types.condition_expression.ConditionExpression"
        ] = None,
        expression_attribute_names: Optional[
            "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
        ] = None,
        expression_attribute_values: Optional[
            "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
        ] = None,
        return_values_on_condition_check_failure: Optional[
            "capo_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
        ] = None,
    ) -> "capo_dynamodb.types.update_item_output.UpdateItemOutput":
        """<p>Edits an existing item's attributes, or adds a new item to the table if it does not already exist. You can put, delete, or add attribute values. You can also perform a conditional update on an existing item (insert a new attribute name-value pair if it doesn't exist, or replace an existing name-value pair if it has certain expected attribute values).</p> <p>You can also return the item's attribute values in the same <code>UpdateItem</code> operation using the <code>ReturnValues</code> parameter.</p>

        Args:
            table_name: <p>The name of the table containing the item to update. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            key: <p>The primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute.</p> <p>For the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.</p>
            attribute_updates: <p>This is a legacy parameter. Use <code>UpdateExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributeUpdates.html">AttributeUpdates</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expected: <p>This is a legacy parameter. Use <code>ConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.Expected.html">Expected</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            conditional_operator: <p>This is a legacy parameter. Use <code>ConditionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html">ConditionalOperator</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            return_values: <p>Use <code>ReturnValues</code> if you want to get the item attributes as they appear before or after they are successfully updated. For <code>UpdateItem</code>, the valid values are:</p> <ul> <li> <p> <code>NONE</code> - If <code>ReturnValues</code> is not specified, or if its value is <code>NONE</code>, then nothing is returned. (This setting is the default for <code>ReturnValues</code>.)</p> </li> <li> <p> <code>ALL_OLD</code> - Returns all of the attributes of the item, as they appeared before the UpdateItem operation.</p> </li> <li> <p> <code>UPDATED_OLD</code> - Returns only the updated attributes, as they appeared before the UpdateItem operation.</p> </li> <li> <p> <code>ALL_NEW</code> - Returns all of the attributes of the item, as they appear after the UpdateItem operation.</p> </li> <li> <p> <code>UPDATED_NEW</code> - Returns only the updated attributes, as they appear after the UpdateItem operation.</p> </li> </ul> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p> <p>The values returned are strongly consistent.</p>
            return_item_collection_metrics: <p>Determines whether item collection metrics are returned. If set to <code>SIZE</code>, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to <code>NONE</code> (the default), no statistics are returned.</p>
            update_expression: <p>An expression that defines one or more attributes to be updated, the action to be performed on them, and new values for them.</p> <p>The following action values are available for <code>UpdateExpression</code>.</p> <ul> <li> <p> <code>SET</code> - Adds one or more attributes and values to an item. If any of these attributes already exist, they are replaced by the new values. You can also use <code>SET</code> to add or subtract from an attribute that is of type Number. For example: <code>SET myNum = myNum + :val</code> </p> <p> <code>SET</code> supports the following functions:</p> <ul> <li> <p> <code>if_not_exists (path, operand)</code> - if the item does not contain an attribute at the specified path, then <code>if_not_exists</code> evaluates to operand; otherwise, it evaluates to path. You can use this function to avoid overwriting an attribute that may already be present in the item.</p> </li> <li> <p> <code>list_append (operand, operand)</code> - evaluates to a list with a new element added to it. You can append the new element to the start or the end of the list by reversing the order of the operands.</p> </li> </ul> <p>These function names are case-sensitive.</p> </li> <li> <p> <code>REMOVE</code> - Removes one or more attributes from an item.</p> </li> <li> <p> <code>ADD</code> - Adds the specified value to the item, if the attribute does not already exist. If the attribute does exist, then the behavior of <code>ADD</code> depends on the data type of the attribute:</p> <ul> <li> <p>If the existing attribute is a number, and if <code>Value</code> is also a number, then <code>Value</code> is mathematically added to the existing attribute. If <code>Value</code> is a negative number, then it is subtracted from the existing attribute.</p> <note> <p>If you use <code>ADD</code> to increment or decrement a number value for an item that doesn't exist before the update, DynamoDB uses <code>0</code> as the initial value.</p> <p>Similarly, if you use <code>ADD</code> for an existing item to increment or decrement an attribute value that doesn't exist before the update, DynamoDB uses <code>0</code> as the initial value. For example, suppose that the item you want to update doesn't have an attribute named <code>itemcount</code>, but you decide to <code>ADD</code> the number <code>3</code> to this attribute anyway. DynamoDB will create the <code>itemcount</code> attribute, set its initial value to <code>0</code>, and finally add <code>3</code> to it. The result will be a new <code>itemcount</code> attribute in the item, with a value of <code>3</code>.</p> </note> </li> <li> <p>If the existing data type is a set and if <code>Value</code> is also a set, then <code>Value</code> is added to the existing set. For example, if the attribute value is the set <code>[1,2]</code>, and the <code>ADD</code> action specified <code>[3]</code>, then the final attribute value is <code>[1,2,3]</code>. An error occurs if an <code>ADD</code> action is specified for a set attribute and the attribute type specified does not match the existing set type. </p> <p>Both sets must have the same primitive data type. For example, if the existing data type is a set of strings, the <code>Value</code> must also be a set of strings.</p> </li> </ul> <important> <p>The <code>ADD</code> action only supports Number and set data types.</p> </important> </li> <li> <p> <code>DELETE</code> - Deletes an element from a set.</p> <p>If a set of values is specified, then those values are subtracted from the old set. For example, if the attribute value was the set <code>[a,b,c]</code> and the <code>DELETE</code> action specifies <code>[a,c]</code>, then the final attribute value is <code>[b]</code>. Specifying an empty set is an error.</p> <important> <p>The <code>DELETE</code> action only supports set data types.</p> </important> </li> </ul> <p>You can have many actions in a single expression, such as the following: <code>SET a=:value1, b=:value2 DELETE :value3, :value4, :value5</code> </p> <p>For more information on update expressions, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.Modifying.html">Modifying Items and Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            condition_expression: <p>A condition that must be satisfied in order for a conditional update to succeed.</p> <p>An expression can contain any of the following:</p> <ul> <li> <p>Functions: <code>attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size</code> </p> <p>These function names are case-sensitive.</p> </li> <li> <p>Comparison operators: <code>= | <> | < | > | <= | >= | BETWEEN | IN </code> </p> </li> <li> <p> Logical operators: <code>AND | OR | NOT</code> </p> </li> </ul> <p>For more information about condition expressions, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Specifying Conditions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_names: <p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>.) To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information about expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            expression_attribute_values: <p>One or more values that can be substituted in an expression.</p> <p>Use the <b>:</b> (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the <code>ProductStatus</code> attribute was one of the following: </p> <p> <code>Available | Backordered | Discontinued</code> </p> <p>You would first need to specify <code>ExpressionAttributeValues</code> as follows:</p> <p> <code>{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }</code> </p> <p>You could then use these values in an expression, such as this:</p> <p> <code>ProductStatus IN (:avail, :back, :disc)</code> </p> <p>For more information on expression attribute values, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html">Condition Expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            return_values_on_condition_check_failure: <p>An optional parameter that returns the item attributes for an <code>UpdateItem</code> operation that failed a condition check.</p> <p>There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed.</p>

        Raises:
            capo_dynamodb.errors.conditional_check_failed_exception.ConditionalCheckFailedException: <p>A condition specified in the operation failed to be evaluated.</p>
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.item_collection_size_limit_exceeded_exception.ItemCollectionSizeLimitExceededException: <p>An item collection is too large. This exception is only returned for tables that have one or more local secondary indexes.</p>
            capo_dynamodb.errors.provisioned_throughput_exceeded_exception.ProvisionedThroughputExceededException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. The Amazon Web Services SDKs for DynamoDB automatically retry requests that receive this exception. Your request is eventually successful, unless your retry queue is too large to finish. Reduce the frequency of requests and use exponential backoff. For more information, go to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.RetryAndBackoff">Error Retries and Exponential Backoff</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>
            capo_dynamodb.errors.replicated_write_conflict_exception.ReplicatedWriteConflictException: <p>The request was rejected because one or more items in the request are being modified by a request in another Region. </p>
            capo_dynamodb.errors.request_limit_exceeded.RequestLimitExceeded: <p>Throughput exceeds the current throughput quota for your account. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception. Contact <a href="https://aws.amazon.com/support">Amazon Web Services Support</a> to request a quota increase.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. For detailed information about why the request was throttled and the ARN of the impacted resource, find the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html">ThrottlingReason</a> field in the returned exception.</p>
            capo_dynamodb.errors.transaction_conflict_exception.TransactionConflictException: <p>Operation was rejected because there is an ongoing transaction for the item.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update an item in a table
            This example updates an item in the Music table. It adds a new attribute (Year) and modifies the AlbumTitle attribute.  All of the attributes in the item, as they appear after the update, are returned in the response.

            >>> client.update_item(table_name='Music', key={'Artist': {'S': 'Acme Band'}, 'SongTitle': {'S': 'Happy Day'}}, update_expression='SET #Y = :y, #AT = :t', expression_attribute_names={'#Y': 'Year', '#AT': 'AlbumTitle'}, expression_attribute_values={':y': {'N': '2015'}, ':t': {'S': 'Louder Than Ever'}}, return_values='ALL_NEW')
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.update_item_input.UpdateItemInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.update_item_output.UpdateItemOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.update_item

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.update_item.update_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.update_item_input.UpdateItemInput = {
            "table_name": table_name,
            "key": key,
        }
        if attribute_updates is not None:
            input_["attribute_updates"] = attribute_updates
        if expected is not None:
            input_["expected"] = expected
        if conditional_operator is not None:
            input_["conditional_operator"] = conditional_operator
        if return_values is not None:
            input_["return_values"] = return_values
        if return_consumed_capacity is not None:
            input_["return_consumed_capacity"] = return_consumed_capacity
        if return_item_collection_metrics is not None:
            input_["return_item_collection_metrics"] = return_item_collection_metrics
        if update_expression is not None:
            input_["update_expression"] = update_expression
        if condition_expression is not None:
            input_["condition_expression"] = condition_expression
        if expression_attribute_names is not None:
            input_["expression_attribute_names"] = expression_attribute_names
        if expression_attribute_values is not None:
            input_["expression_attribute_values"] = expression_attribute_values
        if return_values_on_condition_check_failure is not None:
            input_["return_values_on_condition_check_failure"] = (
                return_values_on_condition_check_failure
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_kinesis_streaming_destination(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        stream_arn: "capo_dynamodb.types.stream_arn.StreamArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        update_kinesis_streaming_configuration: Optional[
            "capo_dynamodb.types.update_kinesis_streaming_configuration.UpdateKinesisStreamingConfiguration"
        ] = None,
    ) -> "capo_dynamodb.types.update_kinesis_streaming_destination_output.UpdateKinesisStreamingDestinationOutput":
        """<p>The command to update the Kinesis stream destination.</p>

        Args:
            table_name: <p>The table name for the Kinesis streaming destination input. You can also provide the ARN of the table in this parameter.</p>
            stream_arn: <p>The Amazon Resource Name (ARN) for the Kinesis stream input.</p>
            update_kinesis_streaming_configuration: <p>The command to update the Kinesis stream configuration.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.update_kinesis_streaming_destination_input.UpdateKinesisStreamingDestinationInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.update_kinesis_streaming_destination_output.UpdateKinesisStreamingDestinationOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.update_kinesis_streaming_destination

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.update_kinesis_streaming_destination.update_kinesis_streaming_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.update_kinesis_streaming_destination_input.UpdateKinesisStreamingDestinationInput = {
            "table_name": table_name,
            "stream_arn": stream_arn,
        }
        if update_kinesis_streaming_configuration is not None:
            input_["update_kinesis_streaming_configuration"] = (
                update_kinesis_streaming_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_table(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        attribute_definitions: Optional[
            "capo_dynamodb.types.attribute_definitions.AttributeDefinitions"
        ] = None,
        billing_mode: Optional["capo_dynamodb.types.billing_mode.BillingMode"] = None,
        provisioned_throughput: Optional[
            "capo_dynamodb.types.provisioned_throughput.ProvisionedThroughput"
        ] = None,
        global_secondary_index_updates: Optional[
            "capo_dynamodb.types.global_secondary_index_update_list.GlobalSecondaryIndexUpdateList"
        ] = None,
        stream_specification: Optional[
            "capo_dynamodb.types.stream_specification.StreamSpecification"
        ] = None,
        sse_specification: Optional[
            "capo_dynamodb.types.sse_specification.SSESpecification"
        ] = None,
        replica_updates: Optional[
            "capo_dynamodb.types.replication_group_update_list.ReplicationGroupUpdateList"
        ] = None,
        table_class: Optional["capo_dynamodb.types.table_class.TableClass"] = None,
        deletion_protection_enabled: Optional[
            "capo_dynamodb.types.deletion_protection_enabled.DeletionProtectionEnabled"
        ] = None,
        multi_region_consistency: Optional[
            "capo_dynamodb.types.multi_region_consistency.MultiRegionConsistency"
        ] = None,
        global_table_witness_updates: Optional[
            "capo_dynamodb.types.global_table_witness_group_update_list.GlobalTableWitnessGroupUpdateList"
        ] = None,
        on_demand_throughput: Optional[
            "capo_dynamodb.types.on_demand_throughput.OnDemandThroughput"
        ] = None,
        warm_throughput: Optional[
            "capo_dynamodb.types.warm_throughput.WarmThroughput"
        ] = None,
        global_table_settings_replication_mode: Optional[
            "capo_dynamodb.types.global_table_settings_replication_mode.GlobalTableSettingsReplicationMode"
        ] = None,
        vector_index_updates: Optional[
            "capo_dynamodb.types.vector_index_update_list.VectorIndexUpdateList"
        ] = None,
    ) -> "capo_dynamodb.types.update_table_output.UpdateTableOutput":
        """<p>Modifies the provisioned throughput settings, global secondary indexes, or DynamoDB Streams settings for a given table.</p> <p>You can only perform one of the following operations at once:</p> <ul> <li> <p>Modify the provisioned throughput settings of the table.</p> </li> <li> <p>Remove a global secondary index from the table.</p> </li> <li> <p>Create a new global secondary index on the table. After the index begins backfilling, you can use <code>UpdateTable</code> to perform other operations.</p> </li> </ul> <p> <code>UpdateTable</code> is an asynchronous operation; while it's executing, the table status changes from <code>ACTIVE</code> to <code>UPDATING</code>. While it's <code>UPDATING</code>, you can't issue another <code>UpdateTable</code> request. When the table returns to the <code>ACTIVE</code> state, the <code>UpdateTable</code> operation is complete.</p>

        Args:
            attribute_definitions: <p>An array of attributes that describe the key schema for the table and indexes. If you are adding a new global secondary index to the table, <code>AttributeDefinitions</code> must include the key element(s) of the new index.</p>
            table_name: <p>The name of the table to be updated. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            billing_mode: <p>Controls how you are charged for read and write throughput and how you manage capacity. When switching from pay-per-request to provisioned capacity, initial provisioned capacity values must be set. The initial provisioned capacity values are estimated based on the consumed read and write capacity of your table and global secondary indexes over the past 30 minutes.</p> <ul> <li> <p> <code>PAY_PER_REQUEST</code> - We recommend using <code>PAY_PER_REQUEST</code> for most DynamoDB workloads. <code>PAY_PER_REQUEST</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html">On-demand capacity mode</a>. </p> </li> <li> <p> <code>PROVISIONED</code> - We recommend using <code>PROVISIONED</code> for steady workloads with predictable growth where capacity requirements can be reliably forecasted. <code>PROVISIONED</code> sets the billing mode to <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html">Provisioned capacity mode</a>.</p> </li> </ul>
            provisioned_throughput: <p>The new provisioned throughput settings for the specified table or index.</p>
            global_secondary_index_updates: <p>An array of one or more global secondary indexes for the table. For each index in the array, you can request one action:</p> <ul> <li> <p> <code>Create</code> - add a new global secondary index to the table.</p> </li> <li> <p> <code>Update</code> - modify the provisioned throughput settings of an existing global secondary index.</p> </li> <li> <p> <code>Delete</code> - remove a global secondary index from the table.</p> </li> </ul> <p>You can create or delete only one global secondary index per <code>UpdateTable</code> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.OnlineOps.html">Managing Global Secondary Indexes</a> in the <i>Amazon DynamoDB Developer Guide</i>. </p>
            stream_specification: <p>Represents the DynamoDB Streams configuration for the table.</p> <note> <p>You receive a <code>ValidationException</code> if you try to enable a stream on a table that already has a stream, or if you try to disable a stream on a table that doesn't have a stream.</p> </note>
            sse_specification: <p>The new server-side encryption settings for the specified table.</p>
            replica_updates: <p>A list of replica update actions (create, delete, or update) for the table.</p>
            table_class: <p>The table class of the table to be updated. Valid values are <code>STANDARD</code> and <code>STANDARD_INFREQUENT_ACCESS</code>.</p>
            deletion_protection_enabled: <p>Indicates whether deletion protection is to be enabled (true) or disabled (false) on the table.</p>
            multi_region_consistency: <p>Specifies the consistency mode for a new global table. This parameter is only valid when you create a global table by specifying one or more <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ReplicationGroupUpdate.html#DDB-Type-ReplicationGroupUpdate-Create">Create</a> actions in the <a href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html#DDB-UpdateTable-request-ReplicaUpdates">ReplicaUpdates</a> action list.</p> <p>You can specify one of the following consistency modes:</p> <ul> <li> <p> <code>EVENTUAL</code>: Configures a new global table for multi-Region eventual consistency (MREC). This is the default consistency mode for global tables.</p> </li> <li> <p> <code>STRONG</code>: Configures a new global table for multi-Region strong consistency (MRSC).</p> </li> </ul> <p>If you don't specify this field, the global table consistency mode defaults to <code>EVENTUAL</code>. For more information about global tables consistency modes, see <a href="https://docs.aws.amazon.com/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes"> Consistency modes</a> in DynamoDB developer guide. </p>
            global_table_witness_updates: <p>A list of witness updates for a MRSC global table. A witness provides a cost-effective alternative to a full replica in a MRSC global table by maintaining replicated change data written to global table replicas. You cannot perform read or write operations on a witness. For each witness, you can request one action:</p> <ul> <li> <p> <code>Create</code> - add a new witness to the global table.</p> </li> <li> <p> <code>Delete</code> - remove a witness from the global table.</p> </li> </ul> <p>You can create or delete only one witness per <code>UpdateTable</code> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes">Multi-Region strong consistency (MRSC)</a> in the Amazon DynamoDB Developer Guide</p>
            on_demand_throughput: <p>Updates the maximum number of read and write units for the specified table in on-demand capacity mode. If you use this parameter, you must specify <code>MaxReadRequestUnits</code>, <code>MaxWriteRequestUnits</code>, or both.</p>
            warm_throughput: <p>Represents the warm throughput (in read units per second and write units per second) for updating a table.</p>
            global_table_settings_replication_mode: <p>Controls the settings replication mode for a global table replica. This attribute can be defined using UpdateTable operation only on a regional table with values:</p> <ul> <li> <p> <code>ENABLED</code>: Defines settings replication on a regional table to be used as a source table for creating Multi-Account Global Table.</p> </li> <li> <p> <code>DISABLED</code>: Remove settings replication on a regional table. Settings replication needs to be defined to ENABLED again in order to create a Multi-Account Global Table using this table. </p> </li> </ul>
            vector_index_updates: <p>A list of vector indexes to be added to or removed from the table. You can add or remove one vector index for each <code>UpdateTable</code> operation.</p> <p>To add a vector index, specify <code>IndexName</code>, <code>VectorAttribute</code>, <code>Dimensions</code>, <code>DistanceFunction</code>, and <code>Projection</code>. To remove a vector index, specify only the <code>IndexName</code>.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.update_table_input.UpdateTableInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.update_table_output.UpdateTableOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.update_table

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.update_table.update_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.update_table_input.UpdateTableInput = {
            "table_name": table_name
        }
        if attribute_definitions is not None:
            input_["attribute_definitions"] = attribute_definitions
        if billing_mode is not None:
            input_["billing_mode"] = billing_mode
        if provisioned_throughput is not None:
            input_["provisioned_throughput"] = provisioned_throughput
        if global_secondary_index_updates is not None:
            input_["global_secondary_index_updates"] = global_secondary_index_updates
        if stream_specification is not None:
            input_["stream_specification"] = stream_specification
        if sse_specification is not None:
            input_["sse_specification"] = sse_specification
        if replica_updates is not None:
            input_["replica_updates"] = replica_updates
        if table_class is not None:
            input_["table_class"] = table_class
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled
        if multi_region_consistency is not None:
            input_["multi_region_consistency"] = multi_region_consistency
        if global_table_witness_updates is not None:
            input_["global_table_witness_updates"] = global_table_witness_updates
        if on_demand_throughput is not None:
            input_["on_demand_throughput"] = on_demand_throughput
        if warm_throughput is not None:
            input_["warm_throughput"] = warm_throughput
        if global_table_settings_replication_mode is not None:
            input_["global_table_settings_replication_mode"] = (
                global_table_settings_replication_mode
            )
        if vector_index_updates is not None:
            input_["vector_index_updates"] = vector_index_updates

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_table_replica_auto_scaling(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
        global_secondary_index_updates: Optional[
            "capo_dynamodb.types.global_secondary_index_auto_scaling_update_list.GlobalSecondaryIndexAutoScalingUpdateList"
        ] = None,
        provisioned_write_capacity_auto_scaling_update: Optional[
            "capo_dynamodb.types.auto_scaling_settings_update.AutoScalingSettingsUpdate"
        ] = None,
        replica_updates: Optional[
            "capo_dynamodb.types.replica_auto_scaling_update_list.ReplicaAutoScalingUpdateList"
        ] = None,
    ) -> "capo_dynamodb.types.update_table_replica_auto_scaling_output.UpdateTableReplicaAutoScalingOutput":
        """<p>Updates auto scaling settings on your global tables at once.</p>

        Args:
            global_secondary_index_updates: <p>Represents the auto scaling settings of the global secondary indexes of the replica to be updated.</p>
            table_name: <p>The name of the global table to be updated. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            replica_updates: <p>Represents the auto scaling settings of replicas of the table that will be modified.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.update_table_replica_auto_scaling_input.UpdateTableReplicaAutoScalingInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.update_table_replica_auto_scaling_output.UpdateTableReplicaAutoScalingOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.update_table_replica_auto_scaling

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.update_table_replica_auto_scaling.update_table_replica_auto_scaling(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.update_table_replica_auto_scaling_input.UpdateTableReplicaAutoScalingInput = {
            "table_name": table_name
        }
        if global_secondary_index_updates is not None:
            input_["global_secondary_index_updates"] = global_secondary_index_updates
        if provisioned_write_capacity_auto_scaling_update is not None:
            input_["provisioned_write_capacity_auto_scaling_update"] = (
                provisioned_write_capacity_auto_scaling_update
            )
        if replica_updates is not None:
            input_["replica_updates"] = replica_updates

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_time_to_live(
        self,
        table_name: "capo_dynamodb.types.table_arn.TableArn",
        time_to_live_specification: "capo_dynamodb.types.time_to_live_specification.TimeToLiveSpecification",
        *,
        config_overrides: Optional[DynamoDBClientConfig] = None,
    ) -> "capo_dynamodb.types.update_time_to_live_output.UpdateTimeToLiveOutput":
        """<p>The <code>UpdateTimeToLive</code> method enables or disables Time to Live (TTL) for the specified table. A successful <code>UpdateTimeToLive</code> call returns the current <code>TimeToLiveSpecification</code>. It can take up to one hour for the change to fully process. Any additional <code>UpdateTimeToLive</code> calls for the same table during this one hour duration result in a <code>ValidationException</code>. </p> <p>TTL compares the current time in epoch time format to the time stored in the TTL attribute of an item. If the epoch time value stored in the attribute is less than the current time, the item is marked as expired and subsequently deleted.</p> <note> <p> The epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC. </p> </note> <p>DynamoDB deletes expired items on a best-effort basis to ensure availability of throughput for other data operations. </p> <important> <p>DynamoDB typically deletes expired items within two days of expiration. The exact duration within which an item gets deleted after expiration is specific to the nature of the workload. Items that have expired and not been deleted will still show up in reads, queries, and scans.</p> </important> <p>As items are deleted, they are removed from any local secondary index and global secondary index immediately in the same eventually consistent way as a standard delete operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html">Time To Live</a> in the Amazon DynamoDB Developer Guide. </p>

        Args:
            table_name: <p>The name of the table to be configured. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>
            time_to_live_specification: <p>Represents the settings used to enable or disable Time to Live for the specified table.</p>

        Raises:
            capo_dynamodb.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_dynamodb.errors.invalid_endpoint_exception.InvalidEndpointException
            capo_dynamodb.errors.limit_exceeded_exception.LimitExceededException: <p>There is no limit to the number of daily on-demand backups that can be taken. </p> <p>For most purposes, up to 500 simultaneous table operations are allowed per account. These operations include <code>CreateTable</code>, <code>UpdateTable</code>, <code>DeleteTable</code>,<code>UpdateTimeToLive</code>, <code>RestoreTableFromBackup</code>, and <code>RestoreTableToPointInTime</code>. </p> <p>When you are creating a table with one or more secondary indexes, you can have up to 250 such requests running at a time. However, if the table or index specifications are complex, then DynamoDB might temporarily reduce the number of concurrent operations.</p> <p>When importing into DynamoDB, up to 50 simultaneous import table operations are allowed per account.</p> <p>There is a soft account quota of 2,500 tables.</p> <p>GetRecords was called with a value of more than 1000 for the limit request parameter.</p> <p>More than 2 processes are reading from the same streams shard at the same time. Exceeding this limit may result in request throttling.</p>
            capo_dynamodb.errors.resource_in_use_exception.ResourceInUseException: <p>The operation conflicts with the resource's availability. For example:</p> <ul> <li> <p>You attempted to recreate an existing table.</p> </li> <li> <p>You tried to delete a table currently in the <code>CREATING</code> state.</p> </li> <li> <p>You tried to update a resource that was already being updated.</p> </li> </ul> <p>When appropriate, wait for the ongoing update to complete and attempt the request again.</p>
            capo_dynamodb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent table or index. The resource might not be specified correctly, or its status might not be <code>ACTIVE</code>.</p>
            capo_dynamodb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_dynamodb.types.update_time_to_live_input.UpdateTimeToLiveInput]",
        ) -> OperationResponse[
            "capo_dynamodb.types.update_time_to_live_output.UpdateTimeToLiveOutput"
        ]:
            import capo_dynamodb._operations.dynamo_db_20120810.update_time_to_live

            output, http_response = (
                capo_dynamodb._operations.dynamo_db_20120810.update_time_to_live.update_time_to_live(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_dynamodb.types.update_time_to_live_input.UpdateTimeToLiveInput = {
            "table_name": table_name,
            "time_to_live_specification": time_to_live_specification,
        }

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
