"""Generated from Smithy shape ``com.amazonaws.finspace#AWSHabaneroManagementService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_finspace._auth._signers
import capo_finspace._auth._sigv4
from capo_finspace._auth._identity import Credentials
from capo_finspace._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_finspace._auth._zapros_handler import AuthMiddleware
from capo_finspace._pagination import resolve_path as _resolve_path
from capo_finspace._services._aws_config import aws_config
from capo_finspace._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_finspace.types.auto_scaling_configuration
    import capo_finspace.types.availability_zone_id
    import capo_finspace.types.availability_zone_ids
    import capo_finspace.types.boolean_value
    import capo_finspace.types.boxed_integer
    import capo_finspace.types.capacity_configuration
    import capo_finspace.types.change_requests
    import capo_finspace.types.changeset_id
    import capo_finspace.types.client_token
    import capo_finspace.types.client_token_string
    import capo_finspace.types.code_configuration
    import capo_finspace.types.create_environment_request
    import capo_finspace.types.create_environment_response
    import capo_finspace.types.create_kx_changeset_request
    import capo_finspace.types.create_kx_changeset_response
    import capo_finspace.types.create_kx_cluster_request
    import capo_finspace.types.create_kx_cluster_response
    import capo_finspace.types.create_kx_database_request
    import capo_finspace.types.create_kx_database_response
    import capo_finspace.types.create_kx_dataview_request
    import capo_finspace.types.create_kx_dataview_response
    import capo_finspace.types.create_kx_environment_request
    import capo_finspace.types.create_kx_environment_response
    import capo_finspace.types.create_kx_scaling_group_request
    import capo_finspace.types.create_kx_scaling_group_response
    import capo_finspace.types.create_kx_user_request
    import capo_finspace.types.create_kx_user_response
    import capo_finspace.types.create_kx_volume_request
    import capo_finspace.types.create_kx_volume_response
    import capo_finspace.types.custom_dns_configuration
    import capo_finspace.types.data_bundle_arns
    import capo_finspace.types.database_name
    import capo_finspace.types.delete_environment_request
    import capo_finspace.types.delete_environment_response
    import capo_finspace.types.delete_kx_cluster_node_request
    import capo_finspace.types.delete_kx_cluster_node_response
    import capo_finspace.types.delete_kx_cluster_request
    import capo_finspace.types.delete_kx_cluster_response
    import capo_finspace.types.delete_kx_database_request
    import capo_finspace.types.delete_kx_database_response
    import capo_finspace.types.delete_kx_dataview_request
    import capo_finspace.types.delete_kx_dataview_response
    import capo_finspace.types.delete_kx_environment_request
    import capo_finspace.types.delete_kx_environment_response
    import capo_finspace.types.delete_kx_scaling_group_request
    import capo_finspace.types.delete_kx_scaling_group_response
    import capo_finspace.types.delete_kx_user_request
    import capo_finspace.types.delete_kx_user_response
    import capo_finspace.types.delete_kx_volume_request
    import capo_finspace.types.delete_kx_volume_response
    import capo_finspace.types.description
    import capo_finspace.types.environment_id
    import capo_finspace.types.environment_name
    import capo_finspace.types.execution_role_arn
    import capo_finspace.types.federation_mode
    import capo_finspace.types.federation_parameters
    import capo_finspace.types.fin_space_taggable_arn
    import capo_finspace.types.get_environment_request
    import capo_finspace.types.get_environment_response
    import capo_finspace.types.get_kx_changeset_request
    import capo_finspace.types.get_kx_changeset_response
    import capo_finspace.types.get_kx_cluster_request
    import capo_finspace.types.get_kx_cluster_response
    import capo_finspace.types.get_kx_connection_string_request
    import capo_finspace.types.get_kx_connection_string_response
    import capo_finspace.types.get_kx_database_request
    import capo_finspace.types.get_kx_database_response
    import capo_finspace.types.get_kx_dataview_request
    import capo_finspace.types.get_kx_dataview_response
    import capo_finspace.types.get_kx_environment_request
    import capo_finspace.types.get_kx_environment_response
    import capo_finspace.types.get_kx_scaling_group_request
    import capo_finspace.types.get_kx_scaling_group_response
    import capo_finspace.types.get_kx_user_request
    import capo_finspace.types.get_kx_user_response
    import capo_finspace.types.get_kx_volume_request
    import capo_finspace.types.get_kx_volume_response
    import capo_finspace.types.id_type
    import capo_finspace.types.initialization_script_file_path
    import capo_finspace.types.kms_key_arn
    import capo_finspace.types.kms_key_id
    import capo_finspace.types.kx_az_mode
    import capo_finspace.types.kx_cache_storage_configurations
    import capo_finspace.types.kx_cluster_code_deployment_configuration
    import capo_finspace.types.kx_cluster_description
    import capo_finspace.types.kx_cluster_name
    import capo_finspace.types.kx_cluster_node_id_string
    import capo_finspace.types.kx_cluster_type
    import capo_finspace.types.kx_command_line_arguments
    import capo_finspace.types.kx_database_configurations
    import capo_finspace.types.kx_dataview_name
    import capo_finspace.types.kx_dataview_segment_configuration_list
    import capo_finspace.types.kx_deployment_configuration
    import capo_finspace.types.kx_environment
    import capo_finspace.types.kx_environment_id
    import capo_finspace.types.kx_environment_name
    import capo_finspace.types.kx_host_type
    import capo_finspace.types.kx_nas1_configuration
    import capo_finspace.types.kx_savedown_storage_configuration
    import capo_finspace.types.kx_scaling_group_configuration
    import capo_finspace.types.kx_scaling_group_name
    import capo_finspace.types.kx_user_arn
    import capo_finspace.types.kx_user_name_string
    import capo_finspace.types.kx_volume_name
    import capo_finspace.types.kx_volume_type
    import capo_finspace.types.list_environments_request
    import capo_finspace.types.list_environments_response
    import capo_finspace.types.list_kx_changesets_request
    import capo_finspace.types.list_kx_changesets_response
    import capo_finspace.types.list_kx_cluster_nodes_request
    import capo_finspace.types.list_kx_cluster_nodes_response
    import capo_finspace.types.list_kx_clusters_request
    import capo_finspace.types.list_kx_clusters_response
    import capo_finspace.types.list_kx_databases_request
    import capo_finspace.types.list_kx_databases_response
    import capo_finspace.types.list_kx_dataviews_request
    import capo_finspace.types.list_kx_dataviews_response
    import capo_finspace.types.list_kx_environments_request
    import capo_finspace.types.list_kx_environments_response
    import capo_finspace.types.list_kx_scaling_groups_request
    import capo_finspace.types.list_kx_scaling_groups_response
    import capo_finspace.types.list_kx_users_request
    import capo_finspace.types.list_kx_users_response
    import capo_finspace.types.list_kx_volumes_request
    import capo_finspace.types.list_kx_volumes_response
    import capo_finspace.types.list_tags_for_resource_request
    import capo_finspace.types.list_tags_for_resource_response
    import capo_finspace.types.max_results
    import capo_finspace.types.pagination_token
    import capo_finspace.types.release_label
    import capo_finspace.types.result_limit
    import capo_finspace.types.role_arn
    import capo_finspace.types.superuser_parameters
    import capo_finspace.types.tag_key_list
    import capo_finspace.types.tag_map
    import capo_finspace.types.tag_resource_request
    import capo_finspace.types.tag_resource_response
    import capo_finspace.types.tickerplant_log_configuration
    import capo_finspace.types.transit_gateway_configuration
    import capo_finspace.types.untag_resource_request
    import capo_finspace.types.untag_resource_response
    import capo_finspace.types.update_environment_request
    import capo_finspace.types.update_environment_response
    import capo_finspace.types.update_kx_cluster_code_configuration_request
    import capo_finspace.types.update_kx_cluster_code_configuration_response
    import capo_finspace.types.update_kx_cluster_databases_request
    import capo_finspace.types.update_kx_cluster_databases_response
    import capo_finspace.types.update_kx_database_request
    import capo_finspace.types.update_kx_database_response
    import capo_finspace.types.update_kx_dataview_request
    import capo_finspace.types.update_kx_dataview_response
    import capo_finspace.types.update_kx_environment_network_request
    import capo_finspace.types.update_kx_environment_network_response
    import capo_finspace.types.update_kx_environment_request
    import capo_finspace.types.update_kx_environment_response
    import capo_finspace.types.update_kx_user_request
    import capo_finspace.types.update_kx_user_response
    import capo_finspace.types.update_kx_volume_request
    import capo_finspace.types.update_kx_volume_response
    import capo_finspace.types.vpc_configuration


class finspaceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class finspaceClient:
    """A client for the ``finspace`` service.

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
        self._config = finspaceClientConfig(
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
        self, config_overrides: Optional[finspaceClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: finspaceClientConfig = config_overrides or {}
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

    def create_environment(
        self,
        name: "capo_finspace.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["capo_finspace.types.description.Description"] = None,
        kms_key_id: Optional["capo_finspace.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_finspace.types.tag_map.TagMap"] = None,
        federation_mode: Optional[
            "capo_finspace.types.federation_mode.FederationMode"
        ] = None,
        federation_parameters: Optional[
            "capo_finspace.types.federation_parameters.FederationParameters"
        ] = None,
        superuser_parameters: Optional[
            "capo_finspace.types.superuser_parameters.SuperuserParameters"
        ] = None,
        data_bundles: Optional[
            "capo_finspace.types.data_bundle_arns.DataBundleArns"
        ] = None,
    ) -> "capo_finspace.types.create_environment_response.CreateEnvironmentResponse":
        """<p>Create a new FinSpace environment.</p>

        Args:
            name: <p>The name of the FinSpace environment to be created.</p>
            description: <p>The description of the FinSpace environment to be created.</p>
            kms_key_id: <p>The KMS key id to encrypt your data in the FinSpace environment.</p>
            tags: <p>Add tags to your FinSpace environment.</p>
            federation_mode: <p>Authentication mode for the environment.</p> <ul> <li> <p> <code>FEDERATED</code> - Users access FinSpace through Single Sign On (SSO) via your Identity provider.</p> </li> <li> <p> <code>LOCAL</code> - Users access FinSpace via email and password managed within the FinSpace environment.</p> </li> </ul>
            federation_parameters: <p>Configuration information when authentication mode is FEDERATED.</p>
            superuser_parameters: <p>Configuration information for the superuser.</p>
            data_bundles: <p>The list of Amazon Resource Names (ARN) of the data bundles to install. Currently supported data bundle ARNs:</p> <ul> <li> <p> <code>arn:aws:finspace:${Region}::data-bundle/capital-markets-sample</code> - Contains sample Capital Markets datasets, categories and controlled vocabularies.</p> </li> <li> <p> <code>arn:aws:finspace:${Region}::data-bundle/taq</code> (default) - Contains trades and quotes data in addition to sample Capital Markets data.</p> </li> </ul>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.create_environment_response.CreateEnvironmentResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.create_environment

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.create_environment_request.CreateEnvironmentRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if federation_mode is not None:
            input_["federation_mode"] = federation_mode
        if federation_parameters is not None:
            input_["federation_parameters"] = federation_parameters
        if superuser_parameters is not None:
            input_["superuser_parameters"] = superuser_parameters
        if data_bundles is not None:
            input_["data_bundles"] = data_bundles

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_kx_changeset(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        change_requests: "capo_finspace.types.change_requests.ChangeRequests",
        client_token: "capo_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.create_kx_changeset_response.CreateKxChangesetResponse":
        """<p> Creates a changeset for a kdb database. A changeset allows you to add and delete existing files by using an ordered list of change requests. </p>

        Args:
            environment_id: <p>A unique identifier of the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
            change_requests: <p>A list of change request objects that are run in order. A change request object consists of <code>changeType</code> , <code>s3Path</code>, and <code>dbPath</code>. A changeType can have the following values: </p> <ul> <li> <p>PUT – Adds or updates files in a database.</p> </li> <li> <p>DELETE – Deletes files in a database.</p> </li> </ul> <p>All the change requests require a mandatory <code>dbPath</code> attribute that defines the path within the database directory. All database paths must start with a leading / and end with a trailing /. The <code>s3Path</code> attribute defines the s3 source file path and is required for a PUT change type. The <code>s3path</code> must end with a trailing / if it is a directory and must end without a trailing / if it is a file. </p> <p>Here are few examples of how you can use the change request object:</p> <ol> <li> <p>This request adds a single sym file at database root location. </p> <p> <code>{ "changeType": "PUT", "s3Path":"s3://bucket/db/sym", "dbPath":"/"}</code> </p> </li> <li> <p>This request adds files in the given <code>s3Path</code> under the 2020.01.02 partition of the database.</p> <p> <code>{ "changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/", "dbPath":"/2020.01.02/"}</code> </p> </li> <li> <p>This request adds files in the given <code>s3Path</code> under the <i>taq</i> table partition of the database.</p> <p> <code>[ { "changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/taq/", "dbPath":"/2020.01.02/taq/"}]</code> </p> </li> <li> <p>This request deletes the 2020.01.02 partition of the database.</p> <p> <code>[{ "changeType": "DELETE", "dbPath": "/2020.01.02/"} ]</code> </p> </li> <li> <p>The <i>DELETE</i> request allows you to delete the existing files under the 2020.01.02 partition of the database, and the <i>PUT</i> request adds a new taq table under it.</p> <p> <code>[ {"changeType": "DELETE", "dbPath":"/2020.01.02/"}, {"changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/taq/", "dbPath":"/2020.01.02/taq/"}]</code> </p> </li> </ol>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.create_kx_changeset_request.CreateKxChangesetRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.create_kx_changeset_response.CreateKxChangesetResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.create_kx_changeset

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.create_kx_changeset.create_kx_changeset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.create_kx_changeset_request.CreateKxChangesetRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
            "change_requests": change_requests,
            "client_token": client_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_kx_cluster(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName",
        cluster_type: "capo_finspace.types.kx_cluster_type.KxClusterType",
        release_label: "capo_finspace.types.release_label.ReleaseLabel",
        vpc_configuration: "capo_finspace.types.vpc_configuration.VpcConfiguration",
        az_mode: "capo_finspace.types.kx_az_mode.KxAzMode",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional["capo_finspace.types.client_token.ClientToken"] = None,
        tickerplant_log_configuration: Optional[
            "capo_finspace.types.tickerplant_log_configuration.TickerplantLogConfiguration"
        ] = None,
        databases: Optional[
            "capo_finspace.types.kx_database_configurations.KxDatabaseConfigurations"
        ] = None,
        cache_storage_configurations: Optional[
            "capo_finspace.types.kx_cache_storage_configurations.KxCacheStorageConfigurations"
        ] = None,
        auto_scaling_configuration: Optional[
            "capo_finspace.types.auto_scaling_configuration.AutoScalingConfiguration"
        ] = None,
        cluster_description: Optional[
            "capo_finspace.types.kx_cluster_description.KxClusterDescription"
        ] = None,
        capacity_configuration: Optional[
            "capo_finspace.types.capacity_configuration.CapacityConfiguration"
        ] = None,
        initialization_script: Optional[
            "capo_finspace.types.initialization_script_file_path.InitializationScriptFilePath"
        ] = None,
        command_line_arguments: Optional[
            "capo_finspace.types.kx_command_line_arguments.KxCommandLineArguments"
        ] = None,
        code: Optional[
            "capo_finspace.types.code_configuration.CodeConfiguration"
        ] = None,
        execution_role: Optional[
            "capo_finspace.types.execution_role_arn.ExecutionRoleArn"
        ] = None,
        savedown_storage_configuration: Optional[
            "capo_finspace.types.kx_savedown_storage_configuration.KxSavedownStorageConfiguration"
        ] = None,
        availability_zone_id: Optional[
            "capo_finspace.types.availability_zone_id.AvailabilityZoneId"
        ] = None,
        tags: Optional["capo_finspace.types.tag_map.TagMap"] = None,
        scaling_group_configuration: Optional[
            "capo_finspace.types.kx_scaling_group_configuration.KxScalingGroupConfiguration"
        ] = None,
    ) -> "capo_finspace.types.create_kx_cluster_response.CreateKxClusterResponse":
        """<p>Creates a new kdb cluster.</p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>A unique name for the cluster that you want to create.</p>
            cluster_type: <p>Specifies the type of KDB database that is being created. The following types are available: </p> <ul> <li> <p>HDB – A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.</p> </li> <li> <p>RDB – A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the <code>savedownStorageConfiguration</code> parameter.</p> </li> <li> <p>GATEWAY – A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.</p> </li> <li> <p>GP – A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only <code>SINGLE</code> AZ mode.</p> </li> <li> <p>Tickerplant – A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.</p> </li> </ul>
            tickerplant_log_configuration: <p> A configuration to store Tickerplant logs. It consists of a list of volumes that will be mounted to your cluster. For the cluster type <code>Tickerplant</code>, the location of the TP volume on the cluster will be available by using the global variable <code>.aws.tp_log_path</code>. </p>
            databases: <p>A list of databases that will be available for querying.</p>
            cache_storage_configurations: <p>The configurations for a read only cache storage associated with a cluster. This cache will be stored as an FSx Lustre that reads from the S3 store. </p>
            auto_scaling_configuration: <p>The configuration based on which FinSpace will scale in or scale out nodes in your cluster.</p>
            cluster_description: <p>A description of the cluster.</p>
            capacity_configuration: <p>A structure for the metadata of a cluster. It includes information like the CPUs needed, memory of instances, and number of instances.</p>
            release_label: <p>The version of FinSpace managed kdb to run.</p>
            vpc_configuration: <p>Configuration details about the network where the Privatelink endpoint of the cluster resides.</p>
            initialization_script: <p>Specifies a Q program that will be run at launch of a cluster. It is a relative path within <i>.zip</i> file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, <code>somedir/init.q</code>.</p>
            command_line_arguments: <p>Defines the key-value pairs to make them available inside the cluster.</p>
            code: <p>The details of the custom code that you want to use inside a cluster when analyzing a data. It consists of the S3 source bucket, location, S3 object version, and the relative path from where the custom code is loaded into the cluster. </p>
            execution_role: <p>An IAM role that defines a set of permissions associated with a cluster. These permissions are assumed when a cluster attempts to access another cluster.</p>
            savedown_storage_configuration: <p>The size and type of the temporary storage that is used to hold data during the savedown process. This parameter is required when you choose <code>clusterType</code> as RDB. All the data written to this storage space is lost when the cluster node is restarted.</p>
            az_mode: <p>The number of availability zones you want to assign per cluster. This can be one of the following </p> <ul> <li> <p> <code>SINGLE</code> – Assigns one availability zone per cluster.</p> </li> <li> <p> <code>MULTI</code> – Assigns all the availability zones per cluster.</p> </li> </ul>
            availability_zone_id: <p>The availability zone identifiers for the requested regions.</p>
            tags: <p>A list of key-value pairs to label the cluster. You can add up to 50 tags to a cluster.</p>
            scaling_group_configuration: <p>The structure that stores the configuration details of a scaling group.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.create_kx_cluster_request.CreateKxClusterRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.create_kx_cluster_response.CreateKxClusterResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.create_kx_cluster

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.create_kx_cluster.create_kx_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.create_kx_cluster_request.CreateKxClusterRequest = {
            "environment_id": environment_id,
            "cluster_name": cluster_name,
            "cluster_type": cluster_type,
            "release_label": release_label,
            "vpc_configuration": vpc_configuration,
            "az_mode": az_mode,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tickerplant_log_configuration is not None:
            input_["tickerplant_log_configuration"] = tickerplant_log_configuration
        if databases is not None:
            input_["databases"] = databases
        if cache_storage_configurations is not None:
            input_["cache_storage_configurations"] = cache_storage_configurations
        if auto_scaling_configuration is not None:
            input_["auto_scaling_configuration"] = auto_scaling_configuration
        if cluster_description is not None:
            input_["cluster_description"] = cluster_description
        if capacity_configuration is not None:
            input_["capacity_configuration"] = capacity_configuration
        if initialization_script is not None:
            input_["initialization_script"] = initialization_script
        if command_line_arguments is not None:
            input_["command_line_arguments"] = command_line_arguments
        if code is not None:
            input_["code"] = code
        if execution_role is not None:
            input_["execution_role"] = execution_role
        if savedown_storage_configuration is not None:
            input_["savedown_storage_configuration"] = savedown_storage_configuration
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if tags is not None:
            input_["tags"] = tags
        if scaling_group_configuration is not None:
            input_["scaling_group_configuration"] = scaling_group_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_kx_database(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        client_token: "capo_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["capo_finspace.types.description.Description"] = None,
        tags: Optional["capo_finspace.types.tag_map.TagMap"] = None,
    ) -> "capo_finspace.types.create_kx_database_response.CreateKxDatabaseResponse":
        """<p>Creates a new kdb database in the environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
            description: <p>A description of the database.</p>
            tags: <p>A list of key-value pairs to label the kdb database. You can add up to 50 tags to your kdb database</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource group already exists.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.create_kx_database_request.CreateKxDatabaseRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.create_kx_database_response.CreateKxDatabaseResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.create_kx_database

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.create_kx_database.create_kx_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.create_kx_database_request.CreateKxDatabaseRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_kx_dataview(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        dataview_name: "capo_finspace.types.kx_dataview_name.KxDataviewName",
        az_mode: "capo_finspace.types.kx_az_mode.KxAzMode",
        client_token: "capo_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        availability_zone_id: Optional[
            "capo_finspace.types.availability_zone_id.AvailabilityZoneId"
        ] = None,
        changeset_id: Optional["capo_finspace.types.changeset_id.ChangesetId"] = None,
        segment_configurations: Optional[
            "capo_finspace.types.kx_dataview_segment_configuration_list.KxDataviewSegmentConfigurationList"
        ] = None,
        auto_update: Optional["capo_finspace.types.boolean_value.booleanValue"] = None,
        read_write: Optional["capo_finspace.types.boolean_value.booleanValue"] = None,
        description: Optional["capo_finspace.types.description.Description"] = None,
        tags: Optional["capo_finspace.types.tag_map.TagMap"] = None,
    ) -> "capo_finspace.types.create_kx_dataview_response.CreateKxDataviewResponse":
        """<p> Creates a snapshot of kdb database with tiered storage capabilities and a pre-warmed cache, ready for mounting on kdb clusters. Dataviews are only available for clusters running on a scaling group. They are not supported on dedicated clusters. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, where you want to create the dataview. </p>
            database_name: <p> The name of the database where you want to create a dataview. </p>
            dataview_name: <p>A unique identifier for the dataview.</p>
            az_mode: <p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>
            availability_zone_id: <p> The identifier of the availability zones. </p>
            changeset_id: <p> A unique identifier of the changeset that you want to use to ingest data. </p>
            segment_configurations: <p> The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment. </p>
            auto_update: <p>The option to specify whether you want to apply all the future additions and corrections automatically to the dataview, when you ingest new changesets. The default value is false.</p>
            read_write: <p> The option to specify whether you want to make the dataview writable to perform database maintenance. The following are some considerations related to writable dataviews. </p> <ul> <li> <p>You cannot create partial writable dataviews. When you create writeable dataviews you must provide the entire database path.</p> </li> <li> <p>You cannot perform updates on a writeable dataview. Hence, <code>autoUpdate</code> must be set as <b>False</b> if <code>readWrite</code> is <b>True</b> for a dataview.</p> </li> <li> <p>You must also use a unique volume for creating a writeable dataview. So, if you choose a volume that is already in use by another dataview, the dataview creation fails.</p> </li> <li> <p>Once you create a dataview as writeable, you cannot change it to read-only. So, you cannot update the <code>readWrite</code> parameter later.</p> </li> </ul>
            description: <p>A description of the dataview.</p>
            tags: <p> A list of key-value pairs to label the dataview. You can add up to 50 tags to a dataview. </p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource group already exists.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.create_kx_dataview_request.CreateKxDataviewRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.create_kx_dataview_response.CreateKxDataviewResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.create_kx_dataview

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.create_kx_dataview.create_kx_dataview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.create_kx_dataview_request.CreateKxDataviewRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
            "dataview_name": dataview_name,
            "az_mode": az_mode,
            "client_token": client_token,
        }
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if changeset_id is not None:
            input_["changeset_id"] = changeset_id
        if segment_configurations is not None:
            input_["segment_configurations"] = segment_configurations
        if auto_update is not None:
            input_["auto_update"] = auto_update
        if read_write is not None:
            input_["read_write"] = read_write
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_kx_environment(
        self,
        name: "capo_finspace.types.kx_environment_name.KxEnvironmentName",
        kms_key_id: "capo_finspace.types.kms_key_arn.KmsKeyARN",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["capo_finspace.types.description.Description"] = None,
        tags: Optional["capo_finspace.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_finspace.types.client_token.ClientToken"] = None,
    ) -> (
        "capo_finspace.types.create_kx_environment_response.CreateKxEnvironmentResponse"
    ):
        """<p>Creates a managed kdb environment for the account.</p>

        Args:
            name: <p>The name of the kdb environment that you want to create.</p>
            description: <p>A description for the kdb environment.</p>
            kms_key_id: <p>The KMS key ID to encrypt your data in the FinSpace environment.</p>
            tags: <p>A list of key-value pairs to label the kdb environment. You can add up to 50 tags to your kdb environment.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.create_kx_environment_request.CreateKxEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.create_kx_environment_response.CreateKxEnvironmentResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.create_kx_environment

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.create_kx_environment.create_kx_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.create_kx_environment_request.CreateKxEnvironmentRequest = {
            "name": name,
            "kms_key_id": kms_key_id,
        }
        if description is not None:
            input_["description"] = description
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

    def create_kx_scaling_group(
        self,
        client_token: "capo_finspace.types.client_token.ClientToken",
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        scaling_group_name: "capo_finspace.types.kx_scaling_group_name.KxScalingGroupName",
        host_type: "capo_finspace.types.kx_host_type.KxHostType",
        availability_zone_id: "capo_finspace.types.availability_zone_id.AvailabilityZoneId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        tags: Optional["capo_finspace.types.tag_map.TagMap"] = None,
    ) -> "capo_finspace.types.create_kx_scaling_group_response.CreateKxScalingGroupResponse":
        """<p>Creates a new scaling group. </p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            environment_id: <p>A unique identifier for the kdb environment, where you want to create the scaling group. </p>
            scaling_group_name: <p>A unique identifier for the kdb scaling group. </p>
            host_type: <p> The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.</p> <p>You can add one of the following values:</p> <ul> <li> <p> <code>kx.sg.large</code> – The host type with a configuration of 16 GiB memory and 2 vCPUs.</p> </li> <li> <p> <code>kx.sg.xlarge</code> – The host type with a configuration of 32 GiB memory and 4 vCPUs.</p> </li> <li> <p> <code>kx.sg.2xlarge</code> – The host type with a configuration of 64 GiB memory and 8 vCPUs.</p> </li> <li> <p> <code>kx.sg.4xlarge</code> – The host type with a configuration of 108 GiB memory and 16 vCPUs.</p> </li> <li> <p> <code>kx.sg.8xlarge</code> – The host type with a configuration of 216 GiB memory and 32 vCPUs.</p> </li> <li> <p> <code>kx.sg.16xlarge</code> – The host type with a configuration of 432 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.sg.32xlarge</code> – The host type with a configuration of 864 GiB memory and 128 vCPUs.</p> </li> <li> <p> <code>kx.sg1.16xlarge</code> – The host type with a configuration of 1949 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.sg1.24xlarge</code> – The host type with a configuration of 2948 GiB memory and 96 vCPUs.</p> </li> </ul>
            availability_zone_id: <p>The identifier of the availability zones.</p>
            tags: <p> A list of key-value pairs to label the scaling group. You can add up to 50 tags to a scaling group. </p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.create_kx_scaling_group_request.CreateKxScalingGroupRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.create_kx_scaling_group_response.CreateKxScalingGroupResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.create_kx_scaling_group

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.create_kx_scaling_group.create_kx_scaling_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.create_kx_scaling_group_request.CreateKxScalingGroupRequest = {
            "client_token": client_token,
            "environment_id": environment_id,
            "scaling_group_name": scaling_group_name,
            "host_type": host_type,
            "availability_zone_id": availability_zone_id,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_kx_user(
        self,
        environment_id: "capo_finspace.types.id_type.IdType",
        user_name: "capo_finspace.types.kx_user_name_string.KxUserNameString",
        iam_role: "capo_finspace.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        tags: Optional["capo_finspace.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_finspace.types.client_token.ClientToken"] = None,
    ) -> "capo_finspace.types.create_kx_user_response.CreateKxUserResponse":
        """<p>Creates a user in FinSpace kdb environment with an associated IAM role.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment where you want to create a user.</p>
            user_name: <p>A unique identifier for the user.</p>
            iam_role: <p>The IAM role ARN that will be associated with the user.</p>
            tags: <p>A list of key-value pairs to label the user. You can add up to 50 tags to a user.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource group already exists.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.create_kx_user_request.CreateKxUserRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.create_kx_user_response.CreateKxUserResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.create_kx_user

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.create_kx_user.create_kx_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.create_kx_user_request.CreateKxUserRequest = {
            "environment_id": environment_id,
            "user_name": user_name,
            "iam_role": iam_role,
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

    def create_kx_volume(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        volume_type: "capo_finspace.types.kx_volume_type.KxVolumeType",
        volume_name: "capo_finspace.types.kx_volume_name.KxVolumeName",
        az_mode: "capo_finspace.types.kx_az_mode.KxAzMode",
        availability_zone_ids: "capo_finspace.types.availability_zone_ids.AvailabilityZoneIds",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional["capo_finspace.types.client_token.ClientToken"] = None,
        description: Optional["capo_finspace.types.description.Description"] = None,
        nas1_configuration: Optional[
            "capo_finspace.types.kx_nas1_configuration.KxNAS1Configuration"
        ] = None,
        tags: Optional["capo_finspace.types.tag_map.TagMap"] = None,
    ) -> "capo_finspace.types.create_kx_volume_response.CreateKxVolumeResponse":
        """<p> Creates a new volume with a specific amount of throughput and storage capacity. </p>

        Args:
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            environment_id: <p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>
            volume_type: <p> The type of file system volume. Currently, FinSpace only supports <code>NAS_1</code> volume type. When you select <code>NAS_1</code> volume type, you must also provide <code>nas1Configuration</code>. </p>
            volume_name: <p>A unique identifier for the volume.</p>
            description: <p> A description of the volume. </p>
            nas1_configuration: <p> Specifies the configuration for the Network attached storage (NAS_1) file system volume. This parameter is required when you choose <code>volumeType</code> as <i>NAS_1</i>.</p>
            az_mode: <p>The number of availability zones you want to assign per volume. Currently, FinSpace only supports <code>SINGLE</code> for volumes. This places dataview in a single AZ.</p>
            availability_zone_ids: <p>The identifier of the availability zones.</p>
            tags: <p> A list of key-value pairs to label the volume. You can add up to 50 tags to a volume. </p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource group already exists.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.create_kx_volume_request.CreateKxVolumeRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.create_kx_volume_response.CreateKxVolumeResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.create_kx_volume

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.create_kx_volume.create_kx_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.create_kx_volume_request.CreateKxVolumeRequest = {
            "environment_id": environment_id,
            "volume_type": volume_type,
            "volume_name": volume_name,
            "az_mode": az_mode,
            "availability_zone_ids": availability_zone_ids,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if nas1_configuration is not None:
            input_["nas1_configuration"] = nas1_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_environment(
        self,
        environment_id: "capo_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.delete_environment_response.DeleteEnvironmentResponse":
        """<p>Delete an FinSpace environment.</p>

        Args:
            environment_id: <p>The identifier for the FinSpace environment.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.delete_environment_response.DeleteEnvironmentResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.delete_environment

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.delete_environment_request.DeleteEnvironmentRequest = {
            "environment_id": environment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_kx_cluster(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "capo_finspace.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "capo_finspace.types.delete_kx_cluster_response.DeleteKxClusterResponse":
        """<p>Deletes a kdb cluster.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>The name of the cluster that you want to delete.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.delete_kx_cluster_request.DeleteKxClusterRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.delete_kx_cluster_response.DeleteKxClusterResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.delete_kx_cluster

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.delete_kx_cluster.delete_kx_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.delete_kx_cluster_request.DeleteKxClusterRequest = {
            "environment_id": environment_id,
            "cluster_name": cluster_name,
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

    def delete_kx_cluster_node(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName",
        node_id: "capo_finspace.types.kx_cluster_node_id_string.KxClusterNodeIdString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.delete_kx_cluster_node_response.DeleteKxClusterNodeResponse":
        """<p>Deletes the specified nodes from a cluster. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>The name of the cluster, for which you want to delete the nodes.</p>
            node_id: <p>A unique identifier for the node that you want to delete.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.delete_kx_cluster_node_request.DeleteKxClusterNodeRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.delete_kx_cluster_node_response.DeleteKxClusterNodeResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.delete_kx_cluster_node

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.delete_kx_cluster_node.delete_kx_cluster_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.delete_kx_cluster_node_request.DeleteKxClusterNodeRequest = {
            "environment_id": environment_id,
            "cluster_name": cluster_name,
            "node_id": node_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_kx_database(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        client_token: "capo_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.delete_kx_database_response.DeleteKxDatabaseResponse":
        """<p>Deletes the specified database and all of its associated data. This action is irreversible. You must copy any data out of the database before deleting it if the data is to be retained.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database that you want to delete.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.delete_kx_database_request.DeleteKxDatabaseRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.delete_kx_database_response.DeleteKxDatabaseResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.delete_kx_database

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.delete_kx_database.delete_kx_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.delete_kx_database_request.DeleteKxDatabaseRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
            "client_token": client_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_kx_dataview(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        dataview_name: "capo_finspace.types.kx_dataview_name.KxDataviewName",
        client_token: "capo_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.delete_kx_dataview_response.DeleteKxDataviewResponse":
        """<p> Deletes the specified dataview. Before deleting a dataview, make sure that it is not in use by any cluster. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, from where you want to delete the dataview. </p>
            database_name: <p>The name of the database whose dataview you want to delete.</p>
            dataview_name: <p>The name of the dataview that you want to delete.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.delete_kx_dataview_request.DeleteKxDataviewRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.delete_kx_dataview_response.DeleteKxDataviewResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.delete_kx_dataview

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.delete_kx_dataview.delete_kx_dataview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.delete_kx_dataview_request.DeleteKxDataviewRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
            "dataview_name": dataview_name,
            "client_token": client_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_kx_environment(
        self,
        environment_id: "capo_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional["capo_finspace.types.client_token.ClientToken"] = None,
    ) -> (
        "capo_finspace.types.delete_kx_environment_response.DeleteKxEnvironmentResponse"
    ):
        """<p>Deletes the kdb environment. This action is irreversible. Deleting a kdb environment will remove all the associated data and any services running in it. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.delete_kx_environment_request.DeleteKxEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.delete_kx_environment_response.DeleteKxEnvironmentResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.delete_kx_environment

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.delete_kx_environment.delete_kx_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.delete_kx_environment_request.DeleteKxEnvironmentRequest = {
            "environment_id": environment_id
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

    def delete_kx_scaling_group(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        scaling_group_name: "capo_finspace.types.kx_scaling_group_name.KxScalingGroupName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "capo_finspace.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "capo_finspace.types.delete_kx_scaling_group_response.DeleteKxScalingGroupResponse":
        """<p> Deletes the specified scaling group. This action is irreversible. You cannot delete a scaling group until all the clusters running on it have been deleted.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, from where you want to delete the dataview. </p>
            scaling_group_name: <p>A unique identifier for the kdb scaling group. </p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.delete_kx_scaling_group_request.DeleteKxScalingGroupRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.delete_kx_scaling_group_response.DeleteKxScalingGroupResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.delete_kx_scaling_group

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.delete_kx_scaling_group.delete_kx_scaling_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.delete_kx_scaling_group_request.DeleteKxScalingGroupRequest = {
            "environment_id": environment_id,
            "scaling_group_name": scaling_group_name,
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

    def delete_kx_user(
        self,
        user_name: "capo_finspace.types.kx_user_name_string.KxUserNameString",
        environment_id: "capo_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional["capo_finspace.types.client_token.ClientToken"] = None,
    ) -> "capo_finspace.types.delete_kx_user_response.DeleteKxUserResponse":
        """<p>Deletes a user in the specified kdb environment.</p>

        Args:
            user_name: <p>A unique identifier for the user that you want to delete.</p>
            environment_id: <p>A unique identifier for the kdb environment.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.delete_kx_user_request.DeleteKxUserRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.delete_kx_user_response.DeleteKxUserResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.delete_kx_user

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.delete_kx_user.delete_kx_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.delete_kx_user_request.DeleteKxUserRequest = {
            "user_name": user_name,
            "environment_id": environment_id,
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

    def delete_kx_volume(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        volume_name: "capo_finspace.types.kx_volume_name.KxVolumeName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "capo_finspace.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "capo_finspace.types.delete_kx_volume_response.DeleteKxVolumeResponse":
        """<p> Deletes a volume. You can only delete a volume if it's not attached to a cluster or a dataview. When a volume is deleted, any data on the volume is lost. This action is irreversible. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>
            volume_name: <p> The name of the volume that you want to delete. </p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.delete_kx_volume_request.DeleteKxVolumeRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.delete_kx_volume_response.DeleteKxVolumeResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.delete_kx_volume

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.delete_kx_volume.delete_kx_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.delete_kx_volume_request.DeleteKxVolumeRequest = {
            "environment_id": environment_id,
            "volume_name": volume_name,
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

    def get_environment(
        self,
        environment_id: "capo_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.get_environment_response.GetEnvironmentResponse":
        """<p>Returns the FinSpace environment object.</p>

        Args:
            environment_id: <p>The identifier of the FinSpace environment.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.get_environment_request.GetEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.get_environment

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.get_environment_request.GetEnvironmentRequest = {
            "environment_id": environment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_kx_changeset(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        changeset_id: "capo_finspace.types.changeset_id.ChangesetId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.get_kx_changeset_response.GetKxChangesetResponse":
        """<p>Returns information about a kdb changeset.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
            changeset_id: <p>A unique identifier of the changeset for which you want to retrieve data.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.get_kx_changeset_request.GetKxChangesetRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.get_kx_changeset_response.GetKxChangesetResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.get_kx_changeset

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.get_kx_changeset.get_kx_changeset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.get_kx_changeset_request.GetKxChangesetRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
            "changeset_id": changeset_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_kx_cluster(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.get_kx_cluster_response.GetKxClusterResponse":
        """<p>Retrieves information about a kdb cluster.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>The name of the cluster that you want to retrieve.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.get_kx_cluster_request.GetKxClusterRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.get_kx_cluster_response.GetKxClusterResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.get_kx_cluster

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.get_kx_cluster.get_kx_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.get_kx_cluster_request.GetKxClusterRequest = {
            "environment_id": environment_id,
            "cluster_name": cluster_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_kx_connection_string(
        self,
        user_arn: "capo_finspace.types.kx_user_arn.KxUserArn",
        environment_id: "capo_finspace.types.id_type.IdType",
        cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.get_kx_connection_string_response.GetKxConnectionStringResponse":
        """<p>Retrieves a connection string for a user to connect to a kdb cluster. You must call this API using the same role that you have defined while creating a user. </p>

        Args:
            user_arn: <p> The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM Identifiers</a> in the <i>IAM User Guide</i>. </p>
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>A name of the kdb cluster.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.get_kx_connection_string_request.GetKxConnectionStringRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.get_kx_connection_string_response.GetKxConnectionStringResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.get_kx_connection_string

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.get_kx_connection_string.get_kx_connection_string(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.get_kx_connection_string_request.GetKxConnectionStringRequest = {
            "user_arn": user_arn,
            "environment_id": environment_id,
            "cluster_name": cluster_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_kx_database(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.get_kx_database_response.GetKxDatabaseResponse":
        """<p>Returns database information for the specified environment ID.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.get_kx_database_request.GetKxDatabaseRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.get_kx_database_response.GetKxDatabaseResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.get_kx_database

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.get_kx_database.get_kx_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.get_kx_database_request.GetKxDatabaseRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_kx_dataview(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        dataview_name: "capo_finspace.types.kx_dataview_name.KxDataviewName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.get_kx_dataview_response.GetKxDataviewResponse":
        """<p> Retrieves details of the dataview. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, from where you want to retrieve the dataview details.</p>
            database_name: <p> The name of the database where you created the dataview.</p>
            dataview_name: <p>A unique identifier for the dataview.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.get_kx_dataview_request.GetKxDataviewRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.get_kx_dataview_response.GetKxDataviewResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.get_kx_dataview

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.get_kx_dataview.get_kx_dataview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.get_kx_dataview_request.GetKxDataviewRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
            "dataview_name": dataview_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_kx_environment(
        self,
        environment_id: "capo_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.get_kx_environment_response.GetKxEnvironmentResponse":
        """<p>Retrieves all the information for the specified kdb environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.get_kx_environment_request.GetKxEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.get_kx_environment_response.GetKxEnvironmentResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.get_kx_environment

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.get_kx_environment.get_kx_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.get_kx_environment_request.GetKxEnvironmentRequest = {
            "environment_id": environment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_kx_scaling_group(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        scaling_group_name: "capo_finspace.types.kx_scaling_group_name.KxScalingGroupName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.get_kx_scaling_group_response.GetKxScalingGroupResponse":
        """<p> Retrieves details of a scaling group.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment. </p>
            scaling_group_name: <p>A unique identifier for the kdb scaling group. </p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.get_kx_scaling_group_request.GetKxScalingGroupRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.get_kx_scaling_group_response.GetKxScalingGroupResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.get_kx_scaling_group

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.get_kx_scaling_group.get_kx_scaling_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.get_kx_scaling_group_request.GetKxScalingGroupRequest = {
            "environment_id": environment_id,
            "scaling_group_name": scaling_group_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_kx_user(
        self,
        user_name: "capo_finspace.types.kx_user_name_string.KxUserNameString",
        environment_id: "capo_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.get_kx_user_response.GetKxUserResponse":
        """<p>Retrieves information about the specified kdb user.</p>

        Args:
            user_name: <p>A unique identifier for the user.</p>
            environment_id: <p>A unique identifier for the kdb environment.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.get_kx_user_request.GetKxUserRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.get_kx_user_response.GetKxUserResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.get_kx_user

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.get_kx_user.get_kx_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.get_kx_user_request.GetKxUserRequest = {
            "user_name": user_name,
            "environment_id": environment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_kx_volume(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        volume_name: "capo_finspace.types.kx_volume_name.KxVolumeName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.get_kx_volume_response.GetKxVolumeResponse":
        """<p> Retrieves the information about the volume. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>
            volume_name: <p>A unique identifier for the volume.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.get_kx_volume_request.GetKxVolumeRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.get_kx_volume_response.GetKxVolumeResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.get_kx_volume

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.get_kx_volume.get_kx_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.get_kx_volume_request.GetKxVolumeRequest = {
            "environment_id": environment_id,
            "volume_name": volume_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_environments(
        self,
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.result_limit.ResultLimit"] = None,
    ) -> "capo_finspace.types.list_environments_response.ListEnvironmentsResponse":
        """<p>A list of all of your FinSpace environments.</p>

        Args:
            next_token: <p>A token generated by FinSpace that specifies where to continue pagination if a previous request was truncated. To get the next set of pages, pass in the <code>nextToken</code>nextToken value from the response object of the previous page call.</p>
            max_results: <p>The maximum number of results to return in this request.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_environments

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_environments_request.ListEnvironmentsRequest = {}
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

    def list_kx_changesets(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.max_results.MaxResults"] = None,
    ) -> "capo_finspace.types.list_kx_changesets_response.ListKxChangesetsResponse":
        """<p>Returns a list of all the changesets for a database.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results to return in this request.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_kx_changesets_request.ListKxChangesetsRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_kx_changesets_response.ListKxChangesetsResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_kx_changesets

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_kx_changesets.list_kx_changesets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_kx_changesets_request.ListKxChangesetsRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
        }
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

    def iter_list_kx_changesets(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_finspace.types.list_kx_changesets_response.ListKxChangesetsResponse]":
        _token = next_token
        while True:
            _response = self.list_kx_changesets(
                environment_id,
                database_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_kx_cluster_nodes(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.result_limit.ResultLimit"] = None,
    ) -> (
        "capo_finspace.types.list_kx_cluster_nodes_response.ListKxClusterNodesResponse"
    ):
        """<p>Lists all the nodes in a kdb cluster.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_name: <p>A unique name for the cluster.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results to return in this request.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_kx_cluster_nodes_request.ListKxClusterNodesRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_kx_cluster_nodes_response.ListKxClusterNodesResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_kx_cluster_nodes

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_kx_cluster_nodes.list_kx_cluster_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_kx_cluster_nodes_request.ListKxClusterNodesRequest = {
            "environment_id": environment_id,
            "cluster_name": cluster_name,
        }
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

    def iter_list_kx_cluster_nodes(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.result_limit.ResultLimit"] = None,
    ) -> "Iterator[capo_finspace.types.list_kx_cluster_nodes_response.ListKxClusterNodesResponse]":
        _token = next_token
        while True:
            _response = self.list_kx_cluster_nodes(
                environment_id,
                cluster_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_kx_clusters(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        cluster_type: Optional[
            "capo_finspace.types.kx_cluster_type.KxClusterType"
        ] = None,
        max_results: Optional["capo_finspace.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_finspace.types.list_kx_clusters_response.ListKxClustersResponse":
        """<p>Returns a list of clusters.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            cluster_type: <p>Specifies the type of KDB database that is being created. The following types are available: </p> <ul> <li> <p>HDB – A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.</p> </li> <li> <p>RDB – A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the <code>savedownStorageConfiguration</code> parameter.</p> </li> <li> <p>GATEWAY – A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.</p> </li> <li> <p>GP – A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only <code>SINGLE</code> AZ mode.</p> </li> <li> <p>Tickerplant – A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.</p> </li> </ul>
            max_results: <p>The maximum number of results to return in this request.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_kx_clusters_request.ListKxClustersRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_kx_clusters_response.ListKxClustersResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_kx_clusters

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_kx_clusters.list_kx_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_kx_clusters_request.ListKxClustersRequest = {
            "environment_id": environment_id
        }
        if cluster_type is not None:
            input_["cluster_type"] = cluster_type
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

    def list_kx_databases(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.max_results.MaxResults"] = None,
    ) -> "capo_finspace.types.list_kx_databases_response.ListKxDatabasesResponse":
        """<p>Returns a list of all the databases in the kdb environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results to return in this request.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_kx_databases_request.ListKxDatabasesRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_kx_databases_response.ListKxDatabasesResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_kx_databases

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_kx_databases.list_kx_databases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_kx_databases_request.ListKxDatabasesRequest = {
            "environment_id": environment_id
        }
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

    def iter_list_kx_databases(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_finspace.types.list_kx_databases_response.ListKxDatabasesResponse]":
        _token = next_token
        while True:
            _response = self.list_kx_databases(
                environment_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_kx_dataviews(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.max_results.MaxResults"] = None,
    ) -> "capo_finspace.types.list_kx_dataviews_response.ListKxDataviewsResponse":
        """<p> Returns a list of all the dataviews in the database.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, for which you want to retrieve a list of dataviews.</p>
            database_name: <p> The name of the database where the dataviews were created.</p>
            next_token: <p> A token that indicates where a results page should begin. </p>
            max_results: <p>The maximum number of results to return in this request.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_kx_dataviews_request.ListKxDataviewsRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_kx_dataviews_response.ListKxDataviewsResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_kx_dataviews

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_kx_dataviews.list_kx_dataviews(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_kx_dataviews_request.ListKxDataviewsRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
        }
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

    def iter_list_kx_dataviews(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_finspace.types.list_kx_dataviews_response.ListKxDataviewsResponse]":
        _token = next_token
        while True:
            _response = self.list_kx_dataviews(
                environment_id,
                database_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_kx_environments(
        self,
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.boxed_integer.BoxedInteger"] = None,
    ) -> "capo_finspace.types.list_kx_environments_response.ListKxEnvironmentsResponse":
        """<p>Returns a list of kdb environments created in an account.</p>

        Args:
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results to return in this request.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_kx_environments_request.ListKxEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_kx_environments_response.ListKxEnvironmentsResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_kx_environments

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_kx_environments.list_kx_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_kx_environments_request.ListKxEnvironmentsRequest = {}
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

    def iter_list_kx_environments(
        self,
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.boxed_integer.BoxedInteger"] = None,
    ) -> "Iterator[capo_finspace.types.kx_environment.KxEnvironment]":
        _token = next_token
        while True:
            _response = self.list_kx_environments(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_kx_scaling_groups(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        max_results: Optional["capo_finspace.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_finspace.types.list_kx_scaling_groups_response.ListKxScalingGroupsResponse":
        """<p> Returns a list of scaling groups in a kdb environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, for which you want to retrieve a list of scaling groups.</p>
            max_results: <p>The maximum number of results to return in this request.</p>
            next_token: <p> A token that indicates where a results page should begin. </p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_kx_scaling_groups_request.ListKxScalingGroupsRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_kx_scaling_groups_response.ListKxScalingGroupsResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_kx_scaling_groups

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_kx_scaling_groups.list_kx_scaling_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_kx_scaling_groups_request.ListKxScalingGroupsRequest = {
            "environment_id": environment_id
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

    def iter_list_kx_scaling_groups(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        max_results: Optional["capo_finspace.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_finspace.types.list_kx_scaling_groups_response.ListKxScalingGroupsResponse]":
        _token = next_token
        while True:
            _response = self.list_kx_scaling_groups(
                environment_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_kx_users(
        self,
        environment_id: "capo_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_finspace.types.result_limit.ResultLimit"] = None,
    ) -> "capo_finspace.types.list_kx_users_response.ListKxUsersResponse":
        """<p>Lists all the users in a kdb environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            max_results: <p>The maximum number of results to return in this request.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_kx_users_request.ListKxUsersRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_kx_users_response.ListKxUsersResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_kx_users

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_kx_users.list_kx_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_kx_users_request.ListKxUsersRequest = {
            "environment_id": environment_id
        }
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

    def list_kx_volumes(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        max_results: Optional["capo_finspace.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_finspace.types.pagination_token.PaginationToken"
        ] = None,
        volume_type: Optional["capo_finspace.types.kx_volume_type.KxVolumeType"] = None,
    ) -> "capo_finspace.types.list_kx_volumes_response.ListKxVolumesResponse":
        """<p> Lists all the volumes in a kdb environment. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>
            max_results: <p>The maximum number of results to return in this request.</p>
            next_token: <p>A token that indicates where a results page should begin.</p>
            volume_type: <p> The type of file system volume. Currently, FinSpace only supports <code>NAS_1</code> volume type. </p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_kx_volumes_request.ListKxVolumesRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_kx_volumes_response.ListKxVolumesResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_kx_volumes

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_kx_volumes.list_kx_volumes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_kx_volumes_request.ListKxVolumesRequest = {
            "environment_id": environment_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if volume_type is not None:
            input_["volume_type"] = volume_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_finspace.types.fin_space_taggable_arn.FinSpaceTaggableArn",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>A list of all tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name of the resource.</p>

        Raises:
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid. Something is wrong with the input to the request.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.list_tags_for_resource

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_finspace.types.fin_space_taggable_arn.FinSpaceTaggableArn",
        tags: "capo_finspace.types.tag_map.TagMap",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.tag_resource_response.TagResourceResponse":
        """<p>Adds metadata tags to a FinSpace resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the resource.</p>
            tags: <p>One or more tags to be assigned to the resource.</p>

        Raises:
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid. Something is wrong with the input to the request.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.tag_resource

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_finspace.types.fin_space_taggable_arn.FinSpaceTaggableArn",
        tag_keys: "capo_finspace.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
    ) -> "capo_finspace.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes metadata tags from a FinSpace resource.</p>

        Args:
            resource_arn: <p>A FinSpace resource from which you want to remove a tag or tags. The value for this parameter is an Amazon Resource Name (ARN).</p>
            tag_keys: <p>The tag keys (names) of one or more tags to be removed.</p>

        Raises:
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.invalid_request_exception.InvalidRequestException: <p>The request is invalid. Something is wrong with the input to the request.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.untag_resource

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.untag_resource_request.UntagResourceRequest = {
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

    def update_environment(
        self,
        environment_id: "capo_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        name: Optional["capo_finspace.types.environment_name.EnvironmentName"] = None,
        description: Optional["capo_finspace.types.description.Description"] = None,
        federation_mode: Optional[
            "capo_finspace.types.federation_mode.FederationMode"
        ] = None,
        federation_parameters: Optional[
            "capo_finspace.types.federation_parameters.FederationParameters"
        ] = None,
    ) -> "capo_finspace.types.update_environment_response.UpdateEnvironmentResponse":
        """<p>Update your FinSpace environment.</p>

        Args:
            environment_id: <p>The identifier of the FinSpace environment.</p>
            name: <p>The name of the environment.</p>
            description: <p>The description of the environment.</p>
            federation_mode: <p>Authentication mode for the environment.</p> <ul> <li> <p> <code>FEDERATED</code> - Users access FinSpace through Single Sign On (SSO) via your Identity provider.</p> </li> <li> <p> <code>LOCAL</code> - Users access FinSpace via email and password managed within the FinSpace environment.</p> </li> </ul>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.update_environment_request.UpdateEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.update_environment_response.UpdateEnvironmentResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.update_environment

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.update_environment.update_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.update_environment_request.UpdateEnvironmentRequest = {
            "environment_id": environment_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if federation_mode is not None:
            input_["federation_mode"] = federation_mode
        if federation_parameters is not None:
            input_["federation_parameters"] = federation_parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_kx_cluster_code_configuration(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName",
        code: "capo_finspace.types.code_configuration.CodeConfiguration",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "capo_finspace.types.client_token_string.ClientTokenString"
        ] = None,
        initialization_script: Optional[
            "capo_finspace.types.initialization_script_file_path.InitializationScriptFilePath"
        ] = None,
        command_line_arguments: Optional[
            "capo_finspace.types.kx_command_line_arguments.KxCommandLineArguments"
        ] = None,
        deployment_configuration: Optional[
            "capo_finspace.types.kx_cluster_code_deployment_configuration.KxClusterCodeDeploymentConfiguration"
        ] = None,
    ) -> "capo_finspace.types.update_kx_cluster_code_configuration_response.UpdateKxClusterCodeConfigurationResponse":
        """<p> Allows you to update code configuration on a running cluster. By using this API you can update the code, the initialization script path, and the command line arguments for a specific cluster. The configuration that you want to update will override any existing configurations on the cluster. </p>

        Args:
            environment_id: <p> A unique identifier of the kdb environment. </p>
            cluster_name: <p>The name of the cluster.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            initialization_script: <p>Specifies a Q program that will be run at launch of a cluster. It is a relative path within <i>.zip</i> file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, <code>somedir/init.q</code>.</p> <p>You cannot update this parameter for a <code>NO_RESTART</code> deployment.</p>
            command_line_arguments: <p>Specifies the key-value pairs to make them available inside the cluster.</p> <p>You cannot update this parameter for a <code>NO_RESTART</code> deployment.</p>
            deployment_configuration: <p> The configuration that allows you to choose how you want to update the code on a cluster. </p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.update_kx_cluster_code_configuration_request.UpdateKxClusterCodeConfigurationRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.update_kx_cluster_code_configuration_response.UpdateKxClusterCodeConfigurationResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.update_kx_cluster_code_configuration

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.update_kx_cluster_code_configuration.update_kx_cluster_code_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.update_kx_cluster_code_configuration_request.UpdateKxClusterCodeConfigurationRequest = {
            "environment_id": environment_id,
            "cluster_name": cluster_name,
            "code": code,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if initialization_script is not None:
            input_["initialization_script"] = initialization_script
        if command_line_arguments is not None:
            input_["command_line_arguments"] = command_line_arguments
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_kx_cluster_databases(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        cluster_name: "capo_finspace.types.kx_cluster_name.KxClusterName",
        databases: "capo_finspace.types.kx_database_configurations.KxDatabaseConfigurations",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional[
            "capo_finspace.types.client_token_string.ClientTokenString"
        ] = None,
        deployment_configuration: Optional[
            "capo_finspace.types.kx_deployment_configuration.KxDeploymentConfiguration"
        ] = None,
    ) -> "capo_finspace.types.update_kx_cluster_databases_response.UpdateKxClusterDatabasesResponse":
        """<p>Updates the databases mounted on a kdb cluster, which includes the <code>changesetId</code> and all the dbPaths to be cached. This API does not allow you to change a database name or add a database if you created a cluster without one. </p> <p>Using this API you can point a cluster to a different changeset and modify a list of partitions being cached.</p>

        Args:
            environment_id: <p>The unique identifier of a kdb environment.</p>
            cluster_name: <p>A unique name for the cluster that you want to modify.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            databases: <p> The structure of databases mounted on the cluster.</p>
            deployment_configuration: <p> The configuration that allows you to choose how you want to update the databases on a cluster. </p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.update_kx_cluster_databases_request.UpdateKxClusterDatabasesRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.update_kx_cluster_databases_response.UpdateKxClusterDatabasesResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.update_kx_cluster_databases

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.update_kx_cluster_databases.update_kx_cluster_databases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.update_kx_cluster_databases_request.UpdateKxClusterDatabasesRequest = {
            "environment_id": environment_id,
            "cluster_name": cluster_name,
            "databases": databases,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_kx_database(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        client_token: "capo_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["capo_finspace.types.description.Description"] = None,
    ) -> "capo_finspace.types.update_kx_database_response.UpdateKxDatabaseResponse":
        """<p>Updates information for the given kdb database.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            database_name: <p>The name of the kdb database.</p>
            description: <p>A description of the database.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.update_kx_database_request.UpdateKxDatabaseRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.update_kx_database_response.UpdateKxDatabaseResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.update_kx_database

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.update_kx_database.update_kx_database(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.update_kx_database_request.UpdateKxDatabaseRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_kx_dataview(
        self,
        environment_id: "capo_finspace.types.environment_id.EnvironmentId",
        database_name: "capo_finspace.types.database_name.DatabaseName",
        dataview_name: "capo_finspace.types.kx_dataview_name.KxDataviewName",
        client_token: "capo_finspace.types.client_token_string.ClientTokenString",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["capo_finspace.types.description.Description"] = None,
        changeset_id: Optional["capo_finspace.types.changeset_id.ChangesetId"] = None,
        segment_configurations: Optional[
            "capo_finspace.types.kx_dataview_segment_configuration_list.KxDataviewSegmentConfigurationList"
        ] = None,
    ) -> "capo_finspace.types.update_kx_dataview_response.UpdateKxDataviewResponse":
        """<p> Updates the specified dataview. The dataviews get automatically updated when any new changesets are ingested. Each update of the dataview creates a new version, including changeset details and cache configurations</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment, where you want to update the dataview.</p>
            database_name: <p> The name of the database.</p>
            dataview_name: <p>The name of the dataview that you want to update.</p>
            description: <p> The description for a dataview. </p>
            changeset_id: <p>A unique identifier for the changeset.</p>
            segment_configurations: <p> The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment. </p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource group already exists.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.update_kx_dataview_request.UpdateKxDataviewRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.update_kx_dataview_response.UpdateKxDataviewResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.update_kx_dataview

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.update_kx_dataview.update_kx_dataview(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.update_kx_dataview_request.UpdateKxDataviewRequest = {
            "environment_id": environment_id,
            "database_name": database_name,
            "dataview_name": dataview_name,
            "client_token": client_token,
        }
        if description is not None:
            input_["description"] = description
        if changeset_id is not None:
            input_["changeset_id"] = changeset_id
        if segment_configurations is not None:
            input_["segment_configurations"] = segment_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_kx_environment(
        self,
        environment_id: "capo_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        name: Optional[
            "capo_finspace.types.kx_environment_name.KxEnvironmentName"
        ] = None,
        description: Optional["capo_finspace.types.description.Description"] = None,
        client_token: Optional["capo_finspace.types.client_token.ClientToken"] = None,
    ) -> (
        "capo_finspace.types.update_kx_environment_response.UpdateKxEnvironmentResponse"
    ):
        """<p>Updates information for the given kdb environment.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            name: <p>The name of the kdb environment.</p>
            description: <p>A description of the kdb environment.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.update_kx_environment_request.UpdateKxEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.update_kx_environment_response.UpdateKxEnvironmentResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.update_kx_environment

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.update_kx_environment.update_kx_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.update_kx_environment_request.UpdateKxEnvironmentRequest = {
            "environment_id": environment_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
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

    def update_kx_environment_network(
        self,
        environment_id: "capo_finspace.types.id_type.IdType",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        transit_gateway_configuration: Optional[
            "capo_finspace.types.transit_gateway_configuration.TransitGatewayConfiguration"
        ] = None,
        custom_dns_configuration: Optional[
            "capo_finspace.types.custom_dns_configuration.CustomDNSConfiguration"
        ] = None,
        client_token: Optional["capo_finspace.types.client_token.ClientToken"] = None,
    ) -> "capo_finspace.types.update_kx_environment_network_response.UpdateKxEnvironmentNetworkResponse":
        """<p>Updates environment network to connect to your internal network by using a transit gateway. This API supports request to create a transit gateway attachment from FinSpace VPC to your transit gateway ID and create a custom Route-53 outbound resolvers.</p> <p>Once you send a request to update a network, you cannot change it again. Network update might require termination of any clusters that are running in the existing network.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            transit_gateway_configuration: <p>Specifies the transit gateway and network configuration to connect the kdb environment to an internal network.</p>
            custom_dns_configuration: <p>A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.update_kx_environment_network_request.UpdateKxEnvironmentNetworkRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.update_kx_environment_network_response.UpdateKxEnvironmentNetworkResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.update_kx_environment_network

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.update_kx_environment_network.update_kx_environment_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.update_kx_environment_network_request.UpdateKxEnvironmentNetworkRequest = {
            "environment_id": environment_id
        }
        if transit_gateway_configuration is not None:
            input_["transit_gateway_configuration"] = transit_gateway_configuration
        if custom_dns_configuration is not None:
            input_["custom_dns_configuration"] = custom_dns_configuration
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

    def update_kx_user(
        self,
        environment_id: "capo_finspace.types.id_type.IdType",
        user_name: "capo_finspace.types.kx_user_name_string.KxUserNameString",
        iam_role: "capo_finspace.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        client_token: Optional["capo_finspace.types.client_token.ClientToken"] = None,
    ) -> "capo_finspace.types.update_kx_user_response.UpdateKxUserResponse":
        """<p>Updates the user details. You can only update the IAM role associated with a user.</p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment.</p>
            user_name: <p>A unique identifier for the user.</p>
            iam_role: <p>The IAM role ARN that is associated with the user.</p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.update_kx_user_request.UpdateKxUserRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.update_kx_user_response.UpdateKxUserResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.update_kx_user

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.update_kx_user.update_kx_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.update_kx_user_request.UpdateKxUserRequest = {
            "environment_id": environment_id,
            "user_name": user_name,
            "iam_role": iam_role,
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

    def update_kx_volume(
        self,
        environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId",
        volume_name: "capo_finspace.types.kx_volume_name.KxVolumeName",
        *,
        config_overrides: Optional[finspaceClientConfig] = None,
        description: Optional["capo_finspace.types.description.Description"] = None,
        client_token: Optional[
            "capo_finspace.types.client_token_string.ClientTokenString"
        ] = None,
        nas1_configuration: Optional[
            "capo_finspace.types.kx_nas1_configuration.KxNAS1Configuration"
        ] = None,
    ) -> "capo_finspace.types.update_kx_volume_response.UpdateKxVolumeResponse":
        """<p> Updates the throughput or capacity of a volume. During the update process, the filesystem might be unavailable for a few minutes. You can retry any operations after the update is complete. </p>

        Args:
            environment_id: <p>A unique identifier for the kdb environment where you created the storage volume. </p>
            volume_name: <p> A unique identifier for the volume.</p>
            description: <p> A description of the volume. </p>
            client_token: <p>A token that ensures idempotency. This token expires in 10 minutes.</p>
            nas1_configuration: <p> Specifies the configuration for the Network attached storage (NAS_1) file system volume.</p>

        Raises:
            capo_finspace.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_finspace.errors.conflict_exception.ConflictException: <p>There was a conflict with this action, and it could not be completed.</p>
            capo_finspace.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_finspace.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit or quota is exceeded.</p>
            capo_finspace.errors.resource_not_found_exception.ResourceNotFoundException: <p>One or more resources can't be found.</p>
            capo_finspace.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_finspace.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_finspace.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_finspace.types.update_kx_volume_request.UpdateKxVolumeRequest]",
        ) -> OperationResponse[
            "capo_finspace.types.update_kx_volume_response.UpdateKxVolumeResponse"
        ]:
            import capo_finspace._operations.aws_habanero_management_service.update_kx_volume

            output, http_response = (
                capo_finspace._operations.aws_habanero_management_service.update_kx_volume.update_kx_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_finspace.types.update_kx_volume_request.UpdateKxVolumeRequest = {
            "environment_id": environment_id,
            "volume_name": volume_name,
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if nas1_configuration is not None:
            input_["nas1_configuration"] = nas1_configuration

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
