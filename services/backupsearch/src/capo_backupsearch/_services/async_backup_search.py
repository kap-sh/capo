"""Generated from Smithy shape ``com.amazonaws.backupsearch#CryoBackupSearchService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_backupsearch._auth._signers
import capo_backupsearch._auth._sigv4
from capo_backupsearch._auth._identity import Credentials
from capo_backupsearch._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_backupsearch._auth._zapros_handler import AuthMiddleware
from capo_backupsearch._pagination import resolve_path as _resolve_path
from capo_backupsearch._resources.cryo_backup_search_service.search_job import (
    AsyncSearchJob,
)
from capo_backupsearch._resources.cryo_backup_search_service.search_result_export_job import (
    AsyncSearchResultExportJob,
)
from capo_backupsearch._services._aws_config import aaws_config
from capo_backupsearch._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_backupsearch.types.encryption_key_arn
    import capo_backupsearch.types.export_job_status
    import capo_backupsearch.types.export_specification
    import capo_backupsearch.types.generic_id
    import capo_backupsearch.types.get_search_job_input
    import capo_backupsearch.types.get_search_job_output
    import capo_backupsearch.types.get_search_result_export_job_input
    import capo_backupsearch.types.get_search_result_export_job_output
    import capo_backupsearch.types.iam_role_arn
    import capo_backupsearch.types.item_filters
    import capo_backupsearch.types.list_search_job_backups_input
    import capo_backupsearch.types.list_search_job_backups_output
    import capo_backupsearch.types.list_search_job_results_input
    import capo_backupsearch.types.list_search_job_results_output
    import capo_backupsearch.types.list_search_jobs_input
    import capo_backupsearch.types.list_search_jobs_output
    import capo_backupsearch.types.list_search_result_export_jobs_input
    import capo_backupsearch.types.list_search_result_export_jobs_output
    import capo_backupsearch.types.list_tags_for_resource_request
    import capo_backupsearch.types.list_tags_for_resource_response
    import capo_backupsearch.types.search_job_backups_result
    import capo_backupsearch.types.search_job_state
    import capo_backupsearch.types.search_scope
    import capo_backupsearch.types.start_search_job_input
    import capo_backupsearch.types.start_search_job_output
    import capo_backupsearch.types.start_search_result_export_job_input
    import capo_backupsearch.types.start_search_result_export_job_output
    import capo_backupsearch.types.stop_search_job_input
    import capo_backupsearch.types.stop_search_job_output
    import capo_backupsearch.types.tag_keys
    import capo_backupsearch.types.tag_map
    import capo_backupsearch.types.tag_resource_request
    import capo_backupsearch.types.tag_resource_response
    import capo_backupsearch.types.untag_resource_request
    import capo_backupsearch.types.untag_resource_response


class AsyncBackupSearchClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncBackupSearchClient:
    """A client for the ``BackupSearch`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncBackupSearchClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.search_job = AsyncSearchJob(self)
        self.search_result_export_job = AsyncSearchResultExportJob(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBackupSearchClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBackupSearchClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def list_search_job_backups(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_backupsearch.types.list_search_job_backups_output.ListSearchJobBackupsOutput":
        """<p>This operation returns a list of all backups (recovery points) in a paginated format that were included in the search job.</p> <p>If a search does not display an expected backup in the results, you can call this operation to display each backup included in the search. Any backups that were not included because they have a <code>FAILED</code> status from a permissions issue will be displayed, along with a status message.</p> <p>Only recovery points with a backup index that has a status of <code>ACTIVE</code> will be included in search results. If the index has any other status, its status will be displayed along with a status message.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            next_token: <p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.list_search_job_backups_input.ListSearchJobBackupsInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.list_search_job_backups_output.ListSearchJobBackupsOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_search_job_backups

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.list_search_job_backups.async_list_search_job_backups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.list_search_job_backups_input.ListSearchJobBackupsInput = {
            "search_job_identifier": search_job_identifier
        }
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

    async def iter_list_search_job_backups(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_backupsearch.types.search_job_backups_result.SearchJobBackupsResult]":
        _token = next_token
        while True:
            _response = await self.list_search_job_backups(
                search_job_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_search_job_results(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_backupsearch.types.list_search_job_results_output.ListSearchJobResultsOutput":
        """<p>This operation returns a list of a specified search job.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            next_token: <p>The next item following a partial list of returned search job results.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of search job results, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.list_search_job_results_input.ListSearchJobResultsInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.list_search_job_results_output.ListSearchJobResultsOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_search_job_results

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.list_search_job_results.async_list_search_job_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.list_search_job_results_input.ListSearchJobResultsInput = {
            "search_job_identifier": search_job_identifier
        }
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

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>This operation returns the tags for a resource type.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource.&gt;</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: str,
        tags: "capo_backupsearch.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.tag_resource_response.TagResourceResponse":
        """<p>This operation puts tags on the resource you indicate.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource.</p> <p>This is the resource that will have the indicated tags.</p>
            tags: <p>Required tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - = . _ : /. </p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: str,
        tag_keys: "capo_backupsearch.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.untag_resource_response.UntagResourceResponse":
        """<p>This operation removes tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies the resource where you want to remove tags.</p>
            tag_keys: <p>This required parameter contains the tag keys you want to remove from the source.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.untag_resource_request.UntagResourceRequest = {
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

    async def start_search_job(
        self,
        search_scope: "capo_backupsearch.types.search_scope.SearchScope",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        tags: Optional["capo_backupsearch.types.tag_map.TagMap"] = None,
        name: Optional[str] = None,
        encryption_key_arn: Optional[
            "capo_backupsearch.types.encryption_key_arn.EncryptionKeyArn"
        ] = None,
        client_token: Optional[str] = None,
        item_filters: Optional[
            "capo_backupsearch.types.item_filters.ItemFilters"
        ] = None,
    ) -> "capo_backupsearch.types.start_search_job_output.StartSearchJobOutput":
        """<p>This operation creates a search job which returns recovery points filtered by SearchScope and items filtered by ItemFilters.</p> <p>You can optionally include ClientToken, EncryptionKeyArn, Name, and/or Tags.</p>

        Args:
            tags: <p>List of tags returned by the operation.</p>
            name: <p>Include alphanumeric characters to create a name for this search job.</p>
            encryption_key_arn: <p>The encryption key for the specified search job.</p>
            client_token: <p>Include this parameter to allow multiple identical calls for idempotency.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.</p>
            search_scope: <p>This object can contain BackupResourceTypes, BackupResourceArns, BackupResourceCreationTime, BackupResourceTags, and SourceResourceArns to filter the recovery points returned by the search job.</p>
            item_filters: <p>Item Filters represent all input item properties specified when the search was created.</p> <p>Contains either EBSItemFilters or S3ItemFilters</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request denied due to exceeding the quota limits permitted.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.start_search_job_input.StartSearchJobInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.start_search_job_output.StartSearchJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.start_search_job

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.start_search_job.async_start_search_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.start_search_job_input.StartSearchJobInput = {
            "search_scope": search_scope
        }
        if tags is not None:
            input_["tags"] = tags
        if name is not None:
            input_["name"] = name
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if item_filters is not None:
            input_["item_filters"] = item_filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_search_job(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.get_search_job_output.GetSearchJobOutput":
        """<p>This operation retrieves metadata of a search job, including its progress.</p>

        Args:
            search_job_identifier: <p>Required unique string that specifies the search job.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.get_search_job_input.GetSearchJobInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.get_search_job_output.GetSearchJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.get_search_job

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.get_search_job.async_get_search_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.get_search_job_input.GetSearchJobInput = {
            "search_job_identifier": search_job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_search_job(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.stop_search_job_output.StopSearchJobOutput":
        """<p>This operations ends a search job.</p> <p>Only a search job with a status of <code>RUNNING</code> can be stopped.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.stop_search_job_input.StopSearchJobInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.stop_search_job_output.StopSearchJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.stop_search_job

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.stop_search_job.async_stop_search_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.stop_search_job_input.StopSearchJobInput = {
            "search_job_identifier": search_job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_search_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        by_status: Optional[
            "capo_backupsearch.types.search_job_state.SearchJobState"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_backupsearch.types.list_search_jobs_output.ListSearchJobsOutput":
        """<p>This operation returns a list of search jobs belonging to an account.</p>

        Args:
            by_status: <p>Include this parameter to filter list by search job status.</p>
            next_token: <p>The next item following a partial list of returned search jobs.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.list_search_jobs_input.ListSearchJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.list_search_jobs_output.ListSearchJobsOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_search_jobs

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.list_search_jobs.async_list_search_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.list_search_jobs_input.ListSearchJobsInput = {}
        if by_status is not None:
            input_["by_status"] = by_status
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

    async def start_search_result_export_job(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        export_specification: "capo_backupsearch.types.export_specification.ExportSpecification",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_backupsearch.types.tag_map.TagMap"] = None,
        role_arn: Optional["capo_backupsearch.types.iam_role_arn.IamRoleArn"] = None,
    ) -> "capo_backupsearch.types.start_search_result_export_job_output.StartSearchResultExportJobOutput":
        """<p>This operations starts a job to export the results of search job to a designated S3 bucket.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            export_specification: <p>This specification contains a required string of the destination bucket; optionally, you can include the destination prefix.</p>
            client_token: <p>Include this parameter to allow multiple identical calls for idempotency.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.</p>
            tags: <p>Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - = . _ : /. </p>
            role_arn: <p>This parameter specifies the role ARN used to start the search results export jobs.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request denied due to exceeding the quota limits permitted.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.start_search_result_export_job_input.StartSearchResultExportJobInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.start_search_result_export_job_output.StartSearchResultExportJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.start_search_result_export_job

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.start_search_result_export_job.async_start_search_result_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.start_search_result_export_job_input.StartSearchResultExportJobInput = {
            "search_job_identifier": search_job_identifier,
            "export_specification": export_specification,
        }
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_search_result_export_job(
        self,
        export_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.get_search_result_export_job_output.GetSearchResultExportJobOutput":
        """<p>This operation retrieves the metadata of an export job.</p> <p>An export job is an operation that transmits the results of a search job to a specified S3 bucket in a .csv file.</p> <p>An export job allows you to retain results of a search beyond the search job's scheduled retention of 7 days.</p>

        Args:
            export_job_identifier: <p>This is the unique string that identifies a specific export job.</p> <p>Required for this operation.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.get_search_result_export_job_input.GetSearchResultExportJobInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.get_search_result_export_job_output.GetSearchResultExportJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.get_search_result_export_job

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.get_search_result_export_job.async_get_search_result_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.get_search_result_export_job_input.GetSearchResultExportJobInput = {
            "export_job_identifier": export_job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_search_result_export_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        status: Optional[
            "capo_backupsearch.types.export_job_status.ExportJobStatus"
        ] = None,
        search_job_identifier: Optional[
            "capo_backupsearch.types.generic_id.GenericId"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_backupsearch.types.list_search_result_export_jobs_output.ListSearchResultExportJobsOutput":
        """<p>This operation exports search results of a search job to a specified destination S3 bucket.</p>

        Args:
            status: <p>The search jobs to be included in the export job can be filtered by including this parameter.</p>
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            next_token: <p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request denied due to exceeding the quota limits permitted.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.list_search_result_export_jobs_input.ListSearchResultExportJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.list_search_result_export_jobs_output.ListSearchResultExportJobsOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_search_result_export_jobs

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.list_search_result_export_jobs.async_list_search_result_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backupsearch.types.list_search_result_export_jobs_input.ListSearchResultExportJobsInput = {}
        if status is not None:
            input_["status"] = status
        if search_job_identifier is not None:
            input_["search_job_identifier"] = search_job_identifier
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
