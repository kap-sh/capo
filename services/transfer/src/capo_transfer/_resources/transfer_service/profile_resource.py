from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_transfer._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_transfer.types.as2_id
    import capo_transfer.types.certificate_ids
    import capo_transfer.types.create_profile_request
    import capo_transfer.types.create_profile_response
    import capo_transfer.types.delete_profile_request
    import capo_transfer.types.describe_profile_request
    import capo_transfer.types.describe_profile_response
    import capo_transfer.types.list_profiles_request
    import capo_transfer.types.list_profiles_response
    import capo_transfer.types.listed_profile
    import capo_transfer.types.max_results
    import capo_transfer.types.next_token
    import capo_transfer.types.profile_id
    import capo_transfer.types.profile_type
    import capo_transfer.types.tags
    import capo_transfer.types.update_profile_request
    import capo_transfer.types.update_profile_response
    from capo_transfer._services.async_transfer import (
        AsyncTransferClient,
        AsyncTransferClientConfig,
    )
    from capo_transfer._services.transfer import TransferClient, TransferClientConfig


class ProfileResource:
    def __init__(self, service: TransferClient) -> None:
        self._service = service

    def create(
        self,
        as2_id: "capo_transfer.types.as2_id.As2Id",
        profile_type: "capo_transfer.types.profile_type.ProfileType",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        certificate_ids: Optional[
            "capo_transfer.types.certificate_ids.CertificateIds"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
    ) -> "capo_transfer.types.create_profile_response.CreateProfileResponse":
        """<p>Creates the local or partner profile to use for AS2 transfers.</p>

        Args:
            as2_id: <p>The <code>As2Id</code> is the <i>AS2-name</i>, as defined in the <a href="https://datatracker.ietf.org/doc/html/rfc4130">RFC 4130</a>. For inbound transfers, this is the <code>AS2-From</code> header for the AS2 messages sent from the partner. For outbound connectors, this is the <code>AS2-To</code> header for the AS2 messages sent to the partner using the <code>StartFileTransfer</code> API operation. This ID cannot include spaces.</p>
            profile_type: <p>Determines the type of profile to create:</p> <ul> <li> <p>Specify <code>LOCAL</code> to create a local profile. A local profile represents the AS2-enabled Transfer Family server organization or party.</p> </li> <li> <p>Specify <code>PARTNER</code> to create a partner profile. A partner profile represents a remote organization, external to Transfer Family.</p> </li> </ul>
            certificate_ids: <p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>
            tags: <p>Key-value pairs that can be used to group and search for AS2 profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.create_profile_request.CreateProfileRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.create_profile_response.CreateProfileResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_profile

            output, http_response = (
                capo_transfer._operations.transfer_service.create_profile.create_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.create_profile_request.CreateProfileRequest = {
            "as2_id": as2_id,
            "profile_type": profile_type,
        }
        if certificate_ids is not None:
            input_["certificate_ids"] = certificate_ids
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
        profile_id: "capo_transfer.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_profile_response.DescribeProfileResponse":
        """<p>Returns the details of the profile that's specified by the <code>ProfileId</code>.</p>

        Args:
            profile_id: <p>The identifier of the profile that you want described.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.describe_profile_request.DescribeProfileRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.describe_profile_response.DescribeProfileResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_profile

            output, http_response = (
                capo_transfer._operations.transfer_service.describe_profile.describe_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.describe_profile_request.DescribeProfileRequest = {
            "profile_id": profile_id
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
        profile_id: "capo_transfer.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        certificate_ids: Optional[
            "capo_transfer.types.certificate_ids.CertificateIds"
        ] = None,
    ) -> "capo_transfer.types.update_profile_response.UpdateProfileResponse":
        """<p>Updates some of the parameters for an existing profile. Provide the <code>ProfileId</code> for the profile that you want to update, along with the new values for the parameters to update.</p>

        Args:
            profile_id: <p>The identifier of the profile object that you are updating.</p>
            certificate_ids: <p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.update_profile_request.UpdateProfileRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.update_profile_response.UpdateProfileResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_profile

            output, http_response = (
                capo_transfer._operations.transfer_service.update_profile.update_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.update_profile_request.UpdateProfileRequest = {
            "profile_id": profile_id
        }
        if certificate_ids is not None:
            input_["certificate_ids"] = certificate_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        profile_id: "capo_transfer.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the profile that's specified in the <code>ProfileId</code> parameter.</p>

        Args:
            profile_id: <p>The identifier of the profile that you are deleting.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.delete_profile_request.DeleteProfileRequest]",
        ) -> OperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_profile

            output, http_response = (
                capo_transfer._operations.transfer_service.delete_profile.delete_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.delete_profile_request.DeleteProfileRequest = {
            "profile_id": profile_id
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
        config_overrides: Optional[TransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
        profile_type: Optional["capo_transfer.types.profile_type.ProfileType"] = None,
    ) -> "capo_transfer.types.list_profiles_response.ListProfilesResponse":
        """<p>Returns a list of the profiles for your system. If you want to limit the results to a certain number, supply a value for the <code>MaxResults</code> parameter. If you ran the command previously and received a value for <code>NextToken</code>, you can supply that value to continue listing profiles from where you left off.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When there are additional results that were not returned, a <code>NextToken</code> parameter is returned. You can use that value for a subsequent call to <code>ListProfiles</code> to continue listing results.</p>
            profile_type: <p>Indicates whether to list only <code>LOCAL</code> type profiles or only <code>PARTNER</code> type profiles. If not supplied in the request, the command lists all types of profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.list_profiles_request.ListProfilesRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.list_profiles_response.ListProfilesResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_profiles

            output, http_response = (
                capo_transfer._operations.transfer_service.list_profiles.list_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.list_profiles_request.ListProfilesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if profile_type is not None:
            input_["profile_type"] = profile_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncProfileResource:
    def __init__(self, service: AsyncTransferClient) -> None:
        self._service = service

    async def create(
        self,
        as2_id: "capo_transfer.types.as2_id.As2Id",
        profile_type: "capo_transfer.types.profile_type.ProfileType",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        certificate_ids: Optional[
            "capo_transfer.types.certificate_ids.CertificateIds"
        ] = None,
        tags: Optional["capo_transfer.types.tags.Tags"] = None,
    ) -> "capo_transfer.types.create_profile_response.CreateProfileResponse":
        """<p>Creates the local or partner profile to use for AS2 transfers.</p>

        Args:
            as2_id: <p>The <code>As2Id</code> is the <i>AS2-name</i>, as defined in the <a href="https://datatracker.ietf.org/doc/html/rfc4130">RFC 4130</a>. For inbound transfers, this is the <code>AS2-From</code> header for the AS2 messages sent from the partner. For outbound connectors, this is the <code>AS2-To</code> header for the AS2 messages sent to the partner using the <code>StartFileTransfer</code> API operation. This ID cannot include spaces.</p>
            profile_type: <p>Determines the type of profile to create:</p> <ul> <li> <p>Specify <code>LOCAL</code> to create a local profile. A local profile represents the AS2-enabled Transfer Family server organization or party.</p> </li> <li> <p>Specify <code>PARTNER</code> to create a partner profile. A partner profile represents a remote organization, external to Transfer Family.</p> </li> </ul>
            certificate_ids: <p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>
            tags: <p>Key-value pairs that can be used to group and search for AS2 profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.create_profile_request.CreateProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.create_profile_response.CreateProfileResponse"
        ]:
            import capo_transfer._operations.transfer_service.create_profile

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.create_profile.async_create_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.create_profile_request.CreateProfileRequest = {
            "as2_id": as2_id,
            "profile_type": profile_type,
        }
        if certificate_ids is not None:
            input_["certificate_ids"] = certificate_ids
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
        profile_id: "capo_transfer.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_profile_response.DescribeProfileResponse":
        """<p>Returns the details of the profile that's specified by the <code>ProfileId</code>.</p>

        Args:
            profile_id: <p>The identifier of the profile that you want described.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_profile_request.DescribeProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_profile_response.DescribeProfileResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_profile

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_profile.async_describe_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.describe_profile_request.DescribeProfileRequest = {
            "profile_id": profile_id
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
        profile_id: "capo_transfer.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        certificate_ids: Optional[
            "capo_transfer.types.certificate_ids.CertificateIds"
        ] = None,
    ) -> "capo_transfer.types.update_profile_response.UpdateProfileResponse":
        """<p>Updates some of the parameters for an existing profile. Provide the <code>ProfileId</code> for the profile that you want to update, along with the new values for the parameters to update.</p>

        Args:
            profile_id: <p>The identifier of the profile object that you are updating.</p>
            certificate_ids: <p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_profile_request.UpdateProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_profile_response.UpdateProfileResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_profile

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_profile.async_update_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.update_profile_request.UpdateProfileRequest = {
            "profile_id": profile_id
        }
        if certificate_ids is not None:
            input_["certificate_ids"] = certificate_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        profile_id: "capo_transfer.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the profile that's specified in the <code>ProfileId</code> parameter.</p>

        Args:
            profile_id: <p>The identifier of the profile that you are deleting.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_profile_request.DeleteProfileRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_profile

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_profile.async_delete_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.delete_profile_request.DeleteProfileRequest = {
            "profile_id": profile_id
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
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["capo_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_transfer.types.next_token.NextToken"] = None,
        profile_type: Optional["capo_transfer.types.profile_type.ProfileType"] = None,
    ) -> "capo_transfer.types.list_profiles_response.ListProfilesResponse":
        """<p>Returns a list of the profiles for your system. If you want to limit the results to a certain number, supply a value for the <code>MaxResults</code> parameter. If you ran the command previously and received a value for <code>NextToken</code>, you can supply that value to continue listing profiles from where you left off.</p>

        Args:
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>When there are additional results that were not returned, a <code>NextToken</code> parameter is returned. You can use that value for a subsequent call to <code>ListProfiles</code> to continue listing results.</p>
            profile_type: <p>Indicates whether to list only <code>LOCAL</code> type profiles or only <code>PARTNER</code> type profiles. If not supplied in the request, the command lists all types of profiles.</p>

        Raises:
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> parameter that was passed is invalid.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed because the Amazon Web ServicesTransfer Family service is not available.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.list_profiles_request.ListProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.list_profiles_response.ListProfilesResponse"
        ]:
            import capo_transfer._operations.transfer_service.list_profiles

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.list_profiles.async_list_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_transfer.types.list_profiles_request.ListProfilesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if profile_type is not None:
            input_["profile_type"] = profile_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
