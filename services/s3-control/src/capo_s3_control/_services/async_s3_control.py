"""Generated from Smithy shape ``com.amazonaws.s3control#AWSS3ControlServiceV20180820``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_s3_control._auth._signers
import capo_s3_control._auth._sigv4
from capo_s3_control._auth._identity import Credentials
from capo_s3_control._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_s3_control._auth._zapros_handler import AuthMiddleware
from capo_s3_control._pagination import resolve_path as _resolve_path
from capo_s3_control._services._aws_config import aaws_config
from capo_s3_control._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_s3_control.types.access_grant_id
    import capo_s3_control.types.access_grants_location_configuration
    import capo_s3_control.types.access_grants_location_id
    import capo_s3_control.types.access_point
    import capo_s3_control.types.access_point_name
    import capo_s3_control.types.account_id
    import capo_s3_control.types.associate_access_grants_identity_center_request
    import capo_s3_control.types.async_request_token_arn
    import capo_s3_control.types.audit_context
    import capo_s3_control.types.boolean
    import capo_s3_control.types.bucket_canned_acl
    import capo_s3_control.types.bucket_name
    import capo_s3_control.types.config_id
    import capo_s3_control.types.confirm_remove_self_bucket_access
    import capo_s3_control.types.confirmation_required
    import capo_s3_control.types.continuation_token
    import capo_s3_control.types.create_access_grant_request
    import capo_s3_control.types.create_access_grant_result
    import capo_s3_control.types.create_access_grants_instance_request
    import capo_s3_control.types.create_access_grants_instance_result
    import capo_s3_control.types.create_access_grants_location_request
    import capo_s3_control.types.create_access_grants_location_result
    import capo_s3_control.types.create_access_point_for_object_lambda_request
    import capo_s3_control.types.create_access_point_for_object_lambda_result
    import capo_s3_control.types.create_access_point_request
    import capo_s3_control.types.create_access_point_result
    import capo_s3_control.types.create_bucket_configuration
    import capo_s3_control.types.create_bucket_request
    import capo_s3_control.types.create_bucket_result
    import capo_s3_control.types.create_job_request
    import capo_s3_control.types.create_job_result
    import capo_s3_control.types.create_multi_region_access_point_input
    import capo_s3_control.types.create_multi_region_access_point_request
    import capo_s3_control.types.create_multi_region_access_point_result
    import capo_s3_control.types.create_storage_lens_group_request
    import capo_s3_control.types.data_source_id
    import capo_s3_control.types.data_source_type
    import capo_s3_control.types.delete_access_grant_request
    import capo_s3_control.types.delete_access_grants_instance_request
    import capo_s3_control.types.delete_access_grants_instance_resource_policy_request
    import capo_s3_control.types.delete_access_grants_location_request
    import capo_s3_control.types.delete_access_point_for_object_lambda_request
    import capo_s3_control.types.delete_access_point_policy_for_object_lambda_request
    import capo_s3_control.types.delete_access_point_policy_request
    import capo_s3_control.types.delete_access_point_request
    import capo_s3_control.types.delete_access_point_scope_request
    import capo_s3_control.types.delete_bucket_lifecycle_configuration_request
    import capo_s3_control.types.delete_bucket_policy_request
    import capo_s3_control.types.delete_bucket_replication_request
    import capo_s3_control.types.delete_bucket_request
    import capo_s3_control.types.delete_bucket_tagging_request
    import capo_s3_control.types.delete_job_tagging_request
    import capo_s3_control.types.delete_job_tagging_result
    import capo_s3_control.types.delete_multi_region_access_point_input
    import capo_s3_control.types.delete_multi_region_access_point_request
    import capo_s3_control.types.delete_multi_region_access_point_result
    import capo_s3_control.types.delete_public_access_block_request
    import capo_s3_control.types.delete_storage_lens_configuration_request
    import capo_s3_control.types.delete_storage_lens_configuration_tagging_request
    import capo_s3_control.types.delete_storage_lens_configuration_tagging_result
    import capo_s3_control.types.delete_storage_lens_group_request
    import capo_s3_control.types.describe_job_request
    import capo_s3_control.types.describe_job_result
    import capo_s3_control.types.describe_multi_region_access_point_operation_request
    import capo_s3_control.types.describe_multi_region_access_point_operation_result
    import capo_s3_control.types.dissociate_access_grants_identity_center_request
    import capo_s3_control.types.duration_seconds
    import capo_s3_control.types.get_access_grant_request
    import capo_s3_control.types.get_access_grant_result
    import capo_s3_control.types.get_access_grants_instance_for_prefix_request
    import capo_s3_control.types.get_access_grants_instance_for_prefix_result
    import capo_s3_control.types.get_access_grants_instance_request
    import capo_s3_control.types.get_access_grants_instance_resource_policy_request
    import capo_s3_control.types.get_access_grants_instance_resource_policy_result
    import capo_s3_control.types.get_access_grants_instance_result
    import capo_s3_control.types.get_access_grants_location_request
    import capo_s3_control.types.get_access_grants_location_result
    import capo_s3_control.types.get_access_point_configuration_for_object_lambda_request
    import capo_s3_control.types.get_access_point_configuration_for_object_lambda_result
    import capo_s3_control.types.get_access_point_for_object_lambda_request
    import capo_s3_control.types.get_access_point_for_object_lambda_result
    import capo_s3_control.types.get_access_point_policy_for_object_lambda_request
    import capo_s3_control.types.get_access_point_policy_for_object_lambda_result
    import capo_s3_control.types.get_access_point_policy_request
    import capo_s3_control.types.get_access_point_policy_result
    import capo_s3_control.types.get_access_point_policy_status_for_object_lambda_request
    import capo_s3_control.types.get_access_point_policy_status_for_object_lambda_result
    import capo_s3_control.types.get_access_point_policy_status_request
    import capo_s3_control.types.get_access_point_policy_status_result
    import capo_s3_control.types.get_access_point_request
    import capo_s3_control.types.get_access_point_result
    import capo_s3_control.types.get_access_point_scope_request
    import capo_s3_control.types.get_access_point_scope_result
    import capo_s3_control.types.get_bucket_lifecycle_configuration_request
    import capo_s3_control.types.get_bucket_lifecycle_configuration_result
    import capo_s3_control.types.get_bucket_policy_request
    import capo_s3_control.types.get_bucket_policy_result
    import capo_s3_control.types.get_bucket_replication_request
    import capo_s3_control.types.get_bucket_replication_result
    import capo_s3_control.types.get_bucket_request
    import capo_s3_control.types.get_bucket_result
    import capo_s3_control.types.get_bucket_tagging_request
    import capo_s3_control.types.get_bucket_tagging_result
    import capo_s3_control.types.get_bucket_versioning_request
    import capo_s3_control.types.get_bucket_versioning_result
    import capo_s3_control.types.get_data_access_request
    import capo_s3_control.types.get_data_access_result
    import capo_s3_control.types.get_job_tagging_request
    import capo_s3_control.types.get_job_tagging_result
    import capo_s3_control.types.get_multi_region_access_point_policy_request
    import capo_s3_control.types.get_multi_region_access_point_policy_result
    import capo_s3_control.types.get_multi_region_access_point_policy_status_request
    import capo_s3_control.types.get_multi_region_access_point_policy_status_result
    import capo_s3_control.types.get_multi_region_access_point_request
    import capo_s3_control.types.get_multi_region_access_point_result
    import capo_s3_control.types.get_multi_region_access_point_routes_request
    import capo_s3_control.types.get_multi_region_access_point_routes_result
    import capo_s3_control.types.get_public_access_block_output
    import capo_s3_control.types.get_public_access_block_request
    import capo_s3_control.types.get_storage_lens_configuration_request
    import capo_s3_control.types.get_storage_lens_configuration_result
    import capo_s3_control.types.get_storage_lens_configuration_tagging_request
    import capo_s3_control.types.get_storage_lens_configuration_tagging_result
    import capo_s3_control.types.get_storage_lens_group_request
    import capo_s3_control.types.get_storage_lens_group_result
    import capo_s3_control.types.grant_full_control
    import capo_s3_control.types.grant_read
    import capo_s3_control.types.grant_read_acp
    import capo_s3_control.types.grant_write
    import capo_s3_control.types.grant_write_acp
    import capo_s3_control.types.grantee
    import capo_s3_control.types.grantee_identifier
    import capo_s3_control.types.grantee_type
    import capo_s3_control.types.iam_role_arn
    import capo_s3_control.types.identity_center_application_arn
    import capo_s3_control.types.identity_center_arn
    import capo_s3_control.types.job_id
    import capo_s3_control.types.job_manifest
    import capo_s3_control.types.job_manifest_generator
    import capo_s3_control.types.job_operation
    import capo_s3_control.types.job_priority
    import capo_s3_control.types.job_report
    import capo_s3_control.types.job_status_list
    import capo_s3_control.types.job_status_update_reason
    import capo_s3_control.types.lifecycle_configuration
    import capo_s3_control.types.list_access_grants_instances_request
    import capo_s3_control.types.list_access_grants_instances_result
    import capo_s3_control.types.list_access_grants_locations_request
    import capo_s3_control.types.list_access_grants_locations_result
    import capo_s3_control.types.list_access_grants_request
    import capo_s3_control.types.list_access_grants_result
    import capo_s3_control.types.list_access_points_for_directory_buckets_request
    import capo_s3_control.types.list_access_points_for_directory_buckets_result
    import capo_s3_control.types.list_access_points_for_object_lambda_request
    import capo_s3_control.types.list_access_points_for_object_lambda_result
    import capo_s3_control.types.list_access_points_request
    import capo_s3_control.types.list_access_points_result
    import capo_s3_control.types.list_caller_access_grants_entry
    import capo_s3_control.types.list_caller_access_grants_request
    import capo_s3_control.types.list_caller_access_grants_result
    import capo_s3_control.types.list_jobs_request
    import capo_s3_control.types.list_jobs_result
    import capo_s3_control.types.list_multi_region_access_points_request
    import capo_s3_control.types.list_multi_region_access_points_result
    import capo_s3_control.types.list_regional_buckets_request
    import capo_s3_control.types.list_regional_buckets_result
    import capo_s3_control.types.list_storage_lens_configurations_request
    import capo_s3_control.types.list_storage_lens_configurations_result
    import capo_s3_control.types.list_storage_lens_groups_request
    import capo_s3_control.types.list_storage_lens_groups_result
    import capo_s3_control.types.list_tags_for_resource_request
    import capo_s3_control.types.list_tags_for_resource_result
    import capo_s3_control.types.max_results
    import capo_s3_control.types.mfa
    import capo_s3_control.types.multi_region_access_point_client_token
    import capo_s3_control.types.multi_region_access_point_id
    import capo_s3_control.types.multi_region_access_point_name
    import capo_s3_control.types.non_empty_max_length64_string
    import capo_s3_control.types.non_empty_max_length256_string
    import capo_s3_control.types.non_empty_max_length1024_string
    import capo_s3_control.types.object_lambda_access_point
    import capo_s3_control.types.object_lambda_access_point_name
    import capo_s3_control.types.object_lambda_configuration
    import capo_s3_control.types.object_lambda_policy
    import capo_s3_control.types.object_lock_enabled_for_bucket
    import capo_s3_control.types.organization
    import capo_s3_control.types.permission
    import capo_s3_control.types.policy
    import capo_s3_control.types.policy_document
    import capo_s3_control.types.privilege
    import capo_s3_control.types.public_access_block_configuration
    import capo_s3_control.types.put_access_grants_instance_resource_policy_request
    import capo_s3_control.types.put_access_grants_instance_resource_policy_result
    import capo_s3_control.types.put_access_point_configuration_for_object_lambda_request
    import capo_s3_control.types.put_access_point_policy_for_object_lambda_request
    import capo_s3_control.types.put_access_point_policy_request
    import capo_s3_control.types.put_access_point_scope_request
    import capo_s3_control.types.put_bucket_lifecycle_configuration_request
    import capo_s3_control.types.put_bucket_policy_request
    import capo_s3_control.types.put_bucket_replication_request
    import capo_s3_control.types.put_bucket_tagging_request
    import capo_s3_control.types.put_bucket_versioning_request
    import capo_s3_control.types.put_job_tagging_request
    import capo_s3_control.types.put_job_tagging_result
    import capo_s3_control.types.put_multi_region_access_point_policy_input
    import capo_s3_control.types.put_multi_region_access_point_policy_request
    import capo_s3_control.types.put_multi_region_access_point_policy_result
    import capo_s3_control.types.put_public_access_block_request
    import capo_s3_control.types.put_storage_lens_configuration_request
    import capo_s3_control.types.put_storage_lens_configuration_tagging_request
    import capo_s3_control.types.put_storage_lens_configuration_tagging_result
    import capo_s3_control.types.replication_configuration
    import capo_s3_control.types.requested_job_status
    import capo_s3_control.types.route_list
    import capo_s3_control.types.s3_prefix
    import capo_s3_control.types.s3_prefix_type
    import capo_s3_control.types.s3_resource_arn
    import capo_s3_control.types.s3_tag_set
    import capo_s3_control.types.scope
    import capo_s3_control.types.storage_lens_configuration
    import capo_s3_control.types.storage_lens_group
    import capo_s3_control.types.storage_lens_group_name
    import capo_s3_control.types.storage_lens_tags
    import capo_s3_control.types.string_for_next_token
    import capo_s3_control.types.submit_multi_region_access_point_routes_request
    import capo_s3_control.types.submit_multi_region_access_point_routes_result
    import capo_s3_control.types.tag_key_list
    import capo_s3_control.types.tag_list
    import capo_s3_control.types.tag_resource_request
    import capo_s3_control.types.tag_resource_result
    import capo_s3_control.types.tagging
    import capo_s3_control.types.untag_resource_request
    import capo_s3_control.types.untag_resource_result
    import capo_s3_control.types.update_access_grants_location_request
    import capo_s3_control.types.update_access_grants_location_result
    import capo_s3_control.types.update_job_priority_request
    import capo_s3_control.types.update_job_priority_result
    import capo_s3_control.types.update_job_status_request
    import capo_s3_control.types.update_job_status_result
    import capo_s3_control.types.update_storage_lens_group_request
    import capo_s3_control.types.versioning_configuration
    import capo_s3_control.types.vpc_configuration


class AsyncS3ControlClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_fips: bool | None
    use_dual_stack: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None
    use_arn_region: bool | None


class AsyncS3ControlClient:
    """A client for the ``S3Control`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
        use_arn_region: Enables this client to use an ARN's region when constructing an endpoint instead of the client's configured region.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_fips: bool | None = None,
        use_dual_stack: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
        use_arn_region: bool | None = None,
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
        self._config = AsyncS3ControlClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "use_dual_stack": use_dual_stack,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
                "use_arn_region": use_arn_region,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncS3ControlClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncS3ControlClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
            use_arn_region=overrides.get(
                "use_arn_region", self._config.get("use_arn_region")
            ),
        )
        return interceptors_, options_

    async def associate_access_grants_identity_center(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        identity_center_arn: "capo_s3_control.types.identity_center_arn.IdentityCenterArn",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p>Associate your S3 Access Grants instance with an Amazon Web Services IAM Identity Center instance. Use this action if you want to create access grants for users or groups from your corporate identity directory. First, you must add your corporate identity directory to Amazon Web Services IAM Identity Center. Then, you can associate this IAM Identity Center instance with your S3 Access Grants instance.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:AssociateAccessGrantsIdentityCenter</code> permission to use this operation. </p> </dd> <dt>Additional Permissions</dt> <dd> <p>You must also have the following permissions: <code>sso:CreateApplication</code>, <code>sso:PutApplicationGrant</code>, and <code>sso:PutApplicationAuthenticationMethod</code>. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            identity_center_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services IAM Identity Center instance that you are associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate identity directory that you added to the IAM Identity Center. You can use the <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html">ListInstances</a> API operation to retrieve a list of your Identity Center instances and their ARNs.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.associate_access_grants_identity_center_request.AssociateAccessGrantsIdentityCenterRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.associate_access_grants_identity_center

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.associate_access_grants_identity_center.async_associate_access_grants_identity_center(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.associate_access_grants_identity_center_request.AssociateAccessGrantsIdentityCenterRequest = {
            "account_id": account_id,
            "identity_center_arn": identity_center_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_access_grant(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        access_grants_location_id: "capo_s3_control.types.access_grants_location_id.AccessGrantsLocationId",
        grantee: "capo_s3_control.types.grantee.Grantee",
        permission: "capo_s3_control.types.permission.Permission",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        access_grants_location_configuration: Optional[
            "capo_s3_control.types.access_grants_location_configuration.AccessGrantsLocationConfiguration"
        ] = None,
        application_arn: Optional[
            "capo_s3_control.types.identity_center_application_arn.IdentityCenterApplicationArn"
        ] = None,
        s3_prefix_type: Optional[
            "capo_s3_control.types.s3_prefix_type.S3PrefixType"
        ] = None,
        tags: Optional["capo_s3_control.types.tag_list.TagList"] = None,
    ) -> "capo_s3_control.types.create_access_grant_result.CreateAccessGrantResult":
        """<p>Creates an access grant that gives a grantee access to your S3 data. The grantee can be an IAM user or role or a directory user, or group. Before you can create a grant, you must have an S3 Access Grants instance in the same Region as the S3 data. You can create an S3 Access Grants instance using the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsInstance.html">CreateAccessGrantsInstance</a>. You must also have registered at least one S3 data location in your S3 Access Grants instance using <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsLocation.html">CreateAccessGrantsLocation</a>. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:CreateAccessGrant</code> permission to use this operation. </p> </dd> <dt>Additional Permissions</dt> <dd> <p>For any directory identity - <code>sso:DescribeInstance</code> and <code>sso:DescribeApplication</code> </p> <p>For directory users - <code>identitystore:DescribeUser</code> </p> <p>For directory groups - <code>identitystore:DescribeGroup</code> </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            access_grants_location_id: <p>The ID of the registered location to which you are granting access. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p> <p>If you are passing the <code>default</code> location, you cannot create an access grant for the entire default location. You must also specify a bucket or a bucket and prefix in the <code>Subprefix</code> field. </p>
            access_grants_location_configuration: <p>The configuration options of the grant location. The grant location is the S3 path to the data to which you are granting access. It contains the <code>S3SubPrefix</code> field. The grant scope is the result of appending the subprefix to the location scope of the registered location.</p>
            grantee: <p>The user, group, or role to which you are granting access. You can grant access to an IAM user or role. If you have added your corporate directory to Amazon Web Services IAM Identity Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee can also be a corporate directory user or group.</p>
            permission: <p>The type of access that you are granting to your S3 data, which can be set to one of the following values:</p> <ul> <li> <p> <code>READ</code> – Grant read-only access to the S3 data.</p> </li> <li> <p> <code>WRITE</code> – Grant write-only access to the S3 data.</p> </li> <li> <p> <code>READWRITE</code> – Grant both read and write access to the S3 data.</p> </li> </ul>
            application_arn: <p>The Amazon Resource Name (ARN) of an Amazon Web Services IAM Identity Center application associated with your Identity Center instance. If an application ARN is included in the request to create an access grant, the grantee can only access the S3 data through this application. </p>
            s3_prefix_type: <p>The type of <code>S3SubPrefix</code>. The only possible value is <code>Object</code>. Pass this value if the access grant scope is an object. Do not pass this value if the access grant scope is a bucket or a bucket and a prefix. </p>
            tags: <p>The Amazon Web Services resource tags that you are adding to the access grant. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.create_access_grant_request.CreateAccessGrantRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.create_access_grant_result.CreateAccessGrantResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.create_access_grant

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.create_access_grant.async_create_access_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.create_access_grant_request.CreateAccessGrantRequest = {
            "account_id": account_id,
            "access_grants_location_id": access_grants_location_id,
            "grantee": grantee,
            "permission": permission,
        }
        if access_grants_location_configuration is not None:
            input_["access_grants_location_configuration"] = (
                access_grants_location_configuration
            )
        if application_arn is not None:
            input_["application_arn"] = application_arn
        if s3_prefix_type is not None:
            input_["s3_prefix_type"] = s3_prefix_type
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_access_grants_instance(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        identity_center_arn: Optional[
            "capo_s3_control.types.identity_center_arn.IdentityCenterArn"
        ] = None,
        tags: Optional["capo_s3_control.types.tag_list.TagList"] = None,
    ) -> "capo_s3_control.types.create_access_grants_instance_result.CreateAccessGrantsInstanceResult":
        """<p>Creates an S3 Access Grants instance, which serves as a logical grouping for access grants. You can create one S3 Access Grants instance per Region per account. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:CreateAccessGrantsInstance</code> permission to use this operation. </p> </dd> <dt>Additional Permissions</dt> <dd> <p>To associate an IAM Identity Center instance with your S3 Access Grants instance, you must also have the <code>sso:DescribeInstance</code>, <code>sso:CreateApplication</code>, <code>sso:PutApplicationGrant</code>, and <code>sso:PutApplicationAuthenticationMethod</code> permissions. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            identity_center_arn: <p>If you would like to associate your S3 Access Grants instance with an Amazon Web Services IAM Identity Center instance, use this field to pass the Amazon Resource Name (ARN) of the Amazon Web Services IAM Identity Center instance that you are associating with your S3 Access Grants instance. An IAM Identity Center instance is your corporate identity directory that you added to the IAM Identity Center. You can use the <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html">ListInstances</a> API operation to retrieve a list of your Identity Center instances and their ARNs. </p>
            tags: <p>The Amazon Web Services resource tags that you are adding to the S3 Access Grants instance. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.create_access_grants_instance_request.CreateAccessGrantsInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.create_access_grants_instance_result.CreateAccessGrantsInstanceResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.create_access_grants_instance

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.create_access_grants_instance.async_create_access_grants_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.create_access_grants_instance_request.CreateAccessGrantsInstanceRequest = {
            "account_id": account_id
        }
        if identity_center_arn is not None:
            input_["identity_center_arn"] = identity_center_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_access_grants_location(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        location_scope: "capo_s3_control.types.s3_prefix.S3Prefix",
        iam_role_arn: "capo_s3_control.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        tags: Optional["capo_s3_control.types.tag_list.TagList"] = None,
    ) -> "capo_s3_control.types.create_access_grants_location_result.CreateAccessGrantsLocationResult":
        """<p>The S3 data location that you would like to register in your S3 Access Grants instance. Your S3 data must be in the same Region as your S3 Access Grants instance. The location can be one of the following: </p> <ul> <li> <p>The default S3 location <code>s3://</code> </p> </li> <li> <p>A bucket - <code>S3://<bucket-name></code> </p> </li> <li> <p>A bucket and prefix - <code>S3://<bucket-name>/<prefix></code> </p> </li> </ul> <p>When you register a location, you must include the IAM role that has permission to manage the S3 location that you are registering. Give S3 Access Grants permission to assume this role <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-location.html">using a policy</a>. S3 Access Grants assumes this role to manage access to the location and to vend temporary credentials to grantees or client applications. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:CreateAccessGrantsLocation</code> permission to use this operation. </p> </dd> <dt>Additional Permissions</dt> <dd> <p>You must also have the following permission for the specified IAM role: <code>iam:PassRole</code> </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            location_scope: <p>The S3 path to the location that you are registering. The location scope can be the default S3 location <code>s3://</code>, the S3 path to a bucket <code>s3://<bucket></code>, or the S3 path to a bucket and prefix <code>s3://<bucket>/<prefix></code>. A prefix in S3 is a string of characters at the beginning of an object key name used to organize the objects that you store in your S3 buckets. For example, object key names that start with the <code>engineering/</code> prefix or object key names that start with the <code>marketing/campaigns/</code> prefix.</p>
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants assumes this role to manage access to the registered location. </p>
            tags: <p>The Amazon Web Services resource tags that you are adding to the S3 Access Grants location. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.create_access_grants_location_request.CreateAccessGrantsLocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.create_access_grants_location_result.CreateAccessGrantsLocationResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.create_access_grants_location

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.create_access_grants_location.async_create_access_grants_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.create_access_grants_location_request.CreateAccessGrantsLocationRequest = {
            "account_id": account_id,
            "location_scope": location_scope,
            "iam_role_arn": iam_role_arn,
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

    async def create_access_point(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.access_point_name.AccessPointName",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        vpc_configuration: Optional[
            "capo_s3_control.types.vpc_configuration.VpcConfiguration"
        ] = None,
        public_access_block_configuration: Optional[
            "capo_s3_control.types.public_access_block_configuration.PublicAccessBlockConfiguration"
        ] = None,
        bucket_account_id: Optional[
            "capo_s3_control.types.account_id.AccountId"
        ] = None,
        scope: Optional["capo_s3_control.types.scope.Scope"] = None,
        tags: Optional["capo_s3_control.types.tag_list.TagList"] = None,
    ) -> "capo_s3_control.types.create_access_point_result.CreateAccessPointResult":
        """<p>Creates an access point and associates it to a specified bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html">Managing access to shared datasets with access points</a> or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html">Managing access to shared datasets in directory buckets with access points</a> in the <i>Amazon S3 User Guide</i>.</p> <p>To create an access point and attach it to a volume on an Amazon FSx file system, see <a href="https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateAndAttachS3AccessPoint.html">CreateAndAttachS3AccessPoint</a> in the <i>Amazon FSx API Reference</i>.</p> <p></p> <note> <p>S3 on Outposts only supports VPC-style access points. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html"> Accessing Amazon S3 on Outposts using virtual private cloud (VPC) only access points</a> in the <i>Amazon S3 User Guide</i>.</p> </note> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html#API_control_CreateAccessPoint_Examples">Examples</a> section.</p> <p></p> <p>The following actions are related to <code>CreateAccessPoint</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html">GetAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html">DeleteAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html">ListAccessPoints</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForDirectoryBuckets.html">ListAccessPointsForDirectoryBuckets</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the account that owns the specified access point.</p>
            name: <p>The name you want to assign to this access point.</p> <p>For directory buckets, the access point name must consist of a base name that you provide and suffix that includes the <code>ZoneID</code> (Amazon Web Services Availability Zone or Local Zone) of your bucket location, followed by <code>--xa-s3</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html">Managing access to shared datasets in directory buckets with access points</a> in the <i>Amazon S3 User Guide</i>.</p>
            bucket: <p>The name of the bucket that you want to associate this access point with.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
            vpc_configuration: <p>If you include this field, Amazon S3 restricts access to this access point to requests from the specified virtual private cloud (VPC).</p> <note> <p>This is required for creating an access point for Amazon S3 on Outposts buckets.</p> </note>
            public_access_block_configuration: <p> The <code>PublicAccessBlock</code> configuration that you want to apply to the access point. </p>
            bucket_account_id: <p>The Amazon Web Services account ID associated with the S3 bucket associated with this access point.</p> <p>For same account access point when your bucket and access point belong to the same account owner, the <code>BucketAccountId</code> is not required. For cross-account access point when your bucket and access point are not in the same account, the <code>BucketAccountId</code> is required. </p>
            scope: <p>For directory buckets, you can filter access control to specific prefixes, API operations, or a combination of both. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html">Managing access to shared datasets in directory buckets with access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Scope is only supported for access points attached to directory buckets.</p> </note>
            tags: <p>An array of tags that you can apply to an access point. Tags are key-value pairs of metadata used to control access to your access points. For more information about tags, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html">Using tags with Amazon S3</a>. For information about tagging access points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#using-tags-for-abac">Using tags for attribute-based access control (ABAC)</a>.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.create_access_point_request.CreateAccessPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.create_access_point_result.CreateAccessPointResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.create_access_point

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.create_access_point.async_create_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.create_access_point_request.CreateAccessPointRequest = {
            "account_id": account_id,
            "name": name,
            "bucket": bucket,
        }
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if public_access_block_configuration is not None:
            input_["public_access_block_configuration"] = (
                public_access_block_configuration
            )
        if bucket_account_id is not None:
            input_["bucket_account_id"] = bucket_account_id
        if scope is not None:
            input_["scope"] = scope
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_access_point_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName",
        configuration: "capo_s3_control.types.object_lambda_configuration.ObjectLambdaConfiguration",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.create_access_point_for_object_lambda_result.CreateAccessPointForObjectLambdaResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Creates an Object Lambda Access Point. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html">Transforming objects with Object Lambda Access Points</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The following actions are related to <code>CreateAccessPointForObjectLambda</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html">DeleteAccessPointForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html">GetAccessPointForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html">ListAccessPointsForObjectLambda</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for owner of the specified Object Lambda Access Point.</p>
            name: <p>The name you want to assign to this Object Lambda Access Point.</p>
            configuration: <p>Object Lambda Access Point configuration as a JSON document.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.create_access_point_for_object_lambda_request.CreateAccessPointForObjectLambdaRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.create_access_point_for_object_lambda_result.CreateAccessPointForObjectLambdaResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.create_access_point_for_object_lambda

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.create_access_point_for_object_lambda.async_create_access_point_for_object_lambda(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.create_access_point_for_object_lambda_request.CreateAccessPointForObjectLambdaRequest = {
            "account_id": account_id,
            "name": name,
            "configuration": configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bucket(
        self,
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        acl: Optional["capo_s3_control.types.bucket_canned_acl.BucketCannedACL"] = None,
        create_bucket_configuration: Optional[
            "capo_s3_control.types.create_bucket_configuration.CreateBucketConfiguration"
        ] = None,
        grant_full_control: Optional[
            "capo_s3_control.types.grant_full_control.GrantFullControl"
        ] = None,
        grant_read: Optional["capo_s3_control.types.grant_read.GrantRead"] = None,
        grant_read_acp: Optional[
            "capo_s3_control.types.grant_read_acp.GrantReadACP"
        ] = None,
        grant_write: Optional["capo_s3_control.types.grant_write.GrantWrite"] = None,
        grant_write_acp: Optional[
            "capo_s3_control.types.grant_write_acp.GrantWriteACP"
        ] = None,
        object_lock_enabled_for_bucket: Optional[
            "capo_s3_control.types.object_lock_enabled_for_bucket.ObjectLockEnabledForBucket"
        ] = None,
        outpost_id: Optional[
            "capo_s3_control.types.non_empty_max_length64_string.NonEmptyMaxLength64String"
        ] = None,
    ) -> "capo_s3_control.types.create_bucket_result.CreateBucketResult":
        """<note> <p>This action creates an Amazon S3 on Outposts bucket. To create an S3 bucket, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html">Create Bucket</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Creates a new Outposts bucket. By creating the bucket, you become the bucket owner. To create an Outposts bucket, you must have S3 on Outposts. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in <i>Amazon S3 User Guide</i>.</p> <p>Not every string is an acceptable bucket name. For information on bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/BucketRestrictions.html#bucketnamingrules">Working with Amazon S3 Buckets</a>.</p> <p>S3 on Outposts buckets support:</p> <ul> <li> <p>Tags</p> </li> <li> <p>LifecycleConfigurations for deleting expired objects</p> </li> </ul> <p>For a complete list of restrictions and Amazon S3 feature limitations on S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OnOutpostsRestrictionsLimitations.html"> Amazon S3 on Outposts Restrictions and Limitations</a>.</p> <p>For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and <code>x-amz-outpost-id</code> in your API request, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html#API_control_CreateBucket_Examples">Examples</a> section.</p> <p>The following actions are related to <code>CreateBucket</code> for Amazon S3 on Outposts:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html">PutObject</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html">GetBucket</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucket.html">DeleteBucket</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html">CreateAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html">PutAccessPointPolicy</a> </p> </li> </ul>

        Args:
            acl: <p>The canned ACL to apply to the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
            bucket: <p>The name of the bucket.</p>
            create_bucket_configuration: <p>The configuration information for the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
            grant_full_control: <p>Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
            grant_read: <p>Allows grantee to list the objects in the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
            grant_read_acp: <p>Allows grantee to read the bucket ACL.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
            grant_write: <p>Allows grantee to create, overwrite, and delete any object in the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
            grant_write_acp: <p>Allows grantee to write the ACL for the applicable bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
            object_lock_enabled_for_bucket: <p>Specifies whether you want S3 Object Lock to be enabled for the new bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
            outpost_id: <p>The ID of the Outposts where the bucket is being created.</p> <note> <p>This ID is required by Amazon S3 on Outposts buckets.</p> </note>

        Raises:
            capo_s3_control.errors.bucket_already_exists.BucketAlreadyExists: <p>The requested Outposts bucket name is not available. The bucket namespace is shared by all users of the Outposts in this Region. Select a different name and try again.</p>
            capo_s3_control.errors.bucket_already_owned_by_you.BucketAlreadyOwnedByYou: <p>The Outposts bucket you tried to create already exists, and you own it. </p>
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.create_bucket_request.CreateBucketRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.create_bucket_result.CreateBucketResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.create_bucket

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.create_bucket.async_create_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.create_bucket_request.CreateBucketRequest = {
            "bucket": bucket
        }
        if acl is not None:
            input_["acl"] = acl
        if create_bucket_configuration is not None:
            input_["create_bucket_configuration"] = create_bucket_configuration
        if grant_full_control is not None:
            input_["grant_full_control"] = grant_full_control
        if grant_read is not None:
            input_["grant_read"] = grant_read
        if grant_read_acp is not None:
            input_["grant_read_acp"] = grant_read_acp
        if grant_write is not None:
            input_["grant_write"] = grant_write
        if grant_write_acp is not None:
            input_["grant_write_acp"] = grant_write_acp
        if object_lock_enabled_for_bucket is not None:
            input_["object_lock_enabled_for_bucket"] = object_lock_enabled_for_bucket
        if outpost_id is not None:
            input_["outpost_id"] = outpost_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_job(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        operation: "capo_s3_control.types.job_operation.JobOperation",
        report: "capo_s3_control.types.job_report.JobReport",
        client_request_token: "capo_s3_control.types.non_empty_max_length64_string.NonEmptyMaxLength64String",
        priority: "capo_s3_control.types.job_priority.JobPriority",
        role_arn: "capo_s3_control.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        confirmation_required: Optional[
            "capo_s3_control.types.confirmation_required.ConfirmationRequired"
        ] = None,
        manifest: Optional["capo_s3_control.types.job_manifest.JobManifest"] = None,
        description: Optional[
            "capo_s3_control.types.non_empty_max_length256_string.NonEmptyMaxLength256String"
        ] = None,
        tags: Optional["capo_s3_control.types.s3_tag_set.S3TagSet"] = None,
        manifest_generator: Optional[
            "capo_s3_control.types.job_manifest_generator.JobManifestGenerator"
        ] = None,
    ) -> "capo_s3_control.types.create_job_result.CreateJobResult":
        """<p>This operation creates an S3 Batch Operations job.</p> <p>You can use S3 Batch Operations to perform large-scale batch actions on Amazon S3 objects. Batch Operations can run a single action on lists of Amazon S3 objects that you specify. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html">S3 Batch Operations</a> in the <i>Amazon S3 User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>For information about permissions required to use the Batch Operations, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-iam-role-policies.html">Granting permissions for S3 Batch Operations</a> in the <i>Amazon S3 User Guide</i>.</p> </dd> </dl> <p></p> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html">DescribeJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html">ListJobs</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html">UpdateJobPriority</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html">UpdateJobStatus</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobOperation.html">JobOperation</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID that creates the job.</p>
            confirmation_required: <p>Indicates whether confirmation is required before Amazon S3 runs the job. Confirmation is only required for jobs created through the Amazon S3 console.</p>
            operation: <p>The action that you want this job to perform on every object listed in the manifest. For more information about the available actions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html">Operations</a> in the <i>Amazon S3 User Guide</i>.</p>
            report: <p>Configuration parameters for the optional job-completion report.</p>
            client_request_token: <p>An idempotency token to ensure that you don't accidentally submit the same request twice. You can use any string up to the maximum length.</p>
            manifest: <p>Configuration parameters for the manifest.</p>
            description: <p>A description for this job. You can use any string within the permitted length. Descriptions don't need to be unique and can be used for multiple jobs.</p>
            priority: <p>The numerical priority for this job. Higher numbers indicate higher priority.</p>
            role_arn: <p>The Amazon Resource Name (ARN) for the Identity and Access Management (IAM) role that Batch Operations will use to run this job's action on every object in the manifest.</p>
            tags: <p>A set of tags to associate with the S3 Batch Operations job. This is an optional parameter. </p>
            manifest_generator: <p>The attribute container for the ManifestGenerator details. Jobs must be created with either a manifest file or a ManifestGenerator, but not both.</p>

        Raises:
            capo_s3_control.errors.bad_request_exception.BadRequestException: <p></p>
            capo_s3_control.errors.idempotency_exception.IdempotencyException: <p></p>
            capo_s3_control.errors.internal_service_exception.InternalServiceException: <p></p>
            capo_s3_control.errors.too_many_requests_exception.TooManyRequestsException: <p></p>
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.create_job_request.CreateJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.create_job_result.CreateJobResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.create_job

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.create_job.async_create_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.create_job_request.CreateJobRequest = {
            "account_id": account_id,
            "operation": operation,
            "report": report,
            "client_request_token": client_request_token,
            "priority": priority,
            "role_arn": role_arn,
        }
        if confirmation_required is not None:
            input_["confirmation_required"] = confirmation_required
        if manifest is not None:
            input_["manifest"] = manifest
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if manifest_generator is not None:
            input_["manifest_generator"] = manifest_generator

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_multi_region_access_point(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        client_token: "capo_s3_control.types.multi_region_access_point_client_token.MultiRegionAccessPointClientToken",
        details: "capo_s3_control.types.create_multi_region_access_point_input.CreateMultiRegionAccessPointInput",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.create_multi_region_access_point_result.CreateMultiRegionAccessPointResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Creates a Multi-Region Access Point and associates it with the specified buckets. For more information about creating Multi-Region Access Points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html">Creating Multi-Region Access Points</a> in the <i>Amazon S3 User Guide</i>.</p> <p>This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html">Multi-Region Access Point restrictions and limitations</a> in the <i>Amazon S3 User Guide</i>.</p> <p>This request is asynchronous, meaning that you might receive a response before the command has completed. When this request provides a response, it provides a token that you can use to monitor the status of the request with <code>DescribeMultiRegionAccessPointOperation</code>.</p> <p>The following actions are related to <code>CreateMultiRegionAccessPoint</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html">DeleteMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html">DescribeMultiRegionAccessPointOperation</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html">GetMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html">ListMultiRegionAccessPoints</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point. The owner of the Multi-Region Access Point also must own the underlying buckets.</p>
            client_token: <p>An idempotency token used to identify the request and guarantee that requests are unique.</p>
            details: <p>A container element containing details about the Multi-Region Access Point.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.create_multi_region_access_point_request.CreateMultiRegionAccessPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.create_multi_region_access_point_result.CreateMultiRegionAccessPointResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.create_multi_region_access_point

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.create_multi_region_access_point.async_create_multi_region_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.create_multi_region_access_point_request.CreateMultiRegionAccessPointRequest = {
            "account_id": account_id,
            "client_token": client_token,
            "details": details,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_storage_lens_group(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        storage_lens_group: "capo_s3_control.types.storage_lens_group.StorageLensGroup",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        tags: Optional["capo_s3_control.types.tag_list.TagList"] = None,
    ) -> None:
        """<p> Creates a new S3 Storage Lens group and associates it with the specified Amazon Web Services account ID. An S3 Storage Lens group is a custom grouping of objects based on prefix, suffix, object tags, object size, object age, or a combination of these filters. For each Storage Lens group that you’ve created, you can also optionally add Amazon Web Services resource tags. For more information about S3 Storage Lens groups, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups-overview.html">Working with S3 Storage Lens groups</a>.</p> <p>To use this operation, you must have the permission to perform the <code>s3:CreateStorageLensGroup</code> action. If you’re trying to create a Storage Lens group with Amazon Web Services resource tags, you must also have permission to perform the <code>s3:TagResource</code> action. For more information about the required Storage Lens Groups permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_groups_permissions">Setting account permissions to use S3 Storage Lens groups</a>.</p> <p>For information about Storage Lens groups errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3LensErrorCodeList">List of Amazon S3 Storage Lens error codes</a>.</p>

        Args:
            account_id: <p> The Amazon Web Services account ID that the Storage Lens group is created from and associated with. </p>
            storage_lens_group: <p> The Storage Lens group configuration. </p>
            tags: <p> The Amazon Web Services resource tags that you're adding to your Storage Lens group. This parameter is optional. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.create_storage_lens_group_request.CreateStorageLensGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.create_storage_lens_group

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.create_storage_lens_group.async_create_storage_lens_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.create_storage_lens_group_request.CreateStorageLensGroupRequest = {
            "account_id": account_id,
            "storage_lens_group": storage_lens_group,
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

    async def delete_access_grant(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        access_grant_id: "capo_s3_control.types.access_grant_id.AccessGrantId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p>Deletes the access grant from the S3 Access Grants instance. You cannot undo an access grant deletion and the grantee will no longer have access to the S3 data.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:DeleteAccessGrant</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            access_grant_id: <p>The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access grant.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_access_grant_request.DeleteAccessGrantRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_access_grant

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_access_grant.async_delete_access_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_access_grant_request.DeleteAccessGrantRequest = {
            "account_id": account_id,
            "access_grant_id": access_grant_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_grants_instance(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p>Deletes your S3 Access Grants instance. You must first delete the access grants and locations before S3 Access Grants can delete the instance. See <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrant.html">DeleteAccessGrant</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsLocation.html">DeleteAccessGrantsLocation</a>. If you have associated an IAM Identity Center instance with your S3 Access Grants instance, you must first dissassociate the Identity Center instance from the S3 Access Grants instance before you can delete the S3 Access Grants instance. See <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AssociateAccessGrantsIdentityCenter.html">AssociateAccessGrantsIdentityCenter</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DissociateAccessGrantsIdentityCenter.html">DissociateAccessGrantsIdentityCenter</a>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:DeleteAccessGrantsInstance</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_access_grants_instance_request.DeleteAccessGrantsInstanceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_access_grants_instance

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_access_grants_instance.async_delete_access_grants_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_access_grants_instance_request.DeleteAccessGrantsInstanceRequest = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_grants_instance_resource_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p>Deletes the resource policy of the S3 Access Grants instance. The resource policy is used to manage cross-account access to your S3 Access Grants instance. By deleting the resource policy, you delete any cross-account permissions to your S3 Access Grants instance. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:DeleteAccessGrantsInstanceResourcePolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_access_grants_instance_resource_policy_request.DeleteAccessGrantsInstanceResourcePolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_access_grants_instance_resource_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_access_grants_instance_resource_policy.async_delete_access_grants_instance_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_access_grants_instance_resource_policy_request.DeleteAccessGrantsInstanceResourcePolicyRequest = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_grants_location(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        access_grants_location_id: "capo_s3_control.types.access_grants_location_id.AccessGrantsLocationId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p>Deregisters a location from your S3 Access Grants instance. You can only delete a location registration from an S3 Access Grants instance if there are no grants associated with this location. See <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrant.html">Delete a grant</a> for information on how to delete grants. You need to have at least one registered location in your S3 Access Grants instance in order to create access grants. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:DeleteAccessGrantsLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            access_grants_location_id: <p>The ID of the registered location that you are deregistering from your S3 Access Grants instance. S3 Access Grants assigned this ID when you registered the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_access_grants_location_request.DeleteAccessGrantsLocationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_access_grants_location

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_access_grants_location.async_delete_access_grants_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_access_grants_location_request.DeleteAccessGrantsLocationRequest = {
            "account_id": account_id,
            "access_grants_location_id": access_grants_location_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_point(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.access_point_name.AccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified access point.</p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html#API_control_DeleteAccessPoint_Examples">Examples</a> section.</p> <p>The following actions are related to <code>DeleteAccessPoint</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html">CreateAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html">GetAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html">ListAccessPoints</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the account that owns the specified access point.</p>
            name: <p>The name of the access point you want to delete.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name></code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_access_point_request.DeleteAccessPointRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_access_point

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_access_point.async_delete_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_access_point_request.DeleteAccessPointRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_point_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Deletes the specified Object Lambda Access Point.</p> <p>The following actions are related to <code>DeleteAccessPointForObjectLambda</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html">CreateAccessPointForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html">GetAccessPointForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html">ListAccessPointsForObjectLambda</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the account that owns the specified Object Lambda Access Point.</p>
            name: <p>The name of the access point you want to delete.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_access_point_for_object_lambda_request.DeleteAccessPointForObjectLambdaRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_access_point_for_object_lambda

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_access_point_for_object_lambda.async_delete_access_point_for_object_lambda(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_access_point_for_object_lambda_request.DeleteAccessPointForObjectLambdaRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_point_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.access_point_name.AccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p>Deletes the access point policy for the specified access point.</p> <p></p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html#API_control_DeleteAccessPointPolicy_Examples">Examples</a> section.</p> <p>The following actions are related to <code>DeleteAccessPointPolicy</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html">PutAccessPointPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html">GetAccessPointPolicy</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the account that owns the specified access point.</p>
            name: <p>The name of the access point whose policy you want to delete.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name></code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_access_point_policy_request.DeleteAccessPointPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_access_point_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_access_point_policy.async_delete_access_point_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_access_point_policy_request.DeleteAccessPointPolicyRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_point_policy_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Removes the resource policy for an Object Lambda Access Point.</p> <p>The following actions are related to <code>DeleteAccessPointPolicyForObjectLambda</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyForObjectLambda.html">GetAccessPointPolicyForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicyForObjectLambda.html">PutAccessPointPolicyForObjectLambda</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the account that owns the specified Object Lambda Access Point.</p>
            name: <p>The name of the Object Lambda Access Point you want to delete the policy for.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_access_point_policy_for_object_lambda_request.DeleteAccessPointPolicyForObjectLambdaRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_access_point_policy_for_object_lambda

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_access_point_policy_for_object_lambda.async_delete_access_point_policy_for_object_lambda(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_access_point_policy_for_object_lambda_request.DeleteAccessPointPolicyForObjectLambdaRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_access_point_scope(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.access_point_name.AccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p> Deletes an existing access point scope for a directory bucket.</p> <note> <p>When you delete the scope of an access point, all prefixes and permissions are deleted.</p> </note> <p>To use this operation, you must have the permission to perform the <code>s3express:DeleteAccessPointScope</code> action.</p> <p>For information about REST API errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#RESTErrorResponses">REST error responses</a>.</p>

        Args:
            account_id: <p> The Amazon Web Services account ID that owns the access point with the scope that you want to delete. </p>
            name: <p> The name of the access point with the scope that you want to delete. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_access_point_scope_request.DeleteAccessPointScopeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_access_point_scope

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_access_point_scope.async_delete_access_point_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_access_point_scope_request.DeleteAccessPointScopeRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bucket(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This action deletes an Amazon S3 on Outposts bucket. To delete an S3 bucket, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html">DeleteBucket</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Deletes the Amazon S3 on Outposts bucket. All objects (including all object versions and delete markers) in the bucket must be deleted before the bucket itself can be deleted. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in <i>Amazon S3 User Guide</i>.</p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucket.html#API_control_DeleteBucket_Examples">Examples</a> section.</p> <p class="title"> <b>Related Resources</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html">CreateBucket</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html">GetBucket</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html">DeleteObject</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID that owns the Outposts bucket.</p>
            bucket: <p>Specifies the bucket being deleted.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_bucket_request.DeleteBucketRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_bucket

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_bucket.async_delete_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_bucket_request.DeleteBucketRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bucket_lifecycle_configuration(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This action deletes an Amazon S3 on Outposts bucket's lifecycle configuration. To delete an S3 bucket's lifecycle configuration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html">DeleteBucketLifecycle</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Deletes the lifecycle configuration from the specified Outposts bucket. Amazon S3 on Outposts removes all the lifecycle configuration rules in the lifecycle subresource associated with the bucket. Your objects never expire, and Amazon S3 on Outposts no longer automatically deletes any objects on the basis of rules contained in the deleted lifecycle configuration. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in <i>Amazon S3 User Guide</i>.</p> <p>To use this operation, you must have permission to perform the <code>s3-outposts:PutLifecycleConfiguration</code> action. By default, the bucket owner has this permission and the Outposts bucket owner can grant this permission to others.</p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketLifecycleConfiguration.html#API_control_DeleteBucketLifecycleConfiguration_Examples">Examples</a> section.</p> <p>For more information about object expiration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#intro-lifecycle-rules-actions">Elements to Describe Lifecycle Actions</a>.</p> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html">PutBucketLifecycleConfiguration</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html">GetBucketLifecycleConfiguration</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID of the lifecycle configuration to delete.</p>
            bucket: <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_bucket_lifecycle_configuration_request.DeleteBucketLifecycleConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_bucket_lifecycle_configuration

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_bucket_lifecycle_configuration.async_delete_bucket_lifecycle_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_bucket_lifecycle_configuration_request.DeleteBucketLifecycleConfigurationRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bucket_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This action deletes an Amazon S3 on Outposts bucket policy. To delete an S3 bucket policy, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html">DeleteBucketPolicy</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>This implementation of the DELETE action uses the policy subresource to delete the policy of a specified Amazon S3 on Outposts bucket. If you are using an identity other than the root user of the Amazon Web Services account that owns the bucket, the calling identity must have the <code>s3-outposts:DeleteBucketPolicy</code> permissions on the specified Outposts bucket and belong to the bucket owner's account to use this action. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in <i>Amazon S3 User Guide</i>.</p> <p>If you don't have <code>DeleteBucketPolicy</code> permissions, Amazon S3 returns a <code>403 Access Denied</code> error. If you have the correct permissions, but you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a <code>405 Method Not Allowed</code> error. </p> <important> <p>As a security precaution, the root user of the Amazon Web Services account that owns a bucket can always use this action, even if the policy explicitly denies the root user the ability to perform this action.</p> </important> <p>For more information about bucket policies, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html">Using Bucket Policies and User Policies</a>. </p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketPolicy.html#API_control_DeleteBucketPolicy_Examples">Examples</a> section.</p> <p>The following actions are related to <code>DeleteBucketPolicy</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html">GetBucketPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketPolicy.html">PutBucketPolicy</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID of the Outposts bucket.</p>
            bucket: <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_bucket_policy_request.DeleteBucketPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_bucket_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_bucket_policy.async_delete_bucket_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_bucket_policy_request.DeleteBucketPolicyRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bucket_replication(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This operation deletes an Amazon S3 on Outposts bucket's replication configuration. To delete an S3 bucket's replication configuration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketReplication.html">DeleteBucketReplication</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Deletes the replication configuration from the specified S3 on Outposts bucket.</p> <p>To use this operation, you must have permissions to perform the <code>s3-outposts:PutReplicationConfiguration</code> action. The Outposts bucket owner has this permission by default and can grant it to others. For more information about permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsIAM.html">Setting up IAM with S3 on Outposts</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsBucketPolicy.html">Managing access to S3 on Outposts buckets</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>It can take a while to propagate <code>PUT</code> or <code>DELETE</code> requests for a replication configuration to all S3 on Outposts systems. Therefore, the replication configuration that's returned by a <code>GET</code> request soon after a <code>PUT</code> or <code>DELETE</code> request might return a more recent result than what's on the Outpost. If an Outpost is offline, the delay in updating the replication configuration on that Outpost can be significant.</p> </note> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketReplication.html#API_control_DeleteBucketReplication_Examples">Examples</a> section.</p> <p>For information about S3 replication on Outposts configuration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsReplication.html">Replicating objects for S3 on Outposts</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The following operations are related to <code>DeleteBucketReplication</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketReplication.html">PutBucketReplication</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html">GetBucketReplication</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket to delete the replication configuration for.</p>
            bucket: <p>Specifies the S3 on Outposts bucket to delete the replication configuration for.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_bucket_replication_request.DeleteBucketReplicationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_bucket_replication

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_bucket_replication.async_delete_bucket_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_bucket_replication_request.DeleteBucketReplicationRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bucket_tagging(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This action deletes an Amazon S3 on Outposts bucket's tags. To delete an S3 bucket tags, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html">DeleteBucketTagging</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Deletes the tags from the Outposts bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in <i>Amazon S3 User Guide</i>.</p> <p>To use this action, you must have permission to perform the <code>PutBucketTagging</code> action. By default, the bucket owner has this permission and can grant this permission to others. </p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketTagging.html#API_control_DeleteBucketTagging_Examples">Examples</a> section.</p> <p>The following actions are related to <code>DeleteBucketTagging</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketTagging.html">GetBucketTagging</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketTagging.html">PutBucketTagging</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket tag set to be removed.</p>
            bucket: <p>The bucket ARN that has the tag set to be removed.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_bucket_tagging_request.DeleteBucketTaggingRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_bucket_tagging

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_bucket_tagging.async_delete_bucket_tagging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_bucket_tagging_request.DeleteBucketTaggingRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_job_tagging(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        job_id: "capo_s3_control.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.delete_job_tagging_result.DeleteJobTaggingResult":
        """<p>Removes the entire tag set from the specified S3 Batch Operations job.</p> <dl> <dt>Permissions</dt> <dd> <p>To use the <code>DeleteJobTagging</code> operation, you must have permission to perform the <code>s3:DeleteJobTagging</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags">Controlling access and labeling jobs using tags</a> in the <i>Amazon S3 User Guide</i>.</p> </dd> </dl> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html">CreateJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html">GetJobTagging</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutJobTagging.html">PutJobTagging</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>
            job_id: <p>The ID for the S3 Batch Operations job whose tags you want to delete.</p>

        Raises:
            capo_s3_control.errors.internal_service_exception.InternalServiceException: <p></p>
            capo_s3_control.errors.not_found_exception.NotFoundException: <p></p>
            capo_s3_control.errors.too_many_requests_exception.TooManyRequestsException: <p></p>
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_job_tagging_request.DeleteJobTaggingRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.delete_job_tagging_result.DeleteJobTaggingResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_job_tagging

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_job_tagging.async_delete_job_tagging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_job_tagging_request.DeleteJobTaggingRequest = {
            "account_id": account_id,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_multi_region_access_point(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        client_token: "capo_s3_control.types.multi_region_access_point_client_token.MultiRegionAccessPointClientToken",
        details: "capo_s3_control.types.delete_multi_region_access_point_input.DeleteMultiRegionAccessPointInput",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.delete_multi_region_access_point_result.DeleteMultiRegionAccessPointResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Deletes a Multi-Region Access Point. This action does not delete the buckets associated with the Multi-Region Access Point, only the Multi-Region Access Point itself.</p> <p>This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html">Multi-Region Access Point restrictions and limitations</a> in the <i>Amazon S3 User Guide</i>.</p> <p>This request is asynchronous, meaning that you might receive a response before the command has completed. When this request provides a response, it provides a token that you can use to monitor the status of the request with <code>DescribeMultiRegionAccessPointOperation</code>.</p> <p>The following actions are related to <code>DeleteMultiRegionAccessPoint</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html">CreateMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html">DescribeMultiRegionAccessPointOperation</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html">GetMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html">ListMultiRegionAccessPoints</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>
            client_token: <p>An idempotency token used to identify the request and guarantee that requests are unique.</p>
            details: <p>A container element containing details about the Multi-Region Access Point.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_multi_region_access_point_request.DeleteMultiRegionAccessPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.delete_multi_region_access_point_result.DeleteMultiRegionAccessPointResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_multi_region_access_point

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_multi_region_access_point.async_delete_multi_region_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_multi_region_access_point_request.DeleteMultiRegionAccessPointRequest = {
            "account_id": account_id,
            "client_token": client_token,
            "details": details,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_public_access_block(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Removes the <code>PublicAccessBlock</code> configuration for an Amazon Web Services account. This operation might be restricted when the account is managed by organization-level Block Public Access policies. You’ll get an Access Denied (403) error when the account is managed by organization-level Block Public Access policies. Organization-level policies override account-level settings, preventing direct account-level modifications. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html"> Using Amazon S3 block public access</a>.</p> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetPublicAccessBlock.html">GetPublicAccessBlock</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutPublicAccessBlock.html">PutPublicAccessBlock</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the Amazon Web Services account whose <code>PublicAccessBlock</code> configuration you want to remove.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_public_access_block_request.DeletePublicAccessBlockRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_public_access_block

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_public_access_block.async_delete_public_access_block(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_public_access_block_request.DeletePublicAccessBlockRequest = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_storage_lens_configuration(
        self,
        config_id: "capo_s3_control.types.config_id.ConfigId",
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Deletes the Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html">Assessing your storage activity and usage with Amazon S3 Storage Lens </a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>To use this action, you must have permission to perform the <code>s3:DeleteStorageLensConfiguration</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html">Setting permissions to use Amazon S3 Storage Lens</a> in the <i>Amazon S3 User Guide</i>.</p> </note>

        Args:
            config_id: <p>The ID of the S3 Storage Lens configuration.</p>
            account_id: <p>The account ID of the requester.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_storage_lens_configuration_request.DeleteStorageLensConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_storage_lens_configuration

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_storage_lens_configuration.async_delete_storage_lens_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_storage_lens_configuration_request.DeleteStorageLensConfigurationRequest = {
            "config_id": config_id,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_storage_lens_configuration_tagging(
        self,
        config_id: "capo_s3_control.types.config_id.ConfigId",
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.delete_storage_lens_configuration_tagging_result.DeleteStorageLensConfigurationTaggingResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Deletes the Amazon S3 Storage Lens configuration tags. For more information about S3 Storage Lens, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html">Assessing your storage activity and usage with Amazon S3 Storage Lens </a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>To use this action, you must have permission to perform the <code>s3:DeleteStorageLensConfigurationTagging</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html">Setting permissions to use Amazon S3 Storage Lens</a> in the <i>Amazon S3 User Guide</i>.</p> </note>

        Args:
            config_id: <p>The ID of the S3 Storage Lens configuration.</p>
            account_id: <p>The account ID of the requester.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_storage_lens_configuration_tagging_request.DeleteStorageLensConfigurationTaggingRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.delete_storage_lens_configuration_tagging_result.DeleteStorageLensConfigurationTaggingResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_storage_lens_configuration_tagging

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_storage_lens_configuration_tagging.async_delete_storage_lens_configuration_tagging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_storage_lens_configuration_tagging_request.DeleteStorageLensConfigurationTaggingRequest = {
            "config_id": config_id,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_storage_lens_group(
        self,
        name: "capo_s3_control.types.storage_lens_group_name.StorageLensGroupName",
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p> Deletes an existing S3 Storage Lens group.</p> <p>To use this operation, you must have the permission to perform the <code>s3:DeleteStorageLensGroup</code> action. For more information about the required Storage Lens Groups permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_groups_permissions">Setting account permissions to use S3 Storage Lens groups</a>.</p> <p>For information about Storage Lens groups errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3LensErrorCodeList">List of Amazon S3 Storage Lens error codes</a>.</p>

        Args:
            name: <p> The name of the Storage Lens group that you're trying to delete. </p>
            account_id: <p> The Amazon Web Services account ID used to create the Storage Lens group that you're trying to delete. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.delete_storage_lens_group_request.DeleteStorageLensGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.delete_storage_lens_group

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.delete_storage_lens_group.async_delete_storage_lens_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.delete_storage_lens_group_request.DeleteStorageLensGroupRequest = {
            "name": name,
            "account_id": account_id,
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
        account_id: "capo_s3_control.types.account_id.AccountId",
        job_id: "capo_s3_control.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.describe_job_result.DescribeJobResult":
        """<p>Retrieves the configuration parameters and status for a Batch Operations job. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html">S3 Batch Operations</a> in the <i>Amazon S3 User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>To use the <code>DescribeJob</code> operation, you must have permission to perform the <code>s3:DescribeJob</code> action.</p> </dd> </dl> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html">CreateJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html">ListJobs</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html">UpdateJobPriority</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html">UpdateJobStatus</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>
            job_id: <p>The ID for the job whose information you want to retrieve.</p>

        Raises:
            capo_s3_control.errors.bad_request_exception.BadRequestException: <p></p>
            capo_s3_control.errors.internal_service_exception.InternalServiceException: <p></p>
            capo_s3_control.errors.not_found_exception.NotFoundException: <p></p>
            capo_s3_control.errors.too_many_requests_exception.TooManyRequestsException: <p></p>
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.describe_job_request.DescribeJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.describe_job_result.DescribeJobResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.describe_job

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.describe_job.async_describe_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.describe_job_request.DescribeJobRequest = {
            "account_id": account_id,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_multi_region_access_point_operation(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        request_token_arn: "capo_s3_control.types.async_request_token_arn.AsyncRequestTokenARN",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.describe_multi_region_access_point_operation_result.DescribeMultiRegionAccessPointOperationResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Retrieves the status of an asynchronous request to manage a Multi-Region Access Point. For more information about managing Multi-Region Access Points and how asynchronous requests work, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html">Using Multi-Region Access Points</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The following actions are related to <code>GetMultiRegionAccessPoint</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html">CreateMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html">DeleteMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html">GetMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html">ListMultiRegionAccessPoints</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>
            request_token_arn: <p>The request token associated with the request you want to know about. This request token is returned as part of the response when you make an asynchronous request. You provide this token to query about the status of the asynchronous action.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.describe_multi_region_access_point_operation_request.DescribeMultiRegionAccessPointOperationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.describe_multi_region_access_point_operation_result.DescribeMultiRegionAccessPointOperationResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.describe_multi_region_access_point_operation

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.describe_multi_region_access_point_operation.async_describe_multi_region_access_point_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.describe_multi_region_access_point_operation_request.DescribeMultiRegionAccessPointOperationRequest = {
            "account_id": account_id,
            "request_token_arn": request_token_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def dissociate_access_grants_identity_center(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p>Dissociates the Amazon Web Services IAM Identity Center instance from the S3 Access Grants instance. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:DissociateAccessGrantsIdentityCenter</code> permission to use this operation. </p> </dd> <dt>Additional Permissions</dt> <dd> <p>You must have the <code>sso:DeleteApplication</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.dissociate_access_grants_identity_center_request.DissociateAccessGrantsIdentityCenterRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.dissociate_access_grants_identity_center

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.dissociate_access_grants_identity_center.async_dissociate_access_grants_identity_center(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.dissociate_access_grants_identity_center_request.DissociateAccessGrantsIdentityCenterRequest = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_grant(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        access_grant_id: "capo_s3_control.types.access_grant_id.AccessGrantId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_grant_result.GetAccessGrantResult":
        """<p>Get the details of an access grant from your S3 Access Grants instance.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:GetAccessGrant</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            access_grant_id: <p>The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access grant.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_grant_request.GetAccessGrantRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_grant_result.GetAccessGrantResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_grant

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_grant.async_get_access_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_grant_request.GetAccessGrantRequest = {
            "account_id": account_id,
            "access_grant_id": access_grant_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_grants_instance(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_grants_instance_result.GetAccessGrantsInstanceResult":
        """<p>Retrieves the S3 Access Grants instance for a Region in your account. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:GetAccessGrantsInstance</code> permission to use this operation. </p> </dd> </dl> <note> <p> <code>GetAccessGrantsInstance</code> is not supported for cross-account access. You can only call the API from the account that owns the S3 Access Grants instance.</p> </note>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_grants_instance_request.GetAccessGrantsInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_grants_instance_result.GetAccessGrantsInstanceResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_grants_instance

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_grants_instance.async_get_access_grants_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_grants_instance_request.GetAccessGrantsInstanceRequest = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_grants_instance_for_prefix(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        s3_prefix: "capo_s3_control.types.s3_prefix.S3Prefix",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_grants_instance_for_prefix_result.GetAccessGrantsInstanceForPrefixResult":
        """<p>Retrieve the S3 Access Grants instance that contains a particular prefix. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:GetAccessGrantsInstanceForPrefix</code> permission for the caller account to use this operation. </p> </dd> <dt>Additional Permissions</dt> <dd> <p>The prefix owner account must grant you the following permissions to their S3 Access Grants instance: <code>s3:GetAccessGrantsInstanceForPrefix</code>. </p> </dd> </dl>

        Args:
            account_id: <p>The ID of the Amazon Web Services account that is making this request.</p>
            s3_prefix: <p>The S3 prefix of the access grants that you would like to retrieve.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_grants_instance_for_prefix_request.GetAccessGrantsInstanceForPrefixRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_grants_instance_for_prefix_result.GetAccessGrantsInstanceForPrefixResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_grants_instance_for_prefix

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_grants_instance_for_prefix.async_get_access_grants_instance_for_prefix(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_grants_instance_for_prefix_request.GetAccessGrantsInstanceForPrefixRequest = {
            "account_id": account_id,
            "s3_prefix": s3_prefix,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_grants_instance_resource_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_grants_instance_resource_policy_result.GetAccessGrantsInstanceResourcePolicyResult":
        """<p>Returns the resource policy of the S3 Access Grants instance. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:GetAccessGrantsInstanceResourcePolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_grants_instance_resource_policy_request.GetAccessGrantsInstanceResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_grants_instance_resource_policy_result.GetAccessGrantsInstanceResourcePolicyResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_grants_instance_resource_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_grants_instance_resource_policy.async_get_access_grants_instance_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_grants_instance_resource_policy_request.GetAccessGrantsInstanceResourcePolicyRequest = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_grants_location(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        access_grants_location_id: "capo_s3_control.types.access_grants_location_id.AccessGrantsLocationId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_grants_location_result.GetAccessGrantsLocationResult":
        """<p>Retrieves the details of a particular location registered in your S3 Access Grants instance. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:GetAccessGrantsLocation</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            access_grants_location_id: <p>The ID of the registered location that you are retrieving. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_grants_location_request.GetAccessGrantsLocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_grants_location_result.GetAccessGrantsLocationResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_grants_location

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_grants_location.async_get_access_grants_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_grants_location_request.GetAccessGrantsLocationRequest = {
            "account_id": account_id,
            "access_grants_location_id": access_grants_location_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_point(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.access_point_name.AccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_point_result.GetAccessPointResult":
        """<p>Returns configuration information about the specified access point.</p> <p></p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html#API_control_GetAccessPoint_Examples">Examples</a> section.</p> <p>The following actions are related to <code>GetAccessPoint</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html">CreateAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html">DeleteAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html">ListAccessPoints</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the account that owns the specified access point.</p>
            name: <p>The name of the access point whose configuration information you want to retrieve.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name></code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_point_request.GetAccessPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_point_result.GetAccessPointResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_point

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_point.async_get_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_point_request.GetAccessPointRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_point_configuration_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_point_configuration_for_object_lambda_result.GetAccessPointConfigurationForObjectLambdaResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns configuration for an Object Lambda Access Point.</p> <p>The following actions are related to <code>GetAccessPointConfigurationForObjectLambda</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointConfigurationForObjectLambda.html">PutAccessPointConfigurationForObjectLambda</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the account that owns the specified Object Lambda Access Point.</p>
            name: <p>The name of the Object Lambda Access Point you want to return the configuration for.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_point_configuration_for_object_lambda_request.GetAccessPointConfigurationForObjectLambdaRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_point_configuration_for_object_lambda_result.GetAccessPointConfigurationForObjectLambdaResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_configuration_for_object_lambda

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_configuration_for_object_lambda.async_get_access_point_configuration_for_object_lambda(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_point_configuration_for_object_lambda_request.GetAccessPointConfigurationForObjectLambdaRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_point_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_point_for_object_lambda_result.GetAccessPointForObjectLambdaResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns configuration information about the specified Object Lambda Access Point</p> <p>The following actions are related to <code>GetAccessPointForObjectLambda</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html">CreateAccessPointForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html">DeleteAccessPointForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html">ListAccessPointsForObjectLambda</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the account that owns the specified Object Lambda Access Point.</p>
            name: <p>The name of the Object Lambda Access Point.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_point_for_object_lambda_request.GetAccessPointForObjectLambdaRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_point_for_object_lambda_result.GetAccessPointForObjectLambdaResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_for_object_lambda

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_for_object_lambda.async_get_access_point_for_object_lambda(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_point_for_object_lambda_request.GetAccessPointForObjectLambdaRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_point_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.access_point_name.AccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_point_policy_result.GetAccessPointPolicyResult":
        """<p>Returns the access point policy associated with the specified access point.</p> <p>The following actions are related to <code>GetAccessPointPolicy</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html">PutAccessPointPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html">DeleteAccessPointPolicy</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the account that owns the specified access point.</p>
            name: <p>The name of the access point whose policy you want to retrieve.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name></code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_point_policy_request.GetAccessPointPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_point_policy_result.GetAccessPointPolicyResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_policy.async_get_access_point_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_point_policy_request.GetAccessPointPolicyRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_point_policy_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_point_policy_for_object_lambda_result.GetAccessPointPolicyForObjectLambdaResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns the resource policy for an Object Lambda Access Point.</p> <p>The following actions are related to <code>GetAccessPointPolicyForObjectLambda</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html">DeleteAccessPointPolicyForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicyForObjectLambda.html">PutAccessPointPolicyForObjectLambda</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the account that owns the specified Object Lambda Access Point.</p>
            name: <p>The name of the Object Lambda Access Point.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_point_policy_for_object_lambda_request.GetAccessPointPolicyForObjectLambdaRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_point_policy_for_object_lambda_result.GetAccessPointPolicyForObjectLambdaResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_policy_for_object_lambda

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_policy_for_object_lambda.async_get_access_point_policy_for_object_lambda(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_point_policy_for_object_lambda_request.GetAccessPointPolicyForObjectLambdaRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_point_policy_status(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.access_point_name.AccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_point_policy_status_result.GetAccessPointPolicyStatusResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Indicates whether the specified access point currently has a policy that allows public access. For more information about public access through access points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html">Managing Data Access with Amazon S3 access points</a> in the <i>Amazon S3 User Guide</i>.</p>

        Args:
            account_id: <p>The account ID for the account that owns the specified access point.</p>
            name: <p>The name of the access point whose policy status you want to retrieve.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_point_policy_status_request.GetAccessPointPolicyStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_point_policy_status_result.GetAccessPointPolicyStatusResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_policy_status

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_policy_status.async_get_access_point_policy_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_point_policy_status_request.GetAccessPointPolicyStatusRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_point_policy_status_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_access_point_policy_status_for_object_lambda_result.GetAccessPointPolicyStatusForObjectLambdaResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns the status of the resource policy associated with an Object Lambda Access Point.</p>

        Args:
            account_id: <p>The account ID for the account that owns the specified Object Lambda Access Point.</p>
            name: <p>The name of the Object Lambda Access Point.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_point_policy_status_for_object_lambda_request.GetAccessPointPolicyStatusForObjectLambdaRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_point_policy_status_for_object_lambda_result.GetAccessPointPolicyStatusForObjectLambdaResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_policy_status_for_object_lambda

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_policy_status_for_object_lambda.async_get_access_point_policy_status_for_object_lambda(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_point_policy_status_for_object_lambda_request.GetAccessPointPolicyStatusForObjectLambdaRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_point_scope(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.access_point_name.AccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> (
        "capo_s3_control.types.get_access_point_scope_result.GetAccessPointScopeResult"
    ):
        """<p> Returns the access point scope for a directory bucket.</p> <p>To use this operation, you must have the permission to perform the <code>s3express:GetAccessPointScope</code> action.</p> <p>For information about REST API errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#RESTErrorResponses">REST error responses</a>.</p>

        Args:
            account_id: <p> The Amazon Web Services account ID that owns the access point with the scope that you want to retrieve. </p>
            name: <p>The name of the access point with the scope you want to retrieve.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_access_point_scope_request.GetAccessPointScopeRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_access_point_scope_result.GetAccessPointScopeResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_scope

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_access_point_scope.async_get_access_point_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_access_point_scope_request.GetAccessPointScopeRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bucket(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_bucket_result.GetBucketResult":
        """<p>Gets an Amazon S3 on Outposts bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html"> Using Amazon S3 on Outposts</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you are using an identity other than the root user of the Amazon Web Services account that owns the Outposts bucket, the calling identity must have the <code>s3-outposts:GetBucket</code> permissions on the specified Outposts bucket and belong to the Outposts bucket owner's account in order to use this action. Only users from Outposts bucket owner account with the right permissions can perform actions on an Outposts bucket. </p> <p>If you don't have <code>s3-outposts:GetBucket</code> permissions or you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a <code>403 Access Denied</code> error.</p> <p>The following actions are related to <code>GetBucket</code> for Amazon S3 on Outposts:</p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html#API_control_GetBucket_Examples">Examples</a> section.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html">PutObject</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html">CreateBucket</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucket.html">DeleteBucket</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket.</p>
            bucket: <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_bucket_request.GetBucketRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_bucket_result.GetBucketResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_bucket

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_bucket.async_get_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_bucket_request.GetBucketRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bucket_lifecycle_configuration(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_bucket_lifecycle_configuration_result.GetBucketLifecycleConfigurationResult":
        """<note> <p>This action gets an Amazon S3 on Outposts bucket's lifecycle configuration. To get an S3 bucket's lifecycle configuration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html">GetBucketLifecycleConfiguration</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Returns the lifecycle configuration information set on the Outposts bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> and for information about lifecycle configuration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html"> Object Lifecycle Management</a> in <i>Amazon S3 User Guide</i>.</p> <p>To use this action, you must have permission to perform the <code>s3-outposts:GetLifecycleConfiguration</code> action. The Outposts bucket owner has this permission, by default. The bucket owner can grant this permission to others. For more information about permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources">Permissions Related to Bucket Subresource Operations</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html">Managing Access Permissions to Your Amazon S3 Resources</a>.</p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html#API_control_GetBucketLifecycleConfiguration_Examples">Examples</a> section.</p> <p> <code>GetBucketLifecycleConfiguration</code> has the following special error:</p> <ul> <li> <p>Error code: <code>NoSuchLifecycleConfiguration</code> </p> <ul> <li> <p>Description: The lifecycle configuration does not exist.</p> </li> <li> <p>HTTP Status Code: 404 Not Found</p> </li> <li> <p>SOAP Fault Code Prefix: Client</p> </li> </ul> </li> </ul> <p>The following actions are related to <code>GetBucketLifecycleConfiguration</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html">PutBucketLifecycleConfiguration</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketLifecycleConfiguration.html">DeleteBucketLifecycleConfiguration</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket.</p>
            bucket: <p>The Amazon Resource Name (ARN) of the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_bucket_lifecycle_configuration_request.GetBucketLifecycleConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_bucket_lifecycle_configuration_result.GetBucketLifecycleConfigurationResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_bucket_lifecycle_configuration

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_bucket_lifecycle_configuration.async_get_bucket_lifecycle_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_bucket_lifecycle_configuration_request.GetBucketLifecycleConfigurationRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bucket_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_bucket_policy_result.GetBucketPolicyResult":
        """<note> <p>This action gets a bucket policy for an Amazon S3 on Outposts bucket. To get a policy for an S3 bucket, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html">GetBucketPolicy</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Returns the policy of a specified Outposts bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you are using an identity other than the root user of the Amazon Web Services account that owns the bucket, the calling identity must have the <code>GetBucketPolicy</code> permissions on the specified bucket and belong to the bucket owner's account in order to use this action.</p> <p>Only users from Outposts bucket owner account with the right permissions can perform actions on an Outposts bucket. If you don't have <code>s3-outposts:GetBucketPolicy</code> permissions or you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a <code>403 Access Denied</code> error.</p> <important> <p>As a security precaution, the root user of the Amazon Web Services account that owns a bucket can always use this action, even if the policy explicitly denies the root user the ability to perform this action.</p> </important> <p>For more information about bucket policies, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html">Using Bucket Policies and User Policies</a>.</p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html#API_control_GetBucketPolicy_Examples">Examples</a> section.</p> <p>The following actions are related to <code>GetBucketPolicy</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html">GetObject</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketPolicy.html">PutBucketPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketPolicy.html">DeleteBucketPolicy</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket.</p>
            bucket: <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_bucket_policy_request.GetBucketPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_bucket_policy_result.GetBucketPolicyResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_bucket_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_bucket_policy.async_get_bucket_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_bucket_policy_request.GetBucketPolicyRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bucket_replication(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> (
        "capo_s3_control.types.get_bucket_replication_result.GetBucketReplicationResult"
    ):
        """<note> <p>This operation gets an Amazon S3 on Outposts bucket's replication configuration. To get an S3 bucket's replication configuration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html">GetBucketReplication</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Returns the replication configuration of an S3 on Outposts bucket. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in the <i>Amazon S3 User Guide</i>. For information about S3 replication on Outposts configuration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsReplication.html">Replicating objects for S3 on Outposts</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>It can take a while to propagate <code>PUT</code> or <code>DELETE</code> requests for a replication configuration to all S3 on Outposts systems. Therefore, the replication configuration that's returned by a <code>GET</code> request soon after a <code>PUT</code> or <code>DELETE</code> request might return a more recent result than what's on the Outpost. If an Outpost is offline, the delay in updating the replication configuration on that Outpost can be significant.</p> </note> <p>This action requires permissions for the <code>s3-outposts:GetReplicationConfiguration</code> action. The Outposts bucket owner has this permission by default and can grant it to others. For more information about permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsIAM.html">Setting up IAM with S3 on Outposts</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsBucketPolicy.html">Managing access to S3 on Outposts bucket</a> in the <i>Amazon S3 User Guide</i>.</p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html#API_control_GetBucketReplication_Examples">Examples</a> section.</p> <p>If you include the <code>Filter</code> element in a replication configuration, you must also include the <code>DeleteMarkerReplication</code>, <code>Status</code>, and <code>Priority</code> elements. The response also returns those elements.</p> <p>For information about S3 on Outposts replication failure reasons, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/outposts-replication-eventbridge.html#outposts-replication-failure-codes">Replication failure reasons</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The following operations are related to <code>GetBucketReplication</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketReplication.html">PutBucketReplication</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketReplication.html">DeleteBucketReplication</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket.</p>
            bucket: <p>Specifies the bucket to get the replication information for.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_bucket_replication_request.GetBucketReplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_bucket_replication_result.GetBucketReplicationResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_bucket_replication

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_bucket_replication.async_get_bucket_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_bucket_replication_request.GetBucketReplicationRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bucket_tagging(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_bucket_tagging_result.GetBucketTaggingResult":
        """<note> <p>This action gets an Amazon S3 on Outposts bucket's tags. To get an S3 bucket tags, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html">GetBucketTagging</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Returns the tag set associated with the Outposts bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in the <i>Amazon S3 User Guide</i>.</p> <p>To use this action, you must have permission to perform the <code>GetBucketTagging</code> action. By default, the bucket owner has this permission and can grant this permission to others.</p> <p> <code>GetBucketTagging</code> has the following special error:</p> <ul> <li> <p>Error code: <code>NoSuchTagSetError</code> </p> <ul> <li> <p>Description: There is no tag set associated with the bucket.</p> </li> </ul> </li> </ul> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketTagging.html#API_control_GetBucketTagging_Examples">Examples</a> section.</p> <p>The following actions are related to <code>GetBucketTagging</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketTagging.html">PutBucketTagging</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketTagging.html">DeleteBucketTagging</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket.</p>
            bucket: <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_bucket_tagging_request.GetBucketTaggingRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_bucket_tagging_result.GetBucketTaggingResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_bucket_tagging

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_bucket_tagging.async_get_bucket_tagging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_bucket_tagging_request.GetBucketTaggingRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bucket_versioning(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_bucket_versioning_result.GetBucketVersioningResult":
        """<note> <p>This operation returns the versioning state for S3 on Outposts buckets only. To return the versioning state for an S3 bucket, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html">GetBucketVersioning</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Returns the versioning state for an S3 on Outposts bucket. With S3 Versioning, you can save multiple distinct copies of your objects and recover from unintended user actions and application failures.</p> <p>If you've never set versioning on your bucket, it has no versioning state. In that case, the <code>GetBucketVersioning</code> request does not return a versioning state value.</p> <p>For more information about versioning, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html">Versioning</a> in the <i>Amazon S3 User Guide</i>.</p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketVersioning.html#API_control_GetBucketVersioning_Examples">Examples</a> section.</p> <p>The following operations are related to <code>GetBucketVersioning</code> for S3 on Outposts.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketVersioning.html">PutBucketVersioning</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html">PutBucketLifecycleConfiguration</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html">GetBucketLifecycleConfiguration</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 on Outposts bucket.</p>
            bucket: <p>The S3 on Outposts bucket to return the versioning state for.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_bucket_versioning_request.GetBucketVersioningRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_bucket_versioning_result.GetBucketVersioningResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_bucket_versioning

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_bucket_versioning.async_get_bucket_versioning(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_bucket_versioning_request.GetBucketVersioningRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_access(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        target: "capo_s3_control.types.s3_prefix.S3Prefix",
        permission: "capo_s3_control.types.permission.Permission",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        duration_seconds: Optional[
            "capo_s3_control.types.duration_seconds.DurationSeconds"
        ] = None,
        privilege: Optional["capo_s3_control.types.privilege.Privilege"] = None,
        target_type: Optional[
            "capo_s3_control.types.s3_prefix_type.S3PrefixType"
        ] = None,
        audit_context: Optional[
            "capo_s3_control.types.audit_context.AuditContext"
        ] = None,
    ) -> "capo_s3_control.types.get_data_access_result.GetDataAccessResult":
        """<p>Returns a temporary access credential from S3 Access Grants to the grantee or client application. The <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_Credentials.html">temporary credential</a> is an Amazon Web Services STS token that grants them access to the S3 data. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:GetDataAccess</code> permission to use this operation. </p> </dd> <dt>Additional Permissions</dt> <dd> <p>The IAM role that S3 Access Grants assumes must have the following permissions specified in the trust policy when registering the location: <code>sts:AssumeRole</code>, for directory users or groups <code>sts:SetContext</code>, and for IAM users or roles <code>sts:SetSourceIdentity</code>. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            target: <p>The S3 URI path of the data to which you are requesting temporary access credentials. If the requesting account has an access grant for this data, S3 Access Grants vends temporary access credentials in the response.</p>
            permission: <p>The type of permission granted to your S3 data, which can be set to one of the following values:</p> <ul> <li> <p> <code>READ</code> – Grant read-only access to the S3 data.</p> </li> <li> <p> <code>WRITE</code> – Grant write-only access to the S3 data.</p> </li> <li> <p> <code>READWRITE</code> – Grant both read and write access to the S3 data.</p> </li> </ul>
            duration_seconds: <p>The session duration, in seconds, of the temporary access credential that S3 Access Grants vends to the grantee or client application. The default value is 1 hour, but the grantee can specify a range from 900 seconds (15 minutes) up to 43200 seconds (12 hours). If the grantee requests a value higher than this maximum, the operation fails. </p>
            privilege: <p>The scope of the temporary access credential that S3 Access Grants vends to the grantee or client application. </p> <ul> <li> <p> <code>Default</code> – The scope of the returned temporary access token is the scope of the grant that is closest to the target scope.</p> </li> <li> <p> <code>Minimal</code> – The scope of the returned temporary access token is the same as the requested target scope as long as the requested scope is the same as or a subset of the grant scope. </p> </li> </ul>
            target_type: <p>The type of <code>Target</code>. The only possible value is <code>Object</code>. Pass this value if the target data that you would like to access is a path to an object. Do not pass this value if the target data is a bucket or a bucket and a prefix. </p>
            audit_context: <p>The context to identify the job or query associated with the credential request. This information will be displayed in CloudTrail log in your account.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_data_access_request.GetDataAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_data_access_result.GetDataAccessResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_data_access

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_data_access.async_get_data_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_data_access_request.GetDataAccessRequest = {
            "account_id": account_id,
            "target": target,
            "permission": permission,
        }
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if privilege is not None:
            input_["privilege"] = privilege
        if target_type is not None:
            input_["target_type"] = target_type
        if audit_context is not None:
            input_["audit_context"] = audit_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_job_tagging(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        job_id: "capo_s3_control.types.job_id.JobId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_job_tagging_result.GetJobTaggingResult":
        """<p>Returns the tags on an S3 Batch Operations job. </p> <dl> <dt>Permissions</dt> <dd> <p>To use the <code>GetJobTagging</code> operation, you must have permission to perform the <code>s3:GetJobTagging</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags">Controlling access and labeling jobs using tags</a> in the <i>Amazon S3 User Guide</i>.</p> </dd> </dl> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html">CreateJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutJobTagging.html">PutJobTagging</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html">DeleteJobTagging</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>
            job_id: <p>The ID for the S3 Batch Operations job whose tags you want to retrieve.</p>

        Raises:
            capo_s3_control.errors.internal_service_exception.InternalServiceException: <p></p>
            capo_s3_control.errors.not_found_exception.NotFoundException: <p></p>
            capo_s3_control.errors.too_many_requests_exception.TooManyRequestsException: <p></p>
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_job_tagging_request.GetJobTaggingRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_job_tagging_result.GetJobTaggingResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_job_tagging

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_job_tagging.async_get_job_tagging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_job_tagging_request.GetJobTaggingRequest = {
            "account_id": account_id,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_multi_region_access_point(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.multi_region_access_point_name.MultiRegionAccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_multi_region_access_point_result.GetMultiRegionAccessPointResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns configuration information about the specified Multi-Region Access Point.</p> <p>This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html">Multi-Region Access Point restrictions and limitations</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The following actions are related to <code>GetMultiRegionAccessPoint</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html">CreateMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html">DeleteMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html">DescribeMultiRegionAccessPointOperation</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html">ListMultiRegionAccessPoints</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>
            name: <p>The name of the Multi-Region Access Point whose configuration information you want to receive. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming">Rules for naming Amazon S3 Multi-Region Access Points</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_multi_region_access_point_request.GetMultiRegionAccessPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_multi_region_access_point_result.GetMultiRegionAccessPointResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_multi_region_access_point

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_multi_region_access_point.async_get_multi_region_access_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_multi_region_access_point_request.GetMultiRegionAccessPointRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_multi_region_access_point_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.multi_region_access_point_name.MultiRegionAccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_multi_region_access_point_policy_result.GetMultiRegionAccessPointPolicyResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns the access control policy of the specified Multi-Region Access Point.</p> <p>This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html">Multi-Region Access Point restrictions and limitations</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The following actions are related to <code>GetMultiRegionAccessPointPolicy</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html">GetMultiRegionAccessPointPolicyStatus</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html">PutMultiRegionAccessPointPolicy</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>
            name: <p>Specifies the Multi-Region Access Point. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming">Rules for naming Amazon S3 Multi-Region Access Points</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_multi_region_access_point_policy_request.GetMultiRegionAccessPointPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_multi_region_access_point_policy_result.GetMultiRegionAccessPointPolicyResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_multi_region_access_point_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_multi_region_access_point_policy.async_get_multi_region_access_point_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_multi_region_access_point_policy_request.GetMultiRegionAccessPointPolicyRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_multi_region_access_point_policy_status(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.multi_region_access_point_name.MultiRegionAccessPointName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_multi_region_access_point_policy_status_result.GetMultiRegionAccessPointPolicyStatusResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Indicates whether the specified Multi-Region Access Point has an access control policy that allows public access.</p> <p>This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html">Multi-Region Access Point restrictions and limitations</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The following actions are related to <code>GetMultiRegionAccessPointPolicyStatus</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html">GetMultiRegionAccessPointPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html">PutMultiRegionAccessPointPolicy</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>
            name: <p>Specifies the Multi-Region Access Point. The name of the Multi-Region Access Point is different from the alias. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming">Rules for naming Amazon S3 Multi-Region Access Points</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_multi_region_access_point_policy_status_request.GetMultiRegionAccessPointPolicyStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_multi_region_access_point_policy_status_result.GetMultiRegionAccessPointPolicyStatusResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_multi_region_access_point_policy_status

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_multi_region_access_point_policy_status.async_get_multi_region_access_point_policy_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_multi_region_access_point_policy_status_request.GetMultiRegionAccessPointPolicyStatusRequest = {
            "account_id": account_id,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_multi_region_access_point_routes(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        mrap: "capo_s3_control.types.multi_region_access_point_id.MultiRegionAccessPointId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_multi_region_access_point_routes_result.GetMultiRegionAccessPointRoutesResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns the routing configuration for a Multi-Region Access Point, indicating which Regions are active or passive.</p> <p>To obtain routing control changes and failover requests, use the Amazon S3 failover control infrastructure endpoints in these five Amazon Web Services Regions:</p> <ul> <li> <p> <code>us-east-1</code> </p> </li> <li> <p> <code>us-west-2</code> </p> </li> <li> <p> <code>ap-southeast-2</code> </p> </li> <li> <p> <code>ap-northeast-1</code> </p> </li> <li> <p> <code>eu-west-1</code> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>
            mrap: <p>The Multi-Region Access Point ARN.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_multi_region_access_point_routes_request.GetMultiRegionAccessPointRoutesRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_multi_region_access_point_routes_result.GetMultiRegionAccessPointRoutesResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_multi_region_access_point_routes

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_multi_region_access_point_routes.async_get_multi_region_access_point_routes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_multi_region_access_point_routes_request.GetMultiRegionAccessPointRoutesRequest = {
            "account_id": account_id,
            "mrap": mrap,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_public_access_block(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_public_access_block_output.GetPublicAccessBlockOutput":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Retrieves the <code>PublicAccessBlock</code> configuration for an Amazon Web Services account. This operation returns the effective account-level configuration, which may inherit from organization-level policies. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html"> Using Amazon S3 block public access</a>.</p> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeletePublicAccessBlock.html">DeletePublicAccessBlock</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutPublicAccessBlock.html">PutPublicAccessBlock</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the Amazon Web Services account whose <code>PublicAccessBlock</code> configuration you want to retrieve.</p>

        Raises:
            capo_s3_control.errors.no_such_public_access_block_configuration.NoSuchPublicAccessBlockConfiguration: <p>Amazon S3 throws this exception if you make a <code>GetPublicAccessBlock</code> request against an account that doesn't have a <code>PublicAccessBlockConfiguration</code> set.</p>
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_public_access_block_request.GetPublicAccessBlockRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_public_access_block_output.GetPublicAccessBlockOutput"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_public_access_block

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_public_access_block.async_get_public_access_block(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_public_access_block_request.GetPublicAccessBlockRequest = {
            "account_id": account_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_storage_lens_configuration(
        self,
        config_id: "capo_s3_control.types.config_id.ConfigId",
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_storage_lens_configuration_result.GetStorageLensConfigurationResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Gets the Amazon S3 Storage Lens configuration. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html">Assessing your storage activity and usage with Amazon S3 Storage Lens </a> in the <i>Amazon S3 User Guide</i>. For a complete list of S3 Storage Lens metrics, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html">S3 Storage Lens metrics glossary</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>To use this action, you must have permission to perform the <code>s3:GetStorageLensConfiguration</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html">Setting permissions to use Amazon S3 Storage Lens</a> in the <i>Amazon S3 User Guide</i>.</p> </note>

        Args:
            config_id: <p>The ID of the Amazon S3 Storage Lens configuration.</p>
            account_id: <p>The account ID of the requester.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_storage_lens_configuration_request.GetStorageLensConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_storage_lens_configuration_result.GetStorageLensConfigurationResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_storage_lens_configuration

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_storage_lens_configuration.async_get_storage_lens_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_storage_lens_configuration_request.GetStorageLensConfigurationRequest = {
            "config_id": config_id,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_storage_lens_configuration_tagging(
        self,
        config_id: "capo_s3_control.types.config_id.ConfigId",
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.get_storage_lens_configuration_tagging_result.GetStorageLensConfigurationTaggingResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Gets the tags of Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html">Assessing your storage activity and usage with Amazon S3 Storage Lens </a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>To use this action, you must have permission to perform the <code>s3:GetStorageLensConfigurationTagging</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html">Setting permissions to use Amazon S3 Storage Lens</a> in the <i>Amazon S3 User Guide</i>.</p> </note>

        Args:
            config_id: <p>The ID of the Amazon S3 Storage Lens configuration.</p>
            account_id: <p>The account ID of the requester.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_storage_lens_configuration_tagging_request.GetStorageLensConfigurationTaggingRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_storage_lens_configuration_tagging_result.GetStorageLensConfigurationTaggingResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_storage_lens_configuration_tagging

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_storage_lens_configuration_tagging.async_get_storage_lens_configuration_tagging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_storage_lens_configuration_tagging_request.GetStorageLensConfigurationTaggingRequest = {
            "config_id": config_id,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_storage_lens_group(
        self,
        name: "capo_s3_control.types.storage_lens_group_name.StorageLensGroupName",
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> (
        "capo_s3_control.types.get_storage_lens_group_result.GetStorageLensGroupResult"
    ):
        """<p> Retrieves the Storage Lens group configuration details.</p> <p>To use this operation, you must have the permission to perform the <code>s3:GetStorageLensGroup</code> action. For more information about the required Storage Lens Groups permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_groups_permissions">Setting account permissions to use S3 Storage Lens groups</a>.</p> <p>For information about Storage Lens groups errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3LensErrorCodeList">List of Amazon S3 Storage Lens error codes</a>.</p>

        Args:
            name: <p> The name of the Storage Lens group that you're trying to retrieve the configuration details for. </p>
            account_id: <p> The Amazon Web Services account ID associated with the Storage Lens group that you're trying to retrieve the details for. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.get_storage_lens_group_request.GetStorageLensGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.get_storage_lens_group_result.GetStorageLensGroupResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.get_storage_lens_group

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.get_storage_lens_group.async_get_storage_lens_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.get_storage_lens_group_request.GetStorageLensGroupRequest = {
            "name": name,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_access_grants(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
        grantee_type: Optional["capo_s3_control.types.grantee_type.GranteeType"] = None,
        grantee_identifier: Optional[
            "capo_s3_control.types.grantee_identifier.GranteeIdentifier"
        ] = None,
        permission: Optional["capo_s3_control.types.permission.Permission"] = None,
        grant_scope: Optional["capo_s3_control.types.s3_prefix.S3Prefix"] = None,
        application_arn: Optional[
            "capo_s3_control.types.identity_center_application_arn.IdentityCenterApplicationArn"
        ] = None,
    ) -> "capo_s3_control.types.list_access_grants_result.ListAccessGrantsResult":
        """<p>Returns the list of access grants in your S3 Access Grants instance.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:ListAccessGrants</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            next_token: <p>A pagination token to request the next page of results. Pass this value into a subsequent <code>List Access Grants</code> request in order to retrieve the next page of results.</p>
            max_results: <p>The maximum number of access grants that you would like returned in the <code>List Access Grants</code> response. If the results include the pagination token <code>NextToken</code>, make another call using the <code>NextToken</code> to determine if there are more results.</p>
            grantee_type: <p>The type of the grantee to which access has been granted. It can be one of the following values:</p> <ul> <li> <p> <code>IAM</code> - An IAM user or role.</p> </li> <li> <p> <code>DIRECTORY_USER</code> - Your corporate directory user. You can use this option if you have added your corporate identity directory to IAM Identity Center and associated the IAM Identity Center instance with your S3 Access Grants instance.</p> </li> <li> <p> <code>DIRECTORY_GROUP</code> - Your corporate directory group. You can use this option if you have added your corporate identity directory to IAM Identity Center and associated the IAM Identity Center instance with your S3 Access Grants instance.</p> </li> </ul>
            grantee_identifier: <p>The unique identifer of the <code>Grantee</code>. If the grantee type is <code>IAM</code>, the identifier is the IAM Amazon Resource Name (ARN) of the user or role. If the grantee type is a directory user or group, the identifier is 128-bit universally unique identifier (UUID) in the format <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>. You can obtain this UUID from your Amazon Web Services IAM Identity Center instance.</p>
            permission: <p>The type of permission granted to your S3 data, which can be set to one of the following values:</p> <ul> <li> <p> <code>READ</code> – Grant read-only access to the S3 data.</p> </li> <li> <p> <code>WRITE</code> – Grant write-only access to the S3 data.</p> </li> <li> <p> <code>READWRITE</code> – Grant both read and write access to the S3 data.</p> </li> </ul>
            grant_scope: <p>The S3 path of the data to which you are granting access. It is the result of appending the <code>Subprefix</code> to the location scope.</p>
            application_arn: <p>The Amazon Resource Name (ARN) of an Amazon Web Services IAM Identity Center application associated with your Identity Center instance. If the grant includes an application ARN, the grantee can only access the S3 data through this application. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_access_grants_request.ListAccessGrantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_access_grants_result.ListAccessGrantsResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_access_grants

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_access_grants.async_list_access_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_access_grants_request.ListAccessGrantsRequest = {
            "account_id": account_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if grantee_type is not None:
            input_["grantee_type"] = grantee_type
        if grantee_identifier is not None:
            input_["grantee_identifier"] = grantee_identifier
        if permission is not None:
            input_["permission"] = permission
        if grant_scope is not None:
            input_["grant_scope"] = grant_scope
        if application_arn is not None:
            input_["application_arn"] = application_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_access_grants(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
        grantee_type: Optional["capo_s3_control.types.grantee_type.GranteeType"] = None,
        grantee_identifier: Optional[
            "capo_s3_control.types.grantee_identifier.GranteeIdentifier"
        ] = None,
        permission: Optional["capo_s3_control.types.permission.Permission"] = None,
        grant_scope: Optional["capo_s3_control.types.s3_prefix.S3Prefix"] = None,
        application_arn: Optional[
            "capo_s3_control.types.identity_center_application_arn.IdentityCenterApplicationArn"
        ] = None,
    ) -> "AsyncIterator[capo_s3_control.types.list_access_grants_result.ListAccessGrantsResult]":
        _token = next_token
        while True:
            _response = await self.list_access_grants(
                account_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                grantee_type=grantee_type,
                grantee_identifier=grantee_identifier,
                permission=permission,
                grant_scope=grant_scope,
                application_arn=application_arn,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_access_grants_instances(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
    ) -> "capo_s3_control.types.list_access_grants_instances_result.ListAccessGrantsInstancesResult":
        """<p>Returns a list of S3 Access Grants instances. An S3 Access Grants instance serves as a logical grouping for your individual access grants. You can only have one S3 Access Grants instance per Region per account.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:ListAccessGrantsInstances</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            next_token: <p>A pagination token to request the next page of results. Pass this value into a subsequent <code>List Access Grants Instances</code> request in order to retrieve the next page of results.</p>
            max_results: <p>The maximum number of access grants that you would like returned in the <code>List Access Grants</code> response. If the results include the pagination token <code>NextToken</code>, make another call using the <code>NextToken</code> to determine if there are more results.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_access_grants_instances_request.ListAccessGrantsInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_access_grants_instances_result.ListAccessGrantsInstancesResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_access_grants_instances

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_access_grants_instances.async_list_access_grants_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_access_grants_instances_request.ListAccessGrantsInstancesRequest = {
            "account_id": account_id
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

    async def iter_list_access_grants_instances(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_s3_control.types.list_access_grants_instances_result.ListAccessGrantsInstancesResult]":
        _token = next_token
        while True:
            _response = await self.list_access_grants_instances(
                account_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_access_grants_locations(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
        location_scope: Optional["capo_s3_control.types.s3_prefix.S3Prefix"] = None,
    ) -> "capo_s3_control.types.list_access_grants_locations_result.ListAccessGrantsLocationsResult":
        """<p>Returns a list of the locations registered in your S3 Access Grants instance.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:ListAccessGrantsLocations</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            next_token: <p>A pagination token to request the next page of results. Pass this value into a subsequent <code>List Access Grants Locations</code> request in order to retrieve the next page of results.</p>
            max_results: <p>The maximum number of access grants that you would like returned in the <code>List Access Grants</code> response. If the results include the pagination token <code>NextToken</code>, make another call using the <code>NextToken</code> to determine if there are more results.</p>
            location_scope: <p>The S3 path to the location that you are registering. The location scope can be the default S3 location <code>s3://</code>, the S3 path to a bucket <code>s3://<bucket></code>, or the S3 path to a bucket and prefix <code>s3://<bucket>/<prefix></code>. A prefix in S3 is a string of characters at the beginning of an object key name used to organize the objects that you store in your S3 buckets. For example, object key names that start with the <code>engineering/</code> prefix or object key names that start with the <code>marketing/campaigns/</code> prefix.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_access_grants_locations_request.ListAccessGrantsLocationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_access_grants_locations_result.ListAccessGrantsLocationsResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_access_grants_locations

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_access_grants_locations.async_list_access_grants_locations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_access_grants_locations_request.ListAccessGrantsLocationsRequest = {
            "account_id": account_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if location_scope is not None:
            input_["location_scope"] = location_scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_access_grants_locations(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
        location_scope: Optional["capo_s3_control.types.s3_prefix.S3Prefix"] = None,
    ) -> "AsyncIterator[capo_s3_control.types.list_access_grants_locations_result.ListAccessGrantsLocationsResult]":
        _token = next_token
        while True:
            _response = await self.list_access_grants_locations(
                account_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                location_scope=location_scope,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_access_points(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        bucket: Optional["capo_s3_control.types.bucket_name.BucketName"] = None,
        next_token: Optional[
            "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
        data_source_id: Optional[
            "capo_s3_control.types.data_source_id.DataSourceId"
        ] = None,
        data_source_type: Optional[
            "capo_s3_control.types.data_source_type.DataSourceType"
        ] = None,
    ) -> "capo_s3_control.types.list_access_points_result.ListAccessPointsResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns a list of the access points. You can retrieve up to 1,000 access points per call. If the call returns more than 1,000 access points (or the number specified in <code>maxResults</code>, whichever is less), the response will include a continuation token that you can use to list the additional access points.</p> <p>Returns only access points attached to S3 buckets by default. To return all access points specify <code>DataSourceType</code> as <code>ALL</code>.</p> <p></p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html#API_control_GetAccessPoint_Examples">Examples</a> section.</p> <p>The following actions are related to <code>ListAccessPoints</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html">CreateAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html">DeleteAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html">GetAccessPoint</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the account that owns the specified access points.</p>
            bucket: <p>The name of the bucket whose associated access points you want to list.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
            next_token: <p>A continuation token. If a previous call to <code>ListAccessPoints</code> returned a continuation token in the <code>NextToken</code> field, then providing that value here causes Amazon S3 to retrieve the next page of results.</p>
            max_results: <p>The maximum number of access points that you want to include in the list. If the specified bucket has more than this number of access points, then the response will include a continuation token in the <code>NextToken</code> field that you can use to retrieve the next page of access points.</p>
            data_source_id: <p>The unique identifier for the data source of the access point.</p>
            data_source_type: <p>The type of the data source that the access point is attached to. Returns only access points attached to S3 buckets by default. To return all access points specify <code>DataSourceType</code> as <code>ALL</code>.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_access_points_request.ListAccessPointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_access_points_result.ListAccessPointsResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_access_points

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_access_points.async_list_access_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_access_points_request.ListAccessPointsRequest = {
            "account_id": account_id
        }
        if bucket is not None:
            input_["bucket"] = bucket
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id
        if data_source_type is not None:
            input_["data_source_type"] = data_source_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_access_points(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        bucket: Optional["capo_s3_control.types.bucket_name.BucketName"] = None,
        next_token: Optional[
            "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
        data_source_id: Optional[
            "capo_s3_control.types.data_source_id.DataSourceId"
        ] = None,
        data_source_type: Optional[
            "capo_s3_control.types.data_source_type.DataSourceType"
        ] = None,
    ) -> "AsyncIterator[capo_s3_control.types.list_access_points_result.ListAccessPointsResult]":
        _token = next_token
        while True:
            _response = await self.list_access_points(
                account_id,
                config_overrides=config_overrides,
                bucket=bucket,
                next_token=_token,
                max_results=max_results,
                data_source_id=data_source_id,
                data_source_type=data_source_type,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_access_points_for_directory_buckets(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        directory_bucket: Optional[
            "capo_s3_control.types.bucket_name.BucketName"
        ] = None,
        next_token: Optional[
            "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
    ) -> "capo_s3_control.types.list_access_points_for_directory_buckets_result.ListAccessPointsForDirectoryBucketsResult":
        """<p>Returns a list of the access points that are owned by the Amazon Web Services account and that are associated with the specified directory bucket.</p> <p>To list access points for general purpose buckets, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html">ListAccesspoints</a>.</p> <p>To use this operation, you must have the permission to perform the <code>s3express:ListAccessPointsForDirectoryBuckets</code> action.</p> <p>For information about REST API errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#RESTErrorResponses">REST error responses</a>.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID that owns the access points.</p>
            directory_bucket: <p>The name of the directory bucket associated with the access points you want to list.</p>
            next_token: <p> If <code>NextToken</code> is returned, there are more access points available than requested in the <code>maxResults</code> value. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>
            max_results: <p>The maximum number of access points that you would like returned in the <code>ListAccessPointsForDirectoryBuckets</code> response. If the directory bucket is associated with more than this number of access points, the results include the pagination token <code>NextToken</code>. Make another call using the <code>NextToken</code> to retrieve more results.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_access_points_for_directory_buckets_request.ListAccessPointsForDirectoryBucketsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_access_points_for_directory_buckets_result.ListAccessPointsForDirectoryBucketsResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_access_points_for_directory_buckets

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_access_points_for_directory_buckets.async_list_access_points_for_directory_buckets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_access_points_for_directory_buckets_request.ListAccessPointsForDirectoryBucketsRequest = {
            "account_id": account_id
        }
        if directory_bucket is not None:
            input_["directory_bucket"] = directory_bucket
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

    async def iter_list_access_points_for_directory_buckets(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        directory_bucket: Optional[
            "capo_s3_control.types.bucket_name.BucketName"
        ] = None,
        next_token: Optional[
            "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_s3_control.types.access_point.AccessPoint]":
        _token = next_token
        while True:
            _response = await self.list_access_points_for_directory_buckets(
                account_id,
                config_overrides=config_overrides,
                directory_bucket=directory_bucket,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("access_point_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_access_points_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
    ) -> "capo_s3_control.types.list_access_points_for_object_lambda_result.ListAccessPointsForObjectLambdaResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns some or all (up to 1,000) access points associated with the Object Lambda Access Point per call. If there are more access points than what can be returned in one call, the response will include a continuation token that you can use to list the additional access points.</p> <p>The following actions are related to <code>ListAccessPointsForObjectLambda</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html">CreateAccessPointForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html">DeleteAccessPointForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointForObjectLambda.html">GetAccessPointForObjectLambda</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the account that owns the specified Object Lambda Access Point.</p>
            next_token: <p>If the list has more access points than can be returned in one call to this API, this field contains a continuation token that you can provide in subsequent calls to this API to retrieve additional access points.</p>
            max_results: <p>The maximum number of access points that you want to include in the list. The response may contain fewer access points but will never contain more. If there are more than this number of access points, then the response will include a continuation token in the <code>NextToken</code> field that you can use to retrieve the next page of access points.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_access_points_for_object_lambda_request.ListAccessPointsForObjectLambdaRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_access_points_for_object_lambda_result.ListAccessPointsForObjectLambdaResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_access_points_for_object_lambda

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_access_points_for_object_lambda.async_list_access_points_for_object_lambda(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_access_points_for_object_lambda_request.ListAccessPointsForObjectLambdaRequest = {
            "account_id": account_id
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

    async def iter_list_access_points_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_s3_control.types.object_lambda_access_point.ObjectLambdaAccessPoint]":
        _token = next_token
        while True:
            _response = await self.list_access_points_for_object_lambda(
                account_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("object_lambda_access_point_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_caller_access_grants(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        grant_scope: Optional["capo_s3_control.types.s3_prefix.S3Prefix"] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
        allowed_by_application: Optional[
            "capo_s3_control.types.boolean.Boolean"
        ] = None,
    ) -> "capo_s3_control.types.list_caller_access_grants_result.ListCallerAccessGrantsResult":
        """<p>Use this API to list the access grants that grant the caller access to Amazon S3 data through S3 Access Grants. The caller (grantee) can be an Identity and Access Management (IAM) identity or Amazon Web Services Identity Center corporate directory identity. You must pass the Amazon Web Services account of the S3 data owner (grantor) in the request. You can, optionally, narrow the results by <code>GrantScope</code>, using a fragment of the data's S3 path, and S3 Access Grants will return only the grants with a path that contains the path fragment. You can also pass the <code>AllowedByApplication</code> filter in the request, which returns only the grants authorized for applications, whether the application is the caller's Identity Center application or any other application (<code>ALL</code>). For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-list-grants.html">List the caller's access grants</a> in the <i>Amazon S3 User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:ListCallerAccessGrants</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            grant_scope: <p>The S3 path of the data that you would like to access. Must start with <code>s3://</code>. You can optionally pass only the beginning characters of a path, and S3 Access Grants will search for all applicable grants for the path fragment. </p>
            next_token: <p>A pagination token to request the next page of results. Pass this value into a subsequent <code>List Caller Access Grants</code> request in order to retrieve the next page of results.</p>
            max_results: <p>The maximum number of access grants that you would like returned in the <code>List Caller Access Grants</code> response. If the results include the pagination token <code>NextToken</code>, make another call using the <code>NextToken</code> to determine if there are more results.</p>
            allowed_by_application: <p>If this optional parameter is passed in the request, a filter is applied to the results. The results will include only the access grants for the caller's Identity Center application or for any other applications (<code>ALL</code>).</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_caller_access_grants_request.ListCallerAccessGrantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_caller_access_grants_result.ListCallerAccessGrantsResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_caller_access_grants

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_caller_access_grants.async_list_caller_access_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_caller_access_grants_request.ListCallerAccessGrantsRequest = {
            "account_id": account_id
        }
        if grant_scope is not None:
            input_["grant_scope"] = grant_scope
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if allowed_by_application is not None:
            input_["allowed_by_application"] = allowed_by_application

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_caller_access_grants(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        grant_scope: Optional["capo_s3_control.types.s3_prefix.S3Prefix"] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
        allowed_by_application: Optional[
            "capo_s3_control.types.boolean.Boolean"
        ] = None,
    ) -> "AsyncIterator[capo_s3_control.types.list_caller_access_grants_entry.ListCallerAccessGrantsEntry]":
        _token = next_token
        while True:
            _response = await self.list_caller_access_grants(
                account_id,
                config_overrides=config_overrides,
                grant_scope=grant_scope,
                next_token=_token,
                max_results=max_results,
                allowed_by_application=allowed_by_application,
            )
            _page = _resolve_path(_response, ("caller_access_grants_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_jobs(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        job_statuses: Optional[
            "capo_s3_control.types.job_status_list.JobStatusList"
        ] = None,
        next_token: Optional[
            "capo_s3_control.types.string_for_next_token.StringForNextToken"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
    ) -> "capo_s3_control.types.list_jobs_result.ListJobsResult":
        """<p>Lists current S3 Batch Operations jobs as well as the jobs that have ended within the last 90 days for the Amazon Web Services account making the request. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html">S3 Batch Operations</a> in the <i>Amazon S3 User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>To use the <code>ListJobs</code> operation, you must have permission to perform the <code>s3:ListJobs</code> action.</p> </dd> </dl> <p>Related actions include:</p> <p></p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html">CreateJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html">DescribeJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html">UpdateJobPriority</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html">UpdateJobStatus</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>
            job_statuses: <p>The <code>List Jobs</code> request returns jobs that match the statuses listed in this element.</p>
            next_token: <p>A pagination token to request the next page of results. Use the token that Amazon S3 returned in the <code>NextToken</code> element of the <code>ListJobsResult</code> from the previous <code>List Jobs</code> request.</p>
            max_results: <p>The maximum number of jobs that Amazon S3 will include in the <code>List Jobs</code> response. If there are more jobs than this number, the response will include a pagination token in the <code>NextToken</code> field to enable you to retrieve the next page of results.</p>

        Raises:
            capo_s3_control.errors.internal_service_exception.InternalServiceException: <p></p>
            capo_s3_control.errors.invalid_next_token_exception.InvalidNextTokenException: <p></p>
            capo_s3_control.errors.invalid_request_exception.InvalidRequestException: <p></p>
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_jobs_request.ListJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_jobs_result.ListJobsResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_jobs

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_jobs.async_list_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_jobs_request.ListJobsRequest = {
            "account_id": account_id
        }
        if job_statuses is not None:
            input_["job_statuses"] = job_statuses
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

    async def iter_list_jobs(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        job_statuses: Optional[
            "capo_s3_control.types.job_status_list.JobStatusList"
        ] = None,
        next_token: Optional[
            "capo_s3_control.types.string_for_next_token.StringForNextToken"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_s3_control.types.list_jobs_result.ListJobsResult]":
        _token = next_token
        while True:
            _response = await self.list_jobs(
                account_id,
                config_overrides=config_overrides,
                job_statuses=job_statuses,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_multi_region_access_points(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
    ) -> "capo_s3_control.types.list_multi_region_access_points_result.ListMultiRegionAccessPointsResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns a list of the Multi-Region Access Points currently associated with the specified Amazon Web Services account. Each call can return up to 100 Multi-Region Access Points, the maximum number of Multi-Region Access Points that can be associated with a single account.</p> <p>This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html">Multi-Region Access Point restrictions and limitations</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The following actions are related to <code>ListMultiRegionAccessPoint</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html">CreateMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html">DeleteMultiRegionAccessPoint</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html">DescribeMultiRegionAccessPointOperation</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html">GetMultiRegionAccessPoint</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>
            next_token: <p>Not currently used. Do not use this parameter.</p>
            max_results: <p>Not currently used. Do not use this parameter.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_multi_region_access_points_request.ListMultiRegionAccessPointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_multi_region_access_points_result.ListMultiRegionAccessPointsResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_multi_region_access_points

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_multi_region_access_points.async_list_multi_region_access_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_multi_region_access_points_request.ListMultiRegionAccessPointsRequest = {
            "account_id": account_id
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

    async def iter_list_multi_region_access_points(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_s3_control.types.list_multi_region_access_points_result.ListMultiRegionAccessPointsResult]":
        _token = next_token
        while True:
            _response = await self.list_multi_region_access_points(
                account_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_regional_buckets(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
        outpost_id: Optional[
            "capo_s3_control.types.non_empty_max_length64_string.NonEmptyMaxLength64String"
        ] = None,
    ) -> "capo_s3_control.types.list_regional_buckets_result.ListRegionalBucketsResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Returns a list of all Outposts buckets in an Outpost that are owned by the authenticated sender of the request. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in the <i>Amazon S3 User Guide</i>.</p> <p>For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and <code>x-amz-outpost-id</code> in your request, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListRegionalBuckets.html#API_control_ListRegionalBuckets_Examples">Examples</a> section.</p>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket.</p>
            next_token: <p></p>
            max_results: <p></p>
            outpost_id: <p>The ID of the Outposts resource.</p> <note> <p>This ID is required by Amazon S3 on Outposts buckets.</p> </note>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_regional_buckets_request.ListRegionalBucketsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_regional_buckets_result.ListRegionalBucketsResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_regional_buckets

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_regional_buckets.async_list_regional_buckets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_regional_buckets_request.ListRegionalBucketsRequest = {
            "account_id": account_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if outpost_id is not None:
            input_["outpost_id"] = outpost_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_regional_buckets(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
        ] = None,
        max_results: Optional["capo_s3_control.types.max_results.MaxResults"] = None,
        outpost_id: Optional[
            "capo_s3_control.types.non_empty_max_length64_string.NonEmptyMaxLength64String"
        ] = None,
    ) -> "AsyncIterator[capo_s3_control.types.list_regional_buckets_result.ListRegionalBucketsResult]":
        _token = next_token
        while True:
            _response = await self.list_regional_buckets(
                account_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                outpost_id=outpost_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_storage_lens_configurations(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
    ) -> "capo_s3_control.types.list_storage_lens_configurations_result.ListStorageLensConfigurationsResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Gets a list of Amazon S3 Storage Lens configurations. For more information about S3 Storage Lens, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html">Assessing your storage activity and usage with Amazon S3 Storage Lens </a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>To use this action, you must have permission to perform the <code>s3:ListStorageLensConfigurations</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html">Setting permissions to use Amazon S3 Storage Lens</a> in the <i>Amazon S3 User Guide</i>.</p> </note>

        Args:
            account_id: <p>The account ID of the requester.</p>
            next_token: <p>A pagination token to request the next page of results.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_storage_lens_configurations_request.ListStorageLensConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_storage_lens_configurations_result.ListStorageLensConfigurationsResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_storage_lens_configurations

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_storage_lens_configurations.async_list_storage_lens_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_storage_lens_configurations_request.ListStorageLensConfigurationsRequest = {
            "account_id": account_id
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_storage_lens_configurations(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
    ) -> "AsyncIterator[capo_s3_control.types.list_storage_lens_configurations_result.ListStorageLensConfigurationsResult]":
        _token = next_token
        while True:
            _response = await self.list_storage_lens_configurations(
                account_id,
                config_overrides=config_overrides,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_storage_lens_groups(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
    ) -> "capo_s3_control.types.list_storage_lens_groups_result.ListStorageLensGroupsResult":
        """<p> Lists all the Storage Lens groups in the specified home Region. </p> <p>To use this operation, you must have the permission to perform the <code>s3:ListStorageLensGroups</code> action. For more information about the required Storage Lens Groups permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_groups_permissions">Setting account permissions to use S3 Storage Lens groups</a>.</p> <p>For information about Storage Lens groups errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3LensErrorCodeList">List of Amazon S3 Storage Lens error codes</a>.</p>

        Args:
            account_id: <p> The Amazon Web Services account ID that owns the Storage Lens groups. </p>
            next_token: <p>The token for the next set of results, or <code>null</code> if there are no more results. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_storage_lens_groups_request.ListStorageLensGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_storage_lens_groups_result.ListStorageLensGroupsResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_storage_lens_groups

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_storage_lens_groups.async_list_storage_lens_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_storage_lens_groups_request.ListStorageLensGroupsRequest = {
            "account_id": account_id
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_storage_lens_groups(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        next_token: Optional[
            "capo_s3_control.types.continuation_token.ContinuationToken"
        ] = None,
    ) -> "AsyncIterator[capo_s3_control.types.list_storage_lens_groups_result.ListStorageLensGroupsResult]":
        _token = next_token
        while True:
            _response = await self.list_storage_lens_groups(
                account_id,
                config_overrides=config_overrides,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        resource_arn: "capo_s3_control.types.s3_resource_arn.S3ResourceArn",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> (
        "capo_s3_control.types.list_tags_for_resource_result.ListTagsForResourceResult"
    ):
        """<p>This operation allows you to list all of the tags for a specified resource. Each tag is a label consisting of a key and value. Tags can help you organize, track costs for, and control access to resources. </p> <note> <p>This operation is only supported for the following Amazon S3 resources:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging.html">General purpose buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-db-tagging.html">Access Points for directory buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-tagging.html">Access Points for general purpose buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html">Directory buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups.html">S3 Storage Lens groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-tagging.html">S3 Access Grants instances, registered locations, and grants</a>.</p> </li> </ul> </note> <dl> <dt>Permissions</dt> <dd> <p>For general purpose buckets, access points for general purpose buckets, Storage Lens groups, and S3 Access Grants, you must have the <code>s3:ListTagsForResource</code> permission to use this operation. </p> </dd> <dt>Directory bucket permissions</dt> <dd> <p>For directory buckets, you must have the <code>s3express:ListTagsForResource</code> permission to use this operation. For more information about directory buckets policies and permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-permissions.html">Identity and Access Management (IAM) for S3 Express One Zone</a> in the <i>Amazon S3 User Guide</i>.</p> </dd> <dt>HTTP Host header syntax</dt> <dd> <p> <b>Directory buckets </b> - The HTTP Host header syntax is <code>s3express-control.<i>region</i>.amazonaws.com</code>.</p> </dd> </dl> <p>For information about S3 Tagging errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3TaggingErrorCodeList">List of Amazon S3 Tagging error codes</a>.</p>

        Args:
            account_id: <p> The Amazon Web Services account ID of the resource owner. </p>
            resource_arn: <p> The Amazon Resource Name (ARN) of the S3 resource that you want to list tags for. The tagged resource can be a directory bucket, S3 Storage Lens group or S3 Access Grants instance, registered location, or grant. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.list_tags_for_resource_result.ListTagsForResourceResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "account_id": account_id,
            "resource_arn": resource_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_access_grants_instance_resource_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        policy: "capo_s3_control.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        organization: Optional[
            "capo_s3_control.types.organization.Organization"
        ] = None,
    ) -> "capo_s3_control.types.put_access_grants_instance_resource_policy_result.PutAccessGrantsInstanceResourcePolicyResult":
        """<p>Updates the resource policy of the S3 Access Grants instance. </p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:PutAccessGrantsInstanceResourcePolicy</code> permission to use this operation. </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            policy: <p>The resource policy of the S3 Access Grants instance that you are updating.</p>
            organization: <p>The Organization of the resource policy of the S3 Access Grants instance.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_access_grants_instance_resource_policy_request.PutAccessGrantsInstanceResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.put_access_grants_instance_resource_policy_result.PutAccessGrantsInstanceResourcePolicyResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_access_grants_instance_resource_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_access_grants_instance_resource_policy.async_put_access_grants_instance_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_access_grants_instance_resource_policy_request.PutAccessGrantsInstanceResourcePolicyRequest = {
            "account_id": account_id,
            "policy": policy,
        }
        if organization is not None:
            input_["organization"] = organization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_access_point_configuration_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName",
        configuration: "capo_s3_control.types.object_lambda_configuration.ObjectLambdaConfiguration",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Replaces configuration for an Object Lambda Access Point.</p> <p>The following actions are related to <code>PutAccessPointConfigurationForObjectLambda</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointConfigurationForObjectLambda.html">GetAccessPointConfigurationForObjectLambda</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the account that owns the specified Object Lambda Access Point.</p>
            name: <p>The name of the Object Lambda Access Point.</p>
            configuration: <p>Object Lambda Access Point configuration document.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_access_point_configuration_for_object_lambda_request.PutAccessPointConfigurationForObjectLambdaRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_access_point_configuration_for_object_lambda

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_access_point_configuration_for_object_lambda.async_put_access_point_configuration_for_object_lambda(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_access_point_configuration_for_object_lambda_request.PutAccessPointConfigurationForObjectLambdaRequest = {
            "account_id": account_id,
            "name": name,
            "configuration": configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_access_point_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.access_point_name.AccessPointName",
        policy: "capo_s3_control.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p>Associates an access policy with the specified access point. Each access point can have only one policy, so a request made to this API replaces any existing policy associated with the specified access point.</p> <p></p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html#API_control_PutAccessPointPolicy_Examples">Examples</a> section.</p> <p>The following actions are related to <code>PutAccessPointPolicy</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html">GetAccessPointPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html">DeleteAccessPointPolicy</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for owner of the bucket associated with the specified access point.</p>
            name: <p>The name of the access point that you want to associate with the specified policy.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name></code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>
            policy: <p>The policy that you want to apply to the specified access point. For more information about access point policies, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html">Managing data access with Amazon S3 access points</a> or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html">Managing access to shared datasets in directory buckets with access points</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_access_point_policy_request.PutAccessPointPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_access_point_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_access_point_policy.async_put_access_point_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_access_point_policy_request.PutAccessPointPolicyRequest = {
            "account_id": account_id,
            "name": name,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_access_point_policy_for_object_lambda(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.object_lambda_access_point_name.ObjectLambdaAccessPointName",
        policy: "capo_s3_control.types.object_lambda_policy.ObjectLambdaPolicy",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Creates or replaces resource policy for an Object Lambda Access Point. For an example policy, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/olap-create.html#olap-create-cli">Creating Object Lambda Access Points</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The following actions are related to <code>PutAccessPointPolicyForObjectLambda</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html">DeleteAccessPointPolicyForObjectLambda</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyForObjectLambda.html">GetAccessPointPolicyForObjectLambda</a> </p> </li> </ul>

        Args:
            account_id: <p>The account ID for the account that owns the specified Object Lambda Access Point.</p>
            name: <p>The name of the Object Lambda Access Point.</p>
            policy: <p>Object Lambda Access Point resource policy document.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_access_point_policy_for_object_lambda_request.PutAccessPointPolicyForObjectLambdaRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_access_point_policy_for_object_lambda

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_access_point_policy_for_object_lambda.async_put_access_point_policy_for_object_lambda(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_access_point_policy_for_object_lambda_request.PutAccessPointPolicyForObjectLambdaRequest = {
            "account_id": account_id,
            "name": name,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_access_point_scope(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        name: "capo_s3_control.types.access_point_name.AccessPointName",
        scope: "capo_s3_control.types.scope.Scope",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p>Creates or replaces the access point scope for a directory bucket. You can use the access point scope to restrict access to specific prefixes, API operations, or a combination of both.</p> <note> <p>You can specify any amount of prefixes, but the total length of characters of all prefixes must be less than 256 bytes in size.</p> </note> <p>To use this operation, you must have the permission to perform the <code>s3express:PutAccessPointScope</code> action.</p> <p>For information about REST API errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#RESTErrorResponses">REST error responses</a>.</p>

        Args:
            account_id: <p> The Amazon Web Services account ID that owns the access point with scope that you want to create or replace. </p>
            name: <p>The name of the access point with the scope that you want to create or replace.</p>
            scope: <p>Object prefixes, API operations, or a combination of both.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_access_point_scope_request.PutAccessPointScopeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_access_point_scope

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_access_point_scope.async_put_access_point_scope(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_access_point_scope_request.PutAccessPointScopeRequest = {
            "account_id": account_id,
            "name": name,
            "scope": scope,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_bucket_lifecycle_configuration(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        lifecycle_configuration: Optional[
            "capo_s3_control.types.lifecycle_configuration.LifecycleConfiguration"
        ] = None,
    ) -> None:
        """<note> <p>This action puts a lifecycle configuration to an Amazon S3 on Outposts bucket. To put a lifecycle configuration to an S3 bucket, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html">PutBucketLifecycleConfiguration</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Creates a new lifecycle configuration for the S3 on Outposts bucket or replaces an existing lifecycle configuration. Outposts buckets only support lifecycle configurations that delete/expire objects after a certain period of time and abort incomplete multipart uploads.</p> <p></p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html#API_control_PutBucketLifecycleConfiguration_Examples">Examples</a> section.</p> <p>The following actions are related to <code>PutBucketLifecycleConfiguration</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html">GetBucketLifecycleConfiguration</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketLifecycleConfiguration.html">DeleteBucketLifecycleConfiguration</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket.</p>
            bucket: <p>The name of the bucket for which to set the configuration.</p>
            lifecycle_configuration: <p>Container for lifecycle rules. You can add as many as 1,000 rules.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_bucket_lifecycle_configuration_request.PutBucketLifecycleConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_bucket_lifecycle_configuration

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_bucket_lifecycle_configuration.async_put_bucket_lifecycle_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_bucket_lifecycle_configuration_request.PutBucketLifecycleConfigurationRequest = {
            "account_id": account_id,
            "bucket": bucket,
        }
        if lifecycle_configuration is not None:
            input_["lifecycle_configuration"] = lifecycle_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_bucket_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        policy: "capo_s3_control.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        confirm_remove_self_bucket_access: Optional[
            "capo_s3_control.types.confirm_remove_self_bucket_access.ConfirmRemoveSelfBucketAccess"
        ] = None,
    ) -> None:
        """<note> <p>This action puts a bucket policy to an Amazon S3 on Outposts bucket. To put a policy on an S3 bucket, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html">PutBucketPolicy</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Applies an Amazon S3 bucket policy to an Outposts bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you are using an identity other than the root user of the Amazon Web Services account that owns the Outposts bucket, the calling identity must have the <code>PutBucketPolicy</code> permissions on the specified Outposts bucket and belong to the bucket owner's account in order to use this action.</p> <p>If you don't have <code>PutBucketPolicy</code> permissions, Amazon S3 returns a <code>403 Access Denied</code> error. If you have the correct permissions, but you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a <code>405 Method Not Allowed</code> error.</p> <important> <p> As a security precaution, the root user of the Amazon Web Services account that owns a bucket can always use this action, even if the policy explicitly denies the root user the ability to perform this action. </p> </important> <p>For more information about bucket policies, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html">Using Bucket Policies and User Policies</a>.</p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketPolicy.html#API_control_PutBucketPolicy_Examples">Examples</a> section.</p> <p>The following actions are related to <code>PutBucketPolicy</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketPolicy.html">GetBucketPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketPolicy.html">DeleteBucketPolicy</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket.</p>
            bucket: <p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
            confirm_remove_self_bucket_access: <p>Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>
            policy: <p>The bucket policy as a JSON document.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_bucket_policy_request.PutBucketPolicyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_bucket_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_bucket_policy.async_put_bucket_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_bucket_policy_request.PutBucketPolicyRequest = {
            "account_id": account_id,
            "bucket": bucket,
            "policy": policy,
        }
        if confirm_remove_self_bucket_access is not None:
            input_["confirm_remove_self_bucket_access"] = (
                confirm_remove_self_bucket_access
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_bucket_replication(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        replication_configuration: "capo_s3_control.types.replication_configuration.ReplicationConfiguration",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This action creates an Amazon S3 on Outposts bucket's replication configuration. To create an S3 bucket's replication configuration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html">PutBucketReplication</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Creates a replication configuration or replaces an existing one. For information about S3 replication on Outposts configuration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsReplication.html">Replicating objects for S3 on Outposts</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>It can take a while to propagate <code>PUT</code> or <code>DELETE</code> requests for a replication configuration to all S3 on Outposts systems. Therefore, the replication configuration that's returned by a <code>GET</code> request soon after a <code>PUT</code> or <code>DELETE</code> request might return a more recent result than what's on the Outpost. If an Outpost is offline, the delay in updating the replication configuration on that Outpost can be significant.</p> </note> <p>Specify the replication configuration in the request body. In the replication configuration, you provide the following information:</p> <ul> <li> <p>The name of the destination bucket or buckets where you want S3 on Outposts to replicate objects</p> </li> <li> <p>The Identity and Access Management (IAM) role that S3 on Outposts can assume to replicate objects on your behalf</p> </li> <li> <p>Other relevant information, such as replication rules</p> </li> </ul> <p>A replication configuration must include at least one rule and can contain a maximum of 100. Each rule identifies a subset of objects to replicate by filtering the objects in the source Outposts bucket. To choose additional subsets of objects to replicate, add a rule for each subset.</p> <p>To specify a subset of the objects in the source Outposts bucket to apply a replication rule to, add the <code>Filter</code> element as a child of the <code>Rule</code> element. You can filter objects based on an object key prefix, one or more object tags, or both. When you add the <code>Filter</code> element in the configuration, you must also add the following elements: <code>DeleteMarkerReplication</code>, <code>Status</code>, and <code>Priority</code>.</p> <p>Using <code>PutBucketReplication</code> on Outposts requires that both the source and destination buckets must have versioning enabled. For information about enabling versioning on a bucket, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsManagingVersioning.html">Managing S3 Versioning for your S3 on Outposts bucket</a>.</p> <p>For information about S3 on Outposts replication failure reasons, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/outposts-replication-eventbridge.html#outposts-replication-failure-codes">Replication failure reasons</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Handling Replication of Encrypted Objects</b> </p> <p>Outposts buckets are encrypted at all times. All the objects in the source Outposts bucket are encrypted and can be replicated. Also, all the replicas in the destination Outposts bucket are encrypted with the same encryption key as the objects in the source Outposts bucket.</p> <p> <b>Permissions</b> </p> <p>To create a <code>PutBucketReplication</code> request, you must have <code>s3-outposts:PutReplicationConfiguration</code> permissions for the bucket. The Outposts bucket owner has this permission by default and can grant it to others. For more information about permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsIAM.html">Setting up IAM with S3 on Outposts</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsBucketPolicy.html">Managing access to S3 on Outposts buckets</a>. </p> <note> <p>To perform this operation, the user or role must also have the <code>iam:CreateRole</code> and <code>iam:PassRole</code> permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html">Granting a user permissions to pass a role to an Amazon Web Services service</a>.</p> </note> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketReplication.html#API_control_PutBucketReplication_Examples">Examples</a> section.</p> <p>The following operations are related to <code>PutBucketReplication</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketReplication.html">GetBucketReplication</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketReplication.html">DeleteBucketReplication</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket.</p>
            bucket: <p>Specifies the S3 on Outposts bucket to set the configuration for.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
            replication_configuration: <p></p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_bucket_replication_request.PutBucketReplicationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_bucket_replication

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_bucket_replication.async_put_bucket_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_bucket_replication_request.PutBucketReplicationRequest = {
            "account_id": account_id,
            "bucket": bucket,
            "replication_configuration": replication_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_bucket_tagging(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        tagging: "capo_s3_control.types.tagging.Tagging",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This action puts tags on an Amazon S3 on Outposts bucket. To put tags on an S3 bucket, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html">PutBucketTagging</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Sets the tags for an S3 on Outposts bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">Using Amazon S3 on Outposts</a> in the <i>Amazon S3 User Guide</i>.</p> <p>Use tags to organize your Amazon Web Services bill to reflect your own cost structure. To do this, sign up to get your Amazon Web Services account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Cost allocation and tagging</a>.</p> <note> <p>Within a bucket, if you add a tag that has the same key as an existing tag, the new value overwrites the old value. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html"> Using cost allocation in Amazon S3 bucket tags</a>.</p> </note> <p>To use this action, you must have permissions to perform the <code>s3-outposts:PutBucketTagging</code> action. The Outposts bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources"> Permissions Related to Bucket Subresource Operations</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html">Managing access permissions to your Amazon S3 resources</a>.</p> <p> <code>PutBucketTagging</code> has the following special errors:</p> <ul> <li> <p>Error code: <code>InvalidTagError</code> </p> <ul> <li> <p>Description: The tag provided was not a valid tag. This error can occur if the tag did not pass input validation. For information about tag restrictions, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html"> User-Defined Tag Restrictions</a> and <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tag-restrictions.html"> Amazon Web Services-Generated Cost Allocation Tag Restrictions</a>.</p> </li> </ul> </li> <li> <p>Error code: <code>MalformedXMLError</code> </p> <ul> <li> <p>Description: The XML provided does not match the schema.</p> </li> </ul> </li> <li> <p>Error code: <code>OperationAbortedError </code> </p> <ul> <li> <p>Description: A conflicting conditional action is currently in progress against this resource. Try again.</p> </li> </ul> </li> <li> <p>Error code: <code>InternalError</code> </p> <ul> <li> <p>Description: The service was unable to apply the provided tag to the bucket.</p> </li> </ul> </li> </ul> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketTagging.html#API_control_PutBucketTagging_Examples">Examples</a> section.</p> <p>The following actions are related to <code>PutBucketTagging</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketTagging.html">GetBucketTagging</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteBucketTagging.html">DeleteBucketTagging</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the Outposts bucket.</p>
            bucket: <p>The Amazon Resource Name (ARN) of the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>
            tagging: <p></p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_bucket_tagging_request.PutBucketTaggingRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_bucket_tagging

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_bucket_tagging.async_put_bucket_tagging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_bucket_tagging_request.PutBucketTaggingRequest = {
            "account_id": account_id,
            "bucket": bucket,
            "tagging": tagging,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_bucket_versioning(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        bucket: "capo_s3_control.types.bucket_name.BucketName",
        versioning_configuration: "capo_s3_control.types.versioning_configuration.VersioningConfiguration",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        mfa: Optional["capo_s3_control.types.mfa.MFA"] = None,
    ) -> None:
        """<note> <p>This operation sets the versioning state for S3 on Outposts buckets only. To set the versioning state for an S3 bucket, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html">PutBucketVersioning</a> in the <i>Amazon S3 API Reference</i>. </p> </note> <p>Sets the versioning state for an S3 on Outposts bucket. With S3 Versioning, you can save multiple distinct copies of your objects and recover from unintended user actions and application failures.</p> <p>You can set the versioning state to one of the following:</p> <ul> <li> <p> <b>Enabled</b> - Enables versioning for the objects in the bucket. All objects added to the bucket receive a unique version ID.</p> </li> <li> <p> <b>Suspended</b> - Suspends versioning for the objects in the bucket. All objects added to the bucket receive the version ID <code>null</code>.</p> </li> </ul> <p>If you've never set versioning on your bucket, it has no versioning state. In that case, a <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketVersioning.html"> GetBucketVersioning</a> request does not return a versioning state value.</p> <p>When you enable S3 Versioning, for each object in your bucket, you have a current version and zero or more noncurrent versions. You can configure your bucket S3 Lifecycle rules to expire noncurrent versions after a specified time period. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsLifecycleManaging.html"> Creating and managing a lifecycle configuration for your S3 on Outposts bucket</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you have an object expiration lifecycle configuration in your non-versioned bucket and you want to maintain the same permanent delete behavior when you enable versioning, you must add a noncurrent expiration policy. The noncurrent expiration lifecycle configuration will manage the deletes of the noncurrent object versions in the version-enabled bucket. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html">Versioning</a> in the <i>Amazon S3 User Guide</i>.</p> <p>All Amazon S3 on Outposts REST API requests for this action require an additional parameter of <code>x-amz-outpost-id</code> to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of <code>s3-control</code>. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the <code>x-amz-outpost-id</code> derived by using the access point ARN, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketVersioning.html#API_control_PutBucketVersioning_Examples">Examples</a> section.</p> <p>The following operations are related to <code>PutBucketVersioning</code> for S3 on Outposts.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketVersioning.html">GetBucketVersioning</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutBucketLifecycleConfiguration.html">PutBucketLifecycleConfiguration</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucketLifecycleConfiguration.html">GetBucketLifecycleConfiguration</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 on Outposts bucket.</p>
            bucket: <p>The S3 on Outposts bucket to set the versioning state for.</p>
            mfa: <p>The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.</p>
            versioning_configuration: <p>The root-level tag for the <code>VersioningConfiguration</code> parameters.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_bucket_versioning_request.PutBucketVersioningRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_bucket_versioning

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_bucket_versioning.async_put_bucket_versioning(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_bucket_versioning_request.PutBucketVersioningRequest = {
            "account_id": account_id,
            "bucket": bucket,
            "versioning_configuration": versioning_configuration,
        }
        if mfa is not None:
            input_["mfa"] = mfa

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_job_tagging(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        job_id: "capo_s3_control.types.job_id.JobId",
        tags: "capo_s3_control.types.s3_tag_set.S3TagSet",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.put_job_tagging_result.PutJobTaggingResult":
        """<p>Sets the supplied tag-set on an S3 Batch Operations job.</p> <p>A tag is a key-value pair. You can associate S3 Batch Operations tags with any job by sending a PUT request against the tagging subresource that is associated with the job. To modify the existing tag set, you can either replace the existing tag set entirely, or make changes within the existing tag set by retrieving the existing tag set using <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html">GetJobTagging</a>, modify that tag set, and use this operation to replace the tag set with the one you modified. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-managing-jobs.html#batch-ops-job-tags">Controlling access and labeling jobs using tags</a> in the <i>Amazon S3 User Guide</i>. </p> <note> <ul> <li> <p>If you send this request with an empty tag set, Amazon S3 deletes the existing tag set on the Batch Operations job. If you use this method, you are charged for a Tier 1 Request (PUT). For more information, see <a href="http://aws.amazon.com/s3/pricing/">Amazon S3 pricing</a>.</p> </li> <li> <p>For deleting existing tags for your Batch Operations job, a <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html">DeleteJobTagging</a> request is preferred because it achieves the same result without incurring charges.</p> </li> <li> <p>A few things to consider about using tags:</p> <ul> <li> <p>Amazon S3 limits the maximum number of tags to 50 tags per job.</p> </li> <li> <p>You can associate up to 50 tags with a job as long as they have unique tag keys.</p> </li> <li> <p>A tag key can be up to 128 Unicode characters in length, and tag values can be up to 256 Unicode characters in length.</p> </li> <li> <p>The key and values are case sensitive.</p> </li> <li> <p>For tagging-related restrictions related to characters and encodings, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html">User-Defined Tag Restrictions</a> in the <i>Billing and Cost Management User Guide</i>.</p> </li> </ul> </li> </ul> </note> <dl> <dt>Permissions</dt> <dd> <p>To use the <code>PutJobTagging</code> operation, you must have permission to perform the <code>s3:PutJobTagging</code> action.</p> </dd> </dl> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html">CreateJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html">GetJobTagging</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html">DeleteJobTagging</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>
            job_id: <p>The ID for the S3 Batch Operations job whose tags you want to replace.</p>
            tags: <p>The set of tags to associate with the S3 Batch Operations job.</p>

        Raises:
            capo_s3_control.errors.internal_service_exception.InternalServiceException: <p></p>
            capo_s3_control.errors.not_found_exception.NotFoundException: <p></p>
            capo_s3_control.errors.too_many_requests_exception.TooManyRequestsException: <p></p>
            capo_s3_control.errors.too_many_tags_exception.TooManyTagsException: <p>Amazon S3 throws this exception if you have too many tags in your tag set.</p>
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_job_tagging_request.PutJobTaggingRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.put_job_tagging_result.PutJobTaggingResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_job_tagging

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_job_tagging.async_put_job_tagging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_job_tagging_request.PutJobTaggingRequest = {
            "account_id": account_id,
            "job_id": job_id,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_multi_region_access_point_policy(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        client_token: "capo_s3_control.types.multi_region_access_point_client_token.MultiRegionAccessPointClientToken",
        details: "capo_s3_control.types.put_multi_region_access_point_policy_input.PutMultiRegionAccessPointPolicyInput",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.put_multi_region_access_point_policy_result.PutMultiRegionAccessPointPolicyResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Associates an access control policy with the specified Multi-Region Access Point. Each Multi-Region Access Point can have only one policy, so a request made to this action replaces any existing policy that is associated with the specified Multi-Region Access Point.</p> <p>This action will always be routed to the US West (Oregon) Region. For more information about the restrictions around working with Multi-Region Access Points, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPointRestrictions.html">Multi-Region Access Point restrictions and limitations</a> in the <i>Amazon S3 User Guide</i>.</p> <p>The following actions are related to <code>PutMultiRegionAccessPointPolicy</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html">GetMultiRegionAccessPointPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html">GetMultiRegionAccessPointPolicyStatus</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>
            client_token: <p>An idempotency token used to identify the request and guarantee that requests are unique.</p>
            details: <p>A container element containing the details of the policy for the Multi-Region Access Point.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_multi_region_access_point_policy_request.PutMultiRegionAccessPointPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.put_multi_region_access_point_policy_result.PutMultiRegionAccessPointPolicyResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_multi_region_access_point_policy

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_multi_region_access_point_policy.async_put_multi_region_access_point_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_multi_region_access_point_policy_request.PutMultiRegionAccessPointPolicyRequest = {
            "account_id": account_id,
            "client_token": client_token,
            "details": details,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_public_access_block(
        self,
        public_access_block_configuration: "capo_s3_control.types.public_access_block_configuration.PublicAccessBlockConfiguration",
        account_id: "capo_s3_control.types.account_id.AccountId",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Creates or modifies the <code>PublicAccessBlock</code> configuration for an Amazon Web Services account. This operation may be restricted when the account is managed by organization-level Block Public Access policies. You might get an Access Denied (403) error when the account is managed by organization-level Block Public Access policies. Organization-level policies override account-level settings, preventing direct account-level modifications. For this operation, users must have the <code>s3:PutAccountPublicAccessBlock</code> permission. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html"> Using Amazon S3 block public access</a>.</p> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetPublicAccessBlock.html">GetPublicAccessBlock</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeletePublicAccessBlock.html">DeletePublicAccessBlock</a> </p> </li> </ul>

        Args:
            public_access_block_configuration: <p>The <code>PublicAccessBlock</code> configuration that you want to apply to the specified Amazon Web Services account.</p>
            account_id: <p>The account ID for the Amazon Web Services account whose <code>PublicAccessBlock</code> configuration you want to set.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_public_access_block_request.PutPublicAccessBlockRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_public_access_block

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_public_access_block.async_put_public_access_block(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_public_access_block_request.PutPublicAccessBlockRequest = {
            "public_access_block_configuration": public_access_block_configuration,
            "account_id": account_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_storage_lens_configuration(
        self,
        config_id: "capo_s3_control.types.config_id.ConfigId",
        account_id: "capo_s3_control.types.account_id.AccountId",
        storage_lens_configuration: "capo_s3_control.types.storage_lens_configuration.StorageLensConfiguration",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        tags: Optional[
            "capo_s3_control.types.storage_lens_tags.StorageLensTags"
        ] = None,
    ) -> None:
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Puts an Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html">Working with Amazon S3 Storage Lens</a> in the <i>Amazon S3 User Guide</i>. For a complete list of S3 Storage Lens metrics, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_metrics_glossary.html">S3 Storage Lens metrics glossary</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>To use this action, you must have permission to perform the <code>s3:PutStorageLensConfiguration</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html">Setting permissions to use Amazon S3 Storage Lens</a> in the <i>Amazon S3 User Guide</i>.</p> </note>

        Args:
            config_id: <p>The ID of the S3 Storage Lens configuration.</p>
            account_id: <p>The account ID of the requester.</p>
            storage_lens_configuration: <p>The S3 Storage Lens configuration.</p>
            tags: <p>The tag set of the S3 Storage Lens configuration.</p> <note> <p>You can set up to a maximum of 50 tags.</p> </note>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_storage_lens_configuration_request.PutStorageLensConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_storage_lens_configuration

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_storage_lens_configuration.async_put_storage_lens_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_storage_lens_configuration_request.PutStorageLensConfigurationRequest = {
            "config_id": config_id,
            "account_id": account_id,
            "storage_lens_configuration": storage_lens_configuration,
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

    async def put_storage_lens_configuration_tagging(
        self,
        config_id: "capo_s3_control.types.config_id.ConfigId",
        account_id: "capo_s3_control.types.account_id.AccountId",
        tags: "capo_s3_control.types.storage_lens_tags.StorageLensTags",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.put_storage_lens_configuration_tagging_result.PutStorageLensConfigurationTaggingResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Put or replace tags on an existing Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html">Assessing your storage activity and usage with Amazon S3 Storage Lens </a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>To use this action, you must have permission to perform the <code>s3:PutStorageLensConfigurationTagging</code> action. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html">Setting permissions to use Amazon S3 Storage Lens</a> in the <i>Amazon S3 User Guide</i>.</p> </note>

        Args:
            config_id: <p>The ID of the S3 Storage Lens configuration.</p>
            account_id: <p>The account ID of the requester.</p>
            tags: <p>The tag set of the S3 Storage Lens configuration.</p> <note> <p>You can set up to a maximum of 50 tags.</p> </note>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.put_storage_lens_configuration_tagging_request.PutStorageLensConfigurationTaggingRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.put_storage_lens_configuration_tagging_result.PutStorageLensConfigurationTaggingResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.put_storage_lens_configuration_tagging

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.put_storage_lens_configuration_tagging.async_put_storage_lens_configuration_tagging(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.put_storage_lens_configuration_tagging_request.PutStorageLensConfigurationTaggingRequest = {
            "config_id": config_id,
            "account_id": account_id,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_multi_region_access_point_routes(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        mrap: "capo_s3_control.types.multi_region_access_point_id.MultiRegionAccessPointId",
        route_updates: "capo_s3_control.types.route_list.RouteList",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.submit_multi_region_access_point_routes_result.SubmitMultiRegionAccessPointRoutesResult":
        """<note> <p>This operation is not supported by directory buckets.</p> </note> <p>Submits an updated route configuration for a Multi-Region Access Point. This API operation updates the routing status for the specified Regions from active to passive, or from passive to active. A value of <code>0</code> indicates a passive status, which means that traffic won't be routed to the specified Region. A value of <code>100</code> indicates an active status, which means that traffic will be routed to the specified Region. At least one Region must be active at all times.</p> <p>When the routing configuration is changed, any in-progress operations (uploads, copies, deletes, and so on) to formerly active Regions will continue to run to their final completion state (success or failure). The routing configurations of any Regions that aren’t specified remain unchanged.</p> <note> <p>Updated routing configurations might not be immediately applied. It can take up to 2 minutes for your changes to take effect.</p> </note> <p>To submit routing control changes and failover requests, use the Amazon S3 failover control infrastructure endpoints in these five Amazon Web Services Regions:</p> <ul> <li> <p> <code>us-east-1</code> </p> </li> <li> <p> <code>us-west-2</code> </p> </li> <li> <p> <code>ap-southeast-2</code> </p> </li> <li> <p> <code>ap-northeast-1</code> </p> </li> <li> <p> <code>eu-west-1</code> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID for the owner of the Multi-Region Access Point.</p>
            mrap: <p>The Multi-Region Access Point ARN.</p>
            route_updates: <p>The different routes that make up the new route configuration. Active routes return a value of <code>100</code>, and passive routes return a value of <code>0</code>.</p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.submit_multi_region_access_point_routes_request.SubmitMultiRegionAccessPointRoutesRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.submit_multi_region_access_point_routes_result.SubmitMultiRegionAccessPointRoutesResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.submit_multi_region_access_point_routes

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.submit_multi_region_access_point_routes.async_submit_multi_region_access_point_routes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.submit_multi_region_access_point_routes_request.SubmitMultiRegionAccessPointRoutesRequest = {
            "account_id": account_id,
            "mrap": mrap,
            "route_updates": route_updates,
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
        account_id: "capo_s3_control.types.account_id.AccountId",
        resource_arn: "capo_s3_control.types.s3_resource_arn.S3ResourceArn",
        tags: "capo_s3_control.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.tag_resource_result.TagResourceResult":
        """<p> Creates a new user-defined tag or updates an existing tag. Each tag is a label consisting of a key and value that is applied to your resource. Tags can help you organize, track costs for, and control access to your resources. You can add up to 50 Amazon Web Services resource tags for each S3 resource. </p> <note> <p>This operation is only supported for the following Amazon S3 resource:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging.html">General purpose buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-db-tagging.html">Access Points for directory buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-tagging.html">Access Points for general purpose buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html">Directory buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups.html">S3 Storage Lens groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-tagging.html">S3 Access Grants instances, registered locations, or grants</a>.</p> </li> </ul> </note> <dl> <dt>Permissions</dt> <dd> <p>For general purpose buckets, access points for general purpose buckets, Storage Lens groups, and S3 Access Grants, you must have the <code>s3:TagResource</code> permission to use this operation. </p> </dd> <dt>Directory bucket permissions</dt> <dd> <p>For directory buckets, you must have the <code>s3express:TagResource</code> permission to use this operation. For more information about directory buckets policies and permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-permissions.html">Identity and Access Management (IAM) for S3 Express One Zone</a> in the <i>Amazon S3 User Guide</i>.</p> </dd> <dt>HTTP Host header syntax</dt> <dd> <p> <b>Directory buckets </b> - The HTTP Host header syntax is <code>s3express-control.<i>region</i>.amazonaws.com</code>.</p> </dd> </dl> <p>For information about S3 Tagging errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3TaggingErrorCodeList">List of Amazon S3 Tagging error codes</a>.</p>

        Args:
            account_id: <p> The Amazon Web Services account ID that created the S3 resource that you're trying to add tags to or the requester's account ID. </p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the S3 resource that you're applying tags to. The tagged resource can be a directory bucket, S3 Storage Lens group or S3 Access Grants instance, registered location, or grant.</p>
            tags: <p> The Amazon Web Services resource tags that you want to add to the specified S3 resource. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.tag_resource_result.TagResourceResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.tag_resource

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.tag_resource_request.TagResourceRequest = {
            "account_id": account_id,
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
        account_id: "capo_s3_control.types.account_id.AccountId",
        resource_arn: "capo_s3_control.types.s3_resource_arn.S3ResourceArn",
        tag_keys: "capo_s3_control.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.untag_resource_result.UntagResourceResult":
        """<p>This operation removes the specified user-defined tags from an S3 resource. You can pass one or more tag keys. </p> <note> <p>This operation is only supported for the following Amazon S3 resources:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging.html">General purpose buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-db-tagging.html">Access Points for directory buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-tagging.html">Access Points for general purpose buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html">Directory buckets</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-groups.html">S3 Storage Lens groups</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-grants-tagging.html">S3 Access Grants instances, registered locations, and grants</a>.</p> </li> </ul> </note> <dl> <dt>Permissions</dt> <dd> <p>For general purpose buckets, access points for general purpose buckets, Storage Lens groups, and S3 Access Grants, you must have the <code>s3:UntagResource</code> permission to use this operation. </p> </dd> <dt>Directory bucket permissions</dt> <dd> <p>For directory buckets, you must have the <code>s3express:UntagResource</code> permission to use this operation. For more information about directory buckets policies and permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-permissions.html">Identity and Access Management (IAM) for S3 Express One Zone</a> in the <i>Amazon S3 User Guide</i>.</p> </dd> <dt>HTTP Host header syntax</dt> <dd> <p> <b>Directory buckets </b> - The HTTP Host header syntax is <code>s3express-control.<i>region</i>.amazonaws.com</code>.</p> </dd> </dl> <p>For information about S3 Tagging errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3TaggingErrorCodeList">List of Amazon S3 Tagging error codes</a>.</p>

        Args:
            account_id: <p> The Amazon Web Services account ID that owns the resource that you're trying to remove the tags from. </p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the S3 resource that you're removing tags from. The tagged resource can be a directory bucket, S3 Storage Lens group or S3 Access Grants instance, registered location, or grant.</p>
            tag_keys: <p> The array of tag key-value pairs that you're trying to remove from of the S3 resource. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.untag_resource_result.UntagResourceResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.untag_resource

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.untag_resource_request.UntagResourceRequest = {
            "account_id": account_id,
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

    async def update_access_grants_location(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        access_grants_location_id: "capo_s3_control.types.access_grants_location_id.AccessGrantsLocationId",
        iam_role_arn: "capo_s3_control.types.iam_role_arn.IAMRoleArn",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.update_access_grants_location_result.UpdateAccessGrantsLocationResult":
        """<p>Updates the IAM role of a registered location in your S3 Access Grants instance.</p> <dl> <dt>Permissions</dt> <dd> <p>You must have the <code>s3:UpdateAccessGrantsLocation</code> permission to use this operation. </p> </dd> <dt>Additional Permissions</dt> <dd> <p>You must also have the following permission: <code>iam:PassRole</code> </p> </dd> </dl>

        Args:
            account_id: <p>The Amazon Web Services account ID of the S3 Access Grants instance.</p>
            access_grants_location_id: <p>The ID of the registered location that you are updating. S3 Access Grants assigns this ID when you register the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p> <p>The ID of the registered location to which you are granting access. S3 Access Grants assigned this ID when you registered the location. S3 Access Grants assigns the ID <code>default</code> to the default location <code>s3://</code> and assigns an auto-generated ID to other locations that you register. </p> <p>If you are passing the <code>default</code> location, you cannot create an access grant for the entire default location. You must also specify a bucket or a bucket and prefix in the <code>Subprefix</code> field. </p>
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants assumes this role to manage access to the registered location. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.update_access_grants_location_request.UpdateAccessGrantsLocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.update_access_grants_location_result.UpdateAccessGrantsLocationResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.update_access_grants_location

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.update_access_grants_location.async_update_access_grants_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.update_access_grants_location_request.UpdateAccessGrantsLocationRequest = {
            "account_id": account_id,
            "access_grants_location_id": access_grants_location_id,
            "iam_role_arn": iam_role_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_job_priority(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        job_id: "capo_s3_control.types.job_id.JobId",
        priority: "capo_s3_control.types.job_priority.JobPriority",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> "capo_s3_control.types.update_job_priority_result.UpdateJobPriorityResult":
        """<p>Updates an existing S3 Batch Operations job's priority. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html">S3 Batch Operations</a> in the <i>Amazon S3 User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>To use the <code>UpdateJobPriority</code> operation, you must have permission to perform the <code>s3:UpdateJobPriority</code> action.</p> </dd> </dl> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html">CreateJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html">ListJobs</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html">DescribeJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html">UpdateJobStatus</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>
            job_id: <p>The ID for the job whose priority you want to update.</p>
            priority: <p>The priority you want to assign to this job.</p>

        Raises:
            capo_s3_control.errors.bad_request_exception.BadRequestException: <p></p>
            capo_s3_control.errors.internal_service_exception.InternalServiceException: <p></p>
            capo_s3_control.errors.not_found_exception.NotFoundException: <p></p>
            capo_s3_control.errors.too_many_requests_exception.TooManyRequestsException: <p></p>
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.update_job_priority_request.UpdateJobPriorityRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.update_job_priority_result.UpdateJobPriorityResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.update_job_priority

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.update_job_priority.async_update_job_priority(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.update_job_priority_request.UpdateJobPriorityRequest = {
            "account_id": account_id,
            "job_id": job_id,
            "priority": priority,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_job_status(
        self,
        account_id: "capo_s3_control.types.account_id.AccountId",
        job_id: "capo_s3_control.types.job_id.JobId",
        requested_job_status: "capo_s3_control.types.requested_job_status.RequestedJobStatus",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
        status_update_reason: Optional[
            "capo_s3_control.types.job_status_update_reason.JobStatusUpdateReason"
        ] = None,
    ) -> "capo_s3_control.types.update_job_status_result.UpdateJobStatusResult":
        """<p>Updates the status for the specified job. Use this operation to confirm that you want to run a job or to cancel an existing job. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html">S3 Batch Operations</a> in the <i>Amazon S3 User Guide</i>.</p> <dl> <dt>Permissions</dt> <dd> <p>To use the <code>UpdateJobStatus</code> operation, you must have permission to perform the <code>s3:UpdateJobStatus</code> action.</p> </dd> </dl> <p>Related actions include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html">CreateJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html">ListJobs</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html">DescribeJob</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html">UpdateJobStatus</a> </p> </li> </ul>

        Args:
            account_id: <p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>
            job_id: <p>The ID of the job whose status you want to update.</p>
            requested_job_status: <p>The status that you want to move the specified job to.</p>
            status_update_reason: <p>A description of the reason why you want to change the specified job's status. This field can be any string up to the maximum length.</p>

        Raises:
            capo_s3_control.errors.bad_request_exception.BadRequestException: <p></p>
            capo_s3_control.errors.internal_service_exception.InternalServiceException: <p></p>
            capo_s3_control.errors.job_status_exception.JobStatusException: <p></p>
            capo_s3_control.errors.not_found_exception.NotFoundException: <p></p>
            capo_s3_control.errors.too_many_requests_exception.TooManyRequestsException: <p></p>
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.update_job_status_request.UpdateJobStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_s3_control.types.update_job_status_result.UpdateJobStatusResult"
        ]:
            import capo_s3_control._operations.awss3_control_service_v20180820.update_job_status

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.update_job_status.async_update_job_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.update_job_status_request.UpdateJobStatusRequest = {
            "account_id": account_id,
            "job_id": job_id,
            "requested_job_status": requested_job_status,
        }
        if status_update_reason is not None:
            input_["status_update_reason"] = status_update_reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_storage_lens_group(
        self,
        name: "capo_s3_control.types.storage_lens_group_name.StorageLensGroupName",
        account_id: "capo_s3_control.types.account_id.AccountId",
        storage_lens_group: "capo_s3_control.types.storage_lens_group.StorageLensGroup",
        *,
        config_overrides: Optional[AsyncS3ControlClientConfig] = None,
    ) -> None:
        """<p> Updates the existing Storage Lens group.</p> <p>To use this operation, you must have the permission to perform the <code>s3:UpdateStorageLensGroup</code> action. For more information about the required Storage Lens Groups permissions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_groups_permissions">Setting account permissions to use S3 Storage Lens groups</a>.</p> <p>For information about Storage Lens groups errors, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3LensErrorCodeList">List of Amazon S3 Storage Lens error codes</a>.</p>

        Args:
            name: <p> The name of the Storage Lens group that you want to update. </p>
            account_id: <p> The Amazon Web Services account ID of the Storage Lens group owner. </p>
            storage_lens_group: <p> The JSON file that contains the Storage Lens group configuration. </p>

        Raises:
            capo_s3_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_s3_control.types.update_storage_lens_group_request.UpdateStorageLensGroupRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_s3_control._operations.awss3_control_service_v20180820.update_storage_lens_group

            (
                output,
                http_response,
            ) = await capo_s3_control._operations.awss3_control_service_v20180820.update_storage_lens_group.async_update_storage_lens_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_s3_control.types.update_storage_lens_group_request.UpdateStorageLensGroupRequest = {
            "name": name,
            "account_id": account_id,
            "storage_lens_group": storage_lens_group,
        }

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
