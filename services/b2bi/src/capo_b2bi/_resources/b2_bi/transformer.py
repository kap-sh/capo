from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_b2bi._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_b2bi.types.create_transformer_request
    import capo_b2bi.types.create_transformer_response
    import capo_b2bi.types.delete_transformer_request
    import capo_b2bi.types.edi_type
    import capo_b2bi.types.file_format
    import capo_b2bi.types.file_location
    import capo_b2bi.types.get_transformer_request
    import capo_b2bi.types.get_transformer_response
    import capo_b2bi.types.input_conversion
    import capo_b2bi.types.list_transformers_request
    import capo_b2bi.types.list_transformers_response
    import capo_b2bi.types.mapping
    import capo_b2bi.types.mapping_template
    import capo_b2bi.types.max_results
    import capo_b2bi.types.output_conversion
    import capo_b2bi.types.page_token
    import capo_b2bi.types.sample_documents
    import capo_b2bi.types.tag_list
    import capo_b2bi.types.transformer_id
    import capo_b2bi.types.transformer_name
    import capo_b2bi.types.transformer_status
    import capo_b2bi.types.transformer_summary
    import capo_b2bi.types.update_transformer_request
    import capo_b2bi.types.update_transformer_response
    from capo_b2bi._services.async_b2bi import Asyncb2biClient, Asyncb2biClientConfig
    from capo_b2bi._services.b2bi import b2biClient, b2biClientConfig


