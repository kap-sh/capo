from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

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
    import capo_continuum.types.associated_environment
    import capo_continuum.types.aws_account_id
    import capo_continuum.types.collector_client_token
    import capo_continuum.types.collector_id
    import capo_continuum.types.collector_name
    import capo_continuum.types.collector_type
    import capo_continuum.types.create_collector_input
    import capo_continuum.types.create_collector_output
    import capo_continuum.types.delete_collector_input
    import capo_continuum.types.environment_arn
    import capo_continuum.types.get_collector_data_access_authorization_input
    import capo_continuum.types.get_collector_data_access_authorization_output
    import capo_continuum.types.get_collector_input
    import capo_continuum.types.get_collector_output
    import capo_continuum.types.kubernetes_cluster_role_configuration
    import capo_continuum.types.kubernetes_cluster_role_update
    import capo_continuum.types.list_associated_environments_input
    import capo_continuum.types.list_associated_environments_output
    import capo_continuum.types.list_collectors_input
    import capo_continuum.types.list_collectors_output
    import capo_continuum.types.max_results
    import capo_continuum.types.next_token
    import capo_continuum.types.update_collector_input
    import capo_continuum.types.update_collector_output
    from capo_continuum._services.async_continuum import (
        AsyncContinuumClient,
        AsyncContinuumClientConfig,
    )
    from capo_continuum._services.continuum import (
        ContinuumClient,
        ContinuumClientConfig,
    )


