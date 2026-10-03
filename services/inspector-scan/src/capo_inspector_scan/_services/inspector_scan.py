"""Generated from Smithy shape ``com.amazonaws.inspectorscan#InspectorScan``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_inspector_scan._auth._signers
import capo_inspector_scan._auth._sigv4
from capo_inspector_scan._auth._identity import Credentials
from capo_inspector_scan._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_inspector_scan._auth._zapros_handler import AuthMiddleware
from capo_inspector_scan._services._aws_config import aws_config
from capo_inspector_scan._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_inspector_scan.types.output_format
    import capo_inspector_scan.types.sbom
    import capo_inspector_scan.types.scan_sbom_request
    import capo_inspector_scan.types.scan_sbom_response


class InspectorScanClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class InspectorScanClient:
    """A client for the ``InspectorScan`` service.

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
        self._config = InspectorScanClientConfig(
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
        self, config_overrides: Optional[InspectorScanClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: InspectorScanClientConfig = config_overrides or {}
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

    def scan_sbom(
        self,
        sbom: "capo_inspector_scan.types.sbom.Sbom",
        *,
        config_overrides: Optional[InspectorScanClientConfig] = None,
        output_format: Optional[
            "capo_inspector_scan.types.output_format.OutputFormat"
        ] = None,
    ) -> "capo_inspector_scan.types.scan_sbom_response.ScanSbomResponse":
        """<p>Scans a provided CycloneDX 1.5 SBOM and reports on any vulnerabilities discovered in that SBOM. You can generate compatible SBOMs for your resources using the <a href="https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html">Amazon Inspector SBOM generator</a>.</p> <note> <p> The output of this action reports NVD and CVSS scores when NVD and CVSS scores are available. Because the output reports both scores, you might notice a discrepency between them. However, you can triage the severity of either score depending on the vendor of your choosing. </p> </note>

        Args:
            sbom: <p>The JSON file for the SBOM you want to scan. The SBOM must be in CycloneDX 1.5 format. This format limits you to passing 2000 components before throwing a <code>ValidException</code> error.</p>
            output_format: <p>The output format for the vulnerability report.</p>

        Raises:
            capo_inspector_scan.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_inspector_scan.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure. </p>
            capo_inspector_scan.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_inspector_scan.errors.validation_exception.ValidationException: <p>The request has failed validation due to missing required fields or having invalid inputs.</p>
            capo_inspector_scan.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ScanSbom Call

            >>> client.scan_sbom(output_format='CYCLONE_DX_1_5', sbom={'bomFormat': 'CycloneDX', 'specVersion': '1.5', 'components': [{'type': 'library', 'name': 'log4j-core', 'purl': 'pkg:maven/org.apache.logging.log4j/log4j-core@2.17.0'}]})
        """

        def _handler(
            req: "OperationRequest[capo_inspector_scan.types.scan_sbom_request.ScanSbomRequest]",
        ) -> OperationResponse[
            "capo_inspector_scan.types.scan_sbom_response.ScanSbomResponse"
        ]:
            import capo_inspector_scan._operations.inspector_scan.scan_sbom

            output, http_response = (
                capo_inspector_scan._operations.inspector_scan.scan_sbom.scan_sbom(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_inspector_scan.types.scan_sbom_request.ScanSbomRequest = {
            "sbom": sbom
        }
        if output_format is not None:
            input_["output_format"] = output_format

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
