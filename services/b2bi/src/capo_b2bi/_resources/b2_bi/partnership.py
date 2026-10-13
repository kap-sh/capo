from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

from capo_b2bi._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_b2bi.types.capability_options
    import capo_b2bi.types.create_partnership_request
    import capo_b2bi.types.create_partnership_response
    import capo_b2bi.types.delete_partnership_request
    import capo_b2bi.types.email
    import capo_b2bi.types.get_partnership_request
    import capo_b2bi.types.get_partnership_response
    import capo_b2bi.types.list_partnerships_request
    import capo_b2bi.types.list_partnerships_response
    import capo_b2bi.types.max_results
    import capo_b2bi.types.page_token
    import capo_b2bi.types.partner_name
    import capo_b2bi.types.partnership_capabilities
    import capo_b2bi.types.partnership_id
    import capo_b2bi.types.partnership_summary
    import capo_b2bi.types.phone
    import capo_b2bi.types.profile_id
    import capo_b2bi.types.tag_list
    import capo_b2bi.types.update_partnership_request
    import capo_b2bi.types.update_partnership_response
    from capo_b2bi._services.async_b2bi import Asyncb2biClient, Asyncb2biClientConfig
    from capo_b2bi._services.b2bi import b2biClient, b2biClientConfig


class Partnership:
    def __init__(self, service: b2biClient) -> None:
        self._service = service

    def create(
        self,
        profile_id: "capo_b2bi.types.profile_id.ProfileId",
        name: "capo_b2bi.types.partner_name.PartnerName",
        email: "capo_b2bi.types.email.Email",
        capabilities: "capo_b2bi.types.partnership_capabilities.PartnershipCapabilities",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        phone: Optional["capo_b2bi.types.phone.Phone"] = None,
        capability_options: Optional[
            "capo_b2bi.types.capability_options.CapabilityOptions"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_b2bi.types.tag_list.TagList"] = None,
    ) -> "capo_b2bi.types.create_partnership_response.CreatePartnershipResponse":
        """<p>Creates a partnership between a customer and a trading partner, based on the supplied parameters. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>
            name: <p>Specifies a descriptive name for the partnership.</p>
            email: <p>Specifies the email address associated with this trading partner.</p>
            phone: <p>Specifies the phone number associated with the partnership.</p>
            capabilities: <p>Specifies a list of the capabilities associated with this partnership.</p>
            capability_options: <p>Specify the structure that contains the details for the associated capabilities.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample CreatePartnership call

            >>> client.create(capabilities=['ca-963a8121e4fc4e348'], client_token='foo', email='john@example.com', name='b2bipartner', phone='5555555555', profile_id='p-60fbc37c87f04fce9', tags=[{'Key': 'sampleKey1', 'Value': 'sampleValue1'}])
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.create_partnership_request.CreatePartnershipRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.create_partnership_response.CreatePartnershipResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_partnership

            output, http_response = (
                capo_b2bi._operations.b2_bi.create_partnership.create_partnership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_b2bi.types.create_partnership_request.CreatePartnershipRequest",
        ) -> dict[str, Any]:
            import capo_b2bi.types.create_partnership_request

            return capo_b2bi.types.create_partnership_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_b2bi.types.create_partnership_response.CreatePartnershipResponse",
        ) -> dict[str, Any]:
            import capo_b2bi.types.create_partnership_response

            return capo_b2bi.types.create_partnership_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreatePartnership",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_b2bi.types.create_partnership_request.CreatePartnershipRequest = {
            "profile_id": profile_id,
            "name": name,
            "email": email,
            "capabilities": capabilities,
        }
        if phone is not None:
            input_["phone"] = phone
        if capability_options is not None:
            input_["capability_options"] = capability_options
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
        partnership_id: "capo_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_partnership_response.GetPartnershipResponse":
        """<p>Retrieves the details for a partnership, based on the partner and profile IDs specified. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetPartnership call

            >>> client.read(partnership_id='ps-219fa02f5b4242af8')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.get_partnership_request.GetPartnershipRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.get_partnership_response.GetPartnershipResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_partnership

            output, http_response = (
                capo_b2bi._operations.b2_bi.get_partnership.get_partnership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_b2bi.types.get_partnership_response.GetPartnershipResponse",
        ) -> dict[str, Any]:
            import capo_b2bi.types.get_partnership_response

            return capo_b2bi.types.get_partnership_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetPartnership", redact_output=_redact_output),
        )
        input_: capo_b2bi.types.get_partnership_request.GetPartnershipRequest = {
            "partnership_id": partnership_id
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
        partnership_id: "capo_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        name: Optional["capo_b2bi.types.partner_name.PartnerName"] = None,
        capabilities: Optional[
            "capo_b2bi.types.partnership_capabilities.PartnershipCapabilities"
        ] = None,
        capability_options: Optional[
            "capo_b2bi.types.capability_options.CapabilityOptions"
        ] = None,
    ) -> "capo_b2bi.types.update_partnership_response.UpdatePartnershipResponse":
        """<p>Updates some of the parameters for a partnership between a customer and trading partner. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>
            name: <p>The name of the partnership, used to identify it.</p>
            capabilities: <p>List of the capabilities associated with this partnership.</p>
            capability_options: <p>To update, specify the structure that contains the details for the associated capabilities.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample UpdatePartnership call

            >>> client.update(capabilities=['ca-963a8121e4fc4e348'], name='b2bipartner', partnership_id='ps-219fa02f5b4242af8')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.update_partnership_request.UpdatePartnershipRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.update_partnership_response.UpdatePartnershipResponse"
        ]:
            import capo_b2bi._operations.b2_bi.update_partnership

            output, http_response = (
                capo_b2bi._operations.b2_bi.update_partnership.update_partnership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_b2bi.types.update_partnership_response.UpdatePartnershipResponse",
        ) -> dict[str, Any]:
            import capo_b2bi.types.update_partnership_response

            return capo_b2bi.types.update_partnership_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdatePartnership", redact_output=_redact_output),
        )
        input_: capo_b2bi.types.update_partnership_request.UpdatePartnershipRequest = {
            "partnership_id": partnership_id
        }
        if name is not None:
            input_["name"] = name
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if capability_options is not None:
            input_["capability_options"] = capability_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        partnership_id: "capo_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified partnership. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeletePartnership call

            >>> client.delete(partnership_id='ps-219fa02f5b4242af8')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.delete_partnership_request.DeletePartnershipRequest]",
        ) -> OperationResponse[None]:
            import capo_b2bi._operations.b2_bi.delete_partnership

            output, http_response = (
                capo_b2bi._operations.b2_bi.delete_partnership.delete_partnership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePartnership")
        )
        input_: capo_b2bi.types.delete_partnership_request.DeletePartnershipRequest = {
            "partnership_id": partnership_id
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
        config_overrides: Optional[b2biClientConfig] = None,
        profile_id: Optional["capo_b2bi.types.profile_id.ProfileId"] = None,
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "capo_b2bi.types.list_partnerships_response.ListPartnershipsResponse":
        """<p>Lists the partnerships associated with your Amazon Web Services account for your current or specified region. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of capabilities to return.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListPartnerships call

            >>> client.list(max_results=50, next_token='foo', profile_id='p-60fbc37c87f04fce9')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.list_partnerships_request.ListPartnershipsRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.list_partnerships_response.ListPartnershipsResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_partnerships

            output, http_response = (
                capo_b2bi._operations.b2_bi.list_partnerships.list_partnerships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPartnerships")
        )
        input_: capo_b2bi.types.list_partnerships_request.ListPartnershipsRequest = {}
        if profile_id is not None:
            input_["profile_id"] = profile_id
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