class Collector:
    def __init__(self, service: ContinuumClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        type: Optional["capo_continuum.types.collector_type.CollectorType"] = None,
        kubernetes_cluster_role: Optional[
            "capo_continuum.types.kubernetes_cluster_role_configuration.KubernetesClusterRoleConfiguration"
        ] = None,
        client_token: Optional[
            "capo_continuum.types.collector_client_token.CollectorClientToken"
        ] = None,
    ) -> "capo_continuum.types.create_collector_output.CreateCollectorOutput":
        """Creates the Collector for the caller's account. Provisions an AWS Config service-linked recorder using the caller's federated access session and begins recording infrastructure changes.

        Args:
            type: Source to collect. Defaults to AWS_COLLECTOR when omitted.
            kubernetes_cluster_role: IAM role configuration used to collect Kubernetes cluster metadata. The authenticated caller must be allowed to pass its exact roleArn to Continuum.
            client_token: Caller-provided token that makes retried create requests return the original Collector rather than creating a duplicate.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request would exceed a service quota. Review your quota and request an increase if needed.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.create_collector_input.CreateCollectorInput]",
        ) -> OperationResponse[
            "capo_continuum.types.create_collector_output.CreateCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.create_collector.create_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.create_collector_input.CreateCollectorInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.create_collector_input

            return capo_continuum.types.create_collector_input.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateCollector", redact_input=_redact_input),
        )
        input_: capo_continuum.types.create_collector_input.CreateCollectorInput = {}
        if type is not None:
            input_["type"] = type
        if kubernetes_cluster_role is not None:
            input_["kubernetes_cluster_role"] = kubernetes_cluster_role
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

    def read(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_collector_output.GetCollectorOutput":
        """Retrieves the current state of the Collector for the caller's account.

        Args:
            collector_id: The unique identifier of the Collector to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_collector_input.GetCollectorInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_collector_output.GetCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_collector.get_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollector")
        )
        input_: capo_continuum.types.get_collector_input.GetCollectorInput = {
            "collector_id": collector_id
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
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        name: Optional["capo_continuum.types.collector_name.CollectorName"] = None,
        kubernetes_cluster_role: Optional[
            "capo_continuum.types.kubernetes_cluster_role_update.KubernetesClusterRoleUpdate"
        ] = None,
    ) -> "capo_continuum.types.update_collector_output.UpdateCollectorOutput":
        """Updates the customer-controlled mutable properties of a Collector. Only the name and Kubernetes cluster IAM role can be changed.

        Args:
            collector_id: The unique identifier of the Collector to update.
            name: The new customer-visible name.
            kubernetes_cluster_role: Atomic update to the IAM role configuration used to collect Kubernetes cluster metadata. The set variant requires a complete configuration; the authenticated caller must be allowed to pass its exact roleArn to Continuum. The remove variant clears both the role and external ID.

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
            req: "OperationRequest[capo_continuum.types.update_collector_input.UpdateCollectorInput]",
        ) -> OperationResponse[
            "capo_continuum.types.update_collector_output.UpdateCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.update_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.update_collector.update_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.update_collector_input.UpdateCollectorInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.update_collector_input

            return capo_continuum.types.update_collector_input.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateCollector", redact_input=_redact_input),
        )
        input_: capo_continuum.types.update_collector_input.UpdateCollectorInput = {
            "collector_id": collector_id
        }
        if name is not None:
            input_["name"] = name
        if kubernetes_cluster_role is not None:
            input_["kubernetes_cluster_role"] = kubernetes_cluster_role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
    ) -> None:
        """Deletes the Collector for the caller's account. The Collector first enters PENDING_DELETION, then the service removes its schedule, AWS Config service-linked recorder, versioned S3 bucket, KMS key, and persisted record.

        Args:
            collector_id: The unique identifier of the Collector to delete.

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
            req: "OperationRequest[capo_continuum.types.delete_collector_input.DeleteCollectorInput]",
        ) -> OperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.delete_collector

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.delete_collector.delete_collector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCollector")
        )
        input_: capo_continuum.types.delete_collector_input.DeleteCollectorInput = {
            "collector_id": collector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self, *, config_overrides: Optional[ContinuumClientConfig] = None
    ) -> "capo_continuum.types.list_collectors_output.ListCollectorsOutput":
        """Lists the Collectors owned by the authenticated caller's account, including a Collector whose deletion is in progress. A Collector that is still being created is omitted. The account-scoped Collector quota currently permits at most one result, so no result ordering applies.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.list_collectors_input.ListCollectorsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_collectors_output.ListCollectorsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_collectors

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_collectors.list_collectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCollectors")
        )
        input_: capo_continuum.types.list_collectors_input.ListCollectorsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_collector_data_access_authorization(
        self,
        account_id: "capo_continuum.types.aws_account_id.AwsAccountId",
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        environment_arn: Optional[
            "capo_continuum.types.environment_arn.EnvironmentArn"
        ] = None,
    ) -> "capo_continuum.types.get_collector_data_access_authorization_output.GetCollectorDataAccessAuthorizationOutput":
        """Authorizes an Environment's access to a Collector's data. Continuum calls this operation with the Environment's Collector data-access role before it reads the Collector's inventory, so grant continuum:GetCollectorDataAccessAuthorization to that role and, for a Collector in another account, in the Collector's resource policy. The operation evaluates the action against the exact Collector ARN and the Collector's current resource policy using IAM and the caller's authenticated request context, with environmentArn as the continuum:EnvironmentArn condition key. A successful request returns HTTP 200 with no response members. If access is not granted, the operation returns AccessDeniedException without disclosing Collector existence, ownership, or the policy layer that denied access. The service does not reinterpret the policy using only an account ID.

        Args:
            account_id: The AWS account that owns the Collector.
            collector_id: The unique identifier of the Collector.
            environment_arn: The full ARN of the Environment requesting the Collector's data. The Environment must be in the caller's account. Continuum supplies this value as the continuum:EnvironmentArn condition key.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_continuum.types.get_collector_data_access_authorization_input.GetCollectorDataAccessAuthorizationInput]",
        ) -> OperationResponse[
            "capo_continuum.types.get_collector_data_access_authorization_output.GetCollectorDataAccessAuthorizationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_collector_data_access_authorization

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.get_collector_data_access_authorization.get_collector_data_access_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollectorDataAccessAuthorization")
        )
        input_: capo_continuum.types.get_collector_data_access_authorization_input.GetCollectorDataAccessAuthorizationInput = {
            "account_id": account_id,
            "collector_id": collector_id,
        }
        if environment_arn is not None:
            input_["environment_arn"] = environment_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_associated_environments(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[ContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_associated_environments_output.ListAssociatedEnvironmentsOutput":
        """Lists the Environments currently associated with one Collector in lexicographically ascending environmentArn order. The ARN identifies each Environment across accounts within the Collector's Region.

        Args:
            collector_id: The unique identifier of the Collector whose associations to list.
            max_results: Maximum number of Environment associations to return.
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
            req: "OperationRequest[capo_continuum.types.list_associated_environments_input.ListAssociatedEnvironmentsInput]",
        ) -> OperationResponse[
            "capo_continuum.types.list_associated_environments_output.ListAssociatedEnvironmentsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_associated_environments

            output, http_response = (
                capo_continuum._operations.continuum_control_plane.list_associated_environments.list_associated_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAssociatedEnvironments")
        )
        input_: capo_continuum.types.list_associated_environments_input.ListAssociatedEnvironmentsInput = {
            "collector_id": collector_id
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


class AsyncCollector:
    def __init__(self, service: AsyncContinuumClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        type: Optional["capo_continuum.types.collector_type.CollectorType"] = None,
        kubernetes_cluster_role: Optional[
            "capo_continuum.types.kubernetes_cluster_role_configuration.KubernetesClusterRoleConfiguration"
        ] = None,
        client_token: Optional[
            "capo_continuum.types.collector_client_token.CollectorClientToken"
        ] = None,
    ) -> "capo_continuum.types.create_collector_output.CreateCollectorOutput":
        """Creates the Collector for the caller's account. Provisions an AWS Config service-linked recorder using the caller's federated access session and begins recording infrastructure changes.

        Args:
            type: Source to collect. Defaults to AWS_COLLECTOR when omitted.
            kubernetes_cluster_role: IAM role configuration used to collect Kubernetes cluster metadata. The authenticated caller must be allowed to pass its exact roleArn to Continuum.
            client_token: Caller-provided token that makes retried create requests return the original Collector rather than creating a duplicate.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.conflict_exception.ConflictException: The request could not be completed due to a conflict with the current state of the resource.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request would exceed a service quota. Review your quota and request an increase if needed.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.create_collector_input.CreateCollectorInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.create_collector_output.CreateCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.create_collector

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.create_collector.async_create_collector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.create_collector_input.CreateCollectorInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.create_collector_input

            return capo_continuum.types.create_collector_input.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateCollector", redact_input=_redact_input),
        )
        input_: capo_continuum.types.create_collector_input.CreateCollectorInput = {}
        if type is not None:
            input_["type"] = type
        if kubernetes_cluster_role is not None:
            input_["kubernetes_cluster_role"] = kubernetes_cluster_role
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

    async def read(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
    ) -> "capo_continuum.types.get_collector_output.GetCollectorOutput":
        """Retrieves the current state of the Collector for the caller's account.

        Args:
            collector_id: The unique identifier of the Collector to retrieve.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.get_collector_input.GetCollectorInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.get_collector_output.GetCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_collector

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.get_collector.async_get_collector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollector")
        )
        input_: capo_continuum.types.get_collector_input.GetCollectorInput = {
            "collector_id": collector_id
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
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        name: Optional["capo_continuum.types.collector_name.CollectorName"] = None,
        kubernetes_cluster_role: Optional[
            "capo_continuum.types.kubernetes_cluster_role_update.KubernetesClusterRoleUpdate"
        ] = None,
    ) -> "capo_continuum.types.update_collector_output.UpdateCollectorOutput":
        """Updates the customer-controlled mutable properties of a Collector. Only the name and Kubernetes cluster IAM role can be changed.

        Args:
            collector_id: The unique identifier of the Collector to update.
            name: The new customer-visible name.
            kubernetes_cluster_role: Atomic update to the IAM role configuration used to collect Kubernetes cluster metadata. The set variant requires a complete configuration; the authenticated caller must be allowed to pass its exact roleArn to Continuum. The remove variant clears both the role and external ID.

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
            req: "AsyncOperationRequest[capo_continuum.types.update_collector_input.UpdateCollectorInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.update_collector_output.UpdateCollectorOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.update_collector

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.update_collector.async_update_collector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_continuum.types.update_collector_input.UpdateCollectorInput",
        ) -> dict[str, Any]:
            import capo_continuum.types.update_collector_input

            return capo_continuum.types.update_collector_input.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateCollector", redact_input=_redact_input),
        )
        input_: capo_continuum.types.update_collector_input.UpdateCollectorInput = {
            "collector_id": collector_id
        }
        if name is not None:
            input_["name"] = name
        if kubernetes_cluster_role is not None:
            input_["kubernetes_cluster_role"] = kubernetes_cluster_role

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
    ) -> None:
        """Deletes the Collector for the caller's account. The Collector first enters PENDING_DELETION, then the service removes its schedule, AWS Config service-linked recorder, versioned S3 bucket, KMS key, and persisted record.

        Args:
            collector_id: The unique identifier of the Collector to delete.

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
            req: "AsyncOperationRequest[capo_continuum.types.delete_collector_input.DeleteCollectorInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_continuum._operations.continuum_control_plane.delete_collector

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.delete_collector.async_delete_collector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCollector")
        )
        input_: capo_continuum.types.delete_collector_input.DeleteCollectorInput = {
            "collector_id": collector_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self, *, config_overrides: Optional[AsyncContinuumClientConfig] = None
    ) -> "capo_continuum.types.list_collectors_output.ListCollectorsOutput":
        """Lists the Collectors owned by the authenticated caller's account, including a Collector whose deletion is in progress. A Collector that is still being created is omitted. The account-scoped Collector quota currently permits at most one result, so no result ordering applies.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.list_collectors_input.ListCollectorsInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.list_collectors_output.ListCollectorsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_collectors

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.list_collectors.async_list_collectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCollectors")
        )
        input_: capo_continuum.types.list_collectors_input.ListCollectorsInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_collector_data_access_authorization(
        self,
        account_id: "capo_continuum.types.aws_account_id.AwsAccountId",
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        environment_arn: Optional[
            "capo_continuum.types.environment_arn.EnvironmentArn"
        ] = None,
    ) -> "capo_continuum.types.get_collector_data_access_authorization_output.GetCollectorDataAccessAuthorizationOutput":
        """Authorizes an Environment's access to a Collector's data. Continuum calls this operation with the Environment's Collector data-access role before it reads the Collector's inventory, so grant continuum:GetCollectorDataAccessAuthorization to that role and, for a Collector in another account, in the Collector's resource policy. The operation evaluates the action against the exact Collector ARN and the Collector's current resource policy using IAM and the caller's authenticated request context, with environmentArn as the continuum:EnvironmentArn condition key. A successful request returns HTTP 200 with no response members. If access is not granted, the operation returns AccessDeniedException without disclosing Collector existence, ownership, or the policy layer that denied access. The service does not reinterpret the policy using only an account ID.

        Args:
            account_id: The AWS account that owns the Collector.
            collector_id: The unique identifier of the Collector.
            environment_arn: The full ARN of the Environment requesting the Collector's data. The Environment must be in the caller's account. Continuum supplies this value as the continuum:EnvironmentArn condition key.

        Raises:
            capo_continuum.errors.access_denied_exception.AccessDeniedException: The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
            capo_continuum.errors.internal_server_exception.InternalServerException: The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
            capo_continuum.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_continuum.errors.validation_exception.ValidationException
            capo_continuum.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_continuum.types.get_collector_data_access_authorization_input.GetCollectorDataAccessAuthorizationInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.get_collector_data_access_authorization_output.GetCollectorDataAccessAuthorizationOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.get_collector_data_access_authorization

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.get_collector_data_access_authorization.async_get_collector_data_access_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollectorDataAccessAuthorization")
        )
        input_: capo_continuum.types.get_collector_data_access_authorization_input.GetCollectorDataAccessAuthorizationInput = {
            "account_id": account_id,
            "collector_id": collector_id,
        }
        if environment_arn is not None:
            input_["environment_arn"] = environment_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_associated_environments(
        self,
        collector_id: "capo_continuum.types.collector_id.CollectorId",
        *,
        config_overrides: Optional[AsyncContinuumClientConfig] = None,
        max_results: Optional["capo_continuum.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_continuum.types.next_token.NextToken"] = None,
    ) -> "capo_continuum.types.list_associated_environments_output.ListAssociatedEnvironmentsOutput":
        """Lists the Environments currently associated with one Collector in lexicographically ascending environmentArn order. The ARN identifies each Environment across accounts within the Collector's Region.

        Args:
            collector_id: The unique identifier of the Collector whose associations to list.
            max_results: Maximum number of Environment associations to return.
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
            req: "AsyncOperationRequest[capo_continuum.types.list_associated_environments_input.ListAssociatedEnvironmentsInput]",
        ) -> AsyncOperationResponse[
            "capo_continuum.types.list_associated_environments_output.ListAssociatedEnvironmentsOutput"
        ]:
            import capo_continuum._operations.continuum_control_plane.list_associated_environments

            (
                output,
                http_response,
            ) = await capo_continuum._operations.continuum_control_plane.list_associated_environments.async_list_associated_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAssociatedEnvironments")
        )
        input_: capo_continuum.types.list_associated_environments_input.ListAssociatedEnvironmentsInput = {
            "collector_id": collector_id
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
