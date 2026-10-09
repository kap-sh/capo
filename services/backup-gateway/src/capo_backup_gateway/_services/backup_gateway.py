"""Generated from Smithy shape ``com.amazonaws.backupgateway#BackupOnPremises_v20210101``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_backup_gateway._auth._signers
import capo_backup_gateway._auth._sigv4
from capo_backup_gateway._auth._identity import Credentials
from capo_backup_gateway._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_backup_gateway._auth._zapros_handler import AuthMiddleware
from capo_backup_gateway._resources.backup_on_premises_v20210101.gateway_resource import (
    GatewayResource,
)
from capo_backup_gateway._resources.backup_on_premises_v20210101.hypervisor_resource import (
    HypervisorResource,
)
from capo_backup_gateway._resources.backup_on_premises_v20210101.virtual_machine_resource import (
    VirtualMachineResource,
)
from capo_backup_gateway._services._aws_config import aws_config
from capo_backup_gateway._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_backup_gateway.types.activation_key
    import capo_backup_gateway.types.associate_gateway_to_server_input
    import capo_backup_gateway.types.associate_gateway_to_server_output
    import capo_backup_gateway.types.bandwidth_rate_limit_intervals
    import capo_backup_gateway.types.create_gateway_input
    import capo_backup_gateway.types.create_gateway_output
    import capo_backup_gateway.types.day_of_month
    import capo_backup_gateway.types.day_of_week
    import capo_backup_gateway.types.delete_gateway_input
    import capo_backup_gateway.types.delete_gateway_output
    import capo_backup_gateway.types.delete_hypervisor_input
    import capo_backup_gateway.types.delete_hypervisor_output
    import capo_backup_gateway.types.disassociate_gateway_from_server_input
    import capo_backup_gateway.types.disassociate_gateway_from_server_output
    import capo_backup_gateway.types.gateway_arn
    import capo_backup_gateway.types.gateway_type
    import capo_backup_gateway.types.get_bandwidth_rate_limit_schedule_input
    import capo_backup_gateway.types.get_bandwidth_rate_limit_schedule_output
    import capo_backup_gateway.types.get_gateway_input
    import capo_backup_gateway.types.get_gateway_output
    import capo_backup_gateway.types.get_hypervisor_input
    import capo_backup_gateway.types.get_hypervisor_output
    import capo_backup_gateway.types.get_hypervisor_property_mappings_input
    import capo_backup_gateway.types.get_hypervisor_property_mappings_output
    import capo_backup_gateway.types.get_virtual_machine_input
    import capo_backup_gateway.types.get_virtual_machine_output
    import capo_backup_gateway.types.host
    import capo_backup_gateway.types.hour_of_day
    import capo_backup_gateway.types.iam_role_arn
    import capo_backup_gateway.types.import_hypervisor_configuration_input
    import capo_backup_gateway.types.import_hypervisor_configuration_output
    import capo_backup_gateway.types.kms_key_arn
    import capo_backup_gateway.types.list_gateways_input
    import capo_backup_gateway.types.list_gateways_output
    import capo_backup_gateway.types.list_hypervisors_input
    import capo_backup_gateway.types.list_hypervisors_output
    import capo_backup_gateway.types.list_tags_for_resource_input
    import capo_backup_gateway.types.list_tags_for_resource_output
    import capo_backup_gateway.types.list_virtual_machines_input
    import capo_backup_gateway.types.list_virtual_machines_output
    import capo_backup_gateway.types.log_group_arn
    import capo_backup_gateway.types.max_results
    import capo_backup_gateway.types.minute_of_hour
    import capo_backup_gateway.types.name
    import capo_backup_gateway.types.next_token
    import capo_backup_gateway.types.password
    import capo_backup_gateway.types.put_bandwidth_rate_limit_schedule_input
    import capo_backup_gateway.types.put_bandwidth_rate_limit_schedule_output
    import capo_backup_gateway.types.put_hypervisor_property_mappings_input
    import capo_backup_gateway.types.put_hypervisor_property_mappings_output
    import capo_backup_gateway.types.put_maintenance_start_time_input
    import capo_backup_gateway.types.put_maintenance_start_time_output
    import capo_backup_gateway.types.resource_arn
    import capo_backup_gateway.types.server_arn
    import capo_backup_gateway.types.start_virtual_machines_metadata_sync_input
    import capo_backup_gateway.types.start_virtual_machines_metadata_sync_output
    import capo_backup_gateway.types.tag_keys
    import capo_backup_gateway.types.tag_resource_input
    import capo_backup_gateway.types.tag_resource_output
    import capo_backup_gateway.types.tags
    import capo_backup_gateway.types.test_hypervisor_configuration_input
    import capo_backup_gateway.types.test_hypervisor_configuration_output
    import capo_backup_gateway.types.untag_resource_input
    import capo_backup_gateway.types.untag_resource_output
    import capo_backup_gateway.types.update_gateway_information_input
    import capo_backup_gateway.types.update_gateway_information_output
    import capo_backup_gateway.types.update_gateway_software_now_input
    import capo_backup_gateway.types.update_gateway_software_now_output
    import capo_backup_gateway.types.update_hypervisor_input
    import capo_backup_gateway.types.update_hypervisor_output
    import capo_backup_gateway.types.username
    import capo_backup_gateway.types.vmware_to_aws_tag_mappings


class BackupGatewayClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class BackupGatewayClient:
    """A client for the ``BackupGateway`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = BackupGatewayClientConfig(
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

        # resources
        self.gateway_resource = GatewayResource(self)
        self.hypervisor_resource = HypervisorResource(self)
        self.virtual_machine_resource = VirtualMachineResource(self)

    def operation_options(
        self, config_overrides: Optional[BackupGatewayClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BackupGatewayClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_backup_gateway.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags applied to the resource identified by its Amazon Resource Name (ARN).</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource's tags to list.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.list_tags_for_resource

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_backup_gateway.types.resource_arn.ResourceArn",
        tags: "capo_backup_gateway.types.tags.Tags",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.tag_resource_output.TagResourceOutput":
        """<p>Tag the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>A list of tags to assign to the resource.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.tag_resource

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_backup_gateway.types.resource_arn.ResourceArn",
        tag_keys: "capo_backup_gateway.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from the resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>The list of tag keys specifying which tags to remove.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.untag_resource

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.untag_resource_input.UntagResourceInput = {
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

    def create_gateway(
        self,
        activation_key: "capo_backup_gateway.types.activation_key.ActivationKey",
        gateway_display_name: "capo_backup_gateway.types.name.Name",
        gateway_type: "capo_backup_gateway.types.gateway_type.GatewayType",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        tags: Optional["capo_backup_gateway.types.tags.Tags"] = None,
    ) -> "capo_backup_gateway.types.create_gateway_output.CreateGatewayOutput":
        """<p>Creates a backup gateway. After you create a gateway, you can associate it with a server using the <code>AssociateGatewayToServer</code> operation.</p>

        Args:
            activation_key: <p>The activation key of the created gateway.</p>
            gateway_display_name: <p>The display name of the created gateway.</p>
            gateway_type: <p>The type of created gateway.</p>
            tags: <p>A list of up to 50 tags to assign to the gateway. Each tag is a key-value pair.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.create_gateway_input.CreateGatewayInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.create_gateway_output.CreateGatewayOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.create_gateway

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.create_gateway.create_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.create_gateway_input.CreateGatewayInput = {
            "activation_key": activation_key,
            "gateway_display_name": gateway_display_name,
            "gateway_type": gateway_type,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gateway(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_gateway_output.GetGatewayOutput":
        """<p>By providing the ARN (Amazon Resource Name), this API returns the gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.get_gateway_input.GetGatewayInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.get_gateway_output.GetGatewayOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_gateway

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.get_gateway.get_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.get_gateway_input.GetGatewayInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_gateway_information(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        gateway_display_name: Optional["capo_backup_gateway.types.name.Name"] = None,
    ) -> "capo_backup_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput":
        """<p>Updates a gateway's name. Specify which gateway to update using the Amazon Resource Name (ARN) of the gateway in your request.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to update.</p>
            gateway_display_name: <p>The updated display name of the gateway.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_information

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_information.update_gateway_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput = {
            "gateway_arn": gateway_arn
        }
        if gateway_display_name is not None:
            input_["gateway_display_name"] = gateway_display_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.delete_gateway_output.DeleteGatewayOutput":
        """<p>Deletes a backup gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to delete.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.delete_gateway_input.DeleteGatewayInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.delete_gateway_output.DeleteGatewayOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.delete_gateway

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.delete_gateway.delete_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.delete_gateway_input.DeleteGatewayInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateways(
        self,
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        max_results: Optional[
            "capo_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_backup_gateway.types.next_token.NextToken"] = None,
    ) -> "capo_backup_gateway.types.list_gateways_output.ListGatewaysOutput":
        """<p>Lists backup gateways owned by an Amazon Web Services account in an Amazon Web Services Region. The returned list is ordered by gateway Amazon Resource Name (ARN).</p>

        Args:
            max_results: <p>The maximum number of gateways to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.list_gateways_input.ListGatewaysInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.list_gateways_output.ListGatewaysOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.list_gateways

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.list_gateways.list_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.list_gateways_input.ListGatewaysInput = {}
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

    def associate_gateway_to_server(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        server_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.associate_gateway_to_server_output.AssociateGatewayToServerOutput":
        """<p>Associates a backup gateway with your server. After you complete the association process, you can back up and restore your VMs through the gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>
            server_arn: <p>The Amazon Resource Name (ARN) of the server that hosts your virtual machines.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.associate_gateway_to_server_input.AssociateGatewayToServerInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.associate_gateway_to_server_output.AssociateGatewayToServerOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.associate_gateway_to_server

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.associate_gateway_to_server.associate_gateway_to_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.associate_gateway_to_server_input.AssociateGatewayToServerInput = {
            "gateway_arn": gateway_arn,
            "server_arn": server_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_gateway_from_server(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.disassociate_gateway_from_server_output.DisassociateGatewayFromServerOutput":
        """<p>Disassociates a backup gateway from the specified server. After the disassociation process finishes, the gateway can no longer access the virtual machines on the server.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to disassociate.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.disassociate_gateway_from_server_input.DisassociateGatewayFromServerInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.disassociate_gateway_from_server_output.DisassociateGatewayFromServerOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.disassociate_gateway_from_server

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.disassociate_gateway_from_server.disassociate_gateway_from_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.disassociate_gateway_from_server_input.DisassociateGatewayFromServerInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_maintenance_start_time(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        hour_of_day: "capo_backup_gateway.types.hour_of_day.HourOfDay",
        minute_of_hour: "capo_backup_gateway.types.minute_of_hour.MinuteOfHour",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        day_of_week: Optional["capo_backup_gateway.types.day_of_week.DayOfWeek"] = None,
        day_of_month: Optional[
            "capo_backup_gateway.types.day_of_month.DayOfMonth"
        ] = None,
    ) -> "capo_backup_gateway.types.put_maintenance_start_time_output.PutMaintenanceStartTimeOutput":
        """<p>Set the maintenance start time for a gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) for the gateway, used to specify its maintenance start time.</p>
            hour_of_day: <p>The hour of the day to start maintenance on a gateway.</p>
            minute_of_hour: <p>The minute of the hour to start maintenance on a gateway.</p>
            day_of_week: <p>The day of the week to start maintenance on a gateway.</p>
            day_of_month: <p>The day of the month start maintenance on a gateway.</p> <p>Valid values range from <code>Sunday</code> to <code>Saturday</code>.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.put_maintenance_start_time_input.PutMaintenanceStartTimeInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.put_maintenance_start_time_output.PutMaintenanceStartTimeOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.put_maintenance_start_time

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.put_maintenance_start_time.put_maintenance_start_time(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.put_maintenance_start_time_input.PutMaintenanceStartTimeInput = {
            "gateway_arn": gateway_arn,
            "hour_of_day": hour_of_day,
            "minute_of_hour": minute_of_hour,
        }
        if day_of_week is not None:
            input_["day_of_week"] = day_of_week
        if day_of_month is not None:
            input_["day_of_month"] = day_of_month

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def test_hypervisor_configuration(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        host: "capo_backup_gateway.types.host.Host",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        username: Optional["capo_backup_gateway.types.username.Username"] = None,
        password: Optional["capo_backup_gateway.types.password.Password"] = None,
    ) -> "capo_backup_gateway.types.test_hypervisor_configuration_output.TestHypervisorConfigurationOutput":
        """<p>Tests your hypervisor configuration to validate that backup gateway can connect with the hypervisor and its resources.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to the hypervisor to test.</p>
            host: <p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The username for the hypervisor.</p>
            password: <p>The password for the hypervisor.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.test_hypervisor_configuration_output.TestHypervisorConfigurationOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.test_hypervisor_configuration

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.test_hypervisor_configuration.test_hypervisor_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput = {
            "gateway_arn": gateway_arn,
            "host": host,
        }
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_gateway_software_now(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput":
        """<p>Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.</p> <note> <p>When you make this request, you get a <code>200 OK</code> success response immediately. However, it might take some time for the update to complete.</p> </note>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to be updated.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_software_now

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_software_now.update_gateway_software_now(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_bandwidth_rate_limit_schedule(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        bandwidth_rate_limit_intervals: "capo_backup_gateway.types.bandwidth_rate_limit_intervals.BandwidthRateLimitIntervals",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.put_bandwidth_rate_limit_schedule_output.PutBandwidthRateLimitScheduleOutput":
        """<p>This action sets the bandwidth rate limit schedule for a specified gateway. By default, gateways do not have a bandwidth rate limit schedule, which means no bandwidth rate limiting is in effect. Use this to initiate a gateway's bandwidth rate limit schedule.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway. Use the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListGateways.html"> <code>ListGateways</code> </a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>
            bandwidth_rate_limit_intervals: <p>An array containing bandwidth rate limit schedule intervals for a gateway. When no bandwidth rate limit intervals have been scheduled, the array is empty.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.put_bandwidth_rate_limit_schedule_input.PutBandwidthRateLimitScheduleInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.put_bandwidth_rate_limit_schedule_output.PutBandwidthRateLimitScheduleOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.put_bandwidth_rate_limit_schedule

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.put_bandwidth_rate_limit_schedule.put_bandwidth_rate_limit_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.put_bandwidth_rate_limit_schedule_input.PutBandwidthRateLimitScheduleInput = {
            "gateway_arn": gateway_arn,
            "bandwidth_rate_limit_intervals": bandwidth_rate_limit_intervals,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_bandwidth_rate_limit_schedule(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_bandwidth_rate_limit_schedule_output.GetBandwidthRateLimitScheduleOutput":
        """<p>Retrieves the bandwidth rate limit schedule for a specified gateway. By default, gateways do not have bandwidth rate limit schedules, which means no bandwidth rate limiting is in effect. Use this to get a gateway's bandwidth rate limit schedule.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway. Use the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListGateways.html"> <code>ListGateways</code> </a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.get_bandwidth_rate_limit_schedule_input.GetBandwidthRateLimitScheduleInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.get_bandwidth_rate_limit_schedule_output.GetBandwidthRateLimitScheduleOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_bandwidth_rate_limit_schedule

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.get_bandwidth_rate_limit_schedule.get_bandwidth_rate_limit_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.get_bandwidth_rate_limit_schedule_input.GetBandwidthRateLimitScheduleInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_hypervisor_configuration(
        self,
        name: "capo_backup_gateway.types.name.Name",
        host: "capo_backup_gateway.types.host.Host",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        username: Optional["capo_backup_gateway.types.username.Username"] = None,
        password: Optional["capo_backup_gateway.types.password.Password"] = None,
        kms_key_arn: Optional["capo_backup_gateway.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_backup_gateway.types.tags.Tags"] = None,
    ) -> "capo_backup_gateway.types.import_hypervisor_configuration_output.ImportHypervisorConfigurationOutput":
        """<p>Connect to a hypervisor by importing its configuration.</p>

        Args:
            name: <p>The name of the hypervisor.</p>
            host: <p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The username for the hypervisor.</p>
            password: <p>The password for the hypervisor.</p>
            kms_key_arn: <p>The Key Management Service for the hypervisor.</p>
            tags: <p>The tags of the hypervisor configuration to import.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.import_hypervisor_configuration_output.ImportHypervisorConfigurationOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.import_hypervisor_configuration

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.import_hypervisor_configuration.import_hypervisor_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput = {
            "name": name,
            "host": host,
        }
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_hypervisor(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_hypervisor_output.GetHypervisorOutput":
        """<p>This action requests information about the specified hypervisor to which the gateway will connect. A hypervisor is hardware, software, or firmware that creates and manages virtual machines, and allocates resources to them.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.get_hypervisor_input.GetHypervisorInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.get_hypervisor_output.GetHypervisorOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor.get_hypervisor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.get_hypervisor_input.GetHypervisorInput = {
            "hypervisor_arn": hypervisor_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_hypervisor(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        host: Optional["capo_backup_gateway.types.host.Host"] = None,
        username: Optional["capo_backup_gateway.types.username.Username"] = None,
        password: Optional["capo_backup_gateway.types.password.Password"] = None,
        name: Optional["capo_backup_gateway.types.name.Name"] = None,
        log_group_arn: Optional[
            "capo_backup_gateway.types.log_group_arn.LogGroupArn"
        ] = None,
    ) -> "capo_backup_gateway.types.update_hypervisor_output.UpdateHypervisorOutput":
        """<p>Updates a hypervisor metadata, including its host, username, and password. Specify which hypervisor to update using the Amazon Resource Name (ARN) of the hypervisor in your request.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor to update.</p>
            host: <p>The updated host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The updated username for the hypervisor.</p>
            password: <p>The updated password for the hypervisor.</p>
            name: <p>The updated name for the hypervisor</p>
            log_group_arn: <p>The Amazon Resource Name (ARN) of the group of gateways within the requested log.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.update_hypervisor_output.UpdateHypervisorOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.update_hypervisor

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.update_hypervisor.update_hypervisor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput = {
            "hypervisor_arn": hypervisor_arn
        }
        if host is not None:
            input_["host"] = host
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if name is not None:
            input_["name"] = name
        if log_group_arn is not None:
            input_["log_group_arn"] = log_group_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_hypervisor(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.delete_hypervisor_output.DeleteHypervisorOutput":
        """<p>Deletes a hypervisor.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor to delete.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.delete_hypervisor_input.DeleteHypervisorInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.delete_hypervisor_output.DeleteHypervisorOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.delete_hypervisor

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.delete_hypervisor.delete_hypervisor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.delete_hypervisor_input.DeleteHypervisorInput = {
            "hypervisor_arn": hypervisor_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_hypervisors(
        self,
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        max_results: Optional[
            "capo_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_backup_gateway.types.next_token.NextToken"] = None,
    ) -> "capo_backup_gateway.types.list_hypervisors_output.ListHypervisorsOutput":
        """<p>Lists your hypervisors.</p>

        Args:
            max_results: <p>The maximum number of hypervisors to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.list_hypervisors_input.ListHypervisorsInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.list_hypervisors_output.ListHypervisorsOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.list_hypervisors

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.list_hypervisors.list_hypervisors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.list_hypervisors_input.ListHypervisorsInput = {}
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

    def start_virtual_machines_metadata_sync(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.start_virtual_machines_metadata_sync_output.StartVirtualMachinesMetadataSyncOutput":
        """<p>This action sends a request to sync metadata across the specified virtual machines.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.start_virtual_machines_metadata_sync_input.StartVirtualMachinesMetadataSyncInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.start_virtual_machines_metadata_sync_output.StartVirtualMachinesMetadataSyncOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.start_virtual_machines_metadata_sync

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.start_virtual_machines_metadata_sync.start_virtual_machines_metadata_sync(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.start_virtual_machines_metadata_sync_input.StartVirtualMachinesMetadataSyncInput = {
            "hypervisor_arn": hypervisor_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_hypervisor_property_mappings(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        vmware_to_aws_tag_mappings: "capo_backup_gateway.types.vmware_to_aws_tag_mappings.VmwareToAwsTagMappings",
        iam_role_arn: "capo_backup_gateway.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.put_hypervisor_property_mappings_output.PutHypervisorPropertyMappingsOutput":
        """<p>This action sets the property mappings for the specified hypervisor. A hypervisor property mapping displays the relationship of entity properties available from the hypervisor to the properties available in Amazon Web Services.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>
            vmware_to_aws_tag_mappings: <p>This action requests the mappings of VMware tags to the Amazon Web Services tags.</p>
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.put_hypervisor_property_mappings_input.PutHypervisorPropertyMappingsInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.put_hypervisor_property_mappings_output.PutHypervisorPropertyMappingsOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.put_hypervisor_property_mappings

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.put_hypervisor_property_mappings.put_hypervisor_property_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.put_hypervisor_property_mappings_input.PutHypervisorPropertyMappingsInput = {
            "hypervisor_arn": hypervisor_arn,
            "vmware_to_aws_tag_mappings": vmware_to_aws_tag_mappings,
            "iam_role_arn": iam_role_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_hypervisor_property_mappings(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_hypervisor_property_mappings_output.GetHypervisorPropertyMappingsOutput":
        """<p>This action retrieves the property mappings for the specified hypervisor. A hypervisor property mapping displays the relationship of entity properties available from the hypervisor to the properties available in Amazon Web Services.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.get_hypervisor_property_mappings_input.GetHypervisorPropertyMappingsInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.get_hypervisor_property_mappings_output.GetHypervisorPropertyMappingsOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor_property_mappings

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor_property_mappings.get_hypervisor_property_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.get_hypervisor_property_mappings_input.GetHypervisorPropertyMappingsInput = {
            "hypervisor_arn": hypervisor_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_virtual_machine(
        self,
        resource_arn: "capo_backup_gateway.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_virtual_machine_output.GetVirtualMachineOutput":
        """<p>By providing the ARN (Amazon Resource Name), this API returns the virtual machine.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the virtual machine.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.get_virtual_machine_input.GetVirtualMachineInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.get_virtual_machine_output.GetVirtualMachineOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_virtual_machine

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.get_virtual_machine.get_virtual_machine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.get_virtual_machine_input.GetVirtualMachineInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_virtual_machines(
        self,
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        hypervisor_arn: Optional[
            "capo_backup_gateway.types.server_arn.ServerArn"
        ] = None,
        max_results: Optional[
            "capo_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_backup_gateway.types.next_token.NextToken"] = None,
    ) -> "capo_backup_gateway.types.list_virtual_machines_output.ListVirtualMachinesOutput":
        """<p>Lists your virtual machines.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor connected to your virtual machine.</p>
            max_results: <p>The maximum number of virtual machines to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.list_virtual_machines_input.ListVirtualMachinesInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.list_virtual_machines_output.ListVirtualMachinesOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.list_virtual_machines

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.list_virtual_machines.list_virtual_machines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_backup_gateway.types.list_virtual_machines_input.ListVirtualMachinesInput = {}
        if hypervisor_arn is not None:
            input_["hypervisor_arn"] = hypervisor_arn
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
