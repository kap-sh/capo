from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_continuum._auth._signers
import capo_continuum._auth._sigv4
from capo_continuum._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_continuum.types.associate_collector_input
    import capo_continuum.types.associate_collector_output
    import capo_continuum.types.associated_collector
    import capo_continuum.types.association_client_token
    import capo_continuum.types.collector_arn
    import capo_continuum.types.create_environment_configuration
    import capo_continuum.types.create_environment_input
    import capo_continuum.types.create_environment_output
    import capo_continuum.types.delete_environment_input
    import capo_continuum.types.disassociate_collector_input
    import capo_continuum.types.environment_id
    import capo_continuum.types.environment_list_entry
    import capo_continuum.types.environment_name
    import capo_continuum.types.environment_source_role_arn
    import capo_continuum.types.get_environment_input
    import capo_continuum.types.get_environment_output
    import capo_continuum.types.list_associated_collectors_input
    import capo_continuum.types.list_associated_collectors_output
    import capo_continuum.types.list_environments_input
    import capo_continuum.types.list_environments_output
    import capo_continuum.types.max_results
    import capo_continuum.types.next_token
    import capo_continuum.types.update_environment_configuration
    import capo_continuum.types.update_environment_input
    import capo_continuum.types.update_environment_output
    from capo_continuum._services.async_continuum import (
        AsyncContinuumClient,
        AsyncContinuumClientConfig,
    )
    from capo_continuum._services.continuum import (
        ContinuumClient,
        ContinuumClientConfig,
    )


