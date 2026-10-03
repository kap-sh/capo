from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_proton._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_proton.types.arn
    import capo_proton.types.create_environment_input
    import capo_proton.types.create_environment_output
    import capo_proton.types.delete_environment_input
    import capo_proton.types.delete_environment_output
    import capo_proton.types.deployment_update_type
    import capo_proton.types.description
    import capo_proton.types.environment_account_connection_id
    import capo_proton.types.environment_summary
    import capo_proton.types.environment_template_filter_list
    import capo_proton.types.get_environment_input
    import capo_proton.types.get_environment_output
    import capo_proton.types.list_environments_input
    import capo_proton.types.list_environments_output
    import capo_proton.types.max_page_results
    import capo_proton.types.next_token
    import capo_proton.types.repository_branch_input
    import capo_proton.types.resource_name
    import capo_proton.types.role_arn
    import capo_proton.types.spec_contents
    import capo_proton.types.tag_list
    import capo_proton.types.template_version_part
    import capo_proton.types.update_environment_input
    import capo_proton.types.update_environment_output
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class EnvironmentResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        spec: "capo_proton.types.spec_contents.SpecContents",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        proton_service_role_arn: Optional["capo_proton.types.arn.Arn"] = None,
        environment_account_connection_id: Optional[
            "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        provisioning_repository: Optional[
            "capo_proton.types.repository_branch_input.RepositoryBranchInput"
        ] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.create_environment_output.CreateEnvironmentOutput":
        """<p>Deploy a new environment. An Proton environment is created from an environment template that defines infrastructure and resources that can be shared across services.</p> <p class="title"> <b>You can provision environments using the following methods:</b> </p> <ul> <li> <p>Amazon Web Services-managed provisioning: Proton makes direct calls to provision your resources.</p> </li> <li> <p>Self-managed provisioning: Proton makes pull requests on your repository to provide compiled infrastructure as code (IaC) files that your IaC engine uses to provision resources.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html">Environments</a> and <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html">Provisioning methods</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the environment.</p>
            template_name: <p>The name of the environment template. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html">Environment Templates</a> in the <i>Proton User Guide</i>.</p>
            template_major_version: <p>The major version of the environment template.</p>
            template_minor_version: <p>The minor version of the environment template.</p>
            description: <p>A description of the environment that's being created and deployed.</p>
            spec: <p>A YAML formatted string that provides inputs as defined in the environment template bundle schema file. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html">Environments</a> in the <i>Proton User Guide</i>.</p>
            proton_service_role_arn: <p>The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make calls to other services on your behalf.</p> <p>To use Amazon Web Services-managed provisioning for the environment, specify either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and omit the <code>provisioningRepository</code> parameter.</p>
            environment_account_connection_id: <p>The ID of the environment account connection that you provide if you're provisioning your environment infrastructure resources to an environment account. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p> <p>To use Amazon Web Services-managed provisioning for the environment, specify either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and omit the <code>provisioningRepository</code> parameter.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            provisioning_repository: <p>The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>To use self-managed provisioning for the environment, specify this parameter and omit the <code>environmentAccountConnectionId</code> and <code>protonServiceRoleArn</code> parameters.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.</p> <p>You must specify <code>componentRoleArn</code> to allow directly defined components to be associated with this environment.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.</p> <p>To use CodeBuild-based provisioning for the environment or for any service instance running in the environment, specify either the <code>environmentAccountConnectionId</code> or <code>codebuildRoleArn</code> parameter.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.create_environment_input.CreateEnvironmentInput]",
        ) -> OperationResponse[
            "capo_proton.types.create_environment_output.CreateEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_environment

            output, http_response = (
                capo_proton._operations.aws_proton20200720.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_environment_input.CreateEnvironmentInput = {
            "name": name,
            "template_name": template_name,
            "template_major_version": template_major_version,
            "spec": spec,
        }
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
        if description is not None:
            input_["description"] = description
        if proton_service_role_arn is not None:
            input_["proton_service_role_arn"] = proton_service_role_arn
        if environment_account_connection_id is not None:
            input_["environment_account_connection_id"] = (
                environment_account_connection_id
            )
        if tags is not None:
            input_["tags"] = tags
        if provisioning_repository is not None:
            input_["provisioning_repository"] = provisioning_repository
        if component_role_arn is not None:
            input_["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input_["codebuild_role_arn"] = codebuild_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.get_environment_output.GetEnvironmentOutput":
        """<p>Get detailed data for an environment.</p>

        Args:
            name: <p>The name of the environment that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_environment_input.GetEnvironmentInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_environment_output.GetEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_environment

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_environment_input.GetEnvironmentInput = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        deployment_type: "capo_proton.types.deployment_update_type.DeploymentUpdateType",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        spec: Optional["capo_proton.types.spec_contents.SpecContents"] = None,
        template_major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        proton_service_role_arn: Optional["capo_proton.types.arn.Arn"] = None,
        environment_account_connection_id: Optional[
            "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
        ] = None,
        provisioning_repository: Optional[
            "capo_proton.types.repository_branch_input.RepositoryBranchInput"
        ] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.update_environment_output.UpdateEnvironmentOutput":
        """<p>Update an environment.</p> <p>If the environment is associated with an environment account connection, <i>don't</i> update or include the <code>protonServiceRoleArn</code> and <code>provisioningRepository</code> parameter to update or connect to an environment account connection.</p> <p>You can only update to a new environment account connection if that connection was created in the same environment account that the current environment account connection was created in. The account connection must also be associated with the current environment.</p> <p>If the environment <i>isn't</i> associated with an environment account connection, <i>don't</i> update or include the <code>environmentAccountConnectionId</code> parameter. You <i>can't</i> update or connect the environment to an environment account connection if it <i>isn't</i> already associated with an environment connection.</p> <p>You can update either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and value. You can’t update both.</p> <p>If the environment was configured for Amazon Web Services-managed provisioning, omit the <code>provisioningRepository</code> parameter.</p> <p>If the environment was configured for self-managed provisioning, specify the <code>provisioningRepository</code> parameter and omit the <code>protonServiceRoleArn</code> and <code>environmentAccountConnectionId</code> parameters.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html">Environments</a> and <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html">Provisioning methods</a> in the <i>Proton User Guide</i>.</p> <p>There are four modes for updating an environment. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include minor or major version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>

        Args:
            name: <p>The name of the environment to update.</p>
            description: <p>A description of the environment update.</p>
            spec: <p>The formatted specification that defines the update.</p>
            template_major_version: <p>The major version of the environment to update.</p>
            template_minor_version: <p>The minor version of the environment to update.</p>
            proton_service_role_arn: <p>The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make API calls to other services your behalf.</p>
            deployment_type: <p>There are four modes for updating an environment. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that is higher than the major version in use and a minor version (optional).</p> </dd> </dl>
            environment_account_connection_id: <p>The ID of the environment account connection.</p> <p>You can only update to a new environment account connection if it was created in the same environment account that the current environment account connection was created in and is associated with the current environment.</p>
            provisioning_repository: <p>The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.</p> <p>The environment must have a <code>componentRoleArn</code> to allow directly defined components to be associated with the environment.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.update_environment_input.UpdateEnvironmentInput]",
        ) -> OperationResponse[
            "capo_proton.types.update_environment_output.UpdateEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_environment

            output, http_response = (
                capo_proton._operations.aws_proton20200720.update_environment.update_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_environment_input.UpdateEnvironmentInput = {
            "name": name,
            "deployment_type": deployment_type,
        }
        if description is not None:
            input_["description"] = description
        if spec is not None:
            input_["spec"] = spec
        if template_major_version is not None:
            input_["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
        if proton_service_role_arn is not None:
            input_["proton_service_role_arn"] = proton_service_role_arn
        if environment_account_connection_id is not None:
            input_["environment_account_connection_id"] = (
                environment_account_connection_id
            )
        if provisioning_repository is not None:
            input_["provisioning_repository"] = provisioning_repository
        if component_role_arn is not None:
            input_["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input_["codebuild_role_arn"] = codebuild_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_environment_output.DeleteEnvironmentOutput":
        """<p>Delete an environment.</p>

        Args:
            name: <p>The name of the environment to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.delete_environment_input.DeleteEnvironmentInput]",
        ) -> OperationResponse[
            "capo_proton.types.delete_environment_output.DeleteEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_environment

            output, http_response = (
                capo_proton._operations.aws_proton20200720.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_environment_input.DeleteEnvironmentInput = {
            "name": name
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
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        environment_templates: Optional[
            "capo_proton.types.environment_template_filter_list.EnvironmentTemplateFilterList"
        ] = None,
    ) -> "capo_proton.types.list_environments_output.ListEnvironmentsOutput":
        """<p>List environments with detail data summaries.</p>

        Args:
            next_token: <p>A token that indicates the location of the next environment in the array of environments, after the list of environments that was previously requested.</p>
            max_results: <p>The maximum number of environments to list.</p>
            environment_templates: <p>An array of the versions of the environment template.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_environments_input.ListEnvironmentsInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_environments_output.ListEnvironmentsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environments

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_environments_input.ListEnvironmentsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if environment_templates is not None:
            input_["environment_templates"] = environment_templates

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEnvironmentResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        spec: "capo_proton.types.spec_contents.SpecContents",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        proton_service_role_arn: Optional["capo_proton.types.arn.Arn"] = None,
        environment_account_connection_id: Optional[
            "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        provisioning_repository: Optional[
            "capo_proton.types.repository_branch_input.RepositoryBranchInput"
        ] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.create_environment_output.CreateEnvironmentOutput":
        """<p>Deploy a new environment. An Proton environment is created from an environment template that defines infrastructure and resources that can be shared across services.</p> <p class="title"> <b>You can provision environments using the following methods:</b> </p> <ul> <li> <p>Amazon Web Services-managed provisioning: Proton makes direct calls to provision your resources.</p> </li> <li> <p>Self-managed provisioning: Proton makes pull requests on your repository to provide compiled infrastructure as code (IaC) files that your IaC engine uses to provision resources.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html">Environments</a> and <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html">Provisioning methods</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the environment.</p>
            template_name: <p>The name of the environment template. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html">Environment Templates</a> in the <i>Proton User Guide</i>.</p>
            template_major_version: <p>The major version of the environment template.</p>
            template_minor_version: <p>The minor version of the environment template.</p>
            description: <p>A description of the environment that's being created and deployed.</p>
            spec: <p>A YAML formatted string that provides inputs as defined in the environment template bundle schema file. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html">Environments</a> in the <i>Proton User Guide</i>.</p>
            proton_service_role_arn: <p>The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make calls to other services on your behalf.</p> <p>To use Amazon Web Services-managed provisioning for the environment, specify either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and omit the <code>provisioningRepository</code> parameter.</p>
            environment_account_connection_id: <p>The ID of the environment account connection that you provide if you're provisioning your environment infrastructure resources to an environment account. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p> <p>To use Amazon Web Services-managed provisioning for the environment, specify either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and omit the <code>provisioningRepository</code> parameter.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            provisioning_repository: <p>The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>To use self-managed provisioning for the environment, specify this parameter and omit the <code>environmentAccountConnectionId</code> and <code>protonServiceRoleArn</code> parameters.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.</p> <p>You must specify <code>componentRoleArn</code> to allow directly defined components to be associated with this environment.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.</p> <p>To use CodeBuild-based provisioning for the environment or for any service instance running in the environment, specify either the <code>environmentAccountConnectionId</code> or <code>codebuildRoleArn</code> parameter.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_environment_input.CreateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_environment_output.CreateEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_environment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_environment.async_create_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_environment_input.CreateEnvironmentInput = {
            "name": name,
            "template_name": template_name,
            "template_major_version": template_major_version,
            "spec": spec,
        }
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
        if description is not None:
            input_["description"] = description
        if proton_service_role_arn is not None:
            input_["proton_service_role_arn"] = proton_service_role_arn
        if environment_account_connection_id is not None:
            input_["environment_account_connection_id"] = (
                environment_account_connection_id
            )
        if tags is not None:
            input_["tags"] = tags
        if provisioning_repository is not None:
            input_["provisioning_repository"] = provisioning_repository
        if component_role_arn is not None:
            input_["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input_["codebuild_role_arn"] = codebuild_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_environment_output.GetEnvironmentOutput":
        """<p>Get detailed data for an environment.</p>

        Args:
            name: <p>The name of the environment that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_environment_input.GetEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_environment_output.GetEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_environment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_environment_input.GetEnvironmentInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        deployment_type: "capo_proton.types.deployment_update_type.DeploymentUpdateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        spec: Optional["capo_proton.types.spec_contents.SpecContents"] = None,
        template_major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        proton_service_role_arn: Optional["capo_proton.types.arn.Arn"] = None,
        environment_account_connection_id: Optional[
            "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId"
        ] = None,
        provisioning_repository: Optional[
            "capo_proton.types.repository_branch_input.RepositoryBranchInput"
        ] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.update_environment_output.UpdateEnvironmentOutput":
        """<p>Update an environment.</p> <p>If the environment is associated with an environment account connection, <i>don't</i> update or include the <code>protonServiceRoleArn</code> and <code>provisioningRepository</code> parameter to update or connect to an environment account connection.</p> <p>You can only update to a new environment account connection if that connection was created in the same environment account that the current environment account connection was created in. The account connection must also be associated with the current environment.</p> <p>If the environment <i>isn't</i> associated with an environment account connection, <i>don't</i> update or include the <code>environmentAccountConnectionId</code> parameter. You <i>can't</i> update or connect the environment to an environment account connection if it <i>isn't</i> already associated with an environment connection.</p> <p>You can update either the <code>environmentAccountConnectionId</code> or <code>protonServiceRoleArn</code> parameter and value. You can’t update both.</p> <p>If the environment was configured for Amazon Web Services-managed provisioning, omit the <code>provisioningRepository</code> parameter.</p> <p>If the environment was configured for self-managed provisioning, specify the <code>provisioningRepository</code> parameter and omit the <code>protonServiceRoleArn</code> and <code>environmentAccountConnectionId</code> parameters.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html">Environments</a> and <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html">Provisioning methods</a> in the <i>Proton User Guide</i>.</p> <p>There are four modes for updating an environment. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include minor or major version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>

        Args:
            name: <p>The name of the environment to update.</p>
            description: <p>A description of the environment update.</p>
            spec: <p>The formatted specification that defines the update.</p>
            template_major_version: <p>The major version of the environment to update.</p>
            template_minor_version: <p>The minor version of the environment to update.</p>
            proton_service_role_arn: <p>The Amazon Resource Name (ARN) of the Proton service role that allows Proton to make API calls to other services your behalf.</p>
            deployment_type: <p>There are four modes for updating an environment. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that is higher than the major version in use and a minor version (optional).</p> </dd> </dl>
            environment_account_connection_id: <p>The ID of the environment account connection.</p> <p>You can only update to a new environment account connection if it was created in the same environment account that the current environment account connection was created in and is associated with the current environment.</p>
            provisioning_repository: <p>The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.</p> <p>The environment must have a <code>componentRoleArn</code> to allow directly defined components to be associated with the environment.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that allows Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_environment_input.UpdateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_environment_output.UpdateEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_environment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_environment.async_update_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_environment_input.UpdateEnvironmentInput = {
            "name": name,
            "deployment_type": deployment_type,
        }
        if description is not None:
            input_["description"] = description
        if spec is not None:
            input_["spec"] = spec
        if template_major_version is not None:
            input_["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version
        if proton_service_role_arn is not None:
            input_["proton_service_role_arn"] = proton_service_role_arn
        if environment_account_connection_id is not None:
            input_["environment_account_connection_id"] = (
                environment_account_connection_id
            )
        if provisioning_repository is not None:
            input_["provisioning_repository"] = provisioning_repository
        if component_role_arn is not None:
            input_["component_role_arn"] = component_role_arn
        if codebuild_role_arn is not None:
            input_["codebuild_role_arn"] = codebuild_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_environment_output.DeleteEnvironmentOutput":
        """<p>Delete an environment.</p>

        Args:
            name: <p>The name of the environment to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_environment_input.DeleteEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_environment_output.DeleteEnvironmentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_environment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_environment.async_delete_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_environment_input.DeleteEnvironmentInput = {
            "name": name
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
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        environment_templates: Optional[
            "capo_proton.types.environment_template_filter_list.EnvironmentTemplateFilterList"
        ] = None,
    ) -> "capo_proton.types.list_environments_output.ListEnvironmentsOutput":
        """<p>List environments with detail data summaries.</p>

        Args:
            next_token: <p>A token that indicates the location of the next environment in the array of environments, after the list of environments that was previously requested.</p>
            max_results: <p>The maximum number of environments to list.</p>
            environment_templates: <p>An array of the versions of the environment template.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_environments_input.ListEnvironmentsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_environments_output.ListEnvironmentsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environments

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_environments_input.ListEnvironmentsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if environment_templates is not None:
            input_["environment_templates"] = environment_templates

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
