from __future__ import annotations

import uuid
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
    import capo_proton.types.accept_environment_account_connection_input
    import capo_proton.types.accept_environment_account_connection_output
    import capo_proton.types.aws_account_id
    import capo_proton.types.client_token
    import capo_proton.types.create_environment_account_connection_input
    import capo_proton.types.create_environment_account_connection_output
    import capo_proton.types.delete_environment_account_connection_input
    import capo_proton.types.delete_environment_account_connection_output
    import capo_proton.types.environment_account_connection_id
    import capo_proton.types.environment_account_connection_requester_account_type
    import capo_proton.types.environment_account_connection_status_list
    import capo_proton.types.environment_account_connection_summary
    import capo_proton.types.get_environment_account_connection_input
    import capo_proton.types.get_environment_account_connection_output
    import capo_proton.types.list_environment_account_connections_input
    import capo_proton.types.list_environment_account_connections_output
    import capo_proton.types.max_page_results
    import capo_proton.types.next_token
    import capo_proton.types.reject_environment_account_connection_input
    import capo_proton.types.reject_environment_account_connection_output
    import capo_proton.types.resource_name
    import capo_proton.types.role_arn
    import capo_proton.types.tag_list
    import capo_proton.types.update_environment_account_connection_input
    import capo_proton.types.update_environment_account_connection_output
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class EnvironmentAccountConnectionResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def create(
        self,
        management_account_id: "capo_proton.types.aws_account_id.AwsAccountId",
        environment_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
        role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.create_environment_account_connection_output.CreateEnvironmentAccountConnectionOutput":
        """<p>Create an environment account connection in an environment account so that environment infrastructure resources can be provisioned in the environment account from a management account.</p> <p>An environment account connection is a secure bi-directional connection between a <i>management account</i> and an <i>environment account</i> that maintains authorization and permissions. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the environment account connection that the first request created.</p>
            management_account_id: <p>The ID of the management account that accepts or rejects the environment account connection. You create and manage the Proton environment in this account. If the management account accepts the environment account connection, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. Proton uses this role to provision infrastructure resources in the associated environment account.</p>
            environment_name: <p>The name of the Proton environment that's created in the associated management account.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment account connection. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>You must specify <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in this account.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.create_environment_account_connection_input.CreateEnvironmentAccountConnectionInput]",
        ) -> OperationResponse[
            "capo_proton.types.create_environment_account_connection_output.CreateEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_environment_account_connection

            output, http_response = (
                capo_proton._operations.aws_proton20200720.create_environment_account_connection.create_environment_account_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_environment_account_connection_input.CreateEnvironmentAccountConnectionInput = {
            "management_account_id": management_account_id,
            "environment_name": environment_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
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
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.get_environment_account_connection_output.GetEnvironmentAccountConnectionOutput":
        """<p>In an environment account, get the detailed data for an environment account connection.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_environment_account_connection_input.GetEnvironmentAccountConnectionInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_environment_account_connection_output.GetEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_environment_account_connection

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_environment_account_connection.get_environment_account_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_environment_account_connection_input.GetEnvironmentAccountConnectionInput = {
            "id": id
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
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.update_environment_account_connection_output.UpdateEnvironmentAccountConnectionOutput":
        """<p>In an environment account, update an environment account connection to use a new IAM role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to update.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that's associated with the environment account connection to update.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>The environment account connection must have a <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in the account.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>

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
            req: "OperationRequest[capo_proton.types.update_environment_account_connection_input.UpdateEnvironmentAccountConnectionInput]",
        ) -> OperationResponse[
            "capo_proton.types.update_environment_account_connection_output.UpdateEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_environment_account_connection

            output, http_response = (
                capo_proton._operations.aws_proton20200720.update_environment_account_connection.update_environment_account_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_environment_account_connection_input.UpdateEnvironmentAccountConnectionInput = {
            "id": id
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
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
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_environment_account_connection_output.DeleteEnvironmentAccountConnectionOutput":
        """<p>In an environment account, delete an environment account connection.</p> <p>After you delete an environment account connection that’s in use by an Proton environment, Proton <i>can’t</i> manage the environment infrastructure resources until a new environment account connection is accepted for the environment account and associated environment. You're responsible for cleaning up provisioned resources that remain without an environment connection.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to delete.</p>

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
            req: "OperationRequest[capo_proton.types.delete_environment_account_connection_input.DeleteEnvironmentAccountConnectionInput]",
        ) -> OperationResponse[
            "capo_proton.types.delete_environment_account_connection_output.DeleteEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_environment_account_connection

            output, http_response = (
                capo_proton._operations.aws_proton20200720.delete_environment_account_connection.delete_environment_account_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_environment_account_connection_input.DeleteEnvironmentAccountConnectionInput = {
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
        requested_by: "capo_proton.types.environment_account_connection_requester_account_type.EnvironmentAccountConnectionRequesterAccountType",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        statuses: Optional[
            "capo_proton.types.environment_account_connection_status_list.EnvironmentAccountConnectionStatusList"
        ] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_environment_account_connections_output.ListEnvironmentAccountConnectionsOutput":
        """<p>View a list of environment account connections.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            requested_by: <p>The type of account making the <code>ListEnvironmentAccountConnections</code> request.</p>
            environment_name: <p>The environment name that's associated with each listed environment account connection.</p>
            statuses: <p>The status details for each listed environment account connection.</p>
            next_token: <p>A token that indicates the location of the next environment account connection in the array of environment account connections, after the list of environment account connections that was previously requested.</p>
            max_results: <p>The maximum number of environment account connections to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_environment_account_connections_input.ListEnvironmentAccountConnectionsInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_environment_account_connections_output.ListEnvironmentAccountConnectionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environment_account_connections

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_environment_account_connections.list_environment_account_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_environment_account_connections_input.ListEnvironmentAccountConnectionsInput = {
            "requested_by": requested_by
        }
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if statuses is not None:
            input_["statuses"] = statuses
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

    def accept_environment_account_connection(
        self,
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.accept_environment_account_connection_output.AcceptEnvironmentAccountConnectionOutput":
        """<p>In a management account, an environment account connection request is accepted. When the environment account connection request is accepted, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection.</p>

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
            req: "OperationRequest[capo_proton.types.accept_environment_account_connection_input.AcceptEnvironmentAccountConnectionInput]",
        ) -> OperationResponse[
            "capo_proton.types.accept_environment_account_connection_output.AcceptEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.accept_environment_account_connection

            output, http_response = (
                capo_proton._operations.aws_proton20200720.accept_environment_account_connection.accept_environment_account_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.accept_environment_account_connection_input.AcceptEnvironmentAccountConnectionInput = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_environment_account_connection(
        self,
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.reject_environment_account_connection_output.RejectEnvironmentAccountConnectionOutput":
        """<p>In a management account, reject an environment account connection from another environment account.</p> <p>After you reject an environment account connection request, you <i>can't</i> accept or use the rejected environment account connection.</p> <p>You <i>can’t</i> reject an environment account connection that's connected to an environment.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to reject.</p>

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
            req: "OperationRequest[capo_proton.types.reject_environment_account_connection_input.RejectEnvironmentAccountConnectionInput]",
        ) -> OperationResponse[
            "capo_proton.types.reject_environment_account_connection_output.RejectEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.reject_environment_account_connection

            output, http_response = (
                capo_proton._operations.aws_proton20200720.reject_environment_account_connection.reject_environment_account_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.reject_environment_account_connection_input.RejectEnvironmentAccountConnectionInput = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEnvironmentAccountConnectionResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def create(
        self,
        management_account_id: "capo_proton.types.aws_account_id.AwsAccountId",
        environment_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
        role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.create_environment_account_connection_output.CreateEnvironmentAccountConnectionOutput":
        """<p>Create an environment account connection in an environment account so that environment infrastructure resources can be provisioned in the environment account from a management account.</p> <p>An environment account connection is a secure bi-directional connection between a <i>management account</i> and an <i>environment account</i> that maintains authorization and permissions. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the environment account connection that the first request created.</p>
            management_account_id: <p>The ID of the management account that accepts or rejects the environment account connection. You create and manage the Proton environment in this account. If the management account accepts the environment account connection, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. Proton uses this role to provision infrastructure resources in the associated environment account.</p>
            environment_name: <p>The name of the Proton environment that's created in the associated management account.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment account connection. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>You must specify <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in this account.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_environment_account_connection_input.CreateEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_environment_account_connection_output.CreateEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_environment_account_connection.async_create_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_environment_account_connection_input.CreateEnvironmentAccountConnectionInput = {
            "management_account_id": management_account_id,
            "environment_name": environment_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
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
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_environment_account_connection_output.GetEnvironmentAccountConnectionOutput":
        """<p>In an environment account, get the detailed data for an environment account connection.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_environment_account_connection_input.GetEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_environment_account_connection_output.GetEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_environment_account_connection.async_get_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_environment_account_connection_input.GetEnvironmentAccountConnectionInput = {
            "id": id
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
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        component_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
        codebuild_role_arn: Optional["capo_proton.types.role_arn.RoleArn"] = None,
    ) -> "capo_proton.types.update_environment_account_connection_output.UpdateEnvironmentAccountConnectionOutput":
        """<p>In an environment account, update an environment account connection to use a new IAM role.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to update.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that's associated with the environment account connection to update.</p>
            component_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role that Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.</p> <p>The environment account connection must have a <code>componentRoleArn</code> to allow directly defined components to be associated with any environments running in the account.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>
            codebuild_role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role in the environment account. Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.update_environment_account_connection_input.UpdateEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_environment_account_connection_output.UpdateEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_environment_account_connection.async_update_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_environment_account_connection_input.UpdateEnvironmentAccountConnectionInput = {
            "id": id
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
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
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_environment_account_connection_output.DeleteEnvironmentAccountConnectionOutput":
        """<p>In an environment account, delete an environment account connection.</p> <p>After you delete an environment account connection that’s in use by an Proton environment, Proton <i>can’t</i> manage the environment infrastructure resources until a new environment account connection is accepted for the environment account and associated environment. You're responsible for cleaning up provisioned resources that remain without an environment connection.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to delete.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.delete_environment_account_connection_input.DeleteEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_environment_account_connection_output.DeleteEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_environment_account_connection.async_delete_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_environment_account_connection_input.DeleteEnvironmentAccountConnectionInput = {
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
        requested_by: "capo_proton.types.environment_account_connection_requester_account_type.EnvironmentAccountConnectionRequesterAccountType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        statuses: Optional[
            "capo_proton.types.environment_account_connection_status_list.EnvironmentAccountConnectionStatusList"
        ] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_environment_account_connections_output.ListEnvironmentAccountConnectionsOutput":
        """<p>View a list of environment account connections.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            requested_by: <p>The type of account making the <code>ListEnvironmentAccountConnections</code> request.</p>
            environment_name: <p>The environment name that's associated with each listed environment account connection.</p>
            statuses: <p>The status details for each listed environment account connection.</p>
            next_token: <p>A token that indicates the location of the next environment account connection in the array of environment account connections, after the list of environment account connections that was previously requested.</p>
            max_results: <p>The maximum number of environment account connections to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_environment_account_connections_input.ListEnvironmentAccountConnectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_environment_account_connections_output.ListEnvironmentAccountConnectionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environment_account_connections

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_environment_account_connections.async_list_environment_account_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_environment_account_connections_input.ListEnvironmentAccountConnectionsInput = {
            "requested_by": requested_by
        }
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if statuses is not None:
            input_["statuses"] = statuses
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def accept_environment_account_connection(
        self,
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.accept_environment_account_connection_output.AcceptEnvironmentAccountConnectionOutput":
        """<p>In a management account, an environment account connection request is accepted. When the environment account connection request is accepted, Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.accept_environment_account_connection_input.AcceptEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.accept_environment_account_connection_output.AcceptEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.accept_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.accept_environment_account_connection.async_accept_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.accept_environment_account_connection_input.AcceptEnvironmentAccountConnectionInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reject_environment_account_connection(
        self,
        id: "capo_proton.types.environment_account_connection_id.EnvironmentAccountConnectionId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.reject_environment_account_connection_output.RejectEnvironmentAccountConnectionOutput":
        """<p>In a management account, reject an environment account connection from another environment account.</p> <p>After you reject an environment account connection request, you <i>can't</i> accept or use the rejected environment account connection.</p> <p>You <i>can’t</i> reject an environment account connection that's connected to an environment.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html">Environment account connections</a> in the <i>Proton User guide</i>.</p>

        Args:
            id: <p>The ID of the environment account connection to reject.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.reject_environment_account_connection_input.RejectEnvironmentAccountConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.reject_environment_account_connection_output.RejectEnvironmentAccountConnectionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.reject_environment_account_connection

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.reject_environment_account_connection.async_reject_environment_account_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.reject_environment_account_connection_input.RejectEnvironmentAccountConnectionInput = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
