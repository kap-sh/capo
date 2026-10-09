"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CodeCatalyst``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_codecatalyst._auth._signers
import capo_codecatalyst._auth._sigv4
from capo_codecatalyst._auth._providers import (
    BearerTokenProvider,
    StaticBearerTokenProvider,
)
from capo_codecatalyst._auth._zapros_handler import AuthMiddleware
from capo_codecatalyst._pagination import resolve_path as _resolve_path
from capo_codecatalyst._resources.code_catalyst.access_token import AccessToken
from capo_codecatalyst._resources.code_catalyst.space import Space
from capo_codecatalyst._services._aws_config import aws_config
from capo_codecatalyst._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_codecatalyst.types.access_token_id
    import capo_codecatalyst.types.access_token_name
    import capo_codecatalyst.types.access_token_summary
    import capo_codecatalyst.types.client_token
    import capo_codecatalyst.types.create_access_token_request
    import capo_codecatalyst.types.create_access_token_response
    import capo_codecatalyst.types.create_dev_environment_request
    import capo_codecatalyst.types.create_dev_environment_response
    import capo_codecatalyst.types.create_project_request
    import capo_codecatalyst.types.create_project_response
    import capo_codecatalyst.types.create_source_repository_branch_request
    import capo_codecatalyst.types.create_source_repository_branch_response
    import capo_codecatalyst.types.create_source_repository_request
    import capo_codecatalyst.types.create_source_repository_response
    import capo_codecatalyst.types.delete_access_token_request
    import capo_codecatalyst.types.delete_access_token_response
    import capo_codecatalyst.types.delete_dev_environment_request
    import capo_codecatalyst.types.delete_dev_environment_response
    import capo_codecatalyst.types.delete_project_request
    import capo_codecatalyst.types.delete_project_response
    import capo_codecatalyst.types.delete_source_repository_request
    import capo_codecatalyst.types.delete_source_repository_response
    import capo_codecatalyst.types.delete_space_request
    import capo_codecatalyst.types.delete_space_response
    import capo_codecatalyst.types.dev_environment_session_configuration
    import capo_codecatalyst.types.dev_environment_session_summary
    import capo_codecatalyst.types.dev_environment_summary
    import capo_codecatalyst.types.event_log_entry
    import capo_codecatalyst.types.filters
    import capo_codecatalyst.types.get_dev_environment_request
    import capo_codecatalyst.types.get_dev_environment_response
    import capo_codecatalyst.types.get_project_request
    import capo_codecatalyst.types.get_project_response
    import capo_codecatalyst.types.get_source_repository_clone_urls_request
    import capo_codecatalyst.types.get_source_repository_clone_urls_response
    import capo_codecatalyst.types.get_source_repository_request
    import capo_codecatalyst.types.get_source_repository_response
    import capo_codecatalyst.types.get_space_request
    import capo_codecatalyst.types.get_space_response
    import capo_codecatalyst.types.get_subscription_request
    import capo_codecatalyst.types.get_subscription_response
    import capo_codecatalyst.types.get_user_details_request
    import capo_codecatalyst.types.get_user_details_response
    import capo_codecatalyst.types.get_workflow_request
    import capo_codecatalyst.types.get_workflow_response
    import capo_codecatalyst.types.get_workflow_run_request
    import capo_codecatalyst.types.get_workflow_run_response
    import capo_codecatalyst.types.ide_configuration_list
    import capo_codecatalyst.types.inactivity_timeout_minutes
    import capo_codecatalyst.types.instance_type
    import capo_codecatalyst.types.list_access_tokens_request
    import capo_codecatalyst.types.list_access_tokens_response
    import capo_codecatalyst.types.list_dev_environment_sessions_request
    import capo_codecatalyst.types.list_dev_environment_sessions_response
    import capo_codecatalyst.types.list_dev_environments_request
    import capo_codecatalyst.types.list_dev_environments_response
    import capo_codecatalyst.types.list_event_logs_request
    import capo_codecatalyst.types.list_event_logs_response
    import capo_codecatalyst.types.list_projects_request
    import capo_codecatalyst.types.list_projects_response
    import capo_codecatalyst.types.list_source_repositories_item
    import capo_codecatalyst.types.list_source_repositories_request
    import capo_codecatalyst.types.list_source_repositories_response
    import capo_codecatalyst.types.list_source_repository_branches_item
    import capo_codecatalyst.types.list_source_repository_branches_request
    import capo_codecatalyst.types.list_source_repository_branches_response
    import capo_codecatalyst.types.list_spaces_request
    import capo_codecatalyst.types.list_spaces_response
    import capo_codecatalyst.types.list_workflow_runs_request
    import capo_codecatalyst.types.list_workflow_runs_response
    import capo_codecatalyst.types.list_workflows_request
    import capo_codecatalyst.types.list_workflows_response
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.persistent_storage_configuration
    import capo_codecatalyst.types.project_description
    import capo_codecatalyst.types.project_display_name
    import capo_codecatalyst.types.project_list_filters
    import capo_codecatalyst.types.project_summary
    import capo_codecatalyst.types.repositories_input
    import capo_codecatalyst.types.source_repository_branch_string
    import capo_codecatalyst.types.source_repository_description_string
    import capo_codecatalyst.types.source_repository_name_string
    import capo_codecatalyst.types.space_description
    import capo_codecatalyst.types.space_summary
    import capo_codecatalyst.types.start_dev_environment_request
    import capo_codecatalyst.types.start_dev_environment_response
    import capo_codecatalyst.types.start_dev_environment_session_request
    import capo_codecatalyst.types.start_dev_environment_session_response
    import capo_codecatalyst.types.start_workflow_run_request
    import capo_codecatalyst.types.start_workflow_run_response
    import capo_codecatalyst.types.stop_dev_environment_request
    import capo_codecatalyst.types.stop_dev_environment_response
    import capo_codecatalyst.types.stop_dev_environment_session_request
    import capo_codecatalyst.types.stop_dev_environment_session_response
    import capo_codecatalyst.types.timestamp
    import capo_codecatalyst.types.update_dev_environment_request
    import capo_codecatalyst.types.update_dev_environment_response
    import capo_codecatalyst.types.update_project_request
    import capo_codecatalyst.types.update_project_response
    import capo_codecatalyst.types.update_space_request
    import capo_codecatalyst.types.update_space_response
    import capo_codecatalyst.types.uuid
    import capo_codecatalyst.types.verify_session_response
    import capo_codecatalyst.types.workflow_run_sort_criteria_list
    import capo_codecatalyst.types.workflow_run_summary
    import capo_codecatalyst.types.workflow_sort_criteria_list
    import capo_codecatalyst.types.workflow_summary


class CodeCatalystClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    region: str | None
    endpoint: str | None
    bearer_provider: BearerTokenProvider | None
    anonymous: bool | None


class CodeCatalystClient:
    """A client for the ``CodeCatalyst`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        bearer: Bearer token for authentication.
        bearer_provider: Provider that resolves bearer tokens. Takes precedence over ``bearer``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        region: str | None = None,
        endpoint: str | None = None,
        bearer: str | None = None,
        bearer_provider: BearerTokenProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if bearer is not None and bearer_provider is not None:
            warnings.warn(
                "Both bearer and bearer_provider given; provider takes precedence"
            )
        if bearer_provider is None and bearer is not None:
            bearer_provider = StaticBearerTokenProvider(bearer)
        self._config = CodeCatalystClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "region": region,
                "endpoint": endpoint,
                "bearer_provider": bearer_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.access_token = AccessToken(self)
        self.space = Space(self)

    def operation_options(
        self, config_overrides: Optional[CodeCatalystClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CodeCatalystClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            region=overrides.get("region", self._config.get("region")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            bearer_provider=overrides.get(
                "bearer_provider", self._config.get("bearer_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def get_user_details(
        self,
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        id: Optional[str] = None,
        user_name: Optional[str] = None,
    ) -> "capo_codecatalyst.types.get_user_details_response.GetUserDetailsResponse":
        """<p>Returns information about a user. </p>

        Args:
            id: <p>The system-generated unique ID of the user. </p>
            user_name: <p>The name of the user as displayed in Amazon CodeCatalyst.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.get_user_details_request.GetUserDetailsRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.get_user_details_response.GetUserDetailsResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_user_details

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.get_user_details.get_user_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.get_user_details_request.GetUserDetailsRequest = {}
        if id is not None:
            input_["id"] = id
        if user_name is not None:
            input_["user_name"] = user_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def verify_session(
        self, *, config_overrides: Optional[CodeCatalystClientConfig] = None
    ) -> "capo_codecatalyst.types.verify_session_response.VerifySessionResponse":
        """<p>Verifies whether the calling user has a valid Amazon CodeCatalyst login and session. If successful, this returns the ID of the user in Amazon CodeCatalyst.</p>

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
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.verify_session_response.VerifySessionResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.verify_session

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.verify_session.verify_session(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_access_token(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def delete_access_token(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def list_access_tokens(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_access_tokens(
        self,
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_codecatalyst.types.access_token_summary.AccessTokenSummary]":
        _token = next_token
        while True:
            _response = self.list_access_tokens(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_space(
        self,
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.get_space_response.GetSpaceResponse":
        """<p>Returns information about an space.</p>

        Args:
            name: <p>The name of the space.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.get_space_request.GetSpaceRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.get_space_response.GetSpaceResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_space

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.get_space.get_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.get_space_request.GetSpaceRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_space(
        self,
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        description: Optional[
            "capo_codecatalyst.types.space_description.SpaceDescription"
        ] = None,
    ) -> "capo_codecatalyst.types.update_space_response.UpdateSpaceResponse":
        """<p>Changes one or more values for a space.</p>

        Args:
            name: <p>The name of the space.</p>
            description: <p>The description of the space.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.update_space_request.UpdateSpaceRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.update_space_response.UpdateSpaceResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.update_space

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.update_space.update_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.update_space_request.UpdateSpaceRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_space(
        self,
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.delete_space_response.DeleteSpaceResponse":
        """<p>Deletes a space.</p> <important> <p>Deleting a space cannot be undone. Additionally, since space names must be unique across Amazon CodeCatalyst, you cannot reuse names of deleted spaces.</p> </important>

        Args:
            name: <p>The name of the space. To retrieve a list of space names, use <a>ListSpaces</a>.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.delete_space_request.DeleteSpaceRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.delete_space_response.DeleteSpaceResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.delete_space

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.delete_space.delete_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.delete_space_request.DeleteSpaceRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_spaces(
        self,
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "capo_codecatalyst.types.list_spaces_response.ListSpacesResponse":
        """<p>Retrieves a list of spaces.</p>

        Args:
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
            req: "OperationRequest[capo_codecatalyst.types.list_spaces_request.ListSpacesRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_spaces_response.ListSpacesResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_spaces

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_spaces.list_spaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_spaces_request.ListSpacesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_spaces(
        self,
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_codecatalyst.types.space_summary.SpaceSummary]":
        _token = next_token
        while True:
            _response = self.list_spaces(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_dev_environments(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        project_name: Optional["capo_codecatalyst.types.name_string.NameString"] = None,
        filters: Optional["capo_codecatalyst.types.filters.Filters"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_codecatalyst.types.list_dev_environments_response.ListDevEnvironmentsResponse":
        """<p>Retrieves a list of Dev Environments in a project.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            filters: <p>Information about filters to apply to narrow the results returned in the list.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.list_dev_environments_request.ListDevEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_dev_environments_response.ListDevEnvironmentsResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_dev_environments

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_dev_environments.list_dev_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_dev_environments_request.ListDevEnvironmentsRequest = {
            "space_name": space_name
        }
        if project_name is not None:
            input_["project_name"] = project_name
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_dev_environments(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        project_name: Optional["capo_codecatalyst.types.name_string.NameString"] = None,
        filters: Optional["capo_codecatalyst.types.filters.Filters"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_codecatalyst.types.dev_environment_summary.DevEnvironmentSummary]":
        _token = next_token
        while True:
            _response = self.list_dev_environments(
                space_name,
                config_overrides=config_overrides,
                project_name=project_name,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_logs(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        start_time: "capo_codecatalyst.types.timestamp.Timestamp",
        end_time: "capo_codecatalyst.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        event_name: Optional[str] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_codecatalyst.types.list_event_logs_response.ListEventLogsResponse":
        """<p>Retrieves a list of events that occurred during a specific time in a space. You can use these events to audit user and system activity in a space. For more information, see <a href="https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa-monitoring.html">Monitoring</a> in the <i>Amazon CodeCatalyst User Guide</i>.</p> <note> <p>ListEventLogs guarantees events for the last 30 days in a given space. You can also view and retrieve a list of management events over the last 90 days for Amazon CodeCatalyst in the CloudTrail console by viewing Event history, or by creating a trail to create and maintain a record of events that extends past 90 days. For more information, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html">Working with CloudTrail Event History</a> and <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-getting-started.html">Working with CloudTrail trails</a>.</p> </note>

        Args:
            space_name: <p>The name of the space.</p>
            start_time: <p>The date and time when you want to start retrieving events, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>
            end_time: <p>The time after which you do not want any events retrieved, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>
            event_name: <p>The name of the event.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.list_event_logs_request.ListEventLogsRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_event_logs_response.ListEventLogsResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_event_logs

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_event_logs.list_event_logs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_event_logs_request.ListEventLogsRequest = {
            "space_name": space_name,
            "start_time": start_time,
            "end_time": end_time,
        }
        if event_name is not None:
            input_["event_name"] = event_name
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

    def iter_list_event_logs(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        start_time: "capo_codecatalyst.types.timestamp.Timestamp",
        end_time: "capo_codecatalyst.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        event_name: Optional[str] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_codecatalyst.types.event_log_entry.EventLogEntry]":
        _token = next_token
        while True:
            _response = self.list_event_logs(
                space_name,
                start_time,
                end_time,
                config_overrides=config_overrides,
                event_name=event_name,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_project(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        display_name: "capo_codecatalyst.types.project_display_name.ProjectDisplayName",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        description: Optional[
            "capo_codecatalyst.types.project_description.ProjectDescription"
        ] = None,
    ) -> "capo_codecatalyst.types.create_project_response.CreateProjectResponse":
        """<p>Creates a project in a specified space.</p>

        Args:
            space_name: <p>The name of the space.</p>
            display_name: <p>The friendly name of the project that will be displayed to users.</p>
            description: <p>The description of the project. This description will be displayed to all users of the project. We recommend providing a brief description of the project and its intended purpose.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.create_project_request.CreateProjectRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.create_project_response.CreateProjectResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.create_project

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.create_project.create_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.create_project_request.CreateProjectRequest = {
            "space_name": space_name,
            "display_name": display_name,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_project(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.get_project_response.GetProjectResponse":
        """<p>Returns information about a project.</p>

        Args:
            space_name: <p>The name of the space.</p>
            name: <p>The name of the project in the space.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.get_project_request.GetProjectRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.get_project_response.GetProjectResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_project

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.get_project.get_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.get_project_request.GetProjectRequest = {
            "space_name": space_name,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_project(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        description: Optional[
            "capo_codecatalyst.types.project_description.ProjectDescription"
        ] = None,
    ) -> "capo_codecatalyst.types.update_project_response.UpdateProjectResponse":
        """<p>Changes one or more values for a project.</p>

        Args:
            space_name: <p>The name of the space.</p>
            name: <p>The name of the project.</p>
            description: <p>The description of the project.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.update_project_request.UpdateProjectRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.update_project_response.UpdateProjectResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.update_project

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.update_project.update_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.update_project_request.UpdateProjectRequest = {
            "space_name": space_name,
            "name": name,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_project(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.delete_project_response.DeleteProjectResponse":
        """<p>Deletes a project in a space.</p>

        Args:
            space_name: <p>The name of the space.</p>
            name: <p>The name of the project in the space. To retrieve a list of project names, use <a>ListProjects</a>.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.delete_project_request.DeleteProjectRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.delete_project_response.DeleteProjectResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.delete_project

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.delete_project.delete_project(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.delete_project_request.DeleteProjectRequest = {
            "space_name": space_name,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_projects(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "capo_codecatalyst.types.project_list_filters.ProjectListFilters"
        ] = None,
    ) -> "capo_codecatalyst.types.list_projects_response.ListProjectsResponse":
        """<p>Retrieves a list of projects.</p>

        Args:
            space_name: <p>The name of the space.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>
            filters: <p>Information about filters to apply to narrow the results returned in the list.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.list_projects_request.ListProjectsRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_projects_response.ListProjectsResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_projects

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_projects.list_projects(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_projects_request.ListProjectsRequest = {
            "space_name": space_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_projects(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "capo_codecatalyst.types.project_list_filters.ProjectListFilters"
        ] = None,
    ) -> "Iterator[capo_codecatalyst.types.project_summary.ProjectSummary]":
        _token = next_token
        while True:
            _response = self.list_projects(
                space_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filters=filters,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_dev_environment(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        instance_type: "capo_codecatalyst.types.instance_type.InstanceType",
        persistent_storage: "capo_codecatalyst.types.persistent_storage_configuration.PersistentStorageConfiguration",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        repositories: Optional[
            "capo_codecatalyst.types.repositories_input.RepositoriesInput"
        ] = None,
        client_token: Optional[
            "capo_codecatalyst.types.client_token.ClientToken"
        ] = None,
        alias: Optional[str] = None,
        ides: Optional[
            "capo_codecatalyst.types.ide_configuration_list.IdeConfigurationList"
        ] = None,
        inactivity_timeout_minutes: Optional[
            "capo_codecatalyst.types.inactivity_timeout_minutes.InactivityTimeoutMinutes"
        ] = None,
        vpc_connection_name: Optional[
            "capo_codecatalyst.types.name_string.NameString"
        ] = None,
    ) -> "capo_codecatalyst.types.create_dev_environment_response.CreateDevEnvironmentResponse":
        """<p>Creates a Dev Environment in Amazon CodeCatalyst, a cloud-based development environment that you can use to quickly work on the code stored in the source repositories of your project. </p> <note> <p>When created in the Amazon CodeCatalyst console, by default a Dev Environment is configured to have a 2 core processor, 4GB of RAM, and 16GB of persistent storage. None of these defaults apply to a Dev Environment created programmatically.</p> </note>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            repositories: <p>The source repository that contains the branch to clone into the Dev Environment. </p>
            client_token: <p>A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.</p>
            alias: <p>The user-defined alias for a Dev Environment.</p>
            ides: <p>Information about the integrated development environment (IDE) configured for a Dev Environment.</p> <note> <p>An IDE is required to create a Dev Environment. For Dev Environment creation, this field contains configuration information and must be provided. </p> </note>
            instance_type: <p>The Amazon EC2 instace type to use for the Dev Environment. </p>
            inactivity_timeout_minutes: <p>The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Only whole integers are allowed. Dev Environments consume compute minutes when running.</p>
            persistent_storage: <p>Information about the amount of storage allocated to the Dev Environment. </p> <note> <p>By default, a Dev Environment is configured to have 16GB of persistent storage when created from the Amazon CodeCatalyst console, but there is no default when programmatically creating a Dev Environment. Valid values for persistent storage are based on memory sizes in 16GB increments. Valid values are 16, 32, and 64.</p> </note>
            vpc_connection_name: <p>The name of the connection that will be used to connect to Amazon VPC, if any.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.create_dev_environment_request.CreateDevEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.create_dev_environment_response.CreateDevEnvironmentResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.create_dev_environment

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.create_dev_environment.create_dev_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.create_dev_environment_request.CreateDevEnvironmentRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "instance_type": instance_type,
            "persistent_storage": persistent_storage,
        }
        if repositories is not None:
            input_["repositories"] = repositories
        if client_token is not None:
            input_["client_token"] = client_token
        if alias is not None:
            input_["alias"] = alias
        if ides is not None:
            input_["ides"] = ides
        if inactivity_timeout_minutes is not None:
            input_["inactivity_timeout_minutes"] = inactivity_timeout_minutes
        if vpc_connection_name is not None:
            input_["vpc_connection_name"] = vpc_connection_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_dev_environment(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        id: "capo_codecatalyst.types.uuid.Uuid",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> (
        "capo_codecatalyst.types.get_dev_environment_response.GetDevEnvironmentResponse"
    ):
        """<p>Returns information about a Dev Environment for a source repository in a project. Dev Environments are specific to the user who creates them.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            id: <p>The system-generated unique ID of the Dev Environment for which you want to view information. To retrieve a list of Dev Environment IDs, use <a>ListDevEnvironments</a>.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.get_dev_environment_request.GetDevEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.get_dev_environment_response.GetDevEnvironmentResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_dev_environment

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.get_dev_environment.get_dev_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.get_dev_environment_request.GetDevEnvironmentRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_dev_environment(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        id: "capo_codecatalyst.types.uuid.Uuid",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        alias: Optional[str] = None,
        ides: Optional[
            "capo_codecatalyst.types.ide_configuration_list.IdeConfigurationList"
        ] = None,
        instance_type: Optional[
            "capo_codecatalyst.types.instance_type.InstanceType"
        ] = None,
        inactivity_timeout_minutes: Optional[
            "capo_codecatalyst.types.inactivity_timeout_minutes.InactivityTimeoutMinutes"
        ] = None,
        client_token: Optional[
            "capo_codecatalyst.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_codecatalyst.types.update_dev_environment_response.UpdateDevEnvironmentResponse":
        """<p>Changes one or more values for a Dev Environment. Updating certain values of the Dev Environment will cause a restart.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            id: <p>The system-generated unique ID of the Dev Environment. </p>
            alias: <p>The user-specified alias for the Dev Environment. Changing this value will not cause a restart.</p>
            ides: <p>Information about the integrated development environment (IDE) configured for a Dev Environment.</p>
            instance_type: <p>The Amazon EC2 instace type to use for the Dev Environment. </p> <note> <p>Changing this value will cause a restart of the Dev Environment if it is running.</p> </note>
            inactivity_timeout_minutes: <p>The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Only whole integers are allowed. Dev Environments consume compute minutes when running.</p> <note> <p>Changing this value will cause a restart of the Dev Environment if it is running.</p> </note>
            client_token: <p>A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.update_dev_environment_request.UpdateDevEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.update_dev_environment_response.UpdateDevEnvironmentResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.update_dev_environment

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.update_dev_environment.update_dev_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.update_dev_environment_request.UpdateDevEnvironmentRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "id": id,
        }
        if alias is not None:
            input_["alias"] = alias
        if ides is not None:
            input_["ides"] = ides
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if inactivity_timeout_minutes is not None:
            input_["inactivity_timeout_minutes"] = inactivity_timeout_minutes
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_dev_environment(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        id: "capo_codecatalyst.types.uuid.Uuid",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.delete_dev_environment_response.DeleteDevEnvironmentResponse":
        """<p>Deletes a Dev Environment. </p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            id: <p>The system-generated unique ID of the Dev Environment you want to delete. To retrieve a list of Dev Environment IDs, use <a>ListDevEnvironments</a>.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.delete_dev_environment_request.DeleteDevEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.delete_dev_environment_response.DeleteDevEnvironmentResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.delete_dev_environment

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.delete_dev_environment.delete_dev_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.delete_dev_environment_request.DeleteDevEnvironmentRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_dev_environment_sessions(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        dev_environment_id: "capo_codecatalyst.types.uuid.Uuid",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_codecatalyst.types.list_dev_environment_sessions_response.ListDevEnvironmentSessionsResponse":
        """<p>Retrieves a list of active sessions for a Dev Environment in a project.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            dev_environment_id: <p>The system-generated unique ID of the Dev Environment.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.list_dev_environment_sessions_request.ListDevEnvironmentSessionsRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_dev_environment_sessions_response.ListDevEnvironmentSessionsResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_dev_environment_sessions

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_dev_environment_sessions.list_dev_environment_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_dev_environment_sessions_request.ListDevEnvironmentSessionsRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "dev_environment_id": dev_environment_id,
        }
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

    def iter_list_dev_environment_sessions(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        dev_environment_id: "capo_codecatalyst.types.uuid.Uuid",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_codecatalyst.types.dev_environment_session_summary.DevEnvironmentSessionSummary]":
        _token = next_token
        while True:
            _response = self.list_dev_environment_sessions(
                space_name,
                project_name,
                dev_environment_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_dev_environment(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        id: "capo_codecatalyst.types.uuid.Uuid",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        ides: Optional[
            "capo_codecatalyst.types.ide_configuration_list.IdeConfigurationList"
        ] = None,
        instance_type: Optional[
            "capo_codecatalyst.types.instance_type.InstanceType"
        ] = None,
        inactivity_timeout_minutes: Optional[
            "capo_codecatalyst.types.inactivity_timeout_minutes.InactivityTimeoutMinutes"
        ] = None,
    ) -> "capo_codecatalyst.types.start_dev_environment_response.StartDevEnvironmentResponse":
        """<p>Starts a specified Dev Environment and puts it into an active state. </p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            id: <p>The system-generated unique ID of the Dev Environment. </p>
            ides: <p>Information about the integrated development environment (IDE) configured for a Dev Environment. </p>
            instance_type: <p>The Amazon EC2 instace type to use for the Dev Environment. </p>
            inactivity_timeout_minutes: <p>The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Only whole integers are allowed. Dev Environments consume compute minutes when running.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.start_dev_environment_request.StartDevEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.start_dev_environment_response.StartDevEnvironmentResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.start_dev_environment

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.start_dev_environment.start_dev_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.start_dev_environment_request.StartDevEnvironmentRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "id": id,
        }
        if ides is not None:
            input_["ides"] = ides
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if inactivity_timeout_minutes is not None:
            input_["inactivity_timeout_minutes"] = inactivity_timeout_minutes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_dev_environment_session(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        id: "capo_codecatalyst.types.uuid.Uuid",
        session_configuration: "capo_codecatalyst.types.dev_environment_session_configuration.DevEnvironmentSessionConfiguration",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.start_dev_environment_session_response.StartDevEnvironmentSessionResponse":
        """<p>Starts a session for a specified Dev Environment.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            id: <p>The system-generated unique ID of the Dev Environment.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.start_dev_environment_session_request.StartDevEnvironmentSessionRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.start_dev_environment_session_response.StartDevEnvironmentSessionResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.start_dev_environment_session

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.start_dev_environment_session.start_dev_environment_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.start_dev_environment_session_request.StartDevEnvironmentSessionRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "id": id,
            "session_configuration": session_configuration,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_dev_environment(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        id: "capo_codecatalyst.types.uuid.Uuid",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.stop_dev_environment_response.StopDevEnvironmentResponse":
        """<p>Pauses a specified Dev Environment and places it in a non-running state. Stopped Dev Environments do not consume compute minutes.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            id: <p>The system-generated unique ID of the Dev Environment. </p>

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
            req: "OperationRequest[capo_codecatalyst.types.stop_dev_environment_request.StopDevEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.stop_dev_environment_response.StopDevEnvironmentResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.stop_dev_environment

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.stop_dev_environment.stop_dev_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.stop_dev_environment_request.StopDevEnvironmentRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_dev_environment_session(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        id: "capo_codecatalyst.types.uuid.Uuid",
        session_id: str,
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.stop_dev_environment_session_response.StopDevEnvironmentSessionResponse":
        """<p>Stops a session for a specified Dev Environment.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            id: <p>The system-generated unique ID of the Dev Environment. To obtain this ID, use <a>ListDevEnvironments</a>.</p>
            session_id: <p>The system-generated unique ID of the Dev Environment session. This ID is returned by <a>StartDevEnvironmentSession</a>.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.stop_dev_environment_session_request.StopDevEnvironmentSessionRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.stop_dev_environment_session_response.StopDevEnvironmentSessionResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.stop_dev_environment_session

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.stop_dev_environment_session.stop_dev_environment_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.stop_dev_environment_session_request.StopDevEnvironmentSessionRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "id": id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_source_repository(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        description: Optional[
            "capo_codecatalyst.types.source_repository_description_string.SourceRepositoryDescriptionString"
        ] = None,
    ) -> "capo_codecatalyst.types.create_source_repository_response.CreateSourceRepositoryResponse":
        """<p>Creates an empty Git-based source repository in a specified project. The repository is created with an initial empty commit with a default branch named <code>main</code>.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            name: <p>The name of the source repository. For more information about name requirements, see <a href="https://docs.aws.amazon.com/codecatalyst/latest/userguide/source-quotas.html">Quotas for source repositories</a>.</p>
            description: <p>The description of the source repository.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.create_source_repository_request.CreateSourceRepositoryRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.create_source_repository_response.CreateSourceRepositoryResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.create_source_repository

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.create_source_repository.create_source_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.create_source_repository_request.CreateSourceRepositoryRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "name": name,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_source_repository(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.get_source_repository_response.GetSourceRepositoryResponse":
        """<p>Returns information about a source repository.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            name: <p>The name of the source repository.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.get_source_repository_request.GetSourceRepositoryRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.get_source_repository_response.GetSourceRepositoryResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_source_repository

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.get_source_repository.get_source_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.get_source_repository_request.GetSourceRepositoryRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_source_repository(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.delete_source_repository_response.DeleteSourceRepositoryResponse":
        """<p>Deletes a source repository in Amazon CodeCatalyst. You cannot use this API to delete a linked repository. It can only be used to delete a Amazon CodeCatalyst source repository.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            name: <p>The name of the source repository.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.delete_source_repository_request.DeleteSourceRepositoryRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.delete_source_repository_response.DeleteSourceRepositoryResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.delete_source_repository

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.delete_source_repository.delete_source_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.delete_source_repository_request.DeleteSourceRepositoryRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "name": name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_source_repositories(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_codecatalyst.types.list_source_repositories_response.ListSourceRepositoriesResponse":
        """<p>Retrieves a list of source repositories in a project.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.list_source_repositories_request.ListSourceRepositoriesRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_source_repositories_response.ListSourceRepositoriesResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_source_repositories

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_source_repositories.list_source_repositories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_source_repositories_request.ListSourceRepositoriesRequest = {
            "space_name": space_name,
            "project_name": project_name,
        }
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

    def iter_list_source_repositories(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_codecatalyst.types.list_source_repositories_item.ListSourceRepositoriesItem]":
        _token = next_token
        while True:
            _response = self.list_source_repositories(
                space_name,
                project_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_source_repository_clone_urls(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        source_repository_name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.get_source_repository_clone_urls_response.GetSourceRepositoryCloneUrlsResponse":
        """<p>Returns information about the URLs that can be used with a Git client to clone a source repository.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            source_repository_name: <p>The name of the source repository.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.get_source_repository_clone_urls_request.GetSourceRepositoryCloneUrlsRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.get_source_repository_clone_urls_response.GetSourceRepositoryCloneUrlsResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_source_repository_clone_urls

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.get_source_repository_clone_urls.get_source_repository_clone_urls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.get_source_repository_clone_urls_request.GetSourceRepositoryCloneUrlsRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "source_repository_name": source_repository_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_source_repository_branch(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        source_repository_name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString",
        name: "capo_codecatalyst.types.source_repository_branch_string.SourceRepositoryBranchString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        head_commit_id: Optional[str] = None,
    ) -> "capo_codecatalyst.types.create_source_repository_branch_response.CreateSourceRepositoryBranchResponse":
        """<p>Creates a branch in a specified source repository in Amazon CodeCatalyst. </p> <note> <p>This API only creates a branch in a source repository hosted in Amazon CodeCatalyst. You cannot use this API to create a branch in a linked repository.</p> </note>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            source_repository_name: <p>The name of the repository where you want to create a branch.</p>
            name: <p>The name for the branch you're creating.</p>
            head_commit_id: <p>The commit ID in an existing branch from which you want to create the new branch.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.create_source_repository_branch_request.CreateSourceRepositoryBranchRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.create_source_repository_branch_response.CreateSourceRepositoryBranchResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.create_source_repository_branch

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.create_source_repository_branch.create_source_repository_branch(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.create_source_repository_branch_request.CreateSourceRepositoryBranchRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "source_repository_name": source_repository_name,
            "name": name,
        }
        if head_commit_id is not None:
            input_["head_commit_id"] = head_commit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_source_repository_branches(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        source_repository_name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_codecatalyst.types.list_source_repository_branches_response.ListSourceRepositoryBranchesResponse":
        """<p>Retrieves a list of branches in a specified source repository.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            source_repository_name: <p>The name of the source repository.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.list_source_repository_branches_request.ListSourceRepositoryBranchesRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_source_repository_branches_response.ListSourceRepositoryBranchesResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_source_repository_branches

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_source_repository_branches.list_source_repository_branches(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_source_repository_branches_request.ListSourceRepositoryBranchesRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "source_repository_name": source_repository_name,
        }
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

    def iter_list_source_repository_branches(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        source_repository_name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_codecatalyst.types.list_source_repository_branches_item.ListSourceRepositoryBranchesItem]":
        _token = next_token
        while True:
            _response = self.list_source_repository_branches(
                space_name,
                project_name,
                source_repository_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_workflow(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        id: "capo_codecatalyst.types.uuid.Uuid",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.get_workflow_response.GetWorkflowResponse":
        """<p>Returns information about a workflow.</p>

        Args:
            space_name: <p>The name of the space.</p>
            id: <p>The ID of the workflow. To rerieve a list of workflow IDs, use <a>ListWorkflows</a>.</p>
            project_name: <p>The name of the project in the space.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.get_workflow_request.GetWorkflowRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.get_workflow_response.GetWorkflowResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_workflow

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.get_workflow.get_workflow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.get_workflow_request.GetWorkflowRequest = {
            "space_name": space_name,
            "id": id,
            "project_name": project_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workflows(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        sort_by: Optional[
            "capo_codecatalyst.types.workflow_sort_criteria_list.WorkflowSortCriteriaList"
        ] = None,
    ) -> "capo_codecatalyst.types.list_workflows_response.ListWorkflowsResponse":
        """<p>Retrieves a list of workflows in a specified project.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>
            sort_by: <p>Information used to sort the items in the returned list.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.list_workflows_request.ListWorkflowsRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_workflows_response.ListWorkflowsResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_workflows

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_workflows.list_workflows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_workflows_request.ListWorkflowsRequest = {
            "space_name": space_name,
            "project_name": project_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_workflows(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        sort_by: Optional[
            "capo_codecatalyst.types.workflow_sort_criteria_list.WorkflowSortCriteriaList"
        ] = None,
    ) -> "Iterator[capo_codecatalyst.types.workflow_summary.WorkflowSummary]":
        _token = next_token
        while True:
            _response = self.list_workflows(
                space_name,
                project_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                sort_by=sort_by,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_workflow_run(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        workflow_id: "capo_codecatalyst.types.uuid.Uuid",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_codecatalyst.types.start_workflow_run_response.StartWorkflowRunResponse":
        """<p>Begins a run of a specified workflow.</p>

        Args:
            space_name: <p>The name of the space.</p>
            project_name: <p>The name of the project in the space.</p>
            workflow_id: <p>The system-generated unique ID of the workflow. To retrieve a list of workflow IDs, use <a>ListWorkflows</a>.</p>
            client_token: <p>A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.start_workflow_run_request.StartWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.start_workflow_run_response.StartWorkflowRunResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.start_workflow_run

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.start_workflow_run.start_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.start_workflow_run_request.StartWorkflowRunRequest = {
            "space_name": space_name,
            "project_name": project_name,
            "workflow_id": workflow_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workflow_run(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        id: "capo_codecatalyst.types.uuid.Uuid",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.get_workflow_run_response.GetWorkflowRunResponse":
        """<p>Returns information about a specified run of a workflow.</p>

        Args:
            space_name: <p>The name of the space.</p>
            id: <p>The ID of the workflow run. To retrieve a list of workflow run IDs, use <a>ListWorkflowRuns</a>.</p>
            project_name: <p>The name of the project in the space.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_workflow_run

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.get_workflow_run.get_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.get_workflow_run_request.GetWorkflowRunRequest = {
            "space_name": space_name,
            "id": id,
            "project_name": project_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workflow_runs(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        workflow_id: Optional["capo_codecatalyst.types.uuid.Uuid"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        sort_by: Optional[
            "capo_codecatalyst.types.workflow_run_sort_criteria_list.WorkflowRunSortCriteriaList"
        ] = None,
    ) -> "capo_codecatalyst.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Retrieves a list of workflow runs of a specified workflow.</p>

        Args:
            space_name: <p>The name of the space.</p>
            workflow_id: <p>The ID of the workflow. To retrieve a list of workflow IDs, use <a>ListWorkflows</a>.</p>
            project_name: <p>The name of the project in the space.</p>
            next_token: <p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>
            max_results: <p>The maximum number of results to show in a single call to this API. If the number of results is larger than the number you specified, the response will include a <code>NextToken</code> element, which you can use to obtain additional results.</p>
            sort_by: <p>Information used to sort the items in the returned list.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.list_workflow_runs

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.list_workflow_runs.list_workflow_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.list_workflow_runs_request.ListWorkflowRunsRequest = {
            "space_name": space_name,
            "project_name": project_name,
        }
        if workflow_id is not None:
            input_["workflow_id"] = workflow_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_workflow_runs(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        project_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
        workflow_id: Optional["capo_codecatalyst.types.uuid.Uuid"] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        sort_by: Optional[
            "capo_codecatalyst.types.workflow_run_sort_criteria_list.WorkflowRunSortCriteriaList"
        ] = None,
    ) -> "Iterator[capo_codecatalyst.types.workflow_run_summary.WorkflowRunSummary]":
        _token = next_token
        while True:
            _response = self.list_workflow_runs(
                space_name,
                project_name,
                config_overrides=config_overrides,
                workflow_id=workflow_id,
                next_token=_token,
                max_results=max_results,
                sort_by=sort_by,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_subscription(
        self,
        space_name: "capo_codecatalyst.types.name_string.NameString",
        *,
        config_overrides: Optional[CodeCatalystClientConfig] = None,
    ) -> "capo_codecatalyst.types.get_subscription_response.GetSubscriptionResponse":
        """<p>Returns information about the Amazon Web Services account used for billing purposes and the billing plan for the space.</p>

        Args:
            space_name: <p>The name of the space.</p>

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
            req: "OperationRequest[capo_codecatalyst.types.get_subscription_request.GetSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_codecatalyst.types.get_subscription_response.GetSubscriptionResponse"
        ]:
            import capo_codecatalyst._operations.code_catalyst.get_subscription

            output, http_response = (
                capo_codecatalyst._operations.code_catalyst.get_subscription.get_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codecatalyst.types.get_subscription_request.GetSubscriptionRequest = {
            "space_name": space_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
