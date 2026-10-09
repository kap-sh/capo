"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#AmazonSageMakerEdge``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_sagemaker_edge._auth._signers
import capo_sagemaker_edge._auth._sigv4
from capo_sagemaker_edge._auth._identity import Credentials
from capo_sagemaker_edge._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sagemaker_edge._auth._zapros_handler import AuthMiddleware
from capo_sagemaker_edge._services._aws_config import aws_config
from capo_sagemaker_edge._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.deployment_result
    import capo_sagemaker_edge.types.device_fleet_name
    import capo_sagemaker_edge.types.device_name
    import capo_sagemaker_edge.types.edge_metrics
    import capo_sagemaker_edge.types.get_deployments_request
    import capo_sagemaker_edge.types.get_deployments_result
    import capo_sagemaker_edge.types.get_device_registration_request
    import capo_sagemaker_edge.types.get_device_registration_result
    import capo_sagemaker_edge.types.models
    import capo_sagemaker_edge.types.send_heartbeat_request
    import capo_sagemaker_edge.types.version


class SagemakerEdgeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class SagemakerEdgeClient:
    """A client for the ``SagemakerEdge`` service.

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
        self._config = SagemakerEdgeClientConfig(
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
        self, config_overrides: Optional[SagemakerEdgeClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SagemakerEdgeClientConfig = config_overrides or {}
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

    def get_deployments(
        self,
        *,
        config_overrides: Optional[SagemakerEdgeClientConfig] = None,
        device_name: Optional[
            "capo_sagemaker_edge.types.device_name.DeviceName"
        ] = None,
        device_fleet_name: Optional[
            "capo_sagemaker_edge.types.device_fleet_name.DeviceFleetName"
        ] = None,
    ) -> "capo_sagemaker_edge.types.get_deployments_result.GetDeploymentsResult":
        """<p>Use to get the active deployments from a device.</p>

        Args:
            device_name: <p>The unique name of the device you want to get the configuration of active deployments from.</p>
            device_fleet_name: <p>The name of the fleet that the device belongs to.</p>

        Raises:
            capo_sagemaker_edge.errors.internal_service_exception.InternalServiceException: <p>An internal failure occurred. Try your request again. If the problem persists, contact Amazon Web Services customer support.</p>
            capo_sagemaker_edge.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_edge.types.get_deployments_request.GetDeploymentsRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_edge.types.get_deployments_result.GetDeploymentsResult"
        ]:
            import capo_sagemaker_edge._operations.amazon_sage_maker_edge.get_deployments

            output, http_response = (
                capo_sagemaker_edge._operations.amazon_sage_maker_edge.get_deployments.get_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_edge.types.get_deployments_request.GetDeploymentsRequest = {}
        if device_name is not None:
            input_["device_name"] = device_name
        if device_fleet_name is not None:
            input_["device_fleet_name"] = device_fleet_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_device_registration(
        self,
        *,
        config_overrides: Optional[SagemakerEdgeClientConfig] = None,
        device_name: Optional[
            "capo_sagemaker_edge.types.device_name.DeviceName"
        ] = None,
        device_fleet_name: Optional[
            "capo_sagemaker_edge.types.device_fleet_name.DeviceFleetName"
        ] = None,
    ) -> "capo_sagemaker_edge.types.get_device_registration_result.GetDeviceRegistrationResult":
        """<p>Use to check if a device is registered with SageMaker Edge Manager.</p>

        Args:
            device_name: <p>The unique name of the device you want to get the registration status from.</p>
            device_fleet_name: <p>The name of the fleet that the device belongs to.</p>

        Raises:
            capo_sagemaker_edge.errors.internal_service_exception.InternalServiceException: <p>An internal failure occurred. Try your request again. If the problem persists, contact Amazon Web Services customer support.</p>
            capo_sagemaker_edge.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_edge.types.get_device_registration_request.GetDeviceRegistrationRequest]",
        ) -> OperationResponse[
            "capo_sagemaker_edge.types.get_device_registration_result.GetDeviceRegistrationResult"
        ]:
            import capo_sagemaker_edge._operations.amazon_sage_maker_edge.get_device_registration

            output, http_response = (
                capo_sagemaker_edge._operations.amazon_sage_maker_edge.get_device_registration.get_device_registration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_edge.types.get_device_registration_request.GetDeviceRegistrationRequest = {}
        if device_name is not None:
            input_["device_name"] = device_name
        if device_fleet_name is not None:
            input_["device_fleet_name"] = device_fleet_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def send_heartbeat(
        self,
        *,
        config_overrides: Optional[SagemakerEdgeClientConfig] = None,
        agent_metrics: Optional[
            "capo_sagemaker_edge.types.edge_metrics.EdgeMetrics"
        ] = None,
        models: Optional["capo_sagemaker_edge.types.models.Models"] = None,
        agent_version: Optional["capo_sagemaker_edge.types.version.Version"] = None,
        device_name: Optional[
            "capo_sagemaker_edge.types.device_name.DeviceName"
        ] = None,
        device_fleet_name: Optional[
            "capo_sagemaker_edge.types.device_fleet_name.DeviceFleetName"
        ] = None,
        deployment_result: Optional[
            "capo_sagemaker_edge.types.deployment_result.DeploymentResult"
        ] = None,
    ) -> None:
        """<p>Use to get the current status of devices registered on SageMaker Edge Manager.</p>

        Args:
            agent_metrics: <p>For internal use. Returns a list of SageMaker Edge Manager agent operating metrics.</p>
            models: <p>Returns a list of models deployed on the the device.</p>
            agent_version: <p>Returns the version of the agent.</p>
            device_name: <p>The unique name of the device.</p>
            device_fleet_name: <p>The name of the fleet that the device belongs to.</p>
            deployment_result: <p>Returns the result of a deployment on the device.</p>

        Raises:
            capo_sagemaker_edge.errors.internal_service_exception.InternalServiceException: <p>An internal failure occurred. Try your request again. If the problem persists, contact Amazon Web Services customer support.</p>
            capo_sagemaker_edge.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_edge.types.send_heartbeat_request.SendHeartbeatRequest]",
        ) -> OperationResponse[None]:
            import capo_sagemaker_edge._operations.amazon_sage_maker_edge.send_heartbeat

            output, http_response = (
                capo_sagemaker_edge._operations.amazon_sage_maker_edge.send_heartbeat.send_heartbeat(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_edge.types.send_heartbeat_request.SendHeartbeatRequest = {}
        if agent_metrics is not None:
            input_["agent_metrics"] = agent_metrics
        if models is not None:
            input_["models"] = models
        if agent_version is not None:
            input_["agent_version"] = agent_version
        if device_name is not None:
            input_["device_name"] = device_name
        if device_fleet_name is not None:
            input_["device_fleet_name"] = device_fleet_name
        if deployment_result is not None:
            input_["deployment_result"] = deployment_result

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
