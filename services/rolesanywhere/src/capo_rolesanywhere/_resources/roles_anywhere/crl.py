from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_rolesanywhere._auth._signers
import capo_rolesanywhere._auth._sigv4
from capo_rolesanywhere._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_rolesanywhere.types.crl_detail
    import capo_rolesanywhere.types.crl_detail_response
    import capo_rolesanywhere.types.import_crl_request
    import capo_rolesanywhere.types.list_crls_response
    import capo_rolesanywhere.types.list_request
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.scalar_crl_request
    import capo_rolesanywhere.types.tag_list
    import capo_rolesanywhere.types.trust_anchor_arn
    import capo_rolesanywhere.types.update_crl_request
    import capo_rolesanywhere.types.uuid
    from capo_rolesanywhere._services.async_roles_anywhere import (
        AsyncRolesAnywhereClient,
        AsyncRolesAnywhereClientConfig,
    )
    from capo_rolesanywhere._services.roles_anywhere import (
        RolesAnywhereClient,
        RolesAnywhereClientConfig,
    )


class Crl:
    def __init__(self, service: RolesAnywhereClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_rolesanywhere.types.resource_name.ResourceName",
        crl_data: bytes,
        trust_anchor_arn: "capo_rolesanywhere.types.trust_anchor_arn.TrustAnchorArn",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        enabled: Optional[bool] = None,
        tags: Optional["capo_rolesanywhere.types.tag_list.TagList"] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Imports the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate Authority (CA).In order to be properly imported, a CRL must be in PEM format. IAM Roles Anywhere validates against the CRL before issuing credentials. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:ImportCrl</code>. </p>

        Args:
            name: <p>The name of the certificate revocation list (CRL).</p>
            crl_data: <p>The x509 v3 specified certificate revocation list (CRL).</p>
            enabled: <p>Specifies whether the certificate revocation list (CRL) is enabled.</p>
            tags: <p>A list of tags to attach to the certificate revocation list (CRL).</p>
            trust_anchor_arn: <p>The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rolesanywhere.types.import_crl_request.ImportCrlRequest]",
        ) -> OperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.import_crl

            output, http_response = (
                capo_rolesanywhere._operations.roles_anywhere.import_crl.import_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_rolesanywhere.types.import_crl_request.ImportCrlRequest",
        ) -> dict[str, Any]:
            import capo_rolesanywhere.types.import_crl_request

            return capo_rolesanywhere.types.import_crl_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ImportCrl", redact_input=_redact_input)
        )
        input_: capo_rolesanywhere.types.import_crl_request.ImportCrlRequest = {
            "name": name,
            "crl_data": crl_data,
            "trust_anchor_arn": trust_anchor_arn,
        }
        if enabled is not None:
            input_["enabled"] = enabled
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
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Gets a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> OperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.get_crl

            output, http_response = (
                capo_rolesanywhere._operations.roles_anywhere.get_crl.get_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCrl")
        )
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
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
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        name: Optional["capo_rolesanywhere.types.resource_name.ResourceName"] = None,
        crl_data: Optional[bytes] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Updates the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate authority (CA). IAM Roles Anywhere validates against the CRL before issuing credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
            name: <p>The name of the Crl.</p>
            crl_data: <p>The x509 v3 specified certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rolesanywhere.types.update_crl_request.UpdateCrlRequest]",
        ) -> OperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.update_crl

            output, http_response = (
                capo_rolesanywhere._operations.roles_anywhere.update_crl.update_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCrl")
        )
        input_: capo_rolesanywhere.types.update_crl_request.UpdateCrlRequest = {
            "crl_id": crl_id
        }
        if name is not None:
            input_["name"] = name
        if crl_data is not None:
            input_["crl_data"] = crl_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Deletes a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> OperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.delete_crl

            output, http_response = (
                capo_rolesanywhere._operations.roles_anywhere.delete_crl.delete_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCrl")
        )
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
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
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "capo_rolesanywhere.types.list_crls_response.ListCrlsResponse":
        """<p>Lists all certificate revocation lists (CRL) in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListCrls</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rolesanywhere.types.list_request.ListRequest]",
        ) -> OperationResponse[
            "capo_rolesanywhere.types.list_crls_response.ListCrlsResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.list_crls

            output, http_response = (
                capo_rolesanywhere._operations.roles_anywhere.list_crls.list_crls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCrls")
        )
        input_: capo_rolesanywhere.types.list_request.ListRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_crl(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Disables a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> OperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.disable_crl

            output, http_response = (
                capo_rolesanywhere._operations.roles_anywhere.disable_crl.disable_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisableCrl")
        )
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def enable_crl(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Enables a certificate revocation list (CRL). When enabled, certificates stored in the CRL are unauthorized to receive session credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> OperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.enable_crl

            output, http_response = (
                capo_rolesanywhere._operations.roles_anywhere.enable_crl.enable_crl(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("EnableCrl")
        )
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCrl:
    def __init__(self, service: AsyncRolesAnywhereClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_rolesanywhere.types.resource_name.ResourceName",
        crl_data: bytes,
        trust_anchor_arn: "capo_rolesanywhere.types.trust_anchor_arn.TrustAnchorArn",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        enabled: Optional[bool] = None,
        tags: Optional["capo_rolesanywhere.types.tag_list.TagList"] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Imports the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate Authority (CA).In order to be properly imported, a CRL must be in PEM format. IAM Roles Anywhere validates against the CRL before issuing credentials. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:ImportCrl</code>. </p>

        Args:
            name: <p>The name of the certificate revocation list (CRL).</p>
            crl_data: <p>The x509 v3 specified certificate revocation list (CRL).</p>
            enabled: <p>Specifies whether the certificate revocation list (CRL) is enabled.</p>
            tags: <p>A list of tags to attach to the certificate revocation list (CRL).</p>
            trust_anchor_arn: <p>The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.import_crl_request.ImportCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.import_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.import_crl.async_import_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_rolesanywhere.types.import_crl_request.ImportCrlRequest",
        ) -> dict[str, Any]:
            import capo_rolesanywhere.types.import_crl_request

            return capo_rolesanywhere.types.import_crl_request.redact_sensitive(input_)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ImportCrl", redact_input=_redact_input)
        )
        input_: capo_rolesanywhere.types.import_crl_request.ImportCrlRequest = {
            "name": name,
            "crl_data": crl_data,
            "trust_anchor_arn": trust_anchor_arn,
        }
        if enabled is not None:
            input_["enabled"] = enabled
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
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Gets a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.get_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.get_crl.async_get_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCrl")
        )
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
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
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        name: Optional["capo_rolesanywhere.types.resource_name.ResourceName"] = None,
        crl_data: Optional[bytes] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Updates the certificate revocation list (CRL). A CRL is a list of certificates that have been revoked by the issuing certificate authority (CA). IAM Roles Anywhere validates against the CRL before issuing credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UpdateCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>
            name: <p>The name of the Crl.</p>
            crl_data: <p>The x509 v3 specified certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.update_crl_request.UpdateCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.update_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.update_crl.async_update_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCrl")
        )
        input_: capo_rolesanywhere.types.update_crl_request.UpdateCrlRequest = {
            "crl_id": crl_id
        }
        if name is not None:
            input_["name"] = name
        if crl_data is not None:
            input_["crl_data"] = crl_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Deletes a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DeleteCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.delete_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.delete_crl.async_delete_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCrl")
        )
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
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
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
        next_token: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> "capo_rolesanywhere.types.list_crls_response.ListCrlsResponse":
        """<p>Lists all certificate revocation lists (CRL) in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListCrls</code>. </p>

        Args:
            next_token: <p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>
            page_size: <p>The number of resources in the paginated list. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.validation_exception.ValidationException: <p>Validation exception error.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.list_request.ListRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.list_crls_response.ListCrlsResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.list_crls

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.list_crls.async_list_crls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCrls")
        )
        input_: capo_rolesanywhere.types.list_request.ListRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_crl(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Disables a certificate revocation list (CRL).</p> <p> <b>Required permissions: </b> <code>rolesanywhere:DisableCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.disable_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.disable_crl.async_disable_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisableCrl")
        )
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_crl(
        self,
        crl_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse":
        """<p>Enables a certificate revocation list (CRL). When enabled, certificates stored in the CRL are unauthorized to receive session credentials.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:EnableCrl</code>. </p>

        Args:
            crl_id: <p>The unique identifier of the certificate revocation list (CRL).</p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.crl_detail_response.CrlDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.enable_crl

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.enable_crl.async_enable_crl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("EnableCrl")
        )
        input_: capo_rolesanywhere.types.scalar_crl_request.ScalarCrlRequest = {
            "crl_id": crl_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
