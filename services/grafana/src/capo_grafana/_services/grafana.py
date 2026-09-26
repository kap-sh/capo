"""Generated from Smithy shape ``com.amazonaws.grafana#AWSGrafanaControlPlane``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_grafana._auth._signers
import capo_grafana._auth._sigv4
from capo_grafana._auth._identity import Credentials
from capo_grafana._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_grafana._auth._zapros_handler import AuthMiddleware
from capo_grafana._pagination import resolve_path as _resolve_path
from capo_grafana._resources.aws_grafana_control_plane.api_key import ApiKey
from capo_grafana._resources.aws_grafana_control_plane.authentication import (
    Authentication,
)
from capo_grafana._resources.aws_grafana_control_plane.configuration import (
    Configuration,
)
from capo_grafana._resources.aws_grafana_control_plane.license import License
from capo_grafana._resources.aws_grafana_control_plane.permission import Permission
from capo_grafana._resources.aws_grafana_control_plane.service_account import (
    ServiceAccount,
)
from capo_grafana._resources.aws_grafana_control_plane.service_account_token import (
    ServiceAccountToken,
)
from capo_grafana._resources.aws_grafana_control_plane.workspace import Workspace
from capo_grafana._services._aws_config import aws_config
from capo_grafana._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_grafana.types.account_access_type
    import capo_grafana.types.api_key_name
    import capo_grafana.types.associate_license_request
    import capo_grafana.types.associate_license_response
    import capo_grafana.types.authentication_providers
    import capo_grafana.types.client_token
    import capo_grafana.types.create_workspace_api_key_request
    import capo_grafana.types.create_workspace_api_key_response
    import capo_grafana.types.create_workspace_request
    import capo_grafana.types.create_workspace_response
    import capo_grafana.types.create_workspace_service_account_request
    import capo_grafana.types.create_workspace_service_account_response
    import capo_grafana.types.create_workspace_service_account_token_request
    import capo_grafana.types.create_workspace_service_account_token_response
    import capo_grafana.types.data_source_types_list
    import capo_grafana.types.delete_workspace_api_key_request
    import capo_grafana.types.delete_workspace_api_key_response
    import capo_grafana.types.delete_workspace_request
    import capo_grafana.types.delete_workspace_response
    import capo_grafana.types.delete_workspace_service_account_request
    import capo_grafana.types.delete_workspace_service_account_response
    import capo_grafana.types.delete_workspace_service_account_token_request
    import capo_grafana.types.delete_workspace_service_account_token_response
    import capo_grafana.types.describe_workspace_authentication_request
    import capo_grafana.types.describe_workspace_authentication_response
    import capo_grafana.types.describe_workspace_configuration_request
    import capo_grafana.types.describe_workspace_configuration_response
    import capo_grafana.types.describe_workspace_request
    import capo_grafana.types.describe_workspace_response
    import capo_grafana.types.description
    import capo_grafana.types.disassociate_license_request
    import capo_grafana.types.disassociate_license_response
    import capo_grafana.types.grafana_token
    import capo_grafana.types.grafana_version
    import capo_grafana.types.iam_role_arn
    import capo_grafana.types.ip_address_type
    import capo_grafana.types.kms_key_id
    import capo_grafana.types.license_type
    import capo_grafana.types.list_permissions_request
    import capo_grafana.types.list_permissions_response
    import capo_grafana.types.list_tags_for_resource_request
    import capo_grafana.types.list_tags_for_resource_response
    import capo_grafana.types.list_versions_request
    import capo_grafana.types.list_versions_response
    import capo_grafana.types.list_workspace_service_account_tokens_request
    import capo_grafana.types.list_workspace_service_account_tokens_response
    import capo_grafana.types.list_workspace_service_accounts_request
    import capo_grafana.types.list_workspace_service_accounts_response
    import capo_grafana.types.list_workspaces_request
    import capo_grafana.types.list_workspaces_response
    import capo_grafana.types.network_access_configuration
    import capo_grafana.types.notification_destinations_list
    import capo_grafana.types.organization_role_name
    import capo_grafana.types.organizational_unit_list
    import capo_grafana.types.overridable_configuration_json
    import capo_grafana.types.pagination_token
    import capo_grafana.types.permission_entry
    import capo_grafana.types.permission_type
    import capo_grafana.types.role
    import capo_grafana.types.saml_configuration
    import capo_grafana.types.service_account_name
    import capo_grafana.types.service_account_summary
    import capo_grafana.types.service_account_token_name
    import capo_grafana.types.service_account_token_summary
    import capo_grafana.types.sso_id
    import capo_grafana.types.stack_set_name
    import capo_grafana.types.tag_keys
    import capo_grafana.types.tag_map
    import capo_grafana.types.tag_resource_request
    import capo_grafana.types.tag_resource_response
    import capo_grafana.types.untag_resource_request
    import capo_grafana.types.untag_resource_response
    import capo_grafana.types.update_instruction_batch
    import capo_grafana.types.update_permissions_request
    import capo_grafana.types.update_permissions_response
    import capo_grafana.types.update_workspace_authentication_request
    import capo_grafana.types.update_workspace_authentication_response
    import capo_grafana.types.update_workspace_configuration_request
    import capo_grafana.types.update_workspace_configuration_response
    import capo_grafana.types.update_workspace_request
    import capo_grafana.types.update_workspace_response
    import capo_grafana.types.user_type
    import capo_grafana.types.vpc_configuration
    import capo_grafana.types.workspace_id
    import capo_grafana.types.workspace_name
    import capo_grafana.types.workspace_summary


class grafanaClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class grafanaClient:
    """A client for the ``grafana`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = grafanaClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.api_key = ApiKey(self)
        self.authentication = Authentication(self)
        self.configuration = Configuration(self)
        self.license = License(self)
        self.permission = Permission(self)
        self.service_account = ServiceAccount(self)
        self.service_account_token = ServiceAccountToken(self)
        self.workspace = Workspace(self)

    def operation_options(
        self, config_overrides: Optional[grafanaClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: grafanaClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> (
        "capo_grafana.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>The <code>ListTagsForResource</code> operation returns the tags that are associated with the Amazon Managed Service for Grafana resource specified by the <code>resourceArn</code>. Currently, the only resource that can be tagged is a workspace. </p>

        Args:
            resource_arn: <p>The ARN of the resource the list of tags are associated with.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_tags_for_resource

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_versions(
        self,
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
        workspace_id: Optional["capo_grafana.types.workspace_id.WorkspaceId"] = None,
    ) -> "capo_grafana.types.list_versions_response.ListVersionsResponse":
        """<p>Lists available versions of Grafana. These are available when calling <code>CreateWorkspace</code>. Optionally, include a workspace to list the versions to which it can be upgraded.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token to use when requesting the next set of results. You receive this token from a previous <code>ListVersions</code> operation.</p>
            workspace_id: <p>The ID of the workspace to list the available upgrade versions. If not included, lists all versions of Grafana that are supported for <code>CreateWorkspace</code>.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.list_versions_request.ListVersionsRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.list_versions_response.ListVersionsResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_versions

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.list_versions.list_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.list_versions_request.ListVersionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if workspace_id is not None:
            input_["workspace_id"] = workspace_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_versions(
        self,
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
        workspace_id: Optional["capo_grafana.types.workspace_id.WorkspaceId"] = None,
    ) -> "Iterator[capo_grafana.types.grafana_version.GrafanaVersion]":
        _token = next_token
        while True:
            _response = self.list_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                workspace_id=workspace_id,
            )
            _page = _resolve_path(_response, ("grafana_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_grafana.types.tag_map.TagMap",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.tag_resource_response.TagResourceResponse":
        """<p>The <code>TagResource</code> operation associates tags with an Amazon Managed Grafana resource. Currently, the only resource that can be tagged is workspaces. </p> <p>If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p>

        Args:
            resource_arn: <p>The ARN of the resource the tag is associated with.</p>
            tags: <p>The list of tag keys and values to associate with the resource. You can associate tag keys only, tags (key and values) only or a combination of tag keys and tags.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.tag_resource

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: str,
        tag_keys: "capo_grafana.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.untag_resource_response.UntagResourceResponse":
        """<p>The <code>UntagResource</code> operation removes the association of the tag with the Amazon Managed Grafana resource. </p>

        Args:
            resource_arn: <p>The ARN of the resource the tag association is removed from. </p>
            tag_keys: <p>The key values of the tag to be removed from the resource.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.untag_resource

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_workspace_api_key(
        self,
        key_name: "capo_grafana.types.api_key_name.ApiKeyName",
        key_role: str,
        seconds_to_live: int,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse":
        r"""<p>Creates a Grafana API key for the workspace. This key can be used to authenticate requests sent to the workspace's HTTP API. See <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html\">https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html</a> for available APIs and example requests.</p> <note> <p>In workspaces compatible with Grafana version 9 or above, use workspace service accounts instead of API keys. API keys will be removed in a future release.</p> </note>

        Args:
            key_name: <p>Specifies the name of the key. Keynames must be unique to the workspace.</p>
            key_role: <p>Specifies the permission level of the key.</p> <p> Valid values: <code>ADMIN</code>|<code>EDITOR</code>|<code>VIEWER</code> </p>
            seconds_to_live: <p>Specifies the time in seconds until the key expires. Keys can be valid for up to 30 days.</p>
            workspace_id: <p>The ID of the workspace to create an API key.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.create_workspace_api_key_request.CreateWorkspaceApiKeyRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.create_workspace_api_key_response.CreateWorkspaceApiKeyResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.create_workspace_api_key

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.create_workspace_api_key.create_workspace_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.create_workspace_api_key_request.CreateWorkspaceApiKeyRequest = {
            "key_name": key_name,
            "key_role": key_role,
            "seconds_to_live": seconds_to_live,
            "workspace_id": workspace_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workspace_api_key(
        self,
        key_name: "capo_grafana.types.api_key_name.ApiKeyName",
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.delete_workspace_api_key_response.DeleteWorkspaceApiKeyResponse":
        """<p>Deletes a Grafana API key for the workspace.</p> <note> <p>In workspaces compatible with Grafana version 9 or above, use workspace service accounts instead of API keys. API keys will be removed in a future release.</p> </note>

        Args:
            key_name: <p>The name of the API key to delete.</p>
            workspace_id: <p>The ID of the workspace to delete.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.delete_workspace_api_key_request.DeleteWorkspaceApiKeyRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.delete_workspace_api_key_response.DeleteWorkspaceApiKeyResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.delete_workspace_api_key

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.delete_workspace_api_key.delete_workspace_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.delete_workspace_api_key_request.DeleteWorkspaceApiKeyRequest = {
            "key_name": key_name,
            "workspace_id": workspace_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_workspace_authentication(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.describe_workspace_authentication_response.DescribeWorkspaceAuthenticationResponse":
        """<p>Displays information about the authentication methods used in one Amazon Managed Grafana workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to return authentication information about.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.describe_workspace_authentication_request.DescribeWorkspaceAuthenticationRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.describe_workspace_authentication_response.DescribeWorkspaceAuthenticationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.describe_workspace_authentication

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.describe_workspace_authentication.describe_workspace_authentication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.describe_workspace_authentication_request.DescribeWorkspaceAuthenticationRequest = {
            "workspace_id": workspace_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workspace_authentication(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        authentication_providers: "capo_grafana.types.authentication_providers.AuthenticationProviders",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        saml_configuration: Optional[
            "capo_grafana.types.saml_configuration.SamlConfiguration"
        ] = None,
    ) -> "capo_grafana.types.update_workspace_authentication_response.UpdateWorkspaceAuthenticationResponse":
        r"""<p>Use this operation to define the identity provider (IdP) that this workspace authenticates users from, using SAML. You can also map SAML assertion attributes to workspace user information and define which groups in the assertion attribute are to have the <code>Admin</code> and <code>Editor</code> roles in the workspace.</p> <note> <p>Changes to the authentication method for a workspace may take a few minutes to take effect.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace to update the authentication for.</p>
            authentication_providers: <p>Specifies whether this workspace uses SAML 2.0, IAM Identity Center, or both to authenticate users for using the Grafana console within a workspace. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html\">User authentication in Amazon Managed Grafana</a>.</p>
            saml_configuration: <p>If the workspace uses SAML, use this structure to map SAML assertion attributes to workspace user information and define which groups in the assertion attribute are to have the <code>Admin</code> and <code>Editor</code> roles in the workspace.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.update_workspace_authentication_request.UpdateWorkspaceAuthenticationRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.update_workspace_authentication_response.UpdateWorkspaceAuthenticationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.update_workspace_authentication

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.update_workspace_authentication.update_workspace_authentication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.update_workspace_authentication_request.UpdateWorkspaceAuthenticationRequest = {
            "workspace_id": workspace_id,
            "authentication_providers": authentication_providers,
        }
        if saml_configuration is not None:
            input_["saml_configuration"] = saml_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_workspace_configuration(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse":
        """<p>Gets the current configuration string for the given workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to get configuration information for.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.describe_workspace_configuration

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.describe_workspace_configuration.describe_workspace_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest = {
            "workspace_id": workspace_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workspace_configuration(
        self,
        configuration: "capo_grafana.types.overridable_configuration_json.OverridableConfigurationJson",
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        grafana_version: Optional[
            "capo_grafana.types.grafana_version.GrafanaVersion"
        ] = None,
    ) -> "capo_grafana.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse":
        r"""<p>Updates the configuration string for the given workspace</p>

        Args:
            configuration: <p>The new configuration string for the workspace. For more information about the format and configuration options available, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html\">Working in your Grafana workspace</a>.</p>
            workspace_id: <p>The ID of the workspace to update.</p>
            grafana_version: <p>Specifies the version of Grafana to support in the workspace. If not specified, keeps the current version of the workspace.</p> <p>Can only be used to upgrade (for example, from 8.4 to 9.4), not downgrade (for example, from 9.4 to 8.4).</p> <p>To know what versions are available to upgrade to for a specific workspace, see the <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html\">ListVersions</a> operation.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.update_workspace_configuration

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.update_workspace_configuration.update_workspace_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest = {
            "configuration": configuration,
            "workspace_id": workspace_id,
        }
        if grafana_version is not None:
            input_["grafana_version"] = grafana_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_license(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        license_type: "capo_grafana.types.license_type.LicenseType",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        grafana_token: Optional["capo_grafana.types.grafana_token.GrafanaToken"] = None,
    ) -> "capo_grafana.types.associate_license_response.AssociateLicenseResponse":
        r"""<p>Assigns a Grafana Enterprise license to a workspace. To upgrade, you must use <code>ENTERPRISE</code> for the <code>licenseType</code>, and pass in a valid Grafana Labs token for the <code>grafanaToken</code>. Upgrading to Grafana Enterprise incurs additional fees. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html\">Upgrade a workspace to Grafana Enterprise</a>.</p>

        Args:
            workspace_id: <p>The ID of the workspace to associate the license with.</p>
            license_type: <p>The type of license to associate with the workspace.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>
            grafana_token: <p>A token from Grafana Labs that ties your Amazon Web Services account with a Grafana Labs account. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise\">Link your account with Grafana Labs</a>.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.associate_license_request.AssociateLicenseRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.associate_license_response.AssociateLicenseResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.associate_license

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.associate_license.associate_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.associate_license_request.AssociateLicenseRequest = {
            "workspace_id": workspace_id,
            "license_type": license_type,
        }
        if grafana_token is not None:
            input_["grafana_token"] = grafana_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_license(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        license_type: "capo_grafana.types.license_type.LicenseType",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.disassociate_license_response.DisassociateLicenseResponse":
        """<p>Removes the Grafana Enterprise license from a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to remove the Grafana Enterprise license from.</p>
            license_type: <p>The type of license to remove from the workspace.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.disassociate_license_request.DisassociateLicenseRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.disassociate_license_response.DisassociateLicenseResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.disassociate_license

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.disassociate_license.disassociate_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.disassociate_license_request.DisassociateLicenseRequest = {
            "workspace_id": workspace_id,
            "license_type": license_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_permissions(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
        user_type: Optional["capo_grafana.types.user_type.UserType"] = None,
        user_id: Optional["capo_grafana.types.sso_id.SsoId"] = None,
        group_id: Optional["capo_grafana.types.sso_id.SsoId"] = None,
    ) -> "capo_grafana.types.list_permissions_response.ListPermissionsResponse":
        """<p>Lists the users and groups who have the Grafana <code>Admin</code> and <code>Editor</code> roles in this workspace. If you use this operation without specifying <code>userId</code> or <code>groupId</code>, the operation returns the roles of all users and groups. If you specify a <code>userId</code> or a <code>groupId</code>, only the roles for that user or group are returned. If you do this, you can specify only one <code>userId</code> or one <code>groupId</code>.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token to use when requesting the next set of results. You received this token from a previous <code>ListPermissions</code> operation.</p>
            user_type: <p>(Optional) If you specify <code>SSO_USER</code>, then only the permissions of IAM Identity Center users are returned. If you specify <code>SSO_GROUP</code>, only the permissions of IAM Identity Center groups are returned.</p>
            user_id: <p>(Optional) Limits the results to only the user that matches this ID.</p>
            group_id: <p>(Optional) Limits the results to only the group that matches this ID.</p>
            workspace_id: <p>The ID of the workspace to list permissions for. This parameter is required.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.list_permissions_request.ListPermissionsRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.list_permissions_response.ListPermissionsResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_permissions

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.list_permissions.list_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.list_permissions_request.ListPermissionsRequest = {
            "workspace_id": workspace_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if user_type is not None:
            input_["user_type"] = user_type
        if user_id is not None:
            input_["user_id"] = user_id
        if group_id is not None:
            input_["group_id"] = group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_permissions(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
        user_type: Optional["capo_grafana.types.user_type.UserType"] = None,
        user_id: Optional["capo_grafana.types.sso_id.SsoId"] = None,
        group_id: Optional["capo_grafana.types.sso_id.SsoId"] = None,
    ) -> "Iterator[capo_grafana.types.permission_entry.PermissionEntry]":
        _token = next_token
        while True:
            _response = self.list_permissions(
                workspace_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                user_type=user_type,
                user_id=user_id,
                group_id=group_id,
            )
            _page = _resolve_path(_response, ("permissions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_permissions(
        self,
        update_instruction_batch: "capo_grafana.types.update_instruction_batch.UpdateInstructionBatch",
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.update_permissions_response.UpdatePermissionsResponse":
        """<p>Updates which users in a workspace have the Grafana <code>Admin</code> or <code>Editor</code> roles.</p>

        Args:
            update_instruction_batch: <p>An array of structures that contain the permission updates to make.</p>
            workspace_id: <p>The ID of the workspace to update.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.update_permissions_request.UpdatePermissionsRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.update_permissions_response.UpdatePermissionsResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.update_permissions

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.update_permissions.update_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.update_permissions_request.UpdatePermissionsRequest = {
            "update_instruction_batch": update_instruction_batch,
            "workspace_id": workspace_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_workspace_service_account(
        self,
        name: "capo_grafana.types.service_account_name.ServiceAccountName",
        grafana_role: "capo_grafana.types.role.Role",
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.create_workspace_service_account_response.CreateWorkspaceServiceAccountResponse":
        r"""<p>Creates a service account for the workspace. A service account can be used to call Grafana HTTP APIs, and run automated workloads. After creating the service account with the correct <code>GrafanaRole</code> for your use case, use <code>CreateWorkspaceServiceAccountToken</code> to create a token that can be used to authenticate and authorize Grafana HTTP API calls.</p> <p>You can only create service accounts for workspaces that are compatible with Grafana version 9 and above.</p> <note> <p>For more information about service accounts, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html\">Service accounts</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> <p>For more information about the Grafana HTTP APIs, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html\">Using Grafana HTTP APIs</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>

        Args:
            name: <p>A name for the service account. The name must be unique within the workspace, as it determines the ID associated with the service account.</p>
            grafana_role: <p>The permission level to use for this service account.</p> <note> <p>For more information about the roles and the permissions each has, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-user-roles.html\">User roles</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>
            workspace_id: <p>The ID of the workspace within which to create the service account.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.create_workspace_service_account_request.CreateWorkspaceServiceAccountRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.create_workspace_service_account_response.CreateWorkspaceServiceAccountResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account.create_workspace_service_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.create_workspace_service_account_request.CreateWorkspaceServiceAccountRequest = {
            "name": name,
            "grafana_role": grafana_role,
            "workspace_id": workspace_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workspace_service_account(
        self,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.delete_workspace_service_account_response.DeleteWorkspaceServiceAccountResponse":
        """<p>Deletes a workspace service account from the workspace.</p> <p>This will delete any tokens created for the service account, as well. If the tokens are currently in use, the will fail to authenticate / authorize after they are deleted.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            service_account_id: <p>The ID of the service account to delete.</p>
            workspace_id: <p>The ID of the workspace where the service account resides.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.delete_workspace_service_account_request.DeleteWorkspaceServiceAccountRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.delete_workspace_service_account_response.DeleteWorkspaceServiceAccountResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account.delete_workspace_service_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.delete_workspace_service_account_request.DeleteWorkspaceServiceAccountRequest = {
            "service_account_id": service_account_id,
            "workspace_id": workspace_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workspace_service_accounts(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_grafana.types.list_workspace_service_accounts_response.ListWorkspaceServiceAccountsResponse":
        """<p>Returns a list of service accounts for a workspace.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            max_results: <p>The maximum number of service accounts to include in the results.</p>
            next_token: <p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccounts</code> operation.)</p>
            workspace_id: <p>The workspace for which to list service accounts.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.list_workspace_service_accounts_request.ListWorkspaceServiceAccountsRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.list_workspace_service_accounts_response.ListWorkspaceServiceAccountsResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_accounts

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_accounts.list_workspace_service_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.list_workspace_service_accounts_request.ListWorkspaceServiceAccountsRequest = {
            "workspace_id": workspace_id
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

    def iter_list_workspace_service_accounts(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_grafana.types.service_account_summary.ServiceAccountSummary]":
        _token = next_token
        while True:
            _response = self.list_workspace_service_accounts(
                workspace_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_workspace_service_account_token(
        self,
        name: "capo_grafana.types.service_account_token_name.ServiceAccountTokenName",
        seconds_to_live: int,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.create_workspace_service_account_token_response.CreateWorkspaceServiceAccountTokenResponse":
        r"""<p>Creates a token that can be used to authenticate and authorize Grafana HTTP API operations for the given <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html\">workspace service account</a>. The service account acts as a user for the API operations, and defines the permissions that are used by the API.</p> <important> <p>When you create the service account token, you will receive a key that is used when calling Grafana APIs. Do not lose this key, as it will not be retrievable again.</p> <p>If you do lose the key, you can delete the token and recreate it to receive a new key. This will disable the initial key.</p> </important> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            name: <p>A name for the token to create.</p>
            seconds_to_live: <p>Sets how long the token will be valid, in seconds. You can set the time up to 30 days in the future.</p>
            service_account_id: <p>The ID of the service account for which to create a token.</p>
            workspace_id: <p>The ID of the workspace the service account resides within.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.create_workspace_service_account_token_request.CreateWorkspaceServiceAccountTokenRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.create_workspace_service_account_token_response.CreateWorkspaceServiceAccountTokenResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account_token

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account_token.create_workspace_service_account_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.create_workspace_service_account_token_request.CreateWorkspaceServiceAccountTokenRequest = {
            "name": name,
            "seconds_to_live": seconds_to_live,
            "service_account_id": service_account_id,
            "workspace_id": workspace_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workspace_service_account_token(
        self,
        token_id: str,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.delete_workspace_service_account_token_response.DeleteWorkspaceServiceAccountTokenResponse":
        """<p>Deletes a token for the workspace service account.</p> <p>This will disable the key associated with the token. If any automation is currently using the key, it will no longer be authenticated or authorized to perform actions with the Grafana HTTP APIs.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            token_id: <p>The ID of the token to delete.</p>
            service_account_id: <p>The ID of the service account from which to delete the token.</p>
            workspace_id: <p>The ID of the workspace from which to delete the token.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.delete_workspace_service_account_token_request.DeleteWorkspaceServiceAccountTokenRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.delete_workspace_service_account_token_response.DeleteWorkspaceServiceAccountTokenResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account_token

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account_token.delete_workspace_service_account_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.delete_workspace_service_account_token_request.DeleteWorkspaceServiceAccountTokenRequest = {
            "token_id": token_id,
            "service_account_id": service_account_id,
            "workspace_id": workspace_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workspace_service_account_tokens(
        self,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_grafana.types.list_workspace_service_account_tokens_response.ListWorkspaceServiceAccountTokensResponse":
        """<p>Returns a list of tokens for a workspace service account.</p> <note> <p>This does not return the key for each token. You cannot access keys after they are created. To create a new key, delete the token and recreate it.</p> </note> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            max_results: <p>The maximum number of tokens to include in the results.</p>
            next_token: <p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccountTokens</code> operation.)</p>
            service_account_id: <p>The ID of the service account for which to return tokens.</p>
            workspace_id: <p>The ID of the workspace for which to return tokens.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.list_workspace_service_account_tokens_request.ListWorkspaceServiceAccountTokensRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.list_workspace_service_account_tokens_response.ListWorkspaceServiceAccountTokensResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_account_tokens

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_account_tokens.list_workspace_service_account_tokens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.list_workspace_service_account_tokens_request.ListWorkspaceServiceAccountTokensRequest = {
            "service_account_id": service_account_id,
            "workspace_id": workspace_id,
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

    def iter_list_workspace_service_account_tokens(
        self,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_grafana.types.service_account_token_summary.ServiceAccountTokenSummary]":
        _token = next_token
        while True:
            _response = self.list_workspace_service_account_tokens(
                service_account_id,
                workspace_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_account_tokens",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_workspace(
        self,
        account_access_type: "capo_grafana.types.account_access_type.AccountAccessType",
        permission_type: "capo_grafana.types.permission_type.PermissionType",
        authentication_providers: "capo_grafana.types.authentication_providers.AuthenticationProviders",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        client_token: Optional["capo_grafana.types.client_token.ClientToken"] = None,
        organization_role_name: Optional[
            "capo_grafana.types.organization_role_name.OrganizationRoleName"
        ] = None,
        stack_set_name: Optional[
            "capo_grafana.types.stack_set_name.StackSetName"
        ] = None,
        workspace_data_sources: Optional[
            "capo_grafana.types.data_source_types_list.DataSourceTypesList"
        ] = None,
        workspace_description: Optional[
            "capo_grafana.types.description.Description"
        ] = None,
        workspace_name: Optional[
            "capo_grafana.types.workspace_name.WorkspaceName"
        ] = None,
        workspace_notification_destinations: Optional[
            "capo_grafana.types.notification_destinations_list.NotificationDestinationsList"
        ] = None,
        workspace_organizational_units: Optional[
            "capo_grafana.types.organizational_unit_list.OrganizationalUnitList"
        ] = None,
        workspace_role_arn: Optional[
            "capo_grafana.types.iam_role_arn.IamRoleArn"
        ] = None,
        tags: Optional["capo_grafana.types.tag_map.TagMap"] = None,
        vpc_configuration: Optional[
            "capo_grafana.types.vpc_configuration.VpcConfiguration"
        ] = None,
        configuration: Optional[
            "capo_grafana.types.overridable_configuration_json.OverridableConfigurationJson"
        ] = None,
        network_access_control: Optional[
            "capo_grafana.types.network_access_configuration.NetworkAccessConfiguration"
        ] = None,
        grafana_version: Optional[
            "capo_grafana.types.grafana_version.GrafanaVersion"
        ] = None,
        ip_address_type: Optional[
            "capo_grafana.types.ip_address_type.IPAddressType"
        ] = None,
        kms_key_id: Optional["capo_grafana.types.kms_key_id.KmsKeyId"] = None,
    ) -> "capo_grafana.types.create_workspace_response.CreateWorkspaceResponse":
        r"""<p>Creates a <i>workspace</i>. In a workspace, you can create Grafana dashboards and visualizations to analyze your metrics, logs, and traces. You don't have to build, package, or deploy any hardware to run the Grafana server.</p> <p>Don't use <code>CreateWorkspace</code> to modify an existing workspace. Instead, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspace.html\">UpdateWorkspace</a>.</p>

        Args:
            account_access_type: <p>Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify <code>ORGANIZATION</code>, you must specify which organizational units the workspace can access in the <code>workspaceOrganizationalUnits</code> parameter.</p>
            client_token: <p>A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.</p>
            organization_role_name: <p>The name of an IAM role that already exists to use with Organizations to access Amazon Web Services data sources and notification channels in other accounts in an organization.</p>
            permission_type: <p>When creating a workspace through the Amazon Web Services API, CLI or Amazon Web Services CloudFormation, you must manage IAM roles and provision the permissions that the workspace needs to use Amazon Web Services data sources and notification channels.</p> <p>You must also specify a <code>workspaceRoleArn</code> for a role that you will manage for the workspace to use when accessing those datasources and notification channels.</p> <p>The ability for Amazon Managed Grafana to create and update IAM roles on behalf of the user is supported only in the Amazon Managed Grafana console, where this value may be set to <code>SERVICE_MANAGED</code>.</p> <note> <p>Use only the <code>CUSTOMER_MANAGED</code> permission type when creating a workspace with the API, CLI or Amazon Web Services CloudFormation. </p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html\">Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels</a>.</p>
            stack_set_name: <p>The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace.</p>
            workspace_data_sources: <p>This parameter is for internal use only, and should not be used.</p>
            workspace_description: <p>A description for the workspace. This is used only to help you identify this workspace.</p> <p>Pattern: <code>^[\\p{L}\\p{Z}\\p{N}\\p{P}]{0,2048}$</code> </p>
            workspace_name: <p>The name for the workspace. It does not have to be unique.</p>
            workspace_notification_destinations: <p>Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.</p>
            workspace_organizational_units: <p>Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.</p>
            workspace_role_arn: <p>Specified the IAM role that grants permissions to the Amazon Web Services resources that the workspace will view data from, including both data sources and notification channels. You are responsible for managing the permissions for this role as new data sources or notification channels are added. </p>
            authentication_providers: <p>Specifies whether this workspace uses SAML 2.0, IAM Identity Center, or both to authenticate users for using the Grafana console within a workspace. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html\">User authentication in Amazon Managed Grafana</a>.</p>
            tags: <p>The list of tags associated with the workspace.</p>
            vpc_configuration: <p>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</p> <note> <p>Connecting to a private VPC is not yet available in the Asia Pacific (Seoul) Region (ap-northeast-2).</p> </note>
            configuration: <p>The configuration string for the workspace that you create. For more information about the format and configuration options available, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html\">Working in your Grafana workspace</a>.</p>
            network_access_control: <p>Configuration for network access to your workspace.</p> <p>When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.</p> <p>If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>
            grafana_version: <p>Specifies the version of Grafana to support in the new workspace. If not specified, defaults to the latest version (for example, 10.4).</p> <p>To get a list of supported versions, use the <code>ListVersions</code> operation.</p>
            ip_address_type: <p>Specifies whether the workspace supports IPv4 only, or IPv4 and IPv6. Valid values are <code>IPv4</code> and <code>DualStack</code>. For more information about IP address types, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html\">Network access control</a>.</p>
            kms_key_id: <p>The ID or ARN of the Key Management Service key to use for encrypting workspace data.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.create_workspace_request.CreateWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.create_workspace_response.CreateWorkspaceResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.create_workspace

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.create_workspace.create_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.create_workspace_request.CreateWorkspaceRequest = {
            "account_access_type": account_access_type,
            "permission_type": permission_type,
            "authentication_providers": authentication_providers,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if organization_role_name is not None:
            input_["organization_role_name"] = organization_role_name
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if workspace_data_sources is not None:
            input_["workspace_data_sources"] = workspace_data_sources
        if workspace_description is not None:
            input_["workspace_description"] = workspace_description
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
        if workspace_notification_destinations is not None:
            input_["workspace_notification_destinations"] = (
                workspace_notification_destinations
            )
        if workspace_organizational_units is not None:
            input_["workspace_organizational_units"] = workspace_organizational_units
        if workspace_role_arn is not None:
            input_["workspace_role_arn"] = workspace_role_arn
        if tags is not None:
            input_["tags"] = tags
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if configuration is not None:
            input_["configuration"] = configuration
        if network_access_control is not None:
            input_["network_access_control"] = network_access_control
        if grafana_version is not None:
            input_["grafana_version"] = grafana_version
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_workspace(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.describe_workspace_response.DescribeWorkspaceResponse":
        """<p>Displays information about one Amazon Managed Grafana workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to display information about.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.describe_workspace_request.DescribeWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.describe_workspace_response.DescribeWorkspaceResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.describe_workspace

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.describe_workspace.describe_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.describe_workspace_request.DescribeWorkspaceRequest = {
            "workspace_id": workspace_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workspace(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        account_access_type: Optional[
            "capo_grafana.types.account_access_type.AccountAccessType"
        ] = None,
        organization_role_name: Optional[
            "capo_grafana.types.organization_role_name.OrganizationRoleName"
        ] = None,
        permission_type: Optional[
            "capo_grafana.types.permission_type.PermissionType"
        ] = None,
        stack_set_name: Optional[
            "capo_grafana.types.stack_set_name.StackSetName"
        ] = None,
        workspace_data_sources: Optional[
            "capo_grafana.types.data_source_types_list.DataSourceTypesList"
        ] = None,
        workspace_description: Optional[
            "capo_grafana.types.description.Description"
        ] = None,
        workspace_name: Optional[
            "capo_grafana.types.workspace_name.WorkspaceName"
        ] = None,
        workspace_notification_destinations: Optional[
            "capo_grafana.types.notification_destinations_list.NotificationDestinationsList"
        ] = None,
        workspace_organizational_units: Optional[
            "capo_grafana.types.organizational_unit_list.OrganizationalUnitList"
        ] = None,
        workspace_role_arn: Optional[
            "capo_grafana.types.iam_role_arn.IamRoleArn"
        ] = None,
        vpc_configuration: Optional[
            "capo_grafana.types.vpc_configuration.VpcConfiguration"
        ] = None,
        remove_vpc_configuration: Optional[bool] = None,
        network_access_control: Optional[
            "capo_grafana.types.network_access_configuration.NetworkAccessConfiguration"
        ] = None,
        remove_network_access_configuration: Optional[bool] = None,
        ip_address_type: Optional[
            "capo_grafana.types.ip_address_type.IPAddressType"
        ] = None,
    ) -> "capo_grafana.types.update_workspace_response.UpdateWorkspaceResponse":
        r"""<p>Modifies an existing Amazon Managed Grafana workspace. If you use this operation and omit any optional parameters, the existing values of those parameters are not changed.</p> <p>To modify the user authentication methods that the workspace uses, such as SAML or IAM Identity Center, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdateWorkspaceAuthentication.html\">UpdateWorkspaceAuthentication</a>.</p> <p>To modify which users in the workspace have the <code>Admin</code> and <code>Editor</code> Grafana roles, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_UpdatePermissions.html\">UpdatePermissions</a>.</p>

        Args:
            account_access_type: <p>Specifies whether the workspace can access Amazon Web Services resources in this Amazon Web Services account only, or whether it can also access Amazon Web Services resources in other accounts in the same organization. If you specify <code>ORGANIZATION</code>, you must specify which organizational units the workspace can access in the <code>workspaceOrganizationalUnits</code> parameter.</p>
            organization_role_name: <p>The name of an IAM role that already exists to use to access resources through Organizations. This can only be used with a workspace that has the <code>permissionType</code> set to <code>CUSTOMER_MANAGED</code>.</p>
            permission_type: <p>Use this parameter if you want to change a workspace from <code>SERVICE_MANAGED</code> to <code>CUSTOMER_MANAGED</code>. This allows you to manage the permissions that the workspace uses to access datasources and notification channels. If the workspace is in a member Amazon Web Services account of an organization, and that account is not a delegated administrator account, and you want the workspace to access data sources in other Amazon Web Services accounts in the organization, you must choose <code>CUSTOMER_MANAGED</code>.</p> <p>If you specify this as <code>CUSTOMER_MANAGED</code>, you must also specify a <code>workspaceRoleArn</code> that the workspace will use for accessing Amazon Web Services resources.</p> <p>For more information on the role and permissions needed, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html\">Amazon Managed Grafana permissions and policies for Amazon Web Services data sources and notification channels</a> </p> <note> <p>Do not use this to convert a <code>CUSTOMER_MANAGED</code> workspace to <code>SERVICE_MANAGED</code>. Do not include this parameter if you want to leave the workspace as <code>SERVICE_MANAGED</code>.</p> <p>You can convert a <code>CUSTOMER_MANAGED</code> workspace to <code>SERVICE_MANAGED</code> using the Amazon Managed Grafana console. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-datasource-and-notification.html\">Managing permissions for data sources and notification channels</a>.</p> </note>
            stack_set_name: <p>The name of the CloudFormation stack set to use to generate IAM roles to be used for this workspace.</p>
            workspace_data_sources: <p>This parameter is for internal use only, and should not be used.</p>
            workspace_description: <p>A description for the workspace. This is used only to help you identify this workspace.</p>
            workspace_id: <p>The ID of the workspace to update.</p>
            workspace_name: <p>A new name for the workspace to update.</p>
            workspace_notification_destinations: <p>Specify the Amazon Web Services notification channels that you plan to use in this workspace. Specifying these data sources here enables Amazon Managed Grafana to create IAM roles and permissions that allow Amazon Managed Grafana to use these channels.</p>
            workspace_organizational_units: <p>Specifies the organizational units that this workspace is allowed to use data sources from, if this workspace is in an account that is part of an organization.</p>
            workspace_role_arn: <p>Specifies an IAM role that grants permissions to Amazon Web Services resources that the workspace accesses, such as data sources and notification channels. If this workspace has <code>permissionType</code> <code>CUSTOMER_MANAGED</code>, then this role is required.</p>
            vpc_configuration: <p>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</p>
            remove_vpc_configuration: <p>Whether to remove the VPC configuration from the workspace.</p> <p>Setting this to <code>true</code> and providing a <code>vpcConfiguration</code> to set will return an error.</p>
            network_access_control: <p>The configuration settings for network access to your workspace.</p> <p>When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization will still be required.</p> <p>If this is not configured, or is removed, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>
            remove_network_access_configuration: <p>Whether to remove the network access configuration from the workspace.</p> <p>Setting this to <code>true</code> and providing a <code>networkAccessControl</code> to set will return an error.</p> <p>If you remove this configuration by setting this to <code>true</code>, then all IP addresses and VPC endpoints will be allowed. Standard Grafana authentication and authorization will still be required.</p>
            ip_address_type: <p>Specifies whether the workspace supports IPv4 only, or IPv4 and IPv6. Valid values are <code>IPv4</code> and <code>DualStack</code>. For more information about IP address types, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-nac.html\">Network access control</a>.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.update_workspace_request.UpdateWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.update_workspace_response.UpdateWorkspaceResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.update_workspace

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.update_workspace.update_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.update_workspace_request.UpdateWorkspaceRequest = {
            "workspace_id": workspace_id
        }
        if account_access_type is not None:
            input_["account_access_type"] = account_access_type
        if organization_role_name is not None:
            input_["organization_role_name"] = organization_role_name
        if permission_type is not None:
            input_["permission_type"] = permission_type
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if workspace_data_sources is not None:
            input_["workspace_data_sources"] = workspace_data_sources
        if workspace_description is not None:
            input_["workspace_description"] = workspace_description
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
        if workspace_notification_destinations is not None:
            input_["workspace_notification_destinations"] = (
                workspace_notification_destinations
            )
        if workspace_organizational_units is not None:
            input_["workspace_organizational_units"] = workspace_organizational_units
        if workspace_role_arn is not None:
            input_["workspace_role_arn"] = workspace_role_arn
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if remove_vpc_configuration is not None:
            input_["remove_vpc_configuration"] = remove_vpc_configuration
        if network_access_control is not None:
            input_["network_access_control"] = network_access_control
        if remove_network_access_configuration is not None:
            input_["remove_network_access_configuration"] = (
                remove_network_access_configuration
            )
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workspace(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.delete_workspace_response.DeleteWorkspaceResponse":
        """<p>Deletes an Amazon Managed Grafana workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to delete.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.delete_workspace_request.DeleteWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.delete_workspace_response.DeleteWorkspaceResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.delete_workspace

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.delete_workspace.delete_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.delete_workspace_request.DeleteWorkspaceRequest = {
            "workspace_id": workspace_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workspaces(
        self,
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_grafana.types.list_workspaces_response.ListWorkspacesResponse":
        r"""<p>Returns a list of Amazon Managed Grafana workspaces in the account, with some information about each workspace. For more complete information about one workspace, use <a href=\"https://docs.aws.amazon.com/grafana/latest/APIReference/API_DescribeWorkspace.html\">DescribeWorkspace</a>.</p>

        Args:
            max_results: <p>The maximum number of workspaces to include in the results.</p>
            next_token: <p>The token for the next set of workspaces to return. (You receive this token from a previous <code>ListWorkspaces</code> operation.)</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.list_workspaces_request.ListWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.list_workspaces_response.ListWorkspacesResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_workspaces

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.list_workspaces.list_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_grafana.types.list_workspaces_request.ListWorkspacesRequest = {}
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

    def iter_list_workspaces(
        self,
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_grafana.types.workspace_summary.WorkspaceSummary]":
        _token = next_token
        while True:
            _response = self.list_workspaces(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("workspaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
