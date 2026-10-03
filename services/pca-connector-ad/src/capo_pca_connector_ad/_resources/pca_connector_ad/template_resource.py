from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_pca_connector_ad._auth._signers
import capo_pca_connector_ad._auth._sigv4
from capo_pca_connector_ad._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.client_token
    import capo_pca_connector_ad.types.connector_arn
    import capo_pca_connector_ad.types.create_template_request
    import capo_pca_connector_ad.types.create_template_response
    import capo_pca_connector_ad.types.delete_template_request
    import capo_pca_connector_ad.types.get_template_request
    import capo_pca_connector_ad.types.get_template_response
    import capo_pca_connector_ad.types.list_templates_request
    import capo_pca_connector_ad.types.list_templates_response
    import capo_pca_connector_ad.types.max_results
    import capo_pca_connector_ad.types.next_token
    import capo_pca_connector_ad.types.tags
    import capo_pca_connector_ad.types.template_arn
    import capo_pca_connector_ad.types.template_definition
    import capo_pca_connector_ad.types.template_name
    import capo_pca_connector_ad.types.template_summary
    import capo_pca_connector_ad.types.update_template_request
    from capo_pca_connector_ad._services.async_pca_connector_ad import (
        AsyncPcaConnectorAdClient,
        AsyncPcaConnectorAdClientConfig,
    )
    from capo_pca_connector_ad._services.pca_connector_ad import (
        PcaConnectorAdClient,
        PcaConnectorAdClientConfig,
    )


