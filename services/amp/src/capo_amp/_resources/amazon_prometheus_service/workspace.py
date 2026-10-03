from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_amp._auth._signers
import capo_amp._auth._sigv4
from capo_amp._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_amp.types.create_workspace_request
    import capo_amp.types.create_workspace_response
    import capo_amp.types.delete_workspace_request
    import capo_amp.types.describe_workspace_request
    import capo_amp.types.describe_workspace_response
    import capo_amp.types.idempotency_token
    import capo_amp.types.kms_key_arn
    import capo_amp.types.list_workspaces_request
    import capo_amp.types.list_workspaces_response
    import capo_amp.types.pagination_token
    import capo_amp.types.tag_map
    import capo_amp.types.update_workspace_alias_request
    import capo_amp.types.workspace_alias
    import capo_amp.types.workspace_id
    import capo_amp.types.workspace_summary
    from capo_amp._services.amp import ampClient, ampClientConfig
    from capo_amp._services.async_amp import AsyncampClient, AsyncampClientConfig


class Workspace:
    def __init__(self, service: ampClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[ampClientConfig] = None,
        alias: Optional["capo_amp.types.workspace_alias.WorkspaceAlias"] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_amp.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional["capo_amp.types.kms_key_arn.KmsKeyArn"] = None,
    ) -> "capo_amp.types.create_workspace_response.CreateWorkspaceResponse":
        """<p>Creates a Prometheus workspace. A workspace is a logical space dedicated to the storage and querying of Prometheus metrics. You can have one or more workspaces in each Region in your account.</p>

        Args:
            alias: <p>An alias that you assign to this workspace to help you identify it. It does not need to be unique.</p> <p>Blank spaces at the beginning or end of the alias that you specify will be trimmed from the value used.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>
            tags: <p>The list of tag keys and values to associate with the workspace.</p>
            kms_key_arn: <p>(optional) The ARN for a customer managed KMS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html">Encryption at rest</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amp.types.create_workspace_request.CreateWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_amp.types.create_workspace_response.CreateWorkspaceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.create_workspace

            output, http_response = (
                capo_amp._operations.amazon_prometheus_service.create_workspace.create_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.create_workspace_request.CreateWorkspaceRequest = {}
        if alias is not None:
            input_["alias"] = alias
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[ampClientConfig] = None,
    ) -> "capo_amp.types.describe_workspace_response.DescribeWorkspaceResponse":
        """<p>Returns information about an existing workspace. </p>

        Args:
            workspace_id: <p>The ID of the workspace to describe.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amp.types.describe_workspace_request.DescribeWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_amp.types.describe_workspace_response.DescribeWorkspaceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_workspace

            output, http_response = (
                capo_amp._operations.amazon_prometheus_service.describe_workspace.describe_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.describe_workspace_request.DescribeWorkspaceRequest = {
            "workspace_id": workspace_id
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
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[ampClientConfig] = None,
        alias: Optional["capo_amp.types.workspace_alias.WorkspaceAlias"] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Updates the alias of an existing workspace. </p>

        Args:
            workspace_id: <p>The ID of the workspace to update.</p>
            alias: <p>The new alias for the workspace. It does not need to be unique.</p> <p>Amazon Managed Service for Prometheus will automatically strip any blank spaces from the beginning and end of the alias that you specify.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amp.types.update_workspace_alias_request.UpdateWorkspaceAliasRequest]",
        ) -> OperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.update_workspace_alias

            output, http_response = (
                capo_amp._operations.amazon_prometheus_service.update_workspace_alias.update_workspace_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.update_workspace_alias_request.UpdateWorkspaceAliasRequest = {
            "workspace_id": workspace_id
        }
        if alias is not None:
            input_["alias"] = alias
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

    def delete(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[ampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Deletes an existing workspace. </p> <note> <p>When you delete a workspace, the data that has been ingested into it is not immediately deleted. It will be permanently deleted within one month.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace to delete.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amp.types.delete_workspace_request.DeleteWorkspaceRequest]",
        ) -> OperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.delete_workspace

            output, http_response = (
                capo_amp._operations.amazon_prometheus_service.delete_workspace.delete_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.delete_workspace_request.DeleteWorkspaceRequest = {
            "workspace_id": workspace_id
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

    def list(
        self,
        *,
        config_overrides: Optional[ampClientConfig] = None,
        next_token: Optional["capo_amp.types.pagination_token.PaginationToken"] = None,
        alias: Optional["capo_amp.types.workspace_alias.WorkspaceAlias"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_amp.types.list_workspaces_response.ListWorkspacesResponse":
        """<p>Lists all of the Amazon Managed Service for Prometheus workspaces in your account. This includes workspaces being created or deleted. </p>

        Args:
            next_token: <p>The token for the next set of items to return. You receive this token from a previous call, and use it to get the next page of results. The other parameters must be the same as the initial call.</p> <p>For example, if your initial request has <code>maxResults</code> of 10, and there are 12 workspaces to return, then your initial request will return 10 and a <code>nextToken</code>. Using the next token in a subsequent call will return the remaining 2 workspaces.</p>
            alias: <p>If this is included, it filters the results to only the workspaces with names that start with the value that you specify here.</p> <p>Amazon Managed Service for Prometheus will automatically strip any blank spaces from the beginning and end of the alias that you specify.</p>
            max_results: <p>The maximum number of workspaces to return per request. The default is 100.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amp.types.list_workspaces_request.ListWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_amp.types.list_workspaces_response.ListWorkspacesResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.list_workspaces

            output, http_response = (
                capo_amp._operations.amazon_prometheus_service.list_workspaces.list_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.list_workspaces_request.ListWorkspacesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if alias is not None:
            input_["alias"] = alias
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncWorkspace:
    def __init__(self, service: AsyncampClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        alias: Optional["capo_amp.types.workspace_alias.WorkspaceAlias"] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_amp.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional["capo_amp.types.kms_key_arn.KmsKeyArn"] = None,
    ) -> "capo_amp.types.create_workspace_response.CreateWorkspaceResponse":
        """<p>Creates a Prometheus workspace. A workspace is a logical space dedicated to the storage and querying of Prometheus metrics. You can have one or more workspaces in each Region in your account.</p>

        Args:
            alias: <p>An alias that you assign to this workspace to help you identify it. It does not need to be unique.</p> <p>Blank spaces at the beginning or end of the alias that you specify will be trimmed from the value used.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>
            tags: <p>The list of tag keys and values to associate with the workspace.</p>
            kms_key_arn: <p>(optional) The ARN for a customer managed KMS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see <a href="https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html">Encryption at rest</a> in the <i>Amazon Managed Service for Prometheus User Guide</i>.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.create_workspace_request.CreateWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.create_workspace_response.CreateWorkspaceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.create_workspace

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.create_workspace.async_create_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.create_workspace_request.CreateWorkspaceRequest = {}
        if alias is not None:
            input_["alias"] = alias
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
    ) -> "capo_amp.types.describe_workspace_response.DescribeWorkspaceResponse":
        """<p>Returns information about an existing workspace. </p>

        Args:
            workspace_id: <p>The ID of the workspace to describe.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.describe_workspace_request.DescribeWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.describe_workspace_response.DescribeWorkspaceResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.describe_workspace

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.describe_workspace.async_describe_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.describe_workspace_request.DescribeWorkspaceRequest = {
            "workspace_id": workspace_id
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
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        alias: Optional["capo_amp.types.workspace_alias.WorkspaceAlias"] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Updates the alias of an existing workspace. </p>

        Args:
            workspace_id: <p>The ID of the workspace to update.</p>
            alias: <p>The new alias for the workspace. It does not need to be unique.</p> <p>Amazon Managed Service for Prometheus will automatically strip any blank spaces from the beginning and end of the alias that you specify.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Completing the request would cause a service quota to be exceeded.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.update_workspace_alias_request.UpdateWorkspaceAliasRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.update_workspace_alias

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.update_workspace_alias.async_update_workspace_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.update_workspace_alias_request.UpdateWorkspaceAliasRequest = {
            "workspace_id": workspace_id
        }
        if alias is not None:
            input_["alias"] = alias
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

    async def delete(
        self,
        workspace_id: "capo_amp.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        client_token: Optional[
            "capo_amp.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> None:
        """<p>Deletes an existing workspace. </p> <note> <p>When you delete a workspace, the data that has been ingested into it is not immediately deleted. It will be permanently deleted within one month.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace to delete.</p>
            client_token: <p>A unique identifier that you can provide to ensure the idempotency of the request. Case-sensitive.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.conflict_exception.ConflictException: <p>The request would cause an inconsistent state.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resources that doesn't exist.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.delete_workspace_request.DeleteWorkspaceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_amp._operations.amazon_prometheus_service.delete_workspace

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.delete_workspace.async_delete_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.delete_workspace_request.DeleteWorkspaceRequest = {
            "workspace_id": workspace_id
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

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncampClientConfig] = None,
        next_token: Optional["capo_amp.types.pagination_token.PaginationToken"] = None,
        alias: Optional["capo_amp.types.workspace_alias.WorkspaceAlias"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_amp.types.list_workspaces_response.ListWorkspacesResponse":
        """<p>Lists all of the Amazon Managed Service for Prometheus workspaces in your account. This includes workspaces being created or deleted. </p>

        Args:
            next_token: <p>The token for the next set of items to return. You receive this token from a previous call, and use it to get the next page of results. The other parameters must be the same as the initial call.</p> <p>For example, if your initial request has <code>maxResults</code> of 10, and there are 12 workspaces to return, then your initial request will return 10 and a <code>nextToken</code>. Using the next token in a subsequent call will return the remaining 2 workspaces.</p>
            alias: <p>If this is included, it filters the results to only the workspaces with names that start with the value that you specify here.</p> <p>Amazon Managed Service for Prometheus will automatically strip any blank spaces from the beginning and end of the alias that you specify.</p>
            max_results: <p>The maximum number of workspaces to return per request. The default is 100.</p>

        Raises:
            capo_amp.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_amp.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during the processing of the request.</p>
            capo_amp.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_amp.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_amp.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_amp.types.list_workspaces_request.ListWorkspacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_amp.types.list_workspaces_response.ListWorkspacesResponse"
        ]:
            import capo_amp._operations.amazon_prometheus_service.list_workspaces

            (
                output,
                http_response,
            ) = await capo_amp._operations.amazon_prometheus_service.list_workspaces.async_list_workspaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_amp.types.list_workspaces_request.ListWorkspacesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if alias is not None:
            input_["alias"] = alias
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
