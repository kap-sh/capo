"""Generated from Smithy shape ``com.amazonaws.rdsdata#RdsDataService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_rds_data._auth._signers
import capo_rds_data._auth._sigv4
from capo_rds_data._auth._identity import Credentials
from capo_rds_data._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_rds_data._auth._zapros_handler import AuthMiddleware
from capo_rds_data._services._aws_config import aaws_config
from capo_rds_data._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_rds_data.types.arn
    import capo_rds_data.types.batch_execute_statement_request
    import capo_rds_data.types.batch_execute_statement_response
    import capo_rds_data.types.begin_transaction_request
    import capo_rds_data.types.begin_transaction_response
    import capo_rds_data.types.boolean
    import capo_rds_data.types.commit_transaction_request
    import capo_rds_data.types.commit_transaction_response
    import capo_rds_data.types.db_name
    import capo_rds_data.types.execute_sql_request
    import capo_rds_data.types.execute_sql_response
    import capo_rds_data.types.execute_statement_request
    import capo_rds_data.types.execute_statement_response
    import capo_rds_data.types.id
    import capo_rds_data.types.records_format_type
    import capo_rds_data.types.result_set_options
    import capo_rds_data.types.rollback_transaction_request
    import capo_rds_data.types.rollback_transaction_response
    import capo_rds_data.types.sql_parameter_sets
    import capo_rds_data.types.sql_parameters_list
    import capo_rds_data.types.sql_statement


class AsyncRDSDataClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncRDSDataClient:
    """A client for the ``RDSData`` service.

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
        self._config = AsyncRDSDataClientConfig(
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
        self, config_overrides: Optional[AsyncRDSDataClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRDSDataClientConfig = config_overrides or {}
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

    async def batch_execute_statement(
        self,
        resource_arn: "capo_rds_data.types.arn.Arn",
        secret_arn: "capo_rds_data.types.arn.Arn",
        sql: "capo_rds_data.types.sql_statement.SqlStatement",
        *,
        config_overrides: Optional[AsyncRDSDataClientConfig] = None,
        database: Optional["capo_rds_data.types.db_name.DbName"] = None,
        schema: Optional["capo_rds_data.types.db_name.DbName"] = None,
        parameter_sets: Optional[
            "capo_rds_data.types.sql_parameter_sets.SqlParameterSets"
        ] = None,
        transaction_id: Optional["capo_rds_data.types.id.Id"] = None,
    ) -> "capo_rds_data.types.batch_execute_statement_response.BatchExecuteStatementResponse":
        """<p>Runs a batch SQL statement over an array of data.</p> <p>You can run bulk update and insert operations for multiple records using a DML statement with different parameter sets. Bulk operations can provide a significant performance improvement over individual insert and update operations.</p> <note> <p>If a call isn't part of a transaction because it doesn't include the <code>transactionID</code> parameter, changes that result from the call are committed automatically.</p> <p>There isn't a fixed upper limit on the number of parameter sets. However, the maximum size of the HTTP request submitted through the Data API is 4 MiB. If the request exceeds this limit, the Data API returns an error and doesn't process the request. This 4-MiB limit includes the size of the HTTP headers and the JSON notation in the request. Thus, the number of parameter sets that you can include depends on a combination of factors, such as the size of the SQL statement and the size of each parameter set.</p> <p>The response size limit is 1 MiB. If the call returns more than 1 MiB of response data, the call is terminated.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>
            secret_arn: <p>The ARN of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.</p> <p>For information about creating the secret, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html">Create a database secret</a>.</p>
            sql: <p>The SQL statement to run. Don't include a semicolon (;) at the end of the SQL statement.</p>
            database: <p>The name of the database.</p>
            schema: <p>The name of the database schema.</p> <note> <p>Currently, the <code>schema</code> parameter isn't supported.</p> </note>
            parameter_sets: <p>The parameter set for the batch operation.</p> <p>The SQL statement is executed as many times as the number of parameter sets provided. To execute a SQL statement with no parameters, use one of the following options:</p> <ul> <li> <p>Specify one or more empty parameter sets.</p> </li> <li> <p>Use the <code>ExecuteStatement</code> operation instead of the <code>BatchExecuteStatement</code> operation.</p> </li> </ul> <note> <p>Array parameters are not supported.</p> </note>
            transaction_id: <p>The identifier of a transaction that was started by using the <code>BeginTransaction</code> operation. Specify the transaction ID of the transaction that you want to include the SQL statement in.</p> <p>If the SQL statement is not part of a transaction, don't set this parameter.</p>

        Raises:
            capo_rds_data.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_rds_data.errors.bad_request_exception.BadRequestException: <p>There is an error in the call or in a SQL statement. This exception is deprecated.</p>
            capo_rds_data.errors.database_error_exception.DatabaseErrorException: <p>There was an error in processing the SQL statement.</p>
            capo_rds_data.errors.database_not_found_exception.DatabaseNotFoundException: <p>The DB cluster doesn't have a DB instance.</p>
            capo_rds_data.errors.database_resuming_exception.DatabaseResumingException: <p>A request was cancelled because the Aurora Serverless DB instance was paused. The Data API request automatically resumes the DB instance. Wait a few seconds and try again.</p>
            capo_rds_data.errors.database_unavailable_exception.DatabaseUnavailableException: <p>The writer instance in the DB cluster isn't available.</p>
            capo_rds_data.errors.forbidden_exception.ForbiddenException: <p>There are insufficient privileges to make the call.</p>
            capo_rds_data.errors.http_endpoint_not_enabled_exception.HttpEndpointNotEnabledException: <p>The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.</p>
            capo_rds_data.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred.</p>
            capo_rds_data.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The resource is in an invalid state.</p>
            capo_rds_data.errors.invalid_secret_exception.InvalidSecretException: <p>The Secrets Manager secret used with the request isn't valid.</p>
            capo_rds_data.errors.secrets_error_exception.SecretsErrorException: <p>There was a problem with the Secrets Manager secret used with the request, caused by one of the following conditions:</p> <ul> <li> <p>RDS Data API timed out retrieving the secret.</p> </li> <li> <p>The secret provided wasn't found.</p> </li> <li> <p>The secret couldn't be decrypted.</p> </li> </ul>
            capo_rds_data.errors.service_unavailable_error.ServiceUnavailableError: <p>The service specified by the <code>resourceArn</code> parameter isn't available.</p>
            capo_rds_data.errors.statement_timeout_exception.StatementTimeoutException: <p>The execution of the SQL statement timed out.</p>
            capo_rds_data.errors.transaction_not_found_exception.TransactionNotFoundException: <p>The transaction ID wasn't found.</p>
            capo_rds_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rds_data.types.batch_execute_statement_request.BatchExecuteStatementRequest]",
        ) -> AsyncOperationResponse[
            "capo_rds_data.types.batch_execute_statement_response.BatchExecuteStatementResponse"
        ]:
            import capo_rds_data._operations.rds_data_service.batch_execute_statement

            (
                output,
                http_response,
            ) = await capo_rds_data._operations.rds_data_service.batch_execute_statement.async_batch_execute_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rds_data.types.batch_execute_statement_request.BatchExecuteStatementRequest = {
            "resource_arn": resource_arn,
            "secret_arn": secret_arn,
            "sql": sql,
        }
        if database is not None:
            input_["database"] = database
        if schema is not None:
            input_["schema"] = schema
        if parameter_sets is not None:
            input_["parameter_sets"] = parameter_sets
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def begin_transaction(
        self,
        resource_arn: "capo_rds_data.types.arn.Arn",
        secret_arn: "capo_rds_data.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncRDSDataClientConfig] = None,
        database: Optional["capo_rds_data.types.db_name.DbName"] = None,
        schema: Optional["capo_rds_data.types.db_name.DbName"] = None,
    ) -> "capo_rds_data.types.begin_transaction_response.BeginTransactionResponse":
        """<p>Starts a SQL transaction.</p> <note> <p>A transaction can run for a maximum of 24 hours. A transaction is terminated and rolled back automatically after 24 hours.</p> <p>A transaction times out if no calls use its transaction ID in three minutes. If a transaction times out before it's committed, it's rolled back automatically.</p> <p>For Aurora MySQL, DDL statements inside a transaction cause an implicit commit. We recommend that you run each MySQL DDL statement in a separate <code>ExecuteStatement</code> call with <code>continueAfterTimeout</code> enabled.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>
            secret_arn: <p>The name or ARN of the secret that enables access to the DB cluster.</p>
            database: <p>The name of the database.</p>
            schema: <p>The name of the database schema.</p>

        Raises:
            capo_rds_data.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_rds_data.errors.bad_request_exception.BadRequestException: <p>There is an error in the call or in a SQL statement. This exception is deprecated.</p>
            capo_rds_data.errors.database_error_exception.DatabaseErrorException: <p>There was an error in processing the SQL statement.</p>
            capo_rds_data.errors.database_not_found_exception.DatabaseNotFoundException: <p>The DB cluster doesn't have a DB instance.</p>
            capo_rds_data.errors.database_resuming_exception.DatabaseResumingException: <p>A request was cancelled because the Aurora Serverless DB instance was paused. The Data API request automatically resumes the DB instance. Wait a few seconds and try again.</p>
            capo_rds_data.errors.database_unavailable_exception.DatabaseUnavailableException: <p>The writer instance in the DB cluster isn't available.</p>
            capo_rds_data.errors.forbidden_exception.ForbiddenException: <p>There are insufficient privileges to make the call.</p>
            capo_rds_data.errors.http_endpoint_not_enabled_exception.HttpEndpointNotEnabledException: <p>The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.</p>
            capo_rds_data.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred.</p>
            capo_rds_data.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The resource is in an invalid state.</p>
            capo_rds_data.errors.invalid_secret_exception.InvalidSecretException: <p>The Secrets Manager secret used with the request isn't valid.</p>
            capo_rds_data.errors.secrets_error_exception.SecretsErrorException: <p>There was a problem with the Secrets Manager secret used with the request, caused by one of the following conditions:</p> <ul> <li> <p>RDS Data API timed out retrieving the secret.</p> </li> <li> <p>The secret provided wasn't found.</p> </li> <li> <p>The secret couldn't be decrypted.</p> </li> </ul>
            capo_rds_data.errors.service_unavailable_error.ServiceUnavailableError: <p>The service specified by the <code>resourceArn</code> parameter isn't available.</p>
            capo_rds_data.errors.statement_timeout_exception.StatementTimeoutException: <p>The execution of the SQL statement timed out.</p>
            capo_rds_data.errors.transaction_not_found_exception.TransactionNotFoundException: <p>The transaction ID wasn't found.</p>
            capo_rds_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rds_data.types.begin_transaction_request.BeginTransactionRequest]",
        ) -> AsyncOperationResponse[
            "capo_rds_data.types.begin_transaction_response.BeginTransactionResponse"
        ]:
            import capo_rds_data._operations.rds_data_service.begin_transaction

            (
                output,
                http_response,
            ) = await capo_rds_data._operations.rds_data_service.begin_transaction.async_begin_transaction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rds_data.types.begin_transaction_request.BeginTransactionRequest = {
            "resource_arn": resource_arn,
            "secret_arn": secret_arn,
        }
        if database is not None:
            input_["database"] = database
        if schema is not None:
            input_["schema"] = schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def commit_transaction(
        self,
        resource_arn: "capo_rds_data.types.arn.Arn",
        secret_arn: "capo_rds_data.types.arn.Arn",
        transaction_id: "capo_rds_data.types.id.Id",
        *,
        config_overrides: Optional[AsyncRDSDataClientConfig] = None,
    ) -> "capo_rds_data.types.commit_transaction_response.CommitTransactionResponse":
        """<p>Ends a SQL transaction started with the <code>BeginTransaction</code> operation and commits the changes.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>
            secret_arn: <p>The name or ARN of the secret that enables access to the DB cluster.</p>
            transaction_id: <p>The identifier of the transaction to end and commit.</p>

        Raises:
            capo_rds_data.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_rds_data.errors.bad_request_exception.BadRequestException: <p>There is an error in the call or in a SQL statement. This exception is deprecated.</p>
            capo_rds_data.errors.database_error_exception.DatabaseErrorException: <p>There was an error in processing the SQL statement.</p>
            capo_rds_data.errors.database_not_found_exception.DatabaseNotFoundException: <p>The DB cluster doesn't have a DB instance.</p>
            capo_rds_data.errors.database_unavailable_exception.DatabaseUnavailableException: <p>The writer instance in the DB cluster isn't available.</p>
            capo_rds_data.errors.forbidden_exception.ForbiddenException: <p>There are insufficient privileges to make the call.</p>
            capo_rds_data.errors.http_endpoint_not_enabled_exception.HttpEndpointNotEnabledException: <p>The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.</p>
            capo_rds_data.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred.</p>
            capo_rds_data.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The resource is in an invalid state.</p>
            capo_rds_data.errors.invalid_secret_exception.InvalidSecretException: <p>The Secrets Manager secret used with the request isn't valid.</p>
            capo_rds_data.errors.not_found_exception.NotFoundException: <p>The <code>resourceArn</code>, <code>secretArn</code>, or <code>transactionId</code> value can't be found.</p>
            capo_rds_data.errors.secrets_error_exception.SecretsErrorException: <p>There was a problem with the Secrets Manager secret used with the request, caused by one of the following conditions:</p> <ul> <li> <p>RDS Data API timed out retrieving the secret.</p> </li> <li> <p>The secret provided wasn't found.</p> </li> <li> <p>The secret couldn't be decrypted.</p> </li> </ul>
            capo_rds_data.errors.service_unavailable_error.ServiceUnavailableError: <p>The service specified by the <code>resourceArn</code> parameter isn't available.</p>
            capo_rds_data.errors.statement_timeout_exception.StatementTimeoutException: <p>The execution of the SQL statement timed out.</p>
            capo_rds_data.errors.transaction_not_found_exception.TransactionNotFoundException: <p>The transaction ID wasn't found.</p>
            capo_rds_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rds_data.types.commit_transaction_request.CommitTransactionRequest]",
        ) -> AsyncOperationResponse[
            "capo_rds_data.types.commit_transaction_response.CommitTransactionResponse"
        ]:
            import capo_rds_data._operations.rds_data_service.commit_transaction

            (
                output,
                http_response,
            ) = await capo_rds_data._operations.rds_data_service.commit_transaction.async_commit_transaction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rds_data.types.commit_transaction_request.CommitTransactionRequest = {
            "resource_arn": resource_arn,
            "secret_arn": secret_arn,
            "transaction_id": transaction_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_sql(
        self,
        db_cluster_or_instance_arn: "capo_rds_data.types.arn.Arn",
        aws_secret_store_arn: "capo_rds_data.types.arn.Arn",
        sql_statements: "capo_rds_data.types.sql_statement.SqlStatement",
        *,
        config_overrides: Optional[AsyncRDSDataClientConfig] = None,
        database: Optional["capo_rds_data.types.db_name.DbName"] = None,
        schema: Optional["capo_rds_data.types.db_name.DbName"] = None,
    ) -> "capo_rds_data.types.execute_sql_response.ExecuteSqlResponse":
        """<p>Runs one or more SQL statements.</p> <note> <p>This operation is deprecated. Please use the <code>BatchExecuteStatement</code> or <code>ExecuteStatement</code> operation.</p> </note>

        Args:
            db_cluster_or_instance_arn: <p>The ARN of the Aurora Serverless DB cluster.</p>
            aws_secret_store_arn: <p>The Amazon Resource Name (ARN) of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.</p> <p>For information about creating the secret, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html">Create a database secret</a>.</p>
            sql_statements: <p>One or more SQL statements to run on the DB cluster.</p> <p>You can separate SQL statements from each other with a semicolon (;). Any valid SQL statement is permitted, including data definition, data manipulation, and commit statements. </p>
            database: <p>The name of the database.</p>
            schema: <p>The name of the database schema.</p>

        Raises:
            capo_rds_data.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_rds_data.errors.bad_request_exception.BadRequestException: <p>There is an error in the call or in a SQL statement. This exception is deprecated.</p>
            capo_rds_data.errors.forbidden_exception.ForbiddenException: <p>There are insufficient privileges to make the call.</p>
            capo_rds_data.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred.</p>
            capo_rds_data.errors.service_unavailable_error.ServiceUnavailableError: <p>The service specified by the <code>resourceArn</code> parameter isn't available.</p>
            capo_rds_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rds_data.types.execute_sql_request.ExecuteSqlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rds_data.types.execute_sql_response.ExecuteSqlResponse"
        ]:
            import capo_rds_data._operations.rds_data_service.execute_sql

            (
                output,
                http_response,
            ) = await capo_rds_data._operations.rds_data_service.execute_sql.async_execute_sql(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rds_data.types.execute_sql_request.ExecuteSqlRequest = {
            "db_cluster_or_instance_arn": db_cluster_or_instance_arn,
            "aws_secret_store_arn": aws_secret_store_arn,
            "sql_statements": sql_statements,
        }
        if database is not None:
            input_["database"] = database
        if schema is not None:
            input_["schema"] = schema

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_statement(
        self,
        resource_arn: "capo_rds_data.types.arn.Arn",
        secret_arn: "capo_rds_data.types.arn.Arn",
        sql: "capo_rds_data.types.sql_statement.SqlStatement",
        *,
        config_overrides: Optional[AsyncRDSDataClientConfig] = None,
        database: Optional["capo_rds_data.types.db_name.DbName"] = None,
        schema: Optional["capo_rds_data.types.db_name.DbName"] = None,
        parameters: Optional[
            "capo_rds_data.types.sql_parameters_list.SqlParametersList"
        ] = None,
        transaction_id: Optional["capo_rds_data.types.id.Id"] = None,
        include_result_metadata: Optional["capo_rds_data.types.boolean.Boolean"] = None,
        continue_after_timeout: Optional["capo_rds_data.types.boolean.Boolean"] = None,
        result_set_options: Optional[
            "capo_rds_data.types.result_set_options.ResultSetOptions"
        ] = None,
        format_records_as: Optional[
            "capo_rds_data.types.records_format_type.RecordsFormatType"
        ] = None,
    ) -> "capo_rds_data.types.execute_statement_response.ExecuteStatementResponse":
        r"""<p>Runs a SQL statement against a database.</p> <note> <p>If a call isn't part of a transaction because it doesn't include the <code>transactionID</code> parameter, changes that result from the call are committed automatically.</p> <p>If the binary response data from the database is more than 1 MB, the call is terminated.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>
            secret_arn: <p>The ARN of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.</p> <p>For information about creating the secret, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html">Create a database secret</a>.</p> <note> <p>When you use the CLI on Linux to reference a secret created in the RDS console, the ARN might include special characters like <code>rds!cluster</code>. If you enclose the ARN in double quotes, the <code>!</code> character might trigger a shell expansion error, such as <code>-bash: !cluster: event not found</code>. To avoid this, escape the exclamation mark (\!) in the ARN or enclose the entire ARN in single quotes (') instead of double quotes.</p> <p>Alternatively, disable shell history expansion by running <code>set +H</code> before you execute the command.</p> </note>
            sql: <p>The SQL statement to run.</p>
            database: <p>The name of the database.</p>
            schema: <p>The name of the database schema.</p> <note> <p>Currently, the <code>schema</code> parameter isn't supported.</p> </note>
            parameters: <p>The parameters for the SQL statement.</p> <note> <p>Array parameters are not supported.</p> </note>
            transaction_id: <p>The identifier of a transaction that was started by using the <code>BeginTransaction</code> operation. Specify the transaction ID of the transaction that you want to include the SQL statement in.</p> <p>If the SQL statement is not part of a transaction, don't set this parameter.</p>
            include_result_metadata: <p>A value that indicates whether to include metadata in the results.</p>
            continue_after_timeout: <p>A value that indicates whether to continue running the statement after the call times out. By default, the statement stops running when the call times out.</p> <note> <p>For DDL statements, we recommend continuing to run the statement after the call times out. When a DDL statement terminates before it is finished running, it can result in errors and possibly corrupted data structures.</p> </note>
            result_set_options: <p>Options that control how the result set is returned.</p>
            format_records_as: <p>A value that indicates whether to format the result set as a single JSON string. This parameter only applies to <code>SELECT</code> statements and is ignored for other types of statements. Allowed values are <code>NONE</code> and <code>JSON</code>. The default value is <code>NONE</code>. The result is returned in the <code>formattedRecords</code> field.</p> <p>For usage information about the JSON format for result sets, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html">Using the Data API</a> in the <i>Amazon Aurora User Guide</i>.</p>

        Raises:
            capo_rds_data.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_rds_data.errors.bad_request_exception.BadRequestException: <p>There is an error in the call or in a SQL statement. This exception is deprecated.</p>
            capo_rds_data.errors.database_error_exception.DatabaseErrorException: <p>There was an error in processing the SQL statement.</p>
            capo_rds_data.errors.database_not_found_exception.DatabaseNotFoundException: <p>The DB cluster doesn't have a DB instance.</p>
            capo_rds_data.errors.database_resuming_exception.DatabaseResumingException: <p>A request was cancelled because the Aurora Serverless DB instance was paused. The Data API request automatically resumes the DB instance. Wait a few seconds and try again.</p>
            capo_rds_data.errors.database_unavailable_exception.DatabaseUnavailableException: <p>The writer instance in the DB cluster isn't available.</p>
            capo_rds_data.errors.forbidden_exception.ForbiddenException: <p>There are insufficient privileges to make the call.</p>
            capo_rds_data.errors.http_endpoint_not_enabled_exception.HttpEndpointNotEnabledException: <p>The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.</p>
            capo_rds_data.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred.</p>
            capo_rds_data.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The resource is in an invalid state.</p>
            capo_rds_data.errors.invalid_secret_exception.InvalidSecretException: <p>The Secrets Manager secret used with the request isn't valid.</p>
            capo_rds_data.errors.secrets_error_exception.SecretsErrorException: <p>There was a problem with the Secrets Manager secret used with the request, caused by one of the following conditions:</p> <ul> <li> <p>RDS Data API timed out retrieving the secret.</p> </li> <li> <p>The secret provided wasn't found.</p> </li> <li> <p>The secret couldn't be decrypted.</p> </li> </ul>
            capo_rds_data.errors.service_unavailable_error.ServiceUnavailableError: <p>The service specified by the <code>resourceArn</code> parameter isn't available.</p>
            capo_rds_data.errors.statement_timeout_exception.StatementTimeoutException: <p>The execution of the SQL statement timed out.</p>
            capo_rds_data.errors.transaction_not_found_exception.TransactionNotFoundException: <p>The transaction ID wasn't found.</p>
            capo_rds_data.errors.unsupported_result_exception.UnsupportedResultException: <p>There was a problem with the result because of one of the following conditions:</p> <ul> <li> <p>It contained an unsupported data type.</p> </li> <li> <p>It contained a multidimensional array.</p> </li> <li> <p>The size was too large.</p> </li> </ul>
            capo_rds_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rds_data.types.execute_statement_request.ExecuteStatementRequest]",
        ) -> AsyncOperationResponse[
            "capo_rds_data.types.execute_statement_response.ExecuteStatementResponse"
        ]:
            import capo_rds_data._operations.rds_data_service.execute_statement

            (
                output,
                http_response,
            ) = await capo_rds_data._operations.rds_data_service.execute_statement.async_execute_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rds_data.types.execute_statement_request.ExecuteStatementRequest = {
            "resource_arn": resource_arn,
            "secret_arn": secret_arn,
            "sql": sql,
        }
        if database is not None:
            input_["database"] = database
        if schema is not None:
            input_["schema"] = schema
        if parameters is not None:
            input_["parameters"] = parameters
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id
        if include_result_metadata is not None:
            input_["include_result_metadata"] = include_result_metadata
        if continue_after_timeout is not None:
            input_["continue_after_timeout"] = continue_after_timeout
        if result_set_options is not None:
            input_["result_set_options"] = result_set_options
        if format_records_as is not None:
            input_["format_records_as"] = format_records_as

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def rollback_transaction(
        self,
        resource_arn: "capo_rds_data.types.arn.Arn",
        secret_arn: "capo_rds_data.types.arn.Arn",
        transaction_id: "capo_rds_data.types.id.Id",
        *,
        config_overrides: Optional[AsyncRDSDataClientConfig] = None,
    ) -> (
        "capo_rds_data.types.rollback_transaction_response.RollbackTransactionResponse"
    ):
        """<p>Performs a rollback of a transaction. Rolling back a transaction cancels its changes.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>
            secret_arn: <p>The name or ARN of the secret that enables access to the DB cluster.</p>
            transaction_id: <p>The identifier of the transaction to roll back.</p>

        Raises:
            capo_rds_data.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_rds_data.errors.bad_request_exception.BadRequestException: <p>There is an error in the call or in a SQL statement. This exception is deprecated.</p>
            capo_rds_data.errors.database_error_exception.DatabaseErrorException: <p>There was an error in processing the SQL statement.</p>
            capo_rds_data.errors.database_not_found_exception.DatabaseNotFoundException: <p>The DB cluster doesn't have a DB instance.</p>
            capo_rds_data.errors.database_unavailable_exception.DatabaseUnavailableException: <p>The writer instance in the DB cluster isn't available.</p>
            capo_rds_data.errors.forbidden_exception.ForbiddenException: <p>There are insufficient privileges to make the call.</p>
            capo_rds_data.errors.http_endpoint_not_enabled_exception.HttpEndpointNotEnabledException: <p>The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.</p>
            capo_rds_data.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal error occurred.</p>
            capo_rds_data.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The resource is in an invalid state.</p>
            capo_rds_data.errors.invalid_secret_exception.InvalidSecretException: <p>The Secrets Manager secret used with the request isn't valid.</p>
            capo_rds_data.errors.not_found_exception.NotFoundException: <p>The <code>resourceArn</code>, <code>secretArn</code>, or <code>transactionId</code> value can't be found.</p>
            capo_rds_data.errors.secrets_error_exception.SecretsErrorException: <p>There was a problem with the Secrets Manager secret used with the request, caused by one of the following conditions:</p> <ul> <li> <p>RDS Data API timed out retrieving the secret.</p> </li> <li> <p>The secret provided wasn't found.</p> </li> <li> <p>The secret couldn't be decrypted.</p> </li> </ul>
            capo_rds_data.errors.service_unavailable_error.ServiceUnavailableError: <p>The service specified by the <code>resourceArn</code> parameter isn't available.</p>
            capo_rds_data.errors.statement_timeout_exception.StatementTimeoutException: <p>The execution of the SQL statement timed out.</p>
            capo_rds_data.errors.transaction_not_found_exception.TransactionNotFoundException: <p>The transaction ID wasn't found.</p>
            capo_rds_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rds_data.types.rollback_transaction_request.RollbackTransactionRequest]",
        ) -> AsyncOperationResponse[
            "capo_rds_data.types.rollback_transaction_response.RollbackTransactionResponse"
        ]:
            import capo_rds_data._operations.rds_data_service.rollback_transaction

            (
                output,
                http_response,
            ) = await capo_rds_data._operations.rds_data_service.rollback_transaction.async_rollback_transaction(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rds_data.types.rollback_transaction_request.RollbackTransactionRequest = {
            "resource_arn": resource_arn,
            "secret_arn": secret_arn,
            "transaction_id": transaction_id,
        }

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
