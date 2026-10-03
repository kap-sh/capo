"""Generated from Smithy shape ``com.amazonaws.lakeformation#AWSLakeFormation``."""

import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_lakeformation._auth._signers
import capo_lakeformation._auth._sigv4
from capo_lakeformation._auth._identity import Credentials
from capo_lakeformation._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lakeformation._auth._zapros_handler import AuthMiddleware
from capo_lakeformation._pagination import resolve_path as _resolve_path
from capo_lakeformation._services._aws_config import aws_config
from capo_lakeformation._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_lakeformation.types.account_id_string
    import capo_lakeformation.types.add_lf_tags_to_resource_request
    import capo_lakeformation.types.add_lf_tags_to_resource_response
    import capo_lakeformation.types.application_status
    import capo_lakeformation.types.assume_decorated_role_with_saml_request
    import capo_lakeformation.types.assume_decorated_role_with_saml_response
    import capo_lakeformation.types.audit_context
    import capo_lakeformation.types.batch_grant_permissions_request
    import capo_lakeformation.types.batch_grant_permissions_response
    import capo_lakeformation.types.batch_permissions_request_entry_list
    import capo_lakeformation.types.batch_revoke_permissions_request
    import capo_lakeformation.types.batch_revoke_permissions_response
    import capo_lakeformation.types.boolean
    import capo_lakeformation.types.boolean_nullable
    import capo_lakeformation.types.cancel_transaction_request
    import capo_lakeformation.types.cancel_transaction_response
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.commit_transaction_request
    import capo_lakeformation.types.commit_transaction_response
    import capo_lakeformation.types.condition
    import capo_lakeformation.types.create_data_cells_filter_request
    import capo_lakeformation.types.create_data_cells_filter_response
    import capo_lakeformation.types.create_lake_formation_identity_center_configuration_request
    import capo_lakeformation.types.create_lake_formation_identity_center_configuration_response
    import capo_lakeformation.types.create_lake_formation_opt_in_request
    import capo_lakeformation.types.create_lake_formation_opt_in_response
    import capo_lakeformation.types.create_lf_tag_expression_request
    import capo_lakeformation.types.create_lf_tag_expression_response
    import capo_lakeformation.types.create_lf_tag_request
    import capo_lakeformation.types.create_lf_tag_response
    import capo_lakeformation.types.credential_timeout_duration_second_integer
    import capo_lakeformation.types.credentials_scope
    import capo_lakeformation.types.data_cells_filter
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.data_lake_principal_list
    import capo_lakeformation.types.data_lake_resource_type
    import capo_lakeformation.types.data_lake_settings
    import capo_lakeformation.types.delete_data_cells_filter_request
    import capo_lakeformation.types.delete_data_cells_filter_response
    import capo_lakeformation.types.delete_lake_formation_identity_center_configuration_request
    import capo_lakeformation.types.delete_lake_formation_identity_center_configuration_response
    import capo_lakeformation.types.delete_lake_formation_opt_in_request
    import capo_lakeformation.types.delete_lake_formation_opt_in_response
    import capo_lakeformation.types.delete_lf_tag_expression_request
    import capo_lakeformation.types.delete_lf_tag_expression_response
    import capo_lakeformation.types.delete_lf_tag_request
    import capo_lakeformation.types.delete_lf_tag_response
    import capo_lakeformation.types.delete_objects_on_cancel_request
    import capo_lakeformation.types.delete_objects_on_cancel_response
    import capo_lakeformation.types.deregister_resource_request
    import capo_lakeformation.types.deregister_resource_response
    import capo_lakeformation.types.describe_lake_formation_identity_center_configuration_request
    import capo_lakeformation.types.describe_lake_formation_identity_center_configuration_response
    import capo_lakeformation.types.describe_resource_request
    import capo_lakeformation.types.describe_resource_response
    import capo_lakeformation.types.describe_transaction_request
    import capo_lakeformation.types.describe_transaction_response
    import capo_lakeformation.types.description_string
    import capo_lakeformation.types.expression
    import capo_lakeformation.types.extend_transaction_request
    import capo_lakeformation.types.extend_transaction_response
    import capo_lakeformation.types.external_filtering_configuration
    import capo_lakeformation.types.filter_condition_list
    import capo_lakeformation.types.get_data_cells_filter_request
    import capo_lakeformation.types.get_data_cells_filter_response
    import capo_lakeformation.types.get_data_lake_principal_request
    import capo_lakeformation.types.get_data_lake_principal_response
    import capo_lakeformation.types.get_data_lake_settings_request
    import capo_lakeformation.types.get_data_lake_settings_response
    import capo_lakeformation.types.get_effective_permissions_for_path_request
    import capo_lakeformation.types.get_effective_permissions_for_path_response
    import capo_lakeformation.types.get_lf_tag_expression_request
    import capo_lakeformation.types.get_lf_tag_expression_response
    import capo_lakeformation.types.get_lf_tag_request
    import capo_lakeformation.types.get_lf_tag_response
    import capo_lakeformation.types.get_query_state_request
    import capo_lakeformation.types.get_query_state_request_query_id_string
    import capo_lakeformation.types.get_query_state_response
    import capo_lakeformation.types.get_query_statistics_request
    import capo_lakeformation.types.get_query_statistics_request_query_id_string
    import capo_lakeformation.types.get_query_statistics_response
    import capo_lakeformation.types.get_resource_lf_tags_request
    import capo_lakeformation.types.get_resource_lf_tags_response
    import capo_lakeformation.types.get_table_objects_request
    import capo_lakeformation.types.get_table_objects_response
    import capo_lakeformation.types.get_temporary_data_location_credentials_request
    import capo_lakeformation.types.get_temporary_data_location_credentials_response
    import capo_lakeformation.types.get_temporary_glue_partition_credentials_request
    import capo_lakeformation.types.get_temporary_glue_partition_credentials_response
    import capo_lakeformation.types.get_temporary_glue_table_credentials_request
    import capo_lakeformation.types.get_temporary_glue_table_credentials_response
    import capo_lakeformation.types.get_work_unit_results_request
    import capo_lakeformation.types.get_work_unit_results_request_query_id_string
    import capo_lakeformation.types.get_work_unit_results_request_work_unit_id_long
    import capo_lakeformation.types.get_work_unit_results_response
    import capo_lakeformation.types.get_work_units_request
    import capo_lakeformation.types.get_work_units_request_query_id_string
    import capo_lakeformation.types.get_work_units_response
    import capo_lakeformation.types.grant_permissions_request
    import capo_lakeformation.types.grant_permissions_response
    import capo_lakeformation.types.iam_role_arn
    import capo_lakeformation.types.iamsaml_provider_arn
    import capo_lakeformation.types.identity_center_instance_arn
    import capo_lakeformation.types.lf_tag_expression
    import capo_lakeformation.types.lf_tag_key
    import capo_lakeformation.types.lf_tag_pair
    import capo_lakeformation.types.lf_tags_list
    import capo_lakeformation.types.list_data_cells_filter_request
    import capo_lakeformation.types.list_data_cells_filter_response
    import capo_lakeformation.types.list_lake_formation_opt_ins_request
    import capo_lakeformation.types.list_lake_formation_opt_ins_response
    import capo_lakeformation.types.list_lf_tag_expressions_request
    import capo_lakeformation.types.list_lf_tag_expressions_response
    import capo_lakeformation.types.list_lf_tags_request
    import capo_lakeformation.types.list_lf_tags_response
    import capo_lakeformation.types.list_permissions_request
    import capo_lakeformation.types.list_permissions_response
    import capo_lakeformation.types.list_resources_request
    import capo_lakeformation.types.list_resources_response
    import capo_lakeformation.types.list_table_storage_optimizers_request
    import capo_lakeformation.types.list_table_storage_optimizers_response
    import capo_lakeformation.types.list_transactions_request
    import capo_lakeformation.types.list_transactions_response
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.nullable_boolean
    import capo_lakeformation.types.optimizer_type
    import capo_lakeformation.types.page_size
    import capo_lakeformation.types.partition_value_list
    import capo_lakeformation.types.path_string
    import capo_lakeformation.types.path_string_list
    import capo_lakeformation.types.permission_list
    import capo_lakeformation.types.permission_type_list
    import capo_lakeformation.types.predicate_string
    import capo_lakeformation.types.put_data_lake_settings_request
    import capo_lakeformation.types.put_data_lake_settings_response
    import capo_lakeformation.types.query_planning_context
    import capo_lakeformation.types.query_session_context
    import capo_lakeformation.types.register_resource_request
    import capo_lakeformation.types.register_resource_response
    import capo_lakeformation.types.remove_lf_tags_from_resource_request
    import capo_lakeformation.types.remove_lf_tags_from_resource_response
    import capo_lakeformation.types.resource
    import capo_lakeformation.types.resource_arn_string
    import capo_lakeformation.types.resource_share_type
    import capo_lakeformation.types.revoke_permissions_request
    import capo_lakeformation.types.revoke_permissions_response
    import capo_lakeformation.types.saml_assertion_string
    import capo_lakeformation.types.search_databases_by_lf_tags_request
    import capo_lakeformation.types.search_databases_by_lf_tags_response
    import capo_lakeformation.types.search_page_size
    import capo_lakeformation.types.search_tables_by_lf_tags_request
    import capo_lakeformation.types.search_tables_by_lf_tags_response
    import capo_lakeformation.types.service_integration_list
    import capo_lakeformation.types.start_query_planning_request
    import capo_lakeformation.types.start_query_planning_response
    import capo_lakeformation.types.start_transaction_request
    import capo_lakeformation.types.start_transaction_response
    import capo_lakeformation.types.storage_optimizer_config_map
    import capo_lakeformation.types.synthetic_get_work_unit_results_request_work_unit_token_string
    import capo_lakeformation.types.synthetic_start_query_planning_request_query_string
    import capo_lakeformation.types.table_resource
    import capo_lakeformation.types.tag_value_list
    import capo_lakeformation.types.tagged_database
    import capo_lakeformation.types.tagged_table
    import capo_lakeformation.types.timestamp
    import capo_lakeformation.types.token
    import capo_lakeformation.types.token_string
    import capo_lakeformation.types.transaction_id_string
    import capo_lakeformation.types.transaction_status_filter
    import capo_lakeformation.types.transaction_type
    import capo_lakeformation.types.true_false_string
    import capo_lakeformation.types.update_data_cells_filter_request
    import capo_lakeformation.types.update_data_cells_filter_response
    import capo_lakeformation.types.update_lake_formation_identity_center_configuration_request
    import capo_lakeformation.types.update_lake_formation_identity_center_configuration_response
    import capo_lakeformation.types.update_lf_tag_expression_request
    import capo_lakeformation.types.update_lf_tag_expression_response
    import capo_lakeformation.types.update_lf_tag_request
    import capo_lakeformation.types.update_lf_tag_response
    import capo_lakeformation.types.update_resource_request
    import capo_lakeformation.types.update_resource_response
    import capo_lakeformation.types.update_table_objects_request
    import capo_lakeformation.types.update_table_objects_response
    import capo_lakeformation.types.update_table_storage_optimizer_request
    import capo_lakeformation.types.update_table_storage_optimizer_response
    import capo_lakeformation.types.virtual_object_list
    import capo_lakeformation.types.work_unit_range
    import capo_lakeformation.types.write_operation_list


class LakeFormationClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class LakeFormationClient:
    """A client for the ``LakeFormation`` service.

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
        self._config = LakeFormationClientConfig(
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
        self, config_overrides: Optional[LakeFormationClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: LakeFormationClientConfig = config_overrides or {}
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

    def add_lf_tags_to_resource(
        self,
        resource: "capo_lakeformation.types.resource.Resource",
        lf_tags: "capo_lakeformation.types.lf_tags_list.LFTagsList",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.add_lf_tags_to_resource_response.AddLFTagsToResourceResponse":
        """<p>Attaches one or more LF-tags to an existing resource.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            resource: <p>The database, table, or column resource to which to attach an LF-tag.</p>
            lf_tags: <p>The LF-tags to attach to the resource.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.add_lf_tags_to_resource_request.AddLFTagsToResourceRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.add_lf_tags_to_resource_response.AddLFTagsToResourceResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.add_lf_tags_to_resource

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.add_lf_tags_to_resource.add_lf_tags_to_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.add_lf_tags_to_resource_request.AddLFTagsToResourceRequest = {
            "resource": resource,
            "lf_tags": lf_tags,
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def assume_decorated_role_with_saml(
        self,
        saml_assertion: "capo_lakeformation.types.saml_assertion_string.SAMLAssertionString",
        role_arn: "capo_lakeformation.types.iam_role_arn.IAMRoleArn",
        principal_arn: "capo_lakeformation.types.iamsaml_provider_arn.IAMSAMLProviderArn",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        duration_seconds: Optional[
            "capo_lakeformation.types.credential_timeout_duration_second_integer.CredentialTimeoutDurationSecondInteger"
        ] = None,
    ) -> "capo_lakeformation.types.assume_decorated_role_with_saml_response.AssumeDecoratedRoleWithSAMLResponse":
        """<p>Allows a caller to assume an IAM role decorated as the SAML user specified in the SAML assertion included in the request. This decoration allows Lake Formation to enforce access policies against the SAML users and groups. This API operation requires SAML federation setup in the caller’s account as it can only be called with valid SAML assertions. Lake Formation does not scope down the permission of the assumed role. All permissions attached to the role via the SAML federation setup will be included in the role session. </p> <p> This decorated role is expected to access data in Amazon S3 by getting temporary access from Lake Formation which is authorized via the virtual API <code>GetDataAccess</code>. Therefore, all SAML roles that can be assumed via <code>AssumeDecoratedRoleWithSAML</code> must at a minimum include <code>lakeformation:GetDataAccess</code> in their role policies. A typical IAM policy attached to such a role would include the following actions: </p> <ul> <li> <p>glue:*Database*</p> </li> <li> <p>glue:*Table*</p> </li> <li> <p>glue:*Partition*</p> </li> <li> <p>glue:*UserDefinedFunction*</p> </li> <li> <p>lakeformation:GetDataAccess</p> </li> </ul>

        Args:
            saml_assertion: <p>A SAML assertion consisting of an assertion statement for the user who needs temporary credentials. This must match the SAML assertion that was issued to IAM. This must be Base64 encoded.</p>
            role_arn: <p>The role that represents an IAM principal whose scope down policy allows it to call credential vending APIs such as <code>GetTemporaryTableCredentials</code>. The caller must also have iam:PassRole permission on this role. </p>
            principal_arn: <p>The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.</p>
            duration_seconds: <p>The time period, between 900 and 43,200 seconds, for the timeout of the temporary credentials.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.assume_decorated_role_with_saml_request.AssumeDecoratedRoleWithSAMLRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.assume_decorated_role_with_saml_response.AssumeDecoratedRoleWithSAMLResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.assume_decorated_role_with_saml

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.assume_decorated_role_with_saml.assume_decorated_role_with_saml(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.assume_decorated_role_with_saml_request.AssumeDecoratedRoleWithSAMLRequest = {
            "saml_assertion": saml_assertion,
            "role_arn": role_arn,
            "principal_arn": principal_arn,
        }
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_grant_permissions(
        self,
        entries: "capo_lakeformation.types.batch_permissions_request_entry_list.BatchPermissionsRequestEntryList",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.batch_grant_permissions_response.BatchGrantPermissionsResponse":
        """<p>Batch operation to grant permissions to the principal.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            entries: <p>A list of up to 20 entries for resource permissions to be granted by batch operation to the principal.</p>

        Raises:
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.batch_grant_permissions_request.BatchGrantPermissionsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.batch_grant_permissions_response.BatchGrantPermissionsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.batch_grant_permissions

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.batch_grant_permissions.batch_grant_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.batch_grant_permissions_request.BatchGrantPermissionsRequest = {
            "entries": entries
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_revoke_permissions(
        self,
        entries: "capo_lakeformation.types.batch_permissions_request_entry_list.BatchPermissionsRequestEntryList",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.batch_revoke_permissions_response.BatchRevokePermissionsResponse":
        """<p>Batch operation to revoke permissions from the principal.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            entries: <p>A list of up to 20 entries for resource permissions to be revoked by batch operation to the principal.</p>

        Raises:
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.batch_revoke_permissions_request.BatchRevokePermissionsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.batch_revoke_permissions_response.BatchRevokePermissionsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.batch_revoke_permissions

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.batch_revoke_permissions.batch_revoke_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.batch_revoke_permissions_request.BatchRevokePermissionsRequest = {
            "entries": entries
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_transaction(
        self,
        transaction_id: "capo_lakeformation.types.transaction_id_string.TransactionIdString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> (
        "capo_lakeformation.types.cancel_transaction_response.CancelTransactionResponse"
    ):
        """<p>Attempts to cancel the specified transaction. Returns an exception if the transaction was previously committed.</p>

        Args:
            transaction_id: <p>The transaction to cancel.</p>

        Raises:
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.transaction_commit_in_progress_exception.TransactionCommitInProgressException: <p>Contains details about an error related to a transaction commit that was in progress.</p>
            capo_lakeformation.errors.transaction_committed_exception.TransactionCommittedException: <p>Contains details about an error where the specified transaction has already been committed and cannot be used for <code>UpdateTableObjects</code>.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.cancel_transaction_request.CancelTransactionRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.cancel_transaction_response.CancelTransactionResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.cancel_transaction

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.cancel_transaction.cancel_transaction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.cancel_transaction_request.CancelTransactionRequest = {
            "transaction_id": transaction_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def commit_transaction(
        self,
        transaction_id: "capo_lakeformation.types.transaction_id_string.TransactionIdString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> (
        "capo_lakeformation.types.commit_transaction_response.CommitTransactionResponse"
    ):
        """<p>Attempts to commit the specified transaction. Returns an exception if the transaction was previously aborted. This API action is idempotent if called multiple times for the same transaction.</p>

        Args:
            transaction_id: <p>The transaction to commit.</p>

        Raises:
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.transaction_canceled_exception.TransactionCanceledException: <p>Contains details about an error related to a transaction that was cancelled.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.commit_transaction_request.CommitTransactionRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.commit_transaction_response.CommitTransactionResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.commit_transaction

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.commit_transaction.commit_transaction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.commit_transaction_request.CommitTransactionRequest = {
            "transaction_id": transaction_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_cells_filter(
        self,
        table_data: "capo_lakeformation.types.data_cells_filter.DataCellsFilter",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> "capo_lakeformation.types.create_data_cells_filter_response.CreateDataCellsFilterResponse":
        """<p>Creates a data cell filter to allow one to grant access to certain columns on certain rows.</p>

        Args:
            table_data: <p>A <code>DataCellsFilter</code> structure containing information about the data cells filter.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.already_exists_exception.AlreadyExistsException: <p>A resource to be created or added already exists.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.resource_number_limit_exceeded_exception.ResourceNumberLimitExceededException: <p>A resource numerical limit was exceeded.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.create_data_cells_filter_request.CreateDataCellsFilterRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.create_data_cells_filter_response.CreateDataCellsFilterResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.create_data_cells_filter

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.create_data_cells_filter.create_data_cells_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.create_data_cells_filter_request.CreateDataCellsFilterRequest = {
            "table_data": table_data
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_lake_formation_identity_center_configuration(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        instance_arn: Optional[
            "capo_lakeformation.types.identity_center_instance_arn.IdentityCenterInstanceArn"
        ] = None,
        external_filtering: Optional[
            "capo_lakeformation.types.external_filtering_configuration.ExternalFilteringConfiguration"
        ] = None,
        share_recipients: Optional[
            "capo_lakeformation.types.data_lake_principal_list.DataLakePrincipalList"
        ] = None,
        service_integrations: Optional[
            "capo_lakeformation.types.service_integration_list.ServiceIntegrationList"
        ] = None,
    ) -> "capo_lakeformation.types.create_lake_formation_identity_center_configuration_response.CreateLakeFormationIdentityCenterConfigurationResponse":
        """<p>Creates an IAM Identity Center connection with Lake Formation to allow IAM Identity Center users and groups to access Data Catalog resources.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, view definitions, and other control information to manage your Lake Formation environment.</p>
            instance_arn: <p>The ARN of the IAM Identity Center instance for which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces in the Amazon Web Services General Reference.</p>
            external_filtering: <p>A list of the account IDs of Amazon Web Services accounts of third-party applications that are allowed to access data managed by Lake Formation.</p>
            share_recipients: <p>A list of Amazon Web Services account IDs and/or Amazon Web Services organization/organizational unit ARNs that are allowed to access data managed by Lake Formation. </p> <p>If the <code>ShareRecipients</code> list includes valid values, a resource share is created with the principals you want to have access to the resources.</p> <p>If the <code>ShareRecipients</code> value is null or the list is empty, no resource share is created.</p>
            service_integrations: <p>A list of service integrations for enabling trusted identity propagation with external services such as Redshift.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.already_exists_exception.AlreadyExistsException: <p>A resource to be created or added already exists.</p>
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.create_lake_formation_identity_center_configuration_request.CreateLakeFormationIdentityCenterConfigurationRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.create_lake_formation_identity_center_configuration_response.CreateLakeFormationIdentityCenterConfigurationResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.create_lake_formation_identity_center_configuration

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.create_lake_formation_identity_center_configuration.create_lake_formation_identity_center_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.create_lake_formation_identity_center_configuration_request.CreateLakeFormationIdentityCenterConfigurationRequest = {}
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if instance_arn is not None:
            input_["instance_arn"] = instance_arn
        if external_filtering is not None:
            input_["external_filtering"] = external_filtering
        if share_recipients is not None:
            input_["share_recipients"] = share_recipients
        if service_integrations is not None:
            input_["service_integrations"] = service_integrations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_lake_formation_opt_in(
        self,
        principal: "capo_lakeformation.types.data_lake_principal.DataLakePrincipal",
        resource: "capo_lakeformation.types.resource.Resource",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        condition: Optional["capo_lakeformation.types.condition.Condition"] = None,
    ) -> "capo_lakeformation.types.create_lake_formation_opt_in_response.CreateLakeFormationOptInResponse":
        """<p>Enforce Lake Formation permissions for the given databases, tables, and principals.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.resource_number_limit_exceeded_exception.ResourceNumberLimitExceededException: <p>A resource numerical limit was exceeded.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.create_lake_formation_opt_in_request.CreateLakeFormationOptInRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.create_lake_formation_opt_in_response.CreateLakeFormationOptInResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.create_lake_formation_opt_in

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.create_lake_formation_opt_in.create_lake_formation_opt_in(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.create_lake_formation_opt_in_request.CreateLakeFormationOptInRequest = {
            "principal": principal,
            "resource": resource,
        }
        if condition is not None:
            input_["condition"] = condition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_lf_tag(
        self,
        tag_key: "capo_lakeformation.types.lf_tag_key.LFTagKey",
        tag_values: "capo_lakeformation.types.tag_value_list.TagValueList",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.create_lf_tag_response.CreateLFTagResponse":
        """<p>Creates an LF-tag with the specified name and values.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            tag_key: <p>The key-name for the LF-tag.</p>
            tag_values: <p>A list of possible values an attribute can take.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.resource_number_limit_exceeded_exception.ResourceNumberLimitExceededException: <p>A resource numerical limit was exceeded.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.create_lf_tag_request.CreateLFTagRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.create_lf_tag_response.CreateLFTagResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.create_lf_tag

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.create_lf_tag.create_lf_tag(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.create_lf_tag_request.CreateLFTagRequest = {
            "tag_key": tag_key,
            "tag_values": tag_values,
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_lf_tag_expression(
        self,
        name: "capo_lakeformation.types.name_string.NameString",
        expression: "capo_lakeformation.types.expression.Expression",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        description: Optional[
            "capo_lakeformation.types.description_string.DescriptionString"
        ] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.create_lf_tag_expression_response.CreateLFTagExpressionResponse":
        """<p>Creates a new LF-Tag expression with the provided name, description, catalog ID, and expression body. This call fails if a LF-Tag expression with the same name already exists in the caller’s account or if the underlying LF-Tags don't exist. To call this API operation, caller needs the following Lake Formation permissions:</p> <p> <code>CREATE_LF_TAG_EXPRESSION</code> on the root catalog resource.</p> <p> <code>GRANT_WITH_LF_TAG_EXPRESSION</code> on all underlying LF-Tag key:value pairs included in the expression. </p>

        Args:
            name: <p>A name for the expression.</p>
            description: <p>A description with information about the LF-Tag expression.</p>
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            expression: <p>A list of LF-Tag conditions (key-value pairs).</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.resource_number_limit_exceeded_exception.ResourceNumberLimitExceededException: <p>A resource numerical limit was exceeded.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.create_lf_tag_expression_request.CreateLFTagExpressionRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.create_lf_tag_expression_response.CreateLFTagExpressionResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.create_lf_tag_expression

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.create_lf_tag_expression.create_lf_tag_expression(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.create_lf_tag_expression_request.CreateLFTagExpressionRequest = {
            "name": name,
            "expression": expression,
        }
        if description is not None:
            input_["description"] = description
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_cells_filter(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        table_catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        database_name: Optional[
            "capo_lakeformation.types.name_string.NameString"
        ] = None,
        table_name: Optional["capo_lakeformation.types.name_string.NameString"] = None,
        name: Optional["capo_lakeformation.types.name_string.NameString"] = None,
    ) -> "capo_lakeformation.types.delete_data_cells_filter_response.DeleteDataCellsFilterResponse":
        """<p>Deletes a data cell filter.</p>

        Args:
            table_catalog_id: <p>The ID of the catalog to which the table belongs.</p>
            database_name: <p>A database in the Glue Data Catalog.</p>
            table_name: <p>A table in the database.</p>
            name: <p>The name given by the user to the data filter cell.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.delete_data_cells_filter_request.DeleteDataCellsFilterRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.delete_data_cells_filter_response.DeleteDataCellsFilterResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.delete_data_cells_filter

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.delete_data_cells_filter.delete_data_cells_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.delete_data_cells_filter_request.DeleteDataCellsFilterRequest = {}
        if table_catalog_id is not None:
            input_["table_catalog_id"] = table_catalog_id
        if database_name is not None:
            input_["database_name"] = database_name
        if table_name is not None:
            input_["table_name"] = table_name
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_lake_formation_identity_center_configuration(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.delete_lake_formation_identity_center_configuration_response.DeleteLakeFormationIdentityCenterConfigurationResponse":
        """<p>Deletes an IAM Identity Center connection with Lake Formation.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, view definition, and other control information to manage your Lake Formation environment.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.delete_lake_formation_identity_center_configuration_request.DeleteLakeFormationIdentityCenterConfigurationRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.delete_lake_formation_identity_center_configuration_response.DeleteLakeFormationIdentityCenterConfigurationResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.delete_lake_formation_identity_center_configuration

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.delete_lake_formation_identity_center_configuration.delete_lake_formation_identity_center_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.delete_lake_formation_identity_center_configuration_request.DeleteLakeFormationIdentityCenterConfigurationRequest = {}
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_lake_formation_opt_in(
        self,
        principal: "capo_lakeformation.types.data_lake_principal.DataLakePrincipal",
        resource: "capo_lakeformation.types.resource.Resource",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        condition: Optional["capo_lakeformation.types.condition.Condition"] = None,
    ) -> "capo_lakeformation.types.delete_lake_formation_opt_in_response.DeleteLakeFormationOptInResponse":
        """<p>Remove the Lake Formation permissions enforcement of the given databases, tables, and principals.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.delete_lake_formation_opt_in_request.DeleteLakeFormationOptInRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.delete_lake_formation_opt_in_response.DeleteLakeFormationOptInResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.delete_lake_formation_opt_in

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.delete_lake_formation_opt_in.delete_lake_formation_opt_in(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.delete_lake_formation_opt_in_request.DeleteLakeFormationOptInRequest = {
            "principal": principal,
            "resource": resource,
        }
        if condition is not None:
            input_["condition"] = condition

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_lf_tag(
        self,
        tag_key: "capo_lakeformation.types.lf_tag_key.LFTagKey",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.delete_lf_tag_response.DeleteLFTagResponse":
        """<p> Deletes an LF-tag by its key name. The operation fails if the specified tag key doesn't exist. When you delete an LF-Tag: </p> <ul> <li> <p>The associated LF-Tag policy becomes invalid.</p> </li> <li> <p> Resources that had this tag assigned will no longer have the tag policy applied to them.</p> </li> </ul>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            tag_key: <p>The key-name for the LF-tag to delete.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.delete_lf_tag_request.DeleteLFTagRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.delete_lf_tag_response.DeleteLFTagResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.delete_lf_tag

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.delete_lf_tag.delete_lf_tag(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.delete_lf_tag_request.DeleteLFTagRequest = {
            "tag_key": tag_key
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_lf_tag_expression(
        self,
        name: "capo_lakeformation.types.name_string.NameString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.delete_lf_tag_expression_response.DeleteLFTagExpressionResponse":
        """<p>Deletes the LF-Tag expression. The caller must be a data lake admin or have <code>DROP</code> permissions on the LF-Tag expression. Deleting a LF-Tag expression will also delete all <code>LFTagPolicy</code> permissions referencing the LF-Tag expression.</p>

        Args:
            name: <p>The name for the LF-Tag expression.</p>
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID in which the LF-Tag expression is saved. </p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.delete_lf_tag_expression_request.DeleteLFTagExpressionRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.delete_lf_tag_expression_response.DeleteLFTagExpressionResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.delete_lf_tag_expression

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.delete_lf_tag_expression.delete_lf_tag_expression(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.delete_lf_tag_expression_request.DeleteLFTagExpressionRequest = {
            "name": name
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_objects_on_cancel(
        self,
        database_name: "capo_lakeformation.types.name_string.NameString",
        table_name: "capo_lakeformation.types.name_string.NameString",
        transaction_id: "capo_lakeformation.types.transaction_id_string.TransactionIdString",
        objects: "capo_lakeformation.types.virtual_object_list.VirtualObjectList",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.delete_objects_on_cancel_response.DeleteObjectsOnCancelResponse":
        """<p>For a specific governed table, provides a list of Amazon S3 objects that will be written during the current transaction and that can be automatically deleted if the transaction is canceled. Without this call, no Amazon S3 objects are automatically deleted when a transaction cancels. </p> <p> The Glue ETL library function <code>write_dynamic_frame.from_catalog()</code> includes an option to automatically call <code>DeleteObjectsOnCancel</code> before writes. For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/transactions-data-operations.html#rolling-back-writes">Rolling Back Amazon S3 Writes</a>. </p>

        Args:
            catalog_id: <p>The Glue data catalog that contains the governed table. Defaults to the current account ID.</p>
            database_name: <p>The database that contains the governed table.</p>
            table_name: <p>The name of the governed table.</p>
            transaction_id: <p>ID of the transaction that the writes occur in.</p>
            objects: <p>A list of VirtualObject structures, which indicates the Amazon S3 objects to be deleted if the transaction cancels.</p>

        Raises:
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.resource_not_ready_exception.ResourceNotReadyException: <p>Contains details about an error related to a resource which is not ready for a transaction.</p>
            capo_lakeformation.errors.transaction_canceled_exception.TransactionCanceledException: <p>Contains details about an error related to a transaction that was cancelled.</p>
            capo_lakeformation.errors.transaction_committed_exception.TransactionCommittedException: <p>Contains details about an error where the specified transaction has already been committed and cannot be used for <code>UpdateTableObjects</code>.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.delete_objects_on_cancel_request.DeleteObjectsOnCancelRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.delete_objects_on_cancel_response.DeleteObjectsOnCancelResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.delete_objects_on_cancel

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.delete_objects_on_cancel.delete_objects_on_cancel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.delete_objects_on_cancel_request.DeleteObjectsOnCancelRequest = {
            "database_name": database_name,
            "table_name": table_name,
            "transaction_id": transaction_id,
            "objects": objects,
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_resource(
        self,
        resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> "capo_lakeformation.types.deregister_resource_response.DeregisterResourceResponse":
        """<p>Deregisters the resource as managed by the Data Catalog.</p> <p>When you deregister a path, Lake Formation removes the path from the inline policy attached to your service-linked role.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to deregister.</p>

        Raises:
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.deregister_resource_request.DeregisterResourceRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.deregister_resource_response.DeregisterResourceResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.deregister_resource

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.deregister_resource.deregister_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.deregister_resource_request.DeregisterResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_lake_formation_identity_center_configuration(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.describe_lake_formation_identity_center_configuration_response.DescribeLakeFormationIdentityCenterConfigurationResponse":
        """<p>Retrieves the instance ARN and application ARN for the connection.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.describe_lake_formation_identity_center_configuration_request.DescribeLakeFormationIdentityCenterConfigurationRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.describe_lake_formation_identity_center_configuration_response.DescribeLakeFormationIdentityCenterConfigurationResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.describe_lake_formation_identity_center_configuration

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.describe_lake_formation_identity_center_configuration.describe_lake_formation_identity_center_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.describe_lake_formation_identity_center_configuration_request.DescribeLakeFormationIdentityCenterConfigurationRequest = {}
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_resource(
        self,
        resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> "capo_lakeformation.types.describe_resource_response.DescribeResourceResponse":
        """<p>Retrieves the current data access role for the given resource registered in Lake Formation.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>

        Raises:
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.describe_resource_request.DescribeResourceRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.describe_resource_response.DescribeResourceResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.describe_resource

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.describe_resource.describe_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.describe_resource_request.DescribeResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_transaction(
        self,
        transaction_id: "capo_lakeformation.types.transaction_id_string.TransactionIdString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> "capo_lakeformation.types.describe_transaction_response.DescribeTransactionResponse":
        """<p>Returns the details of a single transaction.</p>

        Args:
            transaction_id: <p>The transaction for which to return status.</p>

        Raises:
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.describe_transaction_request.DescribeTransactionRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.describe_transaction_response.DescribeTransactionResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.describe_transaction

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.describe_transaction.describe_transaction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.describe_transaction_request.DescribeTransactionRequest = {
            "transaction_id": transaction_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def extend_transaction(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        transaction_id: Optional[
            "capo_lakeformation.types.transaction_id_string.TransactionIdString"
        ] = None,
    ) -> (
        "capo_lakeformation.types.extend_transaction_response.ExtendTransactionResponse"
    ):
        """<p>Indicates to the service that the specified transaction is still active and should not be treated as idle and aborted.</p> <p>Write transactions that remain idle for a long period are automatically aborted unless explicitly extended.</p>

        Args:
            transaction_id: <p>The transaction to extend.</p>

        Raises:
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.transaction_canceled_exception.TransactionCanceledException: <p>Contains details about an error related to a transaction that was cancelled.</p>
            capo_lakeformation.errors.transaction_commit_in_progress_exception.TransactionCommitInProgressException: <p>Contains details about an error related to a transaction commit that was in progress.</p>
            capo_lakeformation.errors.transaction_committed_exception.TransactionCommittedException: <p>Contains details about an error where the specified transaction has already been committed and cannot be used for <code>UpdateTableObjects</code>.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.extend_transaction_request.ExtendTransactionRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.extend_transaction_response.ExtendTransactionResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.extend_transaction

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.extend_transaction.extend_transaction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.extend_transaction_request.ExtendTransactionRequest = {}
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_cells_filter(
        self,
        table_catalog_id: "capo_lakeformation.types.catalog_id_string.CatalogIdString",
        database_name: "capo_lakeformation.types.name_string.NameString",
        table_name: "capo_lakeformation.types.name_string.NameString",
        name: "capo_lakeformation.types.name_string.NameString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> "capo_lakeformation.types.get_data_cells_filter_response.GetDataCellsFilterResponse":
        """<p>Returns a data cells filter.</p>

        Args:
            table_catalog_id: <p>The ID of the catalog to which the table belongs.</p>
            database_name: <p>A database in the Glue Data Catalog.</p>
            table_name: <p>A table in the database.</p>
            name: <p>The name given by the user to the data filter cell.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_data_cells_filter_request.GetDataCellsFilterRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_data_cells_filter_response.GetDataCellsFilterResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_data_cells_filter

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_data_cells_filter.get_data_cells_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_data_cells_filter_request.GetDataCellsFilterRequest = {
            "table_catalog_id": table_catalog_id,
            "database_name": database_name,
            "table_name": table_name,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_lake_principal(
        self, *, config_overrides: Optional[LakeFormationClientConfig] = None
    ) -> "capo_lakeformation.types.get_data_lake_principal_response.GetDataLakePrincipalResponse":
        """<p>Returns the identity of the invoking principal.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_data_lake_principal_request.GetDataLakePrincipalRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_data_lake_principal_response.GetDataLakePrincipalResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_data_lake_principal

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_data_lake_principal.get_data_lake_principal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_data_lake_principal_request.GetDataLakePrincipalRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_lake_settings(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.get_data_lake_settings_response.GetDataLakeSettingsResponse":
        """<p>Retrieves the list of the data lake administrators of a Lake Formation-managed data lake. </p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>

        Raises:
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_data_lake_settings_request.GetDataLakeSettingsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_data_lake_settings_response.GetDataLakeSettingsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_data_lake_settings

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_data_lake_settings.get_data_lake_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_data_lake_settings_request.GetDataLakeSettingsRequest = {}
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_effective_permissions_for_path(
        self,
        resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
    ) -> "capo_lakeformation.types.get_effective_permissions_for_path_response.GetEffectivePermissionsForPathResponse":
        """<p>Returns the Lake Formation permissions for a specified table or database resource located at a path in Amazon S3. <code>GetEffectivePermissionsForPath</code> will not return databases and tables if the catalog is encrypted.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to get permissions.</p>
            next_token: <p>A continuation token, if this is not the first call to retrieve this list.</p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_effective_permissions_for_path_request.GetEffectivePermissionsForPathRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_effective_permissions_for_path_response.GetEffectivePermissionsForPathResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_effective_permissions_for_path

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_effective_permissions_for_path.get_effective_permissions_for_path(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_effective_permissions_for_path_request.GetEffectivePermissionsForPathRequest = {
            "resource_arn": resource_arn
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
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

    def iter_get_effective_permissions_for_path(
        self,
        resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
    ) -> "Iterator[capo_lakeformation.types.get_effective_permissions_for_path_response.GetEffectivePermissionsForPathResponse]":
        _token = next_token
        while True:
            _response = self.get_effective_permissions_for_path(
                resource_arn,
                config_overrides=config_overrides,
                catalog_id=catalog_id,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_lf_tag(
        self,
        tag_key: "capo_lakeformation.types.lf_tag_key.LFTagKey",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.get_lf_tag_response.GetLFTagResponse":
        """<p>Returns an LF-tag definition.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            tag_key: <p>The key-name for the LF-tag.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_lf_tag_request.GetLFTagRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_lf_tag_response.GetLFTagResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_lf_tag

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_lf_tag.get_lf_tag(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_lf_tag_request.GetLFTagRequest = {
            "tag_key": tag_key
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_lf_tag_expression(
        self,
        name: "capo_lakeformation.types.name_string.NameString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.get_lf_tag_expression_response.GetLFTagExpressionResponse":
        """<p>Returns the details about the LF-Tag expression. The caller must be a data lake admin or must have <code>DESCRIBE</code> permission on the LF-Tag expression resource. </p>

        Args:
            name: <p>The name for the LF-Tag expression</p>
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_lf_tag_expression_request.GetLFTagExpressionRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_lf_tag_expression_response.GetLFTagExpressionResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_lf_tag_expression

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_lf_tag_expression.get_lf_tag_expression(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_lf_tag_expression_request.GetLFTagExpressionRequest = {
            "name": name
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_query_state(
        self,
        query_id: "capo_lakeformation.types.get_query_state_request_query_id_string.GetQueryStateRequestQueryIdString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> "capo_lakeformation.types.get_query_state_response.GetQueryStateResponse":
        """<p>Returns the state of a query previously submitted. Clients are expected to poll <code>GetQueryState</code> to monitor the current state of the planning before retrieving the work units. A query state is only visible to the principal that made the initial call to <code>StartQueryPlanning</code>.</p>

        Args:
            query_id: <p>The ID of the plan query operation.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_query_state_request.GetQueryStateRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_query_state_response.GetQueryStateResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_query_state

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_query_state.get_query_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_query_state_request.GetQueryStateRequest = {
            "query_id": query_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_query_statistics(
        self,
        query_id: "capo_lakeformation.types.get_query_statistics_request_query_id_string.GetQueryStatisticsRequestQueryIdString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> "capo_lakeformation.types.get_query_statistics_response.GetQueryStatisticsResponse":
        """<p>Retrieves statistics on the planning and execution of a query.</p>

        Args:
            query_id: <p>The ID of the plan query operation.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.expired_exception.ExpiredException: <p>Contains details about an error where the query request expired.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.statistics_not_ready_yet_exception.StatisticsNotReadyYetException: <p>Contains details about an error related to statistics not being ready.</p>
            capo_lakeformation.errors.throttled_exception.ThrottledException: <p>Contains details about an error where the query request was throttled.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_query_statistics_request.GetQueryStatisticsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_query_statistics_response.GetQueryStatisticsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_query_statistics

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_query_statistics.get_query_statistics(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_query_statistics_request.GetQueryStatisticsRequest = {
            "query_id": query_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_lf_tags(
        self,
        resource: "capo_lakeformation.types.resource.Resource",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        show_assigned_lf_tags: Optional[
            "capo_lakeformation.types.boolean_nullable.BooleanNullable"
        ] = None,
    ) -> "capo_lakeformation.types.get_resource_lf_tags_response.GetResourceLFTagsResponse":
        """<p>Returns the LF-tags applied to a resource.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            resource: <p>The database, table, or column resource for which you want to return LF-tags.</p>
            show_assigned_lf_tags: <p>Indicates whether to show the assigned LF-tags.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.glue_encryption_exception.GlueEncryptionException: <p>An encryption operation failed.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_resource_lf_tags_request.GetResourceLFTagsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_resource_lf_tags_response.GetResourceLFTagsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_resource_lf_tags

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_resource_lf_tags.get_resource_lf_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_resource_lf_tags_request.GetResourceLFTagsRequest = {
            "resource": resource
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if show_assigned_lf_tags is not None:
            input_["show_assigned_lf_tags"] = show_assigned_lf_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_table_objects(
        self,
        database_name: "capo_lakeformation.types.name_string.NameString",
        table_name: "capo_lakeformation.types.name_string.NameString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        transaction_id: Optional[
            "capo_lakeformation.types.transaction_id_string.TransactionIdString"
        ] = None,
        query_as_of_time: Optional[
            "capo_lakeformation.types.timestamp.Timestamp"
        ] = None,
        partition_predicate: Optional[
            "capo_lakeformation.types.predicate_string.PredicateString"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_lakeformation.types.token_string.TokenString"
        ] = None,
    ) -> "capo_lakeformation.types.get_table_objects_response.GetTableObjectsResponse":
        """<p>Returns the set of Amazon S3 objects that make up the specified governed table. A transaction ID or timestamp can be specified for time-travel queries.</p>

        Args:
            catalog_id: <p>The catalog containing the governed table. Defaults to the caller’s account.</p>
            database_name: <p>The database containing the governed table.</p>
            table_name: <p>The governed table for which to retrieve objects.</p>
            transaction_id: <p>The transaction ID at which to read the governed table contents. If this transaction has aborted, an error is returned. If not set, defaults to the most recent committed transaction. Cannot be specified along with <code>QueryAsOfTime</code>.</p>
            query_as_of_time: <p>The time as of when to read the governed table contents. If not set, the most recent transaction commit time is used. Cannot be specified along with <code>TransactionId</code>.</p>
            partition_predicate: <p>A predicate to filter the objects returned based on the partition keys defined in the governed table.</p> <ul> <li> <p>The comparison operators supported are: =, >, <, >=, <=</p> </li> <li> <p>The logical operators supported are: AND</p> </li> <li> <p>The data types supported are integer, long, date(yyyy-MM-dd), timestamp(yyyy-MM-dd HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss"), string and decimal.</p> </li> </ul>
            max_results: <p>Specifies how many values to return in a page.</p>
            next_token: <p>A continuation token if this is not the first call to retrieve these objects.</p>

        Raises:
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.resource_not_ready_exception.ResourceNotReadyException: <p>Contains details about an error related to a resource which is not ready for a transaction.</p>
            capo_lakeformation.errors.transaction_canceled_exception.TransactionCanceledException: <p>Contains details about an error related to a transaction that was cancelled.</p>
            capo_lakeformation.errors.transaction_committed_exception.TransactionCommittedException: <p>Contains details about an error where the specified transaction has already been committed and cannot be used for <code>UpdateTableObjects</code>.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_table_objects_request.GetTableObjectsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_table_objects_response.GetTableObjectsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_table_objects

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_table_objects.get_table_objects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_table_objects_request.GetTableObjectsRequest = {
            "database_name": database_name,
            "table_name": table_name,
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id
        if query_as_of_time is not None:
            input_["query_as_of_time"] = query_as_of_time
        if partition_predicate is not None:
            input_["partition_predicate"] = partition_predicate
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

    def iter_get_table_objects(
        self,
        database_name: "capo_lakeformation.types.name_string.NameString",
        table_name: "capo_lakeformation.types.name_string.NameString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        transaction_id: Optional[
            "capo_lakeformation.types.transaction_id_string.TransactionIdString"
        ] = None,
        query_as_of_time: Optional[
            "capo_lakeformation.types.timestamp.Timestamp"
        ] = None,
        partition_predicate: Optional[
            "capo_lakeformation.types.predicate_string.PredicateString"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_lakeformation.types.token_string.TokenString"
        ] = None,
    ) -> "Iterator[capo_lakeformation.types.get_table_objects_response.GetTableObjectsResponse]":
        _token = next_token
        while True:
            _response = self.get_table_objects(
                database_name,
                table_name,
                config_overrides=config_overrides,
                catalog_id=catalog_id,
                transaction_id=transaction_id,
                query_as_of_time=query_as_of_time,
                partition_predicate=partition_predicate,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_temporary_data_location_credentials(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        duration_seconds: Optional[
            "capo_lakeformation.types.credential_timeout_duration_second_integer.CredentialTimeoutDurationSecondInteger"
        ] = None,
        audit_context: Optional[
            "capo_lakeformation.types.audit_context.AuditContext"
        ] = None,
        data_locations: Optional[
            "capo_lakeformation.types.path_string_list.PathStringList"
        ] = None,
        credentials_scope: Optional[
            "capo_lakeformation.types.credentials_scope.CredentialsScope"
        ] = None,
    ) -> "capo_lakeformation.types.get_temporary_data_location_credentials_response.GetTemporaryDataLocationCredentialsResponse":
        """<p>Allows a user or application in a secure environment to access data in a specific Amazon S3 location registered with Lake Formation by providing temporary scoped credentials that are limited to the requested data location and the caller's authorized access level.</p> <p> <code>GetDataAccess</code> is logged in CloudTrail whenever a principal requests temporary data location credentials to access data in a data lake location that is registered with Lake Formation.</p> <p> The API operation returns an error in the following scenarios:</p> <ul> <li> <p>The data location is not registered with Lake Formation. </p> </li> <li> <p>No Glue table is associated with the data location.</p> </li> <li> <p>The caller doesn't have required permissions on the associated table. The caller must have <code>SELECT</code> or <code>SUPER</code> permissions on the associated table, and credential vending for full table access must be enabled in the data lake settings. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/full-table-credential-vending.html">Application integration for full table access</a>.</p> </li> <li> <p>The data location is in a different Amazon Web Services Region. Lake Formation doesn't support cross-Region access when vending credentials for a data location. Lake Formation only supports Amazon S3 paths registered within the same Region as the API call. </p> </li> </ul>

        Args:
            duration_seconds: <p>The time period, between 900 and 43,200 seconds, for the timeout of the temporary credentials.</p>
            data_locations: <p>The Amazon S3 data location that you want to access.</p>
            credentials_scope: <p>The credential scope is determined by the caller's Lake Formation permission on the associated table. Credential scope can be either:</p> <ul> <li> <p>READ - Provides read-only access to the data location.</p> </li> <li> <p>READ_WRITE - Provides both read and write access to the data location.</p> </li> </ul>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.conflict_exception.ConflictException: <p>Multiple resources exist with the same Amazon S3 location</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.glue_encryption_exception.GlueEncryptionException: <p>An encryption operation failed.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_temporary_data_location_credentials_request.GetTemporaryDataLocationCredentialsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_temporary_data_location_credentials_response.GetTemporaryDataLocationCredentialsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_temporary_data_location_credentials

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_temporary_data_location_credentials.get_temporary_data_location_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_temporary_data_location_credentials_request.GetTemporaryDataLocationCredentialsRequest = {}
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if audit_context is not None:
            input_["audit_context"] = audit_context
        if data_locations is not None:
            input_["data_locations"] = data_locations
        if credentials_scope is not None:
            input_["credentials_scope"] = credentials_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_temporary_glue_partition_credentials(
        self,
        table_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString",
        partition: "capo_lakeformation.types.partition_value_list.PartitionValueList",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        permissions: Optional[
            "capo_lakeformation.types.permission_list.PermissionList"
        ] = None,
        duration_seconds: Optional[
            "capo_lakeformation.types.credential_timeout_duration_second_integer.CredentialTimeoutDurationSecondInteger"
        ] = None,
        audit_context: Optional[
            "capo_lakeformation.types.audit_context.AuditContext"
        ] = None,
        supported_permission_types: Optional[
            "capo_lakeformation.types.permission_type_list.PermissionTypeList"
        ] = None,
    ) -> "capo_lakeformation.types.get_temporary_glue_partition_credentials_response.GetTemporaryGluePartitionCredentialsResponse":
        """<p>This API is identical to <code>GetTemporaryTableCredentials</code> except that this is used when the target Data Catalog resource is of type Partition. Lake Formation restricts the permission of the vended credentials with the same scope down policy which restricts access to a single Amazon S3 prefix.</p>

        Args:
            table_arn: <p>The ARN of the partitions' table.</p>
            partition: <p>A list of partition values identifying a single partition.</p>
            permissions: <p>Filters the request based on the user having been granted a list of specified permissions on the requested resource(s).</p>
            duration_seconds: <p>The time period, between 900 and 21,600 seconds, for the timeout of the temporary credentials.</p>
            audit_context: <p>A structure representing context to access a resource (column names, query ID, etc).</p>
            supported_permission_types: <p>A list of supported permission types for the partition. Valid values are <code>COLUMN_PERMISSION</code> and <code>CELL_FILTER_PERMISSION</code>.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.permission_type_mismatch_exception.PermissionTypeMismatchException: <p>The engine does not support filtering data based on the enforced permissions. For example, if you call the <code>GetTemporaryGlueTableCredentials</code> operation with <code>SupportedPermissionType</code> equal to <code>ColumnPermission</code>, but cell-level permissions exist on the table, this exception is thrown.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_temporary_glue_partition_credentials_request.GetTemporaryGluePartitionCredentialsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_temporary_glue_partition_credentials_response.GetTemporaryGluePartitionCredentialsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_temporary_glue_partition_credentials

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_temporary_glue_partition_credentials.get_temporary_glue_partition_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_temporary_glue_partition_credentials_request.GetTemporaryGluePartitionCredentialsRequest = {
            "table_arn": table_arn,
            "partition": partition,
        }
        if permissions is not None:
            input_["permissions"] = permissions
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if audit_context is not None:
            input_["audit_context"] = audit_context
        if supported_permission_types is not None:
            input_["supported_permission_types"] = supported_permission_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_temporary_glue_table_credentials(
        self,
        table_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        permissions: Optional[
            "capo_lakeformation.types.permission_list.PermissionList"
        ] = None,
        duration_seconds: Optional[
            "capo_lakeformation.types.credential_timeout_duration_second_integer.CredentialTimeoutDurationSecondInteger"
        ] = None,
        audit_context: Optional[
            "capo_lakeformation.types.audit_context.AuditContext"
        ] = None,
        supported_permission_types: Optional[
            "capo_lakeformation.types.permission_type_list.PermissionTypeList"
        ] = None,
        s3_path: Optional["capo_lakeformation.types.path_string.PathString"] = None,
        query_session_context: Optional[
            "capo_lakeformation.types.query_session_context.QuerySessionContext"
        ] = None,
    ) -> "capo_lakeformation.types.get_temporary_glue_table_credentials_response.GetTemporaryGlueTableCredentialsResponse":
        """<p>Allows a caller in a secure environment to assume a role with permission to access Amazon S3. In order to vend such credentials, Lake Formation assumes the role associated with a registered location, for example an Amazon S3 bucket, with a scope down policy which restricts the access to a single prefix.</p> <p>To call this API, the role that the service assumes must have <code>lakeformation:GetDataAccess</code> permission on the resource.</p>

        Args:
            table_arn: <p>The ARN identifying a table in the Data Catalog for the temporary credentials request.</p>
            permissions: <p>Filters the request based on the user having been granted a list of specified permissions on the requested resource(s).</p>
            duration_seconds: <p>The time period, between 900 and 21,600 seconds, for the timeout of the temporary credentials.</p>
            audit_context: <p>A structure representing context to access a resource (column names, query ID, etc).</p>
            supported_permission_types: <p>A list of supported permission types for the table. Valid values are <code>COLUMN_PERMISSION</code> and <code>CELL_FILTER_PERMISSION</code>.</p>
            s3_path: <p>The Amazon S3 path for the table.</p>
            query_session_context: <p>A structure used as a protocol between query engines and Lake Formation or Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.permission_type_mismatch_exception.PermissionTypeMismatchException: <p>The engine does not support filtering data based on the enforced permissions. For example, if you call the <code>GetTemporaryGlueTableCredentials</code> operation with <code>SupportedPermissionType</code> equal to <code>ColumnPermission</code>, but cell-level permissions exist on the table, this exception is thrown.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_temporary_glue_table_credentials_request.GetTemporaryGlueTableCredentialsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_temporary_glue_table_credentials_response.GetTemporaryGlueTableCredentialsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_temporary_glue_table_credentials

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_temporary_glue_table_credentials.get_temporary_glue_table_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_temporary_glue_table_credentials_request.GetTemporaryGlueTableCredentialsRequest = {
            "table_arn": table_arn
        }
        if permissions is not None:
            input_["permissions"] = permissions
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if audit_context is not None:
            input_["audit_context"] = audit_context
        if supported_permission_types is not None:
            input_["supported_permission_types"] = supported_permission_types
        if s3_path is not None:
            input_["s3_path"] = s3_path
        if query_session_context is not None:
            input_["query_session_context"] = query_session_context

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def get_work_unit_results(
        self,
        query_id: "capo_lakeformation.types.get_work_unit_results_request_query_id_string.GetWorkUnitResultsRequestQueryIdString",
        work_unit_id: "capo_lakeformation.types.get_work_unit_results_request_work_unit_id_long.GetWorkUnitResultsRequestWorkUnitIdLong",
        work_unit_token: "capo_lakeformation.types.synthetic_get_work_unit_results_request_work_unit_token_string.SyntheticGetWorkUnitResultsRequestWorkUnitTokenString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> "Generator[capo_lakeformation.types.get_work_unit_results_response.GetWorkUnitResultsResponse]":
        """<p>Returns the work units resulting from the query. Work units can be executed in any order and in parallel. </p>

        Args:
            query_id: <p>The ID of the plan query operation for which to get results.</p>
            work_unit_id: <p>The work unit ID for which to get results. Value generated by enumerating <code>WorkUnitIdMin</code> to <code>WorkUnitIdMax</code> (inclusive) from the <code>WorkUnitRange</code> in the output of <code>GetWorkUnits</code>.</p>
            work_unit_token: <p>A work token used to query the execution service. Token output from <code>GetWorkUnits</code>.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.expired_exception.ExpiredException: <p>Contains details about an error where the query request expired.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.throttled_exception.ThrottledException: <p>Contains details about an error where the query request was throttled.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_work_unit_results_request.GetWorkUnitResultsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_work_unit_results_response.GetWorkUnitResultsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_work_unit_results

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_work_unit_results.get_work_unit_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_work_unit_results_request.GetWorkUnitResultsRequest = {
            "query_id": query_id,
            "work_unit_id": work_unit_id,
            "work_unit_token": work_unit_token,
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

    def get_work_units(
        self,
        query_id: "capo_lakeformation.types.get_work_units_request_query_id_string.GetWorkUnitsRequestQueryIdString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        page_size: Optional[int] = None,
    ) -> "capo_lakeformation.types.get_work_units_response.GetWorkUnitsResponse":
        """<p>Retrieves the work units generated by the <code>StartQueryPlanning</code> operation.</p>

        Args:
            next_token: <p>A continuation token, if this is a continuation call.</p>
            page_size: <p>The size of each page to get in the Amazon Web Services service call. This does not affect the number of items returned in the command's output. Setting a smaller page size results in more calls to the Amazon Web Services service, retrieving fewer items in each call. This can help prevent the Amazon Web Services service calls from timing out.</p>
            query_id: <p>The ID of the plan query operation.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.expired_exception.ExpiredException: <p>Contains details about an error where the query request expired.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.work_units_not_ready_yet_exception.WorkUnitsNotReadyYetException: <p>Contains details about an error related to work units not being ready.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.get_work_units_request.GetWorkUnitsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.get_work_units_response.GetWorkUnitsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.get_work_units

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.get_work_units.get_work_units(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.get_work_units_request.GetWorkUnitsRequest = {
            "query_id": query_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_work_units(
        self,
        query_id: "capo_lakeformation.types.get_work_units_request_query_id_string.GetWorkUnitsRequestQueryIdString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        page_size: Optional[int] = None,
    ) -> "Iterator[capo_lakeformation.types.work_unit_range.WorkUnitRange]":
        _token = next_token
        while True:
            _response = self.get_work_units(
                query_id,
                config_overrides=config_overrides,
                next_token=_token,
                page_size=page_size,
            )
            _page = _resolve_path(_response, ("work_unit_ranges",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def grant_permissions(
        self,
        principal: "capo_lakeformation.types.data_lake_principal.DataLakePrincipal",
        resource: "capo_lakeformation.types.resource.Resource",
        permissions: "capo_lakeformation.types.permission_list.PermissionList",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        condition: Optional["capo_lakeformation.types.condition.Condition"] = None,
        permissions_with_grant_option: Optional[
            "capo_lakeformation.types.permission_list.PermissionList"
        ] = None,
    ) -> "capo_lakeformation.types.grant_permissions_response.GrantPermissionsResponse":
        """<p>Grants permissions to the principal to access metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3.</p> <p>For information about permissions, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html">Security and Access Control to Metadata and Data</a>.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            principal: <p>The principal to be granted the permissions on the resource. Supported principals are IAM users or IAM roles, and they are defined by their principal type and their ARN.</p> <p>Note that if you define a resource with a particular ARN, then later delete, and recreate a resource with that same ARN, the resource maintains the permissions already granted. </p>
            resource: <p>The resource to which permissions are to be granted. Resources in Lake Formation are the Data Catalog, databases, and tables.</p>
            permissions: <p>The permissions granted to the principal on the resource. Lake Formation defines privileges to grant and revoke access to metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3. Lake Formation requires that each principal be authorized to perform a specific task on Lake Formation resources. </p>
            permissions_with_grant_option: <p>Indicates a list of the granted permissions that the principal may pass to other users. These permissions may only be a subset of the permissions granted in the <code>Privileges</code>.</p>

        Raises:
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.grant_permissions_request.GrantPermissionsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.grant_permissions_response.GrantPermissionsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.grant_permissions

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.grant_permissions.grant_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.grant_permissions_request.GrantPermissionsRequest = {
            "principal": principal,
            "resource": resource,
            "permissions": permissions,
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if condition is not None:
            input_["condition"] = condition
        if permissions_with_grant_option is not None:
            input_["permissions_with_grant_option"] = permissions_with_grant_option

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_data_cells_filter(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        table: Optional["capo_lakeformation.types.table_resource.TableResource"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
    ) -> "capo_lakeformation.types.list_data_cells_filter_response.ListDataCellsFilterResponse":
        """<p>Lists all the data cell filters on a table.</p>

        Args:
            table: <p>A table in the Glue Data Catalog.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>
            max_results: <p>The maximum size of the response.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.list_data_cells_filter_request.ListDataCellsFilterRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.list_data_cells_filter_response.ListDataCellsFilterResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.list_data_cells_filter

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.list_data_cells_filter.list_data_cells_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.list_data_cells_filter_request.ListDataCellsFilterRequest = {}
        if table is not None:
            input_["table"] = table
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

    def iter_list_data_cells_filter(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        table: Optional["capo_lakeformation.types.table_resource.TableResource"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
    ) -> "Iterator[capo_lakeformation.types.data_cells_filter.DataCellsFilter]":
        _token = next_token
        while True:
            _response = self.list_data_cells_filter(
                config_overrides=config_overrides,
                table=table,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_cells_filters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_lake_formation_opt_ins(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        principal: Optional[
            "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
        ] = None,
        resource: Optional["capo_lakeformation.types.resource.Resource"] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
    ) -> "capo_lakeformation.types.list_lake_formation_opt_ins_response.ListLakeFormationOptInsResponse":
        """<p>Retrieve the current list of resources and principals that are opt in to enforce Lake Formation permissions.</p>

        Args:
            resource: <p>A structure for the resource.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A continuation token, if this is not the first call to retrieve this list.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.list_lake_formation_opt_ins_request.ListLakeFormationOptInsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.list_lake_formation_opt_ins_response.ListLakeFormationOptInsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.list_lake_formation_opt_ins

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.list_lake_formation_opt_ins.list_lake_formation_opt_ins(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.list_lake_formation_opt_ins_request.ListLakeFormationOptInsRequest = {}
        if principal is not None:
            input_["principal"] = principal
        if resource is not None:
            input_["resource"] = resource
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

    def iter_list_lake_formation_opt_ins(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        principal: Optional[
            "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
        ] = None,
        resource: Optional["capo_lakeformation.types.resource.Resource"] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
    ) -> "Iterator[capo_lakeformation.types.list_lake_formation_opt_ins_response.ListLakeFormationOptInsResponse]":
        _token = next_token
        while True:
            _response = self.list_lake_formation_opt_ins(
                config_overrides=config_overrides,
                principal=principal,
                resource=resource,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_lf_tag_expressions(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
    ) -> "capo_lakeformation.types.list_lf_tag_expressions_response.ListLFTagExpressionsResponse":
        """<p>Returns the LF-Tag expressions in caller’s account filtered based on caller's permissions. Data Lake and read only admins implicitly can see all tag expressions in their account, else caller needs DESCRIBE permissions on tag expression.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. </p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A continuation token, if this is not the first call to retrieve this list.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.list_lf_tag_expressions_request.ListLFTagExpressionsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.list_lf_tag_expressions_response.ListLFTagExpressionsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.list_lf_tag_expressions

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.list_lf_tag_expressions.list_lf_tag_expressions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.list_lf_tag_expressions_request.ListLFTagExpressionsRequest = {}
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
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

    def iter_list_lf_tag_expressions(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
    ) -> "Iterator[capo_lakeformation.types.lf_tag_expression.LFTagExpression]":
        _token = next_token
        while True:
            _response = self.list_lf_tag_expressions(
                config_overrides=config_overrides,
                catalog_id=catalog_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("lf_tag_expressions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_lf_tags(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        resource_share_type: Optional[
            "capo_lakeformation.types.resource_share_type.ResourceShareType"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
    ) -> "capo_lakeformation.types.list_lf_tags_response.ListLFTagsResponse":
        """<p>Lists LF-tags that the requester has permission to view. </p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            resource_share_type: <p>If resource share type is <code>ALL</code>, returns both in-account LF-tags and shared LF-tags that the requester has permission to view. If resource share type is <code>FOREIGN</code>, returns all share LF-tags that the requester can view. If no resource share type is passed, lists LF-tags in the given catalog ID that the requester has permission to view.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>A continuation token, if this is not the first call to retrieve this list.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.list_lf_tags_request.ListLFTagsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.list_lf_tags_response.ListLFTagsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.list_lf_tags

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.list_lf_tags.list_lf_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.list_lf_tags_request.ListLFTagsRequest = {}
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if resource_share_type is not None:
            input_["resource_share_type"] = resource_share_type
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

    def iter_list_lf_tags(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        resource_share_type: Optional[
            "capo_lakeformation.types.resource_share_type.ResourceShareType"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
    ) -> "Iterator[capo_lakeformation.types.lf_tag_pair.LFTagPair]":
        _token = next_token
        while True:
            _response = self.list_lf_tags(
                config_overrides=config_overrides,
                catalog_id=catalog_id,
                resource_share_type=resource_share_type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("lf_tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_permissions(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        principal: Optional[
            "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
        ] = None,
        resource_type: Optional[
            "capo_lakeformation.types.data_lake_resource_type.DataLakeResourceType"
        ] = None,
        resource: Optional["capo_lakeformation.types.resource.Resource"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        include_related: Optional[
            "capo_lakeformation.types.true_false_string.TrueFalseString"
        ] = None,
    ) -> "capo_lakeformation.types.list_permissions_response.ListPermissionsResponse":
        """<p>Returns a list of the principal permissions on the resource, filtered by the permissions of the caller. For example, if you are granted an ALTER permission, you are able to see only the principal permissions for ALTER.</p> <p>This operation returns only those permissions that have been explicitly granted. If both <code>Principal</code> and <code>Resource</code> parameters are provided, the response returns effective permissions rather than the explicitly granted permissions.</p> <p>For information about permissions, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html">Security and Access Control to Metadata and Data</a>.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            principal: <p>Specifies a principal to filter the permissions returned.</p>
            resource_type: <p>Specifies a resource type to filter the permissions returned.</p>
            resource: <p>A resource where you will get a list of the principal permissions.</p> <p>This operation does not support getting privileges on a table with columns. Instead, call this operation on the table, and the operation returns the table and the table w columns.</p>
            next_token: <p>A continuation token, if this is not the first call to retrieve this list.</p>
            max_results: <p>The maximum number of results to return.</p>
            include_related: <p>Indicates that related permissions should be included in the results when listing permissions on a table resource.</p> <p>Set the field to <code>TRUE</code> to show the cell filters on a table resource. Default is <code>FALSE</code>. The Principal parameter must not be specified when requesting cell filter information.</p>

        Raises:
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.list_permissions_request.ListPermissionsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.list_permissions_response.ListPermissionsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.list_permissions

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.list_permissions.list_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.list_permissions_request.ListPermissionsRequest = {}
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if principal is not None:
            input_["principal"] = principal
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource is not None:
            input_["resource"] = resource
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if include_related is not None:
            input_["include_related"] = include_related

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_permissions(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        principal: Optional[
            "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
        ] = None,
        resource_type: Optional[
            "capo_lakeformation.types.data_lake_resource_type.DataLakeResourceType"
        ] = None,
        resource: Optional["capo_lakeformation.types.resource.Resource"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        include_related: Optional[
            "capo_lakeformation.types.true_false_string.TrueFalseString"
        ] = None,
    ) -> "Iterator[capo_lakeformation.types.list_permissions_response.ListPermissionsResponse]":
        _token = next_token
        while True:
            _response = self.list_permissions(
                config_overrides=config_overrides,
                catalog_id=catalog_id,
                principal=principal,
                resource_type=resource_type,
                resource=resource,
                next_token=_token,
                max_results=max_results,
                include_related=include_related,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resources(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        filter_condition_list: Optional[
            "capo_lakeformation.types.filter_condition_list.FilterConditionList"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
    ) -> "capo_lakeformation.types.list_resources_response.ListResourcesResponse":
        """<p>Lists the resources registered to be managed by the Data Catalog.</p>

        Args:
            filter_condition_list: <p>Any applicable row-level and/or column-level filtering conditions for the resources.</p>
            max_results: <p>The maximum number of resource results.</p>
            next_token: <p>A continuation token, if this is not the first call to retrieve these resources.</p>

        Raises:
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.list_resources_request.ListResourcesRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.list_resources_response.ListResourcesResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.list_resources

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.list_resources.list_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.list_resources_request.ListResourcesRequest = {}
        if filter_condition_list is not None:
            input_["filter_condition_list"] = filter_condition_list
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

    def iter_list_resources(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        filter_condition_list: Optional[
            "capo_lakeformation.types.filter_condition_list.FilterConditionList"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
    ) -> "Iterator[capo_lakeformation.types.list_resources_response.ListResourcesResponse]":
        _token = next_token
        while True:
            _response = self.list_resources(
                config_overrides=config_overrides,
                filter_condition_list=filter_condition_list,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_table_storage_optimizers(
        self,
        database_name: "capo_lakeformation.types.name_string.NameString",
        table_name: "capo_lakeformation.types.name_string.NameString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        storage_optimizer_type: Optional[
            "capo_lakeformation.types.optimizer_type.OptimizerType"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
    ) -> "capo_lakeformation.types.list_table_storage_optimizers_response.ListTableStorageOptimizersResponse":
        """<p>Returns the configuration of all storage optimizers associated with a specified table.</p>

        Args:
            catalog_id: <p>The Catalog ID of the table.</p>
            database_name: <p>Name of the database where the table is present.</p>
            table_name: <p>Name of the table.</p>
            storage_optimizer_type: <p>The specific type of storage optimizers to list. The supported value is <code>compaction</code>.</p>
            max_results: <p>The number of storage optimizers to return on each call.</p>
            next_token: <p>A continuation token, if this is a continuation call.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.list_table_storage_optimizers_request.ListTableStorageOptimizersRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.list_table_storage_optimizers_response.ListTableStorageOptimizersResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.list_table_storage_optimizers

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.list_table_storage_optimizers.list_table_storage_optimizers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.list_table_storage_optimizers_request.ListTableStorageOptimizersRequest = {
            "database_name": database_name,
            "table_name": table_name,
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if storage_optimizer_type is not None:
            input_["storage_optimizer_type"] = storage_optimizer_type
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

    def iter_list_table_storage_optimizers(
        self,
        database_name: "capo_lakeformation.types.name_string.NameString",
        table_name: "capo_lakeformation.types.name_string.NameString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        storage_optimizer_type: Optional[
            "capo_lakeformation.types.optimizer_type.OptimizerType"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
    ) -> "Iterator[capo_lakeformation.types.list_table_storage_optimizers_response.ListTableStorageOptimizersResponse]":
        _token = next_token
        while True:
            _response = self.list_table_storage_optimizers(
                database_name,
                table_name,
                config_overrides=config_overrides,
                catalog_id=catalog_id,
                storage_optimizer_type=storage_optimizer_type,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_transactions(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        status_filter: Optional[
            "capo_lakeformation.types.transaction_status_filter.TransactionStatusFilter"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_lakeformation.types.token_string.TokenString"
        ] = None,
    ) -> "capo_lakeformation.types.list_transactions_response.ListTransactionsResponse":
        """<p>Returns metadata about transactions and their status. To prevent the response from growing indefinitely, only uncommitted transactions and those available for time-travel queries are returned.</p> <p>This operation can help you identify uncommitted transactions or to get information about transactions.</p>

        Args:
            catalog_id: <p>The catalog for which to list transactions. Defaults to the account ID of the caller.</p>
            status_filter: <p> A filter indicating the status of transactions to return. Options are ALL | COMPLETED | COMMITTED | ABORTED | ACTIVE. The default is <code>ALL</code>.</p>
            max_results: <p>The maximum number of transactions to return in a single call.</p>
            next_token: <p>A continuation token if this is not the first call to retrieve transactions.</p>

        Raises:
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.list_transactions_request.ListTransactionsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.list_transactions_response.ListTransactionsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.list_transactions

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.list_transactions.list_transactions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.list_transactions_request.ListTransactionsRequest = {}
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if status_filter is not None:
            input_["status_filter"] = status_filter
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

    def iter_list_transactions(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        status_filter: Optional[
            "capo_lakeformation.types.transaction_status_filter.TransactionStatusFilter"
        ] = None,
        max_results: Optional["capo_lakeformation.types.page_size.PageSize"] = None,
        next_token: Optional[
            "capo_lakeformation.types.token_string.TokenString"
        ] = None,
    ) -> "Iterator[capo_lakeformation.types.list_transactions_response.ListTransactionsResponse]":
        _token = next_token
        while True:
            _response = self.list_transactions(
                config_overrides=config_overrides,
                catalog_id=catalog_id,
                status_filter=status_filter,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_data_lake_settings(
        self,
        data_lake_settings: "capo_lakeformation.types.data_lake_settings.DataLakeSettings",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.put_data_lake_settings_response.PutDataLakeSettingsResponse":
        """<p>Sets the list of data lake administrators who have admin privileges on all resources managed by Lake Formation. For more information on admin privileges, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/lake-formation-permissions.html">Granting Lake Formation Permissions</a>.</p> <p>This API replaces the current list of data lake admins with the new list being passed. To add an admin, fetch the current list and add the new admin to that list and pass that list in this API.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            data_lake_settings: <p>A structure representing a list of Lake Formation principals designated as data lake administrators.</p>

        Raises:
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.put_data_lake_settings_request.PutDataLakeSettingsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.put_data_lake_settings_response.PutDataLakeSettingsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.put_data_lake_settings

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.put_data_lake_settings.put_data_lake_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.put_data_lake_settings_request.PutDataLakeSettingsRequest = {
            "data_lake_settings": data_lake_settings
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_resource(
        self,
        resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        use_service_linked_role: Optional[
            "capo_lakeformation.types.nullable_boolean.NullableBoolean"
        ] = None,
        role_arn: Optional["capo_lakeformation.types.iam_role_arn.IAMRoleArn"] = None,
        with_federation: Optional[
            "capo_lakeformation.types.nullable_boolean.NullableBoolean"
        ] = None,
        hybrid_access_enabled: Optional[
            "capo_lakeformation.types.nullable_boolean.NullableBoolean"
        ] = None,
        with_privileged_access: Optional[
            "capo_lakeformation.types.boolean.Boolean"
        ] = None,
        expected_resource_owner_account: Optional[
            "capo_lakeformation.types.account_id_string.AccountIdString"
        ] = None,
    ) -> "capo_lakeformation.types.register_resource_response.RegisterResourceResponse":
        """<p>Registers the resource as managed by the Data Catalog.</p> <p>To add or update data, Lake Formation needs read/write access to the chosen data location. Choose a role that you know has permission to do this, or choose the AWSServiceRoleForLakeFormationDataAccess service-linked role. When you register the first Amazon S3 path, the service-linked role and a new inline policy are created on your behalf. Lake Formation adds the first path to the inline policy and attaches it to the service-linked role. When you register subsequent paths, Lake Formation adds the path to the existing policy.</p> <p>The following request registers a new location and gives Lake Formation permission to use the service-linked role to access that location.</p> <p> <code>ResourceArn = arn:aws:s3:::my-bucket/ UseServiceLinkedRole = true</code> </p> <p>If <code>UseServiceLinkedRole</code> is not set to true, you must provide or set the <code>RoleArn</code>:</p> <p> <code>arn:aws:iam::12345:role/my-data-access-role</code> </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to register.</p>
            use_service_linked_role: <p>Designates an Identity and Access Management (IAM) service-linked role by registering this role with the Data Catalog. A service-linked role is a unique type of IAM role that is linked directly to Lake Formation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/service-linked-roles.html">Using Service-Linked Roles for Lake Formation</a>.</p>
            role_arn: <p>The identifier for the role that registers the resource.</p>
            with_federation: <p>Whether or not the resource is a federated resource.</p>
            hybrid_access_enabled: <p> Specifies whether the data access of tables pointing to the location can be managed by both Lake Formation permissions as well as Amazon S3 bucket policies. </p>
            with_privileged_access: <p>Grants the calling principal the permissions to perform all supported Lake Formation operations on the registered data location. </p>
            expected_resource_owner_account: <p>The Amazon Web Services account that owns the Glue tables associated with specific Amazon S3 locations. </p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.already_exists_exception.AlreadyExistsException: <p>A resource to be created or added already exists.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.resource_number_limit_exceeded_exception.ResourceNumberLimitExceededException: <p>A resource numerical limit was exceeded.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.register_resource_request.RegisterResourceRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.register_resource_response.RegisterResourceResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.register_resource

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.register_resource.register_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.register_resource_request.RegisterResourceRequest = {
            "resource_arn": resource_arn
        }
        if use_service_linked_role is not None:
            input_["use_service_linked_role"] = use_service_linked_role
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if with_federation is not None:
            input_["with_federation"] = with_federation
        if hybrid_access_enabled is not None:
            input_["hybrid_access_enabled"] = hybrid_access_enabled
        if with_privileged_access is not None:
            input_["with_privileged_access"] = with_privileged_access
        if expected_resource_owner_account is not None:
            input_["expected_resource_owner_account"] = expected_resource_owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_lf_tags_from_resource(
        self,
        resource: "capo_lakeformation.types.resource.Resource",
        lf_tags: "capo_lakeformation.types.lf_tags_list.LFTagsList",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.remove_lf_tags_from_resource_response.RemoveLFTagsFromResourceResponse":
        """<p>Removes an LF-tag from the resource. Only database, table, or tableWithColumns resource are allowed. To tag columns, use the column inclusion list in <code>tableWithColumns</code> to specify column input.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            resource: <p>The database, table, or column resource where you want to remove an LF-tag.</p>
            lf_tags: <p>The LF-tags to be removed from the resource.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.glue_encryption_exception.GlueEncryptionException: <p>An encryption operation failed.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.remove_lf_tags_from_resource_request.RemoveLFTagsFromResourceRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.remove_lf_tags_from_resource_response.RemoveLFTagsFromResourceResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.remove_lf_tags_from_resource

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.remove_lf_tags_from_resource.remove_lf_tags_from_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.remove_lf_tags_from_resource_request.RemoveLFTagsFromResourceRequest = {
            "resource": resource,
            "lf_tags": lf_tags,
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def revoke_permissions(
        self,
        principal: "capo_lakeformation.types.data_lake_principal.DataLakePrincipal",
        resource: "capo_lakeformation.types.resource.Resource",
        permissions: "capo_lakeformation.types.permission_list.PermissionList",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        condition: Optional["capo_lakeformation.types.condition.Condition"] = None,
        permissions_with_grant_option: Optional[
            "capo_lakeformation.types.permission_list.PermissionList"
        ] = None,
    ) -> (
        "capo_lakeformation.types.revoke_permissions_response.RevokePermissionsResponse"
    ):
        """<p>Revokes permissions to the principal to access metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            principal: <p>The principal to be revoked permissions on the resource.</p>
            resource: <p>The resource to which permissions are to be revoked.</p>
            permissions: <p>The permissions revoked to the principal on the resource. For information about permissions, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html">Security and Access Control to Metadata and Data</a>.</p>
            permissions_with_grant_option: <p>Indicates a list of permissions for which to revoke the grant option allowing the principal to pass permissions to other principals.</p>

        Raises:
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.revoke_permissions_request.RevokePermissionsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.revoke_permissions_response.RevokePermissionsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.revoke_permissions

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.revoke_permissions.revoke_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.revoke_permissions_request.RevokePermissionsRequest = {
            "principal": principal,
            "resource": resource,
            "permissions": permissions,
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if condition is not None:
            input_["condition"] = condition
        if permissions_with_grant_option is not None:
            input_["permissions_with_grant_option"] = permissions_with_grant_option

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_databases_by_lf_tags(
        self,
        expression: "capo_lakeformation.types.expression.Expression",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        max_results: Optional[
            "capo_lakeformation.types.search_page_size.SearchPageSize"
        ] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.search_databases_by_lf_tags_response.SearchDatabasesByLFTagsResponse":
        """<p>This operation allows a search on <code>DATABASE</code> resources by <code>TagCondition</code>. This operation is used by admins who want to grant user permissions on certain <code>TagConditions</code>. Before making a grant, the admin can use <code>SearchDatabasesByTags</code> to find all resources where the given <code>TagConditions</code> are valid to verify whether the returned resources can be shared.</p>

        Args:
            next_token: <p>A continuation token, if this is not the first call to retrieve this list.</p>
            max_results: <p>The maximum number of results to return.</p>
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            expression: <p>A list of conditions (<code>LFTag</code> structures) to search for in database resources.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.glue_encryption_exception.GlueEncryptionException: <p>An encryption operation failed.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.search_databases_by_lf_tags_request.SearchDatabasesByLFTagsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.search_databases_by_lf_tags_response.SearchDatabasesByLFTagsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.search_databases_by_lf_tags

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.search_databases_by_lf_tags.search_databases_by_lf_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.search_databases_by_lf_tags_request.SearchDatabasesByLFTagsRequest = {
            "expression": expression
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_search_databases_by_lf_tags(
        self,
        expression: "capo_lakeformation.types.expression.Expression",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        max_results: Optional[
            "capo_lakeformation.types.search_page_size.SearchPageSize"
        ] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "Iterator[capo_lakeformation.types.tagged_database.TaggedDatabase]":
        _token = next_token
        while True:
            _response = self.search_databases_by_lf_tags(
                expression,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                catalog_id=catalog_id,
            )
            _page = _resolve_path(_response, ("database_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_tables_by_lf_tags(
        self,
        expression: "capo_lakeformation.types.expression.Expression",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        max_results: Optional[
            "capo_lakeformation.types.search_page_size.SearchPageSize"
        ] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.search_tables_by_lf_tags_response.SearchTablesByLFTagsResponse":
        """<p>This operation allows a search on <code>TABLE</code> resources by <code>LFTag</code>s. This will be used by admins who want to grant user permissions on certain LF-tags. Before making a grant, the admin can use <code>SearchTablesByLFTags</code> to find all resources where the given <code>LFTag</code>s are valid to verify whether the returned resources can be shared.</p>

        Args:
            next_token: <p>A continuation token, if this is not the first call to retrieve this list.</p>
            max_results: <p>The maximum number of results to return.</p>
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            expression: <p>A list of conditions (<code>LFTag</code> structures) to search for in table resources.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.glue_encryption_exception.GlueEncryptionException: <p>An encryption operation failed.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.search_tables_by_lf_tags_request.SearchTablesByLFTagsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.search_tables_by_lf_tags_response.SearchTablesByLFTagsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.search_tables_by_lf_tags

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.search_tables_by_lf_tags.search_tables_by_lf_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.search_tables_by_lf_tags_request.SearchTablesByLFTagsRequest = {
            "expression": expression
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_search_tables_by_lf_tags(
        self,
        expression: "capo_lakeformation.types.expression.Expression",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        next_token: Optional["capo_lakeformation.types.token.Token"] = None,
        max_results: Optional[
            "capo_lakeformation.types.search_page_size.SearchPageSize"
        ] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "Iterator[capo_lakeformation.types.tagged_table.TaggedTable]":
        _token = next_token
        while True:
            _response = self.search_tables_by_lf_tags(
                expression,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                catalog_id=catalog_id,
            )
            _page = _resolve_path(_response, ("table_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_query_planning(
        self,
        query_planning_context: "capo_lakeformation.types.query_planning_context.QueryPlanningContext",
        query_string: "capo_lakeformation.types.synthetic_start_query_planning_request_query_string.SyntheticStartQueryPlanningRequestQueryString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> "capo_lakeformation.types.start_query_planning_response.StartQueryPlanningResponse":
        """<p>Submits a request to process a query statement.</p> <p>This operation generates work units that can be retrieved with the <code>GetWorkUnits</code> operation as soon as the query state is WORKUNITS_AVAILABLE or FINISHED.</p>

        Args:
            query_planning_context: <p>A structure containing information about the query plan.</p>
            query_string: <p>A PartiQL query statement used as an input to the planner service.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.throttled_exception.ThrottledException: <p>Contains details about an error where the query request was throttled.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.start_query_planning_request.StartQueryPlanningRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.start_query_planning_response.StartQueryPlanningResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.start_query_planning

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.start_query_planning.start_query_planning(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.start_query_planning_request.StartQueryPlanningRequest = {
            "query_planning_context": query_planning_context,
            "query_string": query_string,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_transaction(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        transaction_type: Optional[
            "capo_lakeformation.types.transaction_type.TransactionType"
        ] = None,
    ) -> "capo_lakeformation.types.start_transaction_response.StartTransactionResponse":
        """<p>Starts a new transaction and returns its transaction ID. Transaction IDs are opaque objects that you can use to identify a transaction.</p>

        Args:
            transaction_type: <p>Indicates whether this transaction should be read only or read and write. Writes made using a read-only transaction ID will be rejected. Read-only transactions do not need to be committed. </p>

        Raises:
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.start_transaction_request.StartTransactionRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.start_transaction_response.StartTransactionResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.start_transaction

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.start_transaction.start_transaction(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.start_transaction_request.StartTransactionRequest = {}
        if transaction_type is not None:
            input_["transaction_type"] = transaction_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_data_cells_filter(
        self,
        table_data: "capo_lakeformation.types.data_cells_filter.DataCellsFilter",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
    ) -> "capo_lakeformation.types.update_data_cells_filter_response.UpdateDataCellsFilterResponse":
        """<p>Updates a data cell filter.</p>

        Args:
            table_data: <p>A <code>DataCellsFilter</code> structure containing information about the data cells filter.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.update_data_cells_filter_request.UpdateDataCellsFilterRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.update_data_cells_filter_response.UpdateDataCellsFilterResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.update_data_cells_filter

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.update_data_cells_filter.update_data_cells_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.update_data_cells_filter_request.UpdateDataCellsFilterRequest = {
            "table_data": table_data
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_lake_formation_identity_center_configuration(
        self,
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        share_recipients: Optional[
            "capo_lakeformation.types.data_lake_principal_list.DataLakePrincipalList"
        ] = None,
        service_integrations: Optional[
            "capo_lakeformation.types.service_integration_list.ServiceIntegrationList"
        ] = None,
        application_status: Optional[
            "capo_lakeformation.types.application_status.ApplicationStatus"
        ] = None,
        external_filtering: Optional[
            "capo_lakeformation.types.external_filtering_configuration.ExternalFilteringConfiguration"
        ] = None,
    ) -> "capo_lakeformation.types.update_lake_formation_identity_center_configuration_response.UpdateLakeFormationIdentityCenterConfigurationResponse":
        """<p>Updates the IAM Identity Center connection parameters.</p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, view definitions, and other control information to manage your Lake Formation environment.</p>
            share_recipients: <p>A list of Amazon Web Services account IDs or Amazon Web Services organization/organizational unit ARNs that are allowed to access to access data managed by Lake Formation. </p> <p>If the <code>ShareRecipients</code> list includes valid values, then the resource share is updated with the principals you want to have access to the resources.</p> <p>If the <code>ShareRecipients</code> value is null, both the list of share recipients and the resource share remain unchanged.</p> <p>If the <code>ShareRecipients</code> value is an empty list, then the existing share recipients list will be cleared, and the resource share will be deleted.</p>
            service_integrations: <p>A list of service integrations for enabling trusted identity propagation with external services such as Redshift.</p>
            application_status: <p>Allows to enable or disable the IAM Identity Center connection.</p>
            external_filtering: <p>A list of the account IDs of Amazon Web Services accounts of third-party applications that are allowed to access data managed by Lake Formation.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.update_lake_formation_identity_center_configuration_request.UpdateLakeFormationIdentityCenterConfigurationRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.update_lake_formation_identity_center_configuration_response.UpdateLakeFormationIdentityCenterConfigurationResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.update_lake_formation_identity_center_configuration

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.update_lake_formation_identity_center_configuration.update_lake_formation_identity_center_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.update_lake_formation_identity_center_configuration_request.UpdateLakeFormationIdentityCenterConfigurationRequest = {}
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if share_recipients is not None:
            input_["share_recipients"] = share_recipients
        if service_integrations is not None:
            input_["service_integrations"] = service_integrations
        if application_status is not None:
            input_["application_status"] = application_status
        if external_filtering is not None:
            input_["external_filtering"] = external_filtering

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_lf_tag(
        self,
        tag_key: "capo_lakeformation.types.lf_tag_key.LFTagKey",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        tag_values_to_delete: Optional[
            "capo_lakeformation.types.tag_value_list.TagValueList"
        ] = None,
        tag_values_to_add: Optional[
            "capo_lakeformation.types.tag_value_list.TagValueList"
        ] = None,
    ) -> "capo_lakeformation.types.update_lf_tag_response.UpdateLFTagResponse":
        """<p>Updates the list of possible values for the specified LF-tag key. If the LF-tag does not exist, the operation throws an EntityNotFoundException. The values in the delete key values will be deleted from list of possible values. If any value in the delete key values is attached to a resource, then API errors out with a 400 Exception - "Update not allowed". Untag the attribute before deleting the LF-tag key's value. </p>

        Args:
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>
            tag_key: <p>The key-name for the LF-tag for which to add or delete values.</p>
            tag_values_to_delete: <p>A list of LF-tag values to delete from the LF-tag.</p>
            tag_values_to_add: <p>A list of LF-tag values to add from the LF-tag.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.update_lf_tag_request.UpdateLFTagRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.update_lf_tag_response.UpdateLFTagResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.update_lf_tag

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.update_lf_tag.update_lf_tag(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.update_lf_tag_request.UpdateLFTagRequest = {
            "tag_key": tag_key
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if tag_values_to_delete is not None:
            input_["tag_values_to_delete"] = tag_values_to_delete
        if tag_values_to_add is not None:
            input_["tag_values_to_add"] = tag_values_to_add

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_lf_tag_expression(
        self,
        name: "capo_lakeformation.types.name_string.NameString",
        expression: "capo_lakeformation.types.expression.Expression",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        description: Optional[
            "capo_lakeformation.types.description_string.DescriptionString"
        ] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.update_lf_tag_expression_response.UpdateLFTagExpressionResponse":
        """<p>Updates the name of the LF-Tag expression to the new description and expression body provided. Updating a LF-Tag expression immediately changes the permission boundaries of all existing <code>LFTagPolicy</code> permission grants that reference the given LF-Tag expression.</p>

        Args:
            name: <p>The name for the LF-Tag expression.</p>
            description: <p>The description with information about the saved LF-Tag expression.</p>
            catalog_id: <p>The identifier for the Data Catalog. By default, the account ID. </p>
            expression: <p>The LF-Tag expression body composed of one more LF-Tag key-value pairs.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.resource_number_limit_exceeded_exception.ResourceNumberLimitExceededException: <p>A resource numerical limit was exceeded.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.update_lf_tag_expression_request.UpdateLFTagExpressionRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.update_lf_tag_expression_response.UpdateLFTagExpressionResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.update_lf_tag_expression

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.update_lf_tag_expression.update_lf_tag_expression(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.update_lf_tag_expression_request.UpdateLFTagExpressionRequest = {
            "name": name,
            "expression": expression,
        }
        if description is not None:
            input_["description"] = description
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resource(
        self,
        role_arn: "capo_lakeformation.types.iam_role_arn.IAMRoleArn",
        resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        with_federation: Optional[
            "capo_lakeformation.types.nullable_boolean.NullableBoolean"
        ] = None,
        hybrid_access_enabled: Optional[
            "capo_lakeformation.types.nullable_boolean.NullableBoolean"
        ] = None,
        expected_resource_owner_account: Optional[
            "capo_lakeformation.types.account_id_string.AccountIdString"
        ] = None,
    ) -> "capo_lakeformation.types.update_resource_response.UpdateResourceResponse":
        """<p>Updates the data access role used for vending access to the given (registered) resource in Lake Formation. </p>

        Args:
            role_arn: <p>The new role to use for the given resource registered in Lake Formation.</p>
            resource_arn: <p>The resource ARN.</p>
            with_federation: <p>Whether or not the resource is a federated resource.</p>
            hybrid_access_enabled: <p> Specifies whether the data access of tables pointing to the location can be managed by both Lake Formation permissions as well as Amazon S3 bucket policies. </p>
            expected_resource_owner_account: <p>The Amazon Web Services account that owns the Glue tables associated with specific Amazon S3 locations. </p>

        Raises:
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.update_resource_request.UpdateResourceRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.update_resource_response.UpdateResourceResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.update_resource

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.update_resource.update_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.update_resource_request.UpdateResourceRequest = {
            "role_arn": role_arn,
            "resource_arn": resource_arn,
        }
        if with_federation is not None:
            input_["with_federation"] = with_federation
        if hybrid_access_enabled is not None:
            input_["hybrid_access_enabled"] = hybrid_access_enabled
        if expected_resource_owner_account is not None:
            input_["expected_resource_owner_account"] = expected_resource_owner_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_table_objects(
        self,
        database_name: "capo_lakeformation.types.name_string.NameString",
        table_name: "capo_lakeformation.types.name_string.NameString",
        write_operations: "capo_lakeformation.types.write_operation_list.WriteOperationList",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
        transaction_id: Optional[
            "capo_lakeformation.types.transaction_id_string.TransactionIdString"
        ] = None,
    ) -> "capo_lakeformation.types.update_table_objects_response.UpdateTableObjectsResponse":
        """<p>Updates the manifest of Amazon S3 objects that make up the specified governed table.</p>

        Args:
            catalog_id: <p>The catalog containing the governed table to update. Defaults to the caller’s account ID.</p>
            database_name: <p>The database containing the governed table to update.</p>
            table_name: <p>The governed table to update.</p>
            transaction_id: <p>The transaction at which to do the write.</p>
            write_operations: <p>A list of <code>WriteOperation</code> objects that define an object to add to or delete from the manifest for a governed table.</p>

        Raises:
            capo_lakeformation.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Two processes are trying to modify a resource simultaneously.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_lakeformation.errors.resource_not_ready_exception.ResourceNotReadyException: <p>Contains details about an error related to a resource which is not ready for a transaction.</p>
            capo_lakeformation.errors.transaction_canceled_exception.TransactionCanceledException: <p>Contains details about an error related to a transaction that was cancelled.</p>
            capo_lakeformation.errors.transaction_commit_in_progress_exception.TransactionCommitInProgressException: <p>Contains details about an error related to a transaction commit that was in progress.</p>
            capo_lakeformation.errors.transaction_committed_exception.TransactionCommittedException: <p>Contains details about an error where the specified transaction has already been committed and cannot be used for <code>UpdateTableObjects</code>.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.update_table_objects_request.UpdateTableObjectsRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.update_table_objects_response.UpdateTableObjectsResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.update_table_objects

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.update_table_objects.update_table_objects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.update_table_objects_request.UpdateTableObjectsRequest = {
            "database_name": database_name,
            "table_name": table_name,
            "write_operations": write_operations,
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id
        if transaction_id is not None:
            input_["transaction_id"] = transaction_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_table_storage_optimizer(
        self,
        database_name: "capo_lakeformation.types.name_string.NameString",
        table_name: "capo_lakeformation.types.name_string.NameString",
        storage_optimizer_config: "capo_lakeformation.types.storage_optimizer_config_map.StorageOptimizerConfigMap",
        *,
        config_overrides: Optional[LakeFormationClientConfig] = None,
        catalog_id: Optional[
            "capo_lakeformation.types.catalog_id_string.CatalogIdString"
        ] = None,
    ) -> "capo_lakeformation.types.update_table_storage_optimizer_response.UpdateTableStorageOptimizerResponse":
        """<p>Updates the configuration of the storage optimizers for a table.</p>

        Args:
            catalog_id: <p>The Catalog ID of the table.</p>
            database_name: <p>Name of the database where the table is present.</p>
            table_name: <p>Name of the table for which to enable the storage optimizer.</p>
            storage_optimizer_config: <p>Name of the configuration for the storage optimizer.</p>

        Raises:
            capo_lakeformation.errors.access_denied_exception.AccessDeniedException: <p>Access to a resource was denied.</p>
            capo_lakeformation.errors.entity_not_found_exception.EntityNotFoundException: <p>A specified entity does not exist.</p>
            capo_lakeformation.errors.internal_service_exception.InternalServiceException: <p>An internal service error occurred.</p>
            capo_lakeformation.errors.invalid_input_exception.InvalidInputException: <p>The input provided was not valid.</p>
            capo_lakeformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lakeformation.types.update_table_storage_optimizer_request.UpdateTableStorageOptimizerRequest]",
        ) -> OperationResponse[
            "capo_lakeformation.types.update_table_storage_optimizer_response.UpdateTableStorageOptimizerResponse"
        ]:
            import capo_lakeformation._operations.aws_lake_formation.update_table_storage_optimizer

            output, http_response = (
                capo_lakeformation._operations.aws_lake_formation.update_table_storage_optimizer.update_table_storage_optimizer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lakeformation.types.update_table_storage_optimizer_request.UpdateTableStorageOptimizerRequest = {
            "database_name": database_name,
            "table_name": table_name,
            "storage_optimizer_config": storage_optimizer_config,
        }
        if catalog_id is not None:
            input_["catalog_id"] = catalog_id

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