class Transformer:
    def __init__(self, service: b2biClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_b2bi.types.transformer_name.TransformerName",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_b2bi.types.tag_list.TagList"] = None,
        file_format: Optional["capo_b2bi.types.file_format.FileFormat"] = None,
        mapping_template: Optional[
            "capo_b2bi.types.mapping_template.MappingTemplate"
        ] = None,
        edi_type: Optional["capo_b2bi.types.edi_type.EdiType"] = None,
        sample_document: Optional["capo_b2bi.types.file_location.FileLocation"] = None,
        input_conversion: Optional[
            "capo_b2bi.types.input_conversion.InputConversion"
        ] = None,
        mapping: Optional["capo_b2bi.types.mapping.Mapping"] = None,
        output_conversion: Optional[
            "capo_b2bi.types.output_conversion.OutputConversion"
        ] = None,
        sample_documents: Optional[
            "capo_b2bi.types.sample_documents.SampleDocuments"
        ] = None,
    ) -> "capo_b2bi.types.create_transformer_response.CreateTransformerResponse":
        """<p>Creates a transformer. Amazon Web Services B2B Data Interchange currently supports two scenarios:</p> <ul> <li> <p> <i>Inbound EDI</i>: the Amazon Web Services customer receives an EDI file from their trading partner. Amazon Web Services B2B Data Interchange converts this EDI file into a JSON or XML file with a service-defined structure. A mapping template provided by the customer, in JSONata or XSLT format, is optionally applied to this file to produce a JSON or XML file with the structure the customer requires.</p> </li> <li> <p> <i>Outbound EDI</i>: the Amazon Web Services customer has a JSON or XML file containing data that they wish to use in an EDI file. A mapping template, provided by the customer (in either JSONata or XSLT format) is applied to this file to generate a JSON or XML file in the service-defined structure. This file is then converted to an EDI file.</p> </li> </ul> <note> <p>The following fields are provided for backwards compatibility only: <code>fileFormat</code>, <code>mappingTemplate</code>, <code>ediType</code>, and <code>sampleDocument</code>.</p> <ul> <li> <p>Use the <code>mapping</code> data type in place of <code>mappingTemplate</code> and <code>fileFormat</code> </p> </li> <li> <p>Use the <code>sampleDocuments</code> data type in place of <code>sampleDocument</code> </p> </li> <li> <p>Use either the <code>inputConversion</code> or <code>outputConversion</code> in place of <code>ediType</code> </p> </li> </ul> </note>

        Args:
            name: <p>Specifies the name of the transformer, used to identify it.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>
            file_format: <p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>
            mapping_template: <p>Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p> <note> <p>This parameter is available for backwards compatibility. Use the <a href="https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html">Mapping</a> data type instead.</p> </note>
            edi_type: <p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>
            sample_document: <p>Specifies a sample EDI document that is used by a transformer as a guide for processing the EDI data.</p>
            input_conversion: <p>Specify the <code>InputConversion</code> object, which contains the format options for the inbound transformation.</p>
            mapping: <p>Specify the structure that contains the mapping template and its language (either XSLT or JSONATA).</p>
            output_conversion: <p>A structure that contains the <code>OutputConversion</code> object, which contains the format options for the outbound transformation.</p>
            sample_documents: <p>Specify a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.</p>

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
            Sample CreateTransformer call

            >>> client.create(client_token='foo', name='transformX12', input_conversion={'fromFormat': 'X12', 'formatOptions': {'x12': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'advancedOptions': {'x12': {'splitOptions': {'splitBy': 'NONE'}, 'validationOptions': {'validationRules': [{'codeListValidationRule': {'elementId': '1234', 'codesToAdd': ['A', 'B', 'C'], 'codesToRemove': ['X', 'Y', 'Z']}}, {'elementRequirementValidationRule': {'elementPosition': 'NM1-01', 'requirement': 'MANDATORY'}}, {'elementLengthValidationRule': {'elementId': '5678', 'maxLength': 10, 'minLength': 2}}]}}}}, mapping={'templateLanguage': 'JSONATA', 'template': '{}'}, sample_documents={'bucketName': 'test-bucket', 'keys': [{'input': 'sampleDoc.txt'}]}, tags=[{'Key': 'sampleKey', 'Value': 'sampleValue'}])
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.create_transformer_request.CreateTransformerRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.create_transformer_response.CreateTransformerResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_transformer

            output, http_response = (
                capo_b2bi._operations.b2_bi.create_transformer.create_transformer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_b2bi.types.create_transformer_request.CreateTransformerRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if file_format is not None:
            input_["file_format"] = file_format
        if mapping_template is not None:
            input_["mapping_template"] = mapping_template
        if edi_type is not None:
            input_["edi_type"] = edi_type
        if sample_document is not None:
            input_["sample_document"] = sample_document
        if input_conversion is not None:
            input_["input_conversion"] = input_conversion
        if mapping is not None:
            input_["mapping"] = mapping
        if output_conversion is not None:
            input_["output_conversion"] = output_conversion
        if sample_documents is not None:
            input_["sample_documents"] = sample_documents

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_transformer_response.GetTransformerResponse":
        """<p>Retrieves the details for the transformer specified by the transformer ID. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetTransformer call

            >>> client.read(transformer_id='tr-974c129999f84d8c9')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.get_transformer_request.GetTransformerRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.get_transformer_response.GetTransformerResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_transformer

            output, http_response = (
                capo_b2bi._operations.b2_bi.get_transformer.get_transformer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_b2bi.types.get_transformer_request.GetTransformerRequest = {
            "transformer_id": transformer_id
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
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
        name: Optional["capo_b2bi.types.transformer_name.TransformerName"] = None,
        status: Optional["capo_b2bi.types.transformer_status.TransformerStatus"] = None,
        file_format: Optional["capo_b2bi.types.file_format.FileFormat"] = None,
        mapping_template: Optional[
            "capo_b2bi.types.mapping_template.MappingTemplate"
        ] = None,
        edi_type: Optional["capo_b2bi.types.edi_type.EdiType"] = None,
        sample_document: Optional["capo_b2bi.types.file_location.FileLocation"] = None,
        input_conversion: Optional[
            "capo_b2bi.types.input_conversion.InputConversion"
        ] = None,
        mapping: Optional["capo_b2bi.types.mapping.Mapping"] = None,
        output_conversion: Optional[
            "capo_b2bi.types.output_conversion.OutputConversion"
        ] = None,
        sample_documents: Optional[
            "capo_b2bi.types.sample_documents.SampleDocuments"
        ] = None,
    ) -> "capo_b2bi.types.update_transformer_response.UpdateTransformerResponse":
        """<p>Updates the specified parameters for a transformer. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>
            name: <p>Specify a new name for the transformer, if you want to update it.</p>
            status: <p>Specifies the transformer's status. You can update the state of the transformer from <code>inactive</code> to <code>active</code>.</p>
            file_format: <p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>
            mapping_template: <p>Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p> <note> <p>This parameter is available for backwards compatibility. Use the <a href="https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html">Mapping</a> data type instead.</p> </note>
            edi_type: <p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>
            sample_document: <p>Specifies a sample EDI document that is used by a transformer as a guide for processing the EDI data.</p>
            input_conversion: <p>To update, specify the <code>InputConversion</code> object, which contains the format options for the inbound transformation.</p>
            mapping: <p>Specify the structure that contains the mapping template and its language (either XSLT or JSONATA).</p>
            output_conversion: <p>To update, specify the <code>OutputConversion</code> object, which contains the format options for the outbound transformation.</p>
            sample_documents: <p>Specify a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.</p>

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
            Sample UpdateTransformer call

            >>> client.update(input_conversion={'fromFormat': 'X12', 'formatOptions': {'x12': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'advancedOptions': {'x12': {'splitOptions': {'splitBy': 'NONE'}, 'validationOptions': {'validationRules': [{'codeListValidationRule': {'elementId': '1234', 'codesToAdd': ['A', 'B', 'C'], 'codesToRemove': ['X', 'Y', 'Z']}}, {'elementRequirementValidationRule': {'elementPosition': 'NM1-01', 'requirement': 'MANDATORY'}}, {'elementLengthValidationRule': {'elementId': '5678', 'maxLength': 10, 'minLength': 2}}]}}}}, mapping={'templateLanguage': 'JSONATA', 'template': '{}'}, sample_documents={'bucketName': 'test-bucket', 'keys': [{'input': 'sampleDoc.txt'}]}, name='transformX12', status='inactive', transformer_id='tr-974c129999f84d8c9')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.update_transformer_request.UpdateTransformerRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.update_transformer_response.UpdateTransformerResponse"
        ]:
            import capo_b2bi._operations.b2_bi.update_transformer

            output, http_response = (
                capo_b2bi._operations.b2_bi.update_transformer.update_transformer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_b2bi.types.update_transformer_request.UpdateTransformerRequest = {
            "transformer_id": transformer_id
        }
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if file_format is not None:
            input_["file_format"] = file_format
        if mapping_template is not None:
            input_["mapping_template"] = mapping_template
        if edi_type is not None:
            input_["edi_type"] = edi_type
        if sample_document is not None:
            input_["sample_document"] = sample_document
        if input_conversion is not None:
            input_["input_conversion"] = input_conversion
        if mapping is not None:
            input_["mapping"] = mapping
        if output_conversion is not None:
            input_["output_conversion"] = output_conversion
        if sample_documents is not None:
            input_["sample_documents"] = sample_documents

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[b2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified transformer. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeleteTransformer call

            >>> client.delete(transformer_id='tr-974c129999f84d8c9')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.delete_transformer_request.DeleteTransformerRequest]",
        ) -> OperationResponse[None]:
            import capo_b2bi._operations.b2_bi.delete_transformer

            output, http_response = (
                capo_b2bi._operations.b2_bi.delete_transformer.delete_transformer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_b2bi.types.delete_transformer_request.DeleteTransformerRequest = {
            "transformer_id": transformer_id
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
    ) -> "capo_b2bi.types.list_transformers_response.ListTransformersResponse":
        """<p>Lists the available transformers. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the number of items to return for the API response.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListTransformers call

            >>> client.list(max_results=50, next_token='foo')
        """

        def _handler(
            req: "OperationRequest[capo_b2bi.types.list_transformers_request.ListTransformersRequest]",
        ) -> OperationResponse[
            "capo_b2bi.types.list_transformers_response.ListTransformersResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_transformers

            output, http_response = (
                capo_b2bi._operations.b2_bi.list_transformers.list_transformers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_b2bi.types.list_transformers_request.ListTransformersRequest = {}
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


class AsyncTransformer:
    def __init__(self, service: Asyncb2biClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_b2bi.types.transformer_name.TransformerName",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_b2bi.types.tag_list.TagList"] = None,
        file_format: Optional["capo_b2bi.types.file_format.FileFormat"] = None,
        mapping_template: Optional[
            "capo_b2bi.types.mapping_template.MappingTemplate"
        ] = None,
        edi_type: Optional["capo_b2bi.types.edi_type.EdiType"] = None,
        sample_document: Optional["capo_b2bi.types.file_location.FileLocation"] = None,
        input_conversion: Optional[
            "capo_b2bi.types.input_conversion.InputConversion"
        ] = None,
        mapping: Optional["capo_b2bi.types.mapping.Mapping"] = None,
        output_conversion: Optional[
            "capo_b2bi.types.output_conversion.OutputConversion"
        ] = None,
        sample_documents: Optional[
            "capo_b2bi.types.sample_documents.SampleDocuments"
        ] = None,
    ) -> "capo_b2bi.types.create_transformer_response.CreateTransformerResponse":
        """<p>Creates a transformer. Amazon Web Services B2B Data Interchange currently supports two scenarios:</p> <ul> <li> <p> <i>Inbound EDI</i>: the Amazon Web Services customer receives an EDI file from their trading partner. Amazon Web Services B2B Data Interchange converts this EDI file into a JSON or XML file with a service-defined structure. A mapping template provided by the customer, in JSONata or XSLT format, is optionally applied to this file to produce a JSON or XML file with the structure the customer requires.</p> </li> <li> <p> <i>Outbound EDI</i>: the Amazon Web Services customer has a JSON or XML file containing data that they wish to use in an EDI file. A mapping template, provided by the customer (in either JSONata or XSLT format) is applied to this file to generate a JSON or XML file in the service-defined structure. This file is then converted to an EDI file.</p> </li> </ul> <note> <p>The following fields are provided for backwards compatibility only: <code>fileFormat</code>, <code>mappingTemplate</code>, <code>ediType</code>, and <code>sampleDocument</code>.</p> <ul> <li> <p>Use the <code>mapping</code> data type in place of <code>mappingTemplate</code> and <code>fileFormat</code> </p> </li> <li> <p>Use the <code>sampleDocuments</code> data type in place of <code>sampleDocument</code> </p> </li> <li> <p>Use either the <code>inputConversion</code> or <code>outputConversion</code> in place of <code>ediType</code> </p> </li> </ul> </note>

        Args:
            name: <p>Specifies the name of the transformer, used to identify it.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>
            file_format: <p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>
            mapping_template: <p>Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p> <note> <p>This parameter is available for backwards compatibility. Use the <a href="https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html">Mapping</a> data type instead.</p> </note>
            edi_type: <p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>
            sample_document: <p>Specifies a sample EDI document that is used by a transformer as a guide for processing the EDI data.</p>
            input_conversion: <p>Specify the <code>InputConversion</code> object, which contains the format options for the inbound transformation.</p>
            mapping: <p>Specify the structure that contains the mapping template and its language (either XSLT or JSONATA).</p>
            output_conversion: <p>A structure that contains the <code>OutputConversion</code> object, which contains the format options for the outbound transformation.</p>
            sample_documents: <p>Specify a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.</p>

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
            Sample CreateTransformer call

            >>> await client.create(client_token='foo', name='transformX12', input_conversion={'fromFormat': 'X12', 'formatOptions': {'x12': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'advancedOptions': {'x12': {'splitOptions': {'splitBy': 'NONE'}, 'validationOptions': {'validationRules': [{'codeListValidationRule': {'elementId': '1234', 'codesToAdd': ['A', 'B', 'C'], 'codesToRemove': ['X', 'Y', 'Z']}}, {'elementRequirementValidationRule': {'elementPosition': 'NM1-01', 'requirement': 'MANDATORY'}}, {'elementLengthValidationRule': {'elementId': '5678', 'maxLength': 10, 'minLength': 2}}]}}}}, mapping={'templateLanguage': 'JSONATA', 'template': '{}'}, sample_documents={'bucketName': 'test-bucket', 'keys': [{'input': 'sampleDoc.txt'}]}, tags=[{'Key': 'sampleKey', 'Value': 'sampleValue'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.create_transformer_request.CreateTransformerRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.create_transformer_response.CreateTransformerResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_transformer

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.create_transformer.async_create_transformer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_b2bi.types.create_transformer_request.CreateTransformerRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if file_format is not None:
            input_["file_format"] = file_format
        if mapping_template is not None:
            input_["mapping_template"] = mapping_template
        if edi_type is not None:
            input_["edi_type"] = edi_type
        if sample_document is not None:
            input_["sample_document"] = sample_document
        if input_conversion is not None:
            input_["input_conversion"] = input_conversion
        if mapping is not None:
            input_["mapping"] = mapping
        if output_conversion is not None:
            input_["output_conversion"] = output_conversion
        if sample_documents is not None:
            input_["sample_documents"] = sample_documents

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_transformer_response.GetTransformerResponse":
        """<p>Retrieves the details for the transformer specified by the transformer ID. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetTransformer call

            >>> await client.read(transformer_id='tr-974c129999f84d8c9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.get_transformer_request.GetTransformerRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.get_transformer_response.GetTransformerResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_transformer

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.get_transformer.async_get_transformer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_b2bi.types.get_transformer_request.GetTransformerRequest = {
            "transformer_id": transformer_id
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
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        name: Optional["capo_b2bi.types.transformer_name.TransformerName"] = None,
        status: Optional["capo_b2bi.types.transformer_status.TransformerStatus"] = None,
        file_format: Optional["capo_b2bi.types.file_format.FileFormat"] = None,
        mapping_template: Optional[
            "capo_b2bi.types.mapping_template.MappingTemplate"
        ] = None,
        edi_type: Optional["capo_b2bi.types.edi_type.EdiType"] = None,
        sample_document: Optional["capo_b2bi.types.file_location.FileLocation"] = None,
        input_conversion: Optional[
            "capo_b2bi.types.input_conversion.InputConversion"
        ] = None,
        mapping: Optional["capo_b2bi.types.mapping.Mapping"] = None,
        output_conversion: Optional[
            "capo_b2bi.types.output_conversion.OutputConversion"
        ] = None,
        sample_documents: Optional[
            "capo_b2bi.types.sample_documents.SampleDocuments"
        ] = None,
    ) -> "capo_b2bi.types.update_transformer_response.UpdateTransformerResponse":
        """<p>Updates the specified parameters for a transformer. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>
            name: <p>Specify a new name for the transformer, if you want to update it.</p>
            status: <p>Specifies the transformer's status. You can update the state of the transformer from <code>inactive</code> to <code>active</code>.</p>
            file_format: <p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>
            mapping_template: <p>Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p> <note> <p>This parameter is available for backwards compatibility. Use the <a href="https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html">Mapping</a> data type instead.</p> </note>
            edi_type: <p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>
            sample_document: <p>Specifies a sample EDI document that is used by a transformer as a guide for processing the EDI data.</p>
            input_conversion: <p>To update, specify the <code>InputConversion</code> object, which contains the format options for the inbound transformation.</p>
            mapping: <p>Specify the structure that contains the mapping template and its language (either XSLT or JSONATA).</p>
            output_conversion: <p>To update, specify the <code>OutputConversion</code> object, which contains the format options for the outbound transformation.</p>
            sample_documents: <p>Specify a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.</p>

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
            Sample UpdateTransformer call

            >>> await client.update(input_conversion={'fromFormat': 'X12', 'formatOptions': {'x12': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'advancedOptions': {'x12': {'splitOptions': {'splitBy': 'NONE'}, 'validationOptions': {'validationRules': [{'codeListValidationRule': {'elementId': '1234', 'codesToAdd': ['A', 'B', 'C'], 'codesToRemove': ['X', 'Y', 'Z']}}, {'elementRequirementValidationRule': {'elementPosition': 'NM1-01', 'requirement': 'MANDATORY'}}, {'elementLengthValidationRule': {'elementId': '5678', 'maxLength': 10, 'minLength': 2}}]}}}}, mapping={'templateLanguage': 'JSONATA', 'template': '{}'}, sample_documents={'bucketName': 'test-bucket', 'keys': [{'input': 'sampleDoc.txt'}]}, name='transformX12', status='inactive', transformer_id='tr-974c129999f84d8c9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.update_transformer_request.UpdateTransformerRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.update_transformer_response.UpdateTransformerResponse"
        ]:
            import capo_b2bi._operations.b2_bi.update_transformer

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.update_transformer.async_update_transformer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_b2bi.types.update_transformer_request.UpdateTransformerRequest = {
            "transformer_id": transformer_id
        }
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if file_format is not None:
            input_["file_format"] = file_format
        if mapping_template is not None:
            input_["mapping_template"] = mapping_template
        if edi_type is not None:
            input_["edi_type"] = edi_type
        if sample_document is not None:
            input_["sample_document"] = sample_document
        if input_conversion is not None:
            input_["input_conversion"] = input_conversion
        if mapping is not None:
            input_["mapping"] = mapping
        if output_conversion is not None:
            input_["output_conversion"] = output_conversion
        if sample_documents is not None:
            input_["sample_documents"] = sample_documents

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified transformer. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeleteTransformer call

            >>> await client.delete(transformer_id='tr-974c129999f84d8c9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.delete_transformer_request.DeleteTransformerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_b2bi._operations.b2_bi.delete_transformer

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.delete_transformer.async_delete_transformer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_b2bi.types.delete_transformer_request.DeleteTransformerRequest = {
            "transformer_id": transformer_id
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
    ) -> "capo_b2bi.types.list_transformers_response.ListTransformersResponse":
        """<p>Lists the available transformers. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the number of items to return for the API response.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListTransformers call

            >>> await client.list(max_results=50, next_token='foo')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.list_transformers_request.ListTransformersRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.list_transformers_response.ListTransformersResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_transformers

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.list_transformers.async_list_transformers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_b2bi.types.list_transformers_request.ListTransformersRequest = {}
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
