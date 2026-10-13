from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_mwaa_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.code
    import capo_mwaa_serverless.types.create_workflow_request
    import capo_mwaa_serverless.types.create_workflow_response
    import capo_mwaa_serverless.types.definition_s3_location
    import capo_mwaa_serverless.types.delete_workflow_request
    import capo_mwaa_serverless.types.delete_workflow_response
    import capo_mwaa_serverless.types.description_string
    import capo_mwaa_serverless.types.encryption_configuration
    import capo_mwaa_serverless.types.engine_version
    import capo_mwaa_serverless.types.generic_string
    import capo_mwaa_serverless.types.get_workflow_request
    import capo_mwaa_serverless.types.get_workflow_response
    import capo_mwaa_serverless.types.idempotency_token_string
    import capo_mwaa_serverless.types.list_workflows_request
    import capo_mwaa_serverless.types.list_workflows_response
    import capo_mwaa_serverless.types.logging_configuration
    import capo_mwaa_serverless.types.name_string
    import capo_mwaa_serverless.types.network_configuration
    import capo_mwaa_serverless.types.role_arn
    import capo_mwaa_serverless.types.tags
    import capo_mwaa_serverless.types.update_workflow_request
    import capo_mwaa_serverless.types.update_workflow_response
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_summary
    import capo_mwaa_serverless.types.workflow_version
    from capo_mwaa_serverless._services.async_mwaa_serverless import (
        AsyncMWAAServerlessClient,
        AsyncMWAAServerlessClientConfig,
    )
    from capo_mwaa_serverless._services.mwaa_serverless import (
        MWAAServerlessClient,
        MWAAServerlessClientConfig,
    )


