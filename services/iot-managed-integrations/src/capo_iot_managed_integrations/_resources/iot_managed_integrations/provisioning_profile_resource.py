from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
from capo_iot_managed_integrations._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.ca_certificate
    import capo_iot_managed_integrations.types.claim_certificate
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.create_provisioning_profile_request
    import capo_iot_managed_integrations.types.create_provisioning_profile_response
    import capo_iot_managed_integrations.types.delete_provisioning_profile_request
    import capo_iot_managed_integrations.types.get_provisioning_profile_request
    import capo_iot_managed_integrations.types.get_provisioning_profile_response
    import capo_iot_managed_integrations.types.list_provisioning_profiles_request
    import capo_iot_managed_integrations.types.list_provisioning_profiles_response
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.provisioning_profile_id
    import capo_iot_managed_integrations.types.provisioning_profile_name
    import capo_iot_managed_integrations.types.provisioning_profile_summary
    import capo_iot_managed_integrations.types.provisioning_type
    import capo_iot_managed_integrations.types.tags_map
    from capo_iot_managed_integrations._services.async_io_t_managed_integrations import (
        AsyncIoTManagedIntegrationsClient,
        AsyncIoTManagedIntegrationsClientConfig,
    )
    from capo_iot_managed_integrations._services.io_t_managed_integrations import (
        IoTManagedIntegrationsClient,
        IoTManagedIntegrationsClientConfig,
    )


