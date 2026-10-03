from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_s3tables._auth._signers
import capo_s3tables._auth._sigv4
from capo_s3tables._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_s3tables.types.create_namespace_request
    import capo_s3tables.types.create_namespace_response
    import capo_s3tables.types.delete_namespace_request
    import capo_s3tables.types.get_namespace_request
    import capo_s3tables.types.get_namespace_response
    import capo_s3tables.types.list_namespaces_limit
    import capo_s3tables.types.list_namespaces_request
    import capo_s3tables.types.list_namespaces_response
    import capo_s3tables.types.namespace_list
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.namespace_summary
    import capo_s3tables.types.next_token
    import capo_s3tables.types.table_bucket_arn
    from capo_s3tables._services.async_s3_tables import (
        AsyncS3TablesClient,
        AsyncS3TablesClientConfig,
    )
    from capo_s3tables._services.s3_tables import S3TablesClient, S3TablesClientConfig


class NamespaceResource:
    def __init__(self, service: S3TablesClient) -> None:
        self._service = service

    def create_namespace(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_list.NamespaceList",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.create_namespace_response.CreateNamespaceResponse":
        """<p>Creates a namespace. A namespace is a logical grouping of tables within your table bucket, which you can use to organize tables. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-create.html">Create a namespace</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:CreateNamespace</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket to create the namespace in.</p>
            namespace: <p>A name for the namespace.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.create_namespace_request.CreateNamespaceRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.create_namespace_response.CreateNamespaceResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.create_namespace

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.create_namespace.create_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.create_namespace_request.CreateNamespaceRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_namespace(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes a namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-delete.html">Delete a namespace</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteNamespace</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the namespace.</p>
            namespace: <p>The name of the namespace.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.delete_namespace_request.DeleteNamespaceRequest]",
        ) -> OperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_namespace

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.delete_namespace.delete_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_namespace_request.DeleteNamespaceRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_namespace(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_namespace_response.GetNamespaceResponse":
        """<p>Gets details about a namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace.html">Table namespaces</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetNamespace</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The name of the namespace.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.get_namespace_request.GetNamespaceRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.get_namespace_response.GetNamespaceResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_namespace

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.get_namespace.get_namespace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_namespace_request.GetNamespaceRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_namespaces(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[S3TablesClientConfig] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_namespaces: Optional[
            "capo_s3tables.types.list_namespaces_limit.ListNamespacesLimit"
        ] = None,
    ) -> "capo_s3tables.types.list_namespaces_response.ListNamespacesResponse":
        """<p>Lists the namespaces within a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace.html">Table namespaces</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListNamespaces</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            prefix: <p>The prefix of the namespaces.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_namespaces: <p>The maximum number of namespaces to return in the list.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_s3tables.types.list_namespaces_request.ListNamespacesRequest]",
        ) -> OperationResponse[
            "capo_s3tables.types.list_namespaces_response.ListNamespacesResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_namespaces

            output, http_response = (
                capo_s3tables._operations.s3_table_buckets.list_namespaces.list_namespaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.list_namespaces_request.ListNamespacesRequest = {
            "table_bucket_arn": table_bucket_arn
        }
        if prefix is not None:
            input_["prefix"] = prefix
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if max_namespaces is not None:
            input_["max_namespaces"] = max_namespaces

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncNamespaceResource:
    def __init__(self, service: AsyncS3TablesClient) -> None:
        self._service = service

    async def create_namespace(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_list.NamespaceList",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.create_namespace_response.CreateNamespaceResponse":
        """<p>Creates a namespace. A namespace is a logical grouping of tables within your table bucket, which you can use to organize tables. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-create.html">Create a namespace</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:CreateNamespace</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket to create the namespace in.</p>
            namespace: <p>A name for the namespace.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.create_namespace_request.CreateNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.create_namespace_response.CreateNamespaceResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.create_namespace

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.create_namespace.async_create_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.create_namespace_request.CreateNamespaceRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_namespace(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> None:
        """<p>Deletes a namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-delete.html">Delete a namespace</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:DeleteNamespace</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket associated with the namespace.</p>
            namespace: <p>The name of the namespace.</p>

        Raises:
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.delete_namespace_request.DeleteNamespaceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3tables._operations.s3_table_buckets.delete_namespace

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.delete_namespace.async_delete_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.delete_namespace_request.DeleteNamespaceRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_namespace(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        namespace: "capo_s3tables.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
    ) -> "capo_s3tables.types.get_namespace_response.GetNamespaceResponse":
        """<p>Gets details about a namespace. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace.html">Table namespaces</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:GetNamespace</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            namespace: <p>The name of the namespace.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.get_namespace_request.GetNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.get_namespace_response.GetNamespaceResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.get_namespace

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.get_namespace.async_get_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.get_namespace_request.GetNamespaceRequest = {
            "table_bucket_arn": table_bucket_arn,
            "namespace": namespace,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_namespaces(
        self,
        table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN",
        *,
        config_overrides: Optional[AsyncS3TablesClientConfig] = None,
        prefix: Optional[str] = None,
        continuation_token: Optional["capo_s3tables.types.next_token.NextToken"] = None,
        max_namespaces: Optional[
            "capo_s3tables.types.list_namespaces_limit.ListNamespacesLimit"
        ] = None,
    ) -> "capo_s3tables.types.list_namespaces_response.ListNamespacesResponse":
        """<p>Lists the namespaces within a table bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace.html">Table namespaces</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3tables:ListNamespaces</code> permission to use this operation. </p> </dd> </dl>

        Args:
            table_bucket_arn: <p>The Amazon Resource Name (ARN) of the table bucket.</p>
            prefix: <p>The prefix of the namespaces.</p>
            continuation_token: <p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on this bucket with a token. <code>ContinuationToken</code> is obfuscated and is not a real key. You can use this <code>ContinuationToken</code> for pagination of the list results.</p>
            max_namespaces: <p>The maximum number of namespaces to return in the list.</p>

        Raises:
            capo_s3tables.errors.access_denied_exception.AccessDeniedException: <p>The action cannot be performed because you do not have the required permission.</p>
            capo_s3tables.errors.bad_request_exception.BadRequestException: <p>The request is invalid or malformed.</p>
            capo_s3tables.errors.conflict_exception.ConflictException: <p>The request failed because there is a conflict with a previous write. You can retry the request.</p>
            capo_s3tables.errors.forbidden_exception.ForbiddenException: <p>The caller isn't authorized to make the request.</p>
            capo_s3tables.errors.internal_server_error_exception.InternalServerErrorException: <p>The request failed due to an internal server error.</p>
            capo_s3tables.errors.not_found_exception.NotFoundException: <p>The request was rejected because the specified resource could not be found.</p>
            capo_s3tables.errors.too_many_requests_exception.TooManyRequestsException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_s3tables.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3tables.types.list_namespaces_request.ListNamespacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3tables.types.list_namespaces_response.ListNamespacesResponse"
        ]:
            import capo_s3tables._operations.s3_table_buckets.list_namespaces

            (
                output,
                http_response,
            ) = await capo_s3tables._operations.s3_table_buckets.list_namespaces.async_list_namespaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_s3tables.types.list_namespaces_request.ListNamespacesRequest = {
            "table_bucket_arn": table_bucket_arn
        }
        if prefix is not None:
            input_["prefix"] = prefix
        if continuation_token is not None:
            input_["continuation_token"] = continuation_token
        if max_namespaces is not None:
            input_["max_namespaces"] = max_namespaces

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