class Environment:
    def __init__(self, service: ContinuumClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_continuum.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        configuration: Optional[
            "capo_continuum.types.create_environment_configuration.CreateEnvironmentConfiguration"
        ] = None,
    ) -> "capo_continuum.types.create_environment_output.CreateEnvironmentOutput":
        """Creates an environment and starts its validation and any requested provisioning. Storage provisioning and dependency checks may continue after the initial 201 response; use GetEnvironment to observe completion.

        Args:
            name: The customer-visible name of the environment.
            configuration: Type-specific configuration. Omission creates a code environment with the default operating policy and no sources.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request would exceed a service quota. Review your quota and request an increase if needed.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.create_environment_input.CreateEnvironmentInput]",
        ) -> OperationResponse[
            "capo_continuum.types.create_environment_output.CreateEnvironmentOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_environment

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateEnvironment")
        )
        input_: capo_continuum.types.create_environment_input.CreateEnvironmentInput = {
            "name": name
        }
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_environment_output.GetEnvironmentOutput":
        """Retrieves the current state and configuration of an environment.

        Args:
            environment_id: The unique identifier of the environment to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_environment_input.GetEnvironmentInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_environment_output.GetEnvironmentOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_environment

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetEnvironment")
        )
        input_: capo_continuum.types.get_environment_input.GetEnvironmentInput = {
            "environment_id": environment_id
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
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        name: Optional["capo_continuum.types.environment_name.EnvironmentName"] = None,
        configuration: Optional[
            "capo_continuum.types.update_environment_configuration.UpdateEnvironmentConfiguration"
        ] = None,
    ) -> "capo_continuum.types.update_environment_output.UpdateEnvironmentOutput":
        """Updates the customer-controlled mutable properties of an environment. Only the name, the environment's S3 integration source and repository selections, its scan frequency, its network policy, and its patch creation policy can be changed.

        Args:
            environment_id: The unique identifier of the environment to update.
            name: The new customer-visible name.
            configuration: Type-specific configuration changes. Omission preserves the configuration.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.update_environment_input.UpdateEnvironmentInput]",
        ) -> OperationResponse[
            "capo_continuum.types.update_environment_output.UpdateEnvironmentOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.update_environment

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.update_environment.update_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateEnvironment")
        )
        input_: capo_continuum.types.update_environment_input.UpdateEnvironmentInput = {
            "environment_id": environment_id
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> None:
        """Deletes an environment and its associated resources.

        Args:
            environment_id: The unique identifier of the environment to delete.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.delete_environment_input.DeleteEnvironmentInput]",
        ) -> OperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.delete_environment

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteEnvironment")
        )
        input_: capo_continuum.types.delete_environment_input.DeleteEnvironmentInput = {
            "environment_id": environment_id
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
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_environments_output.ListEnvironmentsOutput":
        """Lists all environments in your account in descending environmentId order. This complete-inventory operation intentionally has no response filters; see the input documentation for the API standards justification.

        Args:
            max_results: The maximum number of results to return in a single call.
            next_token: A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_environments_input.ListEnvironmentsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_environments_output.ListEnvironmentsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_environments

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListEnvironments")
        )
        input_: capo_continuum.types.list_environments_input.ListEnvironmentsInput = {}
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

    def associate_collector(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        collector_arn: "capo_continuum.types.collector_arn.CollectorArn",
        collector_data_access_role_arn: "capo_continuum.types.environment_source_role_arn.EnvironmentSourceRoleArn",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        client_token: Optional[
            "capo_continuum.types.association_client_token.AssociationClientToken"
        ] = None,
    ) -> "capo_continuum.types.associate_collector_output.AssociateCollectorOutput":
        """Associates one Collector with this Environment and configures the customer role Continuum uses to authorize access to associated Collector data. The caller must have permission on the Environment and permission to pass the role. Continuum assumes the supplied role and calls GetCollectorDataAccessAuthorization on the requested Collector; only a successful authorization response permits the association. The caller does not need Collector data-access permission. The Environment retains its other Collector associations. Calling again with an existing association is safe and does not create a duplicate.

        Args:
            environment_id: The unique identifier of the Environment making the association.
            client_token: Caller-provided token that makes retried association requests idempotent. The first successful request binds the token to the complete Collector ARN, supplied role, and result for at least 24 hours. During that retry window, reusing it with a different request fails with ConflictException. A matching replay still requires the supplied role to have current Collector access. Once authorized, a matching replay returns the stored result without changing association state. Revocation can deny a replay; it does not remove the stored association or its original result.
            collector_arn: The ARN of the Collector to associate with this Environment.
            collector_data_access_role_arn: IAM role in the Environment account that Continuum assumes before authorizing access to associated Collector inventory. Every association, including a same-account association, requires this role. The supplied ARN replaces the Environment's previously stored role. The customer is responsible for granting the role access to every Collector that should contribute data.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.associate_collector_input.AssociateCollectorInput]",
        ) -> OperationResponse[
            "capo_continuum.types.associate_collector_output.AssociateCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.associate_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.associate_collector.associate_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateCollector")
        )
        input_: capo_continuum.types.associate_collector_input.AssociateCollectorInput = {
            "environment_id": environment_id,
            "collector_arn": collector_arn,
            "collector_data_access_role_arn": collector_data_access_role_arn,
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

    def disassociate_collector(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        collector_arn: "capo_continuum.types.collector_arn.CollectorArn",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> None:
        """Removes one Collector association from this Environment, preserving its other associations. The stored Collector data-access role is cleared when no Collector associations remain. The Environment owner must have permission to disassociate. A current Collector access grant is not required, and the Collector does not need to remain active or present, so stale or revoked associations can be cleaned up.

        Args:
            environment_id: The unique identifier of the Environment whose associations are updated.
            collector_arn: The ARN of the Collector to disassociate from this Environment.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.disassociate_collector_input.DisassociateCollectorInput]",
        ) -> OperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.disassociate_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.disassociate_collector.disassociate_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateCollector")
        )
        input_: capo_continuum.types.disassociate_collector_input.DisassociateCollectorInput = {
            "environment_id": environment_id,
            "collector_arn": collector_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_associated_collectors(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_associated_collectors_output.ListAssociatedCollectorsOutput":
        """Lists the Collectors currently associated with one Environment in ascending collectorId order. Each entry carries the Collector ARN, so a listed association can be passed straight to DisassociateCollector, including when the Collector belongs to another account. An association recorded before Continuum persisted the ARN is omitted from the response, because without the ARN it cannot be acted on.

        Args:
            environment_id: The unique identifier of the Environment whose associations to list.
            max_results: Maximum number of associated Collectors to return.
            next_token: Pagination token returned by a prior request.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_associated_collectors_input.ListAssociatedCollectorsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_associated_collectors_output.ListAssociatedCollectorsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_associated_collectors

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_associated_collectors.list_associated_collectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAssociatedCollectors")
        )
        input_: capo_continuum.types.list_associated_collectors_input.ListAssociatedCollectorsInput = {
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


class AsyncEnvironment:
    def __init__(self, service: AsyncContinuumClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_continuum.types.environment_name.EnvironmentName",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        configuration: Optional[
            "capo_continuum.types.create_environment_configuration.CreateEnvironmentConfiguration"
        ] = None,
    ) -> "capo_continuum.types.create_environment_output.CreateEnvironmentOutput":
        """Creates an environment and starts its validation and any requested provisioning. Storage provisioning and dependency checks may continue after the initial 201 response; use GetEnvironment to observe completion.

        Args:
            name: The customer-visible name of the environment.
            configuration: Type-specific configuration. Omission creates a code environment with the default operating policy and no sources.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request would exceed a service quota. Review your quota and request an increase if needed.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.create_environment_input.CreateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.create_environment_output.CreateEnvironmentOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_environment

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.create_environment.async_create_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateEnvironment")
        )
        input_: capo_continuum.types.create_environment_input.CreateEnvironmentInput = {
            "name": name
        }
        if configuration is not None:
            input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_environment_output.GetEnvironmentOutput":
        """Retrieves the current state and configuration of an environment.

        Args:
            environment_id: The unique identifier of the environment to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.get_environment_input.GetEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.get_environment_output.GetEnvironmentOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_environment

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetEnvironment")
        )
        input_: capo_continuum.types.get_environment_input.GetEnvironmentInput = {
            "environment_id": environment_id
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
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        name: Optional["capo_continuum.types.environment_name.EnvironmentName"] = None,
        configuration: Optional[
            "capo_continuum.types.update_environment_configuration.UpdateEnvironmentConfiguration"
        ] = None,
    ) -> "capo_continuum.types.update_environment_output.UpdateEnvironmentOutput":
        """Updates the customer-controlled mutable properties of an environment. Only the name, the environment's S3 integration source and repository selections, its scan frequency, its network policy, and its patch creation policy can be changed.

        Args:
            environment_id: The unique identifier of the environment to update.
            name: The new customer-visible name.
            configuration: Type-specific configuration changes. Omission preserves the configuration.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.update_environment_input.UpdateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.update_environment_output.UpdateEnvironmentOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.update_environment

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.update_environment.async_update_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateEnvironment")
        )
        input_: capo_continuum.types.update_environment_input.UpdateEnvironmentInput = {
            "environment_id": environment_id
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
    ) -> None:
        """Deletes an environment and its associated resources.

        Args:
            environment_id: The unique identifier of the environment to delete.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.delete_environment_input.DeleteEnvironmentInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.delete_environment

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.delete_environment.async_delete_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteEnvironment")
        )
        input_: capo_continuum.types.delete_environment_input.DeleteEnvironmentInput = {
            "environment_id": environment_id
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
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_environments_output.ListEnvironmentsOutput":
        """Lists all environments in your account in descending environmentId order. This complete-inventory operation intentionally has no response filters; see the input documentation for the API standards justification.

        Args:
            max_results: The maximum number of results to return in a single call.
            next_token: A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.list_environments_input.ListEnvironmentsInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.list_environments_output.ListEnvironmentsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_environments

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListEnvironments")
        )
        input_: capo_continuum.types.list_environments_input.ListEnvironmentsInput = {}
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

    async def associate_collector(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        collector_arn: "capo_continuum.types.collector_arn.CollectorArn",
        collector_data_access_role_arn: "capo_continuum.types.environment_source_role_arn.EnvironmentSourceRoleArn",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        client_token: Optional[
            "capo_continuum.types.association_client_token.AssociationClientToken"
        ] = None,
    ) -> "capo_continuum.types.associate_collector_output.AssociateCollectorOutput":
        """Associates one Collector with this Environment and configures the customer role Continuum uses to authorize access to associated Collector data. The caller must have permission on the Environment and permission to pass the role. Continuum assumes the supplied role and calls GetCollectorDataAccessAuthorization on the requested Collector; only a successful authorization response permits the association. The caller does not need Collector data-access permission. The Environment retains its other Collector associations. Calling again with an existing association is safe and does not create a duplicate.

        Args:
            environment_id: The unique identifier of the Environment making the association.
            client_token: Caller-provided token that makes retried association requests idempotent. The first successful request binds the token to the complete Collector ARN, supplied role, and result for at least 24 hours. During that retry window, reusing it with a different request fails with ConflictException. A matching replay still requires the supplied role to have current Collector access. Once authorized, a matching replay returns the stored result without changing association state. Revocation can deny a replay; it does not remove the stored association or its original result.
            collector_arn: The ARN of the Collector to associate with this Environment.
            collector_data_access_role_arn: IAM role in the Environment account that Continuum assumes before authorizing access to associated Collector inventory. Every association, including a same-account association, requires this role. The supplied ARN replaces the Environment's previously stored role. The customer is responsible for granting the role access to every Collector that should contribute data.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.associate_collector_input.AssociateCollectorInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.associate_collector_output.AssociateCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.associate_collector

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.associate_collector.async_associate_collector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateCollector")
        )
        input_: capo_continuum.types.associate_collector_input.AssociateCollectorInput = {
            "environment_id": environment_id,
            "collector_arn": collector_arn,
            "collector_data_access_role_arn": collector_data_access_role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_collector(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        collector_arn: "capo_continuum.types.collector_arn.CollectorArn",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
    ) -> None:
        """Removes one Collector association from this Environment, preserving its other associations. The stored Collector data-access role is cleared when no Collector associations remain. The Environment owner must have permission to disassociate. A current Collector access grant is not required, and the Collector does not need to remain active or present, so stale or revoked associations can be cleaned up.

        Args:
            environment_id: The unique identifier of the Environment whose associations are updated.
            collector_arn: The ARN of the Collector to disassociate from this Environment.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.disassociate_collector_input.DisassociateCollectorInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.disassociate_collector

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.disassociate_collector.async_disassociate_collector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateCollector")
        )
        input_: capo_continuum.types.disassociate_collector_input.DisassociateCollectorInput = {
            "environment_id": environment_id,
            "collector_arn": collector_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_associated_collectors(
        self,
        environment_id: "capo_continuum.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_associated_collectors_output.ListAssociatedCollectorsOutput":
        """Lists the Collectors currently associated with one Environment in ascending collectorId order. Each entry carries the Collector ARN, so a listed association can be passed straight to DisassociateCollector, including when the Collector belongs to another account. An association recorded before Continuum persisted the ARN is omitted from the response, because without the ARN it cannot be acted on.

        Args:
            environment_id: The unique identifier of the Environment whose associations to list.
            max_results: Maximum number of associated Collectors to return.
            next_token: Pagination token returned by a prior request.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.list_associated_collectors_input.ListAssociatedCollectorsInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.list_associated_collectors_output.ListAssociatedCollectorsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_associated_collectors

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.list_associated_collectors.async_list_associated_collectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAssociatedCollectors")
        )
        input_: capo_continuum.types.list_associated_collectors_input.ListAssociatedCollectorsInput = {
            "environment_id": environment_id
        }
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
