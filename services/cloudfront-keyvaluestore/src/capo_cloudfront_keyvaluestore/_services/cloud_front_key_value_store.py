"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#CloudFrontKeyValueStore``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_cloudfront_keyvaluestore._auth._signers
import capo_cloudfront_keyvaluestore._auth._sigv4
from capo_cloudfront_keyvaluestore._auth._identity import Credentials
from capo_cloudfront_keyvaluestore._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloudfront_keyvaluestore._auth._zapros_handler import AuthMiddleware
from capo_cloudfront_keyvaluestore._pagination import resolve_path as _resolve_path
from capo_cloudfront_keyvaluestore._services._aws_config import aws_config
from capo_cloudfront_keyvaluestore._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.delete_key_request
    import capo_cloudfront_keyvaluestore.types.delete_key_requests_list
    import capo_cloudfront_keyvaluestore.types.delete_key_response
    import capo_cloudfront_keyvaluestore.types.describe_key_value_store_request
    import capo_cloudfront_keyvaluestore.types.describe_key_value_store_response
    import capo_cloudfront_keyvaluestore.types.etag
    import capo_cloudfront_keyvaluestore.types.get_key_request
    import capo_cloudfront_keyvaluestore.types.get_key_response
    import capo_cloudfront_keyvaluestore.types.key
    import capo_cloudfront_keyvaluestore.types.kvs_arn
    import capo_cloudfront_keyvaluestore.types.list_keys_request
    import capo_cloudfront_keyvaluestore.types.list_keys_response
    import capo_cloudfront_keyvaluestore.types.list_keys_response_list_item
    import capo_cloudfront_keyvaluestore.types.put_key_request
    import capo_cloudfront_keyvaluestore.types.put_key_requests_list
    import capo_cloudfront_keyvaluestore.types.put_key_response
    import capo_cloudfront_keyvaluestore.types.update_keys_request
    import capo_cloudfront_keyvaluestore.types.update_keys_response
    import capo_cloudfront_keyvaluestore.types.value


class CloudFrontKeyValueStoreClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class CloudFrontKeyValueStoreClient:
    """A client for the ``CloudFrontKeyValueStore`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = CloudFrontKeyValueStoreClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[CloudFrontKeyValueStoreClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CloudFrontKeyValueStoreClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def delete_key(
        self,
        kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN",
        key: "capo_cloudfront_keyvaluestore.types.key.Key",
        if_match: "capo_cloudfront_keyvaluestore.types.etag.Etag",
        *,
        config_overrides: Optional[CloudFrontKeyValueStoreClientConfig] = None,
    ) -> "capo_cloudfront_keyvaluestore.types.delete_key_response.DeleteKeyResponse":
        """<p>Deletes the key value pair specified by the key.</p>

        Args:
            kvs_arn: <p>The Amazon Resource Name (ARN) of the Key Value Store.</p>
            key: <p>The key to delete.</p>
            if_match: <p>The current version (ETag) of the Key Value Store that you are deleting keys from, which you can get using DescribeKeyValueStore.</p>

        Raises:
            capo_cloudfront_keyvaluestore.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_cloudfront_keyvaluestore.errors.conflict_exception.ConflictException: <p>Resource is not in expected state.</p>
            capo_cloudfront_keyvaluestore.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_cloudfront_keyvaluestore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_cloudfront_keyvaluestore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Limit exceeded.</p>
            capo_cloudfront_keyvaluestore.errors.validation_exception.ValidationException: <p>Validation failed.</p>
            capo_cloudfront_keyvaluestore.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete 'key1' from the key value store with ARN 'arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58'

            >>> client.delete_key(key='key1', kvs_arn='arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58', if_match='KV0AB12C3DEF456')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront_keyvaluestore.types.delete_key_request.DeleteKeyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront_keyvaluestore.types.delete_key_response.DeleteKeyResponse"
        ]:
            import capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.delete_key

            output, http_response = (
                capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.delete_key.delete_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront_keyvaluestore.types.delete_key_request.DeleteKeyRequest = {
            "kvs_arn": kvs_arn,
            "key": key,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_key_value_store(
        self,
        kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN",
        *,
        config_overrides: Optional[CloudFrontKeyValueStoreClientConfig] = None,
    ) -> "capo_cloudfront_keyvaluestore.types.describe_key_value_store_response.DescribeKeyValueStoreResponse":
        """<p>Returns metadata information about Key Value Store.</p>

        Args:
            kvs_arn: <p>The Amazon Resource Name (ARN) of the Key Value Store.</p>

        Raises:
            capo_cloudfront_keyvaluestore.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_cloudfront_keyvaluestore.errors.conflict_exception.ConflictException: <p>Resource is not in expected state.</p>
            capo_cloudfront_keyvaluestore.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_cloudfront_keyvaluestore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_cloudfront_keyvaluestore.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe the key value store with ARN 'arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58'

            >>> client.describe_key_value_store(kvs_arn='arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58')
            Describe the key value store with ARN 'arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-1234a9d35678'

            >>> client.describe_key_value_store(kvs_arn='arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-1234a9d35678')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront_keyvaluestore.types.describe_key_value_store_request.DescribeKeyValueStoreRequest]",
        ) -> OperationResponse[
            "capo_cloudfront_keyvaluestore.types.describe_key_value_store_response.DescribeKeyValueStoreResponse"
        ]:
            import capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.describe_key_value_store

            output, http_response = (
                capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.describe_key_value_store.describe_key_value_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront_keyvaluestore.types.describe_key_value_store_request.DescribeKeyValueStoreRequest = {
            "kvs_arn": kvs_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_key(
        self,
        kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN",
        key: "capo_cloudfront_keyvaluestore.types.key.Key",
        *,
        config_overrides: Optional[CloudFrontKeyValueStoreClientConfig] = None,
    ) -> "capo_cloudfront_keyvaluestore.types.get_key_response.GetKeyResponse":
        """<p>Returns a key value pair.</p>

        Args:
            kvs_arn: <p>The Amazon Resource Name (ARN) of the Key Value Store.</p>
            key: <p>The key to get.</p>

        Raises:
            capo_cloudfront_keyvaluestore.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_cloudfront_keyvaluestore.errors.conflict_exception.ConflictException: <p>Resource is not in expected state.</p>
            capo_cloudfront_keyvaluestore.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_cloudfront_keyvaluestore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_cloudfront_keyvaluestore.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get 'key1' from the key value store with ARN 'arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58'

            >>> client.get_key(key='key1', kvs_arn='arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront_keyvaluestore.types.get_key_request.GetKeyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront_keyvaluestore.types.get_key_response.GetKeyResponse"
        ]:
            import capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.get_key

            output, http_response = (
                capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.get_key.get_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront_keyvaluestore.types.get_key_request.GetKeyRequest = {
            "kvs_arn": kvs_arn,
            "key": key,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_keys(
        self,
        kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN",
        *,
        config_overrides: Optional[CloudFrontKeyValueStoreClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_cloudfront_keyvaluestore.types.list_keys_response.ListKeysResponse":
        """<p>Returns a list of key value pairs.</p>

        Args:
            kvs_arn: <p>The Amazon Resource Name (ARN) of the Key Value Store.</p>
            next_token: <p>If nextToken is returned in the response, there are more results available. Make the next call using the returned token to retrieve the next page.</p>
            max_results: <p>Maximum number of results that are returned per call. The default is 10 and maximum allowed page is 50.</p>

        Raises:
            capo_cloudfront_keyvaluestore.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_cloudfront_keyvaluestore.errors.conflict_exception.ConflictException: <p>Resource is not in expected state.</p>
            capo_cloudfront_keyvaluestore.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_cloudfront_keyvaluestore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_cloudfront_keyvaluestore.errors.validation_exception.ValidationException: <p>Validation failed.</p>
            capo_cloudfront_keyvaluestore.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List keys in the key value store with ARN 'arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58'

            >>> client.list_keys(kvs_arn='arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58', max_results=3)
            List the next page in the key value store with ARN 'arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58'

            >>> client.list_keys(kvs_arn='arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58', max_results=3, next_token='hVTTZndkpBZ0VRZ0R1RF')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront_keyvaluestore.types.list_keys_request.ListKeysRequest]",
        ) -> OperationResponse[
            "capo_cloudfront_keyvaluestore.types.list_keys_response.ListKeysResponse"
        ]:
            import capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.list_keys

            output, http_response = (
                capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.list_keys.list_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront_keyvaluestore.types.list_keys_request.ListKeysRequest = {
            "kvs_arn": kvs_arn
        }
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

    def iter_list_keys(
        self,
        kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN",
        *,
        config_overrides: Optional[CloudFrontKeyValueStoreClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_cloudfront_keyvaluestore.types.list_keys_response_list_item.ListKeysResponseListItem]":
        _token = next_token
        while True:
            _response = self.list_keys(
                kvs_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_key(
        self,
        key: "capo_cloudfront_keyvaluestore.types.key.Key",
        value: "capo_cloudfront_keyvaluestore.types.value.Value",
        kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN",
        if_match: "capo_cloudfront_keyvaluestore.types.etag.Etag",
        *,
        config_overrides: Optional[CloudFrontKeyValueStoreClientConfig] = None,
    ) -> "capo_cloudfront_keyvaluestore.types.put_key_response.PutKeyResponse":
        """<p>Creates a new key value pair or replaces the value of an existing key.</p>

        Args:
            key: <p>The key to put.</p>
            value: <p>The value to put.</p>
            kvs_arn: <p>The Amazon Resource Name (ARN) of the Key Value Store.</p>
            if_match: <p>The current version (ETag) of the Key Value Store that you are putting keys into, which you can get using DescribeKeyValueStore.</p>

        Raises:
            capo_cloudfront_keyvaluestore.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_cloudfront_keyvaluestore.errors.conflict_exception.ConflictException: <p>Resource is not in expected state.</p>
            capo_cloudfront_keyvaluestore.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_cloudfront_keyvaluestore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_cloudfront_keyvaluestore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Limit exceeded.</p>
            capo_cloudfront_keyvaluestore.errors.validation_exception.ValidationException: <p>Validation failed.</p>
            capo_cloudfront_keyvaluestore.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Put 'key1' with 'value1' into the key value store with ARN 'arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58'

            >>> client.put_key(key='key1', value='value1', kvs_arn='arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58', if_match='KV0AB12C3DEF456')
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront_keyvaluestore.types.put_key_request.PutKeyRequest]",
        ) -> OperationResponse[
            "capo_cloudfront_keyvaluestore.types.put_key_response.PutKeyResponse"
        ]:
            import capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.put_key

            output, http_response = (
                capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.put_key.put_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront_keyvaluestore.types.put_key_request.PutKeyRequest = {
            "key": key,
            "value": value,
            "kvs_arn": kvs_arn,
            "if_match": if_match,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_keys(
        self,
        kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN",
        if_match: "capo_cloudfront_keyvaluestore.types.etag.Etag",
        *,
        config_overrides: Optional[CloudFrontKeyValueStoreClientConfig] = None,
        puts: Optional[
            "capo_cloudfront_keyvaluestore.types.put_key_requests_list.PutKeyRequestsList"
        ] = None,
        deletes: Optional[
            "capo_cloudfront_keyvaluestore.types.delete_key_requests_list.DeleteKeyRequestsList"
        ] = None,
    ) -> "capo_cloudfront_keyvaluestore.types.update_keys_response.UpdateKeysResponse":
        """<p>Puts or Deletes multiple key value pairs in a single, all-or-nothing operation.</p>

        Args:
            kvs_arn: <p>The Amazon Resource Name (ARN) of the Key Value Store.</p>
            if_match: <p>The current version (ETag) of the Key Value Store that you are updating keys of, which you can get using DescribeKeyValueStore.</p>
            puts: <p>List of key value pairs to put.</p>
            deletes: <p>List of keys to delete.</p>

        Raises:
            capo_cloudfront_keyvaluestore.errors.access_denied_exception.AccessDeniedException: <p>Access denied.</p>
            capo_cloudfront_keyvaluestore.errors.conflict_exception.ConflictException: <p>Resource is not in expected state.</p>
            capo_cloudfront_keyvaluestore.errors.internal_server_exception.InternalServerException: <p>Internal server error.</p>
            capo_cloudfront_keyvaluestore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource was not found.</p>
            capo_cloudfront_keyvaluestore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Limit exceeded.</p>
            capo_cloudfront_keyvaluestore.errors.validation_exception.ValidationException: <p>Validation failed.</p>
            capo_cloudfront_keyvaluestore.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Put 2 keys into the key value store with ARN 'arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58'

            >>> client.update_keys(kvs_arn='arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58', if_match='KV0AB12C3DEF456', puts=[{'Key': 'key1', 'Value': 'value1'}, {'Key': 'key2', 'Value': 'value2'}])
            Delete 2 keys from the key value store with ARN 'arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58'

            >>> client.update_keys(kvs_arn='arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58', if_match='KV0AB12C3DEF456', deletes=[{'Key': 'key1'}, {'Key': 'key2'}])
            Put 2 keys into and delete 1 key from the key value store with ARN 'arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58'

            >>> client.update_keys(kvs_arn='arn:aws:cloudfront::123456789012:key-value-store/327284aa-bcd5-499f-a3ff-26b9a9d31b58', if_match='KV0AB12C3DEF456', puts=[{'Key': 'key1', 'Value': 'value1'}, {'Key': 'key2', 'Value': 'value2'}], deletes=[{'Key': 'key3'}, {'Key': 'key4'}])
        """

        def _handler(
            req: "OperationRequest[capo_cloudfront_keyvaluestore.types.update_keys_request.UpdateKeysRequest]",
        ) -> OperationResponse[
            "capo_cloudfront_keyvaluestore.types.update_keys_response.UpdateKeysResponse"
        ]:
            import capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.update_keys

            output, http_response = (
                capo_cloudfront_keyvaluestore._operations.cloud_front_key_value_store.update_keys.update_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudfront_keyvaluestore.types.update_keys_request.UpdateKeysRequest = {
            "kvs_arn": kvs_arn,
            "if_match": if_match,
        }
        if puts is not None:
            input_["puts"] = puts
        if deletes is not None:
            input_["deletes"] = deletes

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
