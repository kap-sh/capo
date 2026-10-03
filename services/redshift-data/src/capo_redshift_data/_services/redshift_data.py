"""Generated from Smithy shape ``com.amazonaws.redshiftdata#RedshiftData``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_redshift_data._auth._signers
import capo_redshift_data._auth._sigv4
from capo_redshift_data._auth._identity import Credentials
from capo_redshift_data._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_redshift_data._auth._zapros_handler import AuthMiddleware
from capo_redshift_data._pagination import resolve_path as _resolve_path
from capo_redshift_data._services._aws_config import aws_config
from capo_redshift_data._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_redshift_data.types.batch_execute_statement_input
    import capo_redshift_data.types.batch_execute_statement_output
    import capo_redshift_data.types.cancel_statement_request
    import capo_redshift_data.types.cancel_statement_response
    import capo_redshift_data.types.client_token
    import capo_redshift_data.types.cluster_identifier_string
    import capo_redshift_data.types.column_metadata
    import capo_redshift_data.types.describe_statement_request
    import capo_redshift_data.types.describe_statement_response
    import capo_redshift_data.types.describe_table_request
    import capo_redshift_data.types.describe_table_response
    import capo_redshift_data.types.execute_statement_input
    import capo_redshift_data.types.execute_statement_output
    import capo_redshift_data.types.execution_mode
    import capo_redshift_data.types.field_list
    import capo_redshift_data.types.get_statement_result_request
    import capo_redshift_data.types.get_statement_result_response
    import capo_redshift_data.types.get_statement_result_v2_request
    import capo_redshift_data.types.get_statement_result_v2_response
    import capo_redshift_data.types.list_databases_request
    import capo_redshift_data.types.list_databases_response
    import capo_redshift_data.types.list_schemas_request
    import capo_redshift_data.types.list_schemas_response
    import capo_redshift_data.types.list_sessions_request
    import capo_redshift_data.types.list_sessions_response
    import capo_redshift_data.types.list_statements_limit
    import capo_redshift_data.types.list_statements_request
    import capo_redshift_data.types.list_statements_response
    import capo_redshift_data.types.list_tables_request
    import capo_redshift_data.types.list_tables_response
    import capo_redshift_data.types.page_size
    import capo_redshift_data.types.query_records
    import capo_redshift_data.types.result_format_string
    import capo_redshift_data.types.secret_arn
    import capo_redshift_data.types.session_alive_seconds
    import capo_redshift_data.types.session_data
    import capo_redshift_data.types.session_status_string
    import capo_redshift_data.types.sql_list
    import capo_redshift_data.types.sql_parameters_list
    import capo_redshift_data.types.statement_data
    import capo_redshift_data.types.statement_name_string
    import capo_redshift_data.types.statement_string
    import capo_redshift_data.types.status_string
    import capo_redshift_data.types.string
    import capo_redshift_data.types.table_member
    import capo_redshift_data.types.uuid
    import capo_redshift_data.types.wait_time_seconds
    import capo_redshift_data.types.workgroup_name_string


class RedshiftDataClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class RedshiftDataClient:
    """A client for the ``RedshiftData`` service.

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
        self._config = RedshiftDataClientConfig(
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
        self, config_overrides: Optional[RedshiftDataClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: RedshiftDataClientConfig = config_overrides or {}
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

    def batch_execute_statement(
        self,
        sqls: "capo_redshift_data.types.sql_list.SqlList",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        secret_arn: Optional["capo_redshift_data.types.secret_arn.SecretArn"] = None,
        db_user: Optional["capo_redshift_data.types.string.String"] = None,
        database: Optional["capo_redshift_data.types.string.String"] = None,
        with_event: Optional[bool] = None,
        statement_name: Optional[
            "capo_redshift_data.types.statement_name_string.StatementNameString"
        ] = None,
        parameters: Optional[
            "capo_redshift_data.types.sql_parameters_list.SqlParametersList"
        ] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
        client_token: Optional[
            "capo_redshift_data.types.client_token.ClientToken"
        ] = None,
        result_format: Optional[
            "capo_redshift_data.types.result_format_string.ResultFormatString"
        ] = None,
        session_keep_alive_seconds: Optional[
            "capo_redshift_data.types.session_alive_seconds.SessionAliveSeconds"
        ] = None,
        session_id: Optional["capo_redshift_data.types.uuid.UUID"] = None,
        execution_mode: Optional[
            "capo_redshift_data.types.execution_mode.ExecutionMode"
        ] = None,
        wait_time_seconds: Optional[
            "capo_redshift_data.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "capo_redshift_data.types.batch_execute_statement_output.BatchExecuteStatementOutput":
        """<p>Runs one or more SQL statements, which can be data manipulation language (DML) or data definition language (DDL). Depending on the authorization method, use one of the following combinations of request parameters: </p> <ul> <li> <p>Secrets Manager - when connecting to a cluster, provide the <code>secret-arn</code> of a secret stored in Secrets Manager which has <code>username</code> and <code>password</code>. The specified secret contains credentials to connect to the <code>database</code> you specify. When you are connecting to a cluster, you also supply the database name, If you provide a cluster identifier (<code>dbClusterIdentifier</code>), it must match the cluster identifier stored in the secret. When you are connecting to a serverless workgroup, you also supply the database name.</p> </li> <li> <p>Temporary credentials - when connecting to your data warehouse, choose one of the following options:</p> <ul> <li> <p>When connecting to a serverless workgroup, specify the workgroup name and database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift-serverless:GetCredentials</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as an IAM identity, specify the cluster identifier and the database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift:GetClusterCredentialsWithIAM</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as a database user, specify the cluster identifier, the database name, and the database user name. Also, permission to call the <code>redshift:GetClusterCredentials</code> operation is required.</p> </li> </ul> </li> </ul> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            sqls: <p>One or more SQL statements to run. The SQL statements run serially in the order of the array. Subsequent SQL statements don't start until the previous statement in the array completes. By default, the SQL statements are run as a single transaction. If any SQL statement fails, all work is rolled back. To change this behavior, see the <code>ExecutionMode</code> parameter.</p>
            cluster_identifier: <p>The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either Secrets Manager or temporary credentials. </p>
            secret_arn: <p>The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using Secrets Manager. </p>
            db_user: <p>The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials. </p>
            database: <p>The name of the database. This parameter is required when authenticating using either Secrets Manager or temporary credentials. </p>
            with_event: <p>A value that indicates whether to send an event to the Amazon EventBridge event bus after the SQL statements run. </p>
            statement_name: <p>The name of the SQL statements. You can name the SQL statements when you create them to identify the query. </p>
            parameters: <p>The parameters for the SQL statements. The parameters are available to all SQL statements in the batch. Each statement can reference any subset of the provided parameters. Each provided parameter must be referenced by at least one SQL statement in the batch.</p>
            workgroup_name: <p>The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either Secrets Manager or temporary credentials.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            result_format: <p>The data format of the result of the SQL statement. If no format is specified, the default is JSON.</p>
            session_keep_alive_seconds: <p>The number of seconds to keep the session alive after the query finishes. The maximum time a session can keep alive is 24 hours. After 24 hours, the session is forced closed and the query is terminated.</p>
            session_id: <p>The session identifier of the query.</p>
            execution_mode: <p>Determines how the SQL statements in the batch are run. If set to <code>TRANSACTION</code> (the default), all SQL statements are run as a single transaction and they are committed or rolled back together. If set to <code>AUTO_COMMIT</code>, each SQL statement is committed individually, and a failure of one statement does not affect the others.</p>
            wait_time_seconds: <p>The number of seconds to wait for all SQL statements in the batch to complete execution before returning the response. If the SQL statements do not complete within the specified time, the response returns the current status. The maximum value is 30 seconds.</p>

        Raises:
            capo_redshift_data.errors.active_sessions_exceeded_exception.ActiveSessionsExceededException: <p>The Amazon Redshift Data API operation failed because the maximum number of active sessions exceeded.</p>
            capo_redshift_data.errors.active_statements_exceeded_exception.ActiveStatementsExceededException: <p>The number of active statements exceeds the limit.</p>
            capo_redshift_data.errors.batch_execute_statement_exception.BatchExecuteStatementException: <p>An SQL statement encountered an environmental error while running.</p>
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.batch_execute_statement_input.BatchExecuteStatementInput]",
        ) -> OperationResponse[
            "capo_redshift_data.types.batch_execute_statement_output.BatchExecuteStatementOutput"
        ]:
            import capo_redshift_data._operations.redshift_data.batch_execute_statement

            output, http_response = (
                capo_redshift_data._operations.redshift_data.batch_execute_statement.batch_execute_statement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.batch_execute_statement_input.BatchExecuteStatementInput = {
            "sqls": sqls
        }
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if secret_arn is not None:
            input_["secret_arn"] = secret_arn
        if db_user is not None:
            input_["db_user"] = db_user
        if database is not None:
            input_["database"] = database
        if with_event is not None:
            input_["with_event"] = with_event
        if statement_name is not None:
            input_["statement_name"] = statement_name
        if parameters is not None:
            input_["parameters"] = parameters
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if result_format is not None:
            input_["result_format"] = result_format
        if session_keep_alive_seconds is not None:
            input_["session_keep_alive_seconds"] = session_keep_alive_seconds
        if session_id is not None:
            input_["session_id"] = session_id
        if execution_mode is not None:
            input_["execution_mode"] = execution_mode
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_statement(
        self,
        id: "capo_redshift_data.types.uuid.UUID",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
    ) -> "capo_redshift_data.types.cancel_statement_response.CancelStatementResponse":
        """<p>Cancels a running query. To be canceled, a query must be running. </p> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            id: <p>The identifier of the SQL statement to cancel. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API. This identifier is returned by <code>BatchExecuteStatment</code>, <code>ExecuteStatment</code>, and <code>ListStatements</code>. </p>

        Raises:
            capo_redshift_data.errors.database_connection_exception.DatabaseConnectionException: <p>Connection to a database failed.</p>
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.query_timeout_exception.QueryTimeoutException: <p>The Amazon Redshift Data API operation failed due to timeout.</p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.cancel_statement_request.CancelStatementRequest]",
        ) -> OperationResponse[
            "capo_redshift_data.types.cancel_statement_response.CancelStatementResponse"
        ]:
            import capo_redshift_data._operations.redshift_data.cancel_statement

            output, http_response = (
                capo_redshift_data._operations.redshift_data.cancel_statement.cancel_statement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.cancel_statement_request.CancelStatementRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_statement(
        self,
        id: "capo_redshift_data.types.uuid.UUID",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        wait_time_seconds: Optional[
            "capo_redshift_data.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> (
        "capo_redshift_data.types.describe_statement_response.DescribeStatementResponse"
    ):
        """<p>Describes the details about a specific instance when a query was run by the Amazon Redshift Data API. The information includes when the query started, when it finished, the query status, the number of rows returned, and the SQL statement. </p> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            id: <p>The identifier of the SQL statement to describe. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API. A suffix indicates the number of the SQL statement. For example, <code>d9b6c0c9-0747-4bf4-b142-e8883122f766:2</code> has a suffix of <code>:2</code> that indicates the second SQL statement of a batch query. This identifier is returned by <code>BatchExecuteStatment</code>, <code>ExecuteStatement</code>, and <code>ListStatements</code>. </p>
            wait_time_seconds: <p>The number of seconds to wait for the SQL statement to complete execution before returning the description. The maximum value is 30 seconds.</p>

        Raises:
            capo_redshift_data.errors.active_waiting_requests_exceeded_exception.ActiveWaitingRequestsExceededException: <p>The number of active requests with <code>WaitTimeSeconds</code> for the same SQL statement exceeds the limit.</p>
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.describe_statement_request.DescribeStatementRequest]",
        ) -> OperationResponse[
            "capo_redshift_data.types.describe_statement_response.DescribeStatementResponse"
        ]:
            import capo_redshift_data._operations.redshift_data.describe_statement

            output, http_response = (
                capo_redshift_data._operations.redshift_data.describe_statement.describe_statement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.describe_statement_request.DescribeStatementRequest = {
            "id": id
        }
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_table(
        self,
        database: "capo_redshift_data.types.string.String",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        secret_arn: Optional["capo_redshift_data.types.secret_arn.SecretArn"] = None,
        db_user: Optional["capo_redshift_data.types.string.String"] = None,
        connected_database: Optional["capo_redshift_data.types.string.String"] = None,
        schema: Optional["capo_redshift_data.types.string.String"] = None,
        table: Optional["capo_redshift_data.types.string.String"] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional["capo_redshift_data.types.page_size.PageSize"] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
    ) -> "capo_redshift_data.types.describe_table_response.DescribeTableResponse":
        """<p>Describes the detailed information about a table from metadata in the cluster. The information includes its columns. A token is returned to page through the column list. Depending on the authorization method, use one of the following combinations of request parameters: </p> <ul> <li> <p>Secrets Manager - when connecting to a cluster, provide the <code>secret-arn</code> of a secret stored in Secrets Manager which has <code>username</code> and <code>password</code>. The specified secret contains credentials to connect to the <code>database</code> you specify. When you are connecting to a cluster, you also supply the database name, If you provide a cluster identifier (<code>dbClusterIdentifier</code>), it must match the cluster identifier stored in the secret. When you are connecting to a serverless workgroup, you also supply the database name.</p> </li> <li> <p>Temporary credentials - when connecting to your data warehouse, choose one of the following options:</p> <ul> <li> <p>When connecting to a serverless workgroup, specify the workgroup name and database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift-serverless:GetCredentials</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as an IAM identity, specify the cluster identifier and the database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift:GetClusterCredentialsWithIAM</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as a database user, specify the cluster identifier, the database name, and the database user name. Also, permission to call the <code>redshift:GetClusterCredentials</code> operation is required.</p> </li> </ul> </li> </ul> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            cluster_identifier: <p>The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either Secrets Manager or temporary credentials. </p>
            secret_arn: <p>The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using Secrets Manager. </p>
            db_user: <p>The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials. </p>
            database: <p>The name of the database that contains the tables to be described. If <code>ConnectedDatabase</code> is not specified, this is also the database to connect to with your authentication credentials.</p>
            connected_database: <p>A database name. The connected database is specified when you connect with your authentication credentials. </p>
            schema: <p>The schema that contains the table. If no schema is specified, then matching tables for all schemas are returned. </p>
            table: <p>The table name. If no table is specified, then all tables for all matching schemas are returned. If no table and no schema is specified, then all tables for all schemas in the database are returned</p>
            next_token: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>
            max_results: <p>The maximum number of tables to return in the response. If more tables exist than fit in one response, then <code>NextToken</code> is returned to page through the results. </p>
            workgroup_name: <p>The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either Secrets Manager or temporary credentials.</p>

        Raises:
            capo_redshift_data.errors.database_connection_exception.DatabaseConnectionException: <p>Connection to a database failed.</p>
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.query_timeout_exception.QueryTimeoutException: <p>The Amazon Redshift Data API operation failed due to timeout.</p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.describe_table_request.DescribeTableRequest]",
        ) -> OperationResponse[
            "capo_redshift_data.types.describe_table_response.DescribeTableResponse"
        ]:
            import capo_redshift_data._operations.redshift_data.describe_table

            output, http_response = (
                capo_redshift_data._operations.redshift_data.describe_table.describe_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.describe_table_request.DescribeTableRequest = {
            "database": database
        }
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if secret_arn is not None:
            input_["secret_arn"] = secret_arn
        if db_user is not None:
            input_["db_user"] = db_user
        if connected_database is not None:
            input_["connected_database"] = connected_database
        if schema is not None:
            input_["schema"] = schema
        if table is not None:
            input_["table"] = table
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_table(
        self,
        database: "capo_redshift_data.types.string.String",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        secret_arn: Optional["capo_redshift_data.types.secret_arn.SecretArn"] = None,
        db_user: Optional["capo_redshift_data.types.string.String"] = None,
        connected_database: Optional["capo_redshift_data.types.string.String"] = None,
        schema: Optional["capo_redshift_data.types.string.String"] = None,
        table: Optional["capo_redshift_data.types.string.String"] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional["capo_redshift_data.types.page_size.PageSize"] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
    ) -> "Iterator[capo_redshift_data.types.column_metadata.ColumnMetadata]":
        _token = next_token
        while True:
            _response = self.describe_table(
                database,
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                secret_arn=secret_arn,
                db_user=db_user,
                connected_database=connected_database,
                schema=schema,
                table=table,
                next_token=_token,
                max_results=max_results,
                workgroup_name=workgroup_name,
            )
            _page = _resolve_path(_response, ("column_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def execute_statement(
        self,
        sql: "capo_redshift_data.types.statement_string.StatementString",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        secret_arn: Optional["capo_redshift_data.types.secret_arn.SecretArn"] = None,
        db_user: Optional["capo_redshift_data.types.string.String"] = None,
        database: Optional["capo_redshift_data.types.string.String"] = None,
        with_event: Optional[bool] = None,
        statement_name: Optional[
            "capo_redshift_data.types.statement_name_string.StatementNameString"
        ] = None,
        parameters: Optional[
            "capo_redshift_data.types.sql_parameters_list.SqlParametersList"
        ] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
        client_token: Optional[
            "capo_redshift_data.types.client_token.ClientToken"
        ] = None,
        result_format: Optional[
            "capo_redshift_data.types.result_format_string.ResultFormatString"
        ] = None,
        session_keep_alive_seconds: Optional[
            "capo_redshift_data.types.session_alive_seconds.SessionAliveSeconds"
        ] = None,
        session_id: Optional["capo_redshift_data.types.uuid.UUID"] = None,
        wait_time_seconds: Optional[
            "capo_redshift_data.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "capo_redshift_data.types.execute_statement_output.ExecuteStatementOutput":
        """<p>Runs an SQL statement, which can be data manipulation language (DML) or data definition language (DDL). This statement must be a single SQL statement. Depending on the authorization method, use one of the following combinations of request parameters: </p> <ul> <li> <p>Secrets Manager - when connecting to a cluster, provide the <code>secret-arn</code> of a secret stored in Secrets Manager which has <code>username</code> and <code>password</code>. The specified secret contains credentials to connect to the <code>database</code> you specify. When you are connecting to a cluster, you also supply the database name, If you provide a cluster identifier (<code>dbClusterIdentifier</code>), it must match the cluster identifier stored in the secret. When you are connecting to a serverless workgroup, you also supply the database name.</p> </li> <li> <p>Temporary credentials - when connecting to your data warehouse, choose one of the following options:</p> <ul> <li> <p>When connecting to a serverless workgroup, specify the workgroup name and database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift-serverless:GetCredentials</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as an IAM identity, specify the cluster identifier and the database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift:GetClusterCredentialsWithIAM</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as a database user, specify the cluster identifier, the database name, and the database user name. Also, permission to call the <code>redshift:GetClusterCredentials</code> operation is required.</p> </li> </ul> </li> </ul> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            sql: <p>The SQL statement text to run. </p>
            cluster_identifier: <p>The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either Secrets Manager or temporary credentials. </p>
            secret_arn: <p>The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using Secrets Manager. </p>
            db_user: <p>The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials. </p>
            database: <p>The name of the database. This parameter is required when authenticating using either Secrets Manager or temporary credentials. </p>
            with_event: <p>A value that indicates whether to send an event to the Amazon EventBridge event bus after the SQL statement runs. </p>
            statement_name: <p>The name of the SQL statement. You can name the SQL statement when you create it to identify the query. </p>
            parameters: <p>The parameters for the SQL statement.</p>
            workgroup_name: <p>The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either Secrets Manager or temporary credentials.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            result_format: <p>The data format of the result of the SQL statement. If no format is specified, the default is JSON.</p>
            session_keep_alive_seconds: <p>The number of seconds to keep the session alive after the query finishes. The maximum time a session can keep alive is 24 hours. After 24 hours, the session is forced closed and the query is terminated.</p>
            session_id: <p>The session identifier of the query.</p>
            wait_time_seconds: <p>The number of seconds to wait for the SQL statement to complete execution before returning the response. If the SQL statement does not complete within the specified time, the response returns the current status. The maximum value is 30 seconds.</p>

        Raises:
            capo_redshift_data.errors.active_sessions_exceeded_exception.ActiveSessionsExceededException: <p>The Amazon Redshift Data API operation failed because the maximum number of active sessions exceeded.</p>
            capo_redshift_data.errors.active_statements_exceeded_exception.ActiveStatementsExceededException: <p>The number of active statements exceeds the limit.</p>
            capo_redshift_data.errors.execute_statement_exception.ExecuteStatementException: <p>The SQL statement encountered an environmental error while running.</p>
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.execute_statement_input.ExecuteStatementInput]",
        ) -> OperationResponse[
            "capo_redshift_data.types.execute_statement_output.ExecuteStatementOutput"
        ]:
            import capo_redshift_data._operations.redshift_data.execute_statement

            output, http_response = (
                capo_redshift_data._operations.redshift_data.execute_statement.execute_statement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.execute_statement_input.ExecuteStatementInput = {
            "sql": sql
        }
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if secret_arn is not None:
            input_["secret_arn"] = secret_arn
        if db_user is not None:
            input_["db_user"] = db_user
        if database is not None:
            input_["database"] = database
        if with_event is not None:
            input_["with_event"] = with_event
        if statement_name is not None:
            input_["statement_name"] = statement_name
        if parameters is not None:
            input_["parameters"] = parameters
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if result_format is not None:
            input_["result_format"] = result_format
        if session_keep_alive_seconds is not None:
            input_["session_keep_alive_seconds"] = session_keep_alive_seconds
        if session_id is not None:
            input_["session_id"] = session_id
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_statement_result(
        self,
        id: "capo_redshift_data.types.uuid.UUID",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        wait_time_seconds: Optional[
            "capo_redshift_data.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "capo_redshift_data.types.get_statement_result_response.GetStatementResultResponse":
        """<p>Fetches the temporarily cached result of an SQL statement in JSON format. The <code>ExecuteStatement</code> or <code>BatchExecuteStatement</code> operation that ran the SQL statement must have specified <code>ResultFormat</code> as <code>JSON</code> , or let the format default to JSON. A token is returned to page through the statement results.</p> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            id: <p>The identifier of the SQL statement whose results are to be fetched. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API. A suffix indicates then number of the SQL statement. For example, <code>d9b6c0c9-0747-4bf4-b142-e8883122f766:2</code> has a suffix of <code>:2</code> that indicates the second SQL statement of a batch query. This identifier is returned by <code>BatchExecuteStatment</code>, <code>ExecuteStatment</code>, and <code>ListStatements</code>. </p>
            next_token: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>
            wait_time_seconds: <p>The number of seconds to wait for the SQL statement to complete execution before returning the result. The maximum value is 30 seconds.</p>

        Raises:
            capo_redshift_data.errors.active_waiting_requests_exceeded_exception.ActiveWaitingRequestsExceededException: <p>The number of active requests with <code>WaitTimeSeconds</code> for the same SQL statement exceeds the limit.</p>
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.get_statement_result_request.GetStatementResultRequest]",
        ) -> OperationResponse[
            "capo_redshift_data.types.get_statement_result_response.GetStatementResultResponse"
        ]:
            import capo_redshift_data._operations.redshift_data.get_statement_result

            output, http_response = (
                capo_redshift_data._operations.redshift_data.get_statement_result.get_statement_result(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.get_statement_result_request.GetStatementResultRequest = {
            "id": id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_statement_result(
        self,
        id: "capo_redshift_data.types.uuid.UUID",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        wait_time_seconds: Optional[
            "capo_redshift_data.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "Iterator[capo_redshift_data.types.field_list.FieldList]":
        _token = next_token
        while True:
            _response = self.get_statement_result(
                id,
                config_overrides=config_overrides,
                next_token=_token,
                wait_time_seconds=wait_time_seconds,
            )
            _page = _resolve_path(_response, ("records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_statement_result_v2(
        self,
        id: "capo_redshift_data.types.uuid.UUID",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        wait_time_seconds: Optional[
            "capo_redshift_data.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "capo_redshift_data.types.get_statement_result_v2_response.GetStatementResultV2Response":
        """<p>Fetches the temporarily cached result of an SQL statement in CSV format. The <code>ExecuteStatement</code> or <code>BatchExecuteStatement</code> operation that ran the SQL statement must have specified <code>ResultFormat</code> as <code>CSV</code>. A token is returned to page through the statement results.</p> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            id: <p>The identifier of the SQL statement whose results are to be fetched. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API. A suffix indicates then number of the SQL statement. For example, <code>d9b6c0c9-0747-4bf4-b142-e8883122f766:2</code> has a suffix of <code>:2</code> that indicates the second SQL statement of a batch query. This identifier is returned by <code>BatchExecuteStatment</code>, <code>ExecuteStatment</code>, and <code>ListStatements</code>. </p>
            next_token: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request.</p>
            wait_time_seconds: <p>The number of seconds to wait for the SQL statement to complete execution before returning the result. The maximum value is 30 seconds.</p>

        Raises:
            capo_redshift_data.errors.active_waiting_requests_exceeded_exception.ActiveWaitingRequestsExceededException: <p>The number of active requests with <code>WaitTimeSeconds</code> for the same SQL statement exceeds the limit.</p>
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.get_statement_result_v2_request.GetStatementResultV2Request]",
        ) -> OperationResponse[
            "capo_redshift_data.types.get_statement_result_v2_response.GetStatementResultV2Response"
        ]:
            import capo_redshift_data._operations.redshift_data.get_statement_result_v2

            output, http_response = (
                capo_redshift_data._operations.redshift_data.get_statement_result_v2.get_statement_result_v2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.get_statement_result_v2_request.GetStatementResultV2Request = {
            "id": id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_statement_result_v2(
        self,
        id: "capo_redshift_data.types.uuid.UUID",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        wait_time_seconds: Optional[
            "capo_redshift_data.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
    ) -> "Iterator[capo_redshift_data.types.query_records.QueryRecords]":
        _token = next_token
        while True:
            _response = self.get_statement_result_v2(
                id,
                config_overrides=config_overrides,
                next_token=_token,
                wait_time_seconds=wait_time_seconds,
            )
            _page = _resolve_path(_response, ("records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_databases(
        self,
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        database: Optional["capo_redshift_data.types.string.String"] = None,
        secret_arn: Optional["capo_redshift_data.types.secret_arn.SecretArn"] = None,
        db_user: Optional["capo_redshift_data.types.string.String"] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional["capo_redshift_data.types.page_size.PageSize"] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
    ) -> "capo_redshift_data.types.list_databases_response.ListDatabasesResponse":
        """<p>List the databases in a cluster. A token is returned to page through the database list. Depending on the authorization method, use one of the following combinations of request parameters: </p> <ul> <li> <p>Secrets Manager - when connecting to a cluster, provide the <code>secret-arn</code> of a secret stored in Secrets Manager which has <code>username</code> and <code>password</code>. The specified secret contains credentials to connect to the <code>database</code> you specify. When you are connecting to a cluster, you also supply the database name, If you provide a cluster identifier (<code>dbClusterIdentifier</code>), it must match the cluster identifier stored in the secret. When you are connecting to a serverless workgroup, you also supply the database name.</p> </li> <li> <p>Temporary credentials - when connecting to your data warehouse, choose one of the following options:</p> <ul> <li> <p>When connecting to a serverless workgroup, specify the workgroup name and database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift-serverless:GetCredentials</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as an IAM identity, specify the cluster identifier and the database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift:GetClusterCredentialsWithIAM</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as a database user, specify the cluster identifier, the database name, and the database user name. Also, permission to call the <code>redshift:GetClusterCredentials</code> operation is required.</p> </li> </ul> </li> </ul> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            cluster_identifier: <p>The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either Secrets Manager or temporary credentials. </p>
            database: <p>The name of the database. This parameter is required when authenticating using either Secrets Manager or temporary credentials. </p>
            secret_arn: <p>The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using Secrets Manager. </p>
            db_user: <p>The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials. </p>
            next_token: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>
            max_results: <p>The maximum number of databases to return in the response. If more databases exist than fit in one response, then <code>NextToken</code> is returned to page through the results. </p>
            workgroup_name: <p>The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either Secrets Manager or temporary credentials.</p>

        Raises:
            capo_redshift_data.errors.database_connection_exception.DatabaseConnectionException: <p>Connection to a database failed.</p>
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.query_timeout_exception.QueryTimeoutException: <p>The Amazon Redshift Data API operation failed due to timeout.</p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.list_databases_request.ListDatabasesRequest]",
        ) -> OperationResponse[
            "capo_redshift_data.types.list_databases_response.ListDatabasesResponse"
        ]:
            import capo_redshift_data._operations.redshift_data.list_databases

            output, http_response = (
                capo_redshift_data._operations.redshift_data.list_databases.list_databases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.list_databases_request.ListDatabasesRequest = {}
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if database is not None:
            input_["database"] = database
        if secret_arn is not None:
            input_["secret_arn"] = secret_arn
        if db_user is not None:
            input_["db_user"] = db_user
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_databases(
        self,
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        database: Optional["capo_redshift_data.types.string.String"] = None,
        secret_arn: Optional["capo_redshift_data.types.secret_arn.SecretArn"] = None,
        db_user: Optional["capo_redshift_data.types.string.String"] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional["capo_redshift_data.types.page_size.PageSize"] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
    ) -> "Iterator[capo_redshift_data.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_databases(
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                database=database,
                secret_arn=secret_arn,
                db_user=db_user,
                next_token=_token,
                max_results=max_results,
                workgroup_name=workgroup_name,
            )
            _page = _resolve_path(_response, ("databases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_schemas(
        self,
        database: "capo_redshift_data.types.string.String",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        secret_arn: Optional["capo_redshift_data.types.secret_arn.SecretArn"] = None,
        db_user: Optional["capo_redshift_data.types.string.String"] = None,
        connected_database: Optional["capo_redshift_data.types.string.String"] = None,
        schema_pattern: Optional["capo_redshift_data.types.string.String"] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional["capo_redshift_data.types.page_size.PageSize"] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
    ) -> "capo_redshift_data.types.list_schemas_response.ListSchemasResponse":
        """<p>Lists the schemas in a database. A token is returned to page through the schema list. Depending on the authorization method, use one of the following combinations of request parameters: </p> <ul> <li> <p>Secrets Manager - when connecting to a cluster, provide the <code>secret-arn</code> of a secret stored in Secrets Manager which has <code>username</code> and <code>password</code>. The specified secret contains credentials to connect to the <code>database</code> you specify. When you are connecting to a cluster, you also supply the database name, If you provide a cluster identifier (<code>dbClusterIdentifier</code>), it must match the cluster identifier stored in the secret. When you are connecting to a serverless workgroup, you also supply the database name.</p> </li> <li> <p>Temporary credentials - when connecting to your data warehouse, choose one of the following options:</p> <ul> <li> <p>When connecting to a serverless workgroup, specify the workgroup name and database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift-serverless:GetCredentials</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as an IAM identity, specify the cluster identifier and the database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift:GetClusterCredentialsWithIAM</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as a database user, specify the cluster identifier, the database name, and the database user name. Also, permission to call the <code>redshift:GetClusterCredentials</code> operation is required.</p> </li> </ul> </li> </ul> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            cluster_identifier: <p>The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either Secrets Manager or temporary credentials. </p>
            secret_arn: <p>The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using Secrets Manager. </p>
            db_user: <p>The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials. </p>
            database: <p>The name of the database that contains the schemas to list. If <code>ConnectedDatabase</code> is not specified, this is also the database to connect to with your authentication credentials.</p>
            connected_database: <p>A database name. The connected database is specified when you connect with your authentication credentials. </p>
            schema_pattern: <p>A pattern to filter results by schema name. Within a schema pattern, "%" means match any substring of 0 or more characters and "_" means match any one character. Only schema name entries matching the search pattern are returned. </p>
            next_token: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>
            max_results: <p>The maximum number of schemas to return in the response. If more schemas exist than fit in one response, then <code>NextToken</code> is returned to page through the results. </p>
            workgroup_name: <p>The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either Secrets Manager or temporary credentials.</p>

        Raises:
            capo_redshift_data.errors.database_connection_exception.DatabaseConnectionException: <p>Connection to a database failed.</p>
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.query_timeout_exception.QueryTimeoutException: <p>The Amazon Redshift Data API operation failed due to timeout.</p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.list_schemas_request.ListSchemasRequest]",
        ) -> OperationResponse[
            "capo_redshift_data.types.list_schemas_response.ListSchemasResponse"
        ]:
            import capo_redshift_data._operations.redshift_data.list_schemas

            output, http_response = (
                capo_redshift_data._operations.redshift_data.list_schemas.list_schemas(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.list_schemas_request.ListSchemasRequest = {
            "database": database
        }
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if secret_arn is not None:
            input_["secret_arn"] = secret_arn
        if db_user is not None:
            input_["db_user"] = db_user
        if connected_database is not None:
            input_["connected_database"] = connected_database
        if schema_pattern is not None:
            input_["schema_pattern"] = schema_pattern
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_schemas(
        self,
        database: "capo_redshift_data.types.string.String",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        secret_arn: Optional["capo_redshift_data.types.secret_arn.SecretArn"] = None,
        db_user: Optional["capo_redshift_data.types.string.String"] = None,
        connected_database: Optional["capo_redshift_data.types.string.String"] = None,
        schema_pattern: Optional["capo_redshift_data.types.string.String"] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional["capo_redshift_data.types.page_size.PageSize"] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
    ) -> "Iterator[capo_redshift_data.types.string.String]":
        _token = next_token
        while True:
            _response = self.list_schemas(
                database,
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                secret_arn=secret_arn,
                db_user=db_user,
                connected_database=connected_database,
                schema_pattern=schema_pattern,
                next_token=_token,
                max_results=max_results,
                workgroup_name=workgroup_name,
            )
            _page = _resolve_path(_response, ("schemas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sessions(
        self,
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional[
            "capo_redshift_data.types.list_statements_limit.ListStatementsLimit"
        ] = None,
        session_id: Optional["capo_redshift_data.types.uuid.UUID"] = None,
        status: Optional[
            "capo_redshift_data.types.session_status_string.SessionStatusString"
        ] = None,
        role_level: Optional[bool] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
        database: Optional["capo_redshift_data.types.string.String"] = None,
    ) -> "capo_redshift_data.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists the sessions that the caller created in the last 24 hours. By default, only sessions with a status of <code>AVAILABLE</code> or <code>BUSY</code> are returned. You can filter the results by session status, compute target (cluster or serverless workgroup), or database. To retrieve the metadata for a single session, provide the <code>SessionId</code> parameter. Use <code>NextToken</code> to page through the session list.</p> <p>Returns only the sessions that the caller created. When identity-enhanced role sessions are used, you must provide either the <code>ClusterIdentifier</code> or <code>WorkgroupName</code> parameter to ensure that the IAM Identity Center user can only access the Amazon Redshift IAM Identity Center applications they are assigned. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html"> Trusted identity propagation overview</a>.</p>

        Args:
            next_token: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request.</p>
            max_results: <p>The maximum number of sessions to return in the response. If more sessions exist than fit in one response, the operation returns <code>NextToken</code> to paginate the results.</p>
            session_id: <p>The identifier of a specific session to return metadata for. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API. When you provide <code>SessionId</code>, you can't specify <code>Status</code>, <code>ClusterIdentifier</code>, <code>WorkgroupName</code>, or <code>Database</code>.</p>
            status: <p>The status of the sessions to list. If no status is specified, sessions with a status of <code>AVAILABLE</code> or <code>BUSY</code> are returned. Status values are defined as follows:</p> <ul> <li> <p>AVAILABLE – The session is open and ready to run a SQL statement.</p> </li> <li> <p>BUSY – The session is currently running a SQL statement.</p> </li> <li> <p>CLOSED – The session is closed and can no longer run SQL statements.</p> </li> </ul>
            role_level: <p>Specifies whether to return all sessions created by the caller's IAM role, including sessions from previous IAM sessions. If false, only sessions created in the current IAM session are returned. The default is true.</p>
            cluster_identifier: <p>The cluster identifier. Only sessions on this cluster are returned. When providing <code>ClusterIdentifier</code>, then <code>WorkgroupName</code> can't be specified.</p>
            workgroup_name: <p>The serverless workgroup name or Amazon Resource Name (ARN). Only sessions on this workgroup are returned. When providing <code>WorkgroupName</code>, then <code>ClusterIdentifier</code> can't be specified.</p>
            database: <p>The name of the database. Only sessions connected to this database are returned.</p>

        Raises:
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "capo_redshift_data.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_redshift_data._operations.redshift_data.list_sessions

            output, http_response = (
                capo_redshift_data._operations.redshift_data.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.list_sessions_request.ListSessionsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if session_id is not None:
            input_["session_id"] = session_id
        if status is not None:
            input_["status"] = status
        if role_level is not None:
            input_["role_level"] = role_level
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name
        if database is not None:
            input_["database"] = database

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_sessions(
        self,
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional[
            "capo_redshift_data.types.list_statements_limit.ListStatementsLimit"
        ] = None,
        session_id: Optional["capo_redshift_data.types.uuid.UUID"] = None,
        status: Optional[
            "capo_redshift_data.types.session_status_string.SessionStatusString"
        ] = None,
        role_level: Optional[bool] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
        database: Optional["capo_redshift_data.types.string.String"] = None,
    ) -> "Iterator[capo_redshift_data.types.session_data.SessionData]":
        _token = next_token
        while True:
            _response = self.list_sessions(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                session_id=session_id,
                status=status,
                role_level=role_level,
                cluster_identifier=cluster_identifier,
                workgroup_name=workgroup_name,
                database=database,
            )
            _page = _resolve_path(_response, ("sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_statements(
        self,
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional[
            "capo_redshift_data.types.list_statements_limit.ListStatementsLimit"
        ] = None,
        statement_name: Optional[
            "capo_redshift_data.types.statement_name_string.StatementNameString"
        ] = None,
        status: Optional["capo_redshift_data.types.status_string.StatusString"] = None,
        role_level: Optional[bool] = None,
        database: Optional["capo_redshift_data.types.string.String"] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
    ) -> "capo_redshift_data.types.list_statements_response.ListStatementsResponse":
        """<p>List of SQL statements. By default, only finished statements are shown. A token is returned to page through the statement list. </p> <p>When you use identity-enhanced role sessions to list statements, you must provide either the <code>cluster-identifier</code> or <code>workgroup-name</code> parameter. This ensures that the IdC user can only access the Amazon Redshift IdC applications they are assigned. For more information, see <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html"> Trusted identity propagation overview</a>.</p> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            next_token: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>
            max_results: <p>The maximum number of SQL statements to return in the response. If more SQL statements exist than fit in one response, then <code>NextToken</code> is returned to page through the results. </p>
            statement_name: <p>The name of the SQL statement specified as input to <code>BatchExecuteStatement</code> or <code>ExecuteStatement</code> to identify the query. You can list multiple statements by providing a prefix that matches the beginning of the statement name. For example, to list myStatement1, myStatement2, myStatement3, and so on, then provide the a value of <code>myStatement</code>. Data API does a case-sensitive match of SQL statement names to the prefix value you provide. </p>
            status: <p>The status of the SQL statement to list. Status values are defined as follows: </p> <ul> <li> <p>ABORTED - The query run was stopped by the user. </p> </li> <li> <p>ALL - A status value that includes all query statuses. This value can be used to filter results. </p> </li> <li> <p>FAILED - The query run failed. </p> </li> <li> <p>FINISHED - The query has finished running. </p> </li> <li> <p>PICKED - The query has been chosen to be run. </p> </li> <li> <p>STARTED - The query run has started. </p> </li> <li> <p>SUBMITTED - The query was submitted, but not yet processed. </p> </li> </ul>
            role_level: <p>A value that filters which statements to return in the response. If true, all statements run by the caller's IAM role are returned. If false, only statements run by the caller's IAM role in the current IAM session are returned. The default is true. </p>
            database: <p>The name of the database when listing statements run against a <code>ClusterIdentifier</code> or <code>WorkgroupName</code>. </p>
            cluster_identifier: <p>The cluster identifier. Only statements that ran on this cluster are returned. When providing <code>ClusterIdentifier</code>, then <code>WorkgroupName</code> can't be specified.</p>
            workgroup_name: <p>The serverless workgroup name or Amazon Resource Name (ARN). Only statements that ran on this workgroup are returned. When providing <code>WorkgroupName</code>, then <code>ClusterIdentifier</code> can't be specified.</p>

        Raises:
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.list_statements_request.ListStatementsRequest]",
        ) -> OperationResponse[
            "capo_redshift_data.types.list_statements_response.ListStatementsResponse"
        ]:
            import capo_redshift_data._operations.redshift_data.list_statements

            output, http_response = (
                capo_redshift_data._operations.redshift_data.list_statements.list_statements(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.list_statements_request.ListStatementsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if statement_name is not None:
            input_["statement_name"] = statement_name
        if status is not None:
            input_["status"] = status
        if role_level is not None:
            input_["role_level"] = role_level
        if database is not None:
            input_["database"] = database
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_statements(
        self,
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional[
            "capo_redshift_data.types.list_statements_limit.ListStatementsLimit"
        ] = None,
        statement_name: Optional[
            "capo_redshift_data.types.statement_name_string.StatementNameString"
        ] = None,
        status: Optional["capo_redshift_data.types.status_string.StatusString"] = None,
        role_level: Optional[bool] = None,
        database: Optional["capo_redshift_data.types.string.String"] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
    ) -> "Iterator[capo_redshift_data.types.statement_data.StatementData]":
        _token = next_token
        while True:
            _response = self.list_statements(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                statement_name=statement_name,
                status=status,
                role_level=role_level,
                database=database,
                cluster_identifier=cluster_identifier,
                workgroup_name=workgroup_name,
            )
            _page = _resolve_path(_response, ("statements",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tables(
        self,
        database: "capo_redshift_data.types.string.String",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        secret_arn: Optional["capo_redshift_data.types.secret_arn.SecretArn"] = None,
        db_user: Optional["capo_redshift_data.types.string.String"] = None,
        connected_database: Optional["capo_redshift_data.types.string.String"] = None,
        schema_pattern: Optional["capo_redshift_data.types.string.String"] = None,
        table_pattern: Optional["capo_redshift_data.types.string.String"] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional["capo_redshift_data.types.page_size.PageSize"] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
    ) -> "capo_redshift_data.types.list_tables_response.ListTablesResponse":
        """<p>List the tables in a database. If neither <code>SchemaPattern</code> nor <code>TablePattern</code> are specified, then all tables in the database are returned. A token is returned to page through the table list. Depending on the authorization method, use one of the following combinations of request parameters: </p> <ul> <li> <p>Secrets Manager - when connecting to a cluster, provide the <code>secret-arn</code> of a secret stored in Secrets Manager which has <code>username</code> and <code>password</code>. The specified secret contains credentials to connect to the <code>database</code> you specify. When you are connecting to a cluster, you also supply the database name, If you provide a cluster identifier (<code>dbClusterIdentifier</code>), it must match the cluster identifier stored in the secret. When you are connecting to a serverless workgroup, you also supply the database name.</p> </li> <li> <p>Temporary credentials - when connecting to your data warehouse, choose one of the following options:</p> <ul> <li> <p>When connecting to a serverless workgroup, specify the workgroup name and database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift-serverless:GetCredentials</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as an IAM identity, specify the cluster identifier and the database name. The database user name is derived from the IAM identity. For example, <code>arn:iam::123456789012:user:foo</code> has the database user name <code>IAM:foo</code>. Also, permission to call the <code>redshift:GetClusterCredentialsWithIAM</code> operation is required.</p> </li> <li> <p>When connecting to a cluster as a database user, specify the cluster identifier, the database name, and the database user name. Also, permission to call the <code>redshift:GetClusterCredentials</code> operation is required.</p> </li> </ul> </li> </ul> <p>For more information about the Amazon Redshift Data API and CLI usage examples, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html">Using the Amazon Redshift Data API</a> in the <i>Amazon Redshift Management Guide</i>. </p>

        Args:
            cluster_identifier: <p>The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either Secrets Manager or temporary credentials. </p>
            secret_arn: <p>The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using Secrets Manager. </p>
            db_user: <p>The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials. </p>
            database: <p>The name of the database that contains the tables to list. If <code>ConnectedDatabase</code> is not specified, this is also the database to connect to with your authentication credentials.</p>
            connected_database: <p>A database name. The connected database is specified when you connect with your authentication credentials. </p>
            schema_pattern: <p>A pattern to filter results by schema name. Within a schema pattern, "%" means match any substring of 0 or more characters and "_" means match any one character. Only schema name entries matching the search pattern are returned. If <code>SchemaPattern</code> is not specified, then all tables that match <code>TablePattern</code> are returned. If neither <code>SchemaPattern</code> or <code>TablePattern</code> are specified, then all tables are returned. </p>
            table_pattern: <p>A pattern to filter results by table name. Within a table pattern, "%" means match any substring of 0 or more characters and "_" means match any one character. Only table name entries matching the search pattern are returned. If <code>TablePattern</code> is not specified, then all tables that match <code>SchemaPattern</code>are returned. If neither <code>SchemaPattern</code> or <code>TablePattern</code> are specified, then all tables are returned. </p>
            next_token: <p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>
            max_results: <p>The maximum number of tables to return in the response. If more tables exist than fit in one response, then <code>NextToken</code> is returned to page through the results. </p>
            workgroup_name: <p>The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either Secrets Manager or temporary credentials.</p>

        Raises:
            capo_redshift_data.errors.database_connection_exception.DatabaseConnectionException: <p>Connection to a database failed.</p>
            capo_redshift_data.errors.internal_server_exception.InternalServerException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.query_timeout_exception.QueryTimeoutException: <p>The Amazon Redshift Data API operation failed due to timeout.</p>
            capo_redshift_data.errors.resource_not_found_exception.ResourceNotFoundException: <p>The Amazon Redshift Data API operation failed due to a missing resource. </p>
            capo_redshift_data.errors.validation_exception.ValidationException: <p>The Amazon Redshift Data API operation failed due to invalid input. </p>
            capo_redshift_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_data.types.list_tables_request.ListTablesRequest]",
        ) -> OperationResponse[
            "capo_redshift_data.types.list_tables_response.ListTablesResponse"
        ]:
            import capo_redshift_data._operations.redshift_data.list_tables

            output, http_response = (
                capo_redshift_data._operations.redshift_data.list_tables.list_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_data.types.list_tables_request.ListTablesRequest = {
            "database": database
        }
        if cluster_identifier is not None:
            input_["cluster_identifier"] = cluster_identifier
        if secret_arn is not None:
            input_["secret_arn"] = secret_arn
        if db_user is not None:
            input_["db_user"] = db_user
        if connected_database is not None:
            input_["connected_database"] = connected_database
        if schema_pattern is not None:
            input_["schema_pattern"] = schema_pattern
        if table_pattern is not None:
            input_["table_pattern"] = table_pattern
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_tables(
        self,
        database: "capo_redshift_data.types.string.String",
        *,
        config_overrides: Optional[RedshiftDataClientConfig] = None,
        cluster_identifier: Optional[
            "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
        ] = None,
        secret_arn: Optional["capo_redshift_data.types.secret_arn.SecretArn"] = None,
        db_user: Optional["capo_redshift_data.types.string.String"] = None,
        connected_database: Optional["capo_redshift_data.types.string.String"] = None,
        schema_pattern: Optional["capo_redshift_data.types.string.String"] = None,
        table_pattern: Optional["capo_redshift_data.types.string.String"] = None,
        next_token: Optional["capo_redshift_data.types.string.String"] = None,
        max_results: Optional["capo_redshift_data.types.page_size.PageSize"] = None,
        workgroup_name: Optional[
            "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
        ] = None,
    ) -> "Iterator[capo_redshift_data.types.table_member.TableMember]":
        _token = next_token
        while True:
            _response = self.list_tables(
                database,
                config_overrides=config_overrides,
                cluster_identifier=cluster_identifier,
                secret_arn=secret_arn,
                db_user=db_user,
                connected_database=connected_database,
                schema_pattern=schema_pattern,
                table_pattern=table_pattern,
                next_token=_token,
                max_results=max_results,
                workgroup_name=workgroup_name,
            )
            _page = _resolve_path(_response, ("tables",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