class AsyncPartnership:
    def __init__(self, service: Asyncb2biClient) -> None:
        self._service = service

    async def create(
        self,
        profile_id: "capo_b2bi.types.profile_id.ProfileId",
        name: "capo_b2bi.types.partner_name.PartnerName",
        email: "capo_b2bi.types.email.Email",
        capabilities: "capo_b2bi.types.partnership_capabilities.PartnershipCapabilities",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        phone: Optional["capo_b2bi.types.phone.Phone"] = None,
        capability_options: Optional[
            "capo_b2bi.types.capability_options.CapabilityOptions"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_b2bi.types.tag_list.TagList"] = None,
    ) -> "capo_b2bi.types.create_partnership_response.CreatePartnershipResponse":
        """<p>Creates a partnership between a customer and a trading partner, based on the supplied parameters. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>
            name: <p>Specifies a descriptive name for the partnership.</p>
            email: <p>Specifies the email address associated with this trading partner.</p>
            phone: <p>Specifies the phone number associated with the partnership.</p>
            capabilities: <p>Specifies a list of the capabilities associated with this partnership.</p>
            capability_options: <p>Specify the structure that contains the details for the associated capabilities.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample CreatePartnership call

            >>> await client.create(capabilities=['ca-963a8121e4fc4e348'], client_token='foo', email='john@example.com', name='b2bipartner', phone='5555555555', profile_id='p-60fbc37c87f04fce9', tags=[{'Key': 'sampleKey1', 'Value': 'sampleValue1'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.create_partnership_request.CreatePartnershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.create_partnership_response.CreatePartnershipResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_partnership

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.create_partnership.async_create_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_b2bi.types.create_partnership_request.CreatePartnershipRequest",
        ) -> dict[str, Any]:
            import capo_b2bi.types.create_partnership_request

            return capo_b2bi.types.create_partnership_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_b2bi.types.create_partnership_response.CreatePartnershipResponse",
        ) -> dict[str, Any]:
            import capo_b2bi.types.create_partnership_response

            return capo_b2bi.types.create_partnership_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreatePartnership",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_b2bi.types.create_partnership_request.CreatePartnershipRequest = {
            "profile_id": profile_id,
            "name": name,
            "email": email,
            "capabilities": capabilities,
        }
        if phone is not None:
            input_["phone"] = phone
        if capability_options is not None:
            input_["capability_options"] = capability_options
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
        partnership_id: "capo_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_partnership_response.GetPartnershipResponse":
        """<p>Retrieves the details for a partnership, based on the partner and profile IDs specified. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetPartnership call

            >>> await client.read(partnership_id='ps-219fa02f5b4242af8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.get_partnership_request.GetPartnershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.get_partnership_response.GetPartnershipResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_partnership

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.get_partnership.async_get_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_b2bi.types.get_partnership_response.GetPartnershipResponse",
        ) -> dict[str, Any]:
            import capo_b2bi.types.get_partnership_response

            return capo_b2bi.types.get_partnership_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetPartnership", redact_output=_redact_output),
        )
        input_: capo_b2bi.types.get_partnership_request.GetPartnershipRequest = {
            "partnership_id": partnership_id
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
        partnership_id: "capo_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        name: Optional["capo_b2bi.types.partner_name.PartnerName"] = None,
        capabilities: Optional[
            "capo_b2bi.types.partnership_capabilities.PartnershipCapabilities"
        ] = None,
        capability_options: Optional[
            "capo_b2bi.types.capability_options.CapabilityOptions"
        ] = None,
    ) -> "capo_b2bi.types.update_partnership_response.UpdatePartnershipResponse":
        """<p>Updates some of the parameters for a partnership between a customer and trading partner. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>
            name: <p>The name of the partnership, used to identify it.</p>
            capabilities: <p>List of the capabilities associated with this partnership.</p>
            capability_options: <p>To update, specify the structure that contains the details for the associated capabilities.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample UpdatePartnership call

            >>> await client.update(capabilities=['ca-963a8121e4fc4e348'], name='b2bipartner', partnership_id='ps-219fa02f5b4242af8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.update_partnership_request.UpdatePartnershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.update_partnership_response.UpdatePartnershipResponse"
        ]:
            import capo_b2bi._operations.b2_bi.update_partnership

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.update_partnership.async_update_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_b2bi.types.update_partnership_response.UpdatePartnershipResponse",
        ) -> dict[str, Any]:
            import capo_b2bi.types.update_partnership_response

            return capo_b2bi.types.update_partnership_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdatePartnership", redact_output=_redact_output),
        )
        input_: capo_b2bi.types.update_partnership_request.UpdatePartnershipRequest = {
            "partnership_id": partnership_id
        }
        if name is not None:
            input_["name"] = name
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if capability_options is not None:
            input_["capability_options"] = capability_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        partnership_id: "capo_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified partnership. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeletePartnership call

            >>> await client.delete(partnership_id='ps-219fa02f5b4242af8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.delete_partnership_request.DeletePartnershipRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_b2bi._operations.b2_bi.delete_partnership

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.delete_partnership.async_delete_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePartnership")
        )
        input_: capo_b2bi.types.delete_partnership_request.DeletePartnershipRequest = {
            "partnership_id": partnership_id
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
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        profile_id: Optional["capo_b2bi.types.profile_id.ProfileId"] = None,
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "capo_b2bi.types.list_partnerships_response.ListPartnershipsResponse":
        """<p>Lists the partnerships associated with your Amazon Web Services account for your current or specified region. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of capabilities to return.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListPartnerships call

            >>> await client.list(max_results=50, next_token='foo', profile_id='p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.list_partnerships_request.ListPartnershipsRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.list_partnerships_response.ListPartnershipsResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_partnerships

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.list_partnerships.async_list_partnerships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPartnerships")
        )
        input_: capo_b2bi.types.list_partnerships_request.ListPartnershipsRequest = {}
        if profile_id is not None:
            input_["profile_id"] = profile_id
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
