"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlCatalog``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_controlcatalog._auth._signers
import capo_controlcatalog._auth._sigv4
from capo_controlcatalog._auth._identity import Credentials
from capo_controlcatalog._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_controlcatalog._auth._zapros_handler import AuthMiddleware
from capo_controlcatalog._pagination import resolve_path as _resolve_path
from capo_controlcatalog._resources.control_catalog.common_control_resource import (
    CommonControlResource,
)
from capo_controlcatalog._resources.control_catalog.control_resource import (
    ControlResource,
)
from capo_controlcatalog._resources.control_catalog.domain_resource import (
    DomainResource,
)
from capo_controlcatalog._resources.control_catalog.objective_resource import (
    ObjectiveResource,
)
from capo_controlcatalog._services._aws_config import aws_config
from capo_controlcatalog._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_controlcatalog.types.common_control_filter
    import capo_controlcatalog.types.common_control_summary
    import capo_controlcatalog.types.control_arn
    import capo_controlcatalog.types.control_filter
    import capo_controlcatalog.types.control_mapping
    import capo_controlcatalog.types.control_mapping_filter
    import capo_controlcatalog.types.control_summary
    import capo_controlcatalog.types.domain_summary
    import capo_controlcatalog.types.get_control_request
    import capo_controlcatalog.types.get_control_response
    import capo_controlcatalog.types.list_common_controls_request
    import capo_controlcatalog.types.list_common_controls_response
    import capo_controlcatalog.types.list_control_mappings_request
    import capo_controlcatalog.types.list_control_mappings_response
    import capo_controlcatalog.types.list_controls_request
    import capo_controlcatalog.types.list_controls_response
    import capo_controlcatalog.types.list_domains_request
    import capo_controlcatalog.types.list_domains_response
    import capo_controlcatalog.types.list_objectives_request
    import capo_controlcatalog.types.list_objectives_response
    import capo_controlcatalog.types.max_list_common_controls_results
    import capo_controlcatalog.types.max_list_control_mappings_results
    import capo_controlcatalog.types.max_list_controls_results
    import capo_controlcatalog.types.max_list_domains_results
    import capo_controlcatalog.types.max_list_objectives_results
    import capo_controlcatalog.types.objective_filter
    import capo_controlcatalog.types.objective_summary
    import capo_controlcatalog.types.pagination_token


class ControlCatalogClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ControlCatalogClient:
    """A client for the ``ControlCatalog`` service.

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
        self._config = ControlCatalogClientConfig(
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
        self.common_control_resource = CommonControlResource(self)
        self.control_resource = ControlResource(self)
        self.domain_resource = DomainResource(self)
        self.objective_resource = ObjectiveResource(self)

    def operation_options(
        self, config_overrides: Optional[ControlCatalogClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ControlCatalogClientConfig = config_overrides or {}
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

    def list_control_mappings(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_control_mappings_results.MaxListControlMappingsResults"
        ] = None,
        filter: Optional[
            "capo_controlcatalog.types.control_mapping_filter.ControlMappingFilter"
        ] = None,
    ) -> "capo_controlcatalog.types.list_control_mappings_response.ListControlMappingsResponse":
        """<p>Returns a paginated list of control mappings from the Control Catalog. Control mappings show relationships between controls and other entities, such as common controls or compliance frameworks.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            filter: <p>An optional filter that narrows the results to specific control mappings based on control ARNs, common control ARNs, or mapping types.</p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controlcatalog.types.list_control_mappings_request.ListControlMappingsRequest]",
        ) -> OperationResponse[
            "capo_controlcatalog.types.list_control_mappings_response.ListControlMappingsResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.list_control_mappings

            output, http_response = (
                capo_controlcatalog._operations.control_catalog.list_control_mappings.list_control_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controlcatalog.types.list_control_mappings_request.ListControlMappingsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_control_mappings(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_control_mappings_results.MaxListControlMappingsResults"
        ] = None,
        filter: Optional[
            "capo_controlcatalog.types.control_mapping_filter.ControlMappingFilter"
        ] = None,
    ) -> "Iterator[capo_controlcatalog.types.control_mapping.ControlMapping]":
        _token = next_token
        while True:
            _response = self.list_control_mappings(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("control_mappings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_common_controls(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_common_controls_results.MaxListCommonControlsResults"
        ] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        common_control_filter: Optional[
            "capo_controlcatalog.types.common_control_filter.CommonControlFilter"
        ] = None,
    ) -> "capo_controlcatalog.types.list_common_controls_response.ListCommonControlsResponse":
        """<p>Returns a paginated list of common controls from the Amazon Web Services Control Catalog.</p> <p>You can apply an optional filter to see common controls that have a specific objective. If you don’t provide a filter, the operation returns all common controls. </p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            common_control_filter: <p>An optional filter that narrows the results to a specific objective.</p> <p>This filter allows you to specify one objective ARN at a time. Passing multiple ARNs in the <code>CommonControlFilter</code> isn’t supported.</p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controlcatalog.types.list_common_controls_request.ListCommonControlsRequest]",
        ) -> OperationResponse[
            "capo_controlcatalog.types.list_common_controls_response.ListCommonControlsResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.list_common_controls

            output, http_response = (
                capo_controlcatalog._operations.control_catalog.list_common_controls.list_common_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controlcatalog.types.list_common_controls_request.ListCommonControlsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if common_control_filter is not None:
            input_["common_control_filter"] = common_control_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_common_controls(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_common_controls_results.MaxListCommonControlsResults"
        ] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        common_control_filter: Optional[
            "capo_controlcatalog.types.common_control_filter.CommonControlFilter"
        ] = None,
    ) -> "Iterator[capo_controlcatalog.types.common_control_summary.CommonControlSummary]":
        _token = next_token
        while True:
            _response = self.list_common_controls(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                common_control_filter=common_control_filter,
            )
            _page = _resolve_path(_response, ("common_controls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_control(
        self,
        control_arn: "capo_controlcatalog.types.control_arn.ControlArn",
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
    ) -> "capo_controlcatalog.types.get_control_response.GetControlResponse":
        r"""<p>Returns details about a specific control, most notably a list of Amazon Web Services Regions where this control is supported. Input a value for the <i>ControlArn</i> parameter, in ARN form. <code>GetControl</code> accepts <i>controltower</i> or <i>controlcatalog</i> control ARNs as input. Returns a <i>controlcatalog</i> ARN format.</p> <p>In the API response, controls that have the value <code>GLOBAL</code> in the <code>Scope</code> field do not show the <code>DeployableRegions</code> field, because it does not apply. Controls that have the value <code>REGIONAL</code> in the <code>Scope</code> field return a value for the <code>DeployableRegions</code> field, as shown in the example.</p>

        Args:
            control_arn: <p>The Amazon Resource Name (ARN) of the control. It has one of the following formats:</p> <p> <i>Global format</i> </p> <p> <code>arn:{PARTITION}:controlcatalog:::control/{CONTROL_CATALOG_OPAQUE_ID}</code> </p> <p> <i>Or Regional format</i> </p> <p> <code>arn:{PARTITION}:controltower:{REGION}::control/{CONTROL_TOWER_OPAQUE_ID}</code> </p> <p>Here is a more general pattern that covers Amazon Web Services Control Tower and Control Catalog ARNs:</p> <p> <code>^arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\\-]+$</code> </p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource does not exist.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controlcatalog.types.get_control_request.GetControlRequest]",
        ) -> OperationResponse[
            "capo_controlcatalog.types.get_control_response.GetControlResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.get_control

            output, http_response = (
                capo_controlcatalog._operations.control_catalog.get_control.get_control(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controlcatalog.types.get_control_request.GetControlRequest = {
            "control_arn": control_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_controls(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_controls_results.MaxListControlsResults"
        ] = None,
        filter: Optional[
            "capo_controlcatalog.types.control_filter.ControlFilter"
        ] = None,
    ) -> "capo_controlcatalog.types.list_controls_response.ListControlsResponse":
        """<p>Returns a paginated list of all available controls in the Control Catalog library. Allows you to discover available controls. The list of controls is given as structures of type <i>controlSummary</i>. The ARN is returned in the global <i>controlcatalog</i> format, as shown in the examples.</p>

        Args:
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            filter: <p>An optional filter that narrows the results to controls with specific implementation types or identifiers. If you don't provide a filter, the operation returns all available controls.</p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controlcatalog.types.list_controls_request.ListControlsRequest]",
        ) -> OperationResponse[
            "capo_controlcatalog.types.list_controls_response.ListControlsResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.list_controls

            output, http_response = (
                capo_controlcatalog._operations.control_catalog.list_controls.list_controls(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controlcatalog.types.list_controls_request.ListControlsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_controls(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_controls_results.MaxListControlsResults"
        ] = None,
        filter: Optional[
            "capo_controlcatalog.types.control_filter.ControlFilter"
        ] = None,
    ) -> "Iterator[capo_controlcatalog.types.control_summary.ControlSummary]":
        _token = next_token
        while True:
            _response = self.list_controls(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("controls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_domains(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_domains_results.MaxListDomainsResults"
        ] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_controlcatalog.types.list_domains_response.ListDomainsResponse":
        """<p>Returns a paginated list of domains from the Control Catalog.</p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controlcatalog.types.list_domains_request.ListDomainsRequest]",
        ) -> OperationResponse[
            "capo_controlcatalog.types.list_domains_response.ListDomainsResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.list_domains

            output, http_response = (
                capo_controlcatalog._operations.control_catalog.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controlcatalog.types.list_domains_request.ListDomainsRequest = {}
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

    def iter_list_domains(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_domains_results.MaxListDomainsResults"
        ] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_controlcatalog.types.domain_summary.DomainSummary]":
        _token = next_token
        while True:
            _response = self.list_domains(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("domains",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_objectives(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_objectives_results.MaxListObjectivesResults"
        ] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        objective_filter: Optional[
            "capo_controlcatalog.types.objective_filter.ObjectiveFilter"
        ] = None,
    ) -> "capo_controlcatalog.types.list_objectives_response.ListObjectivesResponse":
        """<p>Returns a paginated list of objectives from the Control Catalog.</p> <p>You can apply an optional filter to see the objectives that belong to a specific domain. If you don’t provide a filter, the operation returns all objectives. </p>

        Args:
            max_results: <p>The maximum number of results on a page or for an API request call.</p>
            next_token: <p>The pagination token that's used to fetch the next set of results.</p>
            objective_filter: <p>An optional filter that narrows the results to a specific domain.</p> <p>This filter allows you to specify one domain ARN at a time. Passing multiple ARNs in the <code>ObjectiveFilter</code> isn’t supported.</p>

        Raises:
            capo_controlcatalog.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controlcatalog.errors.internal_server_exception.InternalServerException: <p>An internal service error occurred during the processing of your request. Try again later.</p>
            capo_controlcatalog.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controlcatalog.errors.validation_exception.ValidationException: <p>The request has invalid or missing parameters.</p>
            capo_controlcatalog.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_controlcatalog.types.list_objectives_request.ListObjectivesRequest]",
        ) -> OperationResponse[
            "capo_controlcatalog.types.list_objectives_response.ListObjectivesResponse"
        ]:
            import capo_controlcatalog._operations.control_catalog.list_objectives

            output, http_response = (
                capo_controlcatalog._operations.control_catalog.list_objectives.list_objectives(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controlcatalog.types.list_objectives_request.ListObjectivesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if objective_filter is not None:
            input_["objective_filter"] = objective_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_objectives(
        self,
        *,
        config_overrides: Optional[ControlCatalogClientConfig] = None,
        max_results: Optional[
            "capo_controlcatalog.types.max_list_objectives_results.MaxListObjectivesResults"
        ] = None,
        next_token: Optional[
            "capo_controlcatalog.types.pagination_token.PaginationToken"
        ] = None,
        objective_filter: Optional[
            "capo_controlcatalog.types.objective_filter.ObjectiveFilter"
        ] = None,
    ) -> "Iterator[capo_controlcatalog.types.objective_summary.ObjectiveSummary]":
        _token = next_token
        while True:
            _response = self.list_objectives(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                objective_filter=objective_filter,
            )
            _page = _resolve_path(_response, ("objectives",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
