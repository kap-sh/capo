"""Generated from Smithy shape ``com.amazonaws.entityresolution#AWSVeniceService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_entityresolution._auth._signers
import capo_entityresolution._auth._sigv4
from capo_entityresolution._auth._identity import Credentials
from capo_entityresolution._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_entityresolution._auth._zapros_handler import AuthMiddleware
from capo_entityresolution._pagination import resolve_path as _resolve_path
from capo_entityresolution._services._aws_config import aws_config
from capo_entityresolution._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_entityresolution.types.add_policy_statement_input
    import capo_entityresolution.types.add_policy_statement_output
    import capo_entityresolution.types.batch_delete_unique_id_input
    import capo_entityresolution.types.batch_delete_unique_id_output
    import capo_entityresolution.types.create_id_mapping_workflow_input
    import capo_entityresolution.types.create_id_mapping_workflow_output
    import capo_entityresolution.types.create_id_namespace_input
    import capo_entityresolution.types.create_id_namespace_output
    import capo_entityresolution.types.create_matching_workflow_input
    import capo_entityresolution.types.create_matching_workflow_output
    import capo_entityresolution.types.create_schema_mapping_input
    import capo_entityresolution.types.create_schema_mapping_output
    import capo_entityresolution.types.delete_id_mapping_workflow_input
    import capo_entityresolution.types.delete_id_mapping_workflow_output
    import capo_entityresolution.types.delete_id_namespace_input
    import capo_entityresolution.types.delete_id_namespace_output
    import capo_entityresolution.types.delete_matching_workflow_input
    import capo_entityresolution.types.delete_matching_workflow_output
    import capo_entityresolution.types.delete_policy_statement_input
    import capo_entityresolution.types.delete_policy_statement_output
    import capo_entityresolution.types.delete_schema_mapping_input
    import capo_entityresolution.types.delete_schema_mapping_output
    import capo_entityresolution.types.description
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.entity_name_or_id_mapping_workflow_arn
    import capo_entityresolution.types.entity_name_or_id_namespace_arn
    import capo_entityresolution.types.generate_match_id_input
    import capo_entityresolution.types.generate_match_id_output
    import capo_entityresolution.types.get_id_mapping_job_input
    import capo_entityresolution.types.get_id_mapping_job_output
    import capo_entityresolution.types.get_id_mapping_workflow_input
    import capo_entityresolution.types.get_id_mapping_workflow_output
    import capo_entityresolution.types.get_id_namespace_input
    import capo_entityresolution.types.get_id_namespace_output
    import capo_entityresolution.types.get_match_id_input
    import capo_entityresolution.types.get_match_id_output
    import capo_entityresolution.types.get_matching_job_input
    import capo_entityresolution.types.get_matching_job_output
    import capo_entityresolution.types.get_matching_workflow_input
    import capo_entityresolution.types.get_matching_workflow_output
    import capo_entityresolution.types.get_policy_input
    import capo_entityresolution.types.get_policy_output
    import capo_entityresolution.types.get_provider_service_input
    import capo_entityresolution.types.get_provider_service_output
    import capo_entityresolution.types.get_schema_mapping_input
    import capo_entityresolution.types.get_schema_mapping_output
    import capo_entityresolution.types.id_mapping_incremental_run_config
    import capo_entityresolution.types.id_mapping_job_output_source_config
    import capo_entityresolution.types.id_mapping_role_arn
    import capo_entityresolution.types.id_mapping_techniques
    import capo_entityresolution.types.id_mapping_workflow_input_source_config
    import capo_entityresolution.types.id_mapping_workflow_output_source_config
    import capo_entityresolution.types.id_mapping_workflow_summary
    import capo_entityresolution.types.id_namespace_id_mapping_workflow_properties_list
    import capo_entityresolution.types.id_namespace_input_source_config
    import capo_entityresolution.types.id_namespace_summary
    import capo_entityresolution.types.id_namespace_type
    import capo_entityresolution.types.incremental_run_config
    import capo_entityresolution.types.input_source_config
    import capo_entityresolution.types.job_id
    import capo_entityresolution.types.job_summary
    import capo_entityresolution.types.job_type
    import capo_entityresolution.types.list_id_mapping_jobs_input
    import capo_entityresolution.types.list_id_mapping_jobs_output
    import capo_entityresolution.types.list_id_mapping_workflows_input
    import capo_entityresolution.types.list_id_mapping_workflows_output
    import capo_entityresolution.types.list_id_namespaces_input
    import capo_entityresolution.types.list_id_namespaces_output
    import capo_entityresolution.types.list_matching_jobs_input
    import capo_entityresolution.types.list_matching_jobs_output
    import capo_entityresolution.types.list_matching_workflows_input
    import capo_entityresolution.types.list_matching_workflows_output
    import capo_entityresolution.types.list_provider_services_input
    import capo_entityresolution.types.list_provider_services_output
    import capo_entityresolution.types.list_schema_mappings_input
    import capo_entityresolution.types.list_schema_mappings_output
    import capo_entityresolution.types.list_tags_for_resource_input
    import capo_entityresolution.types.list_tags_for_resource_output
    import capo_entityresolution.types.matching_workflow_summary
    import capo_entityresolution.types.next_token
    import capo_entityresolution.types.output_source_config
    import capo_entityresolution.types.policy_document
    import capo_entityresolution.types.policy_token
    import capo_entityresolution.types.processing_type
    import capo_entityresolution.types.provider_service_arn
    import capo_entityresolution.types.provider_service_summary
    import capo_entityresolution.types.put_policy_input
    import capo_entityresolution.types.put_policy_output
    import capo_entityresolution.types.record_attribute_map
    import capo_entityresolution.types.record_list
    import capo_entityresolution.types.resolution_techniques
    import capo_entityresolution.types.role_arn
    import capo_entityresolution.types.schema_input_attributes
    import capo_entityresolution.types.schema_mapping_summary
    import capo_entityresolution.types.start_id_mapping_job_input
    import capo_entityresolution.types.start_id_mapping_job_output
    import capo_entityresolution.types.start_matching_job_input
    import capo_entityresolution.types.start_matching_job_output
    import capo_entityresolution.types.statement_action_list
    import capo_entityresolution.types.statement_condition
    import capo_entityresolution.types.statement_effect
    import capo_entityresolution.types.statement_id
    import capo_entityresolution.types.statement_principal_list
    import capo_entityresolution.types.tag_key_list
    import capo_entityresolution.types.tag_map
    import capo_entityresolution.types.tag_resource_input
    import capo_entityresolution.types.tag_resource_output
    import capo_entityresolution.types.unique_id_list
    import capo_entityresolution.types.untag_resource_input
    import capo_entityresolution.types.untag_resource_output
    import capo_entityresolution.types.update_id_mapping_workflow_input
    import capo_entityresolution.types.update_id_mapping_workflow_output
    import capo_entityresolution.types.update_id_namespace_input
    import capo_entityresolution.types.update_id_namespace_output
    import capo_entityresolution.types.update_matching_workflow_input
    import capo_entityresolution.types.update_matching_workflow_output
    import capo_entityresolution.types.update_schema_mapping_input
    import capo_entityresolution.types.update_schema_mapping_output
    import capo_entityresolution.types.venice_global_arn


class EntityResolutionClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class EntityResolutionClient:
    """A client for the ``EntityResolution`` service.

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
        self._config = EntityResolutionClientConfig(
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
        self, config_overrides: Optional[EntityResolutionClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: EntityResolutionClientConfig = config_overrides or {}
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

    def add_policy_statement(
        self,
        arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn",
        statement_id: "capo_entityresolution.types.statement_id.StatementId",
        effect: "capo_entityresolution.types.statement_effect.StatementEffect",
        action: "capo_entityresolution.types.statement_action_list.StatementActionList",
        principal: "capo_entityresolution.types.statement_principal_list.StatementPrincipalList",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        condition: Optional[
            "capo_entityresolution.types.statement_condition.StatementCondition"
        ] = None,
    ) -> "capo_entityresolution.types.add_policy_statement_output.AddPolicyStatementOutput":
        """<p>Adds a policy statement object. To retrieve a list of existing policy statements, use the <code>GetPolicy</code> API.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource that will be accessed by the principal.</p>
            statement_id: <p>A statement identifier that differentiates the statement from others in the same policy.</p>
            effect: <p>Determines whether the permissions specified in the policy are to be allowed (<code>Allow</code>) or denied (<code>Deny</code>).</p> <important> <p> If you set the value of the <code>effect</code> parameter to <code>Deny</code> for the <code>AddPolicyStatement</code> operation, you must also set the value of the <code>effect</code> parameter in the <code>policy</code> to <code>Deny</code> for the <code>PutPolicy</code> operation.</p> </important>
            action: <p>The action that the principal can use on the resource. </p> <p>For example, <code>entityresolution:GetIdMappingJob</code>, <code>entityresolution:GetMatchingJob</code>.</p>
            principal: <p>The Amazon Web Services service or Amazon Web Services account that can access the resource defined as ARN.</p>
            condition: <p>A set of condition keys that you can use in key policies.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.add_policy_statement_input.AddPolicyStatementInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.add_policy_statement_output.AddPolicyStatementOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.add_policy_statement

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.add_policy_statement.add_policy_statement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.add_policy_statement_input.AddPolicyStatementInput = {
            "arn": arn,
            "statement_id": statement_id,
            "effect": effect,
            "action": action,
            "principal": principal,
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

    def batch_delete_unique_id(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        unique_ids: "capo_entityresolution.types.unique_id_list.UniqueIdList",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        input_source: Optional[str] = None,
    ) -> "capo_entityresolution.types.batch_delete_unique_id_output.BatchDeleteUniqueIdOutput":
        """<p>Deletes multiple unique IDs in a matching workflow.</p>

        Args:
            workflow_name: <p>The name of the workflow.</p>
            input_source: <p>The input source for the batch delete unique ID operation.</p>
            unique_ids: <p>The unique IDs to delete.</p>

        Raises:
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.batch_delete_unique_id_input.BatchDeleteUniqueIdInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.batch_delete_unique_id_output.BatchDeleteUniqueIdOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.batch_delete_unique_id

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.batch_delete_unique_id.batch_delete_unique_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.batch_delete_unique_id_input.BatchDeleteUniqueIdInput = {
            "workflow_name": workflow_name,
            "unique_ids": unique_ids,
        }
        if input_source is not None:
            input_["input_source"] = input_source

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_id_mapping_workflow(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        input_source_config: "capo_entityresolution.types.id_mapping_workflow_input_source_config.IdMappingWorkflowInputSourceConfig",
        id_mapping_techniques: "capo_entityresolution.types.id_mapping_techniques.IdMappingTechniques",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        description: Optional[
            "capo_entityresolution.types.description.Description"
        ] = None,
        output_source_config: Optional[
            "capo_entityresolution.types.id_mapping_workflow_output_source_config.IdMappingWorkflowOutputSourceConfig"
        ] = None,
        incremental_run_config: Optional[
            "capo_entityresolution.types.id_mapping_incremental_run_config.IdMappingIncrementalRunConfig"
        ] = None,
        role_arn: Optional[
            "capo_entityresolution.types.id_mapping_role_arn.IdMappingRoleArn"
        ] = None,
        tags: Optional["capo_entityresolution.types.tag_map.TagMap"] = None,
    ) -> "capo_entityresolution.types.create_id_mapping_workflow_output.CreateIdMappingWorkflowOutput":
        """<p>Creates an <code>IdMappingWorkflow</code> object which stores the configuration of the data processing job to be run. Each <code>IdMappingWorkflow</code> must have a unique workflow name. To modify an existing workflow, use the UpdateIdMappingWorkflow API.</p> <important> <p>Incremental processing is not supported for ID mapping workflows. </p> </important>

        Args:
            workflow_name: <p>The name of the workflow. There can't be multiple <code>IdMappingWorkflows</code> with the same name.</p>
            description: <p>A description of the workflow.</p>
            input_source_config: <p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>
            output_source_config: <p>A list of <code>IdMappingWorkflowOutputSource</code> objects, each of which contains fields <code>outputS3Path</code> and <code>KMSArn</code>.</p>
            id_mapping_techniques: <p>An object which defines the ID mapping technique and any additional configurations.</p>
            incremental_run_config: <p> The incremental run configuration for the ID mapping workflow.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.exceeds_limit_exception.ExceedsLimitException: <p>The request was rejected because it attempted to create resources beyond the current Entity Resolution account limits. The error message describes the limit exceeded. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.create_id_mapping_workflow_input.CreateIdMappingWorkflowInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.create_id_mapping_workflow_output.CreateIdMappingWorkflowOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.create_id_mapping_workflow

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.create_id_mapping_workflow.create_id_mapping_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.create_id_mapping_workflow_input.CreateIdMappingWorkflowInput = {
            "workflow_name": workflow_name,
            "input_source_config": input_source_config,
            "id_mapping_techniques": id_mapping_techniques,
        }
        if description is not None:
            input_["description"] = description
        if output_source_config is not None:
            input_["output_source_config"] = output_source_config
        if incremental_run_config is not None:
            input_["incremental_run_config"] = incremental_run_config
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_id_namespace(
        self,
        id_namespace_name: "capo_entityresolution.types.entity_name.EntityName",
        type: "capo_entityresolution.types.id_namespace_type.IdNamespaceType",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        description: Optional[
            "capo_entityresolution.types.description.Description"
        ] = None,
        input_source_config: Optional[
            "capo_entityresolution.types.id_namespace_input_source_config.IdNamespaceInputSourceConfig"
        ] = None,
        id_mapping_workflow_properties: Optional[
            "capo_entityresolution.types.id_namespace_id_mapping_workflow_properties_list.IdNamespaceIdMappingWorkflowPropertiesList"
        ] = None,
        role_arn: Optional["capo_entityresolution.types.role_arn.RoleArn"] = None,
        tags: Optional["capo_entityresolution.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_entityresolution.types.create_id_namespace_output.CreateIdNamespaceOutput"
    ):
        """<p>Creates an ID namespace object which will help customers provide metadata explaining their dataset and how to use it. Each ID namespace must have a unique name. To modify an existing ID namespace, use the UpdateIdNamespace API.</p>

        Args:
            id_namespace_name: <p>The name of the ID namespace.</p>
            description: <p>The description of the ID namespace.</p>
            input_source_config: <p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>
            id_mapping_workflow_properties: <p>Determines the properties of <code>IdMappingWorflow</code> where this <code>IdNamespace</code> can be used as a <code>Source</code> or a <code>Target</code>.</p>
            type: <p>The type of ID namespace. There are two types: <code>SOURCE</code> and <code>TARGET</code>. </p> <p>The <code>SOURCE</code> contains configurations for <code>sourceId</code> data that will be processed in an ID mapping workflow. </p> <p>The <code>TARGET</code> contains a configuration of <code>targetId</code> to which all <code>sourceIds</code> will resolve to.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to access the resources defined in this <code>IdNamespace</code> on your behalf as part of the workflow run.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.exceeds_limit_exception.ExceedsLimitException: <p>The request was rejected because it attempted to create resources beyond the current Entity Resolution account limits. The error message describes the limit exceeded. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.create_id_namespace_input.CreateIdNamespaceInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.create_id_namespace_output.CreateIdNamespaceOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.create_id_namespace

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.create_id_namespace.create_id_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.create_id_namespace_input.CreateIdNamespaceInput = {
            "id_namespace_name": id_namespace_name,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if input_source_config is not None:
            input_["input_source_config"] = input_source_config
        if id_mapping_workflow_properties is not None:
            input_["id_mapping_workflow_properties"] = id_mapping_workflow_properties
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_matching_workflow(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        input_source_config: "capo_entityresolution.types.input_source_config.InputSourceConfig",
        output_source_config: "capo_entityresolution.types.output_source_config.OutputSourceConfig",
        resolution_techniques: "capo_entityresolution.types.resolution_techniques.ResolutionTechniques",
        role_arn: str,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        description: Optional[
            "capo_entityresolution.types.description.Description"
        ] = None,
        incremental_run_config: Optional[
            "capo_entityresolution.types.incremental_run_config.IncrementalRunConfig"
        ] = None,
        tags: Optional["capo_entityresolution.types.tag_map.TagMap"] = None,
    ) -> "capo_entityresolution.types.create_matching_workflow_output.CreateMatchingWorkflowOutput":
        """<p>Creates a matching workflow that defines the configuration for a data processing job. The workflow name must be unique. To modify an existing workflow, use <code>UpdateMatchingWorkflow</code>. </p> <important> <p>For workflows where <code>resolutionType</code> is <code>PROVIDER</code>, incremental processing is not supported. </p> </important>

        Args:
            workflow_name: <p>The name of the workflow. There can't be multiple <code>MatchingWorkflows</code> with the same name.</p>
            description: <p>A description of the workflow.</p>
            input_source_config: <p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>
            output_source_config: <p>A list of <code>OutputSource</code> objects, each of which contains fields <code>outputS3Path</code>, <code>applyNormalization</code>, <code>KMSArn</code>, and <code>output</code>.</p>
            resolution_techniques: <p>An object which defines the <code>resolutionType</code> and the <code>ruleBasedProperties</code>.</p>
            incremental_run_config: <p>Optional. An object that defines the incremental run type. This object contains only the <code>incrementalRunType</code> field, which appears as "Automatic" in the console. </p> <important> <p>For workflows where <code>resolutionType</code> is <code>PROVIDER</code>, incremental processing is not supported. </p> </important>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.exceeds_limit_exception.ExceedsLimitException: <p>The request was rejected because it attempted to create resources beyond the current Entity Resolution account limits. The error message describes the limit exceeded. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.create_matching_workflow_input.CreateMatchingWorkflowInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.create_matching_workflow_output.CreateMatchingWorkflowOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.create_matching_workflow

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.create_matching_workflow.create_matching_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.create_matching_workflow_input.CreateMatchingWorkflowInput = {
            "workflow_name": workflow_name,
            "input_source_config": input_source_config,
            "output_source_config": output_source_config,
            "resolution_techniques": resolution_techniques,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if incremental_run_config is not None:
            input_["incremental_run_config"] = incremental_run_config
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_schema_mapping(
        self,
        schema_name: "capo_entityresolution.types.entity_name.EntityName",
        mapped_input_fields: "capo_entityresolution.types.schema_input_attributes.SchemaInputAttributes",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        description: Optional[
            "capo_entityresolution.types.description.Description"
        ] = None,
        tags: Optional["capo_entityresolution.types.tag_map.TagMap"] = None,
    ) -> "capo_entityresolution.types.create_schema_mapping_output.CreateSchemaMappingOutput":
        """<p>Creates a schema mapping, which defines the schema of the input customer records table. The <code>SchemaMapping</code> also provides Entity Resolution with some metadata about the table, such as the attribute types of the columns and which columns to match on.</p>

        Args:
            schema_name: <p>The name of the schema. There can't be multiple <code>SchemaMappings</code> with the same name.</p>
            description: <p>A description of the schema.</p>
            mapped_input_fields: <p>A list of <code>MappedInputFields</code>. Each <code>MappedInputField</code> corresponds to a column the source data table, and contains column name plus additional information that Entity Resolution uses for matching.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.exceeds_limit_exception.ExceedsLimitException: <p>The request was rejected because it attempted to create resources beyond the current Entity Resolution account limits. The error message describes the limit exceeded. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.create_schema_mapping_input.CreateSchemaMappingInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.create_schema_mapping_output.CreateSchemaMappingOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.create_schema_mapping

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.create_schema_mapping.create_schema_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.create_schema_mapping_input.CreateSchemaMappingInput = {
            "schema_name": schema_name,
            "mapped_input_fields": mapped_input_fields,
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

    def delete_id_mapping_workflow(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.delete_id_mapping_workflow_output.DeleteIdMappingWorkflowOutput":
        """<p>Deletes the <code>IdMappingWorkflow</code> with a given name. This operation returns a <code>ResourceNotFoundException</code> if a workflow with the given name does not exist.</p>

        Args:
            workflow_name: <p>The name of the workflow to be deleted.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.delete_id_mapping_workflow_input.DeleteIdMappingWorkflowInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.delete_id_mapping_workflow_output.DeleteIdMappingWorkflowOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.delete_id_mapping_workflow

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.delete_id_mapping_workflow.delete_id_mapping_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.delete_id_mapping_workflow_input.DeleteIdMappingWorkflowInput = {
            "workflow_name": workflow_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_id_namespace(
        self,
        id_namespace_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> (
        "capo_entityresolution.types.delete_id_namespace_output.DeleteIdNamespaceOutput"
    ):
        """<p>Deletes the <code>IdNamespace</code> with a given name. This operation returns a <code>ResourceNotFoundException</code> if an ID namespace with the given name does not exist.</p>

        Args:
            id_namespace_name: <p>The name of the ID namespace.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.delete_id_namespace_input.DeleteIdNamespaceInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.delete_id_namespace_output.DeleteIdNamespaceOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.delete_id_namespace

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.delete_id_namespace.delete_id_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.delete_id_namespace_input.DeleteIdNamespaceInput = {
            "id_namespace_name": id_namespace_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_matching_workflow(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.delete_matching_workflow_output.DeleteMatchingWorkflowOutput":
        """<p>Deletes the <code>MatchingWorkflow</code> with a given name. This operation returns a <code>ResourceNotFoundException</code> if a workflow with the given name does not exist.</p>

        Args:
            workflow_name: <p>The name of the workflow to be retrieved.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.delete_matching_workflow_input.DeleteMatchingWorkflowInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.delete_matching_workflow_output.DeleteMatchingWorkflowOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.delete_matching_workflow

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.delete_matching_workflow.delete_matching_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.delete_matching_workflow_input.DeleteMatchingWorkflowInput = {
            "workflow_name": workflow_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_policy_statement(
        self,
        arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn",
        statement_id: "capo_entityresolution.types.statement_id.StatementId",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.delete_policy_statement_output.DeletePolicyStatementOutput":
        """<p>Deletes the policy statement.</p>

        Args:
            arn: <p>The ARN of the resource for which the policy need to be deleted.</p>
            statement_id: <p>A statement identifier that differentiates the statement from others in the same policy.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.delete_policy_statement_input.DeletePolicyStatementInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.delete_policy_statement_output.DeletePolicyStatementOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.delete_policy_statement

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.delete_policy_statement.delete_policy_statement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.delete_policy_statement_input.DeletePolicyStatementInput = {
            "arn": arn,
            "statement_id": statement_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_schema_mapping(
        self,
        schema_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.delete_schema_mapping_output.DeleteSchemaMappingOutput":
        """<p>Deletes the <code>SchemaMapping</code> with a given name. This operation returns a <code>ResourceNotFoundException</code> if a schema with the given name does not exist. This operation will fail if there is a <code>MatchingWorkflow</code> object that references the <code>SchemaMapping</code> in the workflow's <code>InputSourceConfig</code>.</p>

        Args:
            schema_name: <p>The name of the schema to delete.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.delete_schema_mapping_input.DeleteSchemaMappingInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.delete_schema_mapping_output.DeleteSchemaMappingOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.delete_schema_mapping

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.delete_schema_mapping.delete_schema_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.delete_schema_mapping_input.DeleteSchemaMappingInput = {
            "schema_name": schema_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def generate_match_id(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        records: "capo_entityresolution.types.record_list.RecordList",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        processing_type: Optional[
            "capo_entityresolution.types.processing_type.ProcessingType"
        ] = None,
    ) -> "capo_entityresolution.types.generate_match_id_output.GenerateMatchIdOutput":
        """<p>Generates or retrieves Match IDs for records using a rule-based matching workflow. When you call this operation, it processes your records against the workflow's matching rules to identify potential matches. For existing records, it retrieves their Match IDs and associated rules. For records without matches, it generates new Match IDs. The operation saves results to Amazon S3. </p> <p>The processing type (<code>processingType</code>) you choose affects both the accuracy and response time of the operation. Additional charges apply for each API call, whether made through the Entity Resolution console or directly via the API. The rule-based matching workflow must exist and be active before calling this operation.</p>

        Args:
            workflow_name: <p> The name of the rule-based matching workflow.</p>
            records: <p> The records to match.</p>
            processing_type: <p>The processing mode that determines how Match IDs are generated and results are saved. Each mode provides different levels of accuracy, response time, and completeness of results.</p> <p>If not specified, defaults to <code>CONSISTENT</code>.</p> <p> <code>CONSISTENT</code>: Performs immediate lookup and matching against all existing records, with results saved synchronously. Provides highest accuracy but slower response time.</p> <p> <code>EVENTUAL</code> (shown as <i>Background</i> in the console): Performs initial match ID lookup or generation immediately, with record updates processed asynchronously in the background. Offers faster initial response time, with complete matching results available later in S3. </p> <p> <code>EVENTUAL_NO_LOOKUP</code> (shown as <i>Quick ID generation</i> in the console): Generates new match IDs without checking existing matches, with updates processed asynchronously. Provides fastest response time but should only be used for records known to be unique. </p> <note> <p>Advanced matching workflows don't support the <code>processingType</code> field.</p> </note>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.generate_match_id_input.GenerateMatchIdInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.generate_match_id_output.GenerateMatchIdOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.generate_match_id

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.generate_match_id.generate_match_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.generate_match_id_input.GenerateMatchIdInput = {
            "workflow_name": workflow_name,
            "records": records,
        }
        if processing_type is not None:
            input_["processing_type"] = processing_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_id_mapping_job(
        self,
        workflow_name: "capo_entityresolution.types.entity_name_or_id_mapping_workflow_arn.EntityNameOrIdMappingWorkflowArn",
        job_id: "capo_entityresolution.types.job_id.JobId",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.get_id_mapping_job_output.GetIdMappingJobOutput":
        """<p>Returns the status, metrics, and errors (if there are any) that are associated with a job.</p>

        Args:
            workflow_name: <p>The name of the workflow.</p>
            job_id: <p>The ID of the job.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.get_id_mapping_job_input.GetIdMappingJobInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.get_id_mapping_job_output.GetIdMappingJobOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.get_id_mapping_job

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.get_id_mapping_job.get_id_mapping_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.get_id_mapping_job_input.GetIdMappingJobInput = {
            "workflow_name": workflow_name,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_id_mapping_workflow(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.get_id_mapping_workflow_output.GetIdMappingWorkflowOutput":
        """<p>Returns the <code>IdMappingWorkflow</code> with a given name, if it exists.</p>

        Args:
            workflow_name: <p>The name of the workflow.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.get_id_mapping_workflow_input.GetIdMappingWorkflowInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.get_id_mapping_workflow_output.GetIdMappingWorkflowOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.get_id_mapping_workflow

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.get_id_mapping_workflow.get_id_mapping_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.get_id_mapping_workflow_input.GetIdMappingWorkflowInput = {
            "workflow_name": workflow_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_id_namespace(
        self,
        id_namespace_name: "capo_entityresolution.types.entity_name_or_id_namespace_arn.EntityNameOrIdNamespaceArn",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.get_id_namespace_output.GetIdNamespaceOutput":
        """<p>Returns the <code>IdNamespace</code> with a given name, if it exists.</p>

        Args:
            id_namespace_name: <p>The name of the ID namespace.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.get_id_namespace_input.GetIdNamespaceInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.get_id_namespace_output.GetIdNamespaceOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.get_id_namespace

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.get_id_namespace.get_id_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.get_id_namespace_input.GetIdNamespaceInput = {
            "id_namespace_name": id_namespace_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_match_id(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        record: "capo_entityresolution.types.record_attribute_map.RecordAttributeMap",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        apply_normalization: Optional[bool] = None,
    ) -> "capo_entityresolution.types.get_match_id_output.GetMatchIdOutput":
        """<p>Returns the corresponding Match ID of a customer record if the record has been processed in a rule-based matching workflow.</p> <p>You can call this API as a dry run of an incremental load on the rule-based matching workflow.</p>

        Args:
            workflow_name: <p>The name of the workflow.</p>
            record: <p>The record to fetch the Match ID for.</p>
            apply_normalization: <p>Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an <code>AttributeType</code> of <code>PHONE_NUMBER</code>, and the data in the input table is in a format of 1234567890, Entity Resolution will normalize this field in the output to (123)-456-7890.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.get_match_id_input.GetMatchIdInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.get_match_id_output.GetMatchIdOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.get_match_id

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.get_match_id.get_match_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.get_match_id_input.GetMatchIdInput = {
            "workflow_name": workflow_name,
            "record": record,
        }
        if apply_normalization is not None:
            input_["apply_normalization"] = apply_normalization

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_matching_job(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        job_id: "capo_entityresolution.types.job_id.JobId",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.get_matching_job_output.GetMatchingJobOutput":
        """<p>Returns the status, metrics, and errors (if there are any) that are associated with a job.</p>

        Args:
            workflow_name: <p>The name of the workflow.</p>
            job_id: <p>The ID of the job.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.get_matching_job_input.GetMatchingJobInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.get_matching_job_output.GetMatchingJobOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.get_matching_job

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.get_matching_job.get_matching_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.get_matching_job_input.GetMatchingJobInput = {
            "workflow_name": workflow_name,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_matching_workflow(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.get_matching_workflow_output.GetMatchingWorkflowOutput":
        """<p>Returns the <code>MatchingWorkflow</code> with a given name, if it exists.</p>

        Args:
            workflow_name: <p>The name of the workflow.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.get_matching_workflow_input.GetMatchingWorkflowInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.get_matching_workflow_output.GetMatchingWorkflowOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.get_matching_workflow

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.get_matching_workflow.get_matching_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.get_matching_workflow_input.GetMatchingWorkflowInput = {
            "workflow_name": workflow_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_policy(
        self,
        arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.get_policy_output.GetPolicyOutput":
        """<p>Returns the resource-based policy.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource for which the policy need to be returned.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.get_policy_input.GetPolicyInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.get_policy_output.GetPolicyOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.get_policy

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.get_policy_input.GetPolicyInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_provider_service(
        self,
        provider_name: "capo_entityresolution.types.entity_name.EntityName",
        provider_service_name: "capo_entityresolution.types.provider_service_arn.ProviderServiceArn",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.get_provider_service_output.GetProviderServiceOutput":
        """<p>Returns the <code>ProviderService</code> of a given name.</p>

        Args:
            provider_name: <p>The name of the provider. This name is typically the company name.</p>
            provider_service_name: <p>The ARN (Amazon Resource Name) of the product that the provider service provides.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.get_provider_service_input.GetProviderServiceInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.get_provider_service_output.GetProviderServiceOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.get_provider_service

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.get_provider_service.get_provider_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.get_provider_service_input.GetProviderServiceInput = {
            "provider_name": provider_name,
            "provider_service_name": provider_service_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_schema_mapping(
        self,
        schema_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.get_schema_mapping_output.GetSchemaMappingOutput":
        """<p>Returns the SchemaMapping of a given name.</p>

        Args:
            schema_name: <p>The name of the schema to be retrieved.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.get_schema_mapping_input.GetSchemaMappingInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.get_schema_mapping_output.GetSchemaMappingOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.get_schema_mapping

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.get_schema_mapping.get_schema_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.get_schema_mapping_input.GetSchemaMappingInput = {
            "schema_name": schema_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_id_mapping_jobs(
        self,
        workflow_name: "capo_entityresolution.types.entity_name_or_id_mapping_workflow_arn.EntityNameOrIdMappingWorkflowArn",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_entityresolution.types.list_id_mapping_jobs_output.ListIdMappingJobsOutput":
        """<p>Lists all ID mapping jobs for a given workflow.</p>

        Args:
            workflow_name: <p>The name of the workflow to be retrieved.</p>
            next_token: <p>The pagination token from the previous API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.list_id_mapping_jobs_input.ListIdMappingJobsInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.list_id_mapping_jobs_output.ListIdMappingJobsOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.list_id_mapping_jobs

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.list_id_mapping_jobs.list_id_mapping_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.list_id_mapping_jobs_input.ListIdMappingJobsInput = {
            "workflow_name": workflow_name
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

    def iter_list_id_mapping_jobs(
        self,
        workflow_name: "capo_entityresolution.types.entity_name_or_id_mapping_workflow_arn.EntityNameOrIdMappingWorkflowArn",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_entityresolution.types.job_summary.JobSummary]":
        _token = next_token
        while True:
            _response = self.list_id_mapping_jobs(
                workflow_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_id_mapping_workflows(
        self,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_entityresolution.types.list_id_mapping_workflows_output.ListIdMappingWorkflowsOutput":
        """<p>Returns a list of all the <code>IdMappingWorkflows</code> that have been created for an Amazon Web Services account.</p>

        Args:
            next_token: <p>The pagination token from the previous API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.list_id_mapping_workflows_input.ListIdMappingWorkflowsInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.list_id_mapping_workflows_output.ListIdMappingWorkflowsOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.list_id_mapping_workflows

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.list_id_mapping_workflows.list_id_mapping_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.list_id_mapping_workflows_input.ListIdMappingWorkflowsInput = {}
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

    def iter_list_id_mapping_workflows(
        self,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_entityresolution.types.id_mapping_workflow_summary.IdMappingWorkflowSummary]":
        _token = next_token
        while True:
            _response = self.list_id_mapping_workflows(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("workflow_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_id_namespaces(
        self,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_entityresolution.types.list_id_namespaces_output.ListIdNamespacesOutput":
        """<p>Returns a list of all ID namespaces.</p>

        Args:
            next_token: <p>The pagination token from the previous API call.</p>
            max_results: <p>The maximum number of <code>IdNamespace</code> objects returned per page.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.list_id_namespaces_input.ListIdNamespacesInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.list_id_namespaces_output.ListIdNamespacesOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.list_id_namespaces

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.list_id_namespaces.list_id_namespaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.list_id_namespaces_input.ListIdNamespacesInput = {}
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

    def iter_list_id_namespaces(
        self,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> (
        "Iterator[capo_entityresolution.types.id_namespace_summary.IdNamespaceSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_id_namespaces(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("id_namespace_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_matching_jobs(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_entityresolution.types.list_matching_jobs_output.ListMatchingJobsOutput":
        """<p>Lists all jobs for a given workflow.</p>

        Args:
            workflow_name: <p>The name of the workflow to be retrieved.</p>
            next_token: <p>The pagination token from the previous API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.list_matching_jobs_input.ListMatchingJobsInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.list_matching_jobs_output.ListMatchingJobsOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.list_matching_jobs

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.list_matching_jobs.list_matching_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.list_matching_jobs_input.ListMatchingJobsInput = {
            "workflow_name": workflow_name
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

    def iter_list_matching_jobs(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_entityresolution.types.job_summary.JobSummary]":
        _token = next_token
        while True:
            _response = self.list_matching_jobs(
                workflow_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_matching_workflows(
        self,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_entityresolution.types.list_matching_workflows_output.ListMatchingWorkflowsOutput":
        """<p>Returns a list of all the <code>MatchingWorkflows</code> that have been created for an Amazon Web Services account.</p>

        Args:
            next_token: <p>The pagination token from the previous API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.list_matching_workflows_input.ListMatchingWorkflowsInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.list_matching_workflows_output.ListMatchingWorkflowsOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.list_matching_workflows

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.list_matching_workflows.list_matching_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.list_matching_workflows_input.ListMatchingWorkflowsInput = {}
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

    def iter_list_matching_workflows(
        self,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_entityresolution.types.matching_workflow_summary.MatchingWorkflowSummary]":
        _token = next_token
        while True:
            _response = self.list_matching_workflows(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("workflow_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_provider_services(
        self,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        provider_name: Optional[
            "capo_entityresolution.types.entity_name.EntityName"
        ] = None,
    ) -> "capo_entityresolution.types.list_provider_services_output.ListProviderServicesOutput":
        """<p>Returns a list of all the <code>ProviderServices</code> that are available in this Amazon Web Services Region.</p>

        Args:
            next_token: <p>The pagination token from the previous API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>
            provider_name: <p>The name of the provider. This name is typically the company name.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.list_provider_services_input.ListProviderServicesInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.list_provider_services_output.ListProviderServicesOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.list_provider_services

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.list_provider_services.list_provider_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.list_provider_services_input.ListProviderServicesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if provider_name is not None:
            input_["provider_name"] = provider_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_provider_services(
        self,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
        provider_name: Optional[
            "capo_entityresolution.types.entity_name.EntityName"
        ] = None,
    ) -> "Iterator[capo_entityresolution.types.provider_service_summary.ProviderServiceSummary]":
        _token = next_token
        while True:
            _response = self.list_provider_services(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                provider_name=provider_name,
            )
            _page = _resolve_path(_response, ("provider_service_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_schema_mappings(
        self,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_entityresolution.types.list_schema_mappings_output.ListSchemaMappingsOutput":
        """<p>Returns a list of all the <code>SchemaMappings</code> that have been created for an Amazon Web Services account.</p>

        Args:
            next_token: <p>The pagination token from the previous API call.</p>
            max_results: <p>The maximum number of objects returned per page.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.list_schema_mappings_input.ListSchemaMappingsInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.list_schema_mappings_output.ListSchemaMappingsOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.list_schema_mappings

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.list_schema_mappings.list_schema_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.list_schema_mappings_input.ListSchemaMappingsInput = {}
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

    def iter_list_schema_mappings(
        self,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        next_token: Optional["capo_entityresolution.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_entityresolution.types.schema_mapping_summary.SchemaMappingSummary]":
        _token = next_token
        while True:
            _response = self.list_schema_mappings(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("schema_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Displays the tags associated with an Entity Resolution resource. In Entity Resolution, <code>SchemaMapping</code>, and <code>MatchingWorkflow</code> can be tagged.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to view tags.</p>

        Raises:
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.list_tags_for_resource

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_policy(
        self,
        arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn",
        policy: "capo_entityresolution.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        token: Optional["capo_entityresolution.types.policy_token.PolicyToken"] = None,
    ) -> "capo_entityresolution.types.put_policy_output.PutPolicyOutput":
        """<p>Updates the resource-based policy.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource for which the policy needs to be updated.</p>
            token: <p>A unique identifier for the current revision of the policy.</p>
            policy: <p>The resource-based policy.</p> <important> <p>If you set the value of the <code>effect</code> parameter in the <code>policy</code> to <code>Deny</code> for the <code>PutPolicy</code> operation, you must also set the value of the <code>effect</code> parameter to <code>Deny</code> for the <code>AddPolicyStatement</code> operation.</p> </important>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.put_policy_input.PutPolicyInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.put_policy_output.PutPolicyOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.put_policy

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.put_policy.put_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.put_policy_input.PutPolicyInput = {
            "arn": arn,
            "policy": policy,
        }
        if token is not None:
            input_["token"] = token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_id_mapping_job(
        self,
        workflow_name: "capo_entityresolution.types.entity_name_or_id_mapping_workflow_arn.EntityNameOrIdMappingWorkflowArn",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        output_source_config: Optional[
            "capo_entityresolution.types.id_mapping_job_output_source_config.IdMappingJobOutputSourceConfig"
        ] = None,
        job_type: Optional["capo_entityresolution.types.job_type.JobType"] = None,
    ) -> "capo_entityresolution.types.start_id_mapping_job_output.StartIdMappingJobOutput":
        """<p>Starts the <code>IdMappingJob</code> of a workflow. The workflow must have previously been created using the <code>CreateIdMappingWorkflow</code> endpoint.</p>

        Args:
            workflow_name: <p>The name of the ID mapping job to be retrieved.</p>
            output_source_config: <p>A list of <code>OutputSource</code> objects.</p>
            job_type: <p> The job type for the ID mapping job.</p> <p>If the <code>jobType</code> value is set to <code>INCREMENTAL</code>, only new or changed data is processed since the last job run. This is the default value if the <code>CreateIdMappingWorkflow</code> API is configured with an <code>incrementalRunConfig</code>.</p> <p>If the <code>jobType</code> value is set to <code>BATCH</code>, all data is processed from the input source, regardless of previous job runs. This is the default value if the <code>CreateIdMappingWorkflow</code> API isn't configured with an <code>incrementalRunConfig</code>.</p> <p>If the <code>jobType</code> value is set to <code>DELETE_ONLY</code>, only deletion requests from <code>BatchDeleteUniqueIds</code> are processed.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.exceeds_limit_exception.ExceedsLimitException: <p>The request was rejected because it attempted to create resources beyond the current Entity Resolution account limits. The error message describes the limit exceeded. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.start_id_mapping_job_input.StartIdMappingJobInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.start_id_mapping_job_output.StartIdMappingJobOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.start_id_mapping_job

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.start_id_mapping_job.start_id_mapping_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.start_id_mapping_job_input.StartIdMappingJobInput = {
            "workflow_name": workflow_name
        }
        if output_source_config is not None:
            input_["output_source_config"] = output_source_config
        if job_type is not None:
            input_["job_type"] = job_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_matching_job(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.start_matching_job_output.StartMatchingJobOutput":
        """<p>Starts the <code>MatchingJob</code> of a workflow. The workflow must have previously been created using the <code>CreateMatchingWorkflow</code> endpoint.</p>

        Args:
            workflow_name: <p>The name of the matching job to be retrieved.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.exceeds_limit_exception.ExceedsLimitException: <p>The request was rejected because it attempted to create resources beyond the current Entity Resolution account limits. The error message describes the limit exceeded. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.start_matching_job_input.StartMatchingJobInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.start_matching_job_output.StartMatchingJobOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.start_matching_job

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.start_matching_job.start_matching_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.start_matching_job_input.StartMatchingJobInput = {
            "workflow_name": workflow_name
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
        resource_arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn",
        tags: "capo_entityresolution.types.tag_map.TagMap",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.tag_resource_output.TagResourceOutput":
        """<p>Assigns one or more tags (key-value pairs) to the specified Entity Resolution resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In Entity Resolution, <code>SchemaMapping</code> and <code>MatchingWorkflow</code> can be tagged. Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters. You can use the <code>TagResource</code> action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to view tags.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.tag_resource

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_entityresolution.types.venice_global_arn.VeniceGlobalArn",
        tag_keys: "capo_entityresolution.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
    ) -> "capo_entityresolution.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes one or more tags from the specified Entity Resolution resource. In Entity Resolution, <code>SchemaMapping</code>, and <code>MatchingWorkflow</code> can be tagged.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to untag.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.untag_resource

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.untag_resource_input.UntagResourceInput = {
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

    def update_id_mapping_workflow(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        input_source_config: "capo_entityresolution.types.id_mapping_workflow_input_source_config.IdMappingWorkflowInputSourceConfig",
        id_mapping_techniques: "capo_entityresolution.types.id_mapping_techniques.IdMappingTechniques",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        description: Optional[
            "capo_entityresolution.types.description.Description"
        ] = None,
        output_source_config: Optional[
            "capo_entityresolution.types.id_mapping_workflow_output_source_config.IdMappingWorkflowOutputSourceConfig"
        ] = None,
        incremental_run_config: Optional[
            "capo_entityresolution.types.id_mapping_incremental_run_config.IdMappingIncrementalRunConfig"
        ] = None,
        role_arn: Optional[
            "capo_entityresolution.types.id_mapping_role_arn.IdMappingRoleArn"
        ] = None,
    ) -> "capo_entityresolution.types.update_id_mapping_workflow_output.UpdateIdMappingWorkflowOutput":
        """<p>Updates an existing <code>IdMappingWorkflow</code>. This method is identical to CreateIdMappingWorkflow, except it uses an HTTP <code>PUT</code> request instead of a <code>POST</code> request, and the <code>IdMappingWorkflow</code> must already exist for the method to succeed.</p> <important> <p>Incremental processing is not supported for ID mapping workflows. </p> </important>

        Args:
            workflow_name: <p>The name of the workflow.</p>
            description: <p>A description of the workflow.</p>
            input_source_config: <p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>
            output_source_config: <p>A list of <code>OutputSource</code> objects, each of which contains fields <code>outputS3Path</code> and <code>KMSArn</code>.</p>
            id_mapping_techniques: <p>An object which defines the ID mapping technique and any additional configurations.</p>
            incremental_run_config: <p> The incremental run configuration for the update ID mapping workflow.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to access Amazon Web Services resources on your behalf.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.update_id_mapping_workflow_input.UpdateIdMappingWorkflowInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.update_id_mapping_workflow_output.UpdateIdMappingWorkflowOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.update_id_mapping_workflow

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.update_id_mapping_workflow.update_id_mapping_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.update_id_mapping_workflow_input.UpdateIdMappingWorkflowInput = {
            "workflow_name": workflow_name,
            "input_source_config": input_source_config,
            "id_mapping_techniques": id_mapping_techniques,
        }
        if description is not None:
            input_["description"] = description
        if output_source_config is not None:
            input_["output_source_config"] = output_source_config
        if incremental_run_config is not None:
            input_["incremental_run_config"] = incremental_run_config
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_id_namespace(
        self,
        id_namespace_name: "capo_entityresolution.types.entity_name.EntityName",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        description: Optional[
            "capo_entityresolution.types.description.Description"
        ] = None,
        input_source_config: Optional[
            "capo_entityresolution.types.id_namespace_input_source_config.IdNamespaceInputSourceConfig"
        ] = None,
        id_mapping_workflow_properties: Optional[
            "capo_entityresolution.types.id_namespace_id_mapping_workflow_properties_list.IdNamespaceIdMappingWorkflowPropertiesList"
        ] = None,
        role_arn: Optional["capo_entityresolution.types.role_arn.RoleArn"] = None,
    ) -> (
        "capo_entityresolution.types.update_id_namespace_output.UpdateIdNamespaceOutput"
    ):
        """<p>Updates an existing ID namespace.</p>

        Args:
            id_namespace_name: <p>The name of the ID namespace.</p>
            description: <p>The description of the ID namespace.</p>
            input_source_config: <p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>
            id_mapping_workflow_properties: <p>Determines the properties of <code>IdMappingWorkflow</code> where this <code>IdNamespace</code> can be used as a <code>Source</code> or a <code>Target</code>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to access the resources defined in this <code>IdNamespace</code> on your behalf as part of a workflow run.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.update_id_namespace_input.UpdateIdNamespaceInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.update_id_namespace_output.UpdateIdNamespaceOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.update_id_namespace

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.update_id_namespace.update_id_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.update_id_namespace_input.UpdateIdNamespaceInput = {
            "id_namespace_name": id_namespace_name
        }
        if description is not None:
            input_["description"] = description
        if input_source_config is not None:
            input_["input_source_config"] = input_source_config
        if id_mapping_workflow_properties is not None:
            input_["id_mapping_workflow_properties"] = id_mapping_workflow_properties
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_matching_workflow(
        self,
        workflow_name: "capo_entityresolution.types.entity_name.EntityName",
        input_source_config: "capo_entityresolution.types.input_source_config.InputSourceConfig",
        output_source_config: "capo_entityresolution.types.output_source_config.OutputSourceConfig",
        resolution_techniques: "capo_entityresolution.types.resolution_techniques.ResolutionTechniques",
        role_arn: str,
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        description: Optional[
            "capo_entityresolution.types.description.Description"
        ] = None,
        incremental_run_config: Optional[
            "capo_entityresolution.types.incremental_run_config.IncrementalRunConfig"
        ] = None,
    ) -> "capo_entityresolution.types.update_matching_workflow_output.UpdateMatchingWorkflowOutput":
        """<p>Updates an existing matching workflow. The workflow must already exist for this operation to succeed.</p> <important> <p>For workflows where <code>resolutionType</code> is <code>PROVIDER</code>, incremental processing is not supported. </p> </important>

        Args:
            workflow_name: <p>The name of the workflow to be retrieved.</p>
            description: <p>A description of the workflow.</p>
            input_source_config: <p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>
            output_source_config: <p>A list of <code>OutputSource</code> objects, each of which contains fields <code>outputS3Path</code>, <code>applyNormalization</code>, <code>KMSArn</code>, and <code>output</code>.</p>
            resolution_techniques: <p>An object which defines the <code>resolutionType</code> and the <code>ruleBasedProperties</code>.</p>
            incremental_run_config: <p>Optional. An object that defines the incremental run type. This object contains only the <code>incrementalRunType</code> field, which appears as "Automatic" in the console. </p> <important> <p>For workflows where <code>resolutionType</code> is <code>PROVIDER</code>, incremental processing is not supported. </p> </important>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.update_matching_workflow_input.UpdateMatchingWorkflowInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.update_matching_workflow_output.UpdateMatchingWorkflowOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.update_matching_workflow

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.update_matching_workflow.update_matching_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.update_matching_workflow_input.UpdateMatchingWorkflowInput = {
            "workflow_name": workflow_name,
            "input_source_config": input_source_config,
            "output_source_config": output_source_config,
            "resolution_techniques": resolution_techniques,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if incremental_run_config is not None:
            input_["incremental_run_config"] = incremental_run_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_schema_mapping(
        self,
        schema_name: "capo_entityresolution.types.entity_name.EntityName",
        mapped_input_fields: "capo_entityresolution.types.schema_input_attributes.SchemaInputAttributes",
        *,
        config_overrides: Optional[EntityResolutionClientConfig] = None,
        description: Optional[
            "capo_entityresolution.types.description.Description"
        ] = None,
    ) -> "capo_entityresolution.types.update_schema_mapping_output.UpdateSchemaMappingOutput":
        """<p>Updates a schema mapping.</p> <note> <p>A schema is immutable if it is being used by a workflow. Therefore, you can't update a schema mapping if it's associated with a workflow. </p> </note>

        Args:
            schema_name: <p>The name of the schema. There can't be multiple <code>SchemaMappings</code> with the same name.</p>
            description: <p>A description of the schema.</p>
            mapped_input_fields: <p>A list of <code>MappedInputFields</code>. Each <code>MappedInputField</code> corresponds to a column the source data table, and contains column name plus additional information that Entity Resolution uses for matching.</p>

        Raises:
            capo_entityresolution.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_entityresolution.errors.conflict_exception.ConflictException: <p>The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc. </p>
            capo_entityresolution.errors.internal_server_exception.InternalServerException: <p>This exception occurs when there is an internal failure in the Entity Resolution service. </p>
            capo_entityresolution.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource couldn't be found. </p>
            capo_entityresolution.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_entityresolution.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by Entity Resolution. </p>
            capo_entityresolution.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_entityresolution.types.update_schema_mapping_input.UpdateSchemaMappingInput]",
        ) -> OperationResponse[
            "capo_entityresolution.types.update_schema_mapping_output.UpdateSchemaMappingOutput"
        ]:
            import capo_entityresolution._operations.aws_venice_service.update_schema_mapping

            output, http_response = (
                capo_entityresolution._operations.aws_venice_service.update_schema_mapping.update_schema_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_entityresolution.types.update_schema_mapping_input.UpdateSchemaMappingInput = {
            "schema_name": schema_name,
            "mapped_input_fields": mapped_input_fields,
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
