from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_codecatalyst._auth._signers
import capo_codecatalyst._auth._sigv4
from capo_codecatalyst._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_codecatalyst.types.access_token_id
    import capo_codecatalyst.types.access_token_name
    import capo_codecatalyst.types.access_token_summary
    import capo_codecatalyst.types.create_access_token_request
    import capo_codecatalyst.types.create_access_token_response
    import capo_codecatalyst.types.delete_access_token_request
    import capo_codecatalyst.types.delete_access_token_response
    import capo_codecatalyst.types.list_access_tokens_request
    import capo_codecatalyst.types.list_access_tokens_response
    import capo_codecatalyst.types.timestamp
    from capo_codecatalyst._services.async_code_catalyst import (
        AsyncCodeCatalystClient,
        AsyncCodeCatalystClientConfig,
    )
    from capo_codecatalyst._services.code_catalyst import (
        CodeCatalystClient,
        CodeCatalystClientConfig,
    )


class AccessToken:
    def __init__(self, service: CodeCatalystClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_codecatalyst.types.access_token_name.AccessTokenName",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        expires_time: Optional["capo_codecatalyst.types.timestamp.Timestamp"] = None,
    ) -> (
        "capo_codecatalyst.types.create_access_token_response.CreateAccessTokenResponse"
    ):
        """<p>Creates a personal access token (PAT) for the current user. A personal access token (PAT) is similar to a password. It is associated with your user identity for use across all spaces and projects in Amazon CodeCatalyst. You use PATs to access CodeCatalyst from resources that include integrated development environments (IDEs) and Git-based source repositories. PATs represent you in Amazon CodeCatalyst and you can manage them in your user settings.For more information, see <a href="https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-tokens-keys.html">Managing personal access tokens in Amazon CodeCatalyst</a>.</p>

        Args:
            name: <p>The friendly name of the personal access token.</p>
            expires_time: <p>The date and time the personal access token expires, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codecatalyst.types.create_access_token_request.CreateAccessTokenRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.create_access_token_response.CreateAccessTokenResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.create_access_token

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.create_access_token.create_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_codecatalyst.types.create_access_token_request.CreateAccessTokenRequest = {
            "name": name
        }
        if expires_time is not None:
            input_["expires_time"] = expires_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_codecatalyst.types.access_token_id.AccessTokenId",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> (
        "capo_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse"
    ):
        """<p>Deletes a specified personal access token (PAT). A personal access token can only be deleted by the user who created it.</p>

        Args:
            id: <p>The ID of the personal access token to delete. You can find the IDs of all PATs associated with your Amazon Web Services Builder ID in a space by calling <a>ListAccessTokens</a>.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.delete_access_token

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.delete_access_token.delete_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest = {
            "id": id
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
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_codecatalyst.types.list_access_tokens_response.ListAccessTokensResponse":
        """<p>Lists all personal access tokens (PATs) associated with the user who calls the API. You can only list PATs associated with your Amazon Web Services Builder ID.</p>

        Args:
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codecatalyst.types.list_access_tokens_request.ListAccessTokensRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_access_tokens_response.ListAccessTokensResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_access_tokens

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_access_tokens.list_access_tokens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_access_tokens_request.ListAccessTokensRequest = {}
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


class AsyncAccessToken:
    def __init__(self, service: AsyncCodeCatalystClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_codecatalyst.types.access_token_name.AccessTokenName",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        expires_time: Optional["capo_codecatalyst.types.timestamp.Timestamp"] = None,
    ) -> (
        "capo_codecatalyst.types.create_access_token_response.CreateAccessTokenResponse"
    ):
        """<p>Creates a personal access token (PAT) for the current user. A personal access token (PAT) is similar to a password. It is associated with your user identity for use across all spaces and projects in Amazon CodeCatalyst. You use PATs to access CodeCatalyst from resources that include integrated development environments (IDEs) and Git-based source repositories. PATs represent you in Amazon CodeCatalyst and you can manage them in your user settings.For more information, see <a href="https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-tokens-keys.html">Managing personal access tokens in Amazon CodeCatalyst</a>.</p>

        Args:
            name: <p>The friendly name of the personal access token.</p>
            expires_time: <p>The date and time the personal access token expires, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codecatalyst.types.create_access_token_request.CreateAccessTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_codecatalyst.types.create_access_token_response.CreateAccessTokenResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.create_access_token

            (
                output,
                http_response,
            ) = await capo_codecatalyst._operations.code_catalyst.create_access_token.async_create_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_codecatalyst.types.create_access_token_request.CreateAccessTokenRequest = {
            "name": name
        }
        if expires_time is not None:
            input_["expires_time"] = expires_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_codecatalyst.types.access_token_id.AccessTokenId",
        *,
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
    ) -> (
        "capo_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse"
    ):
        """<p>Deletes a specified personal access token (PAT). A personal access token can only be deleted by the user who created it.</p>

        Args:
            id: <p>The ID of the personal access token to delete. You can find the IDs of all PATs associated with your Amazon Web Services Builder ID in a space by calling <a>ListAccessTokens</a>.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_codecatalyst.types.delete_access_token_response.DeleteAccessTokenResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.delete_access_token

            (
                output,
                http_response,
            ) = await capo_codecatalyst._operations.code_catalyst.delete_access_token.async_delete_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_codecatalyst.types.delete_access_token_request.DeleteAccessTokenRequest = {
            "id": id
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
        config_overrides: Optional[AsyncCodeCatalystClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_codecatalyst.types.list_access_tokens_response.ListAccessTokensResponse":
        """<p>Lists all personal access tokens (PATs) associated with the user who calls the API. You can only list PATs associated with your Amazon Web Services Builder ID.</p>

        Args:
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>

        Raises:
            capo_codecatalyst.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.</p>
            capo_codecatalyst.errors.conflict_exception.ConflictException: <p>The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.</p>
            capo_codecatalyst.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.</p>
            capo_codecatalyst.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.</p>
            capo_codecatalyst.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codecatalyst.errors.validation_exception.ValidationException: <p>The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.</p>
            capo_codecatalyst.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codecatalyst.types.list_access_tokens_request.ListAccessTokensRequest]",
        ) -> AsyncOperationResponse[
            "capo_codecatalyst.types.list_access_tokens_response.ListAccessTokensResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_access_tokens

            (
                output,
                http_response,
            ) = await capo_codecatalyst._operations.code_catalyst.list_access_tokens.async_list_access_tokens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_access_tokens_request.ListAccessTokensRequest = {}
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
