from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_location._auth._signers
import capo_location._auth._sigv4
from capo_location._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_location.types.api_key_filter
    import capo_location.types.api_key_restrictions
    import capo_location.types.create_key_request
    import capo_location.types.create_key_response
    import capo_location.types.delete_key_request
    import capo_location.types.delete_key_response
    import capo_location.types.describe_key_request
    import capo_location.types.describe_key_response
    import capo_location.types.list_keys_request
    import capo_location.types.list_keys_response
    import capo_location.types.list_keys_response_entry
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.tag_map
    import capo_location.types.timestamp
    import capo_location.types.token
    import capo_location.types.update_key_request
    import capo_location.types.update_key_response
    from capo_location._services.async_location import (
        AsyncLocationClient,
        AsyncLocationClientConfig,
    )
    from capo_location._services.location import LocationClient, LocationClientConfig


class ApiKeyResource:
    def __init__(self, service: LocationClient) -> None:
        self._service = service

    def put(
        self,
        key_name: "capo_location.types.resource_name.ResourceName",
        restrictions: "capo_location.types.api_key_restrictions.ApiKeyRestrictions",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        expire_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        no_expiry: Optional[bool] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.create_key_response.CreateKeyResponse":
        """<p>Creates an API key resource in your Amazon Web Services account, which lets you grant actions for Amazon Location resources to the API key bearer.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            key_name: <p>A custom name for the API key resource.</p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). </p> </li> <li> <p>Must be a unique API key name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExampleAPIKey</code>.</p> </li> </ul>
            restrictions: <p>The API key restrictions for the API key resource.</p>
            description: <p>An optional description for the API key resource.</p>
            expire_time: <p>The optional timestamp for when the API key resource will expire in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. One of <code>NoExpiry</code> or <code>ExpireTime</code> must be set.</p>
            no_expiry: <p>Optionally set to <code>true</code> to set no expiration time for the API key. One of <code>NoExpiry</code> or <code>ExpireTime</code> must be set.</p>
            tags: <p>Applies one or more tags to the map resource. A tag is a key-value pair that helps manage, identify, search, and filter your resources by labelling them.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.create_key_request.CreateKeyRequest]",
        ) -> OperationResponse[
            "capo_location.types.create_key_response.CreateKeyResponse"
        ]:
            import capo_location._operations.location_service.create_key

            output, http_response = (
                capo_location._operations.location_service.create_key.create_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.create_key_request.CreateKeyRequest = {
            "key_name": key_name,
            "restrictions": restrictions,
        }
        if description is not None:
            input_["description"] = description
        if expire_time is not None:
            input_["expire_time"] = expire_time
        if no_expiry is not None:
            input_["no_expiry"] = no_expiry
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        key_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.describe_key_response.DescribeKeyResponse":
        """<p>Retrieves the API key resource details.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            key_name: <p>The name of the API key resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.describe_key_request.DescribeKeyRequest]",
        ) -> OperationResponse[
            "capo_location.types.describe_key_response.DescribeKeyResponse"
        ]:
            import capo_location._operations.location_service.describe_key

            output, http_response = (
                capo_location._operations.location_service.describe_key.describe_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.describe_key_request.DescribeKeyRequest = {
            "key_name": key_name
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
        key_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        expire_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        no_expiry: Optional[bool] = None,
        force_update: Optional[bool] = None,
        restrictions: Optional[
            "capo_location.types.api_key_restrictions.ApiKeyRestrictions"
        ] = None,
    ) -> "capo_location.types.update_key_response.UpdateKeyResponse":
        """<p>Updates the specified properties of a given API key resource.</p>

        Args:
            key_name: <p>The name of the API key resource to update.</p>
            description: <p>Updates the description for the API key resource.</p>
            expire_time: <p>Updates the timestamp for when the API key resource will expire in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>
            no_expiry: <p>Whether the API key should expire. Set to <code>true</code> to set the API key to have no expiration time.</p>
            force_update: <p>The boolean flag to be included for updating <code>ExpireTime</code> or <code>Restrictions</code> details.</p> <p>Must be set to <code>true</code> to update an API key resource that has been used in the past 7 days.</p> <p> <code>False</code> if force update is not preferred</p> <p>Default value: <code>False</code> </p>
            restrictions: <p>Updates the API key restrictions for the API key resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.update_key_request.UpdateKeyRequest]",
        ) -> OperationResponse[
            "capo_location.types.update_key_response.UpdateKeyResponse"
        ]:
            import capo_location._operations.location_service.update_key

            output, http_response = (
                capo_location._operations.location_service.update_key.update_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.update_key_request.UpdateKeyRequest = {
            "key_name": key_name
        }
        if description is not None:
            input_["description"] = description
        if expire_time is not None:
            input_["expire_time"] = expire_time
        if no_expiry is not None:
            input_["no_expiry"] = no_expiry
        if force_update is not None:
            input_["force_update"] = force_update
        if restrictions is not None:
            input_["restrictions"] = restrictions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        key_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        force_delete: Optional[bool] = None,
    ) -> "capo_location.types.delete_key_response.DeleteKeyResponse":
        """<p>Deletes the specified API key. The API key must have been deactivated more than 90 days previously.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            key_name: <p>The name of the API key to delete.</p>
            force_delete: <p>ForceDelete bypasses an API key's expiry conditions and deletes the key. Set the parameter <code>true</code> to delete the key or to <code>false</code> to not preemptively delete the API key.</p> <p>Valid values: <code>true</code>, or <code>false</code>.</p> <p>Required: No</p> <note> <p>This action is irreversible. Only use ForceDelete if you are certain the key is no longer in use.</p> </note>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.delete_key_request.DeleteKeyRequest]",
        ) -> OperationResponse[
            "capo_location.types.delete_key_response.DeleteKeyResponse"
        ]:
            import capo_location._operations.location_service.delete_key

            output, http_response = (
                capo_location._operations.location_service.delete_key.delete_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.delete_key_request.DeleteKeyRequest = {
            "key_name": key_name
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete

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
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
        filter: Optional["capo_location.types.api_key_filter.ApiKeyFilter"] = None,
    ) -> "capo_location.types.list_keys_response.ListKeysResponse":
        """<p>Lists API key resources in your Amazon Web Services account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            max_results: <p>An optional limit for the number of resources returned in a single call. </p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>
            filter: <p>Optionally filter the list to only <code>Active</code> or <code>Expired</code> API keys.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_keys_request.ListKeysRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_keys_response.ListKeysResponse"
        ]:
            import capo_location._operations.location_service.list_keys

            output, http_response = (
                capo_location._operations.location_service.list_keys.list_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_keys_request.ListKeysRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncApiKeyResource:
    def __init__(self, service: AsyncLocationClient) -> None:
        self._service = service

    async def put(
        self,
        key_name: "capo_location.types.resource_name.ResourceName",
        restrictions: "capo_location.types.api_key_restrictions.ApiKeyRestrictions",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        expire_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        no_expiry: Optional[bool] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.create_key_response.CreateKeyResponse":
        """<p>Creates an API key resource in your Amazon Web Services account, which lets you grant actions for Amazon Location resources to the API key bearer.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            key_name: <p>A custom name for the API key resource.</p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). </p> </li> <li> <p>Must be a unique API key name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExampleAPIKey</code>.</p> </li> </ul>
            restrictions: <p>The API key restrictions for the API key resource.</p>
            description: <p>An optional description for the API key resource.</p>
            expire_time: <p>The optional timestamp for when the API key resource will expire in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. One of <code>NoExpiry</code> or <code>ExpireTime</code> must be set.</p>
            no_expiry: <p>Optionally set to <code>true</code> to set no expiration time for the API key. One of <code>NoExpiry</code> or <code>ExpireTime</code> must be set.</p>
            tags: <p>Applies one or more tags to the map resource. A tag is a key-value pair that helps manage, identify, search, and filter your resources by labelling them.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.create_key_request.CreateKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.create_key_response.CreateKeyResponse"
        ]:
            import capo_location._operations.location_service.create_key

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.create_key.async_create_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.create_key_request.CreateKeyRequest = {
            "key_name": key_name,
            "restrictions": restrictions,
        }
        if description is not None:
            input_["description"] = description
        if expire_time is not None:
            input_["expire_time"] = expire_time
        if no_expiry is not None:
            input_["no_expiry"] = no_expiry
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        key_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
    ) -> "capo_location.types.describe_key_response.DescribeKeyResponse":
        """<p>Retrieves the API key resource details.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            key_name: <p>The name of the API key resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.describe_key_request.DescribeKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.describe_key_response.DescribeKeyResponse"
        ]:
            import capo_location._operations.location_service.describe_key

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.describe_key.async_describe_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.describe_key_request.DescribeKeyRequest = {
            "key_name": key_name
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
        key_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        expire_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        no_expiry: Optional[bool] = None,
        force_update: Optional[bool] = None,
        restrictions: Optional[
            "capo_location.types.api_key_restrictions.ApiKeyRestrictions"
        ] = None,
    ) -> "capo_location.types.update_key_response.UpdateKeyResponse":
        """<p>Updates the specified properties of a given API key resource.</p>

        Args:
            key_name: <p>The name of the API key resource to update.</p>
            description: <p>Updates the description for the API key resource.</p>
            expire_time: <p>Updates the timestamp for when the API key resource will expire in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>
            no_expiry: <p>Whether the API key should expire. Set to <code>true</code> to set the API key to have no expiration time.</p>
            force_update: <p>The boolean flag to be included for updating <code>ExpireTime</code> or <code>Restrictions</code> details.</p> <p>Must be set to <code>true</code> to update an API key resource that has been used in the past 7 days.</p> <p> <code>False</code> if force update is not preferred</p> <p>Default value: <code>False</code> </p>
            restrictions: <p>Updates the API key restrictions for the API key resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.update_key_request.UpdateKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.update_key_response.UpdateKeyResponse"
        ]:
            import capo_location._operations.location_service.update_key

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.update_key.async_update_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.update_key_request.UpdateKeyRequest = {
            "key_name": key_name
        }
        if description is not None:
            input_["description"] = description
        if expire_time is not None:
            input_["expire_time"] = expire_time
        if no_expiry is not None:
            input_["no_expiry"] = no_expiry
        if force_update is not None:
            input_["force_update"] = force_update
        if restrictions is not None:
            input_["restrictions"] = restrictions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        key_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        force_delete: Optional[bool] = None,
    ) -> "capo_location.types.delete_key_response.DeleteKeyResponse":
        """<p>Deletes the specified API key. The API key must have been deactivated more than 90 days previously.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            key_name: <p>The name of the API key to delete.</p>
            force_delete: <p>ForceDelete bypasses an API key's expiry conditions and deletes the key. Set the parameter <code>true</code> to delete the key or to <code>false</code> to not preemptively delete the API key.</p> <p>Valid values: <code>true</code>, or <code>false</code>.</p> <p>Required: No</p> <note> <p>This action is irreversible. Only use ForceDelete if you are certain the key is no longer in use.</p> </note>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.delete_key_request.DeleteKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.delete_key_response.DeleteKeyResponse"
        ]:
            import capo_location._operations.location_service.delete_key

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.delete_key.async_delete_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.delete_key_request.DeleteKeyRequest = {
            "key_name": key_name
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete

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
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
        filter: Optional["capo_location.types.api_key_filter.ApiKeyFilter"] = None,
    ) -> "capo_location.types.list_keys_response.ListKeysResponse":
        """<p>Lists API key resources in your Amazon Web Services account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            max_results: <p>An optional limit for the number of resources returned in a single call. </p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>
            filter: <p>Optionally filter the list to only <code>Active</code> or <code>Expired</code> API keys.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.list_keys_request.ListKeysRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.list_keys_response.ListKeysResponse"
        ]:
            import capo_location._operations.location_service.list_keys

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.list_keys.async_list_keys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_keys_request.ListKeysRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
