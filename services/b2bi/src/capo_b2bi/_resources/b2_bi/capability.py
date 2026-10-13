from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

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
    import capo_b2bi.types.capability_configuration
    import capo_b2bi.types.capability_id
    import capo_b2bi.types.capability_name
    import capo_b2bi.types.capability_summary
    import capo_b2bi.types.capability_type
    import capo_b2bi.types.create_capability_request
    import capo_b2bi.types.create_capability_response
    import capo_b2bi.types.delete_capability_request
    import capo_b2bi.types.get_capability_request
    import capo_b2bi.types.get_capability_response
    import capo_b2bi.types.instructions_documents
    import capo_b2bi.types.list_capabilities_request
    import capo_b2bi.types.list_capabilities_response
    import capo_b2bi.types.max_results
    import capo_b2bi.types.page_token
    import capo_b2bi.types.tag_list
    import capo_b2bi.types.update_capability_request
    import capo_b2bi.types.update_capability_response
    from capo_b2bi._services.async_b2bi import Asyncb2biClient, Asyncb2biClientConfig
    from capo_b2bi._services.b2bi import b2biClient, b2biClientConfig


class Capability:
    def __init__(self, service: b2biClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_b2bi.types.capability_name.CapabilityName",
        type: "capo_b2bi.types.capability_type.CapabilityType",
        configuration: "capo_b2bi.types.capability_configuration.CapabilityConfiguration",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        instructions_documents: Optional[
            "capo_b2bi.types.instructions_documents.InstructionsDocuments"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_b2bi.types.tag_list.TagList"] = None,
    ) -> "capo_b2bi.types.create_capability_response.CreateCapabilityResponse":
        """<p>Instantiates a capability based on the specified parameters. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            name: <p>Specifies the name of the capability, used to identify it.</p>
            type: <p>Specifies the type of the capability. Currently, only <code>edi</code> is supported.</p>
            configuration: <p>Specifies a structure that contains the details for a capability.</p>
            instructions_documents: <p>Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>
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
            Sample CreateCapability call

            >>> client.create(name='b2biexample', type='edi', configuration={'edi': {'type': {'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'inputLocation': {'bucketName': 'test-bucket', 'key': 'input/'}, 'outputLocation': {'bucketName': 'test-bucket', 'key': 'output/'}, 'transformerId': 'tr-9a893cf536df4658b'}}, instructions_documents=[{'bucketName': 'test-bucket', 'key': 'instructiondoc.txt'}], client_token='foo', tags=[{'Key': 'capabilityKey1', 'Value': 'capabilityValue1'}])
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.create_capability_request.CreateCapabilityRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.create_capability_response.CreateCapabilityResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_capability

            output, http_response = (
                capo_b2bi._operations.b2_bi.create_capability.create_capability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCapability")
        )
        input_: capo_b2bi.types.create_capability_request.CreateCapabilityRequest = {
            "name": name,
            "type": type,
            "configuration": configuration,
        }
        if instructions_documents is not None:
            input_["instructions_documents"] = instructions_documents
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
        capability_id: "capo_b2bi.types.capability_id.CapabilityId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_capability_response.GetCapabilityResponse":
        """<p>Retrieves the details for the specified capability. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            capability_id: <p>Specifies a system-assigned unique identifier for the capability.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetCapabilty call

            >>> client.read(capability_id='ca-963a8121e4fc4e348')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.get_capability_request.GetCapabilityRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.get_capability_response.GetCapabilityResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_capability

            output, http_response = (
                capo_b2bi._operations.b2_bi.get_capability.get_capability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCapability")
        )
        input_: capo_b2bi.types.get_capability_request.GetCapabilityRequest = {
            "capability_id": capability_id
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
        capability_id: "capo_b2bi.types.capability_id.CapabilityId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        name: Optional["capo_b2bi.types.capability_name.CapabilityName"] = None,
        configuration: Optional[
            "capo_b2bi.types.capability_configuration.CapabilityConfiguration"
        ] = None,
        instructions_documents: Optional[
            "capo_b2bi.types.instructions_documents.InstructionsDocuments"
        ] = None,
    ) -> "capo_b2bi.types.update_capability_response.UpdateCapabilityResponse":
        """<p>Updates some of the parameters for a capability, based on the specified parameters. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            capability_id: <p>Specifies a system-assigned unique identifier for the capability.</p>
            name: <p>Specifies a new name for the capability, to replace the existing name.</p>
            configuration: <p>Specifies a structure that contains the details for a capability.</p>
            instructions_documents: <p>Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>

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
            Sample UpdateCapability call

            >>> client.update(capability_id='ca-963a8121e4fc4e348', name='b2biexample', instructions_documents=[{'bucketName': 'test-bucket', 'key': 'instructiondoc.txt'}], configuration={'edi': {'type': {'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'inputLocation': {'bucketName': 'test-bucket', 'key': 'input/'}, 'outputLocation': {'bucketName': 'test-bucket', 'key': 'output/'}, 'transformerId': 'tr-9a893cf536df4658b'}})
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.update_capability_request.UpdateCapabilityRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.update_capability_response.UpdateCapabilityResponse"
        ]:
            import capo_b2bi._operations.b2_bi.update_capability

            output, http_response = (
                capo_b2bi._operations.b2_bi.update_capability.update_capability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCapability")
        )
        input_: capo_b2bi.types.update_capability_request.UpdateCapabilityRequest = {
            "capability_id": capability_id
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if instructions_documents is not None:
            input_["instructions_documents"] = instructions_documents

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        capability_id: "capo_b2bi.types.capability_id.CapabilityId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified capability. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            capability_id: <p>Specifies a system-assigned unique identifier for the capability.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeleteCapabilty call

            >>> client.delete(capability_id='ca-963a8121e4fc4e348')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.delete_capability_request.DeleteCapabilityRequest]",
        ) -> OperationResponse[None]:
            import capo_b2bi._operations.b2_bi.delete_capability

            output, http_response = (
                capo_b2bi._operations.b2_bi.delete_capability.delete_capability(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCapability")
        )
        input_: capo_b2bi.types.delete_capability_request.DeleteCapabilityRequest = {
            "capability_id": capability_id
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
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "capo_b2bi.types.list_capabilities_response.ListCapabilitiesResponse":
        """<p>Lists the capabilities associated with your Amazon Web Services account for your current or specified region. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of capabilities to return.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListCapabilities call

            >>> client.list(max_results=50, next_token='foo')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.list_capabilities_request.ListCapabilitiesRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.list_capabilities_response.ListCapabilitiesResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_capabilities

            output, http_response = (
                capo_b2bi._operations.b2_bi.list_capabilities.list_capabilities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCapabilities")
        )
        input_: capo_b2bi.types.list_capabilities_request.ListCapabilitiesRequest = {}
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


class AsyncCapability:
    def __init__(self, service: Asyncb2biClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_b2bi.types.capability_name.CapabilityName",
        type: "capo_b2bi.types.capability_type.CapabilityType",
        configuration: "capo_b2bi.types.capability_configuration.CapabilityConfiguration",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        instructions_documents: Optional[
            "capo_b2bi.types.instructions_documents.InstructionsDocuments"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_b2bi.types.tag_list.TagList"] = None,
    ) -> "capo_b2bi.types.create_capability_response.CreateCapabilityResponse":
        """<p>Instantiates a capability based on the specified parameters. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            name: <p>Specifies the name of the capability, used to identify it.</p>
            type: <p>Specifies the type of the capability. Currently, only <code>edi</code> is supported.</p>
            configuration: <p>Specifies a structure that contains the details for a capability.</p>
            instructions_documents: <p>Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>
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
            Sample CreateCapability call

            >>> await client.create(name='b2biexample', type='edi', configuration={'edi': {'type': {'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'inputLocation': {'bucketName': 'test-bucket', 'key': 'input/'}, 'outputLocation': {'bucketName': 'test-bucket', 'key': 'output/'}, 'transformerId': 'tr-9a893cf536df4658b'}}, instructions_documents=[{'bucketName': 'test-bucket', 'key': 'instructiondoc.txt'}], client_token='foo', tags=[{'Key': 'capabilityKey1', 'Value': 'capabilityValue1'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.create_capability_request.CreateCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.create_capability_response.CreateCapabilityResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_capability

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.create_capability.async_create_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateCapability")
        )
        input_: capo_b2bi.types.create_capability_request.CreateCapabilityRequest = {
            "name": name,
            "type": type,
            "configuration": configuration,
        }
        if instructions_documents is not None:
            input_["instructions_documents"] = instructions_documents
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
        capability_id: "capo_b2bi.types.capability_id.CapabilityId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_capability_response.GetCapabilityResponse":
        """<p>Retrieves the details for the specified capability. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            capability_id: <p>Specifies a system-assigned unique identifier for the capability.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetCapabilty call

            >>> await client.read(capability_id='ca-963a8121e4fc4e348')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.get_capability_request.GetCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.get_capability_response.GetCapabilityResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_capability

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.get_capability.async_get_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCapability")
        )
        input_: capo_b2bi.types.get_capability_request.GetCapabilityRequest = {
            "capability_id": capability_id
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
        capability_id: "capo_b2bi.types.capability_id.CapabilityId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        name: Optional["capo_b2bi.types.capability_name.CapabilityName"] = None,
        configuration: Optional[
            "capo_b2bi.types.capability_configuration.CapabilityConfiguration"
        ] = None,
        instructions_documents: Optional[
            "capo_b2bi.types.instructions_documents.InstructionsDocuments"
        ] = None,
    ) -> "capo_b2bi.types.update_capability_response.UpdateCapabilityResponse":
        """<p>Updates some of the parameters for a capability, based on the specified parameters. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            capability_id: <p>Specifies a system-assigned unique identifier for the capability.</p>
            name: <p>Specifies a new name for the capability, to replace the existing name.</p>
            configuration: <p>Specifies a structure that contains the details for a capability.</p>
            instructions_documents: <p>Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>

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
            Sample UpdateCapability call

            >>> await client.update(capability_id='ca-963a8121e4fc4e348', name='b2biexample', instructions_documents=[{'bucketName': 'test-bucket', 'key': 'instructiondoc.txt'}], configuration={'edi': {'type': {'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'inputLocation': {'bucketName': 'test-bucket', 'key': 'input/'}, 'outputLocation': {'bucketName': 'test-bucket', 'key': 'output/'}, 'transformerId': 'tr-9a893cf536df4658b'}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.update_capability_request.UpdateCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.update_capability_response.UpdateCapabilityResponse"
        ]:
            import capo_b2bi._operations.b2_bi.update_capability

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.update_capability.async_update_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateCapability")
        )
        input_: capo_b2bi.types.update_capability_request.UpdateCapabilityRequest = {
            "capability_id": capability_id
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if instructions_documents is not None:
            input_["instructions_documents"] = instructions_documents

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        capability_id: "capo_b2bi.types.capability_id.CapabilityId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified capability. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            capability_id: <p>Specifies a system-assigned unique identifier for the capability.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeleteCapabilty call

            >>> await client.delete(capability_id='ca-963a8121e4fc4e348')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.delete_capability_request.DeleteCapabilityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_b2bi._operations.b2_bi.delete_capability

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.delete_capability.async_delete_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCapability")
        )
        input_: capo_b2bi.types.delete_capability_request.DeleteCapabilityRequest = {
            "capability_id": capability_id
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
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "capo_b2bi.types.list_capabilities_response.ListCapabilitiesResponse":
        """<p>Lists the capabilities associated with your Amazon Web Services account for your current or specified region. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of capabilities to return.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListCapabilities call

            >>> await client.list(max_results=50, next_token='foo')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.list_capabilities_request.ListCapabilitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.list_capabilities_response.ListCapabilitiesResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_capabilities

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.list_capabilities.async_list_capabilities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCapabilities")
        )
        input_: capo_b2bi.types.list_capabilities_request.ListCapabilitiesRequest = {}
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
