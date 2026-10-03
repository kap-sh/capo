"""Generated from Smithy shape ``com.amazonaws.outposts#OutpostsOlafService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_outposts._auth._signers
import capo_outposts._auth._sigv4
from capo_outposts._auth._identity import Credentials
from capo_outposts._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_outposts._auth._zapros_handler import AuthMiddleware
from capo_outposts._pagination import resolve_path as _resolve_path
from capo_outposts._services._aws_config import aws_config
from capo_outposts._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_outposts.types.account_id_list
    import capo_outposts.types.address
    import capo_outposts.types.address_type
    import capo_outposts.types.arn
    import capo_outposts.types.asset_id
    import capo_outposts.types.asset_id_input
    import capo_outposts.types.asset_id_list
    import capo_outposts.types.asset_info
    import capo_outposts.types.asset_instance
    import capo_outposts.types.asset_type_list
    import capo_outposts.types.auto_fill_idempotency_token
    import capo_outposts.types.availability_zone
    import capo_outposts.types.availability_zone_id
    import capo_outposts.types.availability_zone_id_list
    import capo_outposts.types.availability_zone_list
    import capo_outposts.types.aws_service_name_list
    import capo_outposts.types.blocking_instance
    import capo_outposts.types.cancel_capacity_task_input
    import capo_outposts.types.cancel_capacity_task_output
    import capo_outposts.types.cancel_order_input
    import capo_outposts.types.cancel_order_output
    import capo_outposts.types.capacity_task_id
    import capo_outposts.types.capacity_task_status_list
    import capo_outposts.types.capacity_task_summary
    import capo_outposts.types.catalog_item
    import capo_outposts.types.catalog_item_class_list
    import capo_outposts.types.city_list
    import capo_outposts.types.connection_id
    import capo_outposts.types.country_code
    import capo_outposts.types.country_code_list
    import capo_outposts.types.create_order_input
    import capo_outposts.types.create_order_output
    import capo_outposts.types.create_outpost_input
    import capo_outposts.types.create_outpost_output
    import capo_outposts.types.create_private_connectivity_config_input
    import capo_outposts.types.create_private_connectivity_config_output
    import capo_outposts.types.create_quote_input
    import capo_outposts.types.create_quote_output
    import capo_outposts.types.create_renewal_input
    import capo_outposts.types.create_renewal_output
    import capo_outposts.types.create_site_input
    import capo_outposts.types.create_site_output
    import capo_outposts.types.delete_outpost_input
    import capo_outposts.types.delete_outpost_output
    import capo_outposts.types.delete_quote_input
    import capo_outposts.types.delete_quote_output
    import capo_outposts.types.delete_site_input
    import capo_outposts.types.delete_site_output
    import capo_outposts.types.detailed_instance_type_item
    import capo_outposts.types.device_serial_number
    import capo_outposts.types.dry_run
    import capo_outposts.types.ec2_family_list
    import capo_outposts.types.fiber_optic_cable_type
    import capo_outposts.types.get_capacity_task_input
    import capo_outposts.types.get_capacity_task_output
    import capo_outposts.types.get_catalog_item_input
    import capo_outposts.types.get_catalog_item_output
    import capo_outposts.types.get_connection_request
    import capo_outposts.types.get_connection_response
    import capo_outposts.types.get_order_input
    import capo_outposts.types.get_order_output
    import capo_outposts.types.get_outpost_billing_information_input
    import capo_outposts.types.get_outpost_billing_information_output
    import capo_outposts.types.get_outpost_input
    import capo_outposts.types.get_outpost_instance_types_input
    import capo_outposts.types.get_outpost_instance_types_output
    import capo_outposts.types.get_outpost_output
    import capo_outposts.types.get_outpost_supported_instance_types_input
    import capo_outposts.types.get_outpost_supported_instance_types_output
    import capo_outposts.types.get_private_connectivity_config_input
    import capo_outposts.types.get_private_connectivity_config_output
    import capo_outposts.types.get_quote_input
    import capo_outposts.types.get_quote_output
    import capo_outposts.types.get_renewal_pricing_input
    import capo_outposts.types.get_renewal_pricing_output
    import capo_outposts.types.get_site_address_input
    import capo_outposts.types.get_site_address_output
    import capo_outposts.types.get_site_input
    import capo_outposts.types.get_site_output
    import capo_outposts.types.host_id_list
    import capo_outposts.types.instance_type_item
    import capo_outposts.types.instances_to_exclude
    import capo_outposts.types.life_cycle_status_list
    import capo_outposts.types.line_item_request_list_definition
    import capo_outposts.types.list_asset_instances_input
    import capo_outposts.types.list_asset_instances_output
    import capo_outposts.types.list_assets_input
    import capo_outposts.types.list_assets_output
    import capo_outposts.types.list_blocking_instances_for_capacity_task_input
    import capo_outposts.types.list_blocking_instances_for_capacity_task_output
    import capo_outposts.types.list_capacity_tasks_input
    import capo_outposts.types.list_capacity_tasks_output
    import capo_outposts.types.list_catalog_items_input
    import capo_outposts.types.list_catalog_items_output
    import capo_outposts.types.list_orderable_instance_types_input
    import capo_outposts.types.list_orderable_instance_types_output
    import capo_outposts.types.list_orders_input
    import capo_outposts.types.list_orders_output
    import capo_outposts.types.list_outposts_input
    import capo_outposts.types.list_outposts_output
    import capo_outposts.types.list_quotes_input
    import capo_outposts.types.list_quotes_output
    import capo_outposts.types.list_sites_input
    import capo_outposts.types.list_sites_output
    import capo_outposts.types.list_tags_for_resource_request
    import capo_outposts.types.list_tags_for_resource_response
    import capo_outposts.types.max_results1000
    import capo_outposts.types.maximum_supported_weight_lbs
    import capo_outposts.types.network_interface_device_index
    import capo_outposts.types.optical_standard
    import capo_outposts.types.order_id
    import capo_outposts.types.order_summary
    import capo_outposts.types.outpost
    import capo_outposts.types.outpost_description
    import capo_outposts.types.outpost_generation
    import capo_outposts.types.outpost_id
    import capo_outposts.types.outpost_identifier
    import capo_outposts.types.outpost_identifier_or_empty
    import capo_outposts.types.outpost_instance_type_list
    import capo_outposts.types.outpost_name
    import capo_outposts.types.payment_option
    import capo_outposts.types.payment_option_list
    import capo_outposts.types.payment_term
    import capo_outposts.types.payment_term_list
    import capo_outposts.types.power_connector
    import capo_outposts.types.power_draw_kva
    import capo_outposts.types.power_feed_drop
    import capo_outposts.types.power_phase
    import capo_outposts.types.quote_capacity_list
    import capo_outposts.types.quote_constraint_list
    import capo_outposts.types.quote_description
    import capo_outposts.types.quote_identifier
    import capo_outposts.types.quote_option_identifier
    import capo_outposts.types.quote_summary
    import capo_outposts.types.rack_physical_properties
    import capo_outposts.types.requested_instance_pools
    import capo_outposts.types.site
    import capo_outposts.types.site_description
    import capo_outposts.types.site_id
    import capo_outposts.types.site_name
    import capo_outposts.types.site_notes
    import capo_outposts.types.sku_code
    import capo_outposts.types.start_capacity_task_input
    import capo_outposts.types.start_capacity_task_output
    import capo_outposts.types.start_connection_request
    import capo_outposts.types.start_connection_response
    import capo_outposts.types.start_outpost_decommission_input
    import capo_outposts.types.start_outpost_decommission_output
    import capo_outposts.types.state_or_region_list
    import capo_outposts.types.status_list
    import capo_outposts.types.subscription
    import capo_outposts.types.supported_hardware_type
    import capo_outposts.types.supported_storage_list
    import capo_outposts.types.tag_key_list
    import capo_outposts.types.tag_map
    import capo_outposts.types.tag_resource_request
    import capo_outposts.types.tag_resource_response
    import capo_outposts.types.task_action_on_blocking_instances
    import capo_outposts.types.token
    import capo_outposts.types.untag_resource_request
    import capo_outposts.types.untag_resource_response
    import capo_outposts.types.update_outpost_input
    import capo_outposts.types.update_outpost_output
    import capo_outposts.types.update_quote_input
    import capo_outposts.types.update_quote_output
    import capo_outposts.types.update_site_address_input
    import capo_outposts.types.update_site_address_output
    import capo_outposts.types.update_site_input
    import capo_outposts.types.update_site_output
    import capo_outposts.types.update_site_rack_physical_properties_input
    import capo_outposts.types.update_site_rack_physical_properties_output
    import capo_outposts.types.uplink_count
    import capo_outposts.types.uplink_gbps
    import capo_outposts.types.validate_only
    import capo_outposts.types.vpc_information_list
    import capo_outposts.types.wire_guard_public_key


class OutpostsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class OutpostsClient:
    """A client for the ``Outposts`` service.

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
        self._config = OutpostsClientConfig(
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
        self, config_overrides: Optional[OutpostsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: OutpostsClientConfig = config_overrides or {}
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

    def cancel_capacity_task(
        self,
        capacity_task_id: "capo_outposts.types.capacity_task_id.CapacityTaskId",
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.cancel_capacity_task_output.CancelCapacityTaskOutput":
        """<p>Cancels the capacity task.</p>

        Args:
            capacity_task_id: <p>ID of the capacity task that you want to cancel.</p>
            outpost_identifier: <p>ID or ARN of the Outpost associated with the capacity task that you want to cancel.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.cancel_capacity_task_input.CancelCapacityTaskInput]",
        ) -> OperationResponse[
            "capo_outposts.types.cancel_capacity_task_output.CancelCapacityTaskOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.cancel_capacity_task

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.cancel_capacity_task.cancel_capacity_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.cancel_capacity_task_input.CancelCapacityTaskInput = {
            "capacity_task_id": capacity_task_id,
            "outpost_identifier": outpost_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_order(
        self,
        order_id: "capo_outposts.types.order_id.OrderId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.cancel_order_output.CancelOrderOutput":
        """<p>Cancels the specified order for an Outpost.</p>

        Args:
            order_id: <p> The ID of the order. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.cancel_order_input.CancelOrderInput]",
        ) -> OperationResponse[
            "capo_outposts.types.cancel_order_output.CancelOrderOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.cancel_order

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.cancel_order.cancel_order(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.cancel_order_input.CancelOrderInput = {
            "order_id": order_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_order(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        payment_option: "capo_outposts.types.payment_option.PaymentOption",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        quote_identifier: Optional[
            "capo_outposts.types.quote_identifier.QuoteIdentifier"
        ] = None,
        quote_option_identifier: Optional[
            "capo_outposts.types.quote_option_identifier.QuoteOptionIdentifier"
        ] = None,
        line_items: Optional[
            "capo_outposts.types.line_item_request_list_definition.LineItemRequestListDefinition"
        ] = None,
        payment_term: Optional["capo_outposts.types.payment_term.PaymentTerm"] = None,
    ) -> "capo_outposts.types.create_order_output.CreateOrderOutput":
        """<p>Creates an order for an Outpost.</p>

        Args:
            outpost_identifier: <p> The ID or the Amazon Resource Name (ARN) of the Outpost. </p>
            quote_identifier: <p>The ID of the quote to use for the order.</p>
            quote_option_identifier: <p>The ID of the quote option to use for the order.</p>
            line_items: <p>The line items that make up the order.</p>
            payment_option: <p>The payment option.</p>
            payment_term: <p>The payment terms.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded a service quota.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.create_order_input.CreateOrderInput]",
        ) -> OperationResponse[
            "capo_outposts.types.create_order_output.CreateOrderOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.create_order

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.create_order.create_order(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.create_order_input.CreateOrderInput = {
            "outpost_identifier": outpost_identifier,
            "payment_option": payment_option,
        }
        if quote_identifier is not None:
            input_["quote_identifier"] = quote_identifier
        if quote_option_identifier is not None:
            input_["quote_option_identifier"] = quote_option_identifier
        if line_items is not None:
            input_["line_items"] = line_items
        if payment_term is not None:
            input_["payment_term"] = payment_term

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_outpost(
        self,
        name: "capo_outposts.types.outpost_name.OutpostName",
        site_id: "capo_outposts.types.site_id.SiteId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        description: Optional[
            "capo_outposts.types.outpost_description.OutpostDescription"
        ] = None,
        availability_zone: Optional[
            "capo_outposts.types.availability_zone.AvailabilityZone"
        ] = None,
        availability_zone_id: Optional[
            "capo_outposts.types.availability_zone_id.AvailabilityZoneId"
        ] = None,
        tags: Optional["capo_outposts.types.tag_map.TagMap"] = None,
        supported_hardware_type: Optional[
            "capo_outposts.types.supported_hardware_type.SupportedHardwareType"
        ] = None,
    ) -> "capo_outposts.types.create_outpost_output.CreateOutpostOutput":
        """<p>Creates an Outpost.</p> <p>You can specify either an Availability one or an AZ ID.</p>

        Args:
            site_id: <p> The ID or the Amazon Resource Name (ARN) of the site. </p>
            tags: <p>The tags to apply to the Outpost.</p>
            supported_hardware_type: <p> The type of hardware for this Outpost. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded a service quota.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.create_outpost_input.CreateOutpostInput]",
        ) -> OperationResponse[
            "capo_outposts.types.create_outpost_output.CreateOutpostOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.create_outpost

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.create_outpost.create_outpost(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.create_outpost_input.CreateOutpostInput = {
            "name": name,
            "site_id": site_id,
        }
        if description is not None:
            input_["description"] = description
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if tags is not None:
            input_["tags"] = tags
        if supported_hardware_type is not None:
            input_["supported_hardware_type"] = supported_hardware_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_private_connectivity_config(
        self,
        outpost_id: "capo_outposts.types.outpost_id.OutpostId",
        vpc_information_list: "capo_outposts.types.vpc_information_list.VpcInformationList",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.create_private_connectivity_config_output.CreatePrivateConnectivityConfigOutput":
        """<p>Creates the private connectivity configuration for the specified Outpost. Private connectivity establishes a service link VPN connection between the Outpost and its home Amazon Web Services Region using a VPC and subnet that you specify, which allows the service link traffic to flow through your VPC and minimizes public internet exposure.</p>

        Args:
            outpost_id: <p>The ID or ARN of the Outpost.</p>
            vpc_information_list: <p>Information about the VPC used for private connectivity, including the VPC, its subnets, and an associated VPC endpoint. You can specify at most one entry.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.create_private_connectivity_config_input.CreatePrivateConnectivityConfigInput]",
        ) -> OperationResponse[
            "capo_outposts.types.create_private_connectivity_config_output.CreatePrivateConnectivityConfigOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.create_private_connectivity_config

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.create_private_connectivity_config.create_private_connectivity_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.create_private_connectivity_config_input.CreatePrivateConnectivityConfigInput = {
            "outpost_id": outpost_id,
            "vpc_information_list": vpc_information_list,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_quote(
        self,
        country_code: "capo_outposts.types.country_code.CountryCode",
        requested_capacities: "capo_outposts.types.quote_capacity_list.QuoteCapacityList",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        outpost_identifier: Optional[
            "capo_outposts.types.outpost_identifier.OutpostIdentifier"
        ] = None,
        requested_constraints: Optional[
            "capo_outposts.types.quote_constraint_list.QuoteConstraintList"
        ] = None,
        requested_payment_options: Optional[
            "capo_outposts.types.payment_option_list.PaymentOptionList"
        ] = None,
        requested_payment_terms: Optional[
            "capo_outposts.types.payment_term_list.PaymentTermList"
        ] = None,
        description: Optional[
            "capo_outposts.types.quote_description.QuoteDescription"
        ] = None,
    ) -> "capo_outposts.types.create_quote_output.CreateQuoteOutput":
        """<p>Creates a quote for an Outpost. A quote provides pricing and configuration options based on the requested capacity. You can optionally associate the quote with an existing Outpost or create a standalone quote by specifying only the country code and requested capacities.</p>

        Args:
            outpost_identifier: <p>The ID or ARN of the Outpost to associate with the quote. If not specified, the quote is created without an Outpost association.</p>
            country_code: <p>The country code for the Outpost site location.</p>
            requested_capacities: <p>The capacity requirements for the quote. Each entry specifies a capacity type (such as Amazon EC2), the unit, and the quantity. For Amazon EC2, the quantity is the number of additional instances to add to the Outpost. For Amazon EBS and Amazon S3, the quantity is the total desired end-state capacity of the Outpost.</p>
            requested_constraints: <p>The physical constraints for the quote, such as maximum number of racks, maximum power draw per rack, or maximum weight per rack.</p>
            requested_payment_options: <p>The payment options to include in the quote pricing. If not specified, all available payment options are returned.</p>
            requested_payment_terms: <p>The payment terms to include in the quote pricing. If not specified, all available payment terms are returned.</p>
            description: <p>A description for the quote.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.create_quote_input.CreateQuoteInput]",
        ) -> OperationResponse[
            "capo_outposts.types.create_quote_output.CreateQuoteOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.create_quote

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.create_quote.create_quote(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.create_quote_input.CreateQuoteInput = {
            "country_code": country_code,
            "requested_capacities": requested_capacities,
        }
        if outpost_identifier is not None:
            input_["outpost_identifier"] = outpost_identifier
        if requested_constraints is not None:
            input_["requested_constraints"] = requested_constraints
        if requested_payment_options is not None:
            input_["requested_payment_options"] = requested_payment_options
        if requested_payment_terms is not None:
            input_["requested_payment_terms"] = requested_payment_terms
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_renewal(
        self,
        payment_option: "capo_outposts.types.payment_option.PaymentOption",
        payment_term: "capo_outposts.types.payment_term.PaymentTerm",
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        client_token: Optional[
            "capo_outposts.types.auto_fill_idempotency_token.AutoFillIdempotencyToken"
        ] = None,
    ) -> "capo_outposts.types.create_renewal_output.CreateRenewalOutput":
        """<p>Creates a renewal contract for the specified Outpost.</p>

        Args:
            payment_option: <p>The payment option.</p>
            payment_term: <p>The payment term.</p>
            outpost_identifier: <p>The ID or ARN of the Outpost.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.create_renewal_input.CreateRenewalInput]",
        ) -> OperationResponse[
            "capo_outposts.types.create_renewal_output.CreateRenewalOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.create_renewal

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.create_renewal.create_renewal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.create_renewal_input.CreateRenewalInput = {
            "payment_option": payment_option,
            "payment_term": payment_term,
            "outpost_identifier": outpost_identifier,
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

    def create_site(
        self,
        name: "capo_outposts.types.site_name.SiteName",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        description: Optional[
            "capo_outposts.types.site_description.SiteDescription"
        ] = None,
        notes: Optional["capo_outposts.types.site_notes.SiteNotes"] = None,
        tags: Optional["capo_outposts.types.tag_map.TagMap"] = None,
        operating_address: Optional["capo_outposts.types.address.Address"] = None,
        shipping_address: Optional["capo_outposts.types.address.Address"] = None,
        rack_physical_properties: Optional[
            "capo_outposts.types.rack_physical_properties.RackPhysicalProperties"
        ] = None,
    ) -> "capo_outposts.types.create_site_output.CreateSiteOutput":
        """<p> Creates a site for an Outpost. </p>

        Args:
            notes: <p>Additional information that you provide about site access requirements, electrician scheduling, personal protective equipment, or regulation of equipment materials that could affect your installation process. </p>
            tags: <p> The tags to apply to a site. </p>
            operating_address: <p> The location to install and power on the hardware. This address might be different from the shipping address. </p>
            shipping_address: <p> The location to ship the hardware. This address might be different from the operating address. </p>
            rack_physical_properties: <p> Information about the physical and logistical details for the rack at this site. For more information about hardware requirements for racks, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#checklist">Network readiness checklist</a> in the Amazon Web Services Outposts User Guide. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded a service quota.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.create_site_input.CreateSiteInput]",
        ) -> OperationResponse[
            "capo_outposts.types.create_site_output.CreateSiteOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.create_site

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.create_site.create_site(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.create_site_input.CreateSiteInput = {"name": name}
        if description is not None:
            input_["description"] = description
        if notes is not None:
            input_["notes"] = notes
        if tags is not None:
            input_["tags"] = tags
        if operating_address is not None:
            input_["operating_address"] = operating_address
        if shipping_address is not None:
            input_["shipping_address"] = shipping_address
        if rack_physical_properties is not None:
            input_["rack_physical_properties"] = rack_physical_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_outpost(
        self,
        outpost_id: "capo_outposts.types.outpost_id.OutpostId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.delete_outpost_output.DeleteOutpostOutput":
        """<p>Deletes the specified Outpost.</p>

        Args:
            outpost_id: <p> The ID or ARN of the Outpost. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.delete_outpost_input.DeleteOutpostInput]",
        ) -> OperationResponse[
            "capo_outposts.types.delete_outpost_output.DeleteOutpostOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.delete_outpost

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.delete_outpost.delete_outpost(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.delete_outpost_input.DeleteOutpostInput = {
            "outpost_id": outpost_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_quote(
        self,
        quote_identifier: "capo_outposts.types.quote_identifier.QuoteIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.delete_quote_output.DeleteQuoteOutput":
        """<p>Deletes the specified quote.</p>

        Args:
            quote_identifier: <p>The ID of the quote.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.delete_quote_input.DeleteQuoteInput]",
        ) -> OperationResponse[
            "capo_outposts.types.delete_quote_output.DeleteQuoteOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.delete_quote

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.delete_quote.delete_quote(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.delete_quote_input.DeleteQuoteInput = {
            "quote_identifier": quote_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_site(
        self,
        site_id: "capo_outposts.types.site_id.SiteId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.delete_site_output.DeleteSiteOutput":
        """<p>Deletes the specified site.</p>

        Args:
            site_id: <p> The ID or the Amazon Resource Name (ARN) of the site. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.delete_site_input.DeleteSiteInput]",
        ) -> OperationResponse[
            "capo_outposts.types.delete_site_output.DeleteSiteOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.delete_site

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.delete_site.delete_site(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.delete_site_input.DeleteSiteInput = {
            "site_id": site_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_capacity_task(
        self,
        capacity_task_id: "capo_outposts.types.capacity_task_id.CapacityTaskId",
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.get_capacity_task_output.GetCapacityTaskOutput":
        """<p>Gets details of the specified capacity task.</p>

        Args:
            capacity_task_id: <p>ID of the capacity task.</p>
            outpost_identifier: <p>ID or ARN of the Outpost associated with the specified capacity task.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_capacity_task_input.GetCapacityTaskInput]",
        ) -> OperationResponse[
            "capo_outposts.types.get_capacity_task_output.GetCapacityTaskOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.get_capacity_task

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_capacity_task.get_capacity_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_capacity_task_input.GetCapacityTaskInput = {
            "capacity_task_id": capacity_task_id,
            "outpost_identifier": outpost_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_catalog_item(
        self,
        catalog_item_id: "capo_outposts.types.sku_code.SkuCode",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.get_catalog_item_output.GetCatalogItemOutput":
        """<p>Gets information about the specified catalog item.</p>

        Args:
            catalog_item_id: <p>The ID of the catalog item.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_catalog_item_input.GetCatalogItemInput]",
        ) -> OperationResponse[
            "capo_outposts.types.get_catalog_item_output.GetCatalogItemOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.get_catalog_item

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_catalog_item.get_catalog_item(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_catalog_item_input.GetCatalogItemInput = {
            "catalog_item_id": catalog_item_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_connection(
        self,
        connection_id: "capo_outposts.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.get_connection_response.GetConnectionResponse":
        """<note> <p> Amazon Web Services uses this action to install Outpost servers.</p> </note> <p> Gets information about the specified connection. </p> <p> Use CloudTrail to monitor this action or Amazon Web Services managed policy for Amazon Web Services Outposts to secure it. For more information, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/security-iam-awsmanpol.html"> Amazon Web Services managed policies for Amazon Web Services Outposts</a> and <a href="https://docs.aws.amazon.com/outposts/latest/userguide/logging-using-cloudtrail.html"> Logging Amazon Web Services Outposts API calls with Amazon Web Services CloudTrail</a> in the <i>Amazon Web Services Outposts User Guide</i>. </p>

        Args:
            connection_id: <p> The ID of the connection. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_connection_request.GetConnectionRequest]",
        ) -> OperationResponse[
            "capo_outposts.types.get_connection_response.GetConnectionResponse"
        ]:
            import capo_outposts._operations.outposts_olaf_service.get_connection

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_connection.get_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_connection_request.GetConnectionRequest = {
            "connection_id": connection_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_order(
        self,
        order_id: "capo_outposts.types.order_id.OrderId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.get_order_output.GetOrderOutput":
        """<p>Gets information about the specified order.</p>

        Args:
            order_id: <p>The ID of the order.</p>

        Raises:
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_order_input.GetOrderInput]",
        ) -> OperationResponse["capo_outposts.types.get_order_output.GetOrderOutput"]:
            import capo_outposts._operations.outposts_olaf_service.get_order

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_order.get_order(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_order_input.GetOrderInput = {
            "order_id": order_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_outpost(
        self,
        outpost_id: "capo_outposts.types.outpost_id.OutpostId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.get_outpost_output.GetOutpostOutput":
        """<p>Gets information about the specified Outpost.</p>

        Args:
            outpost_id: <p>The ID or ARN of the Outpost.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_outpost_input.GetOutpostInput]",
        ) -> OperationResponse[
            "capo_outposts.types.get_outpost_output.GetOutpostOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.get_outpost

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_outpost.get_outpost(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_outpost_input.GetOutpostInput = {
            "outpost_id": outpost_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_outpost_billing_information(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
    ) -> "capo_outposts.types.get_outpost_billing_information_output.GetOutpostBillingInformationOutput":
        """<p>Gets current and historical billing information about the specified Outpost.</p>

        Args:
            outpost_identifier: <p>The ID or ARN of the Outpost.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_outpost_billing_information_input.GetOutpostBillingInformationInput]",
        ) -> OperationResponse[
            "capo_outposts.types.get_outpost_billing_information_output.GetOutpostBillingInformationOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.get_outpost_billing_information

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_outpost_billing_information.get_outpost_billing_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_outpost_billing_information_input.GetOutpostBillingInformationInput = {
            "outpost_identifier": outpost_identifier
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

    def iter_get_outpost_billing_information(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
    ) -> "Iterator[capo_outposts.types.subscription.Subscription]":
        _token = next_token
        while True:
            _response = self.get_outpost_billing_information(
                outpost_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_outpost_instance_types(
        self,
        outpost_id: "capo_outposts.types.outpost_id.OutpostId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
    ) -> "capo_outposts.types.get_outpost_instance_types_output.GetOutpostInstanceTypesOutput":
        """<p>Gets the instance types for the specified Outpost.</p>

        Args:
            outpost_id: <p> The ID or ARN of the Outpost. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_outpost_instance_types_input.GetOutpostInstanceTypesInput]",
        ) -> OperationResponse[
            "capo_outposts.types.get_outpost_instance_types_output.GetOutpostInstanceTypesOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.get_outpost_instance_types

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_outpost_instance_types.get_outpost_instance_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_outpost_instance_types_input.GetOutpostInstanceTypesInput = {
            "outpost_id": outpost_id
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

    def iter_get_outpost_instance_types(
        self,
        outpost_id: "capo_outposts.types.outpost_id.OutpostId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
    ) -> "Iterator[capo_outposts.types.instance_type_item.InstanceTypeItem]":
        _token = next_token
        while True:
            _response = self.get_outpost_instance_types(
                outpost_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("instance_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_outpost_supported_instance_types(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        order_id: Optional["capo_outposts.types.order_id.OrderId"] = None,
        asset_id: Optional["capo_outposts.types.asset_id_input.AssetIdInput"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
    ) -> "capo_outposts.types.get_outpost_supported_instance_types_output.GetOutpostSupportedInstanceTypesOutput":
        """<p>Gets the instance types that an Outpost can support in <code>InstanceTypeCapacity</code>. This will generally include instance types that are not currently configured and therefore cannot be launched with the current Outpost capacity configuration.</p>

        Args:
            outpost_identifier: <p>The ID or ARN of the Outpost.</p>
            order_id: <p>The ID for the Amazon Web Services Outposts order.</p>
            asset_id: <p>The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_outpost_supported_instance_types_input.GetOutpostSupportedInstanceTypesInput]",
        ) -> OperationResponse[
            "capo_outposts.types.get_outpost_supported_instance_types_output.GetOutpostSupportedInstanceTypesOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.get_outpost_supported_instance_types

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_outpost_supported_instance_types.get_outpost_supported_instance_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_outpost_supported_instance_types_input.GetOutpostSupportedInstanceTypesInput = {
            "outpost_identifier": outpost_identifier
        }
        if order_id is not None:
            input_["order_id"] = order_id
        if asset_id is not None:
            input_["asset_id"] = asset_id
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

    def iter_get_outpost_supported_instance_types(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        order_id: Optional["capo_outposts.types.order_id.OrderId"] = None,
        asset_id: Optional["capo_outposts.types.asset_id_input.AssetIdInput"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
    ) -> "Iterator[capo_outposts.types.instance_type_item.InstanceTypeItem]":
        _token = next_token
        while True:
            _response = self.get_outpost_supported_instance_types(
                outpost_identifier,
                config_overrides=config_overrides,
                order_id=order_id,
                asset_id=asset_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("instance_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_private_connectivity_config(
        self,
        outpost_id: "capo_outposts.types.outpost_id.OutpostId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.get_private_connectivity_config_output.GetPrivateConnectivityConfigOutput":
        """<p>Gets the private connectivity configuration for the specified Outpost.</p>

        Args:
            outpost_id: <p>The ID or ARN of the Outpost.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_private_connectivity_config_input.GetPrivateConnectivityConfigInput]",
        ) -> OperationResponse[
            "capo_outposts.types.get_private_connectivity_config_output.GetPrivateConnectivityConfigOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.get_private_connectivity_config

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_private_connectivity_config.get_private_connectivity_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_private_connectivity_config_input.GetPrivateConnectivityConfigInput = {
            "outpost_id": outpost_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_quote(
        self,
        quote_identifier: "capo_outposts.types.quote_identifier.QuoteIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.get_quote_output.GetQuoteOutput":
        """<p>Gets information about the specified quote.</p>

        Args:
            quote_identifier: <p>The ID of the quote.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_quote_input.GetQuoteInput]",
        ) -> OperationResponse["capo_outposts.types.get_quote_output.GetQuoteOutput"]:
            import capo_outposts._operations.outposts_olaf_service.get_quote

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_quote.get_quote(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_quote_input.GetQuoteInput = {
            "quote_identifier": quote_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_renewal_pricing(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.get_renewal_pricing_output.GetRenewalPricingOutput":
        """<p>Gets all available renewal pricing options for the specified Outpost.</p>

        Args:
            outpost_identifier: <p>The ID or ARN of the Outpost.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_renewal_pricing_input.GetRenewalPricingInput]",
        ) -> OperationResponse[
            "capo_outposts.types.get_renewal_pricing_output.GetRenewalPricingOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.get_renewal_pricing

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_renewal_pricing.get_renewal_pricing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_renewal_pricing_input.GetRenewalPricingInput = {
            "outpost_identifier": outpost_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_site(
        self,
        site_id: "capo_outposts.types.site_id.SiteId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.get_site_output.GetSiteOutput":
        """<p>Gets information about the specified Outpost site.</p>

        Args:
            site_id: <p> The ID or the Amazon Resource Name (ARN) of the site. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_site_input.GetSiteInput]",
        ) -> OperationResponse["capo_outposts.types.get_site_output.GetSiteOutput"]:
            import capo_outposts._operations.outposts_olaf_service.get_site

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_site.get_site(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_site_input.GetSiteInput = {"site_id": site_id}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_site_address(
        self,
        site_id: "capo_outposts.types.site_id.SiteId",
        address_type: "capo_outposts.types.address_type.AddressType",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.get_site_address_output.GetSiteAddressOutput":
        """<p> Gets the site address of the specified site. </p>

        Args:
            site_id: <p> The ID or the Amazon Resource Name (ARN) of the site. </p>
            address_type: <p>The type of the address you request. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.get_site_address_input.GetSiteAddressInput]",
        ) -> OperationResponse[
            "capo_outposts.types.get_site_address_output.GetSiteAddressOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.get_site_address

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.get_site_address.get_site_address(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.get_site_address_input.GetSiteAddressInput = {
            "site_id": site_id,
            "address_type": address_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_asset_instances(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        asset_id_filter: Optional[
            "capo_outposts.types.asset_id_list.AssetIdList"
        ] = None,
        instance_type_filter: Optional[
            "capo_outposts.types.outpost_instance_type_list.OutpostInstanceTypeList"
        ] = None,
        account_id_filter: Optional[
            "capo_outposts.types.account_id_list.AccountIdList"
        ] = None,
        aws_service_filter: Optional[
            "capo_outposts.types.aws_service_name_list.AWSServiceNameList"
        ] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
    ) -> "capo_outposts.types.list_asset_instances_output.ListAssetInstancesOutput":
        """<p>A list of Amazon EC2 instances, belonging to all accounts, running on the specified Outpost. Does not include Amazon EBS or Amazon S3 instances.</p>

        Args:
            outpost_identifier: <p>The ID of the Outpost.</p>
            asset_id_filter: <p>Filters the results by asset ID.</p>
            instance_type_filter: <p>Filters the results by instance ID.</p>
            account_id_filter: <p>Filters the results by account ID.</p>
            aws_service_filter: <p>Filters the results by Amazon Web Services service.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_asset_instances_input.ListAssetInstancesInput]",
        ) -> OperationResponse[
            "capo_outposts.types.list_asset_instances_output.ListAssetInstancesOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.list_asset_instances

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_asset_instances.list_asset_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_asset_instances_input.ListAssetInstancesInput = {
            "outpost_identifier": outpost_identifier
        }
        if asset_id_filter is not None:
            input_["asset_id_filter"] = asset_id_filter
        if instance_type_filter is not None:
            input_["instance_type_filter"] = instance_type_filter
        if account_id_filter is not None:
            input_["account_id_filter"] = account_id_filter
        if aws_service_filter is not None:
            input_["aws_service_filter"] = aws_service_filter
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

    def iter_list_asset_instances(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        asset_id_filter: Optional[
            "capo_outposts.types.asset_id_list.AssetIdList"
        ] = None,
        instance_type_filter: Optional[
            "capo_outposts.types.outpost_instance_type_list.OutpostInstanceTypeList"
        ] = None,
        account_id_filter: Optional[
            "capo_outposts.types.account_id_list.AccountIdList"
        ] = None,
        aws_service_filter: Optional[
            "capo_outposts.types.aws_service_name_list.AWSServiceNameList"
        ] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
    ) -> "Iterator[capo_outposts.types.asset_instance.AssetInstance]":
        _token = next_token
        while True:
            _response = self.list_asset_instances(
                outpost_identifier,
                config_overrides=config_overrides,
                asset_id_filter=asset_id_filter,
                instance_type_filter=instance_type_filter,
                account_id_filter=account_id_filter,
                aws_service_filter=aws_service_filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("asset_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_assets(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        host_id_filter: Optional["capo_outposts.types.host_id_list.HostIdList"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        status_filter: Optional["capo_outposts.types.status_list.StatusList"] = None,
        asset_type_filter: Optional[
            "capo_outposts.types.asset_type_list.AssetTypeList"
        ] = None,
    ) -> "capo_outposts.types.list_assets_output.ListAssetsOutput":
        """<p>Lists the hardware assets for the specified Outpost.</p> <p>Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.</p>

        Args:
            outpost_identifier: <p> The ID or the Amazon Resource Name (ARN) of the Outpost. </p>
            host_id_filter: <p>Filters the results by the host ID of a Dedicated Host.</p>
            status_filter: <p>Filters the results by state.</p>
            asset_type_filter: <p>Filters the results by asset type.</p> <ul> <li> <p>COMPUTE - Server asset used for customer compute </p> </li> <li> <p>STORAGE - Server asset used by storage services </p> </li> <li> <p>POWERSHELF - Powershelf assets </p> </li> <li> <p>SWITCH - Switch assets </p> </li> <li> <p>NETWORKING - Asset managed by Amazon Web Services for networking purposes </p> </li> </ul>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_assets_input.ListAssetsInput]",
        ) -> OperationResponse[
            "capo_outposts.types.list_assets_output.ListAssetsOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.list_assets

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_assets.list_assets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_assets_input.ListAssetsInput = {
            "outpost_identifier": outpost_identifier
        }
        if host_id_filter is not None:
            input_["host_id_filter"] = host_id_filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status_filter is not None:
            input_["status_filter"] = status_filter
        if asset_type_filter is not None:
            input_["asset_type_filter"] = asset_type_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_assets(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        host_id_filter: Optional["capo_outposts.types.host_id_list.HostIdList"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        status_filter: Optional["capo_outposts.types.status_list.StatusList"] = None,
        asset_type_filter: Optional[
            "capo_outposts.types.asset_type_list.AssetTypeList"
        ] = None,
    ) -> "Iterator[capo_outposts.types.asset_info.AssetInfo]":
        _token = next_token
        while True:
            _response = self.list_assets(
                outpost_identifier,
                config_overrides=config_overrides,
                host_id_filter=host_id_filter,
                max_results=max_results,
                next_token=_token,
                status_filter=status_filter,
                asset_type_filter=asset_type_filter,
            )
            _page = _resolve_path(_response, ("assets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_blocking_instances_for_capacity_task(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        capacity_task_id: "capo_outposts.types.capacity_task_id.CapacityTaskId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
    ) -> "capo_outposts.types.list_blocking_instances_for_capacity_task_output.ListBlockingInstancesForCapacityTaskOutput":
        """<p>A list of Amazon EC2 instances running on the Outpost and belonging to the account that initiated the capacity task. Use this list to specify the instances you cannot stop to free up capacity to run the capacity task.</p>

        Args:
            outpost_identifier: <p>The ID or ARN of the Outpost associated with the specified capacity task.</p>
            capacity_task_id: <p>The ID of the capacity task.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_blocking_instances_for_capacity_task_input.ListBlockingInstancesForCapacityTaskInput]",
        ) -> OperationResponse[
            "capo_outposts.types.list_blocking_instances_for_capacity_task_output.ListBlockingInstancesForCapacityTaskOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.list_blocking_instances_for_capacity_task

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_blocking_instances_for_capacity_task.list_blocking_instances_for_capacity_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_blocking_instances_for_capacity_task_input.ListBlockingInstancesForCapacityTaskInput = {
            "outpost_identifier": outpost_identifier,
            "capacity_task_id": capacity_task_id,
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

    def iter_list_blocking_instances_for_capacity_task(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        capacity_task_id: "capo_outposts.types.capacity_task_id.CapacityTaskId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
    ) -> "Iterator[capo_outposts.types.blocking_instance.BlockingInstance]":
        _token = next_token
        while True:
            _response = self.list_blocking_instances_for_capacity_task(
                outpost_identifier,
                capacity_task_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("blocking_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_capacity_tasks(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        outpost_identifier_filter: Optional[
            "capo_outposts.types.outpost_identifier.OutpostIdentifier"
        ] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        capacity_task_status_filter: Optional[
            "capo_outposts.types.capacity_task_status_list.CapacityTaskStatusList"
        ] = None,
    ) -> "capo_outposts.types.list_capacity_tasks_output.ListCapacityTasksOutput":
        """<p>Lists the capacity tasks for your Amazon Web Services account.</p> <p>Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.</p>

        Args:
            outpost_identifier_filter: <p>Filters the results by an Outpost ID or an Outpost ARN.</p>
            capacity_task_status_filter: <p>A list of statuses. For example, <code>REQUESTED</code> or <code>WAITING_FOR_EVACUATION</code>.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_capacity_tasks_input.ListCapacityTasksInput]",
        ) -> OperationResponse[
            "capo_outposts.types.list_capacity_tasks_output.ListCapacityTasksOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.list_capacity_tasks

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_capacity_tasks.list_capacity_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_capacity_tasks_input.ListCapacityTasksInput = {}
        if outpost_identifier_filter is not None:
            input_["outpost_identifier_filter"] = outpost_identifier_filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if capacity_task_status_filter is not None:
            input_["capacity_task_status_filter"] = capacity_task_status_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_capacity_tasks(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        outpost_identifier_filter: Optional[
            "capo_outposts.types.outpost_identifier.OutpostIdentifier"
        ] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        capacity_task_status_filter: Optional[
            "capo_outposts.types.capacity_task_status_list.CapacityTaskStatusList"
        ] = None,
    ) -> "Iterator[capo_outposts.types.capacity_task_summary.CapacityTaskSummary]":
        _token = next_token
        while True:
            _response = self.list_capacity_tasks(
                config_overrides=config_overrides,
                outpost_identifier_filter=outpost_identifier_filter,
                max_results=max_results,
                next_token=_token,
                capacity_task_status_filter=capacity_task_status_filter,
            )
            _page = _resolve_path(_response, ("capacity_tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_catalog_items(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        item_class_filter: Optional[
            "capo_outposts.types.catalog_item_class_list.CatalogItemClassList"
        ] = None,
        supported_storage_filter: Optional[
            "capo_outposts.types.supported_storage_list.SupportedStorageList"
        ] = None,
        ec2_family_filter: Optional[
            "capo_outposts.types.ec2_family_list.EC2FamilyList"
        ] = None,
    ) -> "capo_outposts.types.list_catalog_items_output.ListCatalogItemsOutput":
        """<p>Lists the items in the catalog.</p> <p>Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.</p>

        Args:
            item_class_filter: <p>Filters the results by item class.</p>
            supported_storage_filter: <p>Filters the results by storage option.</p>
            ec2_family_filter: <p>Filters the results by EC2 family (for example, M5).</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_catalog_items_input.ListCatalogItemsInput]",
        ) -> OperationResponse[
            "capo_outposts.types.list_catalog_items_output.ListCatalogItemsOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.list_catalog_items

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_catalog_items.list_catalog_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_catalog_items_input.ListCatalogItemsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if item_class_filter is not None:
            input_["item_class_filter"] = item_class_filter
        if supported_storage_filter is not None:
            input_["supported_storage_filter"] = supported_storage_filter
        if ec2_family_filter is not None:
            input_["ec2_family_filter"] = ec2_family_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_catalog_items(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        item_class_filter: Optional[
            "capo_outposts.types.catalog_item_class_list.CatalogItemClassList"
        ] = None,
        supported_storage_filter: Optional[
            "capo_outposts.types.supported_storage_list.SupportedStorageList"
        ] = None,
        ec2_family_filter: Optional[
            "capo_outposts.types.ec2_family_list.EC2FamilyList"
        ] = None,
    ) -> "Iterator[capo_outposts.types.catalog_item.CatalogItem]":
        _token = next_token
        while True:
            _response = self.list_catalog_items(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                item_class_filter=item_class_filter,
                supported_storage_filter=supported_storage_filter,
                ec2_family_filter=ec2_family_filter,
            )
            _page = _resolve_path(_response, ("catalog_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_orderable_instance_types(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        outpost_generation_filter: Optional[
            "capo_outposts.types.outpost_generation.OutpostGeneration"
        ] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
    ) -> "capo_outposts.types.list_orderable_instance_types_output.ListOrderableInstanceTypesOutput":
        """<p>Lists the instance types that can be ordered for an Outpost. You can filter the results by Outpost generation.</p>

        Args:
            outpost_generation_filter: <p>Filters the results by Outpost generation. Specify <code>GENERATION_1</code> for first-generation rack deployments or <code>GENERATION_2</code> for second-generation rack deployments.</p>
            max_results: <p>The maximum page size.</p>
            next_token: <p>The pagination token.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_orderable_instance_types_input.ListOrderableInstanceTypesInput]",
        ) -> OperationResponse[
            "capo_outposts.types.list_orderable_instance_types_output.ListOrderableInstanceTypesOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.list_orderable_instance_types

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_orderable_instance_types.list_orderable_instance_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_orderable_instance_types_input.ListOrderableInstanceTypesInput = {}
        if outpost_generation_filter is not None:
            input_["outpost_generation_filter"] = outpost_generation_filter
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

    def iter_list_orderable_instance_types(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        outpost_generation_filter: Optional[
            "capo_outposts.types.outpost_generation.OutpostGeneration"
        ] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
    ) -> "Iterator[capo_outposts.types.detailed_instance_type_item.DetailedInstanceTypeItem]":
        _token = next_token
        while True:
            _response = self.list_orderable_instance_types(
                config_overrides=config_overrides,
                outpost_generation_filter=outpost_generation_filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("instance_types",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_orders(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        outpost_identifier_filter: Optional[
            "capo_outposts.types.outpost_identifier.OutpostIdentifier"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
    ) -> "capo_outposts.types.list_orders_output.ListOrdersOutput":
        """<p>Lists the Outpost orders for your Amazon Web Services account.</p>

        Args:
            outpost_identifier_filter: <p> The ID or the Amazon Resource Name (ARN) of the Outpost. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_orders_input.ListOrdersInput]",
        ) -> OperationResponse[
            "capo_outposts.types.list_orders_output.ListOrdersOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.list_orders

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_orders.list_orders(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_orders_input.ListOrdersInput = {}
        if outpost_identifier_filter is not None:
            input_["outpost_identifier_filter"] = outpost_identifier_filter
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

    def iter_list_orders(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        outpost_identifier_filter: Optional[
            "capo_outposts.types.outpost_identifier.OutpostIdentifier"
        ] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
    ) -> "Iterator[capo_outposts.types.order_summary.OrderSummary]":
        _token = next_token
        while True:
            _response = self.list_orders(
                config_overrides=config_overrides,
                outpost_identifier_filter=outpost_identifier_filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("orders",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_outposts(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        life_cycle_status_filter: Optional[
            "capo_outposts.types.life_cycle_status_list.LifeCycleStatusList"
        ] = None,
        availability_zone_filter: Optional[
            "capo_outposts.types.availability_zone_list.AvailabilityZoneList"
        ] = None,
        availability_zone_id_filter: Optional[
            "capo_outposts.types.availability_zone_id_list.AvailabilityZoneIdList"
        ] = None,
    ) -> "capo_outposts.types.list_outposts_output.ListOutpostsOutput":
        """<p>Lists the Outposts for your Amazon Web Services account.</p> <p>Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.</p>

        Args:
            life_cycle_status_filter: <p>Filters the results by the lifecycle status.</p>
            availability_zone_filter: <p>Filters the results by Availability Zone (for example, <code>us-east-1a</code>).</p>
            availability_zone_id_filter: <p>Filters the results by AZ ID (for example, <code>use1-az1</code>).</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_outposts_input.ListOutpostsInput]",
        ) -> OperationResponse[
            "capo_outposts.types.list_outposts_output.ListOutpostsOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.list_outposts

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_outposts.list_outposts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_outposts_input.ListOutpostsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if life_cycle_status_filter is not None:
            input_["life_cycle_status_filter"] = life_cycle_status_filter
        if availability_zone_filter is not None:
            input_["availability_zone_filter"] = availability_zone_filter
        if availability_zone_id_filter is not None:
            input_["availability_zone_id_filter"] = availability_zone_id_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_outposts(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        life_cycle_status_filter: Optional[
            "capo_outposts.types.life_cycle_status_list.LifeCycleStatusList"
        ] = None,
        availability_zone_filter: Optional[
            "capo_outposts.types.availability_zone_list.AvailabilityZoneList"
        ] = None,
        availability_zone_id_filter: Optional[
            "capo_outposts.types.availability_zone_id_list.AvailabilityZoneIdList"
        ] = None,
    ) -> "Iterator[capo_outposts.types.outpost.Outpost]":
        _token = next_token
        while True:
            _response = self.list_outposts(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                life_cycle_status_filter=life_cycle_status_filter,
                availability_zone_filter=availability_zone_filter,
                availability_zone_id_filter=availability_zone_id_filter,
            )
            _page = _resolve_path(_response, ("outposts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_quotes(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
    ) -> "capo_outposts.types.list_quotes_output.ListQuotesOutput":
        """<p>Lists the quotes for your Amazon Web Services account.</p>

        Args:
            next_token: <p>The pagination token.</p>
            max_results: <p>The maximum page size.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_quotes_input.ListQuotesInput]",
        ) -> OperationResponse[
            "capo_outposts.types.list_quotes_output.ListQuotesOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.list_quotes

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_quotes.list_quotes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_quotes_input.ListQuotesInput = {}
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

    def iter_list_quotes(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
    ) -> "Iterator[capo_outposts.types.quote_summary.QuoteSummary]":
        _token = next_token
        while True:
            _response = self.list_quotes(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("quotes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sites(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        operating_address_country_code_filter: Optional[
            "capo_outposts.types.country_code_list.CountryCodeList"
        ] = None,
        operating_address_state_or_region_filter: Optional[
            "capo_outposts.types.state_or_region_list.StateOrRegionList"
        ] = None,
        operating_address_city_filter: Optional[
            "capo_outposts.types.city_list.CityList"
        ] = None,
    ) -> "capo_outposts.types.list_sites_output.ListSitesOutput":
        """<p>Lists the Outpost sites for your Amazon Web Services account. Use filters to return specific results.</p> <p>Use filters to return specific results. If you specify multiple filters, the results include only the resources that match all of the specified filters. For a filter where you can specify multiple values, the results include items that match any of the values that you specify for the filter.</p>

        Args:
            operating_address_country_code_filter: <p>Filters the results by country code.</p>
            operating_address_state_or_region_filter: <p>Filters the results by state or region.</p>
            operating_address_city_filter: <p>Filters the results by city.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_sites_input.ListSitesInput]",
        ) -> OperationResponse["capo_outposts.types.list_sites_output.ListSitesOutput"]:
            import capo_outposts._operations.outposts_olaf_service.list_sites

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_sites.list_sites(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_sites_input.ListSitesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if operating_address_country_code_filter is not None:
            input_["operating_address_country_code_filter"] = (
                operating_address_country_code_filter
            )
        if operating_address_state_or_region_filter is not None:
            input_["operating_address_state_or_region_filter"] = (
                operating_address_state_or_region_filter
            )
        if operating_address_city_filter is not None:
            input_["operating_address_city_filter"] = operating_address_city_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_sites(
        self,
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        next_token: Optional["capo_outposts.types.token.Token"] = None,
        max_results: Optional[
            "capo_outposts.types.max_results1000.MaxResults1000"
        ] = None,
        operating_address_country_code_filter: Optional[
            "capo_outposts.types.country_code_list.CountryCodeList"
        ] = None,
        operating_address_state_or_region_filter: Optional[
            "capo_outposts.types.state_or_region_list.StateOrRegionList"
        ] = None,
        operating_address_city_filter: Optional[
            "capo_outposts.types.city_list.CityList"
        ] = None,
    ) -> "Iterator[capo_outposts.types.site.Site]":
        _token = next_token
        while True:
            _response = self.list_sites(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                operating_address_country_code_filter=operating_address_country_code_filter,
                operating_address_state_or_region_filter=operating_address_state_or_region_filter,
                operating_address_city_filter=operating_address_city_filter,
            )
            _page = _resolve_path(_response, ("sites",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_outposts.types.arn.Arn",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_outposts.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_outposts._operations.outposts_olaf_service.list_tags_for_resource

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_capacity_task(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        instance_pools: "capo_outposts.types.requested_instance_pools.RequestedInstancePools",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        order_id: Optional["capo_outposts.types.order_id.OrderId"] = None,
        asset_id: Optional["capo_outposts.types.asset_id_input.AssetIdInput"] = None,
        instances_to_exclude: Optional[
            "capo_outposts.types.instances_to_exclude.InstancesToExclude"
        ] = None,
        dry_run: Optional["capo_outposts.types.dry_run.DryRun"] = None,
        task_action_on_blocking_instances: Optional[
            "capo_outposts.types.task_action_on_blocking_instances.TaskActionOnBlockingInstances"
        ] = None,
    ) -> "capo_outposts.types.start_capacity_task_output.StartCapacityTaskOutput":
        """<p>Starts the specified capacity task. You can have one active capacity task for each order and each Outpost.</p>

        Args:
            outpost_identifier: <p>The ID or ARN of the Outposts associated with the specified capacity task.</p>
            order_id: <p>The ID of the Amazon Web Services Outposts order associated with the specified capacity task.</p>
            asset_id: <p>The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>
            instance_pools: <p>The instance pools specified in the capacity task.</p>
            instances_to_exclude: <p>List of user-specified running instances that must not be stopped in order to free up the capacity needed to run the capacity task.</p>
            dry_run: <p>You can request a dry run to determine if the instance type and instance size changes is above or below available instance capacity. Requesting a dry run does not make any changes to your plan.</p>
            task_action_on_blocking_instances: <p>Specify one of the following options in case an instance is blocking the capacity task from running.</p> <ul> <li> <p> <code>WAIT_FOR_EVACUATION</code> - Checks every 10 minutes over 48 hours to determine if instances have stopped and capacity is available to complete the task.</p> </li> <li> <p> <code>FAIL_TASK</code> - The capacity task fails.</p> </li> </ul>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.start_capacity_task_input.StartCapacityTaskInput]",
        ) -> OperationResponse[
            "capo_outposts.types.start_capacity_task_output.StartCapacityTaskOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.start_capacity_task

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.start_capacity_task.start_capacity_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.start_capacity_task_input.StartCapacityTaskInput = {
            "outpost_identifier": outpost_identifier,
            "instance_pools": instance_pools,
        }
        if order_id is not None:
            input_["order_id"] = order_id
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if instances_to_exclude is not None:
            input_["instances_to_exclude"] = instances_to_exclude
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if task_action_on_blocking_instances is not None:
            input_["task_action_on_blocking_instances"] = (
                task_action_on_blocking_instances
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_connection(
        self,
        asset_id: "capo_outposts.types.asset_id.AssetId",
        client_public_key: "capo_outposts.types.wire_guard_public_key.WireGuardPublicKey",
        network_interface_device_index: "capo_outposts.types.network_interface_device_index.NetworkInterfaceDeviceIndex",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        device_serial_number: Optional[
            "capo_outposts.types.device_serial_number.DeviceSerialNumber"
        ] = None,
    ) -> "capo_outposts.types.start_connection_response.StartConnectionResponse":
        """<note> <p> Amazon Web Services uses this action to install Outpost servers.</p> </note> <p> Starts the connection required for Outpost server installation. </p> <p> Use CloudTrail to monitor this action or Amazon Web Services managed policy for Amazon Web Services Outposts to secure it. For more information, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/security-iam-awsmanpol.html"> Amazon Web Services managed policies for Amazon Web Services Outposts</a> and <a href="https://docs.aws.amazon.com/outposts/latest/userguide/logging-using-cloudtrail.html"> Logging Amazon Web Services Outposts API calls with Amazon Web Services CloudTrail</a> in the <i>Amazon Web Services Outposts User Guide</i>. </p>

        Args:
            device_serial_number: <p> The serial number of the dongle. </p>
            asset_id: <p> The ID of the Outpost server.</p>
            client_public_key: <p> The public key of the client. </p>
            network_interface_device_index: <p> The device index of the network interface on the Outpost server. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.start_connection_request.StartConnectionRequest]",
        ) -> OperationResponse[
            "capo_outposts.types.start_connection_response.StartConnectionResponse"
        ]:
            import capo_outposts._operations.outposts_olaf_service.start_connection

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.start_connection.start_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.start_connection_request.StartConnectionRequest = {
            "asset_id": asset_id,
            "client_public_key": client_public_key,
            "network_interface_device_index": network_interface_device_index,
        }
        if device_serial_number is not None:
            input_["device_serial_number"] = device_serial_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_outpost_decommission(
        self,
        outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        validate_only: Optional[
            "capo_outposts.types.validate_only.ValidateOnly"
        ] = None,
    ) -> "capo_outposts.types.start_outpost_decommission_output.StartOutpostDecommissionOutput":
        """<p>Starts the decommission process to return the Outposts racks or servers.</p>

        Args:
            outpost_identifier: <p>The ID or ARN of the Outpost that you want to decommission.</p>
            validate_only: <p>Validates the request without starting the decommission process.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.start_outpost_decommission_input.StartOutpostDecommissionInput]",
        ) -> OperationResponse[
            "capo_outposts.types.start_outpost_decommission_output.StartOutpostDecommissionOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.start_outpost_decommission

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.start_outpost_decommission.start_outpost_decommission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.start_outpost_decommission_input.StartOutpostDecommissionInput = {
            "outpost_identifier": outpost_identifier
        }
        if validate_only is not None:
            input_["validate_only"] = validate_only

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_outposts.types.arn.Arn",
        tags: "capo_outposts.types.tag_map.TagMap",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags to add to the resource.</p>

        Raises:
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_outposts.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_outposts._operations.outposts_olaf_service.tag_resource

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_outposts.types.arn.Arn",
        tag_keys: "capo_outposts.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys.</p>

        Raises:
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_outposts.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_outposts._operations.outposts_olaf_service.untag_resource

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.untag_resource_request.UntagResourceRequest = {
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

    def update_outpost(
        self,
        outpost_id: "capo_outposts.types.outpost_id.OutpostId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        name: Optional["capo_outposts.types.outpost_name.OutpostName"] = None,
        description: Optional[
            "capo_outposts.types.outpost_description.OutpostDescription"
        ] = None,
        supported_hardware_type: Optional[
            "capo_outposts.types.supported_hardware_type.SupportedHardwareType"
        ] = None,
    ) -> "capo_outposts.types.update_outpost_output.UpdateOutpostOutput":
        """<p> Updates an Outpost. </p>

        Args:
            outpost_id: <p> The ID or ARN of the Outpost. </p>
            supported_hardware_type: <p> The type of hardware for this Outpost. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.update_outpost_input.UpdateOutpostInput]",
        ) -> OperationResponse[
            "capo_outposts.types.update_outpost_output.UpdateOutpostOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.update_outpost

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.update_outpost.update_outpost(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.update_outpost_input.UpdateOutpostInput = {
            "outpost_id": outpost_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if supported_hardware_type is not None:
            input_["supported_hardware_type"] = supported_hardware_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_quote(
        self,
        quote_identifier: "capo_outposts.types.quote_identifier.QuoteIdentifier",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        outpost_identifier: Optional[
            "capo_outposts.types.outpost_identifier_or_empty.OutpostIdentifierOrEmpty"
        ] = None,
        country_code: Optional["capo_outposts.types.country_code.CountryCode"] = None,
        requested_capacities: Optional[
            "capo_outposts.types.quote_capacity_list.QuoteCapacityList"
        ] = None,
        requested_constraints: Optional[
            "capo_outposts.types.quote_constraint_list.QuoteConstraintList"
        ] = None,
        requested_payment_options: Optional[
            "capo_outposts.types.payment_option_list.PaymentOptionList"
        ] = None,
        requested_payment_terms: Optional[
            "capo_outposts.types.payment_term_list.PaymentTermList"
        ] = None,
        description: Optional[
            "capo_outposts.types.quote_description.QuoteDescription"
        ] = None,
    ) -> "capo_outposts.types.update_quote_output.UpdateQuoteOutput":
        """<p>Updates the specified quote. You can modify the requested capacities, constraints, payment options, payment terms, or Outpost association.</p>

        Args:
            quote_identifier: <p>The ID of the quote.</p>
            outpost_identifier: <p>The ID or ARN of the Outpost to associate with the quote. Specify an empty string to remove the Outpost association.</p>
            country_code: <p>The country code for the Outpost site location.</p>
            requested_capacities: <p>The updated capacity requirements for the quote.</p>
            requested_constraints: <p>The updated physical constraints for the quote.</p>
            requested_payment_options: <p>The updated payment options to include in the quote pricing.</p>
            requested_payment_terms: <p>The updated payment terms to include in the quote pricing.</p>
            description: <p>A description for the quote.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.update_quote_input.UpdateQuoteInput]",
        ) -> OperationResponse[
            "capo_outposts.types.update_quote_output.UpdateQuoteOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.update_quote

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.update_quote.update_quote(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.update_quote_input.UpdateQuoteInput = {
            "quote_identifier": quote_identifier
        }
        if outpost_identifier is not None:
            input_["outpost_identifier"] = outpost_identifier
        if country_code is not None:
            input_["country_code"] = country_code
        if requested_capacities is not None:
            input_["requested_capacities"] = requested_capacities
        if requested_constraints is not None:
            input_["requested_constraints"] = requested_constraints
        if requested_payment_options is not None:
            input_["requested_payment_options"] = requested_payment_options
        if requested_payment_terms is not None:
            input_["requested_payment_terms"] = requested_payment_terms
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_site(
        self,
        site_id: "capo_outposts.types.site_id.SiteId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        name: Optional["capo_outposts.types.site_name.SiteName"] = None,
        description: Optional[
            "capo_outposts.types.site_description.SiteDescription"
        ] = None,
        notes: Optional["capo_outposts.types.site_notes.SiteNotes"] = None,
    ) -> "capo_outposts.types.update_site_output.UpdateSiteOutput":
        """<p>Updates the specified site.</p>

        Args:
            site_id: <p> The ID or the Amazon Resource Name (ARN) of the site. </p>
            notes: <p>Notes about a site.</p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.update_site_input.UpdateSiteInput]",
        ) -> OperationResponse[
            "capo_outposts.types.update_site_output.UpdateSiteOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.update_site

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.update_site.update_site(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.update_site_input.UpdateSiteInput = {
            "site_id": site_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if notes is not None:
            input_["notes"] = notes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_site_address(
        self,
        site_id: "capo_outposts.types.site_id.SiteId",
        address_type: "capo_outposts.types.address_type.AddressType",
        address: "capo_outposts.types.address.Address",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
    ) -> "capo_outposts.types.update_site_address_output.UpdateSiteAddressOutput":
        """<p>Updates the address of the specified site.</p> <p>You can't update a site address if there is an order in progress. You must wait for the order to complete or cancel the order.</p> <p>You can update the operating address before you place an order at the site, or after all Outposts that belong to the site have been deactivated.</p>

        Args:
            site_id: <p> The ID or the Amazon Resource Name (ARN) of the site. </p>
            address_type: <p> The type of the address. </p>
            address: <p> The address for the site. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.update_site_address_input.UpdateSiteAddressInput]",
        ) -> OperationResponse[
            "capo_outposts.types.update_site_address_output.UpdateSiteAddressOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.update_site_address

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.update_site_address.update_site_address(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.update_site_address_input.UpdateSiteAddressInput = {
            "site_id": site_id,
            "address_type": address_type,
            "address": address,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_site_rack_physical_properties(
        self,
        site_id: "capo_outposts.types.site_id.SiteId",
        *,
        config_overrides: Optional[OutpostsClientConfig] = None,
        power_draw_kva: Optional[
            "capo_outposts.types.power_draw_kva.PowerDrawKva"
        ] = None,
        power_phase: Optional["capo_outposts.types.power_phase.PowerPhase"] = None,
        power_connector: Optional[
            "capo_outposts.types.power_connector.PowerConnector"
        ] = None,
        power_feed_drop: Optional[
            "capo_outposts.types.power_feed_drop.PowerFeedDrop"
        ] = None,
        uplink_gbps: Optional["capo_outposts.types.uplink_gbps.UplinkGbps"] = None,
        uplink_count: Optional["capo_outposts.types.uplink_count.UplinkCount"] = None,
        fiber_optic_cable_type: Optional[
            "capo_outposts.types.fiber_optic_cable_type.FiberOpticCableType"
        ] = None,
        optical_standard: Optional[
            "capo_outposts.types.optical_standard.OpticalStandard"
        ] = None,
        maximum_supported_weight_lbs: Optional[
            "capo_outposts.types.maximum_supported_weight_lbs.MaximumSupportedWeightLbs"
        ] = None,
    ) -> "capo_outposts.types.update_site_rack_physical_properties_output.UpdateSiteRackPhysicalPropertiesOutput":
        """<p>Update the physical and logistical details for a rack at a site. For more information about hardware requirements for racks, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#checklist">Network readiness checklist</a> in the Amazon Web Services Outposts User Guide. </p> <p>To update a rack at a site with an order of <code>IN_PROGRESS</code>, you must wait for the order to complete or cancel the order.</p>

        Args:
            site_id: <p> The ID or the Amazon Resource Name (ARN) of the site. </p>
            power_draw_kva: <p>The power draw, in kVA, available at the hardware placement position for the rack.</p>
            power_phase: <p>The power option that you can provide for hardware. </p> <ul> <li> <p>Single-phase AC feed: 200 V to 277 V, 50 Hz or 60 Hz</p> </li> <li> <p>Three-phase AC feed: 346 V to 480 V, 50 Hz or 60 Hz</p> </li> </ul>
            power_connector: <p>The power connector that Amazon Web Services should plan to provide for connections to the hardware. Note the correlation between <code>PowerPhase</code> and <code>PowerConnector</code>. </p> <ul> <li> <p>Single-phase AC feed</p> <ul> <li> <p> <b>L6-30P</b> – (common in US); 30A; single phase</p> </li> <li> <p> <b>IEC309 (blue)</b> – P+N+E, 6hr; 32 A; single phase</p> </li> </ul> </li> <li> <p>Three-phase AC feed</p> <ul> <li> <p> <b>AH530P7W (red)</b> – 3P+N+E, 7hr; 30A; three phase</p> </li> <li> <p> <b>AH532P6W (red)</b> – 3P+N+E, 6hr; 32A; three phase</p> </li> <li> <p> <b>CS8365C</b> – (common in US); 3P+E, 50A; three phase</p> </li> </ul> </li> </ul>
            power_feed_drop: <p>Indicates whether the power feed comes above or below the rack. </p>
            uplink_gbps: <p>The uplink speed the rack should support for the connection to the Region. </p>
            uplink_count: <p>Racks come with two Outpost network devices. Depending on the supported uplink speed at the site, the Outpost network devices provide a variable number of uplinks. Specify the number of uplinks for each Outpost network device that you intend to use to connect the rack to your network. Note the correlation between <code>UplinkGbps</code> and <code>UplinkCount</code>. </p> <ul> <li> <p>1Gbps - Uplinks available: 1, 2, 4, 6, 8</p> </li> <li> <p>10Gbps - Uplinks available: 1, 2, 4, 8, 12, 16</p> </li> <li> <p>40 and 100 Gbps- Uplinks available: 1, 2, 4</p> </li> </ul>
            fiber_optic_cable_type: <p>The type of fiber that you will use to attach the Outpost to your network. </p>
            optical_standard: <p>The type of optical standard that you will use to attach the Outpost to your network. This field is dependent on uplink speed, fiber type, and distance to the upstream device. For more information about networking requirements for racks, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#facility-networking">Network</a> in the Amazon Web Services Outposts User Guide. </p> <ul> <li> <p> <code>OPTIC_10GBASE_SR</code>: 10GBASE-SR</p> </li> <li> <p> <code>OPTIC_10GBASE_IR</code>: 10GBASE-IR</p> </li> <li> <p> <code>OPTIC_10GBASE_LR</code>: 10GBASE-LR</p> </li> <li> <p> <code>OPTIC_40GBASE_SR</code>: 40GBASE-SR</p> </li> <li> <p> <code>OPTIC_40GBASE_ESR</code>: 40GBASE-ESR</p> </li> <li> <p> <code>OPTIC_40GBASE_IR4_LR4L</code>: 40GBASE-IR (LR4L)</p> </li> <li> <p> <code>OPTIC_40GBASE_LR4</code>: 40GBASE-LR4</p> </li> <li> <p> <code>OPTIC_100GBASE_SR4</code>: 100GBASE-SR4</p> </li> <li> <p> <code>OPTIC_100GBASE_CWDM4</code>: 100GBASE-CWDM4</p> </li> <li> <p> <code>OPTIC_100GBASE_LR4</code>: 100GBASE-LR4</p> </li> <li> <p> <code>OPTIC_100G_PSM4_MSA</code>: 100G PSM4 MSA</p> </li> <li> <p> <code>OPTIC_1000BASE_LX</code>: 1000Base-LX</p> </li> <li> <p> <code>OPTIC_1000BASE_SX</code> : 1000Base-SX</p> </li> </ul>
            maximum_supported_weight_lbs: <p>The maximum rack weight that this site can support. <code>NO_LIMIT</code> is over 2000lbs. </p>

        Raises:
            capo_outposts.errors.access_denied_exception.AccessDeniedException: <p>You do not have permission to perform this operation.</p>
            capo_outposts.errors.conflict_exception.ConflictException: <p>Updating or deleting this resource can cause an inconsistent state.</p>
            capo_outposts.errors.internal_server_exception.InternalServerException: <p>An internal error has occurred.</p>
            capo_outposts.errors.not_found_exception.NotFoundException: <p>The specified request is not valid.</p>
            capo_outposts.errors.validation_exception.ValidationException: <p>A parameter is not valid.</p>
            capo_outposts.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_outposts.types.update_site_rack_physical_properties_input.UpdateSiteRackPhysicalPropertiesInput]",
        ) -> OperationResponse[
            "capo_outposts.types.update_site_rack_physical_properties_output.UpdateSiteRackPhysicalPropertiesOutput"
        ]:
            import capo_outposts._operations.outposts_olaf_service.update_site_rack_physical_properties

            output, http_response = (
                capo_outposts._operations.outposts_olaf_service.update_site_rack_physical_properties.update_site_rack_physical_properties(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_outposts.types.update_site_rack_physical_properties_input.UpdateSiteRackPhysicalPropertiesInput = {
            "site_id": site_id
        }
        if power_draw_kva is not None:
            input_["power_draw_kva"] = power_draw_kva
        if power_phase is not None:
            input_["power_phase"] = power_phase
        if power_connector is not None:
            input_["power_connector"] = power_connector
        if power_feed_drop is not None:
            input_["power_feed_drop"] = power_feed_drop
        if uplink_gbps is not None:
            input_["uplink_gbps"] = uplink_gbps
        if uplink_count is not None:
            input_["uplink_count"] = uplink_count
        if fiber_optic_cable_type is not None:
            input_["fiber_optic_cable_type"] = fiber_optic_cable_type
        if optical_standard is not None:
            input_["optical_standard"] = optical_standard
        if maximum_supported_weight_lbs is not None:
            input_["maximum_supported_weight_lbs"] = maximum_supported_weight_lbs

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
