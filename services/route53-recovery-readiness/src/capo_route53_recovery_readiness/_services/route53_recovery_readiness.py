"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#Route53RecoveryReadiness``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_route53_recovery_readiness._auth._signers
import capo_route53_recovery_readiness._auth._sigv4
from capo_route53_recovery_readiness._auth._identity import Credentials
from capo_route53_recovery_readiness._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_route53_recovery_readiness._auth._zapros_handler import AuthMiddleware
from capo_route53_recovery_readiness._pagination import resolve_path as _resolve_path
from capo_route53_recovery_readiness._services._aws_config import aws_config
from capo_route53_recovery_readiness._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__list_of__string
    import capo_route53_recovery_readiness.types.__list_of_resource
    import capo_route53_recovery_readiness.types.__string
    import capo_route53_recovery_readiness.types.__string_pattern_awsa_za_z09_a_za_z09
    import capo_route53_recovery_readiness.types.cell_output
    import capo_route53_recovery_readiness.types.create_cell_request
    import capo_route53_recovery_readiness.types.create_cell_response
    import capo_route53_recovery_readiness.types.create_cross_account_authorization_request
    import capo_route53_recovery_readiness.types.create_cross_account_authorization_response
    import capo_route53_recovery_readiness.types.create_readiness_check_request
    import capo_route53_recovery_readiness.types.create_readiness_check_response
    import capo_route53_recovery_readiness.types.create_recovery_group_request
    import capo_route53_recovery_readiness.types.create_recovery_group_response
    import capo_route53_recovery_readiness.types.create_resource_set_request
    import capo_route53_recovery_readiness.types.create_resource_set_response
    import capo_route53_recovery_readiness.types.cross_account_authorization
    import capo_route53_recovery_readiness.types.delete_cell_request
    import capo_route53_recovery_readiness.types.delete_cross_account_authorization_request
    import capo_route53_recovery_readiness.types.delete_cross_account_authorization_response
    import capo_route53_recovery_readiness.types.delete_readiness_check_request
    import capo_route53_recovery_readiness.types.delete_recovery_group_request
    import capo_route53_recovery_readiness.types.delete_resource_set_request
    import capo_route53_recovery_readiness.types.get_architecture_recommendations_request
    import capo_route53_recovery_readiness.types.get_architecture_recommendations_response
    import capo_route53_recovery_readiness.types.get_cell_readiness_summary_request
    import capo_route53_recovery_readiness.types.get_cell_readiness_summary_response
    import capo_route53_recovery_readiness.types.get_cell_request
    import capo_route53_recovery_readiness.types.get_cell_response
    import capo_route53_recovery_readiness.types.get_readiness_check_request
    import capo_route53_recovery_readiness.types.get_readiness_check_resource_status_request
    import capo_route53_recovery_readiness.types.get_readiness_check_resource_status_response
    import capo_route53_recovery_readiness.types.get_readiness_check_response
    import capo_route53_recovery_readiness.types.get_readiness_check_status_request
    import capo_route53_recovery_readiness.types.get_readiness_check_status_response
    import capo_route53_recovery_readiness.types.get_recovery_group_readiness_summary_request
    import capo_route53_recovery_readiness.types.get_recovery_group_readiness_summary_response
    import capo_route53_recovery_readiness.types.get_recovery_group_request
    import capo_route53_recovery_readiness.types.get_recovery_group_response
    import capo_route53_recovery_readiness.types.get_resource_set_request
    import capo_route53_recovery_readiness.types.get_resource_set_response
    import capo_route53_recovery_readiness.types.list_cells_request
    import capo_route53_recovery_readiness.types.list_cells_response
    import capo_route53_recovery_readiness.types.list_cross_account_authorizations_request
    import capo_route53_recovery_readiness.types.list_cross_account_authorizations_response
    import capo_route53_recovery_readiness.types.list_readiness_checks_request
    import capo_route53_recovery_readiness.types.list_readiness_checks_response
    import capo_route53_recovery_readiness.types.list_recovery_groups_request
    import capo_route53_recovery_readiness.types.list_recovery_groups_response
    import capo_route53_recovery_readiness.types.list_resource_sets_request
    import capo_route53_recovery_readiness.types.list_resource_sets_response
    import capo_route53_recovery_readiness.types.list_rules_output
    import capo_route53_recovery_readiness.types.list_rules_request
    import capo_route53_recovery_readiness.types.list_rules_response
    import capo_route53_recovery_readiness.types.list_tags_for_resources_request
    import capo_route53_recovery_readiness.types.list_tags_for_resources_response
    import capo_route53_recovery_readiness.types.max_results
    import capo_route53_recovery_readiness.types.readiness_check_output
    import capo_route53_recovery_readiness.types.readiness_check_summary
    import capo_route53_recovery_readiness.types.recovery_group_output
    import capo_route53_recovery_readiness.types.resource_result
    import capo_route53_recovery_readiness.types.resource_set_output
    import capo_route53_recovery_readiness.types.rule_result
    import capo_route53_recovery_readiness.types.tag_resource_request
    import capo_route53_recovery_readiness.types.tag_resource_response
    import capo_route53_recovery_readiness.types.tags
    import capo_route53_recovery_readiness.types.untag_resource_request
    import capo_route53_recovery_readiness.types.update_cell_request
    import capo_route53_recovery_readiness.types.update_cell_response
    import capo_route53_recovery_readiness.types.update_readiness_check_request
    import capo_route53_recovery_readiness.types.update_readiness_check_response
    import capo_route53_recovery_readiness.types.update_recovery_group_request
    import capo_route53_recovery_readiness.types.update_recovery_group_response
    import capo_route53_recovery_readiness.types.update_resource_set_request
    import capo_route53_recovery_readiness.types.update_resource_set_response