class WorkflowResource:
    def __init__(self, service: MWAAServerlessClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_mwaa_serverless.types.name_string.NameString",
        definition_s3_location: "capo_mwaa_serverless.types.definition_s3_location.DefinitionS3Location",
        role_arn: "capo_mwaa_serverless.types.role_arn.RoleARN",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        client_token: Optional[
            "capo_mwaa_serverless.types.idempotency_token_string.IdempotencyTokenString"
        ] = None,
        code: Optional["capo_mwaa_serverless.types.code.Code"] = None,
        description: Optional[
            "capo_mwaa_serverless.types.description_string.DescriptionString"
        ] = None,
        encryption_configuration: Optional[
            "capo_mwaa_serverless.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        logging_configuration: Optional[
            "capo_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
        ] = None,
        engine_version: Optional[
            "capo_mwaa_serverless.types.engine_version.EngineVersion"
        ] = None,
        network_configuration: Optional[
            "capo_mwaa_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        tags: Optional["capo_mwaa_serverless.types.tags.Tags"] = None,
        trigger_mode: Optional[
            "capo_mwaa_serverless.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_mwaa_serverless.types.create_workflow_response.CreateWorkflowResponse":
        """<p>Creates a new workflow in Amazon Managed Workflows for Apache Airflow Serverless. This operation initializes a workflow with the specified configuration including the workflow definition, execution role, and optional settings for encryption, logging, and networking. You must provide the workflow definition as a YAML file stored in Amazon S3 that defines the DAG structure using supported Amazon Web Services operators. Amazon Managed Workflows for Apache Airflow Serverless automatically creates the first version of the workflow and sets up the necessary execution environment with multi-tenant isolation and security controls.</p>

        Args:
            name: <p>The name of the workflow. You must use unique workflow names within your Amazon Web Services account. The service generates a unique identifier that is appended to ensure temporal uniqueness across the account lifecycle.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow creation requests.</p>
            definition_s3_location: <p>The Amazon S3 location where the workflow definition file is stored. This must point to a valid YAML file that defines the workflow structure using supported Amazon Web Services operators and tasks. Amazon Managed Workflows for Apache Airflow Serverless takes a snapshot of the definition at creation time, so subsequent changes to the Amazon S3 object will not affect the workflow unless you create a new version. In your YAML definition, include task dependencies, scheduling information, and operator configurations that are compatible with the Amazon Managed Workflows for Apache Airflow Serverless execution environment.</p>
            code: <p>The location of code artifacts in Amazon S3 for the workflow. The service copies the code from this location at the time of the request.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when executing the workflow. This role must have the necessary permissions to access the required Amazon Web Services services and resources that your workflow tasks will interact with. The role is used for task execution in the isolated, multi-tenant environment and should follow the principle of least privilege. Amazon Managed Workflows for Apache Airflow Serverless validates role access during workflow creation but runtime permission checks are performed by the target services.</p>
            description: <p>An optional description of the workflow that you can use to provide additional context about the workflow's purpose and functionality.</p>
            encryption_configuration: <p>The configuration for encrypting workflow data at rest and in transit. Specifies the encryption type and optional KMS key for customer-managed encryption.</p>
            logging_configuration: <p>The configuration for workflow logging. Specifies the CloudWatch log group where workflow execution logs are stored. Amazon Managed Workflows for Apache Airflow Serverless automatically exports worker logs and task-level information to the specified log group in your account using remote logging functionality. This provides comprehensive observability for debugging and monitoring workflow execution across the distributed, serverless environment.</p>
            engine_version: <p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for this workflow. This determines the feature set, supported operators, and execution environment capabilities available to your workflow. Amazon Managed Workflows for Apache Airflow Serverless maintains backward compatibility across versions while introducing new features and improvements. Currently supports version 1 with plans for additional versions as the service evolves.</p>
            network_configuration: <p>Network configuration for the workflow execution environment, including VPC security groups and subnets for secure network access. When specified, Amazon Managed Workflows for Apache Airflow Serverless deploys ECS worker tasks in your customer VPC to provide secure connectivity to your resources. If not specified, tasks run in the service's default worker VPC with network isolation from other customers. This configuration enables secure access to VPC-only resources like RDS databases or private endpoints.</p>
            tags: <p>A map of tags to assign to the workflow resource. Tags are key-value pairs that are used for resource organization and cost allocation.</p>
            trigger_mode: <p>The trigger mode for the workflow execution.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.conflict_exception.ConflictException: <p>You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for Amazon Managed Workflows for Apache Airflow Serverless resources. This can occur when you attempt to create more workflows than allowed, exceed concurrent workflow run limits, or surpass task execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements admission control using DynamoDB-based counters to manage resource utilization across the multi-tenant environment. Contact Amazon Web Services Support to request quota increases if you need higher limits for your use case.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.create_workflow

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.create_workflow.create_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateWorkflow")
        )
        input_: capo_mwaa_serverless.types.create_workflow_request.CreateWorkflowRequest = {
            "name": name,
            "definition_s3_location": definition_s3_location,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if code is not None:
            input_["code"] = code
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if tags is not None:
            input_["tags"] = tags
        if trigger_mode is not None:
            input_["trigger_mode"] = trigger_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
        ] = None,
    ) -> "capo_mwaa_serverless.types.get_workflow_response.GetWorkflowResponse":
        """<p>Retrieves detailed information about a workflow, including its configuration, status, and metadata.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to retrieve.</p>
            workflow_version: <p>Optional. The specific version of the workflow to retrieve. If not specified, the latest version is returned.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.get_workflow_request.GetWorkflowRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow.get_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWorkflow")
        )
        input_: capo_mwaa_serverless.types.get_workflow_request.GetWorkflowRequest = {
            "workflow_arn": workflow_arn
        }
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        definition_s3_location: "capo_mwaa_serverless.types.definition_s3_location.DefinitionS3Location",
        role_arn: "capo_mwaa_serverless.types.role_arn.RoleARN",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        code: Optional["capo_mwaa_serverless.types.code.Code"] = None,
        description: Optional[
            "capo_mwaa_serverless.types.description_string.DescriptionString"
        ] = None,
        logging_configuration: Optional[
            "capo_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
        ] = None,
        engine_version: Optional[
            "capo_mwaa_serverless.types.engine_version.EngineVersion"
        ] = None,
        network_configuration: Optional[
            "capo_mwaa_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        trigger_mode: Optional[
            "capo_mwaa_serverless.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_mwaa_serverless.types.update_workflow_response.UpdateWorkflowResponse":
        """<p>Updates an existing workflow with new configuration settings. This operation allows you to modify the workflow definition, role, and other settings. When you update a workflow, Amazon Managed Workflows for Apache Airflow Serverless automatically creates a new version with the updated configuration and disables scheduling on all previous versions to ensure only one version is actively scheduled at a time. The update operation maintains workflow history while providing a clean transition to the new configuration.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to update.</p>
            definition_s3_location: <p>The Amazon S3 location where the updated workflow definition file is stored.</p>
            code: <p>The location of code artifacts in Amazon S3 for the updated workflow. The service copies the code from this location at the time of the request.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when it executes the updated workflow.</p>
            description: <p>An updated description for the workflow.</p>
            logging_configuration: <p>Updated logging configuration for the workflow.</p>
            engine_version: <p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for the updated workflow.</p>
            network_configuration: <p>Updated network configuration for the workflow execution environment.</p>
            trigger_mode: <p>The trigger mode for the workflow execution.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.conflict_exception.ConflictException: <p>You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for Amazon Managed Workflows for Apache Airflow Serverless resources. This can occur when you attempt to create more workflows than allowed, exceed concurrent workflow run limits, or surpass task execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements admission control using DynamoDB-based counters to manage resource utilization across the multi-tenant environment. Contact Amazon Web Services Support to request quota increases if you need higher limits for your use case.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.update_workflow_request.UpdateWorkflowRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.update_workflow_response.UpdateWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.update_workflow

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.update_workflow.update_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateWorkflow")
        )
        input_: capo_mwaa_serverless.types.update_workflow_request.UpdateWorkflowRequest = {
            "workflow_arn": workflow_arn,
            "definition_s3_location": definition_s3_location,
            "role_arn": role_arn,
        }
        if code is not None:
            input_["code"] = code
        if description is not None:
            input_["description"] = description
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if trigger_mode is not None:
            input_["trigger_mode"] = trigger_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
        ] = None,
    ) -> "capo_mwaa_serverless.types.delete_workflow_response.DeleteWorkflowResponse":
        """<p>Deletes a workflow and all its versions. This operation permanently removes the workflow and cannot be undone. Amazon Managed Workflows for Apache Airflow Serverless ensures that all associated resources are properly cleaned up, including stopping any running executions, removing scheduled triggers, and cleaning up execution history. The deletion process respects the multi-tenant isolation boundaries and ensures that no residual data or configurations remain that could affect other customers or workflows.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to delete.</p>
            workflow_version: <p>Optional. The specific version of the workflow to delete. If not specified, all versions of the workflow are deleted.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.delete_workflow_response.DeleteWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.delete_workflow

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.delete_workflow.delete_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflow")
        )
        input_: capo_mwaa_serverless.types.delete_workflow_request.DeleteWorkflowRequest = {
            "workflow_arn": workflow_arn
        }
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

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
        config_overrides: Optional[MWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mwaa_serverless.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Lists all workflows in your account, with optional pagination support. This operation returns summary information for workflows, showing only the most recently created version of each workflow. Amazon Managed Workflows for Apache Airflow Serverless maintains workflow metadata in a highly available, distributed storage system that enables efficient querying and filtering. The service implements proper access controls to ensure you can only view workflows that you have permissions to access, supporting both individual and team-based workflow management scenarios.</p>

        Args:
            max_results: <p>The maximum number of workflows you want to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflows</code>.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mwaa_serverless.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> OperationResponse[
            "capo_mwaa_serverless.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflows

            output, http_response = (
                capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflows.list_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflows")
        )
        input_: capo_mwaa_serverless.types.list_workflows_request.ListWorkflowsRequest = {}
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


class AsyncWorkflowResource:
    def __init__(self, service: AsyncMWAAServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_mwaa_serverless.types.name_string.NameString",
        definition_s3_location: "capo_mwaa_serverless.types.definition_s3_location.DefinitionS3Location",
        role_arn: "capo_mwaa_serverless.types.role_arn.RoleARN",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        client_token: Optional[
            "capo_mwaa_serverless.types.idempotency_token_string.IdempotencyTokenString"
        ] = None,
        code: Optional["capo_mwaa_serverless.types.code.Code"] = None,
        description: Optional[
            "capo_mwaa_serverless.types.description_string.DescriptionString"
        ] = None,
        encryption_configuration: Optional[
            "capo_mwaa_serverless.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        logging_configuration: Optional[
            "capo_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
        ] = None,
        engine_version: Optional[
            "capo_mwaa_serverless.types.engine_version.EngineVersion"
        ] = None,
        network_configuration: Optional[
            "capo_mwaa_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        tags: Optional["capo_mwaa_serverless.types.tags.Tags"] = None,
        trigger_mode: Optional[
            "capo_mwaa_serverless.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_mwaa_serverless.types.create_workflow_response.CreateWorkflowResponse":
        """<p>Creates a new workflow in Amazon Managed Workflows for Apache Airflow Serverless. This operation initializes a workflow with the specified configuration including the workflow definition, execution role, and optional settings for encryption, logging, and networking. You must provide the workflow definition as a YAML file stored in Amazon S3 that defines the DAG structure using supported Amazon Web Services operators. Amazon Managed Workflows for Apache Airflow Serverless automatically creates the first version of the workflow and sets up the necessary execution environment with multi-tenant isolation and security controls.</p>

        Args:
            name: <p>The name of the workflow. You must use unique workflow names within your Amazon Web Services account. The service generates a unique identifier that is appended to ensure temporal uniqueness across the account lifecycle.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token prevents duplicate workflow creation requests.</p>
            definition_s3_location: <p>The Amazon S3 location where the workflow definition file is stored. This must point to a valid YAML file that defines the workflow structure using supported Amazon Web Services operators and tasks. Amazon Managed Workflows for Apache Airflow Serverless takes a snapshot of the definition at creation time, so subsequent changes to the Amazon S3 object will not affect the workflow unless you create a new version. In your YAML definition, include task dependencies, scheduling information, and operator configurations that are compatible with the Amazon Managed Workflows for Apache Airflow Serverless execution environment.</p>
            code: <p>The location of code artifacts in Amazon S3 for the workflow. The service copies the code from this location at the time of the request.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when executing the workflow. This role must have the necessary permissions to access the required Amazon Web Services services and resources that your workflow tasks will interact with. The role is used for task execution in the isolated, multi-tenant environment and should follow the principle of least privilege. Amazon Managed Workflows for Apache Airflow Serverless validates role access during workflow creation but runtime permission checks are performed by the target services.</p>
            description: <p>An optional description of the workflow that you can use to provide additional context about the workflow's purpose and functionality.</p>
            encryption_configuration: <p>The configuration for encrypting workflow data at rest and in transit. Specifies the encryption type and optional KMS key for customer-managed encryption.</p>
            logging_configuration: <p>The configuration for workflow logging. Specifies the CloudWatch log group where workflow execution logs are stored. Amazon Managed Workflows for Apache Airflow Serverless automatically exports worker logs and task-level information to the specified log group in your account using remote logging functionality. This provides comprehensive observability for debugging and monitoring workflow execution across the distributed, serverless environment.</p>
            engine_version: <p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for this workflow. This determines the feature set, supported operators, and execution environment capabilities available to your workflow. Amazon Managed Workflows for Apache Airflow Serverless maintains backward compatibility across versions while introducing new features and improvements. Currently supports version 1 with plans for additional versions as the service evolves.</p>
            network_configuration: <p>Network configuration for the workflow execution environment, including VPC security groups and subnets for secure network access. When specified, Amazon Managed Workflows for Apache Airflow Serverless deploys ECS worker tasks in your customer VPC to provide secure connectivity to your resources. If not specified, tasks run in the service's default worker VPC with network isolation from other customers. This configuration enables secure access to VPC-only resources like RDS databases or private endpoints.</p>
            tags: <p>A map of tags to assign to the workflow resource. Tags are key-value pairs that are used for resource organization and cost allocation.</p>
            trigger_mode: <p>The trigger mode for the workflow execution.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.conflict_exception.ConflictException: <p>You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for Amazon Managed Workflows for Apache Airflow Serverless resources. This can occur when you attempt to create more workflows than allowed, exceed concurrent workflow run limits, or surpass task execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements admission control using DynamoDB-based counters to manage resource utilization across the multi-tenant environment. Contact Amazon Web Services Support to request quota increases if you need higher limits for your use case.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.create_workflow

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.create_workflow.async_create_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateWorkflow")
        )
        input_: capo_mwaa_serverless.types.create_workflow_request.CreateWorkflowRequest = {
            "name": name,
            "definition_s3_location": definition_s3_location,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if code is not None:
            input_["code"] = code
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if tags is not None:
            input_["tags"] = tags
        if trigger_mode is not None:
            input_["trigger_mode"] = trigger_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
        ] = None,
    ) -> "capo_mwaa_serverless.types.get_workflow_response.GetWorkflowResponse":
        """<p>Retrieves detailed information about a workflow, including its configuration, status, and metadata.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to retrieve.</p>
            workflow_version: <p>Optional. The specific version of the workflow to retrieve. If not specified, the latest version is returned.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.get_workflow_request.GetWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.get_workflow.async_get_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWorkflow")
        )
        input_: capo_mwaa_serverless.types.get_workflow_request.GetWorkflowRequest = {
            "workflow_arn": workflow_arn
        }
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        definition_s3_location: "capo_mwaa_serverless.types.definition_s3_location.DefinitionS3Location",
        role_arn: "capo_mwaa_serverless.types.role_arn.RoleARN",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        code: Optional["capo_mwaa_serverless.types.code.Code"] = None,
        description: Optional[
            "capo_mwaa_serverless.types.description_string.DescriptionString"
        ] = None,
        logging_configuration: Optional[
            "capo_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
        ] = None,
        engine_version: Optional[
            "capo_mwaa_serverless.types.engine_version.EngineVersion"
        ] = None,
        network_configuration: Optional[
            "capo_mwaa_serverless.types.network_configuration.NetworkConfiguration"
        ] = None,
        trigger_mode: Optional[
            "capo_mwaa_serverless.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_mwaa_serverless.types.update_workflow_response.UpdateWorkflowResponse":
        """<p>Updates an existing workflow with new configuration settings. This operation allows you to modify the workflow definition, role, and other settings. When you update a workflow, Amazon Managed Workflows for Apache Airflow Serverless automatically creates a new version with the updated configuration and disables scheduling on all previous versions to ensure only one version is actively scheduled at a time. The update operation maintains workflow history while providing a clean transition to the new configuration.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to update.</p>
            definition_s3_location: <p>The Amazon S3 location where the updated workflow definition file is stored.</p>
            code: <p>The location of code artifacts in Amazon S3 for the updated workflow. The service copies the code from this location at the time of the request.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Amazon Managed Workflows for Apache Airflow Serverless assumes when it executes the updated workflow.</p>
            description: <p>An updated description for the workflow.</p>
            logging_configuration: <p>Updated logging configuration for the workflow.</p>
            engine_version: <p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that you want to use for the updated workflow.</p>
            network_configuration: <p>Updated network configuration for the workflow execution environment.</p>
            trigger_mode: <p>The trigger mode for the workflow execution.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.conflict_exception.ConflictException: <p>You cannot create a resource that already exists, or the resource is in a state that prevents the requested operation.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota for Amazon Managed Workflows for Apache Airflow Serverless resources. This can occur when you attempt to create more workflows than allowed, exceed concurrent workflow run limits, or surpass task execution limits. Amazon Managed Workflows for Apache Airflow Serverless implements admission control using DynamoDB-based counters to manage resource utilization across the multi-tenant environment. Contact Amazon Web Services Support to request quota increases if you need higher limits for your use case.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.update_workflow_request.UpdateWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.update_workflow_response.UpdateWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.update_workflow

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.update_workflow.async_update_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateWorkflow")
        )
        input_: capo_mwaa_serverless.types.update_workflow_request.UpdateWorkflowRequest = {
            "workflow_arn": workflow_arn,
            "definition_s3_location": definition_s3_location,
            "role_arn": role_arn,
        }
        if code is not None:
            input_["code"] = code
        if description is not None:
            input_["description"] = description
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if trigger_mode is not None:
            input_["trigger_mode"] = trigger_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn",
        *,
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        workflow_version: Optional[
            "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
        ] = None,
    ) -> "capo_mwaa_serverless.types.delete_workflow_response.DeleteWorkflowResponse":
        """<p>Deletes a workflow and all its versions. This operation permanently removes the workflow and cannot be undone. Amazon Managed Workflows for Apache Airflow Serverless ensures that all associated resources are properly cleaned up, including stopping any running executions, removing scheduled triggers, and cleaning up execution history. The deletion process respects the multi-tenant isolation boundaries and ensures that no residual data or configurations remain that could affect other customers or workflows.</p>

        Args:
            workflow_arn: <p>The Amazon Resource Name (ARN) of the workflow you want to delete.</p>
            workflow_version: <p>Optional. The specific version of the workflow to delete. If not specified, all versions of the workflow are deleted.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. You can only access or modify a resource that already exists.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.delete_workflow_response.DeleteWorkflowResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.delete_workflow

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.delete_workflow.async_delete_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkflow")
        )
        input_: capo_mwaa_serverless.types.delete_workflow_request.DeleteWorkflowRequest = {
            "workflow_arn": workflow_arn
        }
        if workflow_version is not None:
            input_["workflow_version"] = workflow_version

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
        config_overrides: Optional[AsyncMWAAServerlessClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mwaa_serverless.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Lists all workflows in your account, with optional pagination support. This operation returns summary information for workflows, showing only the most recently created version of each workflow. Amazon Managed Workflows for Apache Airflow Serverless maintains workflow metadata in a highly available, distributed storage system that enables efficient querying and filtering. The service implements proper access controls to ensure you can only view workflows that you have permissions to access, supporting both individual and team-based workflow management scenarios.</p>

        Args:
            max_results: <p>The maximum number of workflows you want to return in a single response.</p>
            next_token: <p>The pagination token you need to use to retrieve the next set of results. This value is returned from a previous call to <code>ListWorkflows</code>.</p>

        Raises:
            capo_mwaa_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permission to perform this action.</p>
            capo_mwaa_serverless.errors.internal_server_exception.InternalServerException: <p>An unexpected server-side error occurred during request processing.</p>
            capo_mwaa_serverless.errors.operation_timeout_exception.OperationTimeoutException: <p>The operation timed out.</p>
            capo_mwaa_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied because too many requests were made in a short period, exceeding the service rate limits. Amazon Managed Workflows for Apache Airflow Serverless implements throttling controls to ensure fair resource allocation across all customers in the multi-tenant environment. This helps maintain service stability and performance. If you encounter throttling, implement exponential backoff and retry logic in your applications, or consider distributing your API calls over a longer time period.</p>
            capo_mwaa_serverless.errors.validation_exception.ValidationException: <p>The specified request parameters are invalid, missing, or inconsistent with Amazon Managed Workflows for Apache Airflow Serverless service requirements. This can occur when workflow definitions contain unsupported operators, when required IAM permissions are missing, when S3 locations are inaccessible, or when network configurations are invalid. The service validates workflow definitions, execution roles, and resource configurations to ensure compatibility with the managed Airflow environment and security requirements.</p>
            capo_mwaa_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mwaa_serverless.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mwaa_serverless.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflows

            (
                output,
                http_response,
            ) = await capo_mwaa_serverless._operations.amazon_mwaa_serverless.list_workflows.async_list_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkflows")
        )
        input_: capo_mwaa_serverless.types.list_workflows_request.ListWorkflowsRequest = {}
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
