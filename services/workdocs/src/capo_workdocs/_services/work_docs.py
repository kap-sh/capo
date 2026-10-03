"""Generated from Smithy shape ``com.amazonaws.workdocs#AWSGorillaBoyService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_workdocs._auth._signers
import capo_workdocs._auth._sigv4
from capo_workdocs._auth._identity import Credentials
from capo_workdocs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_workdocs._auth._zapros_handler import AuthMiddleware
from capo_workdocs._pagination import resolve_path as _resolve_path
from capo_workdocs._services._aws_config import aws_config
from capo_workdocs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_workdocs.types.abort_document_version_upload_request
    import capo_workdocs.types.activate_user_request
    import capo_workdocs.types.activate_user_response
    import capo_workdocs.types.activity
    import capo_workdocs.types.activity_names_filter_type
    import capo_workdocs.types.add_resource_permissions_request
    import capo_workdocs.types.add_resource_permissions_response
    import capo_workdocs.types.additional_response_fields_list
    import capo_workdocs.types.authentication_header_type
    import capo_workdocs.types.boolean_enum_type
    import capo_workdocs.types.boolean_type
    import capo_workdocs.types.comment
    import capo_workdocs.types.comment_id_type
    import capo_workdocs.types.comment_text_type
    import capo_workdocs.types.comment_visibility_type
    import capo_workdocs.types.create_comment_request
    import capo_workdocs.types.create_comment_response
    import capo_workdocs.types.create_custom_metadata_request
    import capo_workdocs.types.create_custom_metadata_response
    import capo_workdocs.types.create_folder_request
    import capo_workdocs.types.create_folder_response
    import capo_workdocs.types.create_labels_request
    import capo_workdocs.types.create_labels_response
    import capo_workdocs.types.create_notification_subscription_request
    import capo_workdocs.types.create_notification_subscription_response
    import capo_workdocs.types.create_user_request
    import capo_workdocs.types.create_user_response
    import capo_workdocs.types.custom_metadata_key_list
    import capo_workdocs.types.custom_metadata_map
    import capo_workdocs.types.deactivate_user_request
    import capo_workdocs.types.delete_comment_request
    import capo_workdocs.types.delete_custom_metadata_request
    import capo_workdocs.types.delete_custom_metadata_response
    import capo_workdocs.types.delete_document_request
    import capo_workdocs.types.delete_document_version_request
    import capo_workdocs.types.delete_folder_contents_request
    import capo_workdocs.types.delete_folder_request
    import capo_workdocs.types.delete_labels_request
    import capo_workdocs.types.delete_labels_response
    import capo_workdocs.types.delete_notification_subscription_request
    import capo_workdocs.types.delete_user_request
    import capo_workdocs.types.describe_activities_request
    import capo_workdocs.types.describe_activities_response
    import capo_workdocs.types.describe_comments_request
    import capo_workdocs.types.describe_comments_response
    import capo_workdocs.types.describe_document_versions_request
    import capo_workdocs.types.describe_document_versions_response
    import capo_workdocs.types.describe_folder_contents_request
    import capo_workdocs.types.describe_folder_contents_response
    import capo_workdocs.types.describe_groups_request
    import capo_workdocs.types.describe_groups_response
    import capo_workdocs.types.describe_notification_subscriptions_request
    import capo_workdocs.types.describe_notification_subscriptions_response
    import capo_workdocs.types.describe_resource_permissions_request
    import capo_workdocs.types.describe_resource_permissions_response
    import capo_workdocs.types.describe_root_folders_request
    import capo_workdocs.types.describe_root_folders_response
    import capo_workdocs.types.describe_users_request
    import capo_workdocs.types.describe_users_response
    import capo_workdocs.types.document_content_type
    import capo_workdocs.types.document_version_id_type
    import capo_workdocs.types.document_version_metadata
    import capo_workdocs.types.document_version_status
    import capo_workdocs.types.email_address_type
    import capo_workdocs.types.field_names_type
    import capo_workdocs.types.filters
    import capo_workdocs.types.folder_content_type
    import capo_workdocs.types.folder_metadata
    import capo_workdocs.types.get_current_user_request
    import capo_workdocs.types.get_current_user_response
    import capo_workdocs.types.get_document_path_request
    import capo_workdocs.types.get_document_path_response
    import capo_workdocs.types.get_document_request
    import capo_workdocs.types.get_document_response
    import capo_workdocs.types.get_document_version_request
    import capo_workdocs.types.get_document_version_response
    import capo_workdocs.types.get_folder_path_request
    import capo_workdocs.types.get_folder_path_response
    import capo_workdocs.types.get_folder_request
    import capo_workdocs.types.get_folder_response
    import capo_workdocs.types.get_resources_request
    import capo_workdocs.types.get_resources_response
    import capo_workdocs.types.group_metadata
    import capo_workdocs.types.id_type
    import capo_workdocs.types.initiate_document_version_upload_request
    import capo_workdocs.types.initiate_document_version_upload_response
    import capo_workdocs.types.limit_type
    import capo_workdocs.types.locale_type
    import capo_workdocs.types.marker_type
    import capo_workdocs.types.next_marker_type
    import capo_workdocs.types.notification_options
    import capo_workdocs.types.order_type
    import capo_workdocs.types.page_marker_type
    import capo_workdocs.types.password_type
    import capo_workdocs.types.positive_integer_type
    import capo_workdocs.types.principal
    import capo_workdocs.types.principal_type
    import capo_workdocs.types.remove_all_resource_permissions_request
    import capo_workdocs.types.remove_resource_permission_request
    import capo_workdocs.types.resource_collection_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.resource_name_type
    import capo_workdocs.types.resource_sort_type
    import capo_workdocs.types.resource_state_type
    import capo_workdocs.types.response_item
    import capo_workdocs.types.restore_document_versions_request
    import capo_workdocs.types.search_marker_type
    import capo_workdocs.types.search_query_scope_type_list
    import capo_workdocs.types.search_query_type
    import capo_workdocs.types.search_resources_request
    import capo_workdocs.types.search_resources_response
    import capo_workdocs.types.search_result_sort_list
    import capo_workdocs.types.search_results_limit_type
    import capo_workdocs.types.share_principal_list
    import capo_workdocs.types.shared_labels
    import capo_workdocs.types.size_type
    import capo_workdocs.types.storage_rule_type
    import capo_workdocs.types.subscription
    import capo_workdocs.types.subscription_end_point_type
    import capo_workdocs.types.subscription_protocol_type
    import capo_workdocs.types.subscription_type
    import capo_workdocs.types.time_zone_id_type
    import capo_workdocs.types.timestamp_type
    import capo_workdocs.types.update_document_request
    import capo_workdocs.types.update_document_version_request
    import capo_workdocs.types.update_folder_request
    import capo_workdocs.types.update_user_request
    import capo_workdocs.types.update_user_response
    import capo_workdocs.types.user
    import capo_workdocs.types.user_attribute_value_type
    import capo_workdocs.types.user_filter_type
    import capo_workdocs.types.user_ids_type
    import capo_workdocs.types.user_sort_type
    import capo_workdocs.types.user_type
    import capo_workdocs.types.username_type


class WorkDocsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class WorkDocsClient:
    """A client for the ``WorkDocs`` service.

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
        self._config = WorkDocsClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[WorkDocsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WorkDocsClientConfig = config_overrides or {}
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

    def abort_document_version_upload(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Aborts the upload of the specified document version that was previously initiated by <a>InitiateDocumentVersionUpload</a>. The client should make this call only when it no longer intends to upload the document version, or fails to do so.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The ID of the version.</p>

        Raises:
            capo_workdocs.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource hierarchy is changing.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.abort_document_version_upload_request.AbortDocumentVersionUploadRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.abort_document_version_upload

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.abort_document_version_upload.abort_document_version_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.abort_document_version_upload_request.AbortDocumentVersionUploadRequest = {
            "document_id": document_id,
            "version_id": version_id,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def activate_user(
        self,
        user_id: "capo_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> "capo_workdocs.types.activate_user_response.ActivateUserResponse":
        """<p>Activates the specified user. Only active users can access Amazon WorkDocs.</p>

        Args:
            user_id: <p>The ID of the user.</p>
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.activate_user_request.ActivateUserRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.activate_user_response.ActivateUserResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.activate_user

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.activate_user.activate_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.activate_user_request.ActivateUserRequest = {
            "user_id": user_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_resource_permissions(
        self,
        resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        principals: "capo_workdocs.types.share_principal_list.SharePrincipalList",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        notification_options: Optional[
            "capo_workdocs.types.notification_options.NotificationOptions"
        ] = None,
    ) -> "capo_workdocs.types.add_resource_permissions_response.AddResourcePermissionsResponse":
        """<p>Creates a set of permissions for the specified folder or document. The resource permissions are overwritten if the principals already have different permissions.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource.</p>
            principals: <p>The users, groups, or organization being granted permission.</p>
            notification_options: <p>The notification options.</p>

        Raises:
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.add_resource_permissions_request.AddResourcePermissionsRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.add_resource_permissions_response.AddResourcePermissionsResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.add_resource_permissions

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.add_resource_permissions.add_resource_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.add_resource_permissions_request.AddResourcePermissionsRequest = {
            "resource_id": resource_id,
            "principals": principals,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if notification_options is not None:
            input_["notification_options"] = notification_options

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_comment(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType",
        text: "capo_workdocs.types.comment_text_type.CommentTextType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        parent_id: Optional["capo_workdocs.types.comment_id_type.CommentIdType"] = None,
        thread_id: Optional["capo_workdocs.types.comment_id_type.CommentIdType"] = None,
        visibility: Optional[
            "capo_workdocs.types.comment_visibility_type.CommentVisibilityType"
        ] = None,
        notify_collaborators: Optional[
            "capo_workdocs.types.boolean_type.BooleanType"
        ] = None,
    ) -> "capo_workdocs.types.create_comment_response.CreateCommentResponse":
        """<p>Adds a new comment to the specified document version.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The ID of the document version.</p>
            parent_id: <p>The ID of the parent comment.</p>
            thread_id: <p>The ID of the root comment in the thread.</p>
            text: <p>The text of the comment.</p>
            visibility: <p>The visibility of the comment. Options are either PRIVATE, where the comment is visible only to the comment author and document owner and co-owners, or PUBLIC, where the comment is visible to document owners, co-owners, and contributors.</p>
            notify_collaborators: <p>Set this parameter to TRUE to send an email out to the document collaborators after the comment is created.</p>

        Raises:
            capo_workdocs.errors.document_locked_for_comments_exception.DocumentLockedForCommentsException: <p>This exception is thrown when the document is locked for comments and user tries to create or delete a comment on that document.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_comment_operation_exception.InvalidCommentOperationException: <p>The requested operation is not allowed on the specified comment object.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.create_comment_request.CreateCommentRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.create_comment_response.CreateCommentResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.create_comment

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.create_comment.create_comment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.create_comment_request.CreateCommentRequest = {
            "document_id": document_id,
            "version_id": version_id,
            "text": text,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if parent_id is not None:
            input_["parent_id"] = parent_id
        if thread_id is not None:
            input_["thread_id"] = thread_id
        if visibility is not None:
            input_["visibility"] = visibility
        if notify_collaborators is not None:
            input_["notify_collaborators"] = notify_collaborators

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_custom_metadata(
        self,
        resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        custom_metadata: "capo_workdocs.types.custom_metadata_map.CustomMetadataMap",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        version_id: Optional[
            "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
        ] = None,
    ) -> "capo_workdocs.types.create_custom_metadata_response.CreateCustomMetadataResponse":
        """<p>Adds one or more custom properties to the specified resource (a folder, document, or version).</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource.</p>
            version_id: <p>The ID of the version, if the custom metadata is being added to a document version.</p>
            custom_metadata: <p>Custom metadata in the form of name-value pairs.</p>

        Raises:
            capo_workdocs.errors.custom_metadata_limit_exceeded_exception.CustomMetadataLimitExceededException: <p>The limit has been reached on the number of custom properties for the specified resource.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.create_custom_metadata_request.CreateCustomMetadataRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.create_custom_metadata_response.CreateCustomMetadataResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.create_custom_metadata

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.create_custom_metadata.create_custom_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.create_custom_metadata_request.CreateCustomMetadataRequest = {
            "resource_id": resource_id,
            "custom_metadata": custom_metadata,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if version_id is not None:
            input_["version_id"] = version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_folder(
        self,
        parent_folder_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        name: Optional[
            "capo_workdocs.types.resource_name_type.ResourceNameType"
        ] = None,
    ) -> "capo_workdocs.types.create_folder_response.CreateFolderResponse":
        """<p>Creates a folder with the specified name and parent folder.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            name: <p>The name of the new folder.</p>
            parent_folder_id: <p>The ID of the parent folder.</p>

        Raises:
            capo_workdocs.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource hierarchy is changing.</p>
            capo_workdocs.errors.conflicting_operation_exception.ConflictingOperationException: <p>Another operation is in progress on the resource that conflicts with the current operation.</p>
            capo_workdocs.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The resource already exists.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.limit_exceeded_exception.LimitExceededException: <p>The maximum of 100,000 files and folders under the parent folder has been exceeded.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.create_folder_request.CreateFolderRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.create_folder_response.CreateFolderResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.create_folder

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.create_folder.create_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.create_folder_request.CreateFolderRequest = {
            "parent_folder_id": parent_folder_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_labels(
        self,
        resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        labels: "capo_workdocs.types.shared_labels.SharedLabels",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> "capo_workdocs.types.create_labels_response.CreateLabelsResponse":
        """<p>Adds the specified list of labels to the given resource (a document or folder)</p>

        Args:
            resource_id: <p>The ID of the resource.</p>
            labels: <p>List of labels to add to the resource.</p>
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.too_many_labels_exception.TooManyLabelsException: <p>The limit has been reached on the number of labels for the specified resource.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.create_labels_request.CreateLabelsRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.create_labels_response.CreateLabelsResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.create_labels

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.create_labels.create_labels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.create_labels_request.CreateLabelsRequest = {
            "resource_id": resource_id,
            "labels": labels,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_notification_subscription(
        self,
        organization_id: "capo_workdocs.types.id_type.IdType",
        endpoint: "capo_workdocs.types.subscription_end_point_type.SubscriptionEndPointType",
        protocol: "capo_workdocs.types.subscription_protocol_type.SubscriptionProtocolType",
        subscription_type: "capo_workdocs.types.subscription_type.SubscriptionType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
    ) -> "capo_workdocs.types.create_notification_subscription_response.CreateNotificationSubscriptionResponse":
        """<p>Configure Amazon WorkDocs to use Amazon SNS notifications. The endpoint receives a confirmation message, and must confirm the subscription.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/workdocs/latest/developerguide/manage-notifications.html">Setting up notifications for an IAM user or role</a> in the <i>Amazon WorkDocs Developer Guide</i>.</p>

        Args:
            organization_id: <p>The ID of the organization.</p>
            endpoint: <p>The endpoint to receive the notifications. If the protocol is HTTPS, the endpoint is a URL that begins with <code>https</code>.</p>
            protocol: <p>The protocol to use. The supported value is https, which delivers JSON-encoded messages using HTTPS POST.</p>
            subscription_type: <p>The notification type.</p>

        Raises:
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.too_many_subscriptions_exception.TooManySubscriptionsException: <p>You've reached the limit on the number of subscriptions for the WorkDocs instance.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.create_notification_subscription_request.CreateNotificationSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.create_notification_subscription_response.CreateNotificationSubscriptionResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.create_notification_subscription

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.create_notification_subscription.create_notification_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.create_notification_subscription_request.CreateNotificationSubscriptionRequest = {
            "organization_id": organization_id,
            "endpoint": endpoint,
            "protocol": protocol,
            "subscription_type": subscription_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_user(
        self,
        username: "capo_workdocs.types.username_type.UsernameType",
        given_name: "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType",
        surname: "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType",
        password: "capo_workdocs.types.password_type.PasswordType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        organization_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        email_address: Optional[
            "capo_workdocs.types.email_address_type.EmailAddressType"
        ] = None,
        time_zone_id: Optional[
            "capo_workdocs.types.time_zone_id_type.TimeZoneIdType"
        ] = None,
        storage_rule: Optional[
            "capo_workdocs.types.storage_rule_type.StorageRuleType"
        ] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> "capo_workdocs.types.create_user_response.CreateUserResponse":
        """<p>Creates a user in a Simple AD or Microsoft AD directory. The status of a newly created user is "ACTIVE". New users can access Amazon WorkDocs.</p>

        Args:
            organization_id: <p>The ID of the organization.</p>
            username: <p>The login name of the user.</p>
            email_address: <p>The email address of the user.</p>
            given_name: <p>The given name of the user.</p>
            surname: <p>The surname of the user.</p>
            password: <p>The password of the user.</p>
            time_zone_id: <p>The time zone ID of the user.</p>
            storage_rule: <p>The amount of storage for the user.</p>
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>

        Raises:
            capo_workdocs.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The resource already exists.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.create_user_response.CreateUserResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.create_user

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.create_user_request.CreateUserRequest = {
            "username": username,
            "given_name": given_name,
            "surname": surname,
            "password": password,
        }
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if email_address is not None:
            input_["email_address"] = email_address
        if time_zone_id is not None:
            input_["time_zone_id"] = time_zone_id
        if storage_rule is not None:
            input_["storage_rule"] = storage_rule
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deactivate_user(
        self,
        user_id: "capo_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Deactivates the specified user, which revokes the user's access to Amazon WorkDocs.</p>

        Args:
            user_id: <p>The ID of the user.</p>
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.deactivate_user_request.DeactivateUserRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.deactivate_user

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.deactivate_user.deactivate_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.deactivate_user_request.DeactivateUserRequest = {
            "user_id": user_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_comment(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType",
        comment_id: "capo_workdocs.types.comment_id_type.CommentIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Deletes the specified comment from the document version.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The ID of the document version.</p>
            comment_id: <p>The ID of the comment.</p>

        Raises:
            capo_workdocs.errors.document_locked_for_comments_exception.DocumentLockedForCommentsException: <p>This exception is thrown when the document is locked for comments and user tries to create or delete a comment on that document.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.delete_comment_request.DeleteCommentRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.delete_comment

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.delete_comment.delete_comment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.delete_comment_request.DeleteCommentRequest = {
            "document_id": document_id,
            "version_id": version_id,
            "comment_id": comment_id,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_custom_metadata(
        self,
        resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        version_id: Optional[
            "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
        ] = None,
        keys: Optional[
            "capo_workdocs.types.custom_metadata_key_list.CustomMetadataKeyList"
        ] = None,
        delete_all: Optional["capo_workdocs.types.boolean_type.BooleanType"] = None,
    ) -> "capo_workdocs.types.delete_custom_metadata_response.DeleteCustomMetadataResponse":
        """<p>Deletes custom metadata from the specified resource.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource, either a document or folder.</p>
            version_id: <p>The ID of the version, if the custom metadata is being deleted from a document version.</p>
            keys: <p>List of properties to remove.</p>
            delete_all: <p>Flag to indicate removal of all custom metadata properties from the specified resource.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.delete_custom_metadata_request.DeleteCustomMetadataRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.delete_custom_metadata_response.DeleteCustomMetadataResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.delete_custom_metadata

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.delete_custom_metadata.delete_custom_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.delete_custom_metadata_request.DeleteCustomMetadataRequest = {
            "resource_id": resource_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if version_id is not None:
            input_["version_id"] = version_id
        if keys is not None:
            input_["keys"] = keys
        if delete_all is not None:
            input_["delete_all"] = delete_all

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_document(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Permanently deletes the specified document and its associated metadata.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>

        Raises:
            capo_workdocs.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource hierarchy is changing.</p>
            capo_workdocs.errors.conflicting_operation_exception.ConflictingOperationException: <p>Another operation is in progress on the resource that conflicts with the current operation.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.limit_exceeded_exception.LimitExceededException: <p>The maximum of 100,000 files and folders under the parent folder has been exceeded.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.delete_document_request.DeleteDocumentRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.delete_document

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.delete_document.delete_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.delete_document_request.DeleteDocumentRequest = {
            "document_id": document_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_document_version(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType",
        delete_prior_versions: "capo_workdocs.types.boolean_type.BooleanType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Deletes a specific version of a document.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document associated with the version being deleted.</p>
            version_id: <p>The ID of the version being deleted.</p>
            delete_prior_versions: <p>Deletes all versions of a document prior to the current version.</p>

        Raises:
            capo_workdocs.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource hierarchy is changing.</p>
            capo_workdocs.errors.conflicting_operation_exception.ConflictingOperationException: <p>Another operation is in progress on the resource that conflicts with the current operation.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is invalid.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.delete_document_version_request.DeleteDocumentVersionRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.delete_document_version

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.delete_document_version.delete_document_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.delete_document_version_request.DeleteDocumentVersionRequest = {
            "document_id": document_id,
            "version_id": version_id,
            "delete_prior_versions": delete_prior_versions,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_folder(
        self,
        folder_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Permanently deletes the specified folder and its contents.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>

        Raises:
            capo_workdocs.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource hierarchy is changing.</p>
            capo_workdocs.errors.conflicting_operation_exception.ConflictingOperationException: <p>Another operation is in progress on the resource that conflicts with the current operation.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.limit_exceeded_exception.LimitExceededException: <p>The maximum of 100,000 files and folders under the parent folder has been exceeded.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.delete_folder_request.DeleteFolderRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.delete_folder

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.delete_folder.delete_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.delete_folder_request.DeleteFolderRequest = {
            "folder_id": folder_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_folder_contents(
        self,
        folder_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Deletes the contents of the specified folder.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>

        Raises:
            capo_workdocs.errors.conflicting_operation_exception.ConflictingOperationException: <p>Another operation is in progress on the resource that conflicts with the current operation.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.delete_folder_contents_request.DeleteFolderContentsRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.delete_folder_contents

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.delete_folder_contents.delete_folder_contents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.delete_folder_contents_request.DeleteFolderContentsRequest = {
            "folder_id": folder_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_labels(
        self,
        resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        labels: Optional["capo_workdocs.types.shared_labels.SharedLabels"] = None,
        delete_all: Optional["capo_workdocs.types.boolean_type.BooleanType"] = None,
    ) -> "capo_workdocs.types.delete_labels_response.DeleteLabelsResponse":
        """<p>Deletes the specified list of labels from a resource.</p>

        Args:
            resource_id: <p>The ID of the resource.</p>
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            labels: <p>List of labels to delete from the resource.</p>
            delete_all: <p>Flag to request removal of all labels from the specified resource.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.delete_labels_request.DeleteLabelsRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.delete_labels_response.DeleteLabelsResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.delete_labels

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.delete_labels.delete_labels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.delete_labels_request.DeleteLabelsRequest = {
            "resource_id": resource_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if labels is not None:
            input_["labels"] = labels
        if delete_all is not None:
            input_["delete_all"] = delete_all

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_notification_subscription(
        self,
        subscription_id: "capo_workdocs.types.id_type.IdType",
        organization_id: "capo_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified subscription from the specified organization.</p>

        Args:
            subscription_id: <p>The ID of the subscription.</p>
            organization_id: <p>The ID of the organization.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.delete_notification_subscription_request.DeleteNotificationSubscriptionRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.delete_notification_subscription

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.delete_notification_subscription.delete_notification_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.delete_notification_subscription_request.DeleteNotificationSubscriptionRequest = {
            "subscription_id": subscription_id,
            "organization_id": organization_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_user(
        self,
        user_id: "capo_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Deletes the specified user from a Simple AD or Microsoft AD directory.</p> <important> <p>Deleting a user immediately and permanently deletes all content in that user's folder structure. Site retention policies do NOT apply to this type of deletion.</p> </important>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Do not set this field when using administrative API actions, as in accessing the API using Amazon Web Services credentials.</p>
            user_id: <p>The ID of the user.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.delete_user

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.delete_user.delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.delete_user_request.DeleteUserRequest = {
            "user_id": user_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_activities(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        start_time: Optional["capo_workdocs.types.timestamp_type.TimestampType"] = None,
        end_time: Optional["capo_workdocs.types.timestamp_type.TimestampType"] = None,
        organization_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        activity_types: Optional[
            "capo_workdocs.types.activity_names_filter_type.ActivityNamesFilterType"
        ] = None,
        resource_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        user_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        include_indirect_activities: Optional[
            "capo_workdocs.types.boolean_type.BooleanType"
        ] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional[
            "capo_workdocs.types.search_marker_type.SearchMarkerType"
        ] = None,
    ) -> "capo_workdocs.types.describe_activities_response.DescribeActivitiesResponse":
        """<p>Describes the user activities in a specified time period.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            start_time: <p>The timestamp that determines the starting time of the activities. The response includes the activities performed after the specified timestamp.</p>
            end_time: <p>The timestamp that determines the end time of the activities. The response includes the activities performed before the specified timestamp.</p>
            organization_id: <p>The ID of the organization. This is a mandatory parameter when using administrative API (SigV4) requests.</p>
            activity_types: <p>Specifies which activity types to include in the response. If this field is left empty, all activity types are returned.</p>
            resource_id: <p>The document or folder ID for which to describe activity types.</p>
            user_id: <p>The ID of the user who performed the action. The response includes activities pertaining to this user. This is an optional parameter and is only applicable for administrative API (SigV4) requests.</p>
            include_indirect_activities: <p>Includes indirect activities. An indirect activity results from a direct activity performed on a parent resource. For example, sharing a parent folder (the direct activity) shares all of the subfolders and documents within the parent folder (the indirect activity).</p>
            limit: <p>The maximum number of items to return.</p>
            marker: <p>The marker for the next set of results.</p>

        Raises:
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.describe_activities_request.DescribeActivitiesRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.describe_activities_response.DescribeActivitiesResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.describe_activities

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.describe_activities.describe_activities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.describe_activities_request.DescribeActivitiesRequest = {}
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if activity_types is not None:
            input_["activity_types"] = activity_types
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if user_id is not None:
            input_["user_id"] = user_id
        if include_indirect_activities is not None:
            input_["include_indirect_activities"] = include_indirect_activities
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_activities(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        start_time: Optional["capo_workdocs.types.timestamp_type.TimestampType"] = None,
        end_time: Optional["capo_workdocs.types.timestamp_type.TimestampType"] = None,
        organization_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        activity_types: Optional[
            "capo_workdocs.types.activity_names_filter_type.ActivityNamesFilterType"
        ] = None,
        resource_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        user_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        include_indirect_activities: Optional[
            "capo_workdocs.types.boolean_type.BooleanType"
        ] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional[
            "capo_workdocs.types.search_marker_type.SearchMarkerType"
        ] = None,
    ) -> "Iterator[capo_workdocs.types.activity.Activity]":
        _token = marker
        while True:
            _response = self.describe_activities(
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                start_time=start_time,
                end_time=end_time,
                organization_id=organization_id,
                activity_types=activity_types,
                resource_id=resource_id,
                user_id=user_id,
                include_indirect_activities=include_indirect_activities,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("user_activities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_comments(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["capo_workdocs.types.marker_type.MarkerType"] = None,
    ) -> "capo_workdocs.types.describe_comments_response.DescribeCommentsResponse":
        """<p>List all the comments for the specified document version.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The ID of the document version.</p>
            limit: <p>The maximum number of items to return.</p>
            marker: <p>The marker for the next set of results. This marker was received from a previous call.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.describe_comments_request.DescribeCommentsRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.describe_comments_response.DescribeCommentsResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.describe_comments

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.describe_comments.describe_comments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.describe_comments_request.DescribeCommentsRequest = {
            "document_id": document_id,
            "version_id": version_id,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_comments(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["capo_workdocs.types.marker_type.MarkerType"] = None,
    ) -> "Iterator[capo_workdocs.types.comment.Comment]":
        _token = marker
        while True:
            _response = self.describe_comments(
                document_id,
                version_id,
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("comments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_document_versions(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        include: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
        fields: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
    ) -> "capo_workdocs.types.describe_document_versions_response.DescribeDocumentVersionsResponse":
        """<p>Retrieves the document versions for the specified document.</p> <p>By default, only active versions are returned.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            limit: <p>The maximum number of versions to return with this call.</p>
            include: <p>A comma-separated list of values. Specify "INITIALIZED" to include incomplete versions.</p>
            fields: <p>Specify "SOURCE" to include initialized versions and a URL for the source document.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.invalid_password_exception.InvalidPasswordException: <p>The password is invalid.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.describe_document_versions_request.DescribeDocumentVersionsRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.describe_document_versions_response.DescribeDocumentVersionsResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.describe_document_versions

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.describe_document_versions.describe_document_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.describe_document_versions_request.DescribeDocumentVersionsRequest = {
            "document_id": document_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit
        if include is not None:
            input_["include"] = include
        if fields is not None:
            input_["fields"] = fields

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_document_versions(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        include: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
        fields: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
    ) -> "Iterator[capo_workdocs.types.document_version_metadata.DocumentVersionMetadata]":
        _token = marker
        while True:
            _response = self.describe_document_versions(
                document_id,
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                marker=_token,
                limit=limit,
                include=include,
                fields=fields,
            )
            _page = _resolve_path(_response, ("document_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_folder_contents(
        self,
        folder_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        sort: Optional[
            "capo_workdocs.types.resource_sort_type.ResourceSortType"
        ] = None,
        order: Optional["capo_workdocs.types.order_type.OrderType"] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
        type: Optional[
            "capo_workdocs.types.folder_content_type.FolderContentType"
        ] = None,
        include: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
    ) -> "capo_workdocs.types.describe_folder_contents_response.DescribeFolderContentsResponse":
        """<p>Describes the contents of the specified folder, including its documents and subfolders.</p> <p>By default, Amazon WorkDocs returns the first 100 active document and folder metadata items. If there are more results, the response includes a marker that you can use to request the next set of results. You can also request initialized documents.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>
            sort: <p>The sorting criteria.</p>
            order: <p>The order for the contents of the folder.</p>
            limit: <p>The maximum number of items to return with this call.</p>
            marker: <p>The marker for the next set of results. This marker was received from a previous call.</p>
            type: <p>The type of items.</p>
            include: <p>The contents to include. Specify "INITIALIZED" to include initialized documents.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.describe_folder_contents_request.DescribeFolderContentsRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.describe_folder_contents_response.DescribeFolderContentsResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.describe_folder_contents

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.describe_folder_contents.describe_folder_contents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.describe_folder_contents_request.DescribeFolderContentsRequest = {
            "folder_id": folder_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if sort is not None:
            input_["sort"] = sort
        if order is not None:
            input_["order"] = order
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker
        if type is not None:
            input_["type"] = type
        if include is not None:
            input_["include"] = include

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_folder_contents(
        self,
        folder_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        sort: Optional[
            "capo_workdocs.types.resource_sort_type.ResourceSortType"
        ] = None,
        order: Optional["capo_workdocs.types.order_type.OrderType"] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
        type: Optional[
            "capo_workdocs.types.folder_content_type.FolderContentType"
        ] = None,
        include: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
    ) -> "Iterator[capo_workdocs.types.describe_folder_contents_response.DescribeFolderContentsResponse]":
        _token = marker
        while True:
            _response = self.describe_folder_contents(
                folder_id,
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                sort=sort,
                order=order,
                limit=limit,
                marker=_token,
                type=type,
                include=include,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_groups(
        self,
        search_query: "capo_workdocs.types.search_query_type.SearchQueryType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        organization_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        marker: Optional["capo_workdocs.types.marker_type.MarkerType"] = None,
        limit: Optional[
            "capo_workdocs.types.positive_integer_type.PositiveIntegerType"
        ] = None,
    ) -> "capo_workdocs.types.describe_groups_response.DescribeGroupsResponse":
        """<p>Describes the groups specified by the query. Groups are defined by the underlying Active Directory.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            search_query: <p>A query to describe groups by group name.</p>
            organization_id: <p>The ID of the organization.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            limit: <p>The maximum number of items to return with this call.</p>

        Raises:
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.describe_groups_request.DescribeGroupsRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.describe_groups_response.DescribeGroupsResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.describe_groups

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.describe_groups.describe_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.describe_groups_request.DescribeGroupsRequest = {
            "search_query": search_query
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_groups(
        self,
        search_query: "capo_workdocs.types.search_query_type.SearchQueryType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        organization_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        marker: Optional["capo_workdocs.types.marker_type.MarkerType"] = None,
        limit: Optional[
            "capo_workdocs.types.positive_integer_type.PositiveIntegerType"
        ] = None,
    ) -> "Iterator[capo_workdocs.types.group_metadata.GroupMetadata]":
        _token = marker
        while True:
            _response = self.describe_groups(
                search_query,
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                organization_id=organization_id,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_notification_subscriptions(
        self,
        organization_id: "capo_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
    ) -> "capo_workdocs.types.describe_notification_subscriptions_response.DescribeNotificationSubscriptionsResponse":
        """<p>Lists the specified notification subscriptions.</p>

        Args:
            organization_id: <p>The ID of the organization.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            limit: <p>The maximum number of items to return with this call.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.describe_notification_subscriptions_request.DescribeNotificationSubscriptionsRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.describe_notification_subscriptions_response.DescribeNotificationSubscriptionsResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.describe_notification_subscriptions

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.describe_notification_subscriptions.describe_notification_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.describe_notification_subscriptions_request.DescribeNotificationSubscriptionsRequest = {
            "organization_id": organization_id
        }
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_notification_subscriptions(
        self,
        organization_id: "capo_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
    ) -> "Iterator[capo_workdocs.types.subscription.Subscription]":
        _token = marker
        while True:
            _response = self.describe_notification_subscriptions(
                organization_id,
                config_overrides=config_overrides,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_resource_permissions(
        self,
        resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        principal_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
    ) -> "capo_workdocs.types.describe_resource_permissions_response.DescribeResourcePermissionsResponse":
        """<p>Describes the permissions of a specified resource.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource.</p>
            principal_id: <p>The ID of the principal to filter permissions by.</p>
            limit: <p>The maximum number of items to return with this call.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call)</p>

        Raises:
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.describe_resource_permissions_request.DescribeResourcePermissionsRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.describe_resource_permissions_response.DescribeResourcePermissionsResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.describe_resource_permissions

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.describe_resource_permissions.describe_resource_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.describe_resource_permissions_request.DescribeResourcePermissionsRequest = {
            "resource_id": resource_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if principal_id is not None:
            input_["principal_id"] = principal_id
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_resource_permissions(
        self,
        resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        principal_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
    ) -> "Iterator[capo_workdocs.types.principal.Principal]":
        _token = marker
        while True:
            _response = self.describe_resource_permissions(
                resource_id,
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                principal_id=principal_id,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("principals",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_root_folders(
        self,
        authentication_token: "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
    ) -> (
        "capo_workdocs.types.describe_root_folders_response.DescribeRootFoldersResponse"
    ):
        """<p>Describes the current user's special folders; the <code>RootFolder</code> and the <code>RecycleBin</code>. <code>RootFolder</code> is the root of user's files and folders and <code>RecycleBin</code> is the root of recycled items. This is not a valid action for SigV4 (administrative API) clients.</p> <p>This action requires an authentication token. To get an authentication token, register an application with Amazon WorkDocs. For more information, see <a href="https://docs.aws.amazon.com/workdocs/latest/developerguide/wd-auth-user.html">Authentication and Access Control for User Applications</a> in the <i>Amazon WorkDocs Developer Guide</i>.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token.</p>
            limit: <p>The maximum number of items to return.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>

        Raises:
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.describe_root_folders_request.DescribeRootFoldersRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.describe_root_folders_response.DescribeRootFoldersResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.describe_root_folders

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.describe_root_folders.describe_root_folders(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.describe_root_folders_request.DescribeRootFoldersRequest = {
            "authentication_token": authentication_token
        }
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_root_folders(
        self,
        authentication_token: "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
    ) -> "Iterator[capo_workdocs.types.folder_metadata.FolderMetadata]":
        _token = marker
        while True:
            _response = self.describe_root_folders(
                authentication_token,
                config_overrides=config_overrides,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("folders",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def describe_users(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        organization_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        user_ids: Optional["capo_workdocs.types.user_ids_type.UserIdsType"] = None,
        query: Optional["capo_workdocs.types.search_query_type.SearchQueryType"] = None,
        include: Optional["capo_workdocs.types.user_filter_type.UserFilterType"] = None,
        order: Optional["capo_workdocs.types.order_type.OrderType"] = None,
        sort: Optional["capo_workdocs.types.user_sort_type.UserSortType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        fields: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
    ) -> "capo_workdocs.types.describe_users_response.DescribeUsersResponse":
        """<p>Describes the specified users. You can describe all users or filter the results (for example, by status or organization).</p> <p>By default, Amazon WorkDocs returns the first 24 active or pending users. If there are more results, the response includes a marker that you can use to request the next set of results.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            organization_id: <p>The ID of the organization.</p>
            user_ids: <p>The IDs of the users.</p>
            query: <p>A query to filter users by user name. Remember the following about the <code>Userids</code> and <code>Query</code> parameters:</p> <ul> <li> <p>If you don't use either parameter, the API returns a paginated list of all users on the site.</p> </li> <li> <p>If you use both parameters, the API ignores the <code>Query</code> parameter.</p> </li> <li> <p>The <code>Userid</code> parameter only returns user names that match a corresponding user ID.</p> </li> <li> <p>The <code>Query</code> parameter runs a "prefix" search for users by the <code>GivenName</code>, <code>SurName</code>, or <code>UserName</code> fields included in a <a href="https://docs.aws.amazon.com/workdocs/latest/APIReference/API_CreateUser.html">CreateUser</a> API call. For example, querying on <code>Ma</code> returns Márcia Oliveira, María García, and Mateo Jackson. If you use multiple characters, the API only returns data that matches all characters. For example, querying on <code>Ma J</code> only returns Mateo Jackson.</p> </li> </ul>
            include: <p>The state of the users. Specify "ALL" to include inactive users.</p>
            order: <p>The order for the results.</p>
            sort: <p>The sorting criteria.</p>
            marker: <p>The marker for the next set of results. (You received this marker from a previous call.)</p>
            limit: <p>The maximum number of items to return.</p>
            fields: <p>A comma-separated list of values. Specify "STORAGE_METADATA" to include the user storage quota and utilization information.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.requested_entity_too_large_exception.RequestedEntityTooLargeException: <p>The response is too large to return. The request must include a filter to reduce the size of the response.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.describe_users_request.DescribeUsersRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.describe_users_response.DescribeUsersResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.describe_users

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.describe_users.describe_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.describe_users_request.DescribeUsersRequest = {}
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if user_ids is not None:
            input_["user_ids"] = user_ids
        if query is not None:
            input_["query"] = query
        if include is not None:
            input_["include"] = include
        if order is not None:
            input_["order"] = order
        if sort is not None:
            input_["sort"] = sort
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit
        if fields is not None:
            input_["fields"] = fields

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_users(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        organization_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        user_ids: Optional["capo_workdocs.types.user_ids_type.UserIdsType"] = None,
        query: Optional["capo_workdocs.types.search_query_type.SearchQueryType"] = None,
        include: Optional["capo_workdocs.types.user_filter_type.UserFilterType"] = None,
        order: Optional["capo_workdocs.types.order_type.OrderType"] = None,
        sort: Optional["capo_workdocs.types.user_sort_type.UserSortType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        fields: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
    ) -> "Iterator[capo_workdocs.types.user.User]":
        _token = marker
        while True:
            _response = self.describe_users(
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                organization_id=organization_id,
                user_ids=user_ids,
                query=query,
                include=include,
                order=order,
                sort=sort,
                marker=_token,
                limit=limit,
                fields=fields,
            )
            _page = _resolve_path(_response, ("users",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def get_current_user(
        self,
        authentication_token: "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
    ) -> "capo_workdocs.types.get_current_user_response.GetCurrentUserResponse":
        """<p>Retrieves details of the current user for whom the authentication token was generated. This is not a valid action for SigV4 (administrative API) clients.</p> <p>This action requires an authentication token. To get an authentication token, register an application with Amazon WorkDocs. For more information, see <a href="https://docs.aws.amazon.com/workdocs/latest/developerguide/wd-auth-user.html">Authentication and Access Control for User Applications</a> in the <i>Amazon WorkDocs Developer Guide</i>.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.get_current_user_request.GetCurrentUserRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.get_current_user_response.GetCurrentUserResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.get_current_user

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.get_current_user.get_current_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.get_current_user_request.GetCurrentUserRequest = {
            "authentication_token": authentication_token
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_document(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        include_custom_metadata: Optional[
            "capo_workdocs.types.boolean_type.BooleanType"
        ] = None,
    ) -> "capo_workdocs.types.get_document_response.GetDocumentResponse":
        """<p>Retrieves details of a document.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            include_custom_metadata: <p>Set this to <code>TRUE</code> to include custom metadata in the response.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.invalid_password_exception.InvalidPasswordException: <p>The password is invalid.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.get_document_request.GetDocumentRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.get_document_response.GetDocumentResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.get_document

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.get_document.get_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.get_document_request.GetDocumentRequest = {
            "document_id": document_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if include_custom_metadata is not None:
            input_["include_custom_metadata"] = include_custom_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_document_path(
        self,
        document_id: "capo_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        fields: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
    ) -> "capo_workdocs.types.get_document_path_response.GetDocumentPathResponse":
        """<p>Retrieves the path information (the hierarchy from the root folder) for the requested document.</p> <p>By default, Amazon WorkDocs returns a maximum of 100 levels upwards from the requested document and only includes the IDs of the parent folders in the path. You can limit the maximum number of levels. You can also request the names of the parent folders.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            limit: <p>The maximum number of levels in the hierarchy to return.</p>
            fields: <p>A comma-separated list of values. Specify <code>NAME</code> to include the names of the parent folders.</p>
            marker: <p>This value is not supported.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.get_document_path_request.GetDocumentPathRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.get_document_path_response.GetDocumentPathResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.get_document_path

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.get_document_path.get_document_path(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.get_document_path_request.GetDocumentPathRequest = {
            "document_id": document_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if limit is not None:
            input_["limit"] = limit
        if fields is not None:
            input_["fields"] = fields
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_document_version(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        fields: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
        include_custom_metadata: Optional[
            "capo_workdocs.types.boolean_type.BooleanType"
        ] = None,
    ) -> "capo_workdocs.types.get_document_version_response.GetDocumentVersionResponse":
        """<p>Retrieves version metadata for the specified document.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The version ID of the document.</p>
            fields: <p>A comma-separated list of values. Specify "SOURCE" to include a URL for the source document.</p>
            include_custom_metadata: <p>Set this to TRUE to include custom metadata in the response.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_password_exception.InvalidPasswordException: <p>The password is invalid.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.get_document_version_request.GetDocumentVersionRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.get_document_version_response.GetDocumentVersionResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.get_document_version

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.get_document_version.get_document_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.get_document_version_request.GetDocumentVersionRequest = {
            "document_id": document_id,
            "version_id": version_id,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if fields is not None:
            input_["fields"] = fields
        if include_custom_metadata is not None:
            input_["include_custom_metadata"] = include_custom_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_folder(
        self,
        folder_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        include_custom_metadata: Optional[
            "capo_workdocs.types.boolean_type.BooleanType"
        ] = None,
    ) -> "capo_workdocs.types.get_folder_response.GetFolderResponse":
        """<p>Retrieves the metadata of the specified folder.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>
            include_custom_metadata: <p>Set to TRUE to include custom metadata in the response.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.get_folder_request.GetFolderRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.get_folder_response.GetFolderResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.get_folder

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.get_folder.get_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.get_folder_request.GetFolderRequest = {
            "folder_id": folder_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if include_custom_metadata is not None:
            input_["include_custom_metadata"] = include_custom_metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_folder_path(
        self,
        folder_id: "capo_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        fields: Optional["capo_workdocs.types.field_names_type.FieldNamesType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
    ) -> "capo_workdocs.types.get_folder_path_response.GetFolderPathResponse":
        """<p>Retrieves the path information (the hierarchy from the root folder) for the specified folder.</p> <p>By default, Amazon WorkDocs returns a maximum of 100 levels upwards from the requested folder and only includes the IDs of the parent folders in the path. You can limit the maximum number of levels. You can also request the parent folder names.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>
            limit: <p>The maximum number of levels in the hierarchy to return.</p>
            fields: <p>A comma-separated list of values. Specify "NAME" to include the names of the parent folders.</p>
            marker: <p>This value is not supported.</p>

        Raises:
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.get_folder_path_request.GetFolderPathRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.get_folder_path_response.GetFolderPathResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.get_folder_path

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.get_folder_path.get_folder_path(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.get_folder_path_request.GetFolderPathRequest = {
            "folder_id": folder_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if limit is not None:
            input_["limit"] = limit
        if fields is not None:
            input_["fields"] = fields
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resources(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        user_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        collection_type: Optional[
            "capo_workdocs.types.resource_collection_type.ResourceCollectionType"
        ] = None,
        limit: Optional["capo_workdocs.types.limit_type.LimitType"] = None,
        marker: Optional["capo_workdocs.types.page_marker_type.PageMarkerType"] = None,
    ) -> "capo_workdocs.types.get_resources_response.GetResourcesResponse":
        """<p>Retrieves a collection of resources, including folders and documents. The only <code>CollectionType</code> supported is <code>SHARED_WITH_ME</code>.</p>

        Args:
            authentication_token: <p>The Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            user_id: <p>The user ID for the resource collection. This is a required field for accessing the API operation using IAM credentials.</p>
            collection_type: <p>The collection type.</p>
            limit: <p>The maximum number of resources to return.</p>
            marker: <p>The marker for the next set of results. This marker was received from a previous call.</p>

        Raises:
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.get_resources_request.GetResourcesRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.get_resources_response.GetResourcesResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.get_resources

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.get_resources.get_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.get_resources_request.GetResourcesRequest = {}
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if user_id is not None:
            input_["user_id"] = user_id
        if collection_type is not None:
            input_["collection_type"] = collection_type
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def initiate_document_version_upload(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        id: Optional["capo_workdocs.types.resource_id_type.ResourceIdType"] = None,
        name: Optional[
            "capo_workdocs.types.resource_name_type.ResourceNameType"
        ] = None,
        content_created_timestamp: Optional[
            "capo_workdocs.types.timestamp_type.TimestampType"
        ] = None,
        content_modified_timestamp: Optional[
            "capo_workdocs.types.timestamp_type.TimestampType"
        ] = None,
        content_type: Optional[
            "capo_workdocs.types.document_content_type.DocumentContentType"
        ] = None,
        document_size_in_bytes: Optional[
            "capo_workdocs.types.size_type.SizeType"
        ] = None,
        parent_folder_id: Optional[
            "capo_workdocs.types.resource_id_type.ResourceIdType"
        ] = None,
    ) -> "capo_workdocs.types.initiate_document_version_upload_response.InitiateDocumentVersionUploadResponse":
        """<p>Creates a new document object and version object.</p> <p>The client specifies the parent folder ID and name of the document to upload. The ID is optionally specified when creating a new version of an existing document. This is the first step to upload a document. Next, upload the document to the URL returned from the call, and then call <a>UpdateDocumentVersion</a>.</p> <p>To cancel the document upload, call <a>AbortDocumentVersionUpload</a>.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            id: <p>The ID of the document.</p>
            name: <p>The name of the document.</p>
            content_created_timestamp: <p>The timestamp when the content of the document was originally created.</p>
            content_modified_timestamp: <p>The timestamp when the content of the document was modified.</p>
            content_type: <p>The content type of the document.</p>
            document_size_in_bytes: <p>The size of the document, in bytes.</p>
            parent_folder_id: <p>The ID of the parent folder.</p>

        Raises:
            capo_workdocs.errors.draft_upload_out_of_sync_exception.DraftUploadOutOfSyncException: <p>This exception is thrown when a valid checkout ID is not presented on document version upload calls for a document that has been checked out from Web client.</p>
            capo_workdocs.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The resource already exists.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.invalid_password_exception.InvalidPasswordException: <p>The password is invalid.</p>
            capo_workdocs.errors.limit_exceeded_exception.LimitExceededException: <p>The maximum of 100,000 files and folders under the parent folder has been exceeded.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.resource_already_checked_out_exception.ResourceAlreadyCheckedOutException: <p>The resource is already checked out.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.storage_limit_exceeded_exception.StorageLimitExceededException: <p>The storage limit has been exceeded.</p>
            capo_workdocs.errors.storage_limit_will_exceed_exception.StorageLimitWillExceedException: <p>The storage limit will be exceeded.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.initiate_document_version_upload_request.InitiateDocumentVersionUploadRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.initiate_document_version_upload_response.InitiateDocumentVersionUploadResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.initiate_document_version_upload

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.initiate_document_version_upload.initiate_document_version_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.initiate_document_version_upload_request.InitiateDocumentVersionUploadRequest = {}
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if id is not None:
            input_["id"] = id
        if name is not None:
            input_["name"] = name
        if content_created_timestamp is not None:
            input_["content_created_timestamp"] = content_created_timestamp
        if content_modified_timestamp is not None:
            input_["content_modified_timestamp"] = content_modified_timestamp
        if content_type is not None:
            input_["content_type"] = content_type
        if document_size_in_bytes is not None:
            input_["document_size_in_bytes"] = document_size_in_bytes
        if parent_folder_id is not None:
            input_["parent_folder_id"] = parent_folder_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_all_resource_permissions(
        self,
        resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Removes all the permissions from the specified resource.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource.</p>

        Raises:
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.remove_all_resource_permissions_request.RemoveAllResourcePermissionsRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.remove_all_resource_permissions

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.remove_all_resource_permissions.remove_all_resource_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.remove_all_resource_permissions_request.RemoveAllResourcePermissionsRequest = {
            "resource_id": resource_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_resource_permission(
        self,
        resource_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        principal_id: "capo_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        principal_type: Optional[
            "capo_workdocs.types.principal_type.PrincipalType"
        ] = None,
    ) -> None:
        """<p>Removes the permission for the specified principal from the specified resource.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            resource_id: <p>The ID of the resource.</p>
            principal_id: <p>The principal ID of the resource.</p>
            principal_type: <p>The principal type of the resource.</p>

        Raises:
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.remove_resource_permission_request.RemoveResourcePermissionRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.remove_resource_permission

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.remove_resource_permission.remove_resource_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.remove_resource_permission_request.RemoveResourcePermissionRequest = {
            "resource_id": resource_id,
            "principal_id": principal_id,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if principal_type is not None:
            input_["principal_type"] = principal_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_document_versions(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
    ) -> None:
        """<p>Recovers a deleted version of an Amazon WorkDocs document.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>

        Raises:
            capo_workdocs.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource hierarchy is changing.</p>
            capo_workdocs.errors.conflicting_operation_exception.ConflictingOperationException: <p>Another operation is in progress on the resource that conflicts with the current operation.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is invalid.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.restore_document_versions_request.RestoreDocumentVersionsRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.restore_document_versions

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.restore_document_versions.restore_document_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.restore_document_versions_request.RestoreDocumentVersionsRequest = {
            "document_id": document_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_resources(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        query_text: Optional[
            "capo_workdocs.types.search_query_type.SearchQueryType"
        ] = None,
        query_scopes: Optional[
            "capo_workdocs.types.search_query_scope_type_list.SearchQueryScopeTypeList"
        ] = None,
        organization_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        additional_response_fields: Optional[
            "capo_workdocs.types.additional_response_fields_list.AdditionalResponseFieldsList"
        ] = None,
        filters: Optional["capo_workdocs.types.filters.Filters"] = None,
        order_by: Optional[
            "capo_workdocs.types.search_result_sort_list.SearchResultSortList"
        ] = None,
        limit: Optional[
            "capo_workdocs.types.search_results_limit_type.SearchResultsLimitType"
        ] = None,
        marker: Optional["capo_workdocs.types.next_marker_type.NextMarkerType"] = None,
    ) -> "capo_workdocs.types.search_resources_response.SearchResourcesResponse":
        """<p>Searches metadata and the content of folders, documents, document versions, and comments.</p>

        Args:
            authentication_token: <p>WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            query_text: <p>The String to search for. Searches across different text fields based on request parameters. Use double quotes around the query string for exact phrase matches.</p>
            query_scopes: <p>Filter based on the text field type. A Folder has only a name and no content. A Comment has only content and no name. A Document or Document Version has a name and content</p>
            organization_id: <p>Filters based on the resource owner OrgId. This is a mandatory parameter when using Admin SigV4 credentials.</p>
            additional_response_fields: <p>A list of attributes to include in the response. Used to request fields that are not normally returned in a standard response.</p>
            filters: <p>Filters results based on entity metadata.</p>
            order_by: <p>Order by results in one or more categories.</p>
            limit: <p>Max results count per page.</p>
            marker: <p>The marker for the next set of results.</p>

        Raises:
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.search_resources_request.SearchResourcesRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.search_resources_response.SearchResourcesResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.search_resources

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.search_resources.search_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.search_resources_request.SearchResourcesRequest = {}
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if query_text is not None:
            input_["query_text"] = query_text
        if query_scopes is not None:
            input_["query_scopes"] = query_scopes
        if organization_id is not None:
            input_["organization_id"] = organization_id
        if additional_response_fields is not None:
            input_["additional_response_fields"] = additional_response_fields
        if filters is not None:
            input_["filters"] = filters
        if order_by is not None:
            input_["order_by"] = order_by
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_search_resources(
        self,
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        query_text: Optional[
            "capo_workdocs.types.search_query_type.SearchQueryType"
        ] = None,
        query_scopes: Optional[
            "capo_workdocs.types.search_query_scope_type_list.SearchQueryScopeTypeList"
        ] = None,
        organization_id: Optional["capo_workdocs.types.id_type.IdType"] = None,
        additional_response_fields: Optional[
            "capo_workdocs.types.additional_response_fields_list.AdditionalResponseFieldsList"
        ] = None,
        filters: Optional["capo_workdocs.types.filters.Filters"] = None,
        order_by: Optional[
            "capo_workdocs.types.search_result_sort_list.SearchResultSortList"
        ] = None,
        limit: Optional[
            "capo_workdocs.types.search_results_limit_type.SearchResultsLimitType"
        ] = None,
        marker: Optional["capo_workdocs.types.next_marker_type.NextMarkerType"] = None,
    ) -> "Iterator[capo_workdocs.types.response_item.ResponseItem]":
        _token = marker
        while True:
            _response = self.search_resources(
                config_overrides=config_overrides,
                authentication_token=authentication_token,
                query_text=query_text,
                query_scopes=query_scopes,
                organization_id=organization_id,
                additional_response_fields=additional_response_fields,
                filters=filters,
                order_by=order_by,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    def update_document(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        name: Optional[
            "capo_workdocs.types.resource_name_type.ResourceNameType"
        ] = None,
        parent_folder_id: Optional[
            "capo_workdocs.types.resource_id_type.ResourceIdType"
        ] = None,
        resource_state: Optional[
            "capo_workdocs.types.resource_state_type.ResourceStateType"
        ] = None,
    ) -> None:
        """<p>Updates the specified attributes of a document. The user must have access to both the document and its parent folder, if applicable.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            name: <p>The name of the document.</p>
            parent_folder_id: <p>The ID of the parent folder.</p>
            resource_state: <p>The resource state of the document. Only ACTIVE and RECYCLED are supported.</p>

        Raises:
            capo_workdocs.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource hierarchy is changing.</p>
            capo_workdocs.errors.conflicting_operation_exception.ConflictingOperationException: <p>Another operation is in progress on the resource that conflicts with the current operation.</p>
            capo_workdocs.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The resource already exists.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.limit_exceeded_exception.LimitExceededException: <p>The maximum of 100,000 files and folders under the parent folder has been exceeded.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.update_document_request.UpdateDocumentRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.update_document

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.update_document.update_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.update_document_request.UpdateDocumentRequest = {
            "document_id": document_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if name is not None:
            input_["name"] = name
        if parent_folder_id is not None:
            input_["parent_folder_id"] = parent_folder_id
        if resource_state is not None:
            input_["resource_state"] = resource_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_document_version(
        self,
        document_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        version_id: "capo_workdocs.types.document_version_id_type.DocumentVersionIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        version_status: Optional[
            "capo_workdocs.types.document_version_status.DocumentVersionStatus"
        ] = None,
    ) -> None:
        """<p>Changes the status of the document version to ACTIVE. </p> <p>Amazon WorkDocs also sets its document container to ACTIVE. This is the last step in a document upload, after the client uploads the document to an S3-presigned URL returned by <a>InitiateDocumentVersionUpload</a>. </p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            document_id: <p>The ID of the document.</p>
            version_id: <p>The version ID of the document.</p>
            version_status: <p>The status of the version.</p>

        Raises:
            capo_workdocs.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource hierarchy is changing.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is invalid.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.update_document_version_request.UpdateDocumentVersionRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.update_document_version

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.update_document_version.update_document_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.update_document_version_request.UpdateDocumentVersionRequest = {
            "document_id": document_id,
            "version_id": version_id,
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if version_status is not None:
            input_["version_status"] = version_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_folder(
        self,
        folder_id: "capo_workdocs.types.resource_id_type.ResourceIdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        name: Optional[
            "capo_workdocs.types.resource_name_type.ResourceNameType"
        ] = None,
        parent_folder_id: Optional[
            "capo_workdocs.types.resource_id_type.ResourceIdType"
        ] = None,
        resource_state: Optional[
            "capo_workdocs.types.resource_state_type.ResourceStateType"
        ] = None,
    ) -> None:
        """<p>Updates the specified attributes of the specified folder. The user must have access to both the folder and its parent folder, if applicable.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            folder_id: <p>The ID of the folder.</p>
            name: <p>The name of the folder.</p>
            parent_folder_id: <p>The ID of the parent folder.</p>
            resource_state: <p>The resource state of the folder. Only ACTIVE and RECYCLED are accepted values from the API.</p>

        Raises:
            capo_workdocs.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The resource hierarchy is changing.</p>
            capo_workdocs.errors.conflicting_operation_exception.ConflictingOperationException: <p>Another operation is in progress on the resource that conflicts with the current operation.</p>
            capo_workdocs.errors.entity_already_exists_exception.EntityAlreadyExistsException: <p>The resource already exists.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.limit_exceeded_exception.LimitExceededException: <p>The maximum of 100,000 files and folders under the parent folder has been exceeded.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.update_folder_request.UpdateFolderRequest]",
        ) -> OperationResponse[None]:
            import capo_workdocs._operations.aws_gorilla_boy_service.update_folder

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.update_folder.update_folder(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.update_folder_request.UpdateFolderRequest = {
            "folder_id": folder_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if name is not None:
            input_["name"] = name
        if parent_folder_id is not None:
            input_["parent_folder_id"] = parent_folder_id
        if resource_state is not None:
            input_["resource_state"] = resource_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_user(
        self,
        user_id: "capo_workdocs.types.id_type.IdType",
        *,
        config_overrides: Optional[WorkDocsClientConfig] = None,
        authentication_token: Optional[
            "capo_workdocs.types.authentication_header_type.AuthenticationHeaderType"
        ] = None,
        given_name: Optional[
            "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
        ] = None,
        surname: Optional[
            "capo_workdocs.types.user_attribute_value_type.UserAttributeValueType"
        ] = None,
        type: Optional["capo_workdocs.types.user_type.UserType"] = None,
        storage_rule: Optional[
            "capo_workdocs.types.storage_rule_type.StorageRuleType"
        ] = None,
        time_zone_id: Optional[
            "capo_workdocs.types.time_zone_id_type.TimeZoneIdType"
        ] = None,
        locale: Optional["capo_workdocs.types.locale_type.LocaleType"] = None,
        grant_poweruser_privileges: Optional[
            "capo_workdocs.types.boolean_enum_type.BooleanEnumType"
        ] = None,
    ) -> "capo_workdocs.types.update_user_response.UpdateUserResponse":
        """<p>Updates the specified attributes of the specified user, and grants or revokes administrative privileges to the Amazon WorkDocs site.</p>

        Args:
            authentication_token: <p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>
            user_id: <p>The ID of the user.</p>
            given_name: <p>The given name of the user.</p>
            surname: <p>The surname of the user.</p>
            type: <p>The type of the user.</p>
            storage_rule: <p>The amount of storage for the user.</p>
            time_zone_id: <p>The time zone ID of the user.</p>
            locale: <p>The locale of the user.</p>
            grant_poweruser_privileges: <p>Boolean value to determine whether the user is granted Power user privileges.</p>

        Raises:
            capo_workdocs.errors.deactivating_last_system_user_exception.DeactivatingLastSystemUserException: <p>The last user in the organization is being deactivated.</p>
            capo_workdocs.errors.entity_not_exists_exception.EntityNotExistsException: <p>The resource does not exist.</p>
            capo_workdocs.errors.failed_dependency_exception.FailedDependencyException: <p>The Directory Service cannot reach an on-premises instance. Or a dependency under the control of the organization is failing, such as a connected Active Directory.</p>
            capo_workdocs.errors.illegal_user_state_exception.IllegalUserStateException: <p>The user is undergoing transfer of ownership.</p>
            capo_workdocs.errors.invalid_argument_exception.InvalidArgumentException: <p>The pagination marker or limit fields are not valid.</p>
            capo_workdocs.errors.prohibited_state_exception.ProhibitedStateException: <p>The specified document version is not in the INITIALIZED state.</p>
            capo_workdocs.errors.service_unavailable_exception.ServiceUnavailableException: <p>One or more of the dependencies is unavailable.</p>
            capo_workdocs.errors.unauthorized_operation_exception.UnauthorizedOperationException: <p>The operation is not permitted.</p>
            capo_workdocs.errors.unauthorized_resource_access_exception.UnauthorizedResourceAccessException: <p>The caller does not have access to perform the action on the resource.</p>
            capo_workdocs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workdocs.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "capo_workdocs.types.update_user_response.UpdateUserResponse"
        ]:
            import capo_workdocs._operations.aws_gorilla_boy_service.update_user

            output, http_response = (
                capo_workdocs._operations.aws_gorilla_boy_service.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workdocs.types.update_user_request.UpdateUserRequest = {
            "user_id": user_id
        }
        if authentication_token is not None:
            input_["authentication_token"] = authentication_token
        if given_name is not None:
            input_["given_name"] = given_name
        if surname is not None:
            input_["surname"] = surname
        if type is not None:
            input_["type"] = type
        if storage_rule is not None:
            input_["storage_rule"] = storage_rule
        if time_zone_id is not None:
            input_["time_zone_id"] = time_zone_id
        if locale is not None:
            input_["locale"] = locale
        if grant_poweruser_privileges is not None:
            input_["grant_poweruser_privileges"] = grant_poweruser_privileges

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
