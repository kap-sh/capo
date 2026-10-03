from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_omics._auth._signers
import capo_omics._auth._sigv4
from capo_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_omics.types.accelerators
    import capo_omics.types.container_registry_map
    import capo_omics.types.create_workflow_request
    import capo_omics.types.create_workflow_response
    import capo_omics.types.definition_repository
    import capo_omics.types.delete_workflow_request
    import capo_omics.types.get_workflow_request
    import capo_omics.types.get_workflow_response
    import capo_omics.types.list_workflows_request
    import capo_omics.types.list_workflows_response
    import capo_omics.types.parameter_template_path
    import capo_omics.types.readme_markdown
    import capo_omics.types.readme_path
    import capo_omics.types.s3_uri_for_object
    import capo_omics.types.storage_type
    import capo_omics.types.tag_map
    import capo_omics.types.update_workflow_request
    import capo_omics.types.uri
    import capo_omics.types.workflow_bucket_owner_id
    import capo_omics.types.workflow_definition
    import capo_omics.types.workflow_description
    import capo_omics.types.workflow_engine
    import capo_omics.types.workflow_export_list
    import capo_omics.types.workflow_id
    import capo_omics.types.workflow_list_item
    import capo_omics.types.workflow_list_token
    import capo_omics.types.workflow_main
    import capo_omics.types.workflow_name
    import capo_omics.types.workflow_owner_id
    import capo_omics.types.workflow_parameter_template
    import capo_omics.types.workflow_request_id
    import capo_omics.types.workflow_type
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class WorkflowResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        request_id: "capo_omics.types.workflow_request_id.WorkflowRequestId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        name: Optional["capo_omics.types.workflow_name.WorkflowName"] = None,
        description: Optional[
            "capo_omics.types.workflow_description.WorkflowDescription"
        ] = None,
        engine: Optional["capo_omics.types.workflow_engine.WorkflowEngine"] = None,
        definition_zip: Optional[bytes] = None,
        definition_uri: Optional[
            "capo_omics.types.workflow_definition.WorkflowDefinition"
        ] = None,
        main: Optional["capo_omics.types.workflow_main.WorkflowMain"] = None,
        parameter_template: Optional[
            "capo_omics.types.workflow_parameter_template.WorkflowParameterTemplate"
        ] = None,
        storage_capacity: Optional[int] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        accelerators: Optional["capo_omics.types.accelerators.Accelerators"] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        container_registry_map: Optional[
            "capo_omics.types.container_registry_map.ContainerRegistryMap"
        ] = None,
        container_registry_map_uri: Optional["capo_omics.types.uri.Uri"] = None,
        readme_markdown: Optional[
            "capo_omics.types.readme_markdown.ReadmeMarkdown"
        ] = None,
        parameter_template_path: Optional[
            "capo_omics.types.parameter_template_path.ParameterTemplatePath"
        ] = None,
        readme_path: Optional["capo_omics.types.readme_path.ReadmePath"] = None,
        definition_repository: Optional[
            "capo_omics.types.definition_repository.DefinitionRepository"
        ] = None,
        workflow_bucket_owner_id: Optional[
            "capo_omics.types.workflow_bucket_owner_id.WorkflowBucketOwnerId"
        ] = None,
        readme_uri: Optional[
            "capo_omics.types.s3_uri_for_object.S3UriForObject"
        ] = None,
    ) -> "capo_omics.types.create_workflow_response.CreateWorkflowResponse":
        """<p>Creates a private workflow. Before you create a private workflow, you must create and configure these required resources:</p> <ul> <li> <p> <i>Workflow definition file:</i> A workflow definition file written in WDL, Nextflow, or CWL. The workflow definition specifies the inputs and outputs for runs that use the workflow. It also includes specifications for the runs and run tasks for your workflow, including compute and memory requirements. The workflow definition file must be in <code>.zip</code> format. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-definition-files.html">Workflow definition files</a> in Amazon Web Services HealthOmics.</p> <ul> <li> <p>You can use Amazon Q CLI to build and validate your workflow definition files in WDL, Nextflow, and CWL. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/getting-started.html#omics-q-prompts">Example prompts for Amazon Q CLI</a> and the <a href="https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai">Amazon Web Services HealthOmics Agentic generative AI tutorial</a> on GitHub.</p> </li> </ul> </li> <li> <p> <i>(Optional) Parameter template file:</i> A parameter template file written in JSON. Create the file to define the run parameters, or Amazon Web Services HealthOmics generates the parameter template for you. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html">Parameter template files for HealthOmics workflows</a>. </p> </li> <li> <p> <i>ECR container images:</i> Create container images for the workflow in a private ECR repository, or synchronize images from a supported upstream registry with your Amazon ECR private repository.</p> </li> <li> <p> <i>(Optional) Sentieon licenses:</i> Request a Sentieon license to use the Sentieon software in private workflows.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/creating-private-workflows.html">Creating or updating a private workflow in Amazon Web Services HealthOmics</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>Name (optional but highly recommended) for the workflow to locate relevant information in the CloudWatch logs and Amazon Web Services HealthOmics console. </p>
            description: <p>A description for the workflow.</p>
            engine: <p>The workflow engine for the workflow. By default, Amazon Web Services HealthOmics detects the engine automatically from your workflow definition. Provide a value if you have workflow definition files from more than one engine in your zip file, or to use WDL lenient.</p> <p>WDL lenient is designed to handle workflows migrated from Cromwell. It supports customer Cromwell directives and some non-conformant logic. For details, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-wdl-type-conversion.html">Implicit type conversion in WDL lenient</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            definition_zip: <p>A ZIP archive containing the main workflow definition file and dependencies that it imports for the workflow. You can use a file with a ://fileb prefix instead of the Base64 string. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-defn-requirements.html">Workflow definition requirements</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            definition_uri: <p>The S3 URI of a definition for the workflow. The S3 bucket must be in the same region as the workflow.</p>
            main: <p>The path of the main definition file for the workflow. This parameter is not required if the ZIP archive contains only one workflow definition file, or if the main definition file is named “main”. An example path is: <code>workflow-definition/main-file.wdl</code>. </p>
            parameter_template: <p>A parameter template for the workflow. If this field is blank, Amazon Web Services HealthOmics will automatically parse the parameter template values from your workflow definition file. To override these service generated default values, provide a parameter template. To view an example of a parameter template, see <a href="https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html">Parameter template files</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            storage_capacity: <p>The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. The <code>storageCapacity</code> can be overwritten at run time. The storage capacity is not required for runs with a <code>DYNAMIC</code> storage type.</p>
            tags: <p>Tags for the workflow. You can define up to 50 tags for the workflow. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            request_id: <p>An idempotency token to ensure that duplicate workflows are not created when Amazon Web Services HealthOmics submits retry requests.</p>
            accelerators: <p>The computational accelerator specified to run the workflow.</p>
            storage_type: <p>The default storage type for runs that use this workflow. The <code>storageType</code> can be overridden at run time. <code>DYNAMIC</code> storage dynamically scales the storage up or down, based on file system utilization. <code>STATIC</code> storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            container_registry_map: <p>(Optional) Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html">Container images</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            container_registry_map_uri: <p>(Optional) URI of the S3 location for the registry mapping file.</p>
            readme_markdown: <p>The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.</p>
            parameter_template_path: <p>The path to the workflow parameter template JSON file within the repository. This file defines the input parameters for runs that use this workflow. If not specified, the workflow will be created without a parameter template.</p>
            readme_path: <p>The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the <code>README.md</code> file from the root directory of the repository will be used.</p>
            definition_repository: <p>The repository information for the workflow definition. This allows you to source your workflow definition directly from a code repository.</p>
            workflow_bucket_owner_id: <p>The Amazon Web Services account ID of the expected owner of the S3 bucket that contains the workflow definition. If not specified, the service skips the validation.</p>
            readme_uri: <p>The S3 URI of the README file for the workflow. This file provides documentation and usage information for the workflow. Requirements include:</p> <ul> <li> <p>The S3 URI must begin with <code>s3://USER-OWNED-BUCKET/</code> </p> </li> <li> <p>The requester must have access to the S3 bucket and object.</p> </li> <li> <p>The max README content length is 500 KiB.</p> </li> </ul>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> OperationResponse[
            "capo_omics.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import capo_omics._operations.omics.create_workflow

            output, http_response = (
                capo_omics._operations.omics.create_workflow.create_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_workflow_request.CreateWorkflowRequest = {
            "request_id": request_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if engine is not None:
            input_["engine"] = engine
        if definition_zip is not None:
            input_["definition_zip"] = definition_zip
        if definition_uri is not None:
            input_["definition_uri"] = definition_uri
        if main is not None:
            input_["main"] = main
        if parameter_template is not None:
            input_["parameter_template"] = parameter_template
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if tags is not None:
            input_["tags"] = tags
        if accelerators is not None:
            input_["accelerators"] = accelerators
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if container_registry_map is not None:
            input_["container_registry_map"] = container_registry_map
        if container_registry_map_uri is not None:
            input_["container_registry_map_uri"] = container_registry_map_uri
        if readme_markdown is not None:
            input_["readme_markdown"] = readme_markdown
        if parameter_template_path is not None:
            input_["parameter_template_path"] = parameter_template_path
        if readme_path is not None:
            input_["readme_path"] = readme_path
        if definition_repository is not None:
            input_["definition_repository"] = definition_repository
        if workflow_bucket_owner_id is not None:
            input_["workflow_bucket_owner_id"] = workflow_bucket_owner_id
        if readme_uri is not None:
            input_["readme_uri"] = readme_uri

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        export: Optional[
            "capo_omics.types.workflow_export_list.WorkflowExportList"
        ] = None,
        workflow_owner_id: Optional[
            "capo_omics.types.workflow_owner_id.WorkflowOwnerId"
        ] = None,
    ) -> "capo_omics.types.get_workflow_response.GetWorkflowResponse":
        """<p>Gets all information about a workflow using its ID.</p> <p>If a workflow is shared with you, you cannot export the workflow.</p> <p>For more information about your workflow status, see <a href="https://docs.aws.amazon.com/omics/latest/dev/using-get-workflow.html">Verify the workflow status</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The workflow's ID.</p>
            type: <p>The workflow's type.</p>
            export: <p>The export format for the workflow.</p>
            workflow_owner_id: <p>The ID of the workflow owner.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.get_workflow_request.GetWorkflowRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import capo_omics._operations.omics.get_workflow

            output, http_response = (
                capo_omics._operations.omics.get_workflow.get_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_workflow_request.GetWorkflowRequest = {"id": id}
        if type is not None:
            input_["type"] = type
        if export is not None:
            input_["export"] = export
        if workflow_owner_id is not None:
            input_["workflow_owner_id"] = workflow_owner_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        name: Optional["capo_omics.types.workflow_name.WorkflowName"] = None,
        description: Optional[
            "capo_omics.types.workflow_description.WorkflowDescription"
        ] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        storage_capacity: Optional[int] = None,
        readme_markdown: Optional[
            "capo_omics.types.readme_markdown.ReadmeMarkdown"
        ] = None,
    ) -> None:
        """<p>Updates information about a workflow.</p> <p>You can update the following workflow information:</p> <ul> <li> <p>Name</p> </li> <li> <p>Description</p> </li> <li> <p>Default storage type</p> </li> <li> <p>Default storage capacity (with workflow ID)</p> </li> </ul> <p>This operation returns a response with no body if the operation is successful. You can check the workflow updates by calling the <code>GetWorkflow</code> API operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/update-private-workflow.html">Update a private workflow</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The workflow's ID.</p>
            name: <p>A name for the workflow.</p>
            description: <p>A description for the workflow.</p>
            storage_type: <p>The default storage type for runs that use this workflow. STATIC storage allocates a fixed amount of storage. DYNAMIC storage dynamically scales the storage up or down, based on file system utilization. For more information about static and dynamic storage, see <a href="https://docs.aws.amazon.com/omics/latest/dev/Using-workflows.html">Running workflows</a> in the <i>Amazon Web Services HealthOmics User Guide</i>. </p>
            storage_capacity: <p>The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. </p>
            readme_markdown: <p>The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.update_workflow_request.UpdateWorkflowRequest]",
        ) -> OperationResponse[None]:
            import capo_omics._operations.omics.update_workflow

            output, http_response = (
                capo_omics._operations.omics.update_workflow.update_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.update_workflow_request.UpdateWorkflowRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if readme_markdown is not None:
            input_["readme_markdown"] = readme_markdown

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a workflow by specifying its ID. This operation returns a response with no body if the deletion is successful.</p> <p>To verify that the workflow is deleted:</p> <ul> <li> <p>Use <code>ListWorkflows</code> to confirm the workflow no longer appears in the list.</p> </li> <li> <p>Use <code>GetWorkflow</code> to verify the workflow cannot be found.</p> </li> </ul>

        Args:
            id: <p>The workflow's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> OperationResponse[None]:
            import capo_omics._operations.omics.delete_workflow

            output, http_response = (
                capo_omics._operations.omics.delete_workflow.delete_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_workflow_request.DeleteWorkflowRequest = {
            "id": id
        }

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
        config_overrides: Optional[OmicsClientConfig] = None,
        type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        name: Optional["capo_omics.types.workflow_name.WorkflowName"] = None,
        starting_token: Optional[
            "capo_omics.types.workflow_list_token.WorkflowListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_omics.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Retrieves a list of existing workflows. You can filter for specific workflows by their name and type. Using the type parameter, specify <code>PRIVATE</code> to retrieve a list of private workflows or specify <code>READY2RUN</code> for a list of all Ready2Run workflows. If you do not specify the type of workflow, this operation returns a list of existing workflows.</p>

        Args:
            type: <p>Filter the list by workflow type.</p>
            name: <p>Filter the list by workflow name.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of workflows to return in one page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import capo_omics._operations.omics.list_workflows

            output, http_response = (
                capo_omics._operations.omics.list_workflows.list_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_workflows_request.ListWorkflowsRequest = {}
        if type is not None:
            input_["type"] = type
        if name is not None:
            input_["name"] = name
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncWorkflowResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        request_id: "capo_omics.types.workflow_request_id.WorkflowRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.workflow_name.WorkflowName"] = None,
        description: Optional[
            "capo_omics.types.workflow_description.WorkflowDescription"
        ] = None,
        engine: Optional["capo_omics.types.workflow_engine.WorkflowEngine"] = None,
        definition_zip: Optional[bytes] = None,
        definition_uri: Optional[
            "capo_omics.types.workflow_definition.WorkflowDefinition"
        ] = None,
        main: Optional["capo_omics.types.workflow_main.WorkflowMain"] = None,
        parameter_template: Optional[
            "capo_omics.types.workflow_parameter_template.WorkflowParameterTemplate"
        ] = None,
        storage_capacity: Optional[int] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        accelerators: Optional["capo_omics.types.accelerators.Accelerators"] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        container_registry_map: Optional[
            "capo_omics.types.container_registry_map.ContainerRegistryMap"
        ] = None,
        container_registry_map_uri: Optional["capo_omics.types.uri.Uri"] = None,
        readme_markdown: Optional[
            "capo_omics.types.readme_markdown.ReadmeMarkdown"
        ] = None,
        parameter_template_path: Optional[
            "capo_omics.types.parameter_template_path.ParameterTemplatePath"
        ] = None,
        readme_path: Optional["capo_omics.types.readme_path.ReadmePath"] = None,
        definition_repository: Optional[
            "capo_omics.types.definition_repository.DefinitionRepository"
        ] = None,
        workflow_bucket_owner_id: Optional[
            "capo_omics.types.workflow_bucket_owner_id.WorkflowBucketOwnerId"
        ] = None,
        readme_uri: Optional[
            "capo_omics.types.s3_uri_for_object.S3UriForObject"
        ] = None,
    ) -> "capo_omics.types.create_workflow_response.CreateWorkflowResponse":
        """<p>Creates a private workflow. Before you create a private workflow, you must create and configure these required resources:</p> <ul> <li> <p> <i>Workflow definition file:</i> A workflow definition file written in WDL, Nextflow, or CWL. The workflow definition specifies the inputs and outputs for runs that use the workflow. It also includes specifications for the runs and run tasks for your workflow, including compute and memory requirements. The workflow definition file must be in <code>.zip</code> format. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-definition-files.html">Workflow definition files</a> in Amazon Web Services HealthOmics.</p> <ul> <li> <p>You can use Amazon Q CLI to build and validate your workflow definition files in WDL, Nextflow, and CWL. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/getting-started.html#omics-q-prompts">Example prompts for Amazon Q CLI</a> and the <a href="https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai">Amazon Web Services HealthOmics Agentic generative AI tutorial</a> on GitHub.</p> </li> </ul> </li> <li> <p> <i>(Optional) Parameter template file:</i> A parameter template file written in JSON. Create the file to define the run parameters, or Amazon Web Services HealthOmics generates the parameter template for you. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html">Parameter template files for HealthOmics workflows</a>. </p> </li> <li> <p> <i>ECR container images:</i> Create container images for the workflow in a private ECR repository, or synchronize images from a supported upstream registry with your Amazon ECR private repository.</p> </li> <li> <p> <i>(Optional) Sentieon licenses:</i> Request a Sentieon license to use the Sentieon software in private workflows.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/creating-private-workflows.html">Creating or updating a private workflow in Amazon Web Services HealthOmics</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>Name (optional but highly recommended) for the workflow to locate relevant information in the CloudWatch logs and Amazon Web Services HealthOmics console. </p>
            description: <p>A description for the workflow.</p>
            engine: <p>The workflow engine for the workflow. By default, Amazon Web Services HealthOmics detects the engine automatically from your workflow definition. Provide a value if you have workflow definition files from more than one engine in your zip file, or to use WDL lenient.</p> <p>WDL lenient is designed to handle workflows migrated from Cromwell. It supports customer Cromwell directives and some non-conformant logic. For details, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-wdl-type-conversion.html">Implicit type conversion in WDL lenient</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            definition_zip: <p>A ZIP archive containing the main workflow definition file and dependencies that it imports for the workflow. You can use a file with a ://fileb prefix instead of the Base64 string. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-defn-requirements.html">Workflow definition requirements</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            definition_uri: <p>The S3 URI of a definition for the workflow. The S3 bucket must be in the same region as the workflow.</p>
            main: <p>The path of the main definition file for the workflow. This parameter is not required if the ZIP archive contains only one workflow definition file, or if the main definition file is named “main”. An example path is: <code>workflow-definition/main-file.wdl</code>. </p>
            parameter_template: <p>A parameter template for the workflow. If this field is blank, Amazon Web Services HealthOmics will automatically parse the parameter template values from your workflow definition file. To override these service generated default values, provide a parameter template. To view an example of a parameter template, see <a href="https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html">Parameter template files</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            storage_capacity: <p>The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. The <code>storageCapacity</code> can be overwritten at run time. The storage capacity is not required for runs with a <code>DYNAMIC</code> storage type.</p>
            tags: <p>Tags for the workflow. You can define up to 50 tags for the workflow. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html">Adding a tag</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            request_id: <p>An idempotency token to ensure that duplicate workflows are not created when Amazon Web Services HealthOmics submits retry requests.</p>
            accelerators: <p>The computational accelerator specified to run the workflow.</p>
            storage_type: <p>The default storage type for runs that use this workflow. The <code>storageType</code> can be overridden at run time. <code>DYNAMIC</code> storage dynamically scales the storage up or down, based on file system utilization. <code>STATIC</code> storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html">Run storage types</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            container_registry_map: <p>(Optional) Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html">Container images</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            container_registry_map_uri: <p>(Optional) URI of the S3 location for the registry mapping file.</p>
            readme_markdown: <p>The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.</p>
            parameter_template_path: <p>The path to the workflow parameter template JSON file within the repository. This file defines the input parameters for runs that use this workflow. If not specified, the workflow will be created without a parameter template.</p>
            readme_path: <p>The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the <code>README.md</code> file from the root directory of the repository will be used.</p>
            definition_repository: <p>The repository information for the workflow definition. This allows you to source your workflow definition directly from a code repository.</p>
            workflow_bucket_owner_id: <p>The Amazon Web Services account ID of the expected owner of the S3 bucket that contains the workflow definition. If not specified, the service skips the validation.</p>
            readme_uri: <p>The S3 URI of the README file for the workflow. This file provides documentation and usage information for the workflow. Requirements include:</p> <ul> <li> <p>The S3 URI must begin with <code>s3://USER-OWNED-BUCKET/</code> </p> </li> <li> <p>The requester must have access to the S3 bucket and object.</p> </li> <li> <p>The max README content length is 500 KiB.</p> </li> </ul>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_workflow_request.CreateWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_workflow_response.CreateWorkflowResponse"
        ]:
            import capo_omics._operations.omics.create_workflow

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_workflow.async_create_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_workflow_request.CreateWorkflowRequest = {
            "request_id": request_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if engine is not None:
            input_["engine"] = engine
        if definition_zip is not None:
            input_["definition_zip"] = definition_zip
        if definition_uri is not None:
            input_["definition_uri"] = definition_uri
        if main is not None:
            input_["main"] = main
        if parameter_template is not None:
            input_["parameter_template"] = parameter_template
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if tags is not None:
            input_["tags"] = tags
        if accelerators is not None:
            input_["accelerators"] = accelerators
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if container_registry_map is not None:
            input_["container_registry_map"] = container_registry_map
        if container_registry_map_uri is not None:
            input_["container_registry_map_uri"] = container_registry_map_uri
        if readme_markdown is not None:
            input_["readme_markdown"] = readme_markdown
        if parameter_template_path is not None:
            input_["parameter_template_path"] = parameter_template_path
        if readme_path is not None:
            input_["readme_path"] = readme_path
        if definition_repository is not None:
            input_["definition_repository"] = definition_repository
        if workflow_bucket_owner_id is not None:
            input_["workflow_bucket_owner_id"] = workflow_bucket_owner_id
        if readme_uri is not None:
            input_["readme_uri"] = readme_uri

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        export: Optional[
            "capo_omics.types.workflow_export_list.WorkflowExportList"
        ] = None,
        workflow_owner_id: Optional[
            "capo_omics.types.workflow_owner_id.WorkflowOwnerId"
        ] = None,
    ) -> "capo_omics.types.get_workflow_response.GetWorkflowResponse":
        """<p>Gets all information about a workflow using its ID.</p> <p>If a workflow is shared with you, you cannot export the workflow.</p> <p>For more information about your workflow status, see <a href="https://docs.aws.amazon.com/omics/latest/dev/using-get-workflow.html">Verify the workflow status</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The workflow's ID.</p>
            type: <p>The workflow's type.</p>
            export: <p>The export format for the workflow.</p>
            workflow_owner_id: <p>The ID of the workflow owner.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_workflow_request.GetWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import capo_omics._operations.omics.get_workflow

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_workflow.async_get_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_workflow_request.GetWorkflowRequest = {"id": id}
        if type is not None:
            input_["type"] = type
        if export is not None:
            input_["export"] = export
        if workflow_owner_id is not None:
            input_["workflow_owner_id"] = workflow_owner_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.workflow_name.WorkflowName"] = None,
        description: Optional[
            "capo_omics.types.workflow_description.WorkflowDescription"
        ] = None,
        storage_type: Optional["capo_omics.types.storage_type.StorageType"] = None,
        storage_capacity: Optional[int] = None,
        readme_markdown: Optional[
            "capo_omics.types.readme_markdown.ReadmeMarkdown"
        ] = None,
    ) -> None:
        """<p>Updates information about a workflow.</p> <p>You can update the following workflow information:</p> <ul> <li> <p>Name</p> </li> <li> <p>Description</p> </li> <li> <p>Default storage type</p> </li> <li> <p>Default storage capacity (with workflow ID)</p> </li> </ul> <p>This operation returns a response with no body if the operation is successful. You can check the workflow updates by calling the <code>GetWorkflow</code> API operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/update-private-workflow.html">Update a private workflow</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The workflow's ID.</p>
            name: <p>A name for the workflow.</p>
            description: <p>A description for the workflow.</p>
            storage_type: <p>The default storage type for runs that use this workflow. STATIC storage allocates a fixed amount of storage. DYNAMIC storage dynamically scales the storage up or down, based on file system utilization. For more information about static and dynamic storage, see <a href="https://docs.aws.amazon.com/omics/latest/dev/Using-workflows.html">Running workflows</a> in the <i>Amazon Web Services HealthOmics User Guide</i>. </p>
            storage_capacity: <p>The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. </p>
            readme_markdown: <p>The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_workflow_request.UpdateWorkflowRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.update_workflow

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_workflow.async_update_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.update_workflow_request.UpdateWorkflowRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if storage_type is not None:
            input_["storage_type"] = storage_type
        if storage_capacity is not None:
            input_["storage_capacity"] = storage_capacity
        if readme_markdown is not None:
            input_["readme_markdown"] = readme_markdown

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_omics.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a workflow by specifying its ID. This operation returns a response with no body if the deletion is successful.</p> <p>To verify that the workflow is deleted:</p> <ul> <li> <p>Use <code>ListWorkflows</code> to confirm the workflow no longer appears in the list.</p> </li> <li> <p>Use <code>GetWorkflow</code> to verify the workflow cannot be found.</p> </li> </ul>

        Args:
            id: <p>The workflow's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_workflow_request.DeleteWorkflowRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_workflow

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_workflow.async_delete_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_workflow_request.DeleteWorkflowRequest = {
            "id": id
        }

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
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        type: Optional["capo_omics.types.workflow_type.WorkflowType"] = None,
        name: Optional["capo_omics.types.workflow_name.WorkflowName"] = None,
        starting_token: Optional[
            "capo_omics.types.workflow_list_token.WorkflowListToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_omics.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Retrieves a list of existing workflows. You can filter for specific workflows by their name and type. Using the type parameter, specify <code>PRIVATE</code> to retrieve a list of private workflows or specify <code>READY2RUN</code> for a list of all Ready2Run workflows. If you do not specify the type of workflow, this operation returns a list of existing workflows.</p>

        Args:
            type: <p>Filter the list by workflow type.</p>
            name: <p>Filter the list by workflow name.</p>
            starting_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of workflows to return in one page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import capo_omics._operations.omics.list_workflows

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_workflows.async_list_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_workflows_request.ListWorkflowsRequest = {}
        if type is not None:
            input_["type"] = type
        if name is not None:
            input_["name"] = name
        if starting_token is not None:
            input_["starting_token"] = starting_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
