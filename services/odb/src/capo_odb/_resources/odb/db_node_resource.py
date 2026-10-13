from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_odb._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_odb.types.db_node_summary
    import capo_odb.types.get_db_node_input
    import capo_odb.types.get_db_node_output
    import capo_odb.types.list_db_nodes_input
    import capo_odb.types.list_db_nodes_output
    import capo_odb.types.reboot_db_node_input
    import capo_odb.types.reboot_db_node_output
    import capo_odb.types.resource_id
    import capo_odb.types.start_db_node_input
    import capo_odb.types.start_db_node_output
    import capo_odb.types.stop_db_node_input
    import capo_odb.types.stop_db_node_output
    from capo_odb._services.async_odb import AsyncodbClient, AsyncodbClientConfig
    from capo_odb._services.odb import odbClient, odbClientConfig


class DbNodeResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service

    def read(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.get_db_node_output.GetDbNodeOutput":
        """<p>Returns information about the specified DB node.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.get_db_node_input.GetDbNodeInput]",
        ) -> OperationResponse["capo_odb.types.get_db_node_output.GetDbNodeOutput"]:
            import capo_odb._operations.odb.get_db_node

            output, http_response = capo_odb._operations.odb.get_db_node.get_db_node(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDbNode")
        )
        input_: capo_odb.types.get_db_node_input.GetDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

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
        config_overrides: Optional[odbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.list_db_nodes_output.ListDbNodesOutput":
        """<p>Returns information about the DB nodes for the specified VM cluster.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.list_db_nodes_input.ListDbNodesInput]",
        ) -> OperationResponse["capo_odb.types.list_db_nodes_output.ListDbNodesOutput"]:
            import capo_odb._operations.odb.list_db_nodes

            output, http_response = (
                capo_odb._operations.odb.list_db_nodes.list_db_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDbNodes")
        )
        input_: capo_odb.types.list_db_nodes_input.ListDbNodesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reboot_db_node(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.reboot_db_node_output.RebootDbNodeOutput":
        """<p>Reboots the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to reboot. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node to reboot. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to reboot.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.reboot_db_node_input.RebootDbNodeInput]",
        ) -> OperationResponse[
            "capo_odb.types.reboot_db_node_output.RebootDbNodeOutput"
        ]:
            import capo_odb._operations.odb.reboot_db_node

            output, http_response = (
                capo_odb._operations.odb.reboot_db_node.reboot_db_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RebootDbNode")
        )
        input_: capo_odb.types.reboot_db_node_input.RebootDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_db_node(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.start_db_node_output.StartDbNodeOutput":
        """<p>Starts the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to start. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node to start. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to start.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.start_db_node_input.StartDbNodeInput]",
        ) -> OperationResponse["capo_odb.types.start_db_node_output.StartDbNodeOutput"]:
            import capo_odb._operations.odb.start_db_node

            output, http_response = (
                capo_odb._operations.odb.start_db_node.start_db_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartDbNode")
        )
        input_: capo_odb.types.start_db_node_input.StartDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_db_node(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[odbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.stop_db_node_output.StopDbNodeOutput":
        """<p>Stops the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to stop. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node to stop. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to stop.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_odb.types.stop_db_node_input.StopDbNodeInput]",
        ) -> OperationResponse["capo_odb.types.stop_db_node_output.StopDbNodeOutput"]:
            import capo_odb._operations.odb.stop_db_node

            output, http_response = capo_odb._operations.odb.stop_db_node.stop_db_node(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopDbNode")
        )
        input_: capo_odb.types.stop_db_node_input.StopDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDbNodeResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service

    async def read(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.get_db_node_output.GetDbNodeOutput":
        """<p>Returns information about the specified DB node.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_db_node_input.GetDbNodeInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_db_node_output.GetDbNodeOutput"
        ]:
            import capo_odb._operations.odb.get_db_node

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_db_node.async_get_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDbNode")
        )
        input_: capo_odb.types.get_db_node_input.GetDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

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
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.list_db_nodes_output.ListDbNodesOutput":
        """<p>Returns information about the DB nodes for the specified VM cluster.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_db_nodes_input.ListDbNodesInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_db_nodes_output.ListDbNodesOutput"
        ]:
            import capo_odb._operations.odb.list_db_nodes

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_db_nodes.async_list_db_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDbNodes")
        )
        input_: capo_odb.types.list_db_nodes_input.ListDbNodesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reboot_db_node(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.reboot_db_node_output.RebootDbNodeOutput":
        """<p>Reboots the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to reboot. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node to reboot. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to reboot.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.reboot_db_node_input.RebootDbNodeInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.reboot_db_node_output.RebootDbNodeOutput"
        ]:
            import capo_odb._operations.odb.reboot_db_node

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.reboot_db_node.async_reboot_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RebootDbNode")
        )
        input_: capo_odb.types.reboot_db_node_input.RebootDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_db_node(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.start_db_node_output.StartDbNodeOutput":
        """<p>Starts the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to start. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node to start. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to start.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.start_db_node_input.StartDbNodeInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.start_db_node_output.StartDbNodeOutput"
        ]:
            import capo_odb._operations.odb.start_db_node

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.start_db_node.async_start_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartDbNode")
        )
        input_: capo_odb.types.start_db_node_input.StartDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_db_node(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.stop_db_node_output.StopDbNodeOutput":
        """<p>Stops the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to stop. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node to stop. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to stop.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.stop_db_node_input.StopDbNodeInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.stop_db_node_output.StopDbNodeOutput"
        ]:
            import capo_odb._operations.odb.stop_db_node

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.stop_db_node.async_stop_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopDbNode")
        )
        input_: capo_odb.types.stop_db_node_input.StopDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
