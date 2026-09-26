"""Generated from Smithy shape ``com.amazonaws.glacier#Glacier``."""

import time
import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_glacier._auth._signers
import capo_glacier._auth._sigv4
from capo_glacier._async import anysleep
from capo_glacier._auth._identity import Credentials
from capo_glacier._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_glacier._auth._zapros_handler import AuthMiddleware
from capo_glacier._body import Body, aclosing_bodies
from capo_glacier._iter import ensure_async_iterator
from capo_glacier._pagination import resolve_path as _resolve_path
from capo_glacier._services._aws_config import aaws_config
from capo_glacier._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)
from capo_glacier.errors import ServiceError, WaiterTimeoutError

if TYPE_CHECKING:
    import capo_glacier.types.abort_multipart_upload_input
    import capo_glacier.types.abort_vault_lock_input
    import capo_glacier.types.add_tags_to_vault_input
    import capo_glacier.types.archive_creation_output
    import capo_glacier.types.complete_multipart_upload_input
    import capo_glacier.types.complete_vault_lock_input
    import capo_glacier.types.create_vault_input
    import capo_glacier.types.create_vault_output
    import capo_glacier.types.data_retrieval_policy
    import capo_glacier.types.delete_archive_input
    import capo_glacier.types.delete_vault_access_policy_input
    import capo_glacier.types.delete_vault_input
    import capo_glacier.types.delete_vault_notifications_input
    import capo_glacier.types.describe_job_input
    import capo_glacier.types.describe_vault_input
    import capo_glacier.types.describe_vault_output
    import capo_glacier.types.get_data_retrieval_policy_input
    import capo_glacier.types.get_data_retrieval_policy_output
    import capo_glacier.types.get_job_output_input
    import capo_glacier.types.get_job_output_output
    import capo_glacier.types.get_vault_access_policy_input
    import capo_glacier.types.get_vault_access_policy_output
    import capo_glacier.types.get_vault_lock_input
    import capo_glacier.types.get_vault_lock_output
    import capo_glacier.types.get_vault_notifications_input
    import capo_glacier.types.get_vault_notifications_output
    import capo_glacier.types.glacier_job_description
    import capo_glacier.types.initiate_job_input
    import capo_glacier.types.initiate_job_output
    import capo_glacier.types.initiate_multipart_upload_input
    import capo_glacier.types.initiate_multipart_upload_output
    import capo_glacier.types.initiate_vault_lock_input
    import capo_glacier.types.initiate_vault_lock_output
    import capo_glacier.types.job_parameters
    import capo_glacier.types.list_jobs_input
    import capo_glacier.types.list_jobs_output
    import capo_glacier.types.list_multipart_uploads_input
    import capo_glacier.types.list_multipart_uploads_output
    import capo_glacier.types.list_parts_input
    import capo_glacier.types.list_parts_output
    import capo_glacier.types.list_provisioned_capacity_input
    import capo_glacier.types.list_provisioned_capacity_output
    import capo_glacier.types.list_tags_for_vault_input
    import capo_glacier.types.list_tags_for_vault_output
    import capo_glacier.types.list_vaults_input
    import capo_glacier.types.list_vaults_output
    import capo_glacier.types.part_list_element
    import capo_glacier.types.purchase_provisioned_capacity_input
    import capo_glacier.types.purchase_provisioned_capacity_output
    import capo_glacier.types.remove_tags_from_vault_input
    import capo_glacier.types.set_data_retrieval_policy_input
    import capo_glacier.types.set_vault_access_policy_input
    import capo_glacier.types.set_vault_notifications_input
    import capo_glacier.types.stream
    import capo_glacier.types.string
    import capo_glacier.types.tag_key_list
    import capo_glacier.types.tag_map
    import capo_glacier.types.upload_archive_input
    import capo_glacier.types.upload_list_element
    import capo_glacier.types.upload_multipart_part_input
    import capo_glacier.types.upload_multipart_part_output
    import capo_glacier.types.vault_access_policy
    import capo_glacier.types.vault_lock_policy
    import capo_glacier.types.vault_notification_config


class AsyncGlacierClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncGlacierClient:
    """A client for the ``Glacier`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AsyncGlacierClientConfig(
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
        self, config_overrides: Optional[AsyncGlacierClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncGlacierClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def abort_multipart_upload(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        upload_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> None:
        r"""<p>This operation aborts a multipart upload identified by the upload ID.</p> <p>After the Abort Multipart Upload request succeeds, you cannot upload any more parts to the multipart upload or complete the multipart upload. Aborting a completed upload fails. However, aborting an already-aborted upload will succeed, for a short time. For more information about uploading a part and completing a multipart upload, see <a>UploadMultipartPart</a> and <a>CompleteMultipartUpload</a>.</p> <p>This operation is idempotent.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p> For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html\">Working with Archives in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-abort-upload.html\">Abort Multipart Upload</a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            upload_id: <p>The upload ID of the multipart upload to delete.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To abort a multipart upload identified by the upload ID
            The example deletes an in-progress multipart upload to a vault named my-vault:

            >>> await client.abort_multipart_upload(account_id='-', vault_name='my-vault', upload_id='19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.abort_multipart_upload_input.AbortMultipartUploadInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.abort_multipart_upload

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.abort_multipart_upload.async_abort_multipart_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.abort_multipart_upload_input.AbortMultipartUploadInput = {
            "account_id": account_id,
            "vault_name": vault_name,
            "upload_id": upload_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def abort_vault_lock(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> None:
        r"""<p>This operation aborts the vault locking process if the vault lock is not in the <code>Locked</code> state. If the vault lock is in the <code>Locked</code> state when this operation is requested, the operation returns an <code>AccessDeniedException</code> error. Aborting the vault locking process removes the vault lock policy from the specified vault. </p> <p>A vault lock is put into the <code>InProgress</code> state by calling <a>InitiateVaultLock</a>. A vault lock is put into the <code>Locked</code> state by calling <a>CompleteVaultLock</a>. You can get the state of a vault lock by calling <a>GetVaultLock</a>. For more information about the vault locking process, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html\">Amazon Glacier Vault Lock</a>. For more information about vault lock policies, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html\">Amazon Glacier Access Control with Vault Lock Policies</a>. </p> <p>This operation is idempotent. You can successfully invoke this operation multiple times, if the vault lock is in the <code>InProgress</code> state or if there is no policy associated with the vault.</p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To abort a vault lock
            The example aborts the vault locking process if the vault lock is not in the Locked state for the vault named examplevault.

            >>> await client.abort_vault_lock(account_id='-', vault_name='examplevault')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.abort_vault_lock_input.AbortVaultLockInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.abort_vault_lock

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.abort_vault_lock.async_abort_vault_lock(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.abort_vault_lock_input.AbortVaultLockInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_tags_to_vault(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        tags: Optional["capo_glacier.types.tag_map.TagMap"] = None,
    ) -> None:
        r"""<p>This operation adds the specified tags to a vault. Each tag is composed of a key and a value. Each vault can have up to 10 tags. If your request would cause the tag limit for the vault to be exceeded, the operation throws the <code>LimitExceededException</code> error. If a tag already exists on the vault under a specified key, the existing key value will be overwritten. For more information about tags, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/tagging.html\">Tagging Amazon Glacier Resources</a>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            tags: <p>The tags to add to the vault. Each tag is composed of a key and a value. The value can be an empty string.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.limit_exceeded_exception.LimitExceededException: <p>Returned if the request results in a vault or account limit being exceeded.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add tags to a vault
            The example adds two tags to a my-vault.

            >>> await client.add_tags_to_vault(account_id='-', vault_name='my-vault', tags={'examplekey1': 'examplevalue1', 'examplekey2': 'examplevalue2'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.add_tags_to_vault_input.AddTagsToVaultInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.add_tags_to_vault

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.add_tags_to_vault.async_add_tags_to_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.add_tags_to_vault_input.AddTagsToVaultInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def complete_multipart_upload(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        upload_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        archive_size: Optional["capo_glacier.types.string.string"] = None,
        checksum: Optional["capo_glacier.types.string.string"] = None,
    ) -> "capo_glacier.types.archive_creation_output.ArchiveCreationOutput":
        r"""<p>You call this operation to inform Amazon Glacier (Glacier) that all the archive parts have been uploaded and that Glacier can now assemble the archive from the uploaded parts. After assembling and saving the archive to the vault, Glacier returns the URI path of the newly created archive resource. Using the URI path, you can then access the archive. After you upload an archive, you should save the archive ID returned to retrieve the archive at a later point. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see <a>InitiateJob</a>.</p> <p>In the request, you must include the computed SHA256 tree hash of the entire archive you have uploaded. For information about computing a SHA256 tree hash, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html\">Computing Checksums</a>. On the server side, Glacier also constructs the SHA256 tree hash of the assembled archive. If the values match, Glacier saves the archive to the vault; otherwise, it returns an error, and the operation fails. The <a>ListParts</a> operation returns a list of parts uploaded for a specific multipart upload. It includes checksum information for each uploaded part that can be used to debug a bad checksum issue.</p> <p>Additionally, Glacier also checks for any missing content ranges when assembling the archive, if missing content ranges are found, Glacier returns an error and the operation fails.</p> <p>Complete Multipart Upload is an idempotent operation. After your first successful complete multipart upload, if you call the operation again within a short period, the operation will succeed and return the same archive ID. This is useful in the event you experience a network issue that causes an aborted connection or receive a 500 server error, in which case you can repeat your Complete Multipart Upload request and get the same archive ID without creating duplicate archives. Note, however, that after the multipart upload completes, you cannot call the List Parts operation and the multipart upload will not appear in List Multipart Uploads response, even if idempotent complete is possible.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p> For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html\">Uploading Large Archives in Parts (Multipart Upload)</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-complete-upload.html\">Complete Multipart Upload</a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            upload_id: <p>The upload ID of the multipart upload.</p>
            archive_size: <p>The total size, in bytes, of the entire archive. This value should be the sum of all the sizes of the individual parts that you uploaded.</p>
            checksum: <p>The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree hash of the individual parts. If the value you specify in the request does not match the SHA256 tree hash of the final assembled archive as computed by Amazon Glacier (Glacier), Glacier returns an error and the request fails.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To complete a multipart upload
            The example completes a multipart upload for a 3 MiB archive.

            >>> await client.complete_multipart_upload(checksum='9628195fcdbcbbe76cdde456d4646fa7de5f219fb39823836d81f0cc0e18aa67', vault_name='my-vault', upload_id='19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ', archive_size='3145728', account_id='-')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.complete_multipart_upload_input.CompleteMultipartUploadInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.archive_creation_output.ArchiveCreationOutput"
        ]:
            import capo_glacier._operations.glacier.complete_multipart_upload

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.complete_multipart_upload.async_complete_multipart_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.complete_multipart_upload_input.CompleteMultipartUploadInput = {
            "account_id": account_id,
            "vault_name": vault_name,
            "upload_id": upload_id,
        }
        if archive_size is not None:
            input_["archive_size"] = archive_size
        if checksum is not None:
            input_["checksum"] = checksum

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def complete_vault_lock(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        lock_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> None:
        r"""<p>This operation completes the vault locking process by transitioning the vault lock from the <code>InProgress</code> state to the <code>Locked</code> state, which causes the vault lock policy to become unchangeable. A vault lock is put into the <code>InProgress</code> state by calling <a>InitiateVaultLock</a>. You can obtain the state of the vault lock by calling <a>GetVaultLock</a>. For more information about the vault locking process, <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html\">Amazon Glacier Vault Lock</a>. </p> <p>This operation is idempotent. This request is always successful if the vault lock is in the <code>Locked</code> state and the provided lock ID matches the lock ID originally used to lock the vault.</p> <p>If an invalid lock ID is passed in the request when the vault lock is in the <code>Locked</code> state, the operation returns an <code>AccessDeniedException</code> error. If an invalid lock ID is passed in the request when the vault lock is in the <code>InProgress</code> state, the operation throws an <code>InvalidParameter</code> error.</p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            lock_id: <p>The <code>lockId</code> value is the lock ID obtained from a <a>InitiateVaultLock</a> request.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To complete a vault lock
            The example completes the vault locking process by transitioning the vault lock from the InProgress state to the Locked state.

            >>> await client.complete_vault_lock(account_id='-', vault_name='example-vault', lock_id='AE863rKkWZU53SLW5be4DUcW')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.complete_vault_lock_input.CompleteVaultLockInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.complete_vault_lock

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.complete_vault_lock.async_complete_vault_lock(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.complete_vault_lock_input.CompleteVaultLockInput = {
            "account_id": account_id,
            "vault_name": vault_name,
            "lock_id": lock_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_vault(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> "capo_glacier.types.create_vault_output.CreateVaultOutput":
        r"""<p>This operation creates a new vault with the specified name. The name of the vault must be unique within a region for an AWS account. You can create up to 1,000 vaults per account. If you need to create more vaults, contact Amazon Glacier.</p> <p>You must use the following guidelines when naming a vault.</p> <ul> <li> <p>Names can be between 1 and 255 characters long.</p> </li> <li> <p>Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period).</p> </li> </ul> <p>This operation is idempotent.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p> For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults.html\">Creating a Vault in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html\">Create Vault </a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.limit_exceeded_exception.LimitExceededException: <p>Returned if the request results in a vault or account limit being exceeded.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a new vault
            The following example creates a new vault named my-vault.

            >>> await client.create_vault(vault_name='my-vault', account_id='-')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.create_vault_input.CreateVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.create_vault_output.CreateVaultOutput"
        ]:
            import capo_glacier._operations.glacier.create_vault

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.create_vault.async_create_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.create_vault_input.CreateVaultInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_archive(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        archive_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> None:
        r"""<p>This operation deletes an archive from a vault. Subsequent requests to initiate a retrieval of this archive will fail. Archive retrievals that are in progress for this archive ID may or may not succeed according to the following scenarios:</p> <ul> <li> <p>If the archive retrieval job is actively preparing the data for download when Amazon Glacier receives the delete archive request, the archival retrieval operation might fail.</p> </li> <li> <p>If the archive retrieval job has successfully prepared the archive for download when Amazon Glacier receives the delete archive request, you will be able to download the output.</p> </li> </ul> <p>This operation is idempotent. Attempting to delete an already-deleted archive does not result in an error.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p> For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive.html\">Deleting an Archive in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html\">Delete Archive</a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            archive_id: <p>The ID of the archive to delete.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete an archive
            The example deletes the archive specified by the archive ID.

            >>> await client.delete_archive(account_id='-', vault_name='examplevault', archive_id='NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.delete_archive_input.DeleteArchiveInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.delete_archive

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.delete_archive.async_delete_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.delete_archive_input.DeleteArchiveInput = {
            "account_id": account_id,
            "vault_name": vault_name,
            "archive_id": archive_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_vault(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> None:
        r"""<p>This operation deletes a vault. Amazon Glacier will delete a vault only if there are no archives in the vault as of the last inventory and there have been no writes to the vault since the last inventory. If either of these conditions is not satisfied, the vault deletion fails (that is, the vault is not removed) and Amazon Glacier returns an error. You can use <a>DescribeVault</a> to return the number of archives in a vault, and you can use <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html\">Initiate a Job (POST jobs)</a> to initiate a new inventory retrieval for a vault. The inventory contains the archive IDs you use to delete archives using <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html\">Delete Archive (DELETE archive)</a>.</p> <p>This operation is idempotent.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p> For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults.html\">Deleting a Vault in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-delete.html\">Delete Vault </a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a vault
            The example deletes a vault named my-vault:

            >>> await client.delete_vault(vault_name='my-vault', account_id='-')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.delete_vault_input.DeleteVaultInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.delete_vault

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.delete_vault.async_delete_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.delete_vault_input.DeleteVaultInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_vault_access_policy(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> None:
        r"""<p>This operation deletes the access policy associated with the specified vault. The operation is eventually consistent; that is, it might take some time for Amazon Glacier to completely remove the access policy, and you might still see the effect of the policy for a short time after you send the delete request.</p> <p>This operation is idempotent. You can invoke delete multiple times, even if there is no policy associated with the vault. For more information about vault access policies, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html\">Amazon Glacier Access Control with Vault Access Policies</a>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete the vault access policy
            The example deletes the access policy associated with the vault named examplevault.

            >>> await client.delete_vault_access_policy(account_id='-', vault_name='examplevault')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.delete_vault_access_policy_input.DeleteVaultAccessPolicyInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.delete_vault_access_policy

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.delete_vault_access_policy.async_delete_vault_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.delete_vault_access_policy_input.DeleteVaultAccessPolicyInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_vault_notifications(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> None:
        r"""<p>This operation deletes the notification configuration set for a vault. The operation is eventually consistent; that is, it might take some time for Amazon Glacier to completely disable the notifications and you might still receive some notifications for a short time after you send the delete request.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p> For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html\">Configuring Vault Notifications in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-delete.html\">Delete Vault Notification Configuration </a> in the Amazon Glacier Developer Guide. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete the notification configuration set for a vault
            The example deletes the notification configuration set for the vault named examplevault.

            >>> await client.delete_vault_notifications(account_id='-', vault_name='examplevault')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.delete_vault_notifications_input.DeleteVaultNotificationsInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.delete_vault_notifications

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.delete_vault_notifications.async_delete_vault_notifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.delete_vault_notifications_input.DeleteVaultNotificationsInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_job(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        job_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> "capo_glacier.types.glacier_job_description.GlacierJobDescription":
        r"""<p>This operation returns information about a job you previously initiated, including the job initiation date, the user who initiated the job, the job status code/message and the Amazon SNS topic to notify after Amazon Glacier (Glacier) completes the job. For more information about initiating a job, see <a>InitiateJob</a>. </p> <note> <p>This operation enables you to check the status of your job. However, it is strongly recommended that you set up an Amazon SNS topic and specify it in your initiate job request so that Glacier can notify the topic after it completes the job.</p> </note> <p>A job ID will not expire for at least 24 hours after Glacier completes the job.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p> For more information about using this operation, see the documentation for the underlying REST API <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-describe-job-get.html\">Describe Job</a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>
            job_id: <p>The ID of the job to describe.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get information about a previously initiated job
            The example returns information about the previously initiated job specified by the job ID.

            >>> await client.describe_job(account_id='-', vault_name='my-vault', job_id='zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4Cn')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.describe_job_input.DescribeJobInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.glacier_job_description.GlacierJobDescription"
        ]:
            import capo_glacier._operations.glacier.describe_job

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.describe_job.async_describe_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.describe_job_input.DescribeJobInput = {
            "account_id": account_id,
            "vault_name": vault_name,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_vault(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> "capo_glacier.types.describe_vault_output.DescribeVaultOutput":
        r"""<p>This operation returns information about a vault, including the vault's Amazon Resource Name (ARN), the date the vault was created, the number of archives it contains, and the total size of all the archives in the vault. The number of archives and their total size are as of the last inventory generation. This means that if you add or remove an archive from a vault, and then immediately use Describe Vault, the change in contents will not be immediately reflected. If you want to retrieve the latest inventory of the vault, use <a>InitiateJob</a>. Amazon Glacier generates vault inventories approximately daily. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html\">Downloading a Vault Inventory in Amazon Glacier</a>. </p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p>For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info.html\">Retrieving Vault Metadata in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-get.html\">Describe Vault </a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve information about a vault
            The example retrieves data about a vault named my-vault.

            >>> await client.describe_vault(vault_name='my-vault', account_id='-')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.describe_vault_input.DescribeVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.describe_vault_output.DescribeVaultOutput"
        ]:
            import capo_glacier._operations.glacier.describe_vault

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.describe_vault.async_describe_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.describe_vault_input.DescribeVaultInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def wait_until_vault_exists(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        max_wait_time: float,
        min_delay: float = 3,
        max_delay: float = 120,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> "capo_glacier.types.describe_vault_output.DescribeVaultOutput":
        """Wait for vault_exists.

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_glacier.types.describe_vault_output.DescribeVaultOutput | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.describe_vault(  # noqa: F841
                    account_id, vault_name, config_overrides=config_overrides
                )
            except ServiceError as e:
                op_error = e
            if op_output is not None:
                return op_output
            elif op_error is not None and op_error.code == "ResourceNotFoundException":
                pass

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("vault_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def wait_until_vault_not_exists(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        max_wait_time: float,
        min_delay: float = 3,
        max_delay: float = 120,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> ServiceError:
        """Wait for vault_not_exists.

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_glacier.types.describe_vault_output.DescribeVaultOutput | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.describe_vault(  # noqa: F841
                    account_id, vault_name, config_overrides=config_overrides
                )
            except ServiceError as e:
                op_error = e
            if op_output is not None:
                pass
            elif op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("vault_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def get_data_retrieval_policy(
        self,
        account_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> "capo_glacier.types.get_data_retrieval_policy_output.GetDataRetrievalPolicyOutput":
        r"""<p>This operation returns the current data retrieval policy for the account and region specified in the GET request. For more information about data retrieval policies, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/data-retrieval-policy.html\">Amazon Glacier Data Retrieval Policies</a>.</p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID. </p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the current data retrieval policy for an account
            The example returns the current data retrieval policy for the account.

            >>> await client.get_data_retrieval_policy(account_id='-')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.get_data_retrieval_policy_input.GetDataRetrievalPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.get_data_retrieval_policy_output.GetDataRetrievalPolicyOutput"
        ]:
            import capo_glacier._operations.glacier.get_data_retrieval_policy

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.get_data_retrieval_policy.async_get_data_retrieval_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.get_data_retrieval_policy_input.GetDataRetrievalPolicyInput = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def get_job_output(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        job_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        range: Optional["capo_glacier.types.string.string"] = None,
    ) -> "AsyncGenerator[capo_glacier.types.get_job_output_output.GetJobOutputOutput]":
        r"""<p>This operation downloads the output of the job you initiated using <a>InitiateJob</a>. Depending on the job type you specified when you initiated the job, the output will be either the content of an archive or a vault inventory.</p> <p>You can download all the job output or download a portion of the output by specifying a byte range. In the case of an archive retrieval job, depending on the byte range you specify, Amazon Glacier (Glacier) returns the checksum for the portion of the data. You can compute the checksum on the client and verify that the values match to ensure the portion you downloaded is the correct data.</p> <p>A job ID will not expire for at least 24 hours after Glacier completes the job. That a byte range. For both archive and inventory retrieval jobs, you should verify the downloaded size against the size returned in the headers from the <b>Get Job Output</b> response.</p> <p>For archive retrieval jobs, you should also verify that the size is what you expected. If you download a portion of the output, the expected size is based on the range of bytes you specified. For example, if you specify a range of <code>bytes=0-1048575</code>, you should verify your download size is 1,048,576 bytes. If you download an entire archive, the expected size is the size of the archive when you uploaded it to Amazon Glacier The expected size is also returned in the headers from the <b>Get Job Output</b> response.</p> <p>In the case of an archive retrieval job, depending on the byte range you specify, Glacier returns the checksum for the portion of the data. To ensure the portion you downloaded is the correct data, compute the checksum on the client, verify that the values match, and verify that the size is what you expected.</p> <p>A job ID does not expire for at least 24 hours after Glacier completes the job. That is, you can download the job output within the 24 hours period after Amazon Glacier completes the job.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p>For conceptual information and the underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html\">Downloading a Vault Inventory</a>, <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive.html\">Downloading an Archive</a>, and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-job-output-get.html\">Get Job Output </a> </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            job_id: <p>The job ID whose data is downloaded.</p>
            range: <p>The range of bytes to retrieve from the output. For example, if you want to download the first 1,048,576 bytes, specify the range as <code>bytes=0-1048575</code>. By default, this operation downloads the entire output.</p> <p>If the job output is large, then you can use a range to retrieve a portion of the output. This allows you to download the entire output in smaller chunks of bytes. For example, suppose you have 1 GB of job output you want to download and you decide to download 128 MB chunks of data at a time, which is a total of eight Get Job Output requests. You use the following process to download the job output:</p> <ol> <li> <p>Download a 128 MB chunk of output by specifying the appropriate byte range. Verify that all 128 MB of data was received.</p> </li> <li> <p>Along with the data, the response includes a SHA256 tree hash of the payload. You compute the checksum of the payload on the client and compare it with the checksum you received in the response to ensure you received all the expected data.</p> </li> <li> <p>Repeat steps 1 and 2 for all the eight 128 MB chunks of output data, each time specifying the appropriate byte range.</p> </li> <li> <p>After downloading all the parts of the job output, you have a list of eight checksum values. Compute the tree hash of these values to find the checksum of the entire output. Using the <a>DescribeJob</a> API, obtain job information of the job that provided you the output. The response includes the checksum of the entire archive stored in Amazon Glacier. You compare this value with the checksum you computed to ensure you have downloaded the entire archive content with no errors.</p> <p></p> </li> </ol>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the output of a previously initiated job
            The example downloads the output of a previously initiated inventory retrieval job that is identified by the job ID.

            >>> await client.get_job_output(account_id='-', vault_name='my-vaul', job_id='zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW', range='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.get_job_output_input.GetJobOutputInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.get_job_output_output.GetJobOutputOutput"
        ]:
            import capo_glacier._operations.glacier.get_job_output

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.get_job_output.async_get_job_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.get_job_output_input.GetJobOutputInput = {
            "account_id": account_id,
            "vault_name": vault_name,
            "job_id": job_id,
        }
        if range is not None:
            input_["range"] = range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def get_vault_access_policy(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> "capo_glacier.types.get_vault_access_policy_output.GetVaultAccessPolicyOutput":
        r"""<p>This operation retrieves the <code>access-policy</code> subresource set on the vault; for more information on setting this subresource, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-SetVaultAccessPolicy.html\">Set Vault Access Policy (PUT access-policy)</a>. If there is no access policy set on the vault, the operation returns a <code>404 Not found</code> error. For more information about vault access policies, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html\">Amazon Glacier Access Control with Vault Access Policies</a>.</p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To  get the access-policy set on the vault
            The example retrieves the access-policy set on the vault named example-vault.

            >>> await client.get_vault_access_policy(account_id='-', vault_name='example-vault')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.get_vault_access_policy_input.GetVaultAccessPolicyInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.get_vault_access_policy_output.GetVaultAccessPolicyOutput"
        ]:
            import capo_glacier._operations.glacier.get_vault_access_policy

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.get_vault_access_policy.async_get_vault_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.get_vault_access_policy_input.GetVaultAccessPolicyInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_vault_lock(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> "capo_glacier.types.get_vault_lock_output.GetVaultLockOutput":
        r"""<p>This operation retrieves the following attributes from the <code>lock-policy</code> subresource set on the specified vault: </p> <ul> <li> <p>The vault lock policy set on the vault.</p> </li> <li> <p>The state of the vault lock, which is either <code>InProgess</code> or <code>Locked</code>.</p> </li> <li> <p>When the lock ID expires. The lock ID is used to complete the vault locking process.</p> </li> <li> <p>When the vault lock was initiated and put into the <code>InProgress</code> state.</p> </li> </ul> <p>A vault lock is put into the <code>InProgress</code> state by calling <a>InitiateVaultLock</a>. A vault lock is put into the <code>Locked</code> state by calling <a>CompleteVaultLock</a>. You can abort the vault locking process by calling <a>AbortVaultLock</a>. For more information about the vault locking process, <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html\">Amazon Glacier Vault Lock</a>. </p> <p>If there is no vault lock policy set on the vault, the operation returns a <code>404 Not found</code> error. For more information about vault lock policies, <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html\">Amazon Glacier Access Control with Vault Lock Policies</a>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To retrieve vault lock-policy related attributes that are set on a vault
            The example retrieves the attributes from the lock-policy subresource set on the vault named examplevault.

            >>> await client.get_vault_lock(account_id='-', vault_name='examplevault')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.get_vault_lock_input.GetVaultLockInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.get_vault_lock_output.GetVaultLockOutput"
        ]:
            import capo_glacier._operations.glacier.get_vault_lock

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.get_vault_lock.async_get_vault_lock(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.get_vault_lock_input.GetVaultLockInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_vault_notifications(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> (
        "capo_glacier.types.get_vault_notifications_output.GetVaultNotificationsOutput"
    ):
        r"""<p>This operation retrieves the <code>notification-configuration</code> subresource of the specified vault.</p> <p>For information about setting a notification configuration on a vault, see <a>SetVaultNotifications</a>. If a notification configuration for a vault is not set, the operation returns a <code>404 Not Found</code> error. For more information about vault notifications, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html\">Configuring Vault Notifications in Amazon Glacier</a>. </p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p>For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html\">Configuring Vault Notifications in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-get.html\">Get Vault Notification Configuration </a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get the notification-configuration for the specified vault
            The example retrieves the notification-configuration for the vault named my-vault.

            >>> await client.get_vault_notifications(account_id='-', vault_name='my-vault')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.get_vault_notifications_input.GetVaultNotificationsInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.get_vault_notifications_output.GetVaultNotificationsOutput"
        ]:
            import capo_glacier._operations.glacier.get_vault_notifications

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.get_vault_notifications.async_get_vault_notifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.get_vault_notifications_input.GetVaultNotificationsInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def initiate_job(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        job_parameters: Optional[
            "capo_glacier.types.job_parameters.JobParameters"
        ] = None,
    ) -> "capo_glacier.types.initiate_job_output.InitiateJobOutput":
        r"""<p>This operation initiates a job of the specified type, which can be a select, an archival retrieval, or a vault retrieval. For more information about using this operation, see the documentation for the underlying REST API <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html\">Initiate a Job</a>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            job_parameters: <p>Provides options for specifying job information.</p>

        Raises:
            capo_glacier.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>Returned if there is insufficient capacity to process this expedited request. This error only applies to expedited retrievals and not to standard or bulk retrievals.</p>
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.policy_enforced_exception.PolicyEnforcedException: <p>Returned if a retrieval job would exceed the current data policy's retrieval rate limit. For more information about data retrieval policies,</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To initiate an inventory-retrieval job
            The example initiates an inventory-retrieval job for the vault named examplevault.

            >>> await client.initiate_job(account_id='-', vault_name='examplevault', job_parameters={'Type': 'inventory-retrieval', 'Description': 'My inventory job', 'Format': 'CSV', 'SNSTopic': 'arn:aws:sns:us-west-2:111111111111:Glacier-InventoryRetrieval-topic-Example'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.initiate_job_input.InitiateJobInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.initiate_job_output.InitiateJobOutput"
        ]:
            import capo_glacier._operations.glacier.initiate_job

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.initiate_job.async_initiate_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.initiate_job_input.InitiateJobInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }
        if job_parameters is not None:
            input_["job_parameters"] = job_parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def initiate_multipart_upload(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        archive_description: Optional["capo_glacier.types.string.string"] = None,
        part_size: Optional["capo_glacier.types.string.string"] = None,
    ) -> "capo_glacier.types.initiate_multipart_upload_output.InitiateMultipartUploadOutput":
        r"""<p>This operation initiates a multipart upload. Amazon Glacier creates a multipart upload resource and returns its ID in the response. The multipart upload ID is used in subsequent requests to upload parts of an archive (see <a>UploadMultipartPart</a>).</p> <p>When you initiate a multipart upload, you specify the part size in number of bytes. The part size must be a megabyte (1024 KB) multiplied by a power of 2-for example, 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB.</p> <p>Every part you upload to this resource (see <a>UploadMultipartPart</a>), except the last one, must have the same size. The last one can be the same size or smaller. For example, suppose you want to upload a 16.2 MB file. If you initiate the multipart upload with a part size of 4 MB, you will upload four parts of 4 MB each and one part of 0.2 MB. </p> <note> <p>You don't need to know the size of the archive when you start a multipart upload because Amazon Glacier does not require you to specify the overall archive size.</p> </note> <p>After you complete the multipart upload, Amazon Glacier (Glacier) removes the multipart upload resource referenced by the ID. Glacier also removes the multipart upload resource if you cancel the multipart upload or it may be removed if there is no activity for a period of 24 hours.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p>For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html\">Uploading Large Archives in Parts (Multipart Upload)</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-initiate-upload.html\">Initiate Multipart Upload</a> in the <i>Amazon Glacier Developer Guide</i>.</p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>
            archive_description: <p>The archive description that you are uploading in parts.</p> <p>The part size must be a megabyte (1024 KB) multiplied by a power of 2, for example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB (4096 MB).</p>
            part_size: <p>The size of each part except the last, in bytes. The last part can be smaller than this part size.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To initiate a multipart upload
            The example initiates a multipart upload to a vault named my-vault with a part size of 1 MiB (1024 x 1024 bytes) per file.

            >>> await client.initiate_multipart_upload(account_id='-', part_size='1048576', vault_name='my-vault')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.initiate_multipart_upload_input.InitiateMultipartUploadInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.initiate_multipart_upload_output.InitiateMultipartUploadOutput"
        ]:
            import capo_glacier._operations.glacier.initiate_multipart_upload

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.initiate_multipart_upload.async_initiate_multipart_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.initiate_multipart_upload_input.InitiateMultipartUploadInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }
        if archive_description is not None:
            input_["archive_description"] = archive_description
        if part_size is not None:
            input_["part_size"] = part_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def initiate_vault_lock(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        policy: Optional["capo_glacier.types.vault_lock_policy.VaultLockPolicy"] = None,
    ) -> "capo_glacier.types.initiate_vault_lock_output.InitiateVaultLockOutput":
        r"""<p>This operation initiates the vault locking process by doing the following:</p> <ul> <li> <p>Installing a vault lock policy on the specified vault.</p> </li> <li> <p>Setting the lock state of vault lock to <code>InProgress</code>.</p> </li> <li> <p>Returning a lock ID, which is used to complete the vault locking process.</p> </li> </ul> <p>You can set one vault lock policy for each vault and this policy can be up to 20 KB in size. For more information about vault lock policies, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html\">Amazon Glacier Access Control with Vault Lock Policies</a>. </p> <p>You must complete the vault locking process within 24 hours after the vault lock enters the <code>InProgress</code> state. After the 24 hour window ends, the lock ID expires, the vault automatically exits the <code>InProgress</code> state, and the vault lock policy is removed from the vault. You call <a>CompleteVaultLock</a> to complete the vault locking process by setting the state of the vault lock to <code>Locked</code>. </p> <p>After a vault lock is in the <code>Locked</code> state, you cannot initiate a new vault lock for the vault.</p> <p>You can abort the vault locking process by calling <a>AbortVaultLock</a>. You can get the state of the vault lock by calling <a>GetVaultLock</a>. For more information about the vault locking process, <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html\">Amazon Glacier Vault Lock</a>.</p> <p>If this operation is called when the vault lock is in the <code>InProgress</code> state, the operation returns an <code>AccessDeniedException</code> error. When the vault lock is in the <code>InProgress</code> state you must call <a>AbortVaultLock</a> before you can initiate a new vault lock policy. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            policy: <p>The vault lock policy as a JSON string, which uses \"\\" as an escape character.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To initiate the vault locking process
            The example initiates the vault locking process for the vault named my-vault.

            >>> await client.initiate_vault_lock(account_id='-', vault_name='my-vault', policy={'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-vault-lock","Effect":"Deny","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault","Condition":{"NumericLessThanEquals":{"glacier:ArchiveAgeinDays":"365"}}}]}'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.initiate_vault_lock_input.InitiateVaultLockInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.initiate_vault_lock_output.InitiateVaultLockOutput"
        ]:
            import capo_glacier._operations.glacier.initiate_vault_lock

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.initiate_vault_lock.async_initiate_vault_lock(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.initiate_vault_lock_input.InitiateVaultLockInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }
        if policy is not None:
            input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_jobs(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        limit: Optional[int] = None,
        marker: Optional["capo_glacier.types.string.string"] = None,
        statuscode: Optional["capo_glacier.types.string.string"] = None,
        completed: Optional["capo_glacier.types.string.string"] = None,
    ) -> "capo_glacier.types.list_jobs_output.ListJobsOutput":
        r"""<p>This operation lists jobs for a vault, including jobs that are in-progress and jobs that have recently finished. The List Job operation returns a list of these jobs sorted by job initiation time.</p> <note> <p>Amazon Glacier retains recently completed jobs for a period before deleting them; however, it eventually removes completed jobs. The output of completed jobs can be retrieved. Retaining completed jobs for a period of time after they have completed enables you to get a job output in the event you miss the job completion notification or your first attempt to download it fails. For example, suppose you start an archive retrieval job to download an archive. After the job completes, you start to download the archive but encounter a network error. In this scenario, you can retry and download the archive while the job exists.</p> </note> <p>The List Jobs operation supports pagination. You should always check the response <code>Marker</code> field. If there are no more jobs to list, the <code>Marker</code> field is set to <code>null</code>. If there are more jobs to list, the <code>Marker</code> field is set to a non-null value, which you can use to continue the pagination of the list. To return a list of jobs that begins at a specific job, set the marker request parameter to the <code>Marker</code> value for that job that you obtained from a previous List Jobs request.</p> <p>You can set a maximum limit for the number of jobs returned in the response by specifying the <code>limit</code> parameter in the request. The default limit is 50. The number of jobs returned might be fewer than the limit, but the number of returned jobs never exceeds the limit.</p> <p>Additionally, you can filter the jobs list returned by specifying the optional <code>statuscode</code> parameter or <code>completed</code> parameter, or both. Using the <code>statuscode</code> parameter, you can specify to return only jobs that match either the <code>InProgress</code>, <code>Succeeded</code>, or <code>Failed</code> status. Using the <code>completed</code> parameter, you can specify to return only jobs that were completed (<code>true</code>) or jobs that were not completed (<code>false</code>).</p> <p>For more information about using this operation, see the documentation for the underlying REST API <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-jobs-get.html\">List Jobs</a>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>
            limit: <p>The maximum number of jobs to be returned. The default limit is 50. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.</p>
            marker: <p>An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.</p>
            statuscode: <p>The type of job status to return. You can specify the following values: <code>InProgress</code>, <code>Succeeded</code>, or <code>Failed</code>.</p>
            completed: <p>The state of the jobs to return. You can specify <code>true</code> or <code>false</code>.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list jobs for a vault
            The example lists jobs for the vault named my-vault.

            >>> await client.list_jobs(account_id='-', vault_name='my-vault')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.list_jobs_input.ListJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.list_jobs_output.ListJobsOutput"
        ]:
            import capo_glacier._operations.glacier.list_jobs

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.list_jobs.async_list_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.list_jobs_input.ListJobsInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker
        if statuscode is not None:
            input_["statuscode"] = statuscode
        if completed is not None:
            input_["completed"] = completed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_jobs(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        limit: Optional[int] = None,
        marker: Optional["capo_glacier.types.string.string"] = None,
        statuscode: Optional["capo_glacier.types.string.string"] = None,
        completed: Optional["capo_glacier.types.string.string"] = None,
    ) -> "AsyncIterator[capo_glacier.types.glacier_job_description.GlacierJobDescription]":
        _token = marker
        while True:
            _response = await self.list_jobs(
                account_id,
                vault_name,
                config_overrides=config_overrides,
                limit=limit,
                marker=_token,
                statuscode=statuscode,
                completed=completed,
            )
            _page = _resolve_path(_response, ("job_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def list_multipart_uploads(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        limit: Optional[int] = None,
        marker: Optional["capo_glacier.types.string.string"] = None,
    ) -> "capo_glacier.types.list_multipart_uploads_output.ListMultipartUploadsOutput":
        r"""<p>This operation lists in-progress multipart uploads for the specified vault. An in-progress multipart upload is a multipart upload that has been initiated by an <a>InitiateMultipartUpload</a> request, but has not yet been completed or aborted. The list returned in the List Multipart Upload response has no guaranteed order. </p> <p>The List Multipart Uploads operation supports pagination. By default, this operation returns up to 50 multipart uploads in the response. You should always check the response for a <code>marker</code> at which to continue the list; if there are no more items the <code>marker</code> is <code>null</code>. To return a list of multipart uploads that begins at a specific upload, set the <code>marker</code> request parameter to the value you obtained from a previous List Multipart Upload request. You can also limit the number of uploads returned in the response by specifying the <code>limit</code> parameter in the request.</p> <p>Note the difference between this operation and listing parts (<a>ListParts</a>). The List Multipart Uploads operation lists all multipart uploads for a vault and does not require a multipart upload ID. The List Parts operation requires a multipart upload ID since parts are associated with a single upload.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p>For conceptual information and the underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html\">Working with Archives in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-uploads.html\">List Multipart Uploads </a> in the <i>Amazon Glacier Developer Guide</i>.</p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>
            limit: <p>Specifies the maximum number of uploads returned in the response body. If this value is not specified, the List Uploads operation returns up to 50 uploads.</p>
            marker: <p>An opaque string used for pagination. This value specifies the upload at which the listing of uploads should begin. Get the marker value from a previous List Uploads response. You need only include the marker if you are continuing the pagination of results started in a previous List Uploads request.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list all the in-progress multipart uploads for a vault
            The example lists all the in-progress multipart uploads for the vault named examplevault.

            >>> await client.list_multipart_uploads(account_id='-', vault_name='examplevault')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.list_multipart_uploads_input.ListMultipartUploadsInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.list_multipart_uploads_output.ListMultipartUploadsOutput"
        ]:
            import capo_glacier._operations.glacier.list_multipart_uploads

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.list_multipart_uploads.async_list_multipart_uploads(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.list_multipart_uploads_input.ListMultipartUploadsInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }
        if limit is not None:
            input_["limit"] = limit
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_multipart_uploads(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        limit: Optional[int] = None,
        marker: Optional["capo_glacier.types.string.string"] = None,
    ) -> "AsyncIterator[capo_glacier.types.upload_list_element.UploadListElement]":
        _token = marker
        while True:
            _response = await self.list_multipart_uploads(
                account_id,
                vault_name,
                config_overrides=config_overrides,
                limit=limit,
                marker=_token,
            )
            _page = _resolve_path(_response, ("uploads_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def list_parts(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        upload_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        marker: Optional["capo_glacier.types.string.string"] = None,
        limit: Optional[int] = None,
    ) -> "capo_glacier.types.list_parts_output.ListPartsOutput":
        r"""<p>This operation lists the parts of an archive that have been uploaded in a specific multipart upload. You can make this request at any time during an in-progress multipart upload before you complete the upload (see <a>CompleteMultipartUpload</a>. List Parts returns an error for completed uploads. The list returned in the List Parts response is sorted by part range. </p> <p>The List Parts operation supports pagination. By default, this operation returns up to 50 uploaded parts in the response. You should always check the response for a <code>marker</code> at which to continue the list; if there are no more items the <code>marker</code> is <code>null</code>. To return a list of parts that begins at a specific part, set the <code>marker</code> request parameter to the value you obtained from a previous List Parts request. You can also limit the number of parts returned in the response by specifying the <code>limit</code> parameter in the request. </p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p>For conceptual information and the underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html\">Working with Archives in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-parts.html\">List Parts</a> in the <i>Amazon Glacier Developer Guide</i>.</p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>
            upload_id: <p>The upload ID of the multipart upload.</p>
            marker: <p>An opaque string used for pagination. This value specifies the part at which the listing of parts should begin. Get the marker value from the response of a previous List Parts response. You need only include the marker if you are continuing the pagination of results started in a previous List Parts request.</p>
            limit: <p>The maximum number of parts to be returned. The default limit is 50. The number of parts returned might be fewer than the specified limit, but the number of returned parts never exceeds the limit.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the parts of an archive that have been uploaded in a multipart upload
            The example lists all the parts of a multipart upload.

            >>> await client.list_parts(account_id='-', vault_name='examplevault', upload_id='OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.list_parts_input.ListPartsInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.list_parts_output.ListPartsOutput"
        ]:
            import capo_glacier._operations.glacier.list_parts

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.list_parts.async_list_parts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.list_parts_input.ListPartsInput = {
            "account_id": account_id,
            "vault_name": vault_name,
            "upload_id": upload_id,
        }
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_parts(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        upload_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        marker: Optional["capo_glacier.types.string.string"] = None,
        limit: Optional[int] = None,
    ) -> "AsyncIterator[capo_glacier.types.part_list_element.PartListElement]":
        _token = marker
        while True:
            _response = await self.list_parts(
                account_id,
                vault_name,
                upload_id,
                config_overrides=config_overrides,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("parts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def list_provisioned_capacity(
        self,
        account_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> "capo_glacier.types.list_provisioned_capacity_output.ListProvisionedCapacityOutput":
        """<p>This operation lists the provisioned capacity units for the specified AWS account.</p>

        Args:
            account_id: <p>The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '-' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don't include any hyphens ('-') in the ID. </p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the provisioned capacity units for an account
            The example lists the provisioned capacity units for an account.

            >>> await client.list_provisioned_capacity(account_id='-')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.list_provisioned_capacity_input.ListProvisionedCapacityInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.list_provisioned_capacity_output.ListProvisionedCapacityOutput"
        ]:
            import capo_glacier._operations.glacier.list_provisioned_capacity

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.list_provisioned_capacity.async_list_provisioned_capacity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.list_provisioned_capacity_input.ListProvisionedCapacityInput = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_vault(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> "capo_glacier.types.list_tags_for_vault_output.ListTagsForVaultOutput":
        r"""<p>This operation lists all the tags attached to a vault. The operation returns an empty map if there are no tags. For more information about tags, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/tagging.html\">Tagging Amazon Glacier Resources</a>.</p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the tags for a vault
            The example lists all the tags attached to the vault examplevault.

            >>> await client.list_tags_for_vault(account_id='-', vault_name='examplevault')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.list_tags_for_vault_input.ListTagsForVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.list_tags_for_vault_output.ListTagsForVaultOutput"
        ]:
            import capo_glacier._operations.glacier.list_tags_for_vault

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.list_tags_for_vault.async_list_tags_for_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.list_tags_for_vault_input.ListTagsForVaultInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_vaults(
        self,
        account_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        marker: Optional["capo_glacier.types.string.string"] = None,
        limit: Optional[int] = None,
    ) -> "capo_glacier.types.list_vaults_output.ListVaultsOutput":
        r"""<p>This operation lists all vaults owned by the calling user's account. The list returned in the response is ASCII-sorted by vault name.</p> <p>By default, this operation returns up to 10 items. If there are more vaults to list, the response <code>marker</code> field contains the vault Amazon Resource Name (ARN) at which to continue the list with a new List Vaults request; otherwise, the <code>marker</code> field is <code>null</code>. To return a list of vaults that begins at a specific vault, set the <code>marker</code> request parameter to the vault ARN you obtained from a previous List Vaults request. You can also limit the number of vaults returned in the response by specifying the <code>limit</code> parameter in the request. </p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p>For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info.html\">Retrieving Vault Metadata in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vaults-get.html\">List Vaults </a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>
            marker: <p>A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin.</p>
            limit: <p>The maximum number of vaults to be returned. The default limit is 10. The number of vaults returned might be fewer than the specified limit, but the number of returned vaults never exceeds the limit.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list all vaults owned by the calling user's account
            The example lists all vaults owned by the specified AWS account.

            >>> await client.list_vaults(account_id='-', marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.list_vaults_input.ListVaultsInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.list_vaults_output.ListVaultsOutput"
        ]:
            import capo_glacier._operations.glacier.list_vaults

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.list_vaults.async_list_vaults(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.list_vaults_input.ListVaultsInput = {
            "account_id": account_id
        }
        if marker is not None:
            input_["marker"] = marker
        if limit is not None:
            input_["limit"] = limit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_vaults(
        self,
        account_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        marker: Optional["capo_glacier.types.string.string"] = None,
        limit: Optional[int] = None,
    ) -> "AsyncIterator[capo_glacier.types.describe_vault_output.DescribeVaultOutput]":
        _token = marker
        while True:
            _response = await self.list_vaults(
                account_id,
                config_overrides=config_overrides,
                marker=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("vault_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def purchase_provisioned_capacity(
        self,
        account_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
    ) -> "capo_glacier.types.purchase_provisioned_capacity_output.PurchaseProvisionedCapacityOutput":
        """<p>This operation purchases a provisioned capacity unit for an AWS account. </p>

        Args:
            account_id: <p>The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '-' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don't include any hyphens ('-') in the ID. </p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.limit_exceeded_exception.LimitExceededException: <p>Returned if the request results in a vault or account limit being exceeded.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To purchases a provisioned capacity unit for an AWS account
            The example purchases provisioned capacity unit for an AWS account.

            >>> await client.purchase_provisioned_capacity(account_id='-')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.purchase_provisioned_capacity_input.PurchaseProvisionedCapacityInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.purchase_provisioned_capacity_output.PurchaseProvisionedCapacityOutput"
        ]:
            import capo_glacier._operations.glacier.purchase_provisioned_capacity

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.purchase_provisioned_capacity.async_purchase_provisioned_capacity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.purchase_provisioned_capacity_input.PurchaseProvisionedCapacityInput = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_tags_from_vault(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        tag_keys: Optional["capo_glacier.types.tag_key_list.TagKeyList"] = None,
    ) -> None:
        r"""<p>This operation removes one or more tags from the set of tags attached to a vault. For more information about tags, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/tagging.html\">Tagging Amazon Glacier Resources</a>. This operation is idempotent. The operation will be successful, even if there are no tags attached to the vault. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            tag_keys: <p>A list of tag keys. Each corresponding tag is removed from the vault.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To remove tags from a vault
            The example removes two tags from the vault named examplevault.

            >>> await client.remove_tags_from_vault(account_id='-', vault_name='examplevault', tag_keys=['examplekey1', 'examplekey2'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.remove_tags_from_vault_input.RemoveTagsFromVaultInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.remove_tags_from_vault

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.remove_tags_from_vault.async_remove_tags_from_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.remove_tags_from_vault_input.RemoveTagsFromVaultInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_data_retrieval_policy(
        self,
        account_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        policy: Optional[
            "capo_glacier.types.data_retrieval_policy.DataRetrievalPolicy"
        ] = None,
    ) -> None:
        r"""<p>This operation sets and then enacts a data retrieval policy in the region specified in the PUT request. You can set one policy per region for an AWS account. The policy is enacted within a few minutes of a successful PUT operation.</p> <p>The set policy operation does not affect retrieval jobs that were in progress before the policy was enacted. For more information about data retrieval policies, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/data-retrieval-policy.html\">Amazon Glacier Data Retrieval Policies</a>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>
            policy: <p>The data retrieval policy in JSON format.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To set and then enact a data retrieval policy
            The example sets and then enacts a data retrieval policy.

            >>> await client.set_data_retrieval_policy(account_id='-', policy={'Rules': [{'Strategy': 'BytesPerHour', 'BytesPerHour': 10737418240}]})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.set_data_retrieval_policy_input.SetDataRetrievalPolicyInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.set_data_retrieval_policy

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.set_data_retrieval_policy.async_set_data_retrieval_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.set_data_retrieval_policy_input.SetDataRetrievalPolicyInput = {
            "account_id": account_id
        }
        if policy is not None:
            input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_vault_access_policy(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        policy: Optional[
            "capo_glacier.types.vault_access_policy.VaultAccessPolicy"
        ] = None,
    ) -> None:
        r"""<p>This operation configures an access policy for a vault and will overwrite an existing policy. To configure a vault access policy, send a PUT request to the <code>access-policy</code> subresource of the vault. An access policy is specific to a vault and is also called a vault subresource. You can set one access policy per vault and the policy can be up to 20 KB in size. For more information about vault access policies, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html\">Amazon Glacier Access Control with Vault Access Policies</a>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            policy: <p>The vault access policy as a JSON string.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To set the access-policy on a vault
            The example configures an access policy for the vault named examplevault.

            >>> await client.set_vault_access_policy(account_id='-', vault_name='examplevault', policy={'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-owner-access-rights","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault"}]}'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.set_vault_access_policy_input.SetVaultAccessPolicyInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.set_vault_access_policy

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.set_vault_access_policy.async_set_vault_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.set_vault_access_policy_input.SetVaultAccessPolicyInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }
        if policy is not None:
            input_["policy"] = policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_vault_notifications(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        vault_notification_config: Optional[
            "capo_glacier.types.vault_notification_config.VaultNotificationConfig"
        ] = None,
    ) -> None:
        r"""<p>This operation configures notifications that will be sent when specific events happen to a vault. By default, you don't get any notifications.</p> <p>To configure vault notifications, send a PUT request to the <code>notification-configuration</code> subresource of the vault. The request should include a JSON document that provides an Amazon SNS topic and specific events for which you want Amazon Glacier to send notifications to the topic.</p> <p>Amazon SNS topics must grant permission to the vault to be allowed to publish notifications to the topic. You can configure a vault to publish a notification for the following vault events:</p> <ul> <li> <p> <b>ArchiveRetrievalCompleted</b> This event occurs when a job that was initiated for an archive retrieval is completed (<a>InitiateJob</a>). The status of the completed job can be \"Succeeded\" or \"Failed\". The notification sent to the SNS topic is the same output as returned from <a>DescribeJob</a>. </p> </li> <li> <p> <b>InventoryRetrievalCompleted</b> This event occurs when a job that was initiated for an inventory retrieval is completed (<a>InitiateJob</a>). The status of the completed job can be \"Succeeded\" or \"Failed\". The notification sent to the SNS topic is the same output as returned from <a>DescribeJob</a>. </p> </li> </ul> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p>For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html\">Configuring Vault Notifications in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-put.html\">Set Vault Notification Configuration </a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>
            vault_name: <p>The name of the vault.</p>
            vault_notification_config: <p>Provides options for specifying notification configuration.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To configure a vault to post a message to an Amazon SNS topic when jobs complete
            The example sets the examplevault notification configuration.

            >>> await client.set_vault_notifications(account_id='-', vault_name='examplevault', vault_notification_config={'Events': ['ArchiveRetrievalCompleted', 'InventoryRetrievalCompleted'], 'SNSTopic': 'arn:aws:sns:us-west-2:012345678901:mytopic'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.set_vault_notifications_input.SetVaultNotificationsInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_glacier._operations.glacier.set_vault_notifications

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.set_vault_notifications.async_set_vault_notifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.set_vault_notifications_input.SetVaultNotificationsInput = {
            "account_id": account_id,
            "vault_name": vault_name,
        }
        if vault_notification_config is not None:
            input_["vault_notification_config"] = vault_notification_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def upload_archive(
        self,
        vault_name: "capo_glacier.types.string.string",
        account_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        archive_description: Optional["capo_glacier.types.string.string"] = None,
        checksum: Optional["capo_glacier.types.string.string"] = None,
        body: Optional[
            Body[AsyncIterator[bytes]] | AsyncIterator[bytes] | bytes
        ] = None,
    ) -> "capo_glacier.types.archive_creation_output.ArchiveCreationOutput":
        r"""<p>This operation adds an archive to a vault. This is a synchronous operation, and for a successful upload, your data is durably persisted. Amazon Glacier returns the archive ID in the <code>x-amz-archive-id</code> header of the response. </p> <p>You must use the archive ID to access your data in Amazon Glacier. After you upload an archive, you should save the archive ID returned so that you can retrieve or delete the archive later. Besides saving the archive ID, you can also index it and give it a friendly name to allow for better searching. You can also use the optional archive description field to specify how the archive is referred to in an external index of archives, such as you might create in Amazon DynamoDB. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see <a>InitiateJob</a>. </p> <p>You must provide a SHA256 tree hash of the data you are uploading. For information about computing a SHA256 tree hash, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html\">Computing Checksums</a>. </p> <p>You can optionally specify an archive description of up to 1,024 printable ASCII characters. You can get the archive description when you either retrieve the archive or get the vault inventory. For more information, see <a>InitiateJob</a>. Amazon Glacier does not interpret the description in any way. An archive description does not need to be unique. You cannot use the description to retrieve or sort the archive list. </p> <p>Archives are immutable. After you upload an archive, you cannot edit the archive or its description.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p> For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive.html\">Uploading an Archive in Amazon Glacier</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html\">Upload Archive</a> in the <i>Amazon Glacier Developer Guide</i>. </p>

        Args:
            vault_name: <p>The name of the vault.</p>
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            archive_description: <p>The optional description of the archive you are uploading.</p>
            checksum: <p>The SHA256 tree hash of the data being uploaded.</p>
            body: <p>The data to upload.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.request_timeout_exception.RequestTimeoutException: <p>Returned if, when uploading an archive, Amazon Glacier times out while receiving the upload.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To upload an archive
            The example adds an archive to a vault.

            >>> await client.upload_archive(vault_name='my-vault', account_id='-', archive_description='', checksum='', body='example-data-to-upload')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.upload_archive_input.UploadArchiveInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.archive_creation_output.ArchiveCreationOutput"
        ]:
            import capo_glacier._operations.glacier.upload_archive

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.upload_archive.async_upload_archive(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.upload_archive_input.UploadArchiveInput = {
            "vault_name": vault_name,
            "account_id": account_id,
        }
        if archive_description is not None:
            input_["archive_description"] = archive_description
        if checksum is not None:
            input_["checksum"] = checksum
        if body is not None:
            input_["body"] = ensure_async_iterator(body)

        async with aclosing_bodies(input_):
            response = await aexecute_pipeline(
                AsyncOperationRequest(input=input_, options=options_),
                handler=_handler,
                interceptors=list(interceptors_),
            )
            await response.response.aclose()
            return response.output

    async def upload_multipart_part(
        self,
        account_id: "capo_glacier.types.string.string",
        vault_name: "capo_glacier.types.string.string",
        upload_id: "capo_glacier.types.string.string",
        *,
        config_overrides: Optional[AsyncGlacierClientConfig] = None,
        checksum: Optional["capo_glacier.types.string.string"] = None,
        range: Optional["capo_glacier.types.string.string"] = None,
        body: Optional[
            Body[AsyncIterator[bytes]] | AsyncIterator[bytes] | bytes
        ] = None,
    ) -> "capo_glacier.types.upload_multipart_part_output.UploadMultipartPartOutput":
        r"""<p>This operation uploads a part of an archive. You can upload archive parts in any order. You can also upload them in parallel. You can upload up to 10,000 parts for a multipart upload.</p> <p>Amazon Glacier rejects your upload part request if any of the following conditions is true:</p> <ul> <li> <p> <b>SHA256 tree hash does not match</b>To ensure that part data is not corrupted in transmission, you compute a SHA256 tree hash of the part and include it in your request. Upon receiving the part data, Amazon Glacier also computes a SHA256 tree hash. If these hash values don't match, the operation fails. For information about computing a SHA256 tree hash, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html\">Computing Checksums</a>.</p> </li> <li> <p> <b>Part size does not match</b>The size of each part except the last must match the size specified in the corresponding <a>InitiateMultipartUpload</a> request. The size of the last part must be the same size as, or smaller than, the specified size.</p> <note> <p>If you upload a part whose size is smaller than the part size you specified in your initiate multipart upload request and that part is not the last part, then the upload part request will succeed. However, the subsequent Complete Multipart Upload request will fail.</p> </note> </li> <li> <p> <b>Range does not align</b>The byte range value in the request does not align with the part size specified in the corresponding initiate request. For example, if you specify a part size of 4194304 bytes (4 MB), then 0 to 4194303 bytes (4 MB - 1) and 4194304 (4 MB) to 8388607 (8 MB - 1) are valid part ranges. However, if you set a range value of 2 MB to 6 MB, the range does not align with the part size and the upload will fail. </p> </li> </ul> <p>This operation is idempotent. If you upload the same part multiple times, the data included in the most recent request overwrites the previously uploaded data.</p> <p>An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html\">Access Control Using AWS Identity and Access Management (IAM)</a>.</p> <p> For conceptual information and underlying REST API, see <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html\">Uploading Large Archives in Parts (Multipart Upload)</a> and <a href=\"https://docs.aws.amazon.com/amazonglacier/latest/dev/api-upload-part.html\">Upload Part </a> in the <i>Amazon Glacier Developer Guide</i>.</p>

        Args:
            account_id: <p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>
            vault_name: <p>The name of the vault.</p>
            upload_id: <p>The upload ID of the multipart upload.</p>
            checksum: <p>The SHA256 tree hash of the data being uploaded.</p>
            range: <p>Identifies the range of bytes in the assembled archive that will be uploaded in this part. Amazon Glacier uses this information to assemble the archive in the proper sequence. The format of this header follows RFC 2616. An example header is Content-Range:bytes 0-4194303/*.</p>
            body: <p>The data to upload.</p>

        Raises:
            capo_glacier.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>Returned if a parameter of the request is incorrectly specified.</p>
            capo_glacier.errors.missing_parameter_value_exception.MissingParameterValueException: <p>Returned if a required header or parameter is missing from the request.</p>
            capo_glacier.errors.no_longer_supported_exception.NoLongerSupportedException: <p>Returned if the request was made by a customer with no Amazon Glacier storage. The request is denied as the API is no longer supported for new customers. Please use Amazon S3 Glacier storage classes instead.</p>
            capo_glacier.errors.request_timeout_exception.RequestTimeoutException: <p>Returned if, when uploading an archive, Amazon Glacier times out while receiving the upload.</p>
            capo_glacier.errors.resource_not_found_exception.ResourceNotFoundException: <p>Returned if the specified resource (such as a vault, upload ID, or job ID) doesn't exist.</p>
            capo_glacier.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_glacier.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To upload the first part of an archive
            The example uploads the first 1 MiB (1024 x 1024 bytes) part of an archive.

            >>> await client.upload_multipart_part(account_id='-', vault_name='examplevault', upload_id='19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ', checksum='c06f7cd4baacb087002a99a5f48bf953', range='bytes 0-1048575/*', body='part1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_glacier.types.upload_multipart_part_input.UploadMultipartPartInput]",
        ) -> AsyncOperationResponse[
            "capo_glacier.types.upload_multipart_part_output.UploadMultipartPartOutput"
        ]:
            import capo_glacier._operations.glacier.upload_multipart_part

            (
                output,
                http_response,
            ) = await capo_glacier._operations.glacier.upload_multipart_part.async_upload_multipart_part(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_glacier.types.upload_multipart_part_input.UploadMultipartPartInput = {
            "account_id": account_id,
            "vault_name": vault_name,
            "upload_id": upload_id,
        }
        if checksum is not None:
            input_["checksum"] = checksum
        if range is not None:
            input_["range"] = range
        if body is not None:
            input_["body"] = ensure_async_iterator(body)

        async with aclosing_bodies(input_):
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