class Route53RecoveryReadinessClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class Route53RecoveryReadinessClient:
    """A client for the ``Route53RecoveryReadiness`` service.

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
        self._config = Route53RecoveryReadinessClientConfig(
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
        self, config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: Route53RecoveryReadinessClientConfig = config_overrides or {}
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

    def create_cell(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        cell_name: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
        cells: Optional[
            "capo_route53_recovery_readiness.types.__list_of__string.__listOf__string"
        ] = None,
        tags: Optional["capo_route53_recovery_readiness.types.tags.Tags"] = None,
    ) -> (
        "capo_route53_recovery_readiness.types.create_cell_response.CreateCellResponse"
    ):
        """<p>Creates a cell in an account.</p>

        Args:
            cell_name: <p>The name of the cell to create.</p>
            cells: <p>A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific Amazon Web Services Regions.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.conflict_exception.ConflictException: Updating or deleting a resource can cause an inconsistent state.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.create_cell_request.CreateCellRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.create_cell_response.CreateCellResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.create_cell

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.create_cell.create_cell(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.create_cell_request.CreateCellRequest = {}
        if cell_name is not None:
            input_["cell_name"] = cell_name
        if cells is not None:
            input_["cells"] = cells
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cross_account_authorization(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        cross_account_authorization: Optional[
            "capo_route53_recovery_readiness.types.cross_account_authorization.CrossAccountAuthorization"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.create_cross_account_authorization_response.CreateCrossAccountAuthorizationResponse":
        """<p>Creates a cross-account readiness authorization. This lets you authorize another account to work with Route 53 Application Recovery Controller, for example, to check the readiness status of resources in a separate account.</p>

        Args:
            cross_account_authorization: <p>The cross-account authorization.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.conflict_exception.ConflictException: Updating or deleting a resource can cause an inconsistent state.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.create_cross_account_authorization_request.CreateCrossAccountAuthorizationRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.create_cross_account_authorization_response.CreateCrossAccountAuthorizationResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.create_cross_account_authorization

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.create_cross_account_authorization.create_cross_account_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.create_cross_account_authorization_request.CreateCrossAccountAuthorizationRequest = {}
        if cross_account_authorization is not None:
            input_["cross_account_authorization"] = cross_account_authorization

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_readiness_check(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        readiness_check_name: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
        resource_set_name: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
        tags: Optional["capo_route53_recovery_readiness.types.tags.Tags"] = None,
    ) -> "capo_route53_recovery_readiness.types.create_readiness_check_response.CreateReadinessCheckResponse":
        """<p>Creates a readiness check in an account. A readiness check monitors a resource set in your application, such as a set of Amazon Aurora instances, that Application Recovery Controller is auditing recovery readiness for. The audits run once every minute on every resource that's associated with a readiness check.</p>

        Args:
            readiness_check_name: <p>The name of the readiness check to create.</p>
            resource_set_name: <p>The name of the resource set to check.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.conflict_exception.ConflictException: Updating or deleting a resource can cause an inconsistent state.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.create_readiness_check_request.CreateReadinessCheckRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.create_readiness_check_response.CreateReadinessCheckResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.create_readiness_check

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.create_readiness_check.create_readiness_check(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.create_readiness_check_request.CreateReadinessCheckRequest = {}
        if readiness_check_name is not None:
            input_["readiness_check_name"] = readiness_check_name
        if resource_set_name is not None:
            input_["resource_set_name"] = resource_set_name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_recovery_group(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        cells: Optional[
            "capo_route53_recovery_readiness.types.__list_of__string.__listOf__string"
        ] = None,
        recovery_group_name: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
        tags: Optional["capo_route53_recovery_readiness.types.tags.Tags"] = None,
    ) -> "capo_route53_recovery_readiness.types.create_recovery_group_response.CreateRecoveryGroupResponse":
        """<p>Creates a recovery group in an account. A recovery group corresponds to an application and includes a list of the cells that make up the application.</p>

        Args:
            cells: <p>A list of the cell Amazon Resource Names (ARNs) in the recovery group.</p>
            recovery_group_name: <p>The name of the recovery group to create.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.conflict_exception.ConflictException: Updating or deleting a resource can cause an inconsistent state.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.create_recovery_group_request.CreateRecoveryGroupRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.create_recovery_group_response.CreateRecoveryGroupResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.create_recovery_group

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.create_recovery_group.create_recovery_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.create_recovery_group_request.CreateRecoveryGroupRequest = {}
        if cells is not None:
            input_["cells"] = cells
        if recovery_group_name is not None:
            input_["recovery_group_name"] = recovery_group_name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_resource_set(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        resource_set_name: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
        resource_set_type: Optional[
            "capo_route53_recovery_readiness.types.__string_pattern_awsa_za_z09_a_za_z09.__stringPatternAWSAZaZ09AZaZ09"
        ] = None,
        resources: Optional[
            "capo_route53_recovery_readiness.types.__list_of_resource.__listOfResource"
        ] = None,
        tags: Optional["capo_route53_recovery_readiness.types.tags.Tags"] = None,
    ) -> "capo_route53_recovery_readiness.types.create_resource_set_response.CreateResourceSetResponse":
        """<p>Creates a resource set. A resource set is a set of resources of one type that span multiple cells. You can associate a resource set with a readiness check to monitor the resources for failover readiness.</p>

        Args:
            resource_set_name: <p>The name of the resource set to create.</p>
            resource_set_type: <p>The resource type of the resources in the resource set. Enter one of the following values for resource type:</p> <p>AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource</p>
            resources: <p>A list of resource objects in the resource set.</p>
            tags: <p>A tag to associate with the parameters for a resource set.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.conflict_exception.ConflictException: Updating or deleting a resource can cause an inconsistent state.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.create_resource_set_request.CreateResourceSetRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.create_resource_set_response.CreateResourceSetResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.create_resource_set

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.create_resource_set.create_resource_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.create_resource_set_request.CreateResourceSetRequest = {}
        if resource_set_name is not None:
            input_["resource_set_name"] = resource_set_name
        if resource_set_type is not None:
            input_["resource_set_type"] = resource_set_type
        if resources is not None:
            input_["resources"] = resources
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cell(
        self,
        cell_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
    ) -> None:
        """<p>Delete a cell. When successful, the response code is 204, with no response body.</p>

        Args:
            cell_name: <p>The name of the cell.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.delete_cell_request.DeleteCellRequest]",
        ) -> OperationResponse[None]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.delete_cell

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.delete_cell.delete_cell(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.delete_cell_request.DeleteCellRequest = {
            "cell_name": cell_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cross_account_authorization(
        self,
        cross_account_authorization: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
    ) -> "capo_route53_recovery_readiness.types.delete_cross_account_authorization_response.DeleteCrossAccountAuthorizationResponse":
        """<p>Deletes cross account readiness authorization.</p>

        Args:
            cross_account_authorization: <p>The cross-account authorization.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.delete_cross_account_authorization_request.DeleteCrossAccountAuthorizationRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.delete_cross_account_authorization_response.DeleteCrossAccountAuthorizationResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.delete_cross_account_authorization

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.delete_cross_account_authorization.delete_cross_account_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.delete_cross_account_authorization_request.DeleteCrossAccountAuthorizationRequest = {
            "cross_account_authorization": cross_account_authorization
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_readiness_check(
        self,
        readiness_check_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
    ) -> None:
        """<p>Deletes a readiness check.</p>

        Args:
            readiness_check_name: <p>Name of a readiness check.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.delete_readiness_check_request.DeleteReadinessCheckRequest]",
        ) -> OperationResponse[None]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.delete_readiness_check

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.delete_readiness_check.delete_readiness_check(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.delete_readiness_check_request.DeleteReadinessCheckRequest = {
            "readiness_check_name": readiness_check_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_recovery_group(
        self,
        recovery_group_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
    ) -> None:
        """<p>Deletes a recovery group.</p>

        Args:
            recovery_group_name: <p>The name of a recovery group.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.delete_recovery_group_request.DeleteRecoveryGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.delete_recovery_group

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.delete_recovery_group.delete_recovery_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.delete_recovery_group_request.DeleteRecoveryGroupRequest = {
            "recovery_group_name": recovery_group_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_set(
        self,
        resource_set_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
    ) -> None:
        """<p>Deletes a resource set.</p>

        Args:
            resource_set_name: <p>Name of a resource set.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.delete_resource_set_request.DeleteResourceSetRequest]",
        ) -> OperationResponse[None]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.delete_resource_set

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.delete_resource_set.delete_resource_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.delete_resource_set_request.DeleteResourceSetRequest = {
            "resource_set_name": resource_set_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_architecture_recommendations(
        self,
        recovery_group_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.get_architecture_recommendations_response.GetArchitectureRecommendationsResponse":
        """<p>Gets recommendations about architecture designs for improving resiliency for an application, based on a recovery group.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            recovery_group_name: <p>The name of a recovery group.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.get_architecture_recommendations_request.GetArchitectureRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.get_architecture_recommendations_response.GetArchitectureRecommendationsResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_architecture_recommendations

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_architecture_recommendations.get_architecture_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.get_architecture_recommendations_request.GetArchitectureRecommendationsRequest = {
            "recovery_group_name": recovery_group_name
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

    def get_cell(
        self,
        cell_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
    ) -> "capo_route53_recovery_readiness.types.get_cell_response.GetCellResponse":
        """<p>Gets information about a cell including cell name, cell Amazon Resource Name (ARN), ARNs of nested cells for this cell, and a list of those cell ARNs with their associated recovery group ARNs.</p>

        Args:
            cell_name: <p>The name of the cell.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.get_cell_request.GetCellRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.get_cell_response.GetCellResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_cell

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_cell.get_cell(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.get_cell_request.GetCellRequest = {
            "cell_name": cell_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cell_readiness_summary(
        self,
        cell_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.get_cell_readiness_summary_response.GetCellReadinessSummaryResponse":
        """<p>Gets readiness for a cell. Aggregates the readiness of all the resources that are associated with the cell into a single value.</p>

        Args:
            cell_name: <p>The name of the cell.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.get_cell_readiness_summary_request.GetCellReadinessSummaryRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.get_cell_readiness_summary_response.GetCellReadinessSummaryResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_cell_readiness_summary

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_cell_readiness_summary.get_cell_readiness_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.get_cell_readiness_summary_request.GetCellReadinessSummaryRequest = {
            "cell_name": cell_name
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

    def iter_get_cell_readiness_summary(
        self,
        cell_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_route53_recovery_readiness.types.readiness_check_summary.ReadinessCheckSummary]":
        _token = next_token
        while True:
            _response = self.get_cell_readiness_summary(
                cell_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("readiness_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_readiness_check(
        self,
        readiness_check_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
    ) -> "capo_route53_recovery_readiness.types.get_readiness_check_response.GetReadinessCheckResponse":
        """<p>Gets details about a readiness check.</p>

        Args:
            readiness_check_name: <p>Name of a readiness check.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.get_readiness_check_request.GetReadinessCheckRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.get_readiness_check_response.GetReadinessCheckResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check.get_readiness_check(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.get_readiness_check_request.GetReadinessCheckRequest = {
            "readiness_check_name": readiness_check_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_readiness_check_resource_status(
        self,
        readiness_check_name: "capo_route53_recovery_readiness.types.__string.__string",
        resource_identifier: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.get_readiness_check_resource_status_response.GetReadinessCheckResourceStatusResponse":
        """<p>Gets individual readiness status for a readiness check. To see the overall readiness status for a recovery group, that considers the readiness status for all the readiness checks in the recovery group, use GetRecoveryGroupReadinessSummary.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            readiness_check_name: <p>Name of a readiness check.</p>
            resource_identifier: <p>The resource identifier, which is the Amazon Resource Name (ARN) or the identifier generated for the resource by Application Recovery Controller (for example, for a DNS target resource).</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.get_readiness_check_resource_status_request.GetReadinessCheckResourceStatusRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.get_readiness_check_resource_status_response.GetReadinessCheckResourceStatusResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check_resource_status

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check_resource_status.get_readiness_check_resource_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.get_readiness_check_resource_status_request.GetReadinessCheckResourceStatusRequest = {
            "readiness_check_name": readiness_check_name,
            "resource_identifier": resource_identifier,
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

    def iter_get_readiness_check_resource_status(
        self,
        readiness_check_name: "capo_route53_recovery_readiness.types.__string.__string",
        resource_identifier: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_route53_recovery_readiness.types.rule_result.RuleResult]":
        _token = next_token
        while True:
            _response = self.get_readiness_check_resource_status(
                readiness_check_name,
                resource_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_readiness_check_status(
        self,
        readiness_check_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.get_readiness_check_status_response.GetReadinessCheckStatusResponse":
        """<p>Gets the readiness status for an individual readiness check. To see the overall readiness status for a recovery group, that considers the readiness status for all the readiness checks in a recovery group, use GetRecoveryGroupReadinessSummary.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            readiness_check_name: <p>Name of a readiness check.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.get_readiness_check_status_request.GetReadinessCheckStatusRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.get_readiness_check_status_response.GetReadinessCheckStatusResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check_status

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_readiness_check_status.get_readiness_check_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.get_readiness_check_status_request.GetReadinessCheckStatusRequest = {
            "readiness_check_name": readiness_check_name
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

    def iter_get_readiness_check_status(
        self,
        readiness_check_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> (
        "Iterator[capo_route53_recovery_readiness.types.resource_result.ResourceResult]"
    ):
        _token = next_token
        while True:
            _response = self.get_readiness_check_status(
                readiness_check_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_recovery_group(
        self,
        recovery_group_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
    ) -> "capo_route53_recovery_readiness.types.get_recovery_group_response.GetRecoveryGroupResponse":
        """<p>Gets details about a recovery group, including a list of the cells that are included in it.</p>

        Args:
            recovery_group_name: <p>The name of a recovery group.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.get_recovery_group_request.GetRecoveryGroupRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.get_recovery_group_response.GetRecoveryGroupResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_recovery_group

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_recovery_group.get_recovery_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.get_recovery_group_request.GetRecoveryGroupRequest = {
            "recovery_group_name": recovery_group_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recovery_group_readiness_summary(
        self,
        recovery_group_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.get_recovery_group_readiness_summary_response.GetRecoveryGroupReadinessSummaryResponse":
        """<p>Displays a summary of information about a recovery group's readiness status. Includes the readiness checks for resources in the recovery group and the readiness status of each one.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            recovery_group_name: <p>The name of a recovery group.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.get_recovery_group_readiness_summary_request.GetRecoveryGroupReadinessSummaryRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.get_recovery_group_readiness_summary_response.GetRecoveryGroupReadinessSummaryResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_recovery_group_readiness_summary

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_recovery_group_readiness_summary.get_recovery_group_readiness_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.get_recovery_group_readiness_summary_request.GetRecoveryGroupReadinessSummaryRequest = {
            "recovery_group_name": recovery_group_name
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

    def iter_get_recovery_group_readiness_summary(
        self,
        recovery_group_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_route53_recovery_readiness.types.readiness_check_summary.ReadinessCheckSummary]":
        _token = next_token
        while True:
            _response = self.get_recovery_group_readiness_summary(
                recovery_group_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("readiness_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_resource_set(
        self,
        resource_set_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
    ) -> "capo_route53_recovery_readiness.types.get_resource_set_response.GetResourceSetResponse":
        """<p>Displays the details about a resource set, including a list of the resources in the set.</p>

        Args:
            resource_set_name: <p>Name of a resource set.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.get_resource_set_request.GetResourceSetRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.get_resource_set_response.GetResourceSetResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_resource_set

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.get_resource_set.get_resource_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.get_resource_set_request.GetResourceSetRequest = {
            "resource_set_name": resource_set_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_cells(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.list_cells_response.ListCellsResponse":
        """<p>Lists the cells for an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.list_cells_request.ListCellsRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.list_cells_response.ListCellsResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_cells

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_cells.list_cells(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.list_cells_request.ListCellsRequest = {}
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

    def iter_list_cells(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_route53_recovery_readiness.types.cell_output.CellOutput]":
        _token = next_token
        while True:
            _response = self.list_cells(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cells",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cross_account_authorizations(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.list_cross_account_authorizations_response.ListCrossAccountAuthorizationsResponse":
        """<p>Lists the cross-account readiness authorizations that are in place for an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.list_cross_account_authorizations_request.ListCrossAccountAuthorizationsRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.list_cross_account_authorizations_response.ListCrossAccountAuthorizationsResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_cross_account_authorizations

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_cross_account_authorizations.list_cross_account_authorizations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.list_cross_account_authorizations_request.ListCrossAccountAuthorizationsRequest = {}
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

    def iter_list_cross_account_authorizations(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_route53_recovery_readiness.types.cross_account_authorization.CrossAccountAuthorization]":
        _token = next_token
        while True:
            _response = self.list_cross_account_authorizations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cross_account_authorizations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_readiness_checks(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.list_readiness_checks_response.ListReadinessChecksResponse":
        """<p>Lists the readiness checks for an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.list_readiness_checks_request.ListReadinessChecksRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.list_readiness_checks_response.ListReadinessChecksResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_readiness_checks

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_readiness_checks.list_readiness_checks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.list_readiness_checks_request.ListReadinessChecksRequest = {}
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

    def iter_list_readiness_checks(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_route53_recovery_readiness.types.readiness_check_output.ReadinessCheckOutput]":
        _token = next_token
        while True:
            _response = self.list_readiness_checks(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("readiness_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recovery_groups(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.list_recovery_groups_response.ListRecoveryGroupsResponse":
        """<p>Lists the recovery groups in an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.list_recovery_groups_request.ListRecoveryGroupsRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.list_recovery_groups_response.ListRecoveryGroupsResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_recovery_groups

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_recovery_groups.list_recovery_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.list_recovery_groups_request.ListRecoveryGroupsRequest = {}
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

    def iter_list_recovery_groups(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_route53_recovery_readiness.types.recovery_group_output.RecoveryGroupOutput]":
        _token = next_token
        while True:
            _response = self.list_recovery_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("recovery_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_sets(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.list_resource_sets_response.ListResourceSetsResponse":
        """<p>Lists the resource sets in an account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.list_resource_sets_request.ListResourceSetsRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.list_resource_sets_response.ListResourceSetsResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_resource_sets

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_resource_sets.list_resource_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.list_resource_sets_request.ListResourceSetsRequest = {}
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

    def iter_list_resource_sets(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_route53_recovery_readiness.types.resource_set_output.ResourceSetOutput]":
        _token = next_token
        while True:
            _response = self.list_resource_sets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_rules(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
        resource_type: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.list_rules_response.ListRulesResponse":
        """<p>Lists all readiness rules, or lists the readiness rules for a specific resource type.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>The token that identifies which batch of results you want to see.</p>
            resource_type: <p>The resource type that a readiness rule applies to.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.list_rules_request.ListRulesRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.list_rules_response.ListRulesResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_rules

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_rules.list_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.list_rules_request.ListRulesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_type is not None:
            input_["resource_type"] = resource_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_rules(
        self,
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        max_results: Optional[
            "capo_route53_recovery_readiness.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
        resource_type: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_route53_recovery_readiness.types.list_rules_output.ListRulesOutput]":
        _token = next_token
        while True:
            _response = self.list_rules(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                resource_type=resource_type,
            )
            _page = _resolve_path(_response, ("rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resources(
        self,
        resource_arn: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
    ) -> "capo_route53_recovery_readiness.types.list_tags_for_resources_response.ListTagsForResourcesResponse":
        """<p>Lists the tags for a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a resource.</p>

        Raises:
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.list_tags_for_resources_request.ListTagsForResourcesRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.list_tags_for_resources_response.ListTagsForResourcesResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_tags_for_resources

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.list_tags_for_resources.list_tags_for_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.list_tags_for_resources_request.ListTagsForResourcesRequest = {
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
        resource_arn: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        tags: Optional["capo_route53_recovery_readiness.types.tags.Tags"] = None,
    ) -> "capo_route53_recovery_readiness.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a resource.</p>
            tags: <p></p>

        Raises:
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.tag_resource

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
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

    def untag_resource(
        self,
        resource_arn: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        tag_keys: Optional[
            "capo_route53_recovery_readiness.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> None:
        """<p>Removes a tag from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for a resource.</p>
            tag_keys: <p>The keys for tags you add to resources.</p>

        Raises:
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.untag_resource

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cell(
        self,
        cell_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        cells: Optional[
            "capo_route53_recovery_readiness.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> (
        "capo_route53_recovery_readiness.types.update_cell_response.UpdateCellResponse"
    ):
        """<p>Updates a cell to replace the list of nested cells with a new list of nested cells.</p>

        Args:
            cell_name: <p>The name of the cell.</p>
            cells: <p>A list of cell Amazon Resource Names (ARNs), which completely replaces the previous list.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.update_cell_request.UpdateCellRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.update_cell_response.UpdateCellResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.update_cell

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.update_cell.update_cell(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.update_cell_request.UpdateCellRequest = {
            "cell_name": cell_name
        }
        if cells is not None:
            input_["cells"] = cells

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_readiness_check(
        self,
        readiness_check_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        resource_set_name: Optional[
            "capo_route53_recovery_readiness.types.__string.__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.update_readiness_check_response.UpdateReadinessCheckResponse":
        """<p>Updates a readiness check.</p>

        Args:
            readiness_check_name: <p>Name of a readiness check.</p>
            resource_set_name: <p>The name of the resource set to be checked.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.update_readiness_check_request.UpdateReadinessCheckRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.update_readiness_check_response.UpdateReadinessCheckResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.update_readiness_check

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.update_readiness_check.update_readiness_check(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.update_readiness_check_request.UpdateReadinessCheckRequest = {
            "readiness_check_name": readiness_check_name
        }
        if resource_set_name is not None:
            input_["resource_set_name"] = resource_set_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_recovery_group(
        self,
        recovery_group_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        cells: Optional[
            "capo_route53_recovery_readiness.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.update_recovery_group_response.UpdateRecoveryGroupResponse":
        """<p>Updates a recovery group.</p>

        Args:
            cells: <p>A list of cell Amazon Resource Names (ARNs). This list completely replaces the previous list.</p>
            recovery_group_name: <p>The name of a recovery group.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.update_recovery_group_request.UpdateRecoveryGroupRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.update_recovery_group_response.UpdateRecoveryGroupResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.update_recovery_group

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.update_recovery_group.update_recovery_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.update_recovery_group_request.UpdateRecoveryGroupRequest = {
            "recovery_group_name": recovery_group_name
        }
        if cells is not None:
            input_["cells"] = cells

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_resource_set(
        self,
        resource_set_name: "capo_route53_recovery_readiness.types.__string.__string",
        *,
        config_overrides: Optional[Route53RecoveryReadinessClientConfig] = None,
        resource_set_type: Optional[
            "capo_route53_recovery_readiness.types.__string_pattern_awsa_za_z09_a_za_z09.__stringPatternAWSAZaZ09AZaZ09"
        ] = None,
        resources: Optional[
            "capo_route53_recovery_readiness.types.__list_of_resource.__listOfResource"
        ] = None,
    ) -> "capo_route53_recovery_readiness.types.update_resource_set_response.UpdateResourceSetResponse":
        """<p>Updates a resource set.</p>

        Args:
            resource_set_name: <p>Name of a resource set.</p>
            resource_set_type: <p>The resource type of the resources in the resource set. Enter one of the following values for resource type:</p> <p>AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource</p>
            resources: <p>A list of resource objects.</p>

        Raises:
            capo_route53_recovery_readiness.errors.access_denied_exception.AccessDeniedException: User does not have sufficient access to perform this action.
            capo_route53_recovery_readiness.errors.internal_server_exception.InternalServerException: An unexpected error occurred.
            capo_route53_recovery_readiness.errors.resource_not_found_exception.ResourceNotFoundException: The requested resource does not exist.
            capo_route53_recovery_readiness.errors.throttling_exception.ThrottlingException: Request was denied due to request throttling.
            capo_route53_recovery_readiness.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by an AWS service.
            capo_route53_recovery_readiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_route53_recovery_readiness.types.update_resource_set_request.UpdateResourceSetRequest]",
        ) -> OperationResponse[
            "capo_route53_recovery_readiness.types.update_resource_set_response.UpdateResourceSetResponse"
        ]:
            import capo_route53_recovery_readiness._operations.route53_recovery_readiness.update_resource_set

            output, http_response = (
                capo_route53_recovery_readiness._operations.route53_recovery_readiness.update_resource_set.update_resource_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_route53_recovery_readiness.types.update_resource_set_request.UpdateResourceSetRequest = {
            "resource_set_name": resource_set_name
        }
        if resource_set_type is not None:
            input_["resource_set_type"] = resource_set_type
        if resources is not None:
            input_["resources"] = resources

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