class TemplateResource:
    def __init__(self, service: PcaConnectorAdClient) -> None:
        self._service = service

    def create(
        self,
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        name: "capo_pca_connector_ad.types.template_name.TemplateName",
        definition: "capo_pca_connector_ad.types.template_definition.TemplateDefinition",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_ad.types.tags.Tags"] = None,
    ) -> "capo_pca_connector_ad.types.create_template_response.CreateTemplateResponse":
        """<p>Creates an Active Directory compatible certificate template. The connectors issues certificates using these templates based on the requester’s Active Directory group membership.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>
            name: <p>Name of the template. The template name must be unique.</p>
            definition: <p>Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.</p>
            client_token: <p>Idempotency token.</p>
            tags: <p>Metadata assigned to a template consisting of a key-value pair.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.create_template_request.CreateTemplateRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_ad.types.create_template_response.CreateTemplateResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_template

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.create_template.create_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_template_request.CreateTemplateRequest = {
            "connector_arn": connector_arn,
            "name": name,
            "definition": definition,
        }
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
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_template_response.GetTemplateResponse":
        """<p>Retrieves a certificate template that the connector uses to issue certificates from a private CA.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.get_template_request.GetTemplateRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_ad.types.get_template_response.GetTemplateResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_template

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.get_template.get_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_template_request.GetTemplateRequest = {
            "template_arn": template_arn
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
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        definition: Optional[
            "capo_pca_connector_ad.types.template_definition.TemplateDefinition"
        ] = None,
        reenroll_all_certificate_holders: Optional[bool] = None,
    ) -> None:
        """<p>Update template configuration to define the information included in certificates.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>
            definition: <p>Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.</p>
            reenroll_all_certificate_holders: <p>This setting allows the major version of a template to be increased automatically. All members of Active Directory groups that are allowed to enroll with a template will receive a new certificate issued using that template.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.update_template_request.UpdateTemplateRequest]",
        ) -> OperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.update_template

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.update_template.update_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.update_template_request.UpdateTemplateRequest = {
            "template_arn": template_arn
        }
        if definition is not None:
            input_["definition"] = definition
        if reenroll_all_certificate_holders is not None:
            input_["reenroll_all_certificate_holders"] = (
                reenroll_all_certificate_holders
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a template. Certificates issued using the template are still valid until they are revoked or expired.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.delete_template_request.DeleteTemplateRequest]",
        ) -> OperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_template

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.delete_template.delete_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_template_request.DeleteTemplateRequest = {
            "template_arn": template_arn
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
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[PcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_templates_response.ListTemplatesResponse":
        """<p>Lists the templates, if any, that are associated with a connector.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_pca_connector_ad.types.list_templates_request.ListTemplatesRequest]",
        ) -> OperationResponse[
            "capo_pca_connector_ad.types.list_templates_response.ListTemplatesResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_templates

            output, http_response = (
                capo_pca_connector_ad._operations.pca_connector_ad.list_templates.list_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_templates_request.ListTemplatesRequest = {
            "connector_arn": connector_arn
        }
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


class AsyncTemplateResource:
    def __init__(self, service: AsyncPcaConnectorAdClient) -> None:
        self._service = service

    async def create(
        self,
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        name: "capo_pca_connector_ad.types.template_name.TemplateName",
        definition: "capo_pca_connector_ad.types.template_definition.TemplateDefinition",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        client_token: Optional[
            "capo_pca_connector_ad.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_pca_connector_ad.types.tags.Tags"] = None,
    ) -> "capo_pca_connector_ad.types.create_template_response.CreateTemplateResponse":
        """<p>Creates an Active Directory compatible certificate template. The connectors issues certificates using these templates based on the requester’s Active Directory group membership.</p>

        Args:
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>
            name: <p>Name of the template. The template name must be unique.</p>
            definition: <p>Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.</p>
            client_token: <p>Idempotency token.</p>
            tags: <p>Metadata assigned to a template consisting of a key-value pair.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.create_template_request.CreateTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.create_template_response.CreateTemplateResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.create_template

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.create_template.async_create_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.create_template_request.CreateTemplateRequest = {
            "connector_arn": connector_arn,
            "name": name,
            "definition": definition,
        }
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
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> "capo_pca_connector_ad.types.get_template_response.GetTemplateResponse":
        """<p>Retrieves a certificate template that the connector uses to issue certificates from a private CA.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.get_template_request.GetTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.get_template_response.GetTemplateResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.get_template

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.get_template.async_get_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.get_template_request.GetTemplateRequest = {
            "template_arn": template_arn
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
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        definition: Optional[
            "capo_pca_connector_ad.types.template_definition.TemplateDefinition"
        ] = None,
        reenroll_all_certificate_holders: Optional[bool] = None,
    ) -> None:
        """<p>Update template configuration to define the information included in certificates.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>
            definition: <p>Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.</p>
            reenroll_all_certificate_holders: <p>This setting allows the major version of a template to be increased automatically. All members of Active Directory groups that are allowed to enroll with a template will receive a new certificate issued using that template.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.update_template_request.UpdateTemplateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.update_template

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.update_template.async_update_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.update_template_request.UpdateTemplateRequest = {
            "template_arn": template_arn
        }
        if definition is not None:
            input_["definition"] = definition
        if reenroll_all_certificate_holders is not None:
            input_["reenroll_all_certificate_holders"] = (
                reenroll_all_certificate_holders
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
    ) -> None:
        """<p>Deletes a template. Certificates issued using the template are still valid until they are revoked or expired.</p>

        Args:
            template_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons because the requested resource was being concurrently modified by another request.</p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.delete_template_request.DeleteTemplateRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_pca_connector_ad._operations.pca_connector_ad.delete_template

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.delete_template.async_delete_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.delete_template_request.DeleteTemplateRequest = {
            "template_arn": template_arn
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
        connector_arn: "capo_pca_connector_ad.types.connector_arn.ConnectorArn",
        *,
        config_overrides: Optional[AsyncPcaConnectorAdClientConfig] = None,
        max_results: Optional[
            "capo_pca_connector_ad.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_pca_connector_ad.types.next_token.NextToken"] = None,
    ) -> "capo_pca_connector_ad.types.list_templates_response.ListTemplatesResponse":
        """<p>Lists the templates, if any, that are associated with a connector.</p>

        Args:
            max_results: <p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>
            next_token: <p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>
            connector_arn: <p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>.</p>

        Raises:
            capo_pca_connector_ad.errors.access_denied_exception.AccessDeniedException: <p>You can receive this error if you attempt to create a resource share when you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your Amazon Web Services Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an Amazon Web Services Organizations service control policy (SCP) that affects your Amazon Web Services account. </p>
            capo_pca_connector_ad.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server. </p>
            capo_pca_connector_ad.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a nonexistent resource. The resource might not be specified correctly, or its status might not be ACTIVE.</p>
            capo_pca_connector_ad.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded. </p>
            capo_pca_connector_ad.errors.validation_exception.ValidationException: <p>An input validation error occurred. For example, invalid characters in a template name, or if a pagination token is invalid. </p>
            capo_pca_connector_ad.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pca_connector_ad.types.list_templates_request.ListTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_pca_connector_ad.types.list_templates_response.ListTemplatesResponse"
        ]:
            import capo_pca_connector_ad._operations.pca_connector_ad.list_templates

            (
                output,
                http_response,
            ) = await capo_pca_connector_ad._operations.pca_connector_ad.list_templates.async_list_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_pca_connector_ad.types.list_templates_request.ListTemplatesRequest = {
            "connector_arn": connector_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
