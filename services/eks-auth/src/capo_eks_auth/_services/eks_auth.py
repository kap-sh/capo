"""Generated from Smithy shape ``com.amazonaws.eksauth#EKSAuthFrontend``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_eks_auth._auth._signers
import capo_eks_auth._auth._sigv4
from capo_eks_auth._auth._identity import Credentials
from capo_eks_auth._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_eks_auth._auth._zapros_handler import AuthMiddleware
from capo_eks_auth._services._aws_config import aws_config
from capo_eks_auth._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_eks_auth.types.assume_role_for_pod_identity_request
    import capo_eks_auth.types.assume_role_for_pod_identity_response
    import capo_eks_auth.types.cluster_name
    import capo_eks_auth.types.jwt_token


class EKSAuthClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class EKSAuthClient:
    """A client for the ``EKSAuth`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
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
        self._config = EKSAuthClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[EKSAuthClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: EKSAuthClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def assume_role_for_pod_identity(
        self,
        cluster_name: "capo_eks_auth.types.cluster_name.ClusterName",
        token: "capo_eks_auth.types.jwt_token.JwtToken",
        *,
        config_overrides: Optional[EKSAuthClientConfig] = None,
        eks_node_name: Optional[str] = None,
        instance_id: Optional[str] = None,
        zone: Optional[str] = None,
    ) -> "capo_eks_auth.types.assume_role_for_pod_identity_response.AssumeRoleForPodIdentityResponse":
        """<p>The Amazon EKS Auth API and the <code>AssumeRoleForPodIdentity</code> action are only used by the EKS Pod Identity Agent.</p> <p>We recommend that applications use the Amazon Web Services SDKs to connect to Amazon Web Services services; if credentials from an EKS Pod Identity association are available in the pod, the latest versions of the SDKs use them automatically.</p>

        Args:
            cluster_name: <p>The name of the cluster for the request.</p>
            token: <p>The token of the Kubernetes service account for the pod.</p>
            eks_node_name: <p>The Kubernetes node name of the worker node where the pod is running.</p>
            instance_id: <p>The Amazon EC2 instance ID of the worker node where the pod is running.</p>
            zone: <p>The Availability Zone ID of the worker node where the pod is running.</p>

        Raises:
            capo_eks_auth.errors.access_denied_exception.AccessDeniedException: <p>You don't have permissions to perform the requested operation. The IAM principal making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html">Access management</a> in the <i>IAM User Guide</i>. </p>
            capo_eks_auth.errors.expired_token_exception.ExpiredTokenException: <p>The specified Kubernetes service account token is expired.</p>
            capo_eks_auth.errors.internal_server_exception.InternalServerException: <p>These errors are usually caused by a server-side issue.</p>
            capo_eks_auth.errors.invalid_parameter_exception.InvalidParameterException: <p>The specified parameter is invalid. Review the available parameters for the API request.</p>
            capo_eks_auth.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning will depend on the API, and will be documented in the error message.</p>
            capo_eks_auth.errors.invalid_token_exception.InvalidTokenException: <p>The specified Kubernetes service account token is invalid.</p>
            capo_eks_auth.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource could not be found.</p>
            capo_eks_auth.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is unavailable. Back off and retry the operation.</p>
            capo_eks_auth.errors.throttling_exception.ThrottlingException: <p>The request was denied because your request rate is too high. Reduce the frequency of requests.</p>
            capo_eks_auth.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_eks_auth.types.assume_role_for_pod_identity_request.AssumeRoleForPodIdentityRequest]",
        ) -> OperationResponse[
            "capo_eks_auth.types.assume_role_for_pod_identity_response.AssumeRoleForPodIdentityResponse"
        ]:
            import capo_eks_auth._operations.eks_auth_frontend.assume_role_for_pod_identity

            output, http_response = (
                capo_eks_auth._operations.eks_auth_frontend.assume_role_for_pod_identity.assume_role_for_pod_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eks_auth.types.assume_role_for_pod_identity_request.AssumeRoleForPodIdentityRequest = {
            "cluster_name": cluster_name,
            "token": token,
        }
        if eks_node_name is not None:
            input_["eks_node_name"] = eks_node_name
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if zone is not None:
            input_["zone"] = zone

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
