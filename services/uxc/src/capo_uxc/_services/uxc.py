"""Generated from Smithy shape ``com.amazonaws.uxc#AWSAccountUXSetting``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_uxc._auth._signers
import capo_uxc._auth._sigv4
from capo_uxc._auth._identity import Credentials
from capo_uxc._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_uxc._auth._zapros_handler import AuthMiddleware
from capo_uxc._pagination import resolve_path as _resolve_path
from capo_uxc._services._aws_config import aws_config
from capo_uxc._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_uxc.types.account_color
    import capo_uxc.types.get_account_customizations_input
    import capo_uxc.types.get_account_customizations_output
    import capo_uxc.types.list_services_input
    import capo_uxc.types.list_services_output
    import capo_uxc.types.max_results
    import capo_uxc.types.next_token
    import capo_uxc.types.regions_list
    import capo_uxc.types.service
    import capo_uxc.types.service_list
    import capo_uxc.types.update_account_customizations_input
    import capo_uxc.types.update_account_customizations_output


class uxcClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class uxcClient:
    """A client for the ``uxc`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = uxcClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[uxcClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: uxcClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def get_account_customizations(
        self, *, config_overrides: Optional[uxcClientConfig] = None
    ) -> "capo_uxc.types.get_account_customizations_output.GetAccountCustomizationsOutput":
        """<p>Returns the current account customization settings, including account color, visible services, and visible Regions. Settings that you have not configured return their default values: visible Regions and visible services return `null`, and account color returns `none`.</p> <note> <p>The <code>visibleServices</code> and <code>visibleRegions</code> settings control only the appearance of services and Regions in the Amazon Web Services Management Console. They do not restrict access through the CLI, SDKs, or other APIs.</p> </note>

        Raises:
            capo_uxc.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. Verify that your IAM policy includes the required <code>uxc:</code> permissions for the operation that you are calling. For more information on IAM permissions, see <a href="https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/security-iam-awsmanpol.html">Amazon Web Services managed policies for Amazon Web Services Management Console</a>.</p>
            capo_uxc.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_uxc.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce the frequency of your requests.</p>
            capo_uxc.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_uxc.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get account customizations
            Retrieves all account customization settings

            >>> client.get_account_customizations()
        """

        def _handler(
            req: "OperationRequest[capo_uxc.types.get_account_customizations_input.GetAccountCustomizationsInput]",
        ) -> OperationResponse[
            "capo_uxc.types.get_account_customizations_output.GetAccountCustomizationsOutput"
        ]:
            import capo_uxc._operations.aws_account_ux_setting.get_account_customizations

            output, http_response = (
                capo_uxc._operations.aws_account_ux_setting.get_account_customizations.get_account_customizations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_uxc.types.get_account_customizations_input.GetAccountCustomizationsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_services(
        self,
        *,
        config_overrides: Optional[uxcClientConfig] = None,
        next_token: Optional["capo_uxc.types.next_token.NextToken"] = None,
        max_results: Optional["capo_uxc.types.max_results.MaxResults"] = None,
    ) -> "capo_uxc.types.list_services_output.ListServicesOutput":
        """<p>Returns a paginated list of Amazon Web Services service identifiers that you can use as values for the <code>visibleServices</code> setting in <a href="https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_UpdateAccountCustomizations.html">UpdateAccountCustomizations</a>. The available services vary by Amazon Web Services partition. Use pagination to retrieve all results.</p> <note> <p>The <code>visibleServices</code> setting controls only the appearance of services in the Amazon Web Services Management Console. It does not restrict access through the CLI, SDKs, or other APIs.</p> </note>

        Args:
            next_token: <p>The token for retrieving the next page of results. Use the <code>nextToken</code> value from a previous response.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_uxc.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. Verify that your IAM policy includes the required <code>uxc:</code> permissions for the operation that you are calling. For more information on IAM permissions, see <a href="https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/security-iam-awsmanpol.html">Amazon Web Services managed policies for Amazon Web Services Management Console</a>.</p>
            capo_uxc.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_uxc.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce the frequency of your requests.</p>
            capo_uxc.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_uxc.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List available services
            Retrieves a paginated list of available AWS services

            >>> client.list_services()
        """

        def _handler(
            req: "OperationRequest[capo_uxc.types.list_services_input.ListServicesInput]",
        ) -> OperationResponse[
            "capo_uxc.types.list_services_output.ListServicesOutput"
        ]:
            import capo_uxc._operations.aws_account_ux_setting.list_services

            output, http_response = (
                capo_uxc._operations.aws_account_ux_setting.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_uxc.types.list_services_input.ListServicesInput = {}
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

    def iter_list_services(
        self,
        *,
        config_overrides: Optional[uxcClientConfig] = None,
        next_token: Optional["capo_uxc.types.next_token.NextToken"] = None,
        max_results: Optional["capo_uxc.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_uxc.types.service.Service]":
        _token = next_token
        while True:
            _response = self.list_services(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_account_customizations(
        self,
        *,
        config_overrides: Optional[uxcClientConfig] = None,
        account_color: Optional["capo_uxc.types.account_color.AccountColor"] = None,
        visible_services: Optional["capo_uxc.types.service_list.ServiceList"] = None,
        visible_regions: Optional["capo_uxc.types.regions_list.RegionsList"] = None,
    ) -> "capo_uxc.types.update_account_customizations_output.UpdateAccountCustomizationsOutput":
        """<p>Updates one or more account customization settings. You can update account color, visible services, and visible Regions in a single request. Only the settings that you include in the request body are modified. Omitted settings remain unchanged. To reset a setting to its default behavior, set the value to <code>null</code> for visible Regions and visible services, or <code>none</code> for account color. This operation is idempotent.</p> <note> <p>The <code>visibleServices</code> and <code>visibleRegions</code> settings control only the appearance of services and Regions in the Amazon Web Services Management Console. They do not restrict access through the CLI, SDKs, or other APIs.</p> </note>

        Args:
            account_color: <p>The account color preference to set. Set to <code>none</code> to reset to the default (no color).</p>
            visible_services: <p>The list of Amazon Web Services service identifiers to make visible in the Amazon Web Services Management Console. Set to <code>null</code> to reset to the default, which makes all services visible. For valid service identifiers, call <a href="https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_ListServices.html">ListServices</a>.</p>
            visible_regions: <p>The list of Amazon Web Services Region codes to make visible in the Amazon Web Services Management Console. Set to <code>null</code> to reset to the default, which makes all Regions visible. For a list of valid Region codes, see <a href="https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html">Amazon Web Services Regions</a>.</p>

        Raises:
            capo_uxc.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. Verify that your IAM policy includes the required <code>uxc:</code> permissions for the operation that you are calling. For more information on IAM permissions, see <a href="https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/security-iam-awsmanpol.html">Amazon Web Services managed policies for Amazon Web Services Management Console</a>.</p>
            capo_uxc.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_uxc.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce the frequency of your requests.</p>
            capo_uxc.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_uxc.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update account customizations
            Updates account customization settings with new values

            >>> client.update_account_customizations(account_color='green', visible_services=['s3', 'ec2', 'lambda'])
        """

        def _handler(
            req: "OperationRequest[capo_uxc.types.update_account_customizations_input.UpdateAccountCustomizationsInput]",
        ) -> OperationResponse[
            "capo_uxc.types.update_account_customizations_output.UpdateAccountCustomizationsOutput"
        ]:
            import capo_uxc._operations.aws_account_ux_setting.update_account_customizations

            output, http_response = (
                capo_uxc._operations.aws_account_ux_setting.update_account_customizations.update_account_customizations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_uxc.types.update_account_customizations_input.UpdateAccountCustomizationsInput = {}
        if account_color is not None:
            input_["account_color"] = account_color
        if visible_services is not None:
            input_["visible_services"] = visible_services
        if visible_regions is not None:
            input_["visible_regions"] = visible_regions

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
