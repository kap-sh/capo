from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
from capo_lambda._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda.types.allowed_publishers
    import capo_lambda.types.code_signing_config_arn
    import capo_lambda.types.code_signing_policies
    import capo_lambda.types.create_code_signing_config_request
    import capo_lambda.types.create_code_signing_config_response
    import capo_lambda.types.delete_code_signing_config_request
    import capo_lambda.types.delete_code_signing_config_response
    import capo_lambda.types.description
    import capo_lambda.types.get_code_signing_config_request
    import capo_lambda.types.get_code_signing_config_response
    import capo_lambda.types.list_code_signing_configs_request
    import capo_lambda.types.list_code_signing_configs_response
    import capo_lambda.types.list_functions_by_code_signing_config_request
    import capo_lambda.types.list_functions_by_code_signing_config_response
    import capo_lambda.types.max_list_items
    import capo_lambda.types.string
    import capo_lambda.types.tags
    import capo_lambda.types.update_code_signing_config_request
    import capo_lambda.types.update_code_signing_config_response
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class CodeSigningConfigResource:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def create(
        self,
        allowed_publishers: "capo_lambda.types.allowed_publishers.AllowedPublishers",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        code_signing_policies: Optional[
            "capo_lambda.types.code_signing_policies.CodeSigningPolicies"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
    ) -> "capo_lambda.types.create_code_signing_config_response.CreateCodeSigningConfigResponse":
        """<p>Creates a code signing configuration. A <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html">code signing configuration</a> defines a list of allowed signing profiles and defines the code-signing validation policy (action to be taken if deployment validation checks fail). </p>

        Args:
            description: <p>Descriptive name for this code signing configuration.</p>
            allowed_publishers: <p>Signing profiles for this code signing configuration.</p>
            code_signing_policies: <p>The code signing policies define the actions to take if the validation checks fail. </p>
            tags: <p>A list of tags to add to the code signing configuration.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_code_signing_config_request.CreateCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.create_code_signing_config_response.CreateCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_code_signing_config.create_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_code_signing_config_request.CreateCodeSigningConfigRequest = {
            "allowed_publishers": allowed_publishers
        }
        if description is not None:
            input_["description"] = description
        if code_signing_policies is not None:
            input_["code_signing_policies"] = code_signing_policies
        if tags is not None:
            input_["tags"] = tags

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
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_code_signing_configs_response.ListCodeSigningConfigsResponse":
        """<p>Returns a list of <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuring-codesigning.html">code signing configurations</a>. A request returns up to 10,000 configurations per call. You can use the <code>MaxItems</code> parameter to return fewer configurations per call. </p>

        Args:
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Maximum number of items to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_code_signing_configs_request.ListCodeSigningConfigsRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_code_signing_configs_response.ListCodeSigningConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_code_signing_configs

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_code_signing_configs.list_code_signing_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_code_signing_configs_request.ListCodeSigningConfigsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.delete_code_signing_config_response.DeleteCodeSigningConfigResponse":
        """<p>Deletes the code signing configuration. You can delete the code signing configuration only if no function is using it. </p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_code_signing_config_request.DeleteCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.delete_code_signing_config_response.DeleteCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_code_signing_config.delete_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_code_signing_config_request.DeleteCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_code_signing_config_response.GetCodeSigningConfigResponse":
        """<p>Returns information about the specified code signing configuration.</p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration. </p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_code_signing_config_request.GetCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_code_signing_config_response.GetCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_code_signing_config.get_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_code_signing_config_request.GetCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_functions_by_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_functions_by_code_signing_config_response.ListFunctionsByCodeSigningConfigResponse":
        """<p>List the functions that use the specified code signing configuration. You can use this method prior to deleting a code signing configuration, to verify that no functions are using it.</p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Maximum number of items to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_functions_by_code_signing_config_request.ListFunctionsByCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_functions_by_code_signing_config_response.ListFunctionsByCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_functions_by_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_functions_by_code_signing_config.list_functions_by_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_functions_by_code_signing_config_request.ListFunctionsByCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        allowed_publishers: Optional[
            "capo_lambda.types.allowed_publishers.AllowedPublishers"
        ] = None,
        code_signing_policies: Optional[
            "capo_lambda.types.code_signing_policies.CodeSigningPolicies"
        ] = None,
    ) -> "capo_lambda.types.update_code_signing_config_response.UpdateCodeSigningConfigResponse":
        """<p>Update the code signing configuration. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function. </p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>
            description: <p>Descriptive name for this code signing configuration.</p>
            allowed_publishers: <p>Signing profiles for this code signing configuration.</p>
            code_signing_policies: <p>The code signing policy.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_code_signing_config_request.UpdateCodeSigningConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.update_code_signing_config_response.UpdateCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_code_signing_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_code_signing_config.update_code_signing_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_code_signing_config_request.UpdateCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }
        if description is not None:
            input_["description"] = description
        if allowed_publishers is not None:
            input_["allowed_publishers"] = allowed_publishers
        if code_signing_policies is not None:
            input_["code_signing_policies"] = code_signing_policies

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCodeSigningConfigResource:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def create(
        self,
        allowed_publishers: "capo_lambda.types.allowed_publishers.AllowedPublishers",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        code_signing_policies: Optional[
            "capo_lambda.types.code_signing_policies.CodeSigningPolicies"
        ] = None,
        tags: Optional["capo_lambda.types.tags.Tags"] = None,
    ) -> "capo_lambda.types.create_code_signing_config_response.CreateCodeSigningConfigResponse":
        """<p>Creates a code signing configuration. A <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html">code signing configuration</a> defines a list of allowed signing profiles and defines the code-signing validation policy (action to be taken if deployment validation checks fail). </p>

        Args:
            description: <p>Descriptive name for this code signing configuration.</p>
            allowed_publishers: <p>Signing profiles for this code signing configuration.</p>
            code_signing_policies: <p>The code signing policies define the actions to take if the validation checks fail. </p>
            tags: <p>A list of tags to add to the code signing configuration.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.create_code_signing_config_request.CreateCodeSigningConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.create_code_signing_config_response.CreateCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_code_signing_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.create_code_signing_config.async_create_code_signing_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_code_signing_config_request.CreateCodeSigningConfigRequest = {
            "allowed_publishers": allowed_publishers
        }
        if description is not None:
            input_["description"] = description
        if code_signing_policies is not None:
            input_["code_signing_policies"] = code_signing_policies
        if tags is not None:
            input_["tags"] = tags

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
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_code_signing_configs_response.ListCodeSigningConfigsResponse":
        """<p>Returns a list of <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuring-codesigning.html">code signing configurations</a>. A request returns up to 10,000 configurations per call. You can use the <code>MaxItems</code> parameter to return fewer configurations per call. </p>

        Args:
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Maximum number of items to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_code_signing_configs_request.ListCodeSigningConfigsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_code_signing_configs_response.ListCodeSigningConfigsResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_code_signing_configs

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_code_signing_configs.async_list_code_signing_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_code_signing_configs_request.ListCodeSigningConfigsRequest = {}
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.delete_code_signing_config_response.DeleteCodeSigningConfigResponse":
        """<p>Deletes the code signing configuration. You can delete the code signing configuration only if no function is using it. </p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.delete_code_signing_config_request.DeleteCodeSigningConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.delete_code_signing_config_response.DeleteCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.delete_code_signing_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.delete_code_signing_config.async_delete_code_signing_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_code_signing_config_request.DeleteCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_code_signing_config_response.GetCodeSigningConfigResponse":
        """<p>Returns information about the specified code signing configuration.</p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration. </p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_code_signing_config_request.GetCodeSigningConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_code_signing_config_response.GetCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_code_signing_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_code_signing_config.async_get_code_signing_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_code_signing_config_request.GetCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_functions_by_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_functions_by_code_signing_config_response.ListFunctionsByCodeSigningConfigResponse":
        """<p>List the functions that use the specified code signing configuration. You can use this method prior to deleting a code signing configuration, to verify that no functions are using it.</p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Maximum number of items to return.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_functions_by_code_signing_config_request.ListFunctionsByCodeSigningConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_functions_by_code_signing_config_response.ListFunctionsByCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_functions_by_code_signing_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_functions_by_code_signing_config.async_list_functions_by_code_signing_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_functions_by_code_signing_config_request.ListFunctionsByCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_code_signing_config(
        self,
        code_signing_config_arn: "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        allowed_publishers: Optional[
            "capo_lambda.types.allowed_publishers.AllowedPublishers"
        ] = None,
        code_signing_policies: Optional[
            "capo_lambda.types.code_signing_policies.CodeSigningPolicies"
        ] = None,
    ) -> "capo_lambda.types.update_code_signing_config_response.UpdateCodeSigningConfigResponse":
        """<p>Update the code signing configuration. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function. </p>

        Args:
            code_signing_config_arn: <p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>
            description: <p>Descriptive name for this code signing configuration.</p>
            allowed_publishers: <p>Signing profiles for this code signing configuration.</p>
            code_signing_policies: <p>The code signing policy.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.update_code_signing_config_request.UpdateCodeSigningConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.update_code_signing_config_response.UpdateCodeSigningConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_code_signing_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.update_code_signing_config.async_update_code_signing_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_code_signing_config_request.UpdateCodeSigningConfigRequest = {
            "code_signing_config_arn": code_signing_config_arn
        }
        if description is not None:
            input_["description"] = description
        if allowed_publishers is not None:
            input_["allowed_publishers"] = allowed_publishers
        if code_signing_policies is not None:
            input_["code_signing_policies"] = code_signing_policies

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
