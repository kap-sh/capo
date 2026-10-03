"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#RedshiftServerless``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_redshift_serverless._auth._signers
import capo_redshift_serverless._auth._sigv4
from capo_redshift_serverless._auth._identity import Credentials
from capo_redshift_serverless._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_redshift_serverless._auth._zapros_handler import AuthMiddleware
from capo_redshift_serverless._pagination import resolve_path as _resolve_path
from capo_redshift_serverless._resources.redshift_serverless.cross_vpc_endpoint_resource import (
    AsyncCrossVpcEndpointResource,
)
from capo_redshift_serverless._resources.redshift_serverless.managed_workgroup_resource import (
    AsyncManagedWorkgroupResource,
)
from capo_redshift_serverless._resources.redshift_serverless.namespace_resource import (
    AsyncNamespaceResource,
)
from capo_redshift_serverless._resources.redshift_serverless.recovery_point_resource import (
    AsyncRecoveryPointResource,
)
from capo_redshift_serverless._resources.redshift_serverless.reservation_resource import (
    AsyncReservationResource,
)
from capo_redshift_serverless._resources.redshift_serverless.scheduled_action_resource import (
    AsyncScheduledActionResource,
)
from capo_redshift_serverless._resources.redshift_serverless.snapshot_resource import (
    AsyncSnapshotResource,
)
from capo_redshift_serverless._resources.redshift_serverless.usage_limit_resource import (
    AsyncUsageLimitResource,
)
from capo_redshift_serverless._resources.redshift_serverless.workgroup_resource import (
    AsyncWorkgroupResource,
)
from capo_redshift_serverless._services._aws_config import aaws_config
from capo_redshift_serverless._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_redshift_serverless.types.amazon_resource_name
    import capo_redshift_serverless.types.association
    import capo_redshift_serverless.types.capacity
    import capo_redshift_serverless.types.catalog_name_string
    import capo_redshift_serverless.types.config_parameter_list
    import capo_redshift_serverless.types.convert_recovery_point_to_snapshot_request
    import capo_redshift_serverless.types.convert_recovery_point_to_snapshot_response
    import capo_redshift_serverless.types.create_custom_domain_association_request
    import capo_redshift_serverless.types.create_custom_domain_association_response
    import capo_redshift_serverless.types.create_endpoint_access_request
    import capo_redshift_serverless.types.create_endpoint_access_response
    import capo_redshift_serverless.types.create_namespace_request
    import capo_redshift_serverless.types.create_namespace_response
    import capo_redshift_serverless.types.create_reservation_request
    import capo_redshift_serverless.types.create_reservation_response
    import capo_redshift_serverless.types.create_scheduled_action_request
    import capo_redshift_serverless.types.create_scheduled_action_response
    import capo_redshift_serverless.types.create_snapshot_copy_configuration_request
    import capo_redshift_serverless.types.create_snapshot_copy_configuration_response
    import capo_redshift_serverless.types.create_snapshot_request
    import capo_redshift_serverless.types.create_snapshot_response
    import capo_redshift_serverless.types.create_usage_limit_request
    import capo_redshift_serverless.types.create_usage_limit_response
    import capo_redshift_serverless.types.create_workgroup_request
    import capo_redshift_serverless.types.create_workgroup_response
    import capo_redshift_serverless.types.custom_domain_certificate_arn_string
    import capo_redshift_serverless.types.custom_domain_name
    import capo_redshift_serverless.types.db_name
    import capo_redshift_serverless.types.db_password
    import capo_redshift_serverless.types.db_user
    import capo_redshift_serverless.types.delete_custom_domain_association_request
    import capo_redshift_serverless.types.delete_custom_domain_association_response
    import capo_redshift_serverless.types.delete_endpoint_access_request
    import capo_redshift_serverless.types.delete_endpoint_access_response
    import capo_redshift_serverless.types.delete_namespace_request
    import capo_redshift_serverless.types.delete_namespace_response
    import capo_redshift_serverless.types.delete_resource_policy_request
    import capo_redshift_serverless.types.delete_resource_policy_response
    import capo_redshift_serverless.types.delete_scheduled_action_request
    import capo_redshift_serverless.types.delete_scheduled_action_response
    import capo_redshift_serverless.types.delete_snapshot_copy_configuration_request
    import capo_redshift_serverless.types.delete_snapshot_copy_configuration_response
    import capo_redshift_serverless.types.delete_snapshot_request
    import capo_redshift_serverless.types.delete_snapshot_response
    import capo_redshift_serverless.types.delete_usage_limit_request
    import capo_redshift_serverless.types.delete_usage_limit_response
    import capo_redshift_serverless.types.delete_workgroup_request
    import capo_redshift_serverless.types.delete_workgroup_response
    import capo_redshift_serverless.types.endpoint_access
    import capo_redshift_serverless.types.get_credentials_request
    import capo_redshift_serverless.types.get_credentials_response
    import capo_redshift_serverless.types.get_custom_domain_association_request
    import capo_redshift_serverless.types.get_custom_domain_association_response
    import capo_redshift_serverless.types.get_endpoint_access_request
    import capo_redshift_serverless.types.get_endpoint_access_response
    import capo_redshift_serverless.types.get_identity_center_auth_token_request
    import capo_redshift_serverless.types.get_identity_center_auth_token_response
    import capo_redshift_serverless.types.get_namespace_request
    import capo_redshift_serverless.types.get_namespace_response
    import capo_redshift_serverless.types.get_recovery_point_request
    import capo_redshift_serverless.types.get_recovery_point_response
    import capo_redshift_serverless.types.get_reservation_offering_request
    import capo_redshift_serverless.types.get_reservation_offering_response
    import capo_redshift_serverless.types.get_reservation_request
    import capo_redshift_serverless.types.get_reservation_response
    import capo_redshift_serverless.types.get_resource_policy_request
    import capo_redshift_serverless.types.get_resource_policy_response
    import capo_redshift_serverless.types.get_scheduled_action_request
    import capo_redshift_serverless.types.get_scheduled_action_response
    import capo_redshift_serverless.types.get_snapshot_request
    import capo_redshift_serverless.types.get_snapshot_response
    import capo_redshift_serverless.types.get_table_restore_status_request
    import capo_redshift_serverless.types.get_table_restore_status_response
    import capo_redshift_serverless.types.get_track_request
    import capo_redshift_serverless.types.get_track_response
    import capo_redshift_serverless.types.get_usage_limit_request
    import capo_redshift_serverless.types.get_usage_limit_response
    import capo_redshift_serverless.types.get_workgroup_request
    import capo_redshift_serverless.types.get_workgroup_response
    import capo_redshift_serverless.types.iam_role_arn
    import capo_redshift_serverless.types.iam_role_arn_list
    import capo_redshift_serverless.types.ip_address_type
    import capo_redshift_serverless.types.kms_key_id
    import capo_redshift_serverless.types.lakehouse_idc_registration
    import capo_redshift_serverless.types.lakehouse_registration
    import capo_redshift_serverless.types.list_custom_domain_associations_request
    import capo_redshift_serverless.types.list_custom_domain_associations_response
    import capo_redshift_serverless.types.list_endpoint_access_request
    import capo_redshift_serverless.types.list_endpoint_access_response
    import capo_redshift_serverless.types.list_managed_workgroups_request
    import capo_redshift_serverless.types.list_managed_workgroups_response
    import capo_redshift_serverless.types.list_namespaces_request
    import capo_redshift_serverless.types.list_namespaces_response
    import capo_redshift_serverless.types.list_recovery_points_request
    import capo_redshift_serverless.types.list_recovery_points_response
    import capo_redshift_serverless.types.list_reservation_offerings_request
    import capo_redshift_serverless.types.list_reservation_offerings_response
    import capo_redshift_serverless.types.list_reservations_request
    import capo_redshift_serverless.types.list_reservations_response
    import capo_redshift_serverless.types.list_scheduled_actions_request
    import capo_redshift_serverless.types.list_scheduled_actions_response
    import capo_redshift_serverless.types.list_snapshot_copy_configurations_request
    import capo_redshift_serverless.types.list_snapshot_copy_configurations_response
    import capo_redshift_serverless.types.list_snapshots_request
    import capo_redshift_serverless.types.list_snapshots_response
    import capo_redshift_serverless.types.list_table_restore_status_request
    import capo_redshift_serverless.types.list_table_restore_status_response
    import capo_redshift_serverless.types.list_tags_for_resource_request
    import capo_redshift_serverless.types.list_tags_for_resource_response
    import capo_redshift_serverless.types.list_tracks_request
    import capo_redshift_serverless.types.list_tracks_response
    import capo_redshift_serverless.types.list_usage_limits_request
    import capo_redshift_serverless.types.list_usage_limits_response
    import capo_redshift_serverless.types.list_workgroups_request
    import capo_redshift_serverless.types.list_workgroups_response
    import capo_redshift_serverless.types.log_destination_type
    import capo_redshift_serverless.types.log_export_list
    import capo_redshift_serverless.types.managed_workgroup_list_item
    import capo_redshift_serverless.types.namespace
    import capo_redshift_serverless.types.namespace_name
    import capo_redshift_serverless.types.offering_id
    import capo_redshift_serverless.types.owner_account
    import capo_redshift_serverless.types.pagination_token
    import capo_redshift_serverless.types.performance_target
    import capo_redshift_serverless.types.put_resource_policy_request
    import capo_redshift_serverless.types.put_resource_policy_response
    import capo_redshift_serverless.types.recovery_point
    import capo_redshift_serverless.types.redshift_idc_application_arn
    import capo_redshift_serverless.types.reservation
    import capo_redshift_serverless.types.reservation_id
    import capo_redshift_serverless.types.reservation_offering
    import capo_redshift_serverless.types.restore_from_recovery_point_request
    import capo_redshift_serverless.types.restore_from_recovery_point_response
    import capo_redshift_serverless.types.restore_from_snapshot_request
    import capo_redshift_serverless.types.restore_from_snapshot_response
    import capo_redshift_serverless.types.restore_table_from_recovery_point_request
    import capo_redshift_serverless.types.restore_table_from_recovery_point_response
    import capo_redshift_serverless.types.restore_table_from_snapshot_request
    import capo_redshift_serverless.types.restore_table_from_snapshot_response
    import capo_redshift_serverless.types.s3_table_action
    import capo_redshift_serverless.types.s3_table_granularity
    import capo_redshift_serverless.types.s3_table_name_list
    import capo_redshift_serverless.types.schedule
    import capo_redshift_serverless.types.scheduled_action_association
    import capo_redshift_serverless.types.scheduled_action_name
    import capo_redshift_serverless.types.security_group_id_list
    import capo_redshift_serverless.types.serverless_track
    import capo_redshift_serverless.types.snapshot
    import capo_redshift_serverless.types.snapshot_copy_configuration
    import capo_redshift_serverless.types.source_arn
    import capo_redshift_serverless.types.subnet_id_list
    import capo_redshift_serverless.types.table_restore_status
    import capo_redshift_serverless.types.tag_key_list
    import capo_redshift_serverless.types.tag_list
    import capo_redshift_serverless.types.tag_resource_request
    import capo_redshift_serverless.types.tag_resource_response
    import capo_redshift_serverless.types.target_action
    import capo_redshift_serverless.types.track_name
    import capo_redshift_serverless.types.untag_resource_request
    import capo_redshift_serverless.types.untag_resource_response
    import capo_redshift_serverless.types.update_custom_domain_association_request
    import capo_redshift_serverless.types.update_custom_domain_association_response
    import capo_redshift_serverless.types.update_endpoint_access_request
    import capo_redshift_serverless.types.update_endpoint_access_response
    import capo_redshift_serverless.types.update_lakehouse_configuration_request
    import capo_redshift_serverless.types.update_lakehouse_configuration_response
    import capo_redshift_serverless.types.update_namespace_request
    import capo_redshift_serverless.types.update_namespace_response
    import capo_redshift_serverless.types.update_scheduled_action_request
    import capo_redshift_serverless.types.update_scheduled_action_response
    import capo_redshift_serverless.types.update_snapshot_copy_configuration_request
    import capo_redshift_serverless.types.update_snapshot_copy_configuration_response
    import capo_redshift_serverless.types.update_snapshot_request
    import capo_redshift_serverless.types.update_snapshot_response
    import capo_redshift_serverless.types.update_usage_limit_request
    import capo_redshift_serverless.types.update_usage_limit_response
    import capo_redshift_serverless.types.update_workgroup_request
    import capo_redshift_serverless.types.update_workgroup_response
    import capo_redshift_serverless.types.usage_limit
    import capo_redshift_serverless.types.usage_limit_breach_action
    import capo_redshift_serverless.types.usage_limit_period
    import capo_redshift_serverless.types.usage_limit_usage_type
    import capo_redshift_serverless.types.vpc_security_group_id_list
    import capo_redshift_serverless.types.workgroup
    import capo_redshift_serverless.types.workgroup_name
    import capo_redshift_serverless.types.workgroup_name_list


class AsyncRedshiftServerlessClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncRedshiftServerlessClient:
    """A client for the ``RedshiftServerless`` service.

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
        self._config = AsyncRedshiftServerlessClientConfig(
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
        self.cross_vpc_endpoint_resource = AsyncCrossVpcEndpointResource(self)
        self.managed_workgroup_resource = AsyncManagedWorkgroupResource(self)
        self.namespace_resource = AsyncNamespaceResource(self)
        self.recovery_point_resource = AsyncRecoveryPointResource(self)
        self.reservation_resource = AsyncReservationResource(self)
        self.scheduled_action_resource = AsyncScheduledActionResource(self)
        self.snapshot_resource = AsyncSnapshotResource(self)
        self.usage_limit_resource = AsyncUsageLimitResource(self)
        self.workgroup_resource = AsyncWorkgroupResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRedshiftServerlessClientConfig = config_overrides or {}
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

    async def create_custom_domain_association(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        custom_domain_name: "capo_redshift_serverless.types.custom_domain_name.CustomDomainName",
        custom_domain_certificate_arn: "capo_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.create_custom_domain_association_response.CreateCustomDomainAssociationResponse":
        """<p>Creates a custom domain association for Amazon Redshift Serverless.</p>

        Args:
            workgroup_name: <p>The name of the workgroup associated with the database.</p>
            custom_domain_name: <p>The custom domain name to associate with the workgroup.</p>
            custom_domain_certificate_arn: <p>The custom domain name’s certificate Amazon resource name (ARN).</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_custom_domain_association_request.CreateCustomDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_custom_domain_association_response.CreateCustomDomainAssociationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_custom_domain_association

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_custom_domain_association.async_create_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_custom_domain_association_request.CreateCustomDomainAssociationRequest = {
            "workgroup_name": workgroup_name,
            "custom_domain_name": custom_domain_name,
            "custom_domain_certificate_arn": custom_domain_certificate_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_domain_association(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        custom_domain_name: "capo_redshift_serverless.types.custom_domain_name.CustomDomainName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_custom_domain_association_response.DeleteCustomDomainAssociationResponse":
        """<p>Deletes a custom domain association for Amazon Redshift Serverless.</p>

        Args:
            workgroup_name: <p>The name of the workgroup associated with the database.</p>
            custom_domain_name: <p>The custom domain name associated with the workgroup.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_custom_domain_association_request.DeleteCustomDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_custom_domain_association_response.DeleteCustomDomainAssociationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_custom_domain_association

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_custom_domain_association.async_delete_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_custom_domain_association_request.DeleteCustomDomainAssociationRequest = {
            "workgroup_name": workgroup_name,
            "custom_domain_name": custom_domain_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes the specified resource policy.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the policy to delete.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_credentials(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        db_name: Optional["capo_redshift_serverless.types.db_name.DbName"] = None,
        duration_seconds: Optional[int] = None,
        workgroup_name: Optional[
            "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
        ] = None,
        custom_domain_name: Optional[
            "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
        ] = None,
    ) -> (
        "capo_redshift_serverless.types.get_credentials_response.GetCredentialsResponse"
    ):
        """<p>Returns a database user name and temporary password with temporary authorization to log in to Amazon Redshift Serverless.</p> <p>By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes).</p> <p>The Identity and Access Management (IAM) user or role that runs GetCredentials must have an IAM policy attached that allows access to all necessary actions and resources.</p> <p>If the <code>DbName</code> parameter is specified, the IAM policy must allow access to the resource dbname for the specified database name.</p>

        Args:
            db_name: <p>The name of the database to get temporary authorization to log on to.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 64 alphanumeric characters or hyphens.</p> </li> <li> <p>Must contain only uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Must not contain a colon ( : ) or slash ( / ).</p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html">Reserved Words </a> in the Amazon Redshift Database Developer Guide</p> </li> </ul>
            duration_seconds: <p>The number of seconds until the returned temporary password expires. The minimum is 900 seconds, and the maximum is 3600 seconds.</p>
            workgroup_name: <p>The name of the workgroup associated with the database.</p>
            custom_domain_name: <p>The custom domain name associated with the workgroup. The custom domain name or the workgroup name must be included in the request.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_credentials_request.GetCredentialsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_credentials_response.GetCredentialsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_credentials

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_credentials.async_get_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_credentials_request.GetCredentialsRequest = {}
        if db_name is not None:
            input_["db_name"] = db_name
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_custom_domain_association(
        self,
        custom_domain_name: "capo_redshift_serverless.types.custom_domain_name.CustomDomainName",
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_custom_domain_association_response.GetCustomDomainAssociationResponse":
        """<p>Gets information about a specific custom domain association.</p>

        Args:
            custom_domain_name: <p>The custom domain name associated with the workgroup.</p>
            workgroup_name: <p>The name of the workgroup associated with the database.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_custom_domain_association_request.GetCustomDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_custom_domain_association_response.GetCustomDomainAssociationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_custom_domain_association

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_custom_domain_association.async_get_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_custom_domain_association_request.GetCustomDomainAssociationRequest = {
            "custom_domain_name": custom_domain_name,
            "workgroup_name": workgroup_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_identity_center_auth_token(
        self,
        workgroup_names: "capo_redshift_serverless.types.workgroup_name_list.WorkgroupNameList",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_identity_center_auth_token_response.GetIdentityCenterAuthTokenResponse":
        """<p>Returns an Identity Center authentication token for accessing Amazon Redshift Serverless workgroups.</p> <p>The token provides secure access to data within the specified workgroups using Identity Center identity propagation. The token expires after a specified duration and must be refreshed for continued access.</p> <p>The Identity and Access Management (IAM) user or role that runs GetIdentityCenterAuthToken must have appropriate permissions to access the specified workgroups and Identity Center integration must be configured for the workgroups.</p>

        Args:
            workgroup_names: <p>A list of workgroup names for which to generate the Identity Center authentication token.</p> <p>Constraints:</p> <ul> <li> <p>Must contain between 1 and 20 workgroup names.</p> </li> <li> <p>Each workgroup name must be a valid Amazon Redshift Serverless workgroup identifier.</p> </li> <li> <p>All specified workgroups must have Identity Center integration enabled.</p> </li> </ul>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.dry_run_exception.DryRunException: <p>This exception is thrown when the request was successful, but dry run was enabled so no action was taken.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_identity_center_auth_token_request.GetIdentityCenterAuthTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_identity_center_auth_token_response.GetIdentityCenterAuthTokenResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_identity_center_auth_token

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_identity_center_auth_token.async_get_identity_center_auth_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_identity_center_auth_token_request.GetIdentityCenterAuthTokenRequest = {
            "workgroup_names": workgroup_names
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Returns a resource policy.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to return.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_track(
        self,
        track_name: "capo_redshift_serverless.types.track_name.TrackName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_track_response.GetTrackResponse":
        """<p>Get the Redshift Serverless version for a specified track.</p>

        Args:
            track_name: <p>The name of the track of which its version is fetched.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.dry_run_exception.DryRunException: <p>This exception is thrown when the request was successful, but dry run was enabled so no action was taken.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_track_request.GetTrackRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_track_response.GetTrackResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_track

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_track.async_get_track(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_track_request.GetTrackRequest = {
            "track_name": track_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_custom_domain_associations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        custom_domain_name: Optional[
            "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
        ] = None,
        custom_domain_certificate_arn: Optional[
            "capo_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
        ] = None,
    ) -> "capo_redshift_serverless.types.list_custom_domain_associations_response.ListCustomDomainAssociationsResponse":
        """<p> Lists custom domain associations for Amazon Redshift Serverless.</p>

        Args:
            next_token: <p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            custom_domain_name: <p>The custom domain name associated with the workgroup.</p>
            custom_domain_certificate_arn: <p>The custom domain name’s certificate Amazon resource name (ARN).</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.invalid_pagination_exception.InvalidPaginationException: <p>The provided pagination token is invalid.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_custom_domain_associations_request.ListCustomDomainAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_custom_domain_associations_response.ListCustomDomainAssociationsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_custom_domain_associations

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_custom_domain_associations.async_list_custom_domain_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_custom_domain_associations_request.ListCustomDomainAssociationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if custom_domain_certificate_arn is not None:
            input_["custom_domain_certificate_arn"] = custom_domain_certificate_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_custom_domain_associations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        custom_domain_name: Optional[
            "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
        ] = None,
        custom_domain_certificate_arn: Optional[
            "capo_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
        ] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.association.Association]":
        _token = next_token
        while True:
            _response = await self.list_custom_domain_associations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                custom_domain_name=custom_domain_name,
                custom_domain_certificate_arn=custom_domain_certificate_arn,
            )
            _page = _resolve_path(_response, ("associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_redshift_serverless.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags assigned to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tracks(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_tracks_response.ListTracksResponse":
        """<p>List the Amazon Redshift Serverless versions.</p>

        Args:
            next_token: <p>If your initial <code>ListTracksRequest</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListTracksRequest</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.invalid_pagination_exception.InvalidPaginationException: <p>The provided pagination token is invalid.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_tracks_request.ListTracksRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_tracks_response.ListTracksResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_tracks

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_tracks.async_list_tracks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_tracks_request.ListTracksRequest = {}
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

    async def iter_list_tracks(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> (
        "AsyncIterator[capo_redshift_serverless.types.serverless_track.ServerlessTrack]"
    ):
        _token = next_token
        while True:
            _response = await self.list_tracks(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tracks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_resource_policy(
        self,
        resource_arn: str,
        policy: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.put_resource_policy_response.PutResourcePolicyResponse":
        r"""<p>Creates or updates a resource policy. Currently, you can use policies to share snapshots across Amazon Web Services accounts.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the account to create or update a resource policy for.</p>
            policy: <p>The policy to create or update. For example, the following policy grants a user authorization to restore a snapshot.</p> <p> <code>"{\"Version\": \"2012-10-17\", \"Statement\" : [{ \"Sid\": \"AllowUserRestoreFromSnapshot\", \"Principal\":{\"AWS\": [\"739247239426\"]}, \"Action\": [\"redshift-serverless:RestoreFromSnapshot\"] , \"Effect\": \"Allow\" }]}"</code> </p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
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
        resource_arn: "capo_redshift_serverless.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_redshift_serverless.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>The map of the key-value pairs used to tag the resource.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.tag_resource

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_redshift_serverless.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_redshift_serverless.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag or set of tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The tag or set of tags to remove from the resource.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.untag_resource

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_custom_domain_association(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        custom_domain_name: "capo_redshift_serverless.types.custom_domain_name.CustomDomainName",
        custom_domain_certificate_arn: "capo_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.update_custom_domain_association_response.UpdateCustomDomainAssociationResponse":
        """<p>Updates an Amazon Redshift Serverless certificate associated with a custom domain.</p>

        Args:
            workgroup_name: <p>The name of the workgroup associated with the database.</p>
            custom_domain_name: <p>The custom domain name associated with the workgroup.</p>
            custom_domain_certificate_arn: <p>The custom domain name’s certificate Amazon resource name (ARN). This is optional.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_custom_domain_association_request.UpdateCustomDomainAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_custom_domain_association_response.UpdateCustomDomainAssociationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_custom_domain_association

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_custom_domain_association.async_update_custom_domain_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_custom_domain_association_request.UpdateCustomDomainAssociationRequest = {
            "workgroup_name": workgroup_name,
            "custom_domain_name": custom_domain_name,
            "custom_domain_certificate_arn": custom_domain_certificate_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_endpoint_access(
        self,
        endpoint_name: str,
        subnet_ids: "capo_redshift_serverless.types.subnet_id_list.SubnetIdList",
        workgroup_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "capo_redshift_serverless.types.create_endpoint_access_response.CreateEndpointAccessResponse":
        """<p>Creates an Amazon Redshift Serverless managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint. An endpoint name must contain 1-30 characters. Valid characters are A-Z, a-z, 0-9, and hyphen(-). The first character must be a letter. The name can't contain two consecutive hyphens or end with a hyphen.</p>
            subnet_ids: <p>The unique identifers of subnets from which Amazon Redshift Serverless chooses one to deploy a VPC endpoint.</p>
            workgroup_name: <p>The name of the workgroup to associate with the VPC endpoint.</p>
            vpc_security_group_ids: <p>The unique identifiers of the security group that defines the ports, protocols, and sources for inbound traffic that you are authorizing into your endpoint.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_endpoint_access_request.CreateEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_endpoint_access_response.CreateEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_endpoint_access.async_create_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_endpoint_access_request.CreateEndpointAccessRequest = {
            "endpoint_name": endpoint_name,
            "subnet_ids": subnet_ids,
            "workgroup_name": workgroup_name,
        }
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_endpoint_access_response.DeleteEndpointAccessResponse":
        """<p>Deletes an Amazon Redshift Serverless managed VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to delete.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_endpoint_access_request.DeleteEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_endpoint_access_response.DeleteEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_endpoint_access.async_delete_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_endpoint_access_request.DeleteEndpointAccessRequest = {
            "endpoint_name": endpoint_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_endpoint_access_response.GetEndpointAccessResponse":
        """<p>Returns information, such as the name, about a VPC endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to return information for.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_endpoint_access_request.GetEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_endpoint_access_response.GetEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_endpoint_access.async_get_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_endpoint_access_request.GetEndpointAccessRequest = {
            "endpoint_name": endpoint_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        workgroup_name: Optional[str] = None,
        vpc_id: Optional[str] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "capo_redshift_serverless.types.list_endpoint_access_response.ListEndpointAccessResponse":
        """<p>Returns an array of <code>EndpointAccess</code> objects and relevant information.</p>

        Args:
            next_token: <p>If your initial <code>ListEndpointAccess</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListEndpointAccess</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            workgroup_name: <p>The name of the workgroup associated with the VPC endpoint to return.</p>
            vpc_id: <p>The unique identifier of the virtual private cloud with access to Amazon Redshift Serverless.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_endpoint_access_request.ListEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_endpoint_access_response.ListEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_endpoint_access.async_list_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_endpoint_access_request.ListEndpointAccessRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_endpoint_access(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        workgroup_name: Optional[str] = None,
        vpc_id: Optional[str] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.endpoint_access.EndpointAccess]":
        _token = next_token
        while True:
            _response = await self.list_endpoint_access(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                workgroup_name=workgroup_name,
                vpc_id=vpc_id,
                owner_account=owner_account,
            )
            _page = _resolve_path(_response, ("endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_endpoint_access(
        self,
        endpoint_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        vpc_security_group_ids: Optional[
            "capo_redshift_serverless.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
    ) -> "capo_redshift_serverless.types.update_endpoint_access_response.UpdateEndpointAccessResponse":
        """<p>Updates an Amazon Redshift Serverless managed endpoint.</p>

        Args:
            endpoint_name: <p>The name of the VPC endpoint to update.</p>
            vpc_security_group_ids: <p>The list of VPC security groups associated with the endpoint after the endpoint is modified.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_endpoint_access_request.UpdateEndpointAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_endpoint_access_response.UpdateEndpointAccessResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_endpoint_access

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_endpoint_access.async_update_endpoint_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_endpoint_access_request.UpdateEndpointAccessRequest = {
            "endpoint_name": endpoint_name
        }
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_workgroups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        source_arn: Optional[
            "capo_redshift_serverless.types.source_arn.SourceArn"
        ] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_managed_workgroups_response.ListManagedWorkgroupsResponse":
        """<p>Returns information about a list of specified managed workgroups in your account.</p>

        Args:
            source_arn: <p>The Amazon Resource Name (ARN) for the managed workgroup in the Glue Data Catalog.</p>
            next_token: <p>If your initial ListManagedWorkgroups operation returns a nextToken, you can include the returned nextToken in following ListManagedWorkgroups operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_managed_workgroups_request.ListManagedWorkgroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_managed_workgroups_response.ListManagedWorkgroupsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_managed_workgroups

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_managed_workgroups.async_list_managed_workgroups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_managed_workgroups_request.ListManagedWorkgroupsRequest = {}
        if source_arn is not None:
            input_["source_arn"] = source_arn
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

    async def iter_list_managed_workgroups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        source_arn: Optional[
            "capo_redshift_serverless.types.source_arn.SourceArn"
        ] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.managed_workgroup_list_item.ManagedWorkgroupListItem]":
        _token = next_token
        while True:
            _response = await self.list_managed_workgroups(
                config_overrides=config_overrides,
                source_arn=source_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("managed_workgroups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_namespace(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        admin_username: Optional[
            "capo_redshift_serverless.types.db_user.DbUser"
        ] = None,
        admin_user_password: Optional[
            "capo_redshift_serverless.types.db_password.DbPassword"
        ] = None,
        db_name: Optional[str] = None,
        kms_key_id: Optional[str] = None,
        default_iam_role_arn: Optional[str] = None,
        iam_roles: Optional[
            "capo_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        log_exports: Optional[
            "capo_redshift_serverless.types.log_export_list.LogExportList"
        ] = None,
        tags: Optional["capo_redshift_serverless.types.tag_list.TagList"] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        redshift_idc_application_arn: Optional[
            "capo_redshift_serverless.types.redshift_idc_application_arn.RedshiftIdcApplicationArn"
        ] = None,
    ) -> "capo_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse":
        """<p>Creates a namespace in Amazon Redshift Serverless.</p>

        Args:
            namespace_name: <p>The name of the namespace.</p>
            admin_username: <p>The username of the administrator for the first database created in the namespace.</p>
            admin_user_password: <p>The password of the administrator for the first database created in the namespace.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p>
            db_name: <p>The name of the first database created in the namespace.</p>
            kms_key_id: <p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.</p>
            iam_roles: <p>A list of IAM roles to associate with the namespace.</p>
            log_exports: <p>The types of logs the namespace can export. Available export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>
            tags: <p>A list of tag instances.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>
            redshift_idc_application_arn: <p>The ARN for the Redshift application that integrates with IAM Identity Center.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_namespace_response.CreateNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_namespace

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_namespace.async_create_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_namespace_request.CreateNamespaceRequest = {
            "namespace_name": namespace_name
        }
        if admin_username is not None:
            input_["admin_username"] = admin_username
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if db_name is not None:
            input_["db_name"] = db_name
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if log_exports is not None:
            input_["log_exports"] = log_exports
        if tags is not None:
            input_["tags"] = tags
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )
        if redshift_idc_application_arn is not None:
            input_["redshift_idc_application_arn"] = redshift_idc_application_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_namespace(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_namespace_response.GetNamespaceResponse":
        """<p>Returns information about a namespace in Amazon Redshift Serverless.</p>

        Args:
            namespace_name: <p>The name of the namespace to retrieve information for.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_namespace_request.GetNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_namespace_response.GetNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_namespace

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_namespace.async_get_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_namespace_request.GetNamespaceRequest = {
            "namespace_name": namespace_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_namespace(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        admin_user_password: Optional[
            "capo_redshift_serverless.types.db_password.DbPassword"
        ] = None,
        admin_username: Optional[
            "capo_redshift_serverless.types.db_user.DbUser"
        ] = None,
        kms_key_id: Optional[str] = None,
        default_iam_role_arn: Optional[str] = None,
        iam_roles: Optional[
            "capo_redshift_serverless.types.iam_role_arn_list.IamRoleArnList"
        ] = None,
        log_exports: Optional[
            "capo_redshift_serverless.types.log_export_list.LogExportList"
        ] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        log_destination_type: Optional[
            "capo_redshift_serverless.types.log_destination_type.LogDestinationType"
        ] = None,
        s3_table_action: Optional[
            "capo_redshift_serverless.types.s3_table_action.S3TableAction"
        ] = None,
        s3_table_names: Optional[
            "capo_redshift_serverless.types.s3_table_name_list.S3TableNameList"
        ] = None,
        s3_table_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        s3_table_granularity: Optional[
            "capo_redshift_serverless.types.s3_table_granularity.S3TableGranularity"
        ] = None,
    ) -> "capo_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse":
        """<p>Updates a namespace with the specified settings. Unless required, you can't update multiple parameters in one request. For example, you must specify both <code>adminUsername</code> and <code>adminUserPassword</code> to update either field, but you can't update both <code>kmsKeyId</code> and <code>logExports</code> in a single request.</p> <p>Similarly, an S3 Tables log-publishing update (a request where <code>logDestinationType</code> is <code>s3table</code>) cannot be combined with any other namespace configuration change and must be submitted as its own request.</p>

        Args:
            namespace_name: <p>The name of the namespace to update. You can't update the name of a namespace once it is created.</p>
            admin_user_password: <p>The password of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUsername</code>.</p> <p>You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. </p> <p>If your admin user account is locked, this operation also unlocks your account and resets the failed-login counter. This option is available only when account lockout security is enabled for the namespace.</p>
            admin_username: <p>The username of the administrator for the first database created in the namespace. This parameter must be updated together with <code>adminUserPassword</code>.</p>
            kms_key_id: <p>The ID of the Amazon Web Services Key Management Service key used to encrypt your data.</p>
            default_iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace. This parameter must be updated together with <code>iamRoles</code>.</p>
            iam_roles: <p>A list of IAM roles to associate with the namespace. This parameter must be updated together with <code>defaultIamRoleArn</code>.</p>
            log_exports: <p>The types of logs the namespace can export. The export types are <code>userlog</code>, <code>connectionlog</code>, and <code>useractivitylog</code>.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the namespace's admin credentials. You can't use <code>adminUserPassword</code> if <code>manageAdminPassword</code> is true. If <code>manageAdminPassword</code> is false or not set, Amazon Redshift uses <code>adminUserPassword</code> for the admin user account's password. </p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if <code>manageAdminPassword</code> is true.</p>
            log_destination_type: <p>The destination for the log data. Valid values are <code>s3table</code> and <code>cloudwatch</code>.</p> <p>Set this to <code>s3table</code> to manage Amazon S3 Tables system-table publishing for the namespace.</p>
            s3_table_action: <p>Whether to enable or disable Amazon S3 Tables publishing. Valid values are <code>Enable</code> and <code>Disable</code>, matched case-insensitively.</p> <p>When omitted, defaults to <code>Enable</code>. Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>
            s3_table_names: <p>The system tables to publish (on enable) or to stop publishing (on disable). Each value is either a system table view name that begins with <code>sys_</code> or the keyword <code>all</code>.</p> <p>Omitting this parameter, passing an empty list, or including <code>all</code> each select every current and future system table. Each name must be 1-128 characters, and the list can contain up to 256 names.</p> <p>Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>
            s3_table_kms_key_id: <p>The identifier of the Key Management Service key used to encrypt the published Amazon S3 Tables data. When omitted, the data is encrypted with SSE-S3 (Amazon S3 managed keys).</p> <p>Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>
            s3_table_granularity: <p>The scope of the Amazon S3 Tables destination. Valid values are <code>namespace</code> and <code>account</code>, matched case-insensitively. <code>namespace</code> scopes the published tables to this namespace; <code>account</code> scopes them to the Amazon Web Services account.</p> <p>Required when enabling. Omitting this parameter or passing a blank value fails with <code>ValidationException</code>. Valid only when <code>logDestinationType</code> is <code>s3table</code>.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_namespace_response.UpdateNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_namespace

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_namespace.async_update_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_namespace_request.UpdateNamespaceRequest = {
            "namespace_name": namespace_name
        }
        if admin_user_password is not None:
            input_["admin_user_password"] = admin_user_password
        if admin_username is not None:
            input_["admin_username"] = admin_username
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if default_iam_role_arn is not None:
            input_["default_iam_role_arn"] = default_iam_role_arn
        if iam_roles is not None:
            input_["iam_roles"] = iam_roles
        if log_exports is not None:
            input_["log_exports"] = log_exports
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )
        if log_destination_type is not None:
            input_["log_destination_type"] = log_destination_type
        if s3_table_action is not None:
            input_["s3_table_action"] = s3_table_action
        if s3_table_names is not None:
            input_["s3_table_names"] = s3_table_names
        if s3_table_kms_key_id is not None:
            input_["s3_table_kms_key_id"] = s3_table_kms_key_id
        if s3_table_granularity is not None:
            input_["s3_table_granularity"] = s3_table_granularity

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_namespace(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        final_snapshot_name: Optional[str] = None,
        final_snapshot_retention_period: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse":
        """<p>Deletes a namespace from Amazon Redshift Serverless. Before you delete the namespace, you can create a final snapshot that has all of the data within the namespace.</p>

        Args:
            namespace_name: <p>The name of the namespace to delete.</p>
            final_snapshot_name: <p>The name of the snapshot to be created before the namespace is deleted.</p>
            final_snapshot_retention_period: <p>How long to retain the final snapshot.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_namespace_request.DeleteNamespaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_namespace_response.DeleteNamespaceResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_namespace

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_namespace.async_delete_namespace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_namespace_request.DeleteNamespaceRequest = {
            "namespace_name": namespace_name
        }
        if final_snapshot_name is not None:
            input_["final_snapshot_name"] = final_snapshot_name
        if final_snapshot_retention_period is not None:
            input_["final_snapshot_retention_period"] = final_snapshot_retention_period

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_namespaces(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "capo_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse"
    ):
        """<p>Returns information about a list of specified namespaces.</p>

        Args:
            next_token: <p>If your initial <code>ListNamespaces</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListNamespaces</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_namespaces_request.ListNamespacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_namespaces_response.ListNamespacesResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_namespaces

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_namespaces.async_list_namespaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_namespaces_request.ListNamespacesRequest = {}
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

    async def iter_list_namespaces(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.namespace.Namespace]":
        _token = next_token
        while True:
            _response = await self.list_namespaces(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("namespaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_lakehouse_configuration(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        lakehouse_registration: Optional[
            "capo_redshift_serverless.types.lakehouse_registration.LakehouseRegistration"
        ] = None,
        catalog_name: Optional[
            "capo_redshift_serverless.types.catalog_name_string.CatalogNameString"
        ] = None,
        lakehouse_idc_registration: Optional[
            "capo_redshift_serverless.types.lakehouse_idc_registration.LakehouseIdcRegistration"
        ] = None,
        lakehouse_idc_application_arn: Optional[str] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.update_lakehouse_configuration_response.UpdateLakehouseConfigurationResponse":
        """<p>Modifies the lakehouse configuration for a namespace. This operation allows you to manage Amazon Redshift federated permissions and Amazon Web Services IAM Identity Center trusted identity propagation.</p>

        Args:
            namespace_name: <p>The name of the namespace whose lakehouse configuration you want to modify.</p>
            lakehouse_registration: <p>Specifies whether to register or deregister the namespace with Amazon Redshift federated permissions. Valid values are <code>Register</code> or <code>Deregister</code>.</p>
            catalog_name: <p>The name of the Glue Data Catalog that will be associated with the namespace enabled with Amazon Redshift federated permissions.</p> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p>
            lakehouse_idc_registration: <p>Modifies the Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions. Valid values are <code>Associate</code> or <code>Disassociate</code>.</p>
            lakehouse_idc_application_arn: <p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a namespace enabled with Amazon Redshift federated permissions.</p>
            dry_run: <p>A boolean value that, if <code>true</code>, validates the request without actually updating the lakehouse configuration. Use this to check for errors before making changes.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.dry_run_exception.DryRunException: <p>This exception is thrown when the request was successful, but dry run was enabled so no action was taken.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_lakehouse_configuration_request.UpdateLakehouseConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_lakehouse_configuration_response.UpdateLakehouseConfigurationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_lakehouse_configuration

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_lakehouse_configuration.async_update_lakehouse_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_lakehouse_configuration_request.UpdateLakehouseConfigurationRequest = {
            "namespace_name": namespace_name
        }
        if lakehouse_registration is not None:
            input_["lakehouse_registration"] = lakehouse_registration
        if catalog_name is not None:
            input_["catalog_name"] = catalog_name
        if lakehouse_idc_registration is not None:
            input_["lakehouse_idc_registration"] = lakehouse_idc_registration
        if lakehouse_idc_application_arn is not None:
            input_["lakehouse_idc_application_arn"] = lakehouse_idc_application_arn
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def convert_recovery_point_to_snapshot(
        self,
        recovery_point_id: str,
        snapshot_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        retention_period: Optional[int] = None,
        tags: Optional["capo_redshift_serverless.types.tag_list.TagList"] = None,
    ) -> "capo_redshift_serverless.types.convert_recovery_point_to_snapshot_response.ConvertRecoveryPointToSnapshotResponse":
        """<p>Converts a recovery point to a snapshot. For more information about recovery points and snapshots, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery-points.html">Working with snapshots and recovery points</a>.</p>

        Args:
            recovery_point_id: <p>The unique identifier of the recovery point.</p>
            snapshot_name: <p>The name of the snapshot.</p>
            retention_period: <p>How long to retain the snapshot.</p>
            tags: <p>An array of <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html">Tag objects</a> to associate with the created snapshot.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.convert_recovery_point_to_snapshot_request.ConvertRecoveryPointToSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.convert_recovery_point_to_snapshot_response.ConvertRecoveryPointToSnapshotResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.convert_recovery_point_to_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.convert_recovery_point_to_snapshot.async_convert_recovery_point_to_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.convert_recovery_point_to_snapshot_request.ConvertRecoveryPointToSnapshotRequest = {
            "recovery_point_id": recovery_point_id,
            "snapshot_name": snapshot_name,
        }
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_recovery_point(
        self,
        recovery_point_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_recovery_point_response.GetRecoveryPointResponse":
        """<p>Returns information about a recovery point.</p>

        Args:
            recovery_point_id: <p>The unique identifier of the recovery point to return information for.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_recovery_point_request.GetRecoveryPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_recovery_point_response.GetRecoveryPointResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_recovery_point

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_recovery_point.async_get_recovery_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_recovery_point_request.GetRecoveryPointRequest = {
            "recovery_point_id": recovery_point_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_recovery_points(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        namespace_name: Optional[
            "capo_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
        namespace_arn: Optional[str] = None,
    ) -> "capo_redshift_serverless.types.list_recovery_points_response.ListRecoveryPointsResponse":
        """<p>Returns an array of recovery points.</p>

        Args:
            next_token: <p>If your initial <code>ListRecoveryPoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListRecoveryPoints</code> operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            start_time: <p>The time when the recovery point's creation was initiated.</p>
            end_time: <p>The time when creation of the recovery point finished.</p>
            namespace_name: <p>The name of the namespace to list recovery points for.</p>
            namespace_arn: <p>The Amazon Resource Name (ARN) of the namespace from which to list recovery points.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_recovery_points_request.ListRecoveryPointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_recovery_points_response.ListRecoveryPointsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_recovery_points

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_recovery_points.async_list_recovery_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_recovery_points_request.ListRecoveryPointsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
        if namespace_arn is not None:
            input_["namespace_arn"] = namespace_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_recovery_points(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        namespace_name: Optional[
            "capo_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
        namespace_arn: Optional[str] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.recovery_point.RecoveryPoint]":
        _token = next_token
        while True:
            _response = await self.list_recovery_points(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                start_time=start_time,
                end_time=end_time,
                namespace_name=namespace_name,
                namespace_arn=namespace_arn,
            )
            _page = _resolve_path(_response, ("recovery_points",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def restore_from_recovery_point(
        self,
        recovery_point_id: str,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        maintain_integration: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.restore_from_recovery_point_response.RestoreFromRecoveryPointResponse":
        """<p>Restore the data from a recovery point.</p>

        Args:
            recovery_point_id: <p>The unique identifier of the recovery point to restore from.</p>
            namespace_name: <p>The name of the namespace to restore data into.</p>
            workgroup_name: <p>The name of the workgroup used to restore data.</p>
            maintain_integration: <p>If <code>true</code>, maintain existing data sharing, zero-ETL and S3 event integrations when restoring. Otherwise, integrations will not be maintained after the restore operation. Integrations are only maintained when restored to the same serverless namespace.</p> <p>Default: true</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.restore_from_recovery_point_request.RestoreFromRecoveryPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.restore_from_recovery_point_response.RestoreFromRecoveryPointResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.restore_from_recovery_point

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.restore_from_recovery_point.async_restore_from_recovery_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.restore_from_recovery_point_request.RestoreFromRecoveryPointRequest = {
            "recovery_point_id": recovery_point_id,
            "namespace_name": namespace_name,
            "workgroup_name": workgroup_name,
        }
        if maintain_integration is not None:
            input_["maintain_integration"] = maintain_integration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_table_from_recovery_point(
        self,
        namespace_name: str,
        workgroup_name: str,
        recovery_point_id: str,
        source_database_name: str,
        source_table_name: str,
        new_table_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        source_schema_name: Optional[str] = None,
        target_database_name: Optional[str] = None,
        target_schema_name: Optional[str] = None,
        activate_case_sensitive_identifier: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.restore_table_from_recovery_point_response.RestoreTableFromRecoveryPointResponse":
        """<p>Restores a table from a recovery point to your Amazon Redshift Serverless instance. You can't use this operation to restore tables with interleaved sort keys.</p>

        Args:
            namespace_name: <p>Namespace of the recovery point to restore from.</p>
            workgroup_name: <p>The workgroup to restore the table to.</p>
            recovery_point_id: <p>The ID of the recovery point to restore the table from.</p>
            source_database_name: <p>The name of the source database that contains the table being restored.</p>
            source_schema_name: <p>The name of the source schema that contains the table being restored.</p>
            source_table_name: <p>The name of the source table being restored.</p>
            target_database_name: <p>The name of the database to restore the table to.</p>
            target_schema_name: <p>The name of the schema to restore the table to.</p>
            new_table_name: <p>The name of the table to create from the restore operation.</p>
            activate_case_sensitive_identifier: <p>Indicates whether name identifiers for database, schema, and table are case sensitive. If true, the names are case sensitive. If false, the names are not case sensitive. The default is false.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.restore_table_from_recovery_point_request.RestoreTableFromRecoveryPointRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.restore_table_from_recovery_point_response.RestoreTableFromRecoveryPointResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.restore_table_from_recovery_point

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.restore_table_from_recovery_point.async_restore_table_from_recovery_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.restore_table_from_recovery_point_request.RestoreTableFromRecoveryPointRequest = {
            "namespace_name": namespace_name,
            "workgroup_name": workgroup_name,
            "recovery_point_id": recovery_point_id,
            "source_database_name": source_database_name,
            "source_table_name": source_table_name,
            "new_table_name": new_table_name,
        }
        if source_schema_name is not None:
            input_["source_schema_name"] = source_schema_name
        if target_database_name is not None:
            input_["target_database_name"] = target_database_name
        if target_schema_name is not None:
            input_["target_schema_name"] = target_schema_name
        if activate_case_sensitive_identifier is not None:
            input_["activate_case_sensitive_identifier"] = (
                activate_case_sensitive_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_reservation(
        self,
        capacity: "capo_redshift_serverless.types.capacity.Capacity",
        offering_id: "capo_redshift_serverless.types.offering_id.OfferingId",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_redshift_serverless.types.create_reservation_response.CreateReservationResponse":
        """<p>Creates an Amazon Redshift Serverless reservation, which gives you the option to commit to a specified number of Redshift Processing Units (RPUs) for a year at a discount from Serverless on-demand (OD) rates.</p>

        Args:
            capacity: <p>The number of Redshift Processing Units (RPUs) to reserve.</p>
            offering_id: <p>The ID of the offering associated with the reservation. The offering determines the payment schedule for the reservation.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. This token must be a valid UUIDv4 value. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/"> Making retries safe with idempotent APIs </a>.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_reservation_request.CreateReservationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_reservation_response.CreateReservationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_reservation

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_reservation.async_create_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_reservation_request.CreateReservationRequest = {
            "capacity": capacity,
            "offering_id": offering_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_reservation(
        self,
        reservation_id: "capo_redshift_serverless.types.reservation_id.ReservationId",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> (
        "capo_redshift_serverless.types.get_reservation_response.GetReservationResponse"
    ):
        """<p>Gets an Amazon Redshift Serverless reservation. A reservation gives you the option to commit to a specified number of Redshift Processing Units (RPUs) for a year at a discount from Serverless on-demand (OD) rates.</p>

        Args:
            reservation_id: <p>The ID of the reservation to retrieve.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_reservation_request.GetReservationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_reservation_response.GetReservationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_reservation

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_reservation.async_get_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_reservation_request.GetReservationRequest = {
            "reservation_id": reservation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_reservation_offering(
        self,
        offering_id: "capo_redshift_serverless.types.offering_id.OfferingId",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_reservation_offering_response.GetReservationOfferingResponse":
        """<p>Returns the reservation offering. The offering determines the payment schedule for the reservation.</p>

        Args:
            offering_id: <p>The identifier for the offering..</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_reservation_offering_request.GetReservationOfferingRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_reservation_offering_response.GetReservationOfferingResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_reservation_offering

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_reservation_offering.async_get_reservation_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_reservation_offering_request.GetReservationOfferingRequest = {
            "offering_id": offering_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_reservation_offerings(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_reservation_offerings_response.ListReservationOfferingsResponse":
        """<p>Returns the current reservation offerings in your account.</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_reservation_offerings_request.ListReservationOfferingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_reservation_offerings_response.ListReservationOfferingsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_reservation_offerings

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_reservation_offerings.async_list_reservation_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_reservation_offerings_request.ListReservationOfferingsRequest = {}
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

    async def iter_list_reservation_offerings(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.reservation_offering.ReservationOffering]":
        _token = next_token
        while True:
            _response = await self.list_reservation_offerings(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("reservation_offerings_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_reservations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_reservations_response.ListReservationsResponse":
        """<p>Returns a list of Reservation objects.</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_reservations_request.ListReservationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_reservations_response.ListReservationsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_reservations

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_reservations.async_list_reservations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_reservations_request.ListReservationsRequest = {}
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

    async def iter_list_reservations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.reservation.Reservation]":
        _token = next_token
        while True:
            _response = await self.list_reservations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("reservations_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        target_action: "capo_redshift_serverless.types.target_action.TargetAction",
        schedule: "capo_redshift_serverless.types.schedule.Schedule",
        role_arn: "capo_redshift_serverless.types.iam_role_arn.IamRoleArn",
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        enabled: Optional[bool] = None,
        scheduled_action_description: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "capo_redshift_serverless.types.create_scheduled_action_response.CreateScheduledActionResponse":
        """<p>Creates a scheduled action. A scheduled action contains a schedule and an Amazon Redshift API action. For example, you can create a schedule of when to run the <code>CreateSnapshot</code> API operation.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action.</p>
            schedule: <p>The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.</p> <ul> <li> <p>Format of at timestamp is <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2016-03-04T17:27:00</code>.</p> </li> <li> <p>Format of cron expression is <code>(Minutes Hours Day-of-month Month Day-of-week Year)</code>. For example, <code>"(0 10 ? * MON *)"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> </li> </ul>
            role_arn: <p>The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots. (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using Identity-Based Policies for Amazon Redshift</a> in the Amazon Redshift Management Guide</p>
            namespace_name: <p>The name of the namespace for which to create a scheduled action.</p>
            enabled: <p>Indicates whether the schedule is enabled. If false, the scheduled action does not trigger. For more information about <code>state</code> of the scheduled action, see <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ScheduledAction.html">ScheduledAction</a>.</p>
            scheduled_action_description: <p>The description of the scheduled action.</p>
            start_time: <p>The start time in UTC when the schedule is active. Before this time, the scheduled action does not trigger.</p>
            end_time: <p>The end time in UTC when the schedule is no longer active. After this time, the scheduled action does not trigger.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_scheduled_action_request.CreateScheduledActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_scheduled_action_response.CreateScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_scheduled_action.async_create_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_scheduled_action_request.CreateScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name,
            "target_action": target_action,
            "schedule": schedule,
            "role_arn": role_arn,
            "namespace_name": namespace_name,
        }
        if enabled is not None:
            input_["enabled"] = enabled
        if scheduled_action_description is not None:
            input_["scheduled_action_description"] = scheduled_action_description
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_scheduled_action_response.DeleteScheduledActionResponse":
        """<p>Deletes a scheduled action.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action to delete.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_scheduled_action_request.DeleteScheduledActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_scheduled_action_response.DeleteScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_scheduled_action.async_delete_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_scheduled_action_request.DeleteScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_scheduled_action_response.GetScheduledActionResponse":
        """<p>Returns information about a scheduled action.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_scheduled_action_request.GetScheduledActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_scheduled_action_response.GetScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_scheduled_action.async_get_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_scheduled_action_request.GetScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_scheduled_actions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[
            "capo_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
    ) -> "capo_redshift_serverless.types.list_scheduled_actions_response.ListScheduledActionsResponse":
        """<p>Returns a list of scheduled actions. You can use the flags to filter the list of returned scheduled actions.</p>

        Args:
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. Use <code>nextToken</code> to display the next page of results.</p>
            namespace_name: <p>The name of namespace associated with the scheduled action to retrieve.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.invalid_pagination_exception.InvalidPaginationException: <p>The provided pagination token is invalid.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_scheduled_actions_request.ListScheduledActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_scheduled_actions_response.ListScheduledActionsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_scheduled_actions

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_scheduled_actions.async_list_scheduled_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_scheduled_actions_request.ListScheduledActionsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_scheduled_actions(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[
            "capo_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.scheduled_action_association.ScheduledActionAssociation]":
        _token = next_token
        while True:
            _response = await self.list_scheduled_actions(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                namespace_name=namespace_name,
            )
            _page = _resolve_path(_response, ("scheduled_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_scheduled_action(
        self,
        scheduled_action_name: "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        target_action: Optional[
            "capo_redshift_serverless.types.target_action.TargetAction"
        ] = None,
        schedule: Optional["capo_redshift_serverless.types.schedule.Schedule"] = None,
        role_arn: Optional[
            "capo_redshift_serverless.types.iam_role_arn.IamRoleArn"
        ] = None,
        enabled: Optional[bool] = None,
        scheduled_action_description: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "capo_redshift_serverless.types.update_scheduled_action_response.UpdateScheduledActionResponse":
        """<p>Updates a scheduled action.</p>

        Args:
            scheduled_action_name: <p>The name of the scheduled action to update to.</p>
            schedule: <p>The schedule for a one-time (at timestamp format) or recurring (cron format) scheduled action. Schedule invocations must be separated by at least one hour. Times are in UTC.</p> <ul> <li> <p>Format of at timestamp is <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2016-03-04T17:27:00</code>.</p> </li> <li> <p>Format of cron expression is <code>(Minutes Hours Day-of-month Month Day-of-week Year)</code>. For example, <code>"(0 10 ? * MON *)"</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions">Cron Expressions</a> in the <i>Amazon CloudWatch Events User Guide</i>.</p> </li> </ul>
            role_arn: <p>The ARN of the IAM role to assume to run the scheduled action. This IAM role must have permission to run the Amazon Redshift Serverless API operation in the scheduled action. This IAM role must allow the Amazon Redshift scheduler to schedule creating snapshots (Principal scheduler.redshift.amazonaws.com) to assume permissions on your behalf. For more information about the IAM role to use with the Amazon Redshift scheduler, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html">Using Identity-Based Policies for Amazon Redshift</a> in the Amazon Redshift Management Guide</p>
            enabled: <p>Specifies whether to enable the scheduled action.</p>
            scheduled_action_description: <p>The descripion of the scheduled action to update to.</p>
            start_time: <p>The start time in UTC of the scheduled action to update to.</p>
            end_time: <p>The end time in UTC of the scheduled action to update.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_scheduled_action_request.UpdateScheduledActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_scheduled_action_response.UpdateScheduledActionResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_scheduled_action

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_scheduled_action.async_update_scheduled_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_scheduled_action_request.UpdateScheduledActionRequest = {
            "scheduled_action_name": scheduled_action_name
        }
        if target_action is not None:
            input_["target_action"] = target_action
        if schedule is not None:
            input_["schedule"] = schedule
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if enabled is not None:
            input_["enabled"] = enabled
        if scheduled_action_description is not None:
            input_["scheduled_action_description"] = scheduled_action_description
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_snapshot(
        self,
        namespace_name: str,
        snapshot_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        retention_period: Optional[int] = None,
        tags: Optional["capo_redshift_serverless.types.tag_list.TagList"] = None,
    ) -> (
        "capo_redshift_serverless.types.create_snapshot_response.CreateSnapshotResponse"
    ):
        """<p>Creates a snapshot of all databases in a namespace. For more information about snapshots, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-snapshots-recovery-points.html"> Working with snapshots and recovery points</a>.</p>

        Args:
            namespace_name: <p>The namespace to create a snapshot for.</p>
            snapshot_name: <p>The name of the snapshot.</p>
            retention_period: <p>How long to retain the created snapshot.</p>
            tags: <p>An array of <a href="https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html">Tag objects</a> to associate with the snapshot.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_snapshot_request.CreateSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_snapshot_response.CreateSnapshotResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_snapshot.async_create_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_snapshot_request.CreateSnapshotRequest = {
            "namespace_name": namespace_name,
            "snapshot_name": snapshot_name,
        }
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_snapshot_copy_configuration(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        destination_region: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        snapshot_retention_period: Optional[int] = None,
        destination_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "capo_redshift_serverless.types.create_snapshot_copy_configuration_response.CreateSnapshotCopyConfigurationResponse":
        """<p>Creates a snapshot copy configuration that lets you copy snapshots to another Amazon Web Services Region.</p>

        Args:
            namespace_name: <p>The name of the namespace to copy snapshots from.</p>
            destination_region: <p>The destination Amazon Web Services Region that you want to copy snapshots to.</p>
            snapshot_retention_period: <p>The retention period of the snapshots that you copy to the destination Amazon Web Services Region.</p>
            destination_kms_key_id: <p>The KMS key to use to encrypt your snapshots in the destination Amazon Web Services Region.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_snapshot_copy_configuration_request.CreateSnapshotCopyConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_snapshot_copy_configuration_response.CreateSnapshotCopyConfigurationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_snapshot_copy_configuration

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_snapshot_copy_configuration.async_create_snapshot_copy_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_snapshot_copy_configuration_request.CreateSnapshotCopyConfigurationRequest = {
            "namespace_name": namespace_name,
            "destination_region": destination_region,
        }
        if snapshot_retention_period is not None:
            input_["snapshot_retention_period"] = snapshot_retention_period
        if destination_kms_key_id is not None:
            input_["destination_kms_key_id"] = destination_kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_snapshot(
        self,
        snapshot_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> (
        "capo_redshift_serverless.types.delete_snapshot_response.DeleteSnapshotResponse"
    ):
        """<p>Deletes a snapshot from Amazon Redshift Serverless.</p>

        Args:
            snapshot_name: <p>The name of the snapshot to be deleted.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_snapshot_request.DeleteSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_snapshot_response.DeleteSnapshotResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_snapshot.async_delete_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_snapshot_request.DeleteSnapshotRequest = {
            "snapshot_name": snapshot_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_snapshot_copy_configuration(
        self,
        snapshot_copy_configuration_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_snapshot_copy_configuration_response.DeleteSnapshotCopyConfigurationResponse":
        """<p>Deletes a snapshot copy configuration</p>

        Args:
            snapshot_copy_configuration_id: <p>The ID of the snapshot copy configuration to delete.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_snapshot_copy_configuration_request.DeleteSnapshotCopyConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_snapshot_copy_configuration_response.DeleteSnapshotCopyConfigurationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_snapshot_copy_configuration

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_snapshot_copy_configuration.async_delete_snapshot_copy_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_snapshot_copy_configuration_request.DeleteSnapshotCopyConfigurationRequest = {
            "snapshot_copy_configuration_id": snapshot_copy_configuration_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_snapshot(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        snapshot_name: Optional[str] = None,
        owner_account: Optional[str] = None,
        snapshot_arn: Optional[str] = None,
    ) -> "capo_redshift_serverless.types.get_snapshot_response.GetSnapshotResponse":
        """<p>Returns information about a specific snapshot.</p>

        Args:
            snapshot_name: <p>The name of the snapshot to return.</p>
            owner_account: <p>The owner Amazon Web Services account of a snapshot shared with another user.</p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot to return.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_snapshot_request.GetSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_snapshot_response.GetSnapshotResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_snapshot.async_get_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_snapshot_request.GetSnapshotRequest = {}
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_table_restore_status(
        self,
        table_restore_request_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_table_restore_status_response.GetTableRestoreStatusResponse":
        """<p>Returns information about a <code>TableRestoreStatus</code> object.</p>

        Args:
            table_restore_request_id: <p>The ID of the <code>RestoreTableFromSnapshot</code> request to return status for.</p>

        Raises:
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_table_restore_status_request.GetTableRestoreStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_table_restore_status_response.GetTableRestoreStatusResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_table_restore_status

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_table_restore_status.async_get_table_restore_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_table_restore_status_request.GetTableRestoreStatusRequest = {
            "table_restore_request_id": table_restore_request_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_snapshot_copy_configurations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        namespace_name: Optional[
            "capo_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_snapshot_copy_configurations_response.ListSnapshotCopyConfigurationsResponse":
        """<p>Returns a list of snapshot copy configurations.</p>

        Args:
            namespace_name: <p>The namespace from which to list all snapshot copy configurations.</p>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.invalid_pagination_exception.InvalidPaginationException: <p>The provided pagination token is invalid.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_snapshot_copy_configurations_request.ListSnapshotCopyConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_snapshot_copy_configurations_response.ListSnapshotCopyConfigurationsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_snapshot_copy_configurations

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_snapshot_copy_configurations.async_list_snapshot_copy_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_snapshot_copy_configurations_request.ListSnapshotCopyConfigurationsRequest = {}
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
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

    async def iter_list_snapshot_copy_configurations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        namespace_name: Optional[
            "capo_redshift_serverless.types.namespace_name.NamespaceName"
        ] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.snapshot_copy_configuration.SnapshotCopyConfiguration]":
        _token = next_token
        while True:
            _response = await self.list_snapshot_copy_configurations(
                config_overrides=config_overrides,
                namespace_name=namespace_name,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("snapshot_copy_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[str] = None,
        namespace_arn: Optional[str] = None,
        owner_account: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "capo_redshift_serverless.types.list_snapshots_response.ListSnapshotsResponse":
        """<p>Returns a list of snapshots.</p>

        Args:
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            namespace_name: <p>The namespace from which to list all snapshots.</p>
            namespace_arn: <p>The Amazon Resource Name (ARN) of the namespace from which to list all snapshots.</p>
            owner_account: <p>The owner Amazon Web Services account of the snapshot.</p>
            start_time: <p>The time when the creation of the snapshot was initiated.</p>
            end_time: <p>The timestamp showing when the snapshot creation finished.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_snapshots_request.ListSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_snapshots_response.ListSnapshotsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_snapshots

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_snapshots.async_list_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_snapshots_request.ListSnapshotsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
        if namespace_arn is not None:
            input_["namespace_arn"] = namespace_arn
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[str] = None,
        namespace_arn: Optional[str] = None,
        owner_account: Optional[str] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.snapshot.Snapshot]":
        _token = next_token
        while True:
            _response = await self.list_snapshots(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                namespace_name=namespace_name,
                namespace_arn=namespace_arn,
                owner_account=owner_account,
                start_time=start_time,
                end_time=end_time,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_table_restore_status(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[str] = None,
        workgroup_name: Optional[str] = None,
    ) -> "capo_redshift_serverless.types.list_table_restore_status_response.ListTableRestoreStatusResponse":
        """<p>Returns information about an array of <code>TableRestoreStatus</code> objects.</p>

        Args:
            next_token: <p>If your initial <code>ListTableRestoreStatus</code> operation returns a nextToken, you can include the returned <code>nextToken</code> in following <code>ListTableRestoreStatus</code> operations. This will return results on the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.</p>
            namespace_name: <p>The namespace from which to list all of the statuses of <code>RestoreTableFromSnapshot</code> operations .</p>
            workgroup_name: <p>The workgroup from which to list all of the statuses of <code>RestoreTableFromSnapshot</code> operations.</p>

        Raises:
            capo_redshift_serverless.errors.invalid_pagination_exception.InvalidPaginationException: <p>The provided pagination token is invalid.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_table_restore_status_request.ListTableRestoreStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_table_restore_status_response.ListTableRestoreStatusResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_table_restore_status

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_table_restore_status.async_list_table_restore_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_table_restore_status_request.ListTableRestoreStatusRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if namespace_name is not None:
            input_["namespace_name"] = namespace_name
        if workgroup_name is not None:
            input_["workgroup_name"] = workgroup_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_table_restore_status(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
        namespace_name: Optional[str] = None,
        workgroup_name: Optional[str] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.table_restore_status.TableRestoreStatus]":
        _token = next_token
        while True:
            _response = await self.list_table_restore_status(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                namespace_name=namespace_name,
                workgroup_name=workgroup_name,
            )
            _page = _resolve_path(_response, ("table_restore_statuses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def restore_from_snapshot(
        self,
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        snapshot_name: Optional[str] = None,
        snapshot_arn: Optional[str] = None,
        owner_account: Optional[str] = None,
        manage_admin_password: Optional[bool] = None,
        admin_password_secret_kms_key_id: Optional[
            "capo_redshift_serverless.types.kms_key_id.KmsKeyId"
        ] = None,
        maintain_integration: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.restore_from_snapshot_response.RestoreFromSnapshotResponse":
        """<p>Restores a namespace from a snapshot.</p>

        Args:
            namespace_name: <p>The name of the namespace to restore the snapshot to.</p>
            workgroup_name: <p>The name of the workgroup used to restore the snapshot.</p>
            snapshot_name: <p>The name of the snapshot to restore from. Must not be specified at the same time as <code>snapshotArn</code>.</p>
            snapshot_arn: <p>The Amazon Resource Name (ARN) of the snapshot to restore from. Required if restoring from a provisioned cluster to Amazon Redshift Serverless. Must not be specified at the same time as <code>snapshotName</code>.</p> <p>The format of the ARN is arn:aws:redshift:&lt;region&gt;:&lt;account_id&gt;:snapshot:&lt;cluster_identifier&gt;/&lt;snapshot_identifier&gt;.</p>
            owner_account: <p>The Amazon Web Services account that owns the snapshot.</p>
            manage_admin_password: <p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the restored snapshot's admin credentials. If <code>MmanageAdminPassword</code> is false or not set, Amazon Redshift uses the admin credentials that the namespace or cluster had at the time the snapshot was taken.</p>
            admin_password_secret_kms_key_id: <p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.</p>
            maintain_integration: <p>If <code>true</code>, maintain existing data sharing, zero-ETL and S3 event integrations when restoring. Otherwise, integrations will not be maintained after the restore operation. Integrations are only maintained when restored to the same serverless namespace.</p> <p>Default: true</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.restore_from_snapshot_request.RestoreFromSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.restore_from_snapshot_response.RestoreFromSnapshotResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.restore_from_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.restore_from_snapshot.async_restore_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.restore_from_snapshot_request.RestoreFromSnapshotRequest = {
            "namespace_name": namespace_name,
            "workgroup_name": workgroup_name,
        }
        if snapshot_name is not None:
            input_["snapshot_name"] = snapshot_name
        if snapshot_arn is not None:
            input_["snapshot_arn"] = snapshot_arn
        if owner_account is not None:
            input_["owner_account"] = owner_account
        if manage_admin_password is not None:
            input_["manage_admin_password"] = manage_admin_password
        if admin_password_secret_kms_key_id is not None:
            input_["admin_password_secret_kms_key_id"] = (
                admin_password_secret_kms_key_id
            )
        if maintain_integration is not None:
            input_["maintain_integration"] = maintain_integration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_table_from_snapshot(
        self,
        namespace_name: str,
        workgroup_name: str,
        snapshot_name: str,
        source_database_name: str,
        source_table_name: str,
        new_table_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        source_schema_name: Optional[str] = None,
        target_database_name: Optional[str] = None,
        target_schema_name: Optional[str] = None,
        activate_case_sensitive_identifier: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.restore_table_from_snapshot_response.RestoreTableFromSnapshotResponse":
        """<p>Restores a table from a snapshot to your Amazon Redshift Serverless instance. You can't use this operation to restore tables with <a href="https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html#t_Sorting_data-interleaved">interleaved sort keys</a>.</p>

        Args:
            namespace_name: <p>The namespace of the snapshot to restore from.</p>
            workgroup_name: <p>The workgroup to restore the table to.</p>
            snapshot_name: <p>The name of the snapshot to restore the table from.</p>
            source_database_name: <p>The name of the source database that contains the table being restored.</p>
            source_schema_name: <p>The name of the source schema that contains the table being restored.</p>
            source_table_name: <p>The name of the source table being restored.</p>
            target_database_name: <p>The name of the database to restore the table to.</p>
            target_schema_name: <p>The name of the schema to restore the table to.</p>
            new_table_name: <p>The name of the table to create from the restore operation.</p>
            activate_case_sensitive_identifier: <p>Indicates whether name identifiers for database, schema, and table are case sensitive. If true, the names are case sensitive. If false, the names are not case sensitive. The default is false.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.restore_table_from_snapshot_request.RestoreTableFromSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.restore_table_from_snapshot_response.RestoreTableFromSnapshotResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.restore_table_from_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.restore_table_from_snapshot.async_restore_table_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.restore_table_from_snapshot_request.RestoreTableFromSnapshotRequest = {
            "namespace_name": namespace_name,
            "workgroup_name": workgroup_name,
            "snapshot_name": snapshot_name,
            "source_database_name": source_database_name,
            "source_table_name": source_table_name,
            "new_table_name": new_table_name,
        }
        if source_schema_name is not None:
            input_["source_schema_name"] = source_schema_name
        if target_database_name is not None:
            input_["target_database_name"] = target_database_name
        if target_schema_name is not None:
            input_["target_schema_name"] = target_schema_name
        if activate_case_sensitive_identifier is not None:
            input_["activate_case_sensitive_identifier"] = (
                activate_case_sensitive_identifier
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_snapshot(
        self,
        snapshot_name: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        retention_period: Optional[int] = None,
    ) -> (
        "capo_redshift_serverless.types.update_snapshot_response.UpdateSnapshotResponse"
    ):
        """<p>Updates a snapshot.</p>

        Args:
            snapshot_name: <p>The name of the snapshot.</p>
            retention_period: <p>The new retention period of the snapshot.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_snapshot_request.UpdateSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_snapshot_response.UpdateSnapshotResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_snapshot

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_snapshot.async_update_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_snapshot_request.UpdateSnapshotRequest = {
            "snapshot_name": snapshot_name
        }
        if retention_period is not None:
            input_["retention_period"] = retention_period

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_snapshot_copy_configuration(
        self,
        snapshot_copy_configuration_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        snapshot_retention_period: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.update_snapshot_copy_configuration_response.UpdateSnapshotCopyConfigurationResponse":
        """<p>Updates a snapshot copy configuration.</p>

        Args:
            snapshot_copy_configuration_id: <p>The ID of the snapshot copy configuration to update.</p>
            snapshot_retention_period: <p>The new retention period of how long to keep a snapshot in the destination Amazon Web Services Region.</p>

        Raises:
            capo_redshift_serverless.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_snapshot_copy_configuration_request.UpdateSnapshotCopyConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_snapshot_copy_configuration_response.UpdateSnapshotCopyConfigurationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_snapshot_copy_configuration

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_snapshot_copy_configuration.async_update_snapshot_copy_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_snapshot_copy_configuration_request.UpdateSnapshotCopyConfigurationRequest = {
            "snapshot_copy_configuration_id": snapshot_copy_configuration_id
        }
        if snapshot_retention_period is not None:
            input_["snapshot_retention_period"] = snapshot_retention_period

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_usage_limit(
        self,
        resource_arn: str,
        usage_type: "capo_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType",
        amount: int,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        period: Optional[
            "capo_redshift_serverless.types.usage_limit_period.UsageLimitPeriod"
        ] = None,
        breach_action: Optional[
            "capo_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
        ] = None,
    ) -> "capo_redshift_serverless.types.create_usage_limit_response.CreateUsageLimitResponse":
        """<p>Creates a usage limit for a specified Amazon Redshift Serverless usage type. The usage limit is identified by the returned usage limit identifier. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Redshift Serverless resource to create the usage limit for.</p>
            usage_type: <p>The type of Amazon Redshift Serverless usage to create a usage limit for.</p>
            amount: <p>The limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.</p>
            period: <p>The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly.</p>
            breach_action: <p>The action that Amazon Redshift Serverless takes when the limit is reached. The default is log.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_usage_limit_request.CreateUsageLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_usage_limit_response.CreateUsageLimitResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_usage_limit

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_usage_limit.async_create_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_usage_limit_request.CreateUsageLimitRequest = {
            "resource_arn": resource_arn,
            "usage_type": usage_type,
            "amount": amount,
        }
        if period is not None:
            input_["period"] = period
        if breach_action is not None:
            input_["breach_action"] = breach_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_usage_limit(
        self,
        usage_limit_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_usage_limit_response.DeleteUsageLimitResponse":
        """<p>Deletes a usage limit from Amazon Redshift Serverless.</p>

        Args:
            usage_limit_id: <p>The unique identifier of the usage limit to delete.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_usage_limit_request.DeleteUsageLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_usage_limit_response.DeleteUsageLimitResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_usage_limit

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_usage_limit.async_delete_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_usage_limit_request.DeleteUsageLimitRequest = {
            "usage_limit_id": usage_limit_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_usage_limit(
        self,
        usage_limit_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> (
        "capo_redshift_serverless.types.get_usage_limit_response.GetUsageLimitResponse"
    ):
        """<p>Returns information about a usage limit.</p>

        Args:
            usage_limit_id: <p>The unique identifier of the usage limit to return information for.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_usage_limit_request.GetUsageLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_usage_limit_response.GetUsageLimitResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_usage_limit

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_usage_limit.async_get_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_usage_limit_request.GetUsageLimitRequest = {
            "usage_limit_id": usage_limit_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_usage_limits(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        resource_arn: Optional[str] = None,
        usage_type: Optional[
            "capo_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType"
        ] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_usage_limits_response.ListUsageLimitsResponse":
        """<p>Lists all usage limits within Amazon Redshift Serverless.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) associated with the resource whose usage limits you want to list.</p>
            usage_type: <p>The Amazon Redshift Serverless feature whose limits you want to see.</p>
            next_token: <p>If your initial <code>ListUsageLimits</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListUsageLimits</code> operations, which returns results in the next page. </p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 100.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.invalid_pagination_exception.InvalidPaginationException: <p>The provided pagination token is invalid.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_usage_limits_request.ListUsageLimitsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_usage_limits_response.ListUsageLimitsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_usage_limits

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_usage_limits.async_list_usage_limits(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_usage_limits_request.ListUsageLimitsRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if usage_type is not None:
            input_["usage_type"] = usage_type
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

    async def iter_list_usage_limits(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        resource_arn: Optional[str] = None,
        usage_type: Optional[
            "capo_redshift_serverless.types.usage_limit_usage_type.UsageLimitUsageType"
        ] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.usage_limit.UsageLimit]":
        _token = next_token
        while True:
            _response = await self.list_usage_limits(
                config_overrides=config_overrides,
                resource_arn=resource_arn,
                usage_type=usage_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("usage_limits",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_usage_limit(
        self,
        usage_limit_id: str,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        amount: Optional[int] = None,
        breach_action: Optional[
            "capo_redshift_serverless.types.usage_limit_breach_action.UsageLimitBreachAction"
        ] = None,
    ) -> "capo_redshift_serverless.types.update_usage_limit_response.UpdateUsageLimitResponse":
        """<p>Update a usage limit in Amazon Redshift Serverless. You can't update the usage type or period of a usage limit.</p>

        Args:
            usage_limit_id: <p>The identifier of the usage limit to update.</p>
            amount: <p>The new limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.</p>
            breach_action: <p>The new action that Amazon Redshift Serverless takes when the limit is reached.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_usage_limit_request.UpdateUsageLimitRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_usage_limit_response.UpdateUsageLimitResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_usage_limit

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_usage_limit.async_update_usage_limit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_usage_limit_request.UpdateUsageLimitRequest = {
            "usage_limit_id": usage_limit_id
        }
        if amount is not None:
            input_["amount"] = amount
        if breach_action is not None:
            input_["breach_action"] = breach_action

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_workgroup(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        namespace_name: "capo_redshift_serverless.types.namespace_name.NamespaceName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        base_capacity: Optional[int] = None,
        enhanced_vpc_routing: Optional[bool] = None,
        config_parameters: Optional[
            "capo_redshift_serverless.types.config_parameter_list.ConfigParameterList"
        ] = None,
        security_group_ids: Optional[
            "capo_redshift_serverless.types.security_group_id_list.SecurityGroupIdList"
        ] = None,
        subnet_ids: Optional[
            "capo_redshift_serverless.types.subnet_id_list.SubnetIdList"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        tags: Optional["capo_redshift_serverless.types.tag_list.TagList"] = None,
        port: Optional[int] = None,
        max_capacity: Optional[int] = None,
        price_performance_target: Optional[
            "capo_redshift_serverless.types.performance_target.PerformanceTarget"
        ] = None,
        ip_address_type: Optional[
            "capo_redshift_serverless.types.ip_address_type.IpAddressType"
        ] = None,
        track_name: Optional[
            "capo_redshift_serverless.types.track_name.TrackName"
        ] = None,
        extra_compute_for_automatic_optimization: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.create_workgroup_response.CreateWorkgroupResponse":
        """<p>Creates an workgroup in Amazon Redshift Serverless.</p> <p>VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a workgroup is in an account with VPC BPA turned on, the following capabilities are blocked: </p> <ul> <li> <p>Creating a public access workgroup</p> </li> <li> <p>Modifying a private workgroup to public</p> </li> <li> <p>Adding a subnet with VPC BPA turned on to the workgroup when the workgroup is public</p> </li> </ul> <p>For more information about VPC BPA, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html">Block public access to VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            workgroup_name: <p>The name of the created workgroup.</p>
            namespace_name: <p>The name of the namespace to associate with the workgroup.</p>
            base_capacity: <p>The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).</p>
            enhanced_vpc_routing: <p>The value that specifies whether to turn on enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC instead of over the internet.</p>
            config_parameters: <p>An array of parameters to set for advanced control over a database. The options are <code>auto_mv</code>, <code>datestyle</code>, <code>enable_case_sensitive_identifier</code>, <code>enable_user_activity_logging</code>, <code>query_group</code>, <code>search_path</code>, <code>require_ssl</code>, <code>use_fips_ssl</code>, and either <code>wlm_json_configuration</code> or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as <code>max_scan_row_count</code>, <code>max_query_execution_time</code>) or use <code>wlm_json_configuration</code> to define query queues with rules, but not both. If you're using <code>wlm_json_configuration</code>, the maximum size of <code>parameterValue</code> is 8000 characters. For more information about query monitoring rules and available metrics, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless"> Query monitoring metrics for Amazon Redshift Serverless</a>.</p>
            security_group_ids: <p>An array of security group IDs to associate with the workgroup.</p>
            subnet_ids: <p>An array of VPC subnet IDs to associate with the workgroup.</p>
            publicly_accessible: <p>A value that specifies whether the workgroup can be accessed from a public network.</p>
            tags: <p>A array of tag instances.</p>
            port: <p>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</p>
            max_capacity: <p>The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.</p>
            price_performance_target: <p>An object that represents the price performance target settings for the workgroup.</p>
            ip_address_type: <p>The IP address type that the workgroup supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>
            track_name: <p>An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the <code>current</code> track.</p>
            extra_compute_for_automatic_optimization: <p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>There is an insufficient capacity to perform the action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.ipv6_cidr_block_not_found_exception.Ipv6CidrBlockNotFoundException: <p>There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_workgroup_request.CreateWorkgroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_workgroup_response.CreateWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_workgroup

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_workgroup.async_create_workgroup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_workgroup_request.CreateWorkgroupRequest = {
            "workgroup_name": workgroup_name,
            "namespace_name": namespace_name,
        }
        if base_capacity is not None:
            input_["base_capacity"] = base_capacity
        if enhanced_vpc_routing is not None:
            input_["enhanced_vpc_routing"] = enhanced_vpc_routing
        if config_parameters is not None:
            input_["config_parameters"] = config_parameters
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if tags is not None:
            input_["tags"] = tags
        if port is not None:
            input_["port"] = port
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if price_performance_target is not None:
            input_["price_performance_target"] = price_performance_target
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if track_name is not None:
            input_["track_name"] = track_name
        if extra_compute_for_automatic_optimization is not None:
            input_["extra_compute_for_automatic_optimization"] = (
                extra_compute_for_automatic_optimization
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workgroup(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_workgroup_response.GetWorkgroupResponse":
        """<p>Returns information about a specific workgroup.</p>

        Args:
            workgroup_name: <p>The name of the workgroup to return information for.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_workgroup_request.GetWorkgroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_workgroup_response.GetWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_workgroup

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_workgroup.async_get_workgroup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_workgroup_request.GetWorkgroupRequest = {
            "workgroup_name": workgroup_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workgroup(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        base_capacity: Optional[int] = None,
        enhanced_vpc_routing: Optional[bool] = None,
        config_parameters: Optional[
            "capo_redshift_serverless.types.config_parameter_list.ConfigParameterList"
        ] = None,
        publicly_accessible: Optional[bool] = None,
        subnet_ids: Optional[
            "capo_redshift_serverless.types.subnet_id_list.SubnetIdList"
        ] = None,
        security_group_ids: Optional[
            "capo_redshift_serverless.types.security_group_id_list.SecurityGroupIdList"
        ] = None,
        port: Optional[int] = None,
        max_capacity: Optional[int] = None,
        ip_address_type: Optional[
            "capo_redshift_serverless.types.ip_address_type.IpAddressType"
        ] = None,
        price_performance_target: Optional[
            "capo_redshift_serverless.types.performance_target.PerformanceTarget"
        ] = None,
        track_name: Optional[
            "capo_redshift_serverless.types.track_name.TrackName"
        ] = None,
        extra_compute_for_automatic_optimization: Optional[bool] = None,
    ) -> "capo_redshift_serverless.types.update_workgroup_response.UpdateWorkgroupResponse":
        """<p>Updates a workgroup with the specified configuration settings. You can't update multiple parameters in one request. For example, you can update <code>baseCapacity</code> or <code>port</code> in a single request, but you can't update both in the same request.</p> <p>VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a workgroup is in an account with VPC BPA turned on, the following capabilities are blocked: </p> <ul> <li> <p>Creating a public access workgroup</p> </li> <li> <p>Modifying a private workgroup to public</p> </li> <li> <p>Adding a subnet with VPC BPA turned on to the workgroup when the workgroup is public</p> </li> </ul> <p>For more information about VPC BPA, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html">Block public access to VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p>

        Args:
            workgroup_name: <p>The name of the workgroup to update. You can't update the name of a workgroup once it is created.</p>
            base_capacity: <p>The new base data warehouse capacity in Redshift Processing Units (RPUs).</p>
            enhanced_vpc_routing: <p>The value that specifies whether to turn on enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.</p>
            config_parameters: <p>An array of parameters to set for advanced control over a database. The options are <code>auto_mv</code>, <code>datestyle</code>, <code>enable_case_sensitive_identifier</code>, <code>enable_user_activity_logging</code>, <code>query_group</code>, <code>search_path</code>, <code>require_ssl</code>, <code>use_fips_ssl</code>, and either <code>wlm_json_configuration</code> or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as <code>max_scan_row_count</code>, <code>max_query_execution_time</code>) or use <code>wlm_json_configuration</code> to define query queues with rules, but not both. If you're using <code>wlm_json_configuration</code>, the maximum size of <code>parameterValue</code> is 8000 characters. For more information about query monitoring rules and available metrics, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless"> Query monitoring metrics for Amazon Redshift Serverless</a>.</p>
            publicly_accessible: <p>A value that specifies whether the workgroup can be accessible from a public network.</p>
            subnet_ids: <p>An array of VPC subnet IDs to associate with the workgroup.</p>
            security_group_ids: <p>An array of security group IDs to associate with the workgroup.</p>
            port: <p>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</p>
            max_capacity: <p>The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.</p>
            ip_address_type: <p>The IP address type that the workgroup supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>
            price_performance_target: <p>An object that represents the price performance target settings for the workgroup.</p>
            track_name: <p>An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the <code>current</code> track.</p>
            extra_compute_for_automatic_optimization: <p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.insufficient_capacity_exception.InsufficientCapacityException: <p>There is an insufficient capacity to perform the action.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.ipv6_cidr_block_not_found_exception.Ipv6CidrBlockNotFoundException: <p>There are no subnets in your VPC with associated IPv6 CIDR blocks. To use dual-stack mode, associate an IPv6 CIDR block with each subnet in your VPC.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.update_workgroup_request.UpdateWorkgroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.update_workgroup_response.UpdateWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.update_workgroup

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.update_workgroup.async_update_workgroup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.update_workgroup_request.UpdateWorkgroupRequest = {
            "workgroup_name": workgroup_name
        }
        if base_capacity is not None:
            input_["base_capacity"] = base_capacity
        if enhanced_vpc_routing is not None:
            input_["enhanced_vpc_routing"] = enhanced_vpc_routing
        if config_parameters is not None:
            input_["config_parameters"] = config_parameters
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if port is not None:
            input_["port"] = port
        if max_capacity is not None:
            input_["max_capacity"] = max_capacity
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if price_performance_target is not None:
            input_["price_performance_target"] = price_performance_target
        if track_name is not None:
            input_["track_name"] = track_name
        if extra_compute_for_automatic_optimization is not None:
            input_["extra_compute_for_automatic_optimization"] = (
                extra_compute_for_automatic_optimization
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workgroup(
        self,
        workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.delete_workgroup_response.DeleteWorkgroupResponse":
        """<p>Deletes a workgroup.</p>

        Args:
            workgroup_name: <p>The name of the workgroup to be deleted.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.delete_workgroup_request.DeleteWorkgroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.delete_workgroup_response.DeleteWorkgroupResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.delete_workgroup

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.delete_workgroup.async_delete_workgroup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.delete_workgroup_request.DeleteWorkgroupRequest = {
            "workgroup_name": workgroup_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workgroups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> (
        "capo_redshift_serverless.types.list_workgroups_response.ListWorkgroupsResponse"
    ):
        """<p>Returns information about a list of specified workgroups.</p>

        Args:
            next_token: <p>If your initial ListWorkgroups operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following ListNamespaces operations, which returns results in the next page.</p>
            max_results: <p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>
            owner_account: <p>The owner Amazon Web Services account for the Amazon Redshift Serverless workgroup.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_workgroups_request.ListWorkgroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_workgroups_response.ListWorkgroupsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_workgroups

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_workgroups.async_list_workgroups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_workgroups_request.ListWorkgroupsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if owner_account is not None:
            input_["owner_account"] = owner_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_workgroups(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        owner_account: Optional[
            "capo_redshift_serverless.types.owner_account.OwnerAccount"
        ] = None,
    ) -> "AsyncIterator[capo_redshift_serverless.types.workgroup.Workgroup]":
        _token = next_token
        while True:
            _response = await self.list_workgroups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                owner_account=owner_account,
            )
            _page = _resolve_path(_response, ("workgroups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
