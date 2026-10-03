"""Generated from Smithy shape ``com.amazonaws.mediastoredata#MediaStoreObject_20170901``."""

import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_mediastore_data._auth._signers
import capo_mediastore_data._auth._sigv4
from capo_mediastore_data._auth._identity import Credentials
from capo_mediastore_data._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mediastore_data._auth._zapros_handler import AuthMiddleware
from capo_mediastore_data._body import Body, closing_bodies
from capo_mediastore_data._iter import ensure_sync_iterator
from capo_mediastore_data._pagination import resolve_path as _resolve_path
from capo_mediastore_data._services._aws_config import aws_config
from capo_mediastore_data._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_mediastore_data.types.content_type
    import capo_mediastore_data.types.delete_object_request
    import capo_mediastore_data.types.delete_object_response
    import capo_mediastore_data.types.describe_object_request
    import capo_mediastore_data.types.describe_object_response
    import capo_mediastore_data.types.get_object_request
    import capo_mediastore_data.types.get_object_response
    import capo_mediastore_data.types.list_items_request
    import capo_mediastore_data.types.list_items_response
    import capo_mediastore_data.types.list_limit
    import capo_mediastore_data.types.list_path_naming
    import capo_mediastore_data.types.pagination_token
    import capo_mediastore_data.types.path_naming
    import capo_mediastore_data.types.payload_blob
    import capo_mediastore_data.types.put_object_request
    import capo_mediastore_data.types.put_object_response
    import capo_mediastore_data.types.range_pattern
    import capo_mediastore_data.types.storage_class
    import capo_mediastore_data.types.string_primitive
    import capo_mediastore_data.types.upload_availability


class MediaStoreDataClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class MediaStoreDataClient:
    """A client for the ``MediaStoreData`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = MediaStoreDataClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[MediaStoreDataClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MediaStoreDataClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def delete_object(
        self,
        path: "capo_mediastore_data.types.path_naming.PathNaming",
        *,
        config_overrides: Optional[MediaStoreDataClientConfig] = None,
    ) -> "capo_mediastore_data.types.delete_object_response.DeleteObjectResponse":
        """<p>Deletes an object at the specified path.</p>

        Args:
            path: <p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p>

        Raises:
            capo_mediastore_data.errors.container_not_found_exception.ContainerNotFoundException: <p>The specified container was not found for the specified account.</p>
            capo_mediastore_data.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore_data.errors.object_not_found_exception.ObjectNotFoundException: <p>Could not perform an operation on an object that does not exist.</p>
            capo_mediastore_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediastore_data.types.delete_object_request.DeleteObjectRequest]",
        ) -> OperationResponse[
            "capo_mediastore_data.types.delete_object_response.DeleteObjectResponse"
        ]:
            import capo_mediastore_data._operations.media_store_object_20170901.delete_object

            output, http_response = (
                capo_mediastore_data._operations.media_store_object_20170901.delete_object.delete_object(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore_data.types.delete_object_request.DeleteObjectRequest = {
            "path": path
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_object(
        self,
        path: "capo_mediastore_data.types.path_naming.PathNaming",
        *,
        config_overrides: Optional[MediaStoreDataClientConfig] = None,
    ) -> "capo_mediastore_data.types.describe_object_response.DescribeObjectResponse":
        """<p>Gets the headers for an object at the specified path.</p>

        Args:
            path: <p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p>

        Raises:
            capo_mediastore_data.errors.container_not_found_exception.ContainerNotFoundException: <p>The specified container was not found for the specified account.</p>
            capo_mediastore_data.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore_data.errors.object_not_found_exception.ObjectNotFoundException: <p>Could not perform an operation on an object that does not exist.</p>
            capo_mediastore_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediastore_data.types.describe_object_request.DescribeObjectRequest]",
        ) -> OperationResponse[
            "capo_mediastore_data.types.describe_object_response.DescribeObjectResponse"
        ]:
            import capo_mediastore_data._operations.media_store_object_20170901.describe_object

            output, http_response = (
                capo_mediastore_data._operations.media_store_object_20170901.describe_object.describe_object(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore_data.types.describe_object_request.DescribeObjectRequest = {
            "path": path
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def get_object(
        self,
        path: "capo_mediastore_data.types.path_naming.PathNaming",
        *,
        config_overrides: Optional[MediaStoreDataClientConfig] = None,
        range: Optional["capo_mediastore_data.types.range_pattern.RangePattern"] = None,
    ) -> "Generator[capo_mediastore_data.types.get_object_response.GetObjectResponse]":
        r"""<p>Downloads the object at the specified path. If the object’s upload availability is set to <code>streaming</code>, AWS Elemental MediaStore downloads the object even if it’s still uploading the object.</p>

        Args:
            path: <p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p> <p>For example, to upload the file <code>mlaw.avi</code> to the folder path <code>premium\canada</code> in the container <code>movies</code>, enter the path <code>premium/canada/mlaw.avi</code>.</p> <p>Do not include the container name in this path.</p> <p>If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing <code>premium/usa</code> subfolder. If you specify <code>premium/canada</code>, the service creates a <code>canada</code> subfolder in the <code>premium</code> folder. You then have two subfolders, <code>usa</code> and <code>canada</code>, in the <code>premium</code> folder. </p> <p>There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.</p> <p>For more information about folders and how they exist in a container, see the <a href="http://docs.aws.amazon.com/mediastore/latest/ug/">AWS Elemental MediaStore User Guide</a>.</p> <p>The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. </p>
            range: <p>The range bytes of an object to retrieve. For more information about the <code>Range</code> header, see <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35">http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35</a>. AWS Elemental MediaStore ignores this header for partially uploaded objects that have streaming upload availability.</p>

        Raises:
            capo_mediastore_data.errors.container_not_found_exception.ContainerNotFoundException: <p>The specified container was not found for the specified account.</p>
            capo_mediastore_data.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore_data.errors.object_not_found_exception.ObjectNotFoundException: <p>Could not perform an operation on an object that does not exist.</p>
            capo_mediastore_data.errors.requested_range_not_satisfiable_exception.RequestedRangeNotSatisfiableException: <p>The requested content range is not valid.</p>
            capo_mediastore_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediastore_data.types.get_object_request.GetObjectRequest]",
        ) -> OperationResponse[
            "capo_mediastore_data.types.get_object_response.GetObjectResponse"
        ]:
            import capo_mediastore_data._operations.media_store_object_20170901.get_object

            output, http_response = (
                capo_mediastore_data._operations.media_store_object_20170901.get_object.get_object(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore_data.types.get_object_request.GetObjectRequest = {
            "path": path
        }
        if range is not None:
            input_["range"] = range

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def list_items(
        self,
        *,
        config_overrides: Optional[MediaStoreDataClientConfig] = None,
        path: Optional[
            "capo_mediastore_data.types.list_path_naming.ListPathNaming"
        ] = None,
        max_results: Optional["capo_mediastore_data.types.list_limit.ListLimit"] = None,
        next_token: Optional[
            "capo_mediastore_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_mediastore_data.types.list_items_response.ListItemsResponse":
        """<p>Provides a list of metadata entries about folders and objects in the specified folder.</p>

        Args:
            path: <p>The path in the container from which to retrieve items. Format: <folder name>/<folder name>/<file name></p>
            max_results: <p>The maximum number of results to return per API request. For example, you submit a <code>ListItems</code> request with <code>MaxResults</code> set at 500. Although 2,000 items match your request, the service returns no more than the first 500 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) The service might return fewer results than the <code>MaxResults</code> value.</p> <p>If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 1,000 results per page.</p>
            next_token: <p>The token that identifies which batch of results that you want to see. For example, you submit a <code>ListItems</code> request with <code>MaxResults</code> set at 500. The service returns the first batch of results (up to 500) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListItems</code> request a second time and specify the <code>NextToken</code> value.</p> <p>Tokens expire after 15 minutes.</p>

        Raises:
            capo_mediastore_data.errors.container_not_found_exception.ContainerNotFoundException: <p>The specified container was not found for the specified account.</p>
            capo_mediastore_data.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediastore_data.types.list_items_request.ListItemsRequest]",
        ) -> OperationResponse[
            "capo_mediastore_data.types.list_items_response.ListItemsResponse"
        ]:
            import capo_mediastore_data._operations.media_store_object_20170901.list_items

            output, http_response = (
                capo_mediastore_data._operations.media_store_object_20170901.list_items.list_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore_data.types.list_items_request.ListItemsRequest = {}
        if path is not None:
            input_["path"] = path
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

    def iter_list_items(
        self,
        *,
        config_overrides: Optional[MediaStoreDataClientConfig] = None,
        path: Optional[
            "capo_mediastore_data.types.list_path_naming.ListPathNaming"
        ] = None,
        max_results: Optional["capo_mediastore_data.types.list_limit.ListLimit"] = None,
        next_token: Optional[
            "capo_mediastore_data.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_mediastore_data.types.list_items_response.ListItemsResponse]":
        _token = next_token
        while True:
            _response = self.list_items(
                config_overrides=config_overrides,
                path=path,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_object(
        self,
        body: Body[Iterator[bytes]] | Iterator[bytes] | bytes,
        path: "capo_mediastore_data.types.path_naming.PathNaming",
        *,
        config_overrides: Optional[MediaStoreDataClientConfig] = None,
        content_type: Optional[
            "capo_mediastore_data.types.content_type.ContentType"
        ] = None,
        cache_control: Optional[
            "capo_mediastore_data.types.string_primitive.StringPrimitive"
        ] = None,
        storage_class: Optional[
            "capo_mediastore_data.types.storage_class.StorageClass"
        ] = None,
        upload_availability: Optional[
            "capo_mediastore_data.types.upload_availability.UploadAvailability"
        ] = None,
    ) -> "capo_mediastore_data.types.put_object_response.PutObjectResponse":
        r"""<p>Uploads an object to the specified path. Object sizes are limited to 25 MB for standard upload availability and 10 MB for streaming upload availability.</p>

        Args:
            body: <p>The bytes to be stored. </p>
            path: <p>The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name></p> <p>For example, to upload the file <code>mlaw.avi</code> to the folder path <code>premium\canada</code> in the container <code>movies</code>, enter the path <code>premium/canada/mlaw.avi</code>.</p> <p>Do not include the container name in this path.</p> <p>If the path includes any folders that don't exist yet, the service creates them. For example, suppose you have an existing <code>premium/usa</code> subfolder. If you specify <code>premium/canada</code>, the service creates a <code>canada</code> subfolder in the <code>premium</code> folder. You then have two subfolders, <code>usa</code> and <code>canada</code>, in the <code>premium</code> folder. </p> <p>There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.</p> <p>For more information about folders and how they exist in a container, see the <a href="http://docs.aws.amazon.com/mediastore/latest/ug/">AWS Elemental MediaStore User Guide</a>.</p> <p>The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension. </p>
            content_type: <p>The content type of the object.</p>
            cache_control: <p>An optional <code>CacheControl</code> header that allows the caller to control the object's cache behavior. Headers can be passed in as specified in the HTTP at <a href="https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9">https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9</a>.</p> <p>Headers with a custom user-defined value are also accepted.</p>
            storage_class: <p>Indicates the storage class of a <code>Put</code> request. Defaults to high-performance temporal storage class, and objects are persisted into durable storage shortly after being received.</p>
            upload_availability: <p>Indicates the availability of an object while it is still uploading. If the value is set to <code>streaming</code>, the object is available for downloading after some initial buffering but before the object is uploaded completely. If the value is set to <code>standard</code>, the object is available for downloading only when it is uploaded completely. The default value for this header is <code>standard</code>.</p> <p>To use this header, you must also set the HTTP <code>Transfer-Encoding</code> header to <code>chunked</code>.</p>

        Raises:
            capo_mediastore_data.errors.container_not_found_exception.ContainerNotFoundException: <p>The specified container was not found for the specified account.</p>
            capo_mediastore_data.errors.internal_server_error.InternalServerError: <p>The service is temporarily unavailable.</p>
            capo_mediastore_data.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediastore_data.types.put_object_request.PutObjectRequest]",
        ) -> OperationResponse[
            "capo_mediastore_data.types.put_object_response.PutObjectResponse"
        ]:
            import capo_mediastore_data._operations.media_store_object_20170901.put_object

            output, http_response = (
                capo_mediastore_data._operations.media_store_object_20170901.put_object.put_object(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mediastore_data.types.put_object_request.PutObjectRequest = {
            "body": ensure_sync_iterator(body),
            "path": path,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if cache_control is not None:
            input_["cache_control"] = cache_control
        if storage_class is not None:
            input_["storage_class"] = storage_class
        if upload_availability is not None:
            input_["upload_availability"] = upload_availability

        with closing_bodies(input_):
            response = execute_pipeline(
                OperationRequest(input=input_, options=options_),
                handler=_handler,
                interceptors=list(interceptors_),
            )
            response.response.close()
            return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
