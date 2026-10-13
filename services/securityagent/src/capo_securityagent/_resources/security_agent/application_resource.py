from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_securityagent._auth._signers
import capo_securityagent._auth._sigv4
from capo_securityagent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_securityagent.types.application_id
    import capo_securityagent.types.application_summary
    import capo_securityagent.types.create_application_request
    import capo_securityagent.types.create_application_response
    import capo_securityagent.types.default_kms_key_id
    import capo_securityagent.types.delete_application_request
    import capo_securityagent.types.get_application_request
    import capo_securityagent.types.get_application_response
    import capo_securityagent.types.id_c_instance_arn
    import capo_securityagent.types.list_applications_request
    import capo_securityagent.types.list_applications_response
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token
    import capo_securityagent.types.role_arn
    import capo_securityagent.types.tag_map
    import capo_securityagent.types.update_application_request
    import capo_securityagent.types.update_application_response
    from capo_securityagent._services.async_security_agent import (
        AsyncSecurityAgentClient,
        AsyncSecurityAgentClientConfig,
    )
    from capo_securityagent._services.security_agent import (
        SecurityAgentClient,
        SecurityAgentClientConfig,
    )


class ApplicationResource:
    def __init__(self, service: SecurityAgentClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        idc_instance_arn: Optional[
            "capo_securityagent.types.id_c_instance_arn.IdCInstanceArn"
        ] = None,
        role_arn: Optional["capo_securityagent.types.role_arn.RoleArn"] = None,
        default_kms_key_id: Optional[
            "capo_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
        ] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_securityagent.types.create_application_response.CreateApplicationResponse"
    ):
        """<p>Creates a new application. An application is the top-level organizational unit that supports IAM Identity Center integration.</p>

        Args:
            idc_instance_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center instance to associate with the application.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to associate with the application.</p>
            default_kms_key_id: <p>The identifier of the default AWS KMS key to use for encrypting data in the application.</p>
            tags: <p>The tags to associate with the application.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_securityagent.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_securityagent._operations.security_agent.create_application

            output, http_response = (
                capo_securityagent._operations.security_agent.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateApplication")
        )
        input_: capo_securityagent.types.create_application_request.CreateApplicationRequest = {}
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if default_kms_key_id is not None:
            input_["default_kms_key_id"] = default_kms_key_id
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
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.get_application_response.GetApplicationResponse":
        """<p>Retrieves information about an application.</p>

        Args:
            application_id: <p>The unique identifier of the application to retrieve.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse[
            "capo_securityagent.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_securityagent._operations.security_agent.get_application

            output, http_response = (
                capo_securityagent._operations.security_agent.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetApplication")
        )
        input_: capo_securityagent.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
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
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        role_arn: Optional["capo_securityagent.types.role_arn.RoleArn"] = None,
        default_kms_key_id: Optional[
            "capo_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
        ] = None,
    ) -> (
        "capo_securityagent.types.update_application_response.UpdateApplicationResponse"
    ):
        """<p>Updates the configuration of an existing application, including the IAM role and default KMS key.</p>

        Args:
            application_id: <p>The unique identifier of the application to update.</p>
            role_arn: <p>The updated Amazon Resource Name (ARN) of the IAM role for the application.</p>
            default_kms_key_id: <p>The updated identifier of the default AWS KMS key for the application.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "capo_securityagent.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_securityagent._operations.security_agent.update_application

            output, http_response = (
                capo_securityagent._operations.security_agent.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateApplication")
        )
        input_: capo_securityagent.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if default_kms_key_id is not None:
            input_["default_kms_key_id"] = default_kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[SecurityAgentClientConfig] = None,
    ) -> None:
        """<p>Deletes an application and its associated configuration, including IAM Identity Center settings.</p>

        Args:
            application_id: <p>The unique identifier of the application to delete.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[None]:
            import capo_securityagent._operations.security_agent.delete_application

            output, http_response = (
                capo_securityagent._operations.security_agent.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteApplication")
        )
        input_: capo_securityagent.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
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
        config_overrides: Optional[SecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_applications_response.ListApplicationsResponse":
        """<p>Returns a paginated list of application summaries in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securityagent.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_securityagent.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_securityagent._operations.security_agent.list_applications

            output, http_response = (
                capo_securityagent._operations.security_agent.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListApplications")
        )
        input_: capo_securityagent.types.list_applications_request.ListApplicationsRequest = {}
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


class AsyncApplicationResource:
    def __init__(self, service: AsyncSecurityAgentClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        idc_instance_arn: Optional[
            "capo_securityagent.types.id_c_instance_arn.IdCInstanceArn"
        ] = None,
        role_arn: Optional["capo_securityagent.types.role_arn.RoleArn"] = None,
        default_kms_key_id: Optional[
            "capo_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
        ] = None,
        tags: Optional["capo_securityagent.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_securityagent.types.create_application_response.CreateApplicationResponse"
    ):
        """<p>Creates a new application. An application is the top-level organizational unit that supports IAM Identity Center integration.</p>

        Args:
            idc_instance_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center instance to associate with the application.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to associate with the application.</p>
            default_kms_key_id: <p>The identifier of the default AWS KMS key to use for encrypting data in the application.</p>
            tags: <p>The tags to associate with the application.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_securityagent._operations.security_agent.create_application

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateApplication")
        )
        input_: capo_securityagent.types.create_application_request.CreateApplicationRequest = {}
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if default_kms_key_id is not None:
            input_["default_kms_key_id"] = default_kms_key_id
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
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> "capo_securityagent.types.get_application_response.GetApplicationResponse":
        """<p>Retrieves information about an application.</p>

        Args:
            application_id: <p>The unique identifier of the application to retrieve.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_securityagent._operations.security_agent.get_application

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetApplication")
        )
        input_: capo_securityagent.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
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
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        role_arn: Optional["capo_securityagent.types.role_arn.RoleArn"] = None,
        default_kms_key_id: Optional[
            "capo_securityagent.types.default_kms_key_id.DefaultKmsKeyId"
        ] = None,
    ) -> (
        "capo_securityagent.types.update_application_response.UpdateApplicationResponse"
    ):
        """<p>Updates the configuration of an existing application, including the IAM role and default KMS key.</p>

        Args:
            application_id: <p>The unique identifier of the application to update.</p>
            role_arn: <p>The updated Amazon Resource Name (ARN) of the IAM role for the application.</p>
            default_kms_key_id: <p>The updated identifier of the default AWS KMS key for the application.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_securityagent._operations.security_agent.update_application

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateApplication")
        )
        input_: capo_securityagent.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if default_kms_key_id is not None:
            input_["default_kms_key_id"] = default_kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        application_id: "capo_securityagent.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
    ) -> None:
        """<p>Deletes an application and its associated configuration, including IAM Identity Center settings.</p>

        Args:
            application_id: <p>The unique identifier of the application to delete.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_securityagent._operations.security_agent.delete_application

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteApplication")
        )
        input_: capo_securityagent.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
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
        config_overrides: Optional[AsyncSecurityAgentClientConfig] = None,
        next_token: Optional["capo_securityagent.types.next_token.NextToken"] = None,
        max_results: Optional["capo_securityagent.types.max_results.MaxResults"] = None,
    ) -> "capo_securityagent.types.list_applications_response.ListApplicationsResponse":
        """<p>Returns a paginated list of application summaries in your account.</p>

        Args:
            next_token: <p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_securityagent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securityagent.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_securityagent.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_securityagent._operations.security_agent.list_applications

            (
                output,
                http_response,
            ) = await capo_securityagent._operations.security_agent.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListApplications")
        )
        input_: capo_securityagent.types.list_applications_request.ListApplicationsRequest = {}
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
