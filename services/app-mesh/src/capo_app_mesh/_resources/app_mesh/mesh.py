from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_app_mesh._auth._signers
import capo_app_mesh._auth._sigv4
from capo_app_mesh._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_app_mesh.types.account_id
    import capo_app_mesh.types.create_mesh_input
    import capo_app_mesh.types.create_mesh_output
    import capo_app_mesh.types.delete_mesh_input
    import capo_app_mesh.types.delete_mesh_output
    import capo_app_mesh.types.describe_mesh_input
    import capo_app_mesh.types.describe_mesh_output
    import capo_app_mesh.types.list_meshes_input
    import capo_app_mesh.types.list_meshes_limit
    import capo_app_mesh.types.list_meshes_output
    import capo_app_mesh.types.mesh_ref
    import capo_app_mesh.types.mesh_spec
    import capo_app_mesh.types.resource_name
    import capo_app_mesh.types.tag_list
    import capo_app_mesh.types.update_mesh_input
    import capo_app_mesh.types.update_mesh_output
    from capo_app_mesh._services.app_mesh import AppMeshClient, AppMeshClientConfig
    from capo_app_mesh._services.async_app_mesh import (
        AsyncAppMeshClient,
        AsyncAppMeshClientConfig,
    )


class Mesh:
    def __init__(self, service: AppMeshClient) -> None:
        self._service = service

    def put(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        spec: Optional["capo_app_mesh.types.mesh_spec.MeshSpec"] = None,
        tags: Optional["capo_app_mesh.types.tag_list.TagList"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_app_mesh.types.create_mesh_output.CreateMeshOutput":
        """<p>Creates a service mesh.</p> <p> A service mesh is a logical boundary for network traffic between services that are represented by resources within the mesh. After you create your service mesh, you can create virtual services, virtual nodes, virtual routers, and routes to distribute traffic between the applications in your mesh.</p> <p>For more information about service meshes, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html">Service meshes</a>.</p>

        Args:
            mesh_name: <p>The name to use for the service mesh.</p>
            spec: <p>The service mesh specification to apply.</p>
            tags: <p>Optional metadata that you can apply to the service mesh to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.create_mesh_input.CreateMeshInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.create_mesh_output.CreateMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.create_mesh

            output, http_response = (
                capo_app_mesh._operations.app_mesh.create_mesh.create_mesh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_app_mesh.types.create_mesh_input.CreateMeshInput = {
            "mesh_name": mesh_name
        }
        if spec is not None:
            input_["spec"] = spec
        if tags is not None:
            input_["tags"] = tags
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
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.describe_mesh_output.DescribeMeshOutput":
        """<p>Describes an existing service mesh.</p>

        Args:
            mesh_name: <p>The name of the service mesh to describe.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.describe_mesh_input.DescribeMeshInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.describe_mesh_output.DescribeMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.describe_mesh

            output, http_response = (
                capo_app_mesh._operations.app_mesh.describe_mesh.describe_mesh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_app_mesh.types.describe_mesh_input.DescribeMeshInput = {
            "mesh_name": mesh_name
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        spec: Optional["capo_app_mesh.types.mesh_spec.MeshSpec"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_app_mesh.types.update_mesh_output.UpdateMeshOutput":
        """<p>Updates an existing service mesh.</p>

        Args:
            mesh_name: <p>The name of the service mesh to update.</p>
            spec: <p>The service mesh specification to apply.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.update_mesh_input.UpdateMeshInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.update_mesh_output.UpdateMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.update_mesh

            output, http_response = (
                capo_app_mesh._operations.app_mesh.update_mesh.update_mesh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_app_mesh.types.update_mesh_input.UpdateMeshInput = {
            "mesh_name": mesh_name
        }
        if spec is not None:
            input_["spec"] = spec
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
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
    ) -> "capo_app_mesh.types.delete_mesh_output.DeleteMeshOutput":
        """<p>Deletes an existing service mesh.</p> <p>You must delete all resources (virtual services, routes, virtual routers, and virtual nodes) in the service mesh before you can delete the mesh itself.</p>

        Args:
            mesh_name: <p>The name of the service mesh to delete.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.resource_in_use_exception.ResourceInUseException: <p>You can't delete the specified resource because it's in use or required by another resource.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.delete_mesh_input.DeleteMeshInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.delete_mesh_output.DeleteMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.delete_mesh

            output, http_response = (
                capo_app_mesh._operations.app_mesh.delete_mesh.delete_mesh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_app_mesh.types.delete_mesh_input.DeleteMeshInput = {
            "mesh_name": mesh_name
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
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["capo_app_mesh.types.list_meshes_limit.ListMeshesLimit"] = None,
    ) -> "capo_app_mesh.types.list_meshes_output.ListMeshesOutput":
        """<p>Returns a list of existing service meshes.</p>

        Args:
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListMeshes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            limit: <p>The maximum number of results returned by <code>ListMeshes</code> in paginated output. When you use this parameter, <code>ListMeshes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListMeshes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListMeshes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.list_meshes_input.ListMeshesInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.list_meshes_output.ListMeshesOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_meshes

            output, http_response = (
                capo_app_mesh._operations.app_mesh.list_meshes.list_meshes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_meshes_input.ListMeshesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMesh:
    def __init__(self, service: AsyncAppMeshClient) -> None:
        self._service = service

    async def put(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
        spec: Optional["capo_app_mesh.types.mesh_spec.MeshSpec"] = None,
        tags: Optional["capo_app_mesh.types.tag_list.TagList"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_app_mesh.types.create_mesh_output.CreateMeshOutput":
        """<p>Creates a service mesh.</p> <p> A service mesh is a logical boundary for network traffic between services that are represented by resources within the mesh. After you create your service mesh, you can create virtual services, virtual nodes, virtual routers, and routes to distribute traffic between the applications in your mesh.</p> <p>For more information about service meshes, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html">Service meshes</a>.</p>

        Args:
            mesh_name: <p>The name to use for the service mesh.</p>
            spec: <p>The service mesh specification to apply.</p>
            tags: <p>Optional metadata that you can apply to the service mesh to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_app_mesh.types.create_mesh_input.CreateMeshInput]",
        ) -> AsyncOperationResponse[
            "capo_app_mesh.types.create_mesh_output.CreateMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.create_mesh

            (
                output,
                http_response,
            ) = await capo_app_mesh._operations.app_mesh.create_mesh.async_create_mesh(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_app_mesh.types.create_mesh_input.CreateMeshInput = {
            "mesh_name": mesh_name
        }
        if spec is not None:
            input_["spec"] = spec
        if tags is not None:
            input_["tags"] = tags
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
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.describe_mesh_output.DescribeMeshOutput":
        """<p>Describes an existing service mesh.</p>

        Args:
            mesh_name: <p>The name of the service mesh to describe.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_app_mesh.types.describe_mesh_input.DescribeMeshInput]",
        ) -> AsyncOperationResponse[
            "capo_app_mesh.types.describe_mesh_output.DescribeMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.describe_mesh

            (
                output,
                http_response,
            ) = await capo_app_mesh._operations.app_mesh.describe_mesh.async_describe_mesh(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_app_mesh.types.describe_mesh_input.DescribeMeshInput = {
            "mesh_name": mesh_name
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
        spec: Optional["capo_app_mesh.types.mesh_spec.MeshSpec"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_app_mesh.types.update_mesh_output.UpdateMeshOutput":
        """<p>Updates an existing service mesh.</p>

        Args:
            mesh_name: <p>The name of the service mesh to update.</p>
            spec: <p>The service mesh specification to apply.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_app_mesh.types.update_mesh_input.UpdateMeshInput]",
        ) -> AsyncOperationResponse[
            "capo_app_mesh.types.update_mesh_output.UpdateMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.update_mesh

            (
                output,
                http_response,
            ) = await capo_app_mesh._operations.app_mesh.update_mesh.async_update_mesh(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_app_mesh.types.update_mesh_input.UpdateMeshInput = {
            "mesh_name": mesh_name
        }
        if spec is not None:
            input_["spec"] = spec
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
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
    ) -> "capo_app_mesh.types.delete_mesh_output.DeleteMeshOutput":
        """<p>Deletes an existing service mesh.</p> <p>You must delete all resources (virtual services, routes, virtual routers, and virtual nodes) in the service mesh before you can delete the mesh itself.</p>

        Args:
            mesh_name: <p>The name of the service mesh to delete.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.resource_in_use_exception.ResourceInUseException: <p>You can't delete the specified resource because it's in use or required by another resource.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_app_mesh.types.delete_mesh_input.DeleteMeshInput]",
        ) -> AsyncOperationResponse[
            "capo_app_mesh.types.delete_mesh_output.DeleteMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.delete_mesh

            (
                output,
                http_response,
            ) = await capo_app_mesh._operations.app_mesh.delete_mesh.async_delete_mesh(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_app_mesh.types.delete_mesh_input.DeleteMeshInput = {
            "mesh_name": mesh_name
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
        config_overrides: Optional[AsyncAppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["capo_app_mesh.types.list_meshes_limit.ListMeshesLimit"] = None,
    ) -> "capo_app_mesh.types.list_meshes_output.ListMeshesOutput":
        """<p>Returns a list of existing service meshes.</p>

        Args:
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListMeshes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            limit: <p>The maximum number of results returned by <code>ListMeshes</code> in paginated output. When you use this parameter, <code>ListMeshes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListMeshes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListMeshes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_app_mesh.types.list_meshes_input.ListMeshesInput]",
        ) -> AsyncOperationResponse[
            "capo_app_mesh.types.list_meshes_output.ListMeshesOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_meshes

            (
                output,
                http_response,
            ) = await capo_app_mesh._operations.app_mesh.list_meshes.async_list_meshes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_meshes_input.ListMeshesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