class ProvisioningProfileResource:
    def __init__(self, service: IoTManagedIntegrationsClient) -> None:
        self._service = service

    def create(
        self,
        provisioning_type: "capo_iot_managed_integrations.types.provisioning_type.ProvisioningType",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        ca_certificate: Optional[
            "capo_iot_managed_integrations.types.ca_certificate.CaCertificate"
        ] = None,
        claim_certificate: Optional[
            "capo_iot_managed_integrations.types.claim_certificate.ClaimCertificate"
        ] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.provisioning_profile_name.ProvisioningProfileName"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse":
        """<p>Create a provisioning profile for executing device provisioning flows. The provisioning profile is a document that defines the set of resources and policies applied to a device during the provisioning process.</p>

        Args:
            provisioning_type: <p>The type of provisioning workflow the device uses for onboarding to IoT managed integrations.</p>
            ca_certificate: <p>The body of the PEM-encoded certificate authority (CA) certificate.</p>
            claim_certificate: <p>The body of the PEM-encoded claim certificate. If a claim certificate is provided, it will be used for the provisioning profile. Otherwise, a claim certificate will be generated.</p>
            name: <p>The name of the provisioning profile.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the provisioning profile.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_provisioning_profile

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.create_provisioning_profile.create_provisioning_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_provisioning_profile_request

            return capo_iot_managed_integrations.types.create_provisioning_profile_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_provisioning_profile_response

            return capo_iot_managed_integrations.types.create_provisioning_profile_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateProvisioningProfile",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest = {
            "provisioning_type": provisioning_type
        }
        if ca_certificate is not None:
            input_["ca_certificate"] = ca_certificate
        if claim_certificate is not None:
            input_["claim_certificate"] = claim_certificate
        if name is not None:
            input_["name"] = name
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        identifier: "capo_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse":
        """<p>Get details of a provisioning profile.</p>

        Args:
            identifier: <p>The id of a provisioning profile.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.get_provisioning_profile_request.GetProvisioningProfileRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_provisioning_profile

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.get_provisioning_profile.get_provisioning_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_provisioning_profile_response

            return capo_iot_managed_integrations.types.get_provisioning_profile_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetProvisioningProfile", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_provisioning_profile_request.GetProvisioningProfileRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        identifier: "capo_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId",
        *,
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a provisioning profile.</p>

        Args:
            identifier: <p>The id of the provisioning profile.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.delete_provisioning_profile_request.DeleteProvisioningProfileRequest]",
        ) -> OperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_provisioning_profile

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.delete_provisioning_profile.delete_provisioning_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteProvisioningProfile")
        )
        input_: capo_iot_managed_integrations.types.delete_provisioning_profile_request.DeleteProvisioningProfileRequest = {
            "identifier": identifier
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
        config_overrides: Optional[IoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_provisioning_profiles_response.ListProvisioningProfilesResponse":
        """<p>List the provisioning profiles within the Amazon Web Services account.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_iot_managed_integrations.types.list_provisioning_profiles_request.ListProvisioningProfilesRequest]",
        ) -> OperationResponse[
            "capo_iot_managed_integrations.types.list_provisioning_profiles_response.ListProvisioningProfilesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_provisioning_profiles

            output, http_response = (
                capo_iot_managed_integrations._operations.iot_managed_integrations.list_provisioning_profiles.list_provisioning_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListProvisioningProfiles")
        )
        input_: capo_iot_managed_integrations.types.list_provisioning_profiles_request.ListProvisioningProfilesRequest = {}
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


class AsyncProvisioningProfileResource:
    def __init__(self, service: AsyncIoTManagedIntegrationsClient) -> None:
        self._service = service

    async def create(
        self,
        provisioning_type: "capo_iot_managed_integrations.types.provisioning_type.ProvisioningType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        ca_certificate: Optional[
            "capo_iot_managed_integrations.types.ca_certificate.CaCertificate"
        ] = None,
        claim_certificate: Optional[
            "capo_iot_managed_integrations.types.claim_certificate.ClaimCertificate"
        ] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.provisioning_profile_name.ProvisioningProfileName"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse":
        """<p>Create a provisioning profile for executing device provisioning flows. The provisioning profile is a document that defines the set of resources and policies applied to a device during the provisioning process.</p>

        Args:
            provisioning_type: <p>The type of provisioning workflow the device uses for onboarding to IoT managed integrations.</p>
            ca_certificate: <p>The body of the PEM-encoded certificate authority (CA) certificate.</p>
            claim_certificate: <p>The body of the PEM-encoded claim certificate. If a claim certificate is provided, it will be used for the provisioning profile. Otherwise, a claim certificate will be generated.</p>
            name: <p>The name of the provisioning profile.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the provisioning profile.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_provisioning_profile

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_provisioning_profile.async_create_provisioning_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_provisioning_profile_request

            return capo_iot_managed_integrations.types.create_provisioning_profile_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.create_provisioning_profile_response

            return capo_iot_managed_integrations.types.create_provisioning_profile_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateProvisioningProfile",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest = {
            "provisioning_type": provisioning_type
        }
        if ca_certificate is not None:
            input_["ca_certificate"] = ca_certificate
        if claim_certificate is not None:
            input_["claim_certificate"] = claim_certificate
        if name is not None:
            input_["name"] = name
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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
        identifier: "capo_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse":
        """<p>Get details of a provisioning profile.</p>

        Args:
            identifier: <p>The id of a provisioning profile.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_provisioning_profile_request.GetProvisioningProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_provisioning_profile

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_provisioning_profile.async_get_provisioning_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse",
        ) -> dict[str, Any]:
            import capo_iot_managed_integrations.types.get_provisioning_profile_response

            return capo_iot_managed_integrations.types.get_provisioning_profile_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetProvisioningProfile", redact_output=_redact_output),
        )
        input_: capo_iot_managed_integrations.types.get_provisioning_profile_request.GetProvisioningProfileRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        identifier: "capo_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a provisioning profile.</p>

        Args:
            identifier: <p>The id of the provisioning profile.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_provisioning_profile_request.DeleteProvisioningProfileRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_provisioning_profile

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_provisioning_profile.async_delete_provisioning_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteProvisioningProfile")
        )
        input_: capo_iot_managed_integrations.types.delete_provisioning_profile_request.DeleteProvisioningProfileRequest = {
            "identifier": identifier
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
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_provisioning_profiles_response.ListProvisioningProfilesResponse":
        """<p>List the provisioning profiles within the Amazon Web Services account.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_provisioning_profiles_request.ListProvisioningProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_provisioning_profiles_response.ListProvisioningProfilesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_provisioning_profiles

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_provisioning_profiles.async_list_provisioning_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListProvisioningProfiles")
        )
        input_: capo_iot_managed_integrations.types.list_provisioning_profiles_request.ListProvisioningProfilesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
