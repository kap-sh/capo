from __future__ import annotations

from typing import TYPE_CHECKING, Optional

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
    import capo_rolesanywhere.types.list_request
    import capo_rolesanywhere.types.list_subjects_response
    import capo_rolesanywhere.types.scalar_subject_request
    import capo_rolesanywhere.types.subject_detail_response
    import capo_rolesanywhere.types.subject_summary
    import capo_rolesanywhere.types.uuid
    from capo_rolesanywhere._services.async_roles_anywhere import (
        AsyncRolesAnywhereClient,
        AsyncRolesAnywhereClientConfig,
    )
    from capo_rolesanywhere._services.roles_anywhere import (
        RolesAnywhereClient,
        RolesAnywhereClientConfig,
    )


class Subject:
    def __init__(self, service: RolesAnywhereClient) -> None:
        self._service = service

    def read(
        self,
        subject_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[RolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.subject_detail_response.SubjectDetailResponse":
        """<p>Gets a <i>subject</i>, which associates a certificate identity with authentication attempts. The subject stores auditing information such as the status of the last authentication attempt, the certificate data used in the attempt, and the last time the associated identity attempted authentication. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetSubject</code>. </p>

        Args:
            subject_id: <p>The unique identifier of the subject. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_rolesanywhere.types.scalar_subject_request.ScalarSubjectRequest]",
        ) -> OperationResponse[
            "capo_rolesanywhere.types.subject_detail_response.SubjectDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.get_subject

            output, http_response = (
                capo_rolesanywhere._operations.roles_anywhere.get_subject.get_subject(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSubject")
        )
        input_: capo_rolesanywhere.types.scalar_subject_request.ScalarSubjectRequest = {
            "subject_id": subject_id
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
    ) -> "capo_rolesanywhere.types.list_subjects_response.ListSubjectsResponse":
        """<p>Lists the subjects in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListSubjects</code>. </p>

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
            "capo_rolesanywhere.types.list_subjects_response.ListSubjectsResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.list_subjects

            output, http_response = (
                capo_rolesanywhere._operations.roles_anywhere.list_subjects.list_subjects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSubjects")
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


class AsyncSubject:
    def __init__(self, service: AsyncRolesAnywhereClient) -> None:
        self._service = service

    async def read(
        self,
        subject_id: "capo_rolesanywhere.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "capo_rolesanywhere.types.subject_detail_response.SubjectDetailResponse":
        """<p>Gets a <i>subject</i>, which associates a certificate identity with authentication attempts. The subject stores auditing information such as the status of the last authentication attempt, the certificate data used in the attempt, and the last time the associated identity attempted authentication. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:GetSubject</code>. </p>

        Args:
            subject_id: <p>The unique identifier of the subject. </p>

        Raises:
            capo_rolesanywhere.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_rolesanywhere.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_rolesanywhere.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rolesanywhere.types.scalar_subject_request.ScalarSubjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_rolesanywhere.types.subject_detail_response.SubjectDetailResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.get_subject

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.get_subject.async_get_subject(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSubject")
        )
        input_: capo_rolesanywhere.types.scalar_subject_request.ScalarSubjectRequest = {
            "subject_id": subject_id
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
    ) -> "capo_rolesanywhere.types.list_subjects_response.ListSubjectsResponse":
        """<p>Lists the subjects in the authenticated account and Amazon Web Services Region.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListSubjects</code>. </p>

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
            "capo_rolesanywhere.types.list_subjects_response.ListSubjectsResponse"
        ]:
            import capo_rolesanywhere._operations.roles_anywhere.list_subjects

            (
                output,
                http_response,
            ) = await capo_rolesanywhere._operations.roles_anywhere.list_subjects.async_list_subjects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSubjects")
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
