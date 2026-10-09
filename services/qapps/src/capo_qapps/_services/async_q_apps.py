"""Generated from Smithy shape ``com.amazonaws.qapps#QAppsService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_qapps._auth._signers
import capo_qapps._auth._sigv4
from capo_qapps._auth._identity import Credentials
from capo_qapps._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_qapps._auth._zapros_handler import AuthMiddleware
from capo_qapps._pagination import resolve_path as _resolve_path
from capo_qapps._services._aws_config import aaws_config
from capo_qapps._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_qapps.types.amazon_resource_name
    import capo_qapps.types.app_definition_input
    import capo_qapps.types.app_version
    import capo_qapps.types.associate_library_item_review_input
    import capo_qapps.types.associate_q_app_with_user_input
    import capo_qapps.types.batch_create_category_input
    import capo_qapps.types.batch_create_category_input_category_list
    import capo_qapps.types.batch_delete_category_input
    import capo_qapps.types.batch_update_category_input
    import capo_qapps.types.card_value_list
    import capo_qapps.types.category_id_list
    import capo_qapps.types.category_list_input
    import capo_qapps.types.create_library_item_input
    import capo_qapps.types.create_library_item_output
    import capo_qapps.types.create_presigned_url_input
    import capo_qapps.types.create_presigned_url_output
    import capo_qapps.types.create_q_app_input
    import capo_qapps.types.create_q_app_output
    import capo_qapps.types.delete_category_input_list
    import capo_qapps.types.delete_library_item_input
    import capo_qapps.types.delete_q_app_input
    import capo_qapps.types.describe_q_app_permissions_input
    import capo_qapps.types.describe_q_app_permissions_output
    import capo_qapps.types.description
    import capo_qapps.types.disassociate_library_item_review_input
    import capo_qapps.types.disassociate_q_app_from_user_input
    import capo_qapps.types.document_scope
    import capo_qapps.types.export_q_app_session_data_input
    import capo_qapps.types.export_q_app_session_data_output
    import capo_qapps.types.filename
    import capo_qapps.types.get_library_item_input
    import capo_qapps.types.get_library_item_output
    import capo_qapps.types.get_q_app_input
    import capo_qapps.types.get_q_app_output
    import capo_qapps.types.get_q_app_session_input
    import capo_qapps.types.get_q_app_session_metadata_input
    import capo_qapps.types.get_q_app_session_metadata_output
    import capo_qapps.types.get_q_app_session_output
    import capo_qapps.types.import_document_input
    import capo_qapps.types.import_document_output
    import capo_qapps.types.instance_id
    import capo_qapps.types.library_item_member
    import capo_qapps.types.library_item_status
    import capo_qapps.types.list_categories_input
    import capo_qapps.types.list_categories_output
    import capo_qapps.types.list_library_items_input
    import capo_qapps.types.list_library_items_output
    import capo_qapps.types.list_q_app_session_data_input
    import capo_qapps.types.list_q_app_session_data_output
    import capo_qapps.types.list_q_apps_input
    import capo_qapps.types.list_q_apps_output
    import capo_qapps.types.list_tags_for_resource_request
    import capo_qapps.types.list_tags_for_resource_response
    import capo_qapps.types.page_limit
    import capo_qapps.types.pagination_token
    import capo_qapps.types.permissions_input_list
    import capo_qapps.types.predict_q_app_input
    import capo_qapps.types.predict_q_app_input_options
    import capo_qapps.types.predict_q_app_output
    import capo_qapps.types.session_name
    import capo_qapps.types.session_sharing_configuration
    import capo_qapps.types.start_q_app_session_input
    import capo_qapps.types.start_q_app_session_output
    import capo_qapps.types.stop_q_app_session_input
    import capo_qapps.types.tag_keys
    import capo_qapps.types.tag_map
    import capo_qapps.types.tag_resource_request
    import capo_qapps.types.tag_resource_response
    import capo_qapps.types.tags
    import capo_qapps.types.title
    import capo_qapps.types.untag_resource_request
    import capo_qapps.types.untag_resource_response
    import capo_qapps.types.update_library_item_input
    import capo_qapps.types.update_library_item_metadata_input
    import capo_qapps.types.update_library_item_output
    import capo_qapps.types.update_q_app_input
    import capo_qapps.types.update_q_app_output
    import capo_qapps.types.update_q_app_permissions_input
    import capo_qapps.types.update_q_app_permissions_output
    import capo_qapps.types.update_q_app_session_input
    import capo_qapps.types.update_q_app_session_metadata_input
    import capo_qapps.types.update_q_app_session_metadata_output
    import capo_qapps.types.update_q_app_session_output
    import capo_qapps.types.user_app_item
    import capo_qapps.types.uuid


class AsyncQAppsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncQAppsClient:
    """A client for the ``QApps`` service.

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
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncQAppsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncQAppsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncQAppsClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def associate_library_item_review(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        library_item_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> None:
        """<p>Associates a rating or review for a library item with the user submitting the request. This increments the rating count for the specified library item.</p>

        Args:
            instance_id: <p>The unique identifier for the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the library item to associate the review with.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.conflict_exception.ConflictException: <p>The requested operation could not be completed due to a conflict with the current state of the resource.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Increase the rating counter by 1 for the related app for this user

            >>> await client.associate_library_item_review(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', library_item_id='cb9ecf72-8563-450d-9db9-994f98297316')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.associate_library_item_review_input.AssociateLibraryItemReviewInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.associate_library_item_review

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.associate_library_item_review.async_associate_library_item_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.associate_library_item_review_input.AssociateLibraryItemReviewInput = {
            "instance_id": instance_id,
            "library_item_id": library_item_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_q_app_with_user(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        app_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> None:
        """<p>This operation creates a link between the user's identity calling the operation and a specific Q App. This is useful to mark the Q App as a <i>favorite</i> for the user if the user doesn't own the Amazon Q App so they can still run it and see it in their inventory of Q Apps.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The ID of the Amazon Q App to associate with the user.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Links an Amazon Q App to the invoker's list of apps

            >>> await client.associate_q_app_with_user(app_id='393e77fb-0a30-4f47-ad30-75d71aeaed8a', instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.associate_q_app_with_user_input.AssociateQAppWithUserInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.associate_q_app_with_user

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.associate_q_app_with_user.async_associate_q_app_with_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.associate_q_app_with_user_input.AssociateQAppWithUserInput = {
            "instance_id": instance_id,
            "app_id": app_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_create_category(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        categories: "capo_qapps.types.batch_create_category_input_category_list.BatchCreateCategoryInputCategoryList",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> None:
        """<p>Creates Categories for the Amazon Q Business application environment instance. Web experience users use Categories to tag and filter library items. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-custom-labels.html">Custom labels for Amazon Q Apps</a>.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            categories: <p>The list of category objects to be created</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.conflict_exception.ConflictException: <p>The requested operation could not be completed due to a conflict with the current state of the resource.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Creates the categories for the library

            >>> await client.batch_create_category(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', categories=[{'id': '549abfe0-f5c4-45a2-bb9b-c05987a49c6d', 'title': 'HR'}, {'id': '18cbebaa-196a-4aa5-a840-88d548e07f8f', 'title': 'Marketing'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.batch_create_category_input.BatchCreateCategoryInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.batch_create_category

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.batch_create_category.async_batch_create_category(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.batch_create_category_input.BatchCreateCategoryInput = {
            "instance_id": instance_id,
            "categories": categories,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_category(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        categories: "capo_qapps.types.delete_category_input_list.DeleteCategoryInputList",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> None:
        """<p>Deletes Categories for the Amazon Q Business application environment instance. Web experience users use Categories to tag and filter library items. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-custom-labels.html">Custom labels for Amazon Q Apps</a>.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            categories: <p>The list of IDs of the categories to be deleted.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.conflict_exception.ConflictException: <p>The requested operation could not be completed due to a conflict with the current state of the resource.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Deletes the categories in the library

            >>> await client.batch_delete_category(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', categories=['9c871ed4-1c41-4065-aefe-321cd4b61cf8'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.batch_delete_category_input.BatchDeleteCategoryInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.batch_delete_category

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.batch_delete_category.async_batch_delete_category(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.batch_delete_category_input.BatchDeleteCategoryInput = {
            "instance_id": instance_id,
            "categories": categories,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_category(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        categories: "capo_qapps.types.category_list_input.CategoryListInput",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> None:
        """<p>Updates Categories for the Amazon Q Business application environment instance. Web experience users use Categories to tag and filter library items. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-custom-labels.html">Custom labels for Amazon Q Apps</a>.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            categories: <p>The list of categories to be updated with their new values.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.conflict_exception.ConflictException: <p>The requested operation could not be completed due to a conflict with the current state of the resource.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updates the categories in the library

            >>> await client.batch_update_category(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', categories=[{'id': '549abfe0-f5c4-45a2-bb9b-c05987a49c6d', 'title': 'HR Management'}, {'id': '18cbebaa-196a-4aa5-a840-88d548e07f8f', 'title': 'Sales'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.batch_update_category_input.BatchUpdateCategoryInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.batch_update_category

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.batch_update_category.async_batch_update_category(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.batch_update_category_input.BatchUpdateCategoryInput = {
            "instance_id": instance_id,
            "categories": categories,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_library_item(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        app_id: "capo_qapps.types.uuid.UUID",
        app_version: "capo_qapps.types.app_version.AppVersion",
        categories: "capo_qapps.types.category_id_list.CategoryIdList",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> "capo_qapps.types.create_library_item_output.CreateLibraryItemOutput":
        """<p>Creates a new library item for an Amazon Q App, allowing it to be discovered and used by other allowed users. </p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Amazon Q App to publish to the library.</p>
            app_version: <p>The version of the Amazon Q App to publish to the library.</p>
            categories: <p>The categories to associate with the library item for easier discovery.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a Library Item

            >>> await client.create_library_item(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', app_id='7a11f34b-42d4-4bc8-b668-ae4a788dae1e', app_version=6, categories=['9c871ed4-1c41-4065-aefe-321cd4b61cf8'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.create_library_item_input.CreateLibraryItemInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.create_library_item_output.CreateLibraryItemOutput"
        ]:
            import capo_qapps._operations.q_apps_service.create_library_item

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.create_library_item.async_create_library_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.create_library_item_input.CreateLibraryItemInput = {
            "instance_id": instance_id,
            "app_id": app_id,
            "app_version": app_version,
            "categories": categories,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_presigned_url(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        card_id: "capo_qapps.types.uuid.UUID",
        app_id: "capo_qapps.types.uuid.UUID",
        file_contents_sha256: str,
        file_name: "capo_qapps.types.filename.Filename",
        scope: "capo_qapps.types.document_scope.DocumentScope",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        session_id: Optional["capo_qapps.types.uuid.UUID"] = None,
    ) -> "capo_qapps.types.create_presigned_url_output.CreatePresignedUrlOutput":
        """<p>Creates a presigned URL for an S3 POST operation to upload a file. You can use this URL to set a default file for a <code>FileUploadCard</code> in a Q App definition or to provide a file for a single Q App run. The <code>scope</code> parameter determines how the file will be used, either at the app definition level or the app session level.</p> <note> <p>The IAM permissions are derived from the <code>qapps:ImportDocument</code> action. For more information on the IAM policy for Amazon Q Apps, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/deploy-q-apps-iam-permissions.html">IAM permissions for using Amazon Q Apps</a>.</p> </note>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            card_id: <p>The unique identifier of the card the file is associated with.</p>
            app_id: <p>The unique identifier of the Q App the file is associated with.</p>
            file_contents_sha256: <p>The Base64-encoded SHA-256 digest of the contents of the file to be uploaded.</p>
            file_name: <p>The name of the file to be uploaded.</p>
            scope: <p>Whether the file is associated with a Q App definition or a specific Q App session.</p>
            session_id: <p>The unique identifier of the Q App session the file is associated with, if applicable.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Upload a file to a specific session

            >>> await client.create_presigned_url(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', file_contents_sha256='wXY7GD8m4fmHhdtuQyBdXzNQpdCseVwBcOBIlzfm+kg=', file_name='myFile.txt', card_id='82f69028-22a9-4bea-8727-0eabf58e9fed', app_id='4263767c-d889-4cb2-a8f6-8b649bc66af0', scope='SESSION', session_id='4f0e5b87-9d38-41cd-9eb4-ebce2f2917cc')
            Upload a file into a application

            >>> await client.create_presigned_url(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', file_contents_sha256='wXY7GD8m4fmHhdtuQyBdXzNQpdCseVwBcOBIlzfm+kg=', file_name='anApplicationFile.txt', app_id='4263767c-d889-4cb2-a8f6-8b649bc66af0', card_id='7a11f34b-42d4-4bc8-b668-ae4a788dae1e', scope='APPLICATION')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.create_presigned_url_input.CreatePresignedUrlInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.create_presigned_url_output.CreatePresignedUrlOutput"
        ]:
            import capo_qapps._operations.q_apps_service.create_presigned_url

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.create_presigned_url.async_create_presigned_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.create_presigned_url_input.CreatePresignedUrlInput = {
            "instance_id": instance_id,
            "card_id": card_id,
            "app_id": app_id,
            "file_contents_sha256": file_contents_sha256,
            "file_name": file_name,
            "scope": scope,
        }
        if session_id is not None:
            input_["session_id"] = session_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_q_app(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        title: "capo_qapps.types.title.Title",
        app_definition: "capo_qapps.types.app_definition_input.AppDefinitionInput",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        description: Optional["capo_qapps.types.description.Description"] = None,
        tags: Optional["capo_qapps.types.tag_map.TagMap"] = None,
    ) -> "capo_qapps.types.create_q_app_output.CreateQAppOutput":
        """<p>Creates a new Amazon Q App based on the provided definition. The Q App definition specifies the cards and flow of the Q App. This operation also calculates the dependencies between the cards by inspecting the references in the prompts. </p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            title: <p>The title of the new Q App.</p>
            description: <p>The description of the new Q App.</p>
            app_definition: <p>The definition of the new Q App, specifying the cards and flow.</p>
            tags: <p>Optional tags to associate with the new Q App.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.conflict_exception.ConflictException: <p>The requested operation could not be completed due to a conflict with the current state of the resource.</p>
            capo_qapps.errors.content_too_large_exception.ContentTooLargeException: <p>The requested operation could not be completed because the content exceeds the maximum allowed size.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            A basic application with 1 text input card and 1 output card

            >>> await client.create_q_app(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', title='Color Palette Generator', app_definition={'cards': [{'textInput': {'type': 'text-input', 'title': 'Color Base', 'id': '4cf94d96-8819-45c2-98cc-58c56b35c72f'}}, {'qQuery': {'type': 'q-query', 'title': 'Recommended Palette', 'id': '18870b94-1e63-40e0-8c12-669c90ac5acc', 'prompt': 'Recommend me a list of colors that go well with @4cf94d96-8819-45c2-98cc-58c56b35c72f'}}], 'initialPrompt': 'Create an app that recommend a list of colors based on input.'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.create_q_app_input.CreateQAppInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.create_q_app_output.CreateQAppOutput"
        ]:
            import capo_qapps._operations.q_apps_service.create_q_app

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.create_q_app.async_create_q_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.create_q_app_input.CreateQAppInput = {
            "instance_id": instance_id,
            "title": title,
            "app_definition": app_definition,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_library_item(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        library_item_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> None:
        """<p>Deletes a library item for an Amazon Q App, removing it from the library so it can no longer be discovered or used by other users.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the library item to delete.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a library item

            >>> await client.delete_library_item(instance_id='3642ba81-344c-42fd-a480-9119a5a5f26b', library_item_id='72088fd4-78b6-43da-bfb8-8621323c3cfb')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.delete_library_item_input.DeleteLibraryItemInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.delete_library_item

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.delete_library_item.async_delete_library_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.delete_library_item_input.DeleteLibraryItemInput = {
            "instance_id": instance_id,
            "library_item_id": library_item_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_q_app(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        app_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> None:
        """<p>Deletes an Amazon Q App owned by the user. If the Q App was previously published to the library, it is also removed from the library.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Q App to delete.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an Amazon Q App

            >>> await client.delete_q_app(app_id='393e77fb-0a30-4f47-ad30-75d71aeaed8a', instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.delete_q_app_input.DeleteQAppInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.delete_q_app

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.delete_q_app.async_delete_q_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.delete_q_app_input.DeleteQAppInput = {
            "instance_id": instance_id,
            "app_id": app_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_q_app_permissions(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        app_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> "capo_qapps.types.describe_q_app_permissions_output.DescribeQAppPermissionsOutput":
        """<p> Describes read permissions for a Amazon Q App in Amazon Q Business application environment instance.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Amazon Q App for which to retrieve permissions.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe permissions for the app

            >>> await client.describe_q_app_permissions(instance_id='01793661-ad73-4c7d-8eaa-1c95a10151c2', app_id='fe0acf86-49e5-4def-a0c2-40ce0cafee14')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.describe_q_app_permissions_input.DescribeQAppPermissionsInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.describe_q_app_permissions_output.DescribeQAppPermissionsOutput"
        ]:
            import capo_qapps._operations.q_apps_service.describe_q_app_permissions

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.describe_q_app_permissions.async_describe_q_app_permissions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.describe_q_app_permissions_input.DescribeQAppPermissionsInput = {
            "instance_id": instance_id,
            "app_id": app_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_library_item_review(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        library_item_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> None:
        """<p>Removes a rating or review previously submitted by the user for a library item.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the library item to remove the review from.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.conflict_exception.ConflictException: <p>The requested operation could not be completed due to a conflict with the current state of the resource.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Decrease the rating counter by 1 for the related app for this user

            >>> await client.disassociate_library_item_review(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', library_item_id='cb9ecf72-8563-450d-9db9-994f98297316')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.disassociate_library_item_review_input.DisassociateLibraryItemReviewInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.disassociate_library_item_review

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.disassociate_library_item_review.async_disassociate_library_item_review(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.disassociate_library_item_review_input.DisassociateLibraryItemReviewInput = {
            "instance_id": instance_id,
            "library_item_id": library_item_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_q_app_from_user(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        app_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> None:
        """<p>Disassociates a Q App from a user removing the user's access to run the Q App.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Q App to disassociate from the user.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Unlinks an Amazon Q App from the invoker's list of apps

            >>> await client.disassociate_q_app_from_user(app_id='393e77fb-0a30-4f47-ad30-75d71aeaed8a', instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.disassociate_q_app_from_user_input.DisassociateQAppFromUserInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.disassociate_q_app_from_user

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.disassociate_q_app_from_user.async_disassociate_q_app_from_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.disassociate_q_app_from_user_input.DisassociateQAppFromUserInput = {
            "instance_id": instance_id,
            "app_id": app_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_q_app_session_data(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        session_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> (
        "capo_qapps.types.export_q_app_session_data_output.ExportQAppSessionDataOutput"
    ):
        """<p>Exports the collected data of a Q App data collection session.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App data collection session.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.conflict_exception.ConflictException: <p>The requested operation could not be completed due to a conflict with the current state of the resource.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.export_q_app_session_data_input.ExportQAppSessionDataInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.export_q_app_session_data_output.ExportQAppSessionDataOutput"
        ]:
            import capo_qapps._operations.q_apps_service.export_q_app_session_data

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.export_q_app_session_data.async_export_q_app_session_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.export_q_app_session_data_input.ExportQAppSessionDataInput = {
            "instance_id": instance_id,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_library_item(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        library_item_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        app_id: Optional["capo_qapps.types.uuid.UUID"] = None,
    ) -> "capo_qapps.types.get_library_item_output.GetLibraryItemOutput":
        """<p>Retrieves details about a library item for an Amazon Q App, including its metadata, categories, ratings, and usage statistics.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the library item to retrieve.</p>
            app_id: <p>The unique identifier of the Amazon Q App associated with the library item.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve a library item

            >>> await client.get_library_item(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', library_item_id='18cbebaa-196a-4aa5-a840-88d548e07f8f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.get_library_item_input.GetLibraryItemInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.get_library_item_output.GetLibraryItemOutput"
        ]:
            import capo_qapps._operations.q_apps_service.get_library_item

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.get_library_item.async_get_library_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.get_library_item_input.GetLibraryItemInput = {
            "instance_id": instance_id,
            "library_item_id": library_item_id,
        }
        if app_id is not None:
            input_["app_id"] = app_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_q_app(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        app_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        app_version: Optional["capo_qapps.types.app_version.AppVersion"] = None,
    ) -> "capo_qapps.types.get_q_app_output.GetQAppOutput":
        """<p>Retrieves the full details of an Q App, including its definition specifying the cards and flow.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Q App to retrieve.</p>
            app_version: <p>The version of the Q App.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            A basic application with 1 text input card and 1 output card

            >>> await client.get_q_app(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', app_id='3d110749-efc3-427c-87e8-15e966e5c168')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.get_q_app_input.GetQAppInput]",
        ) -> AsyncOperationResponse["capo_qapps.types.get_q_app_output.GetQAppOutput"]:
            import capo_qapps._operations.q_apps_service.get_q_app

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.get_q_app.async_get_q_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.get_q_app_input.GetQAppInput = {
            "instance_id": instance_id,
            "app_id": app_id,
        }
        if app_version is not None:
            input_["app_version"] = app_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_q_app_session(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        session_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> "capo_qapps.types.get_q_app_session_output.GetQAppSessionOutput":
        """<p>Retrieves the current state and results for an active session of an Amazon Q App.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App session to retrieve.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieves an existing session for an Amazon Q App

            >>> await client.get_q_app_session(instance_id='288ae830-1df2-4871-b6c0-4314d74dadef', session_id='1fca878e-64c5-4dc4-b1d9-c93effed4e82')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.get_q_app_session_input.GetQAppSessionInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.get_q_app_session_output.GetQAppSessionOutput"
        ]:
            import capo_qapps._operations.q_apps_service.get_q_app_session

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.get_q_app_session.async_get_q_app_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.get_q_app_session_input.GetQAppSessionInput = {
            "instance_id": instance_id,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_q_app_session_metadata(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        session_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> "capo_qapps.types.get_q_app_session_metadata_output.GetQAppSessionMetadataOutput":
        """<p>Retrieves the current configuration of a Q App session.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App session.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieves an existing session metadata for an Amazon Q App

            >>> await client.get_q_app_session_metadata(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', session_id='56ae47c3-10bc-4c2c-8b27-9b9fe23b3edb')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.get_q_app_session_metadata_input.GetQAppSessionMetadataInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.get_q_app_session_metadata_output.GetQAppSessionMetadataOutput"
        ]:
            import capo_qapps._operations.q_apps_service.get_q_app_session_metadata

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.get_q_app_session_metadata.async_get_q_app_session_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.get_q_app_session_metadata_input.GetQAppSessionMetadataInput = {
            "instance_id": instance_id,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_document(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        card_id: "capo_qapps.types.uuid.UUID",
        app_id: "capo_qapps.types.uuid.UUID",
        file_contents_base64: str,
        file_name: "capo_qapps.types.filename.Filename",
        scope: "capo_qapps.types.document_scope.DocumentScope",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        session_id: Optional["capo_qapps.types.uuid.UUID"] = None,
    ) -> "capo_qapps.types.import_document_output.ImportDocumentOutput":
        """<p>Uploads a file that can then be used either as a default in a <code>FileUploadCard</code> from Q App definition or as a file that is used inside a single Q App run. The purpose of the document is determined by a scope parameter that indicates whether it is at the app definition level or at the app session level.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            card_id: <p>The unique identifier of the card the file is associated with.</p>
            app_id: <p>The unique identifier of the Q App the file is associated with.</p>
            file_contents_base64: <p>The base64-encoded contents of the file to upload.</p>
            file_name: <p>The name of the file being uploaded.</p>
            scope: <p>Whether the file is associated with a Q App definition or a specific Q App session.</p>
            session_id: <p>The unique identifier of the Q App session the file is associated with, if applicable.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.content_too_large_exception.ContentTooLargeException: <p>The requested operation could not be completed because the content exceeds the maximum allowed size.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Upload a file to a specific session

            >>> await client.import_document(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', file_contents_base64='data:text/plain;base64,SomeFileEncodedInBase64', file_name='myFile.txt', card_id='82f69028-22a9-4bea-8727-0eabf58e9fed', app_id='4263767c-d889-4cb2-a8f6-8b649bc66af0', scope='SESSION', session_id='4f0e5b87-9d38-41cd-9eb4-ebce2f2917cc')
            Upload a file into a application

            >>> await client.import_document(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', file_contents_base64='data:text/plain;base64,SomeFileEncodedInBase64', file_name='anApplicationFile.txt', app_id='4263767c-d889-4cb2-a8f6-8b649bc66af0', card_id='7a11f34b-42d4-4bc8-b668-ae4a788dae1e', scope='APPLICATION')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.import_document_input.ImportDocumentInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.import_document_output.ImportDocumentOutput"
        ]:
            import capo_qapps._operations.q_apps_service.import_document

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.import_document.async_import_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.import_document_input.ImportDocumentInput = {
            "instance_id": instance_id,
            "card_id": card_id,
            "app_id": app_id,
            "file_contents_base64": file_contents_base64,
            "file_name": file_name,
            "scope": scope,
        }
        if session_id is not None:
            input_["session_id"] = session_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_categories(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> "capo_qapps.types.list_categories_output.ListCategoriesOutput":
        """<p>Lists the categories of a Amazon Q Business application environment instance. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qapps-custom-labels.html">Custom labels for Amazon Q Apps</a>.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List categories available for the library items in this instance

            >>> await client.list_categories(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.list_categories_input.ListCategoriesInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.list_categories_output.ListCategoriesOutput"
        ]:
            import capo_qapps._operations.q_apps_service.list_categories

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.list_categories.async_list_categories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.list_categories_input.ListCategoriesInput = {
            "instance_id": instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_library_items(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        limit: Optional["capo_qapps.types.page_limit.PageLimit"] = None,
        next_token: Optional[
            "capo_qapps.types.pagination_token.PaginationToken"
        ] = None,
        category_id: Optional["capo_qapps.types.uuid.UUID"] = None,
    ) -> "capo_qapps.types.list_library_items_output.ListLibraryItemsOutput":
        """<p>Lists the library items for Amazon Q Apps that are published and available for users in your Amazon Web Services account.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            limit: <p>The maximum number of library items to return in the response.</p>
            next_token: <p>The token to request the next page of results.</p>
            category_id: <p>Optional category to filter the library items by.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List at most 3 library items for this instance

            >>> await client.list_library_items(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', limit=3)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.list_library_items_input.ListLibraryItemsInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.list_library_items_output.ListLibraryItemsOutput"
        ]:
            import capo_qapps._operations.q_apps_service.list_library_items

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.list_library_items.async_list_library_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.list_library_items_input.ListLibraryItemsInput = {
            "instance_id": instance_id
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if category_id is not None:
            input_["category_id"] = category_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_library_items(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        limit: Optional["capo_qapps.types.page_limit.PageLimit"] = None,
        next_token: Optional[
            "capo_qapps.types.pagination_token.PaginationToken"
        ] = None,
        category_id: Optional["capo_qapps.types.uuid.UUID"] = None,
    ) -> "AsyncIterator[capo_qapps.types.library_item_member.LibraryItemMember]":
        _token = next_token
        while True:
            _response = await self.list_library_items(
                instance_id,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
                category_id=category_id,
            )
            _page = _resolve_path(_response, ("library_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_q_apps(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        limit: Optional["capo_qapps.types.page_limit.PageLimit"] = None,
        next_token: Optional[
            "capo_qapps.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_qapps.types.list_q_apps_output.ListQAppsOutput":
        """<p>Lists the Amazon Q Apps owned by or associated with the user either because they created it or because they used it from the library in the past. The user identity is extracted from the credentials used to invoke this operation..</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            limit: <p>The maximum number of Q Apps to return in the response.</p>
            next_token: <p>The token to request the next page of results.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List at most 3 Amazon Q Apps in an Q Business application

            >>> await client.list_q_apps(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', limit=3)
            Retrieve the next page of Amazon Q Apps

            >>> await client.list_q_apps(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', limit=3, next_token='bXlzdGVyaW91c1BhZ2luYXRpb25Ub2tlbg==')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.list_q_apps_input.ListQAppsInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.list_q_apps_output.ListQAppsOutput"
        ]:
            import capo_qapps._operations.q_apps_service.list_q_apps

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.list_q_apps.async_list_q_apps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.list_q_apps_input.ListQAppsInput = {
            "instance_id": instance_id
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_q_apps(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        limit: Optional["capo_qapps.types.page_limit.PageLimit"] = None,
        next_token: Optional[
            "capo_qapps.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_qapps.types.user_app_item.UserAppItem]":
        _token = next_token
        while True:
            _response = await self.list_q_apps(
                instance_id,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("apps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_q_app_session_data(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        session_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> "capo_qapps.types.list_q_app_session_data_output.ListQAppSessionDataOutput":
        """<p>Lists the collected data of a Q App data collection session.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App data collection session.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.list_q_app_session_data_input.ListQAppSessionDataInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.list_q_app_session_data_output.ListQAppSessionDataOutput"
        ]:
            import capo_qapps._operations.q_apps_service.list_q_app_session_data

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.list_q_app_session_data.async_list_q_app_session_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.list_q_app_session_data_input.ListQAppSessionDataInput = {
            "instance_id": instance_id,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_qapps.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> "capo_qapps.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with an Amazon Q Apps resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags should be listed.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            A call to list tags for a resource

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:qapps:us-west-2:123456789012:application/3642ba81-344c-42fd-a480-9119a5a5f26b/qapp/7212ff04-de7b-4831-bd80-45d6975ba1b0')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_qapps._operations.q_apps_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def predict_q_app(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        options: Optional[
            "capo_qapps.types.predict_q_app_input_options.PredictQAppInputOptions"
        ] = None,
    ) -> "capo_qapps.types.predict_q_app_output.PredictQAppOutput":
        """<p>Generates an Amazon Q App definition based on either a conversation or a problem statement provided as input.The resulting app definition can be used to call <code>CreateQApp</code>. This API doesn't create Amazon Q Apps directly.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            options: <p>The input to generate the Q App definition from, either a conversation or problem statement.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.predict_q_app_input.PredictQAppInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.predict_q_app_output.PredictQAppOutput"
        ]:
            import capo_qapps._operations.q_apps_service.predict_q_app

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.predict_q_app.async_predict_q_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.predict_q_app_input.PredictQAppInput = {
            "instance_id": instance_id
        }
        if options is not None:
            input_["options"] = options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_q_app_session(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        app_id: "capo_qapps.types.uuid.UUID",
        app_version: "capo_qapps.types.app_version.AppVersion",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        initial_values: Optional[
            "capo_qapps.types.card_value_list.CardValueList"
        ] = None,
        session_id: Optional[str] = None,
        tags: Optional["capo_qapps.types.tag_map.TagMap"] = None,
    ) -> "capo_qapps.types.start_q_app_session_output.StartQAppSessionOutput":
        """<p>Starts a new session for an Amazon Q App, allowing inputs to be provided and the app to be run.</p> <note> <p>Each Q App session will be condensed into a single conversation in the web experience.</p> </note>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Q App to start a session for.</p>
            app_version: <p>The version of the Q App to use for the session.</p>
            initial_values: <p>Optional initial input values to provide for the Q App session.</p>
            session_id: <p>The unique identifier of the a Q App session.</p>
            tags: <p>Optional tags to associate with the new Q App session.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Start a session for an Amazon Q App using version 1, passing in initial values for one card

            >>> await client.start_q_app_session(instance_id='4cc5e4c2-d2a2-4188-a114-9ca125b4aedc', app_id='65e7dce7-226a-47f9-b689-22850becef89', app_version=1, initial_values=[{'cardId': '6fb5b404-3b7b-48a4-8a8b-56406922a606', 'value': 'What is the circumference of Earth?'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.start_q_app_session_input.StartQAppSessionInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.start_q_app_session_output.StartQAppSessionOutput"
        ]:
            import capo_qapps._operations.q_apps_service.start_q_app_session

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.start_q_app_session.async_start_q_app_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.start_q_app_session_input.StartQAppSessionInput = {
            "instance_id": instance_id,
            "app_id": app_id,
            "app_version": app_version,
        }
        if initial_values is not None:
            input_["initial_values"] = initial_values
        if session_id is not None:
            input_["session_id"] = session_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_q_app_session(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        session_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> None:
        """<p>Stops an active session for an Amazon Q App.This deletes all data related to the session and makes it invalid for future uses. The results of the session will be persisted as part of the conversation.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App session to stop.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.stop_q_app_session_input.StopQAppSessionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.stop_q_app_session

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.stop_q_app_session.async_stop_q_app_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.stop_q_app_session_input.StopQAppSessionInput = {
            "instance_id": instance_id,
            "session_id": session_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_qapps.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_qapps.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> "capo_qapps.types.tag_resource_response.TagResourceResponse":
        """<p>Associates tags with an Amazon Q Apps resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>The tags to associate with the resource.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.conflict_exception.ConflictException: <p>The requested operation could not be completed due to a conflict with the current state of the resource.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            A call to tag a resource

            >>> await client.tag_resource(resource_arn='arn:aws:qapps:us-west-2:123456789012:application/3642ba81-344c-42fd-a480-9119a5a5f26b/qapp/7212ff04-de7b-4831-bd80-45d6975ba1b0', tags={'department': 'HR'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_qapps._operations.q_apps_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_qapps.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_qapps.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
    ) -> "capo_qapps.types.untag_resource_response.UntagResourceResponse":
        """<p>Disassociates tags from an Amazon Q Apps resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to disassociate the tag from.</p>
            tag_keys: <p>The keys of the tags to disassociate from the resource.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            A call to untag a resource

            >>> await client.untag_resource(resource_arn='arn:aws:qapps:us-west-2:123456789012:application/3642ba81-344c-42fd-a480-9119a5a5f26b/qapp/7212ff04-de7b-4831-bd80-45d6975ba1b0', tag_keys=['department'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_qapps._operations.q_apps_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_library_item(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        library_item_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        status: Optional[
            "capo_qapps.types.library_item_status.LibraryItemStatus"
        ] = None,
        categories: Optional["capo_qapps.types.category_id_list.CategoryIdList"] = None,
    ) -> "capo_qapps.types.update_library_item_output.UpdateLibraryItemOutput":
        """<p>Updates the library item for an Amazon Q App.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the library item to update.</p>
            status: <p>The new status to set for the library item, such as "Published" or "Hidden".</p>
            categories: <p>The new categories to associate with the library item.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.conflict_exception.ConflictException: <p>The requested operation could not be completed due to a conflict with the current state of the resource.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sets the status of a library item to DISABLED

            >>> await client.update_library_item(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', library_item_id='cb9ecf72-8563-450d-9db9-994f98297316', status='DISABLED')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.update_library_item_input.UpdateLibraryItemInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.update_library_item_output.UpdateLibraryItemOutput"
        ]:
            import capo_qapps._operations.q_apps_service.update_library_item

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.update_library_item.async_update_library_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.update_library_item_input.UpdateLibraryItemInput = {
            "instance_id": instance_id,
            "library_item_id": library_item_id,
        }
        if status is not None:
            input_["status"] = status
        if categories is not None:
            input_["categories"] = categories

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_library_item_metadata(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        library_item_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        is_verified: Optional[bool] = None,
    ) -> None:
        """<p>Updates the verification status of a library item for an Amazon Q App.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            library_item_id: <p>The unique identifier of the updated library item.</p>
            is_verified: <p>The verification status of the library item</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.conflict_exception.ConflictException: <p>The requested operation could not be completed due to a conflict with the current state of the resource.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a library item to be verified

            >>> await client.update_library_item_metadata(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', library_item_id='cb9ecf72-8563-450d-9db9-994f98297316', is_verified=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.update_library_item_metadata_input.UpdateLibraryItemMetadataInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_qapps._operations.q_apps_service.update_library_item_metadata

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.update_library_item_metadata.async_update_library_item_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.update_library_item_metadata_input.UpdateLibraryItemMetadataInput = {
            "instance_id": instance_id,
            "library_item_id": library_item_id,
        }
        if is_verified is not None:
            input_["is_verified"] = is_verified

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_q_app(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        app_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        title: Optional["capo_qapps.types.title.Title"] = None,
        description: Optional["capo_qapps.types.description.Description"] = None,
        app_definition: Optional[
            "capo_qapps.types.app_definition_input.AppDefinitionInput"
        ] = None,
    ) -> "capo_qapps.types.update_q_app_output.UpdateQAppOutput":
        """<p>Updates an existing Amazon Q App, allowing modifications to its title, description, and definition.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Q App to update.</p>
            title: <p>The new title for the Q App.</p>
            description: <p>The new description for the Q App.</p>
            app_definition: <p>The new definition specifying the cards and flow for the Q App.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.content_too_large_exception.ContentTooLargeException: <p>The requested operation could not be completed because the content exceeds the maximum allowed size.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updating the title of an app

            >>> await client.update_q_app(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', app_id='7212ff04-de7b-4831-bd80-45d6975ba1b0', title='This is the new title')
            Updating the app so it has a single q-query card

            >>> await client.update_q_app(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', app_id='7212ff04-de7b-4831-bd80-45d6975ba1b0', app_definition={'cards': [{'qQuery': {'type': 'q-query', 'title': 'Trip Ideas', 'id': '18870b94-1e63-40e0-8c12-669c90ac5acc', 'prompt': 'Recommend me an itinerary for a trip'}}]})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.update_q_app_input.UpdateQAppInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.update_q_app_output.UpdateQAppOutput"
        ]:
            import capo_qapps._operations.q_apps_service.update_q_app

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.update_q_app.async_update_q_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.update_q_app_input.UpdateQAppInput = {
            "instance_id": instance_id,
            "app_id": app_id,
        }
        if title is not None:
            input_["title"] = title
        if description is not None:
            input_["description"] = description
        if app_definition is not None:
            input_["app_definition"] = app_definition

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_q_app_permissions(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        app_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        grant_permissions: Optional[
            "capo_qapps.types.permissions_input_list.PermissionsInputList"
        ] = None,
        revoke_permissions: Optional[
            "capo_qapps.types.permissions_input_list.PermissionsInputList"
        ] = None,
    ) -> "capo_qapps.types.update_q_app_permissions_output.UpdateQAppPermissionsOutput":
        """<p>Updates read permissions for a Amazon Q App in Amazon Q Business application environment instance.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            app_id: <p>The unique identifier of the Amazon Q App for which permissions are being updated.</p>
            grant_permissions: <p>The list of permissions to grant for the Amazon Q App.</p>
            revoke_permissions: <p>The list of permissions to revoke for the Amazon Q App.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Grant permissions for the app

            >>> await client.update_q_app_permissions(instance_id='01793661-ad73-4c7d-8eaa-1c95a10151c2', app_id='fe0acf86-49e5-4def-a0c2-40ce0cafee14', grant_permissions=[{'action': 'read', 'principal': 'user2@example.com'}])
            Revoke permissions for the app

            >>> await client.update_q_app_permissions(instance_id='01793661-ad73-4c7d-8eaa-1c95a10151c2', app_id='fe0acf86-49e5-4def-a0c2-40ce0cafee14', revoke_permissions=[{'action': 'read', 'principal': 'user2@example.com'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.update_q_app_permissions_input.UpdateQAppPermissionsInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.update_q_app_permissions_output.UpdateQAppPermissionsOutput"
        ]:
            import capo_qapps._operations.q_apps_service.update_q_app_permissions

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.update_q_app_permissions.async_update_q_app_permissions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.update_q_app_permissions_input.UpdateQAppPermissionsInput = {
            "instance_id": instance_id,
            "app_id": app_id,
        }
        if grant_permissions is not None:
            input_["grant_permissions"] = grant_permissions
        if revoke_permissions is not None:
            input_["revoke_permissions"] = revoke_permissions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_q_app_session(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        session_id: "capo_qapps.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        values: Optional["capo_qapps.types.card_value_list.CardValueList"] = None,
    ) -> "capo_qapps.types.update_q_app_session_output.UpdateQAppSessionOutput":
        """<p>Updates the session for a given Q App <code>sessionId</code>. This is only valid when at least one card of the session is in the <code>WAITING</code> state. Data for each <code>WAITING</code> card can be provided as input. If inputs are not provided, the call will be accepted but session will not move forward. Inputs for cards that are not in the <code>WAITING</code> status will be ignored.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App session to provide input for.</p>
            values: <p>The input values to provide for the current state of the Q App session.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.update_q_app_session_input.UpdateQAppSessionInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.update_q_app_session_output.UpdateQAppSessionOutput"
        ]:
            import capo_qapps._operations.q_apps_service.update_q_app_session

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.update_q_app_session.async_update_q_app_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.update_q_app_session_input.UpdateQAppSessionInput = {
            "instance_id": instance_id,
            "session_id": session_id,
        }
        if values is not None:
            input_["values"] = values

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_q_app_session_metadata(
        self,
        instance_id: "capo_qapps.types.instance_id.InstanceId",
        session_id: "capo_qapps.types.uuid.UUID",
        sharing_configuration: "capo_qapps.types.session_sharing_configuration.SessionSharingConfiguration",
        *,
        config_overrides: Optional[AsyncQAppsClientConfig] = None,
        session_name: Optional["capo_qapps.types.session_name.SessionName"] = None,
    ) -> "capo_qapps.types.update_q_app_session_metadata_output.UpdateQAppSessionMetadataOutput":
        """<p>Updates the configuration metadata of a session for a given Q App <code>sessionId</code>.</p>

        Args:
            instance_id: <p>The unique identifier of the Amazon Q Business application environment instance.</p>
            session_id: <p>The unique identifier of the Q App session to update configuration for.</p>
            session_name: <p>The new name for the Q App session.</p>
            sharing_configuration: <p>The new sharing configuration for the Q App data collection session.</p>

        Raises:
            capo_qapps.errors.access_denied_exception.AccessDeniedException: <p>The client is not authorized to perform the requested operation.</p>
            capo_qapps.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred while processing the request.</p>
            capo_qapps.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_qapps.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The requested operation could not be completed because it would exceed the service's quota or limit.</p>
            capo_qapps.errors.throttling_exception.ThrottlingException: <p>The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.</p>
            capo_qapps.errors.unauthorized_exception.UnauthorizedException: <p>The client is not authenticated or authorized to perform the requested operation.</p>
            capo_qapps.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by the service.</p>
            capo_qapps.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updates an existing session metadata for an Amazon Q App

            >>> await client.update_q_app_session_metadata(instance_id='0b95c9c4-89cc-4aa8-9aae-aa91cbec699f', session_id='56ae47c3-10bc-4c2c-8b27-9b9fe23b3edb', session_name='Trip itinerary collection session', sharing_configuration={'enabled': True, 'acceptResponses': True, 'revealCards': False})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qapps.types.update_q_app_session_metadata_input.UpdateQAppSessionMetadataInput]",
        ) -> AsyncOperationResponse[
            "capo_qapps.types.update_q_app_session_metadata_output.UpdateQAppSessionMetadataOutput"
        ]:
            import capo_qapps._operations.q_apps_service.update_q_app_session_metadata

            (
                output,
                http_response,
            ) = await capo_qapps._operations.q_apps_service.update_q_app_session_metadata.async_update_q_app_session_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qapps.types.update_q_app_session_metadata_input.UpdateQAppSessionMetadataInput = {
            "instance_id": instance_id,
            "session_id": session_id,
            "sharing_configuration": sharing_configuration,
        }
        if session_name is not None:
            input_["session_name"] = session_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
