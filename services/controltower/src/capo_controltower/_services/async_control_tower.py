"""Generated from Smithy shape ``com.amazonaws.controltower#AWSControlTowerApis``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_controltower._auth._signers
import capo_controltower._auth._sigv4
from capo_controltower._auth._identity import Credentials
from capo_controltower._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_controltower._auth._zapros_handler import AuthMiddleware
from capo_controltower._pagination import resolve_path as _resolve_path
from capo_controltower._resources.aws_control_tower_apis.baseline_operation_resource import (
    AsyncBaselineOperationResource,
)
from capo_controltower._resources.aws_control_tower_apis.baseline_resource import (
    AsyncBaselineResource,
)
from capo_controltower._resources.aws_control_tower_apis.control_operation_resource import (
    AsyncControlOperationResource,
)
from capo_controltower._resources.aws_control_tower_apis.enabled_baseline_resource import (
    AsyncEnabledBaselineResource,
)
from capo_controltower._resources.aws_control_tower_apis.enabled_control_resource import (
    AsyncEnabledControlResource,
)
from capo_controltower._resources.aws_control_tower_apis.landing_zone_operation_resource import (
    AsyncLandingZoneOperationResource,
)
from capo_controltower._resources.aws_control_tower_apis.landing_zone_resource import (
    AsyncLandingZoneResource,
)
from capo_controltower._resources.aws_control_tower_apis.tagging_resource import (
    AsyncTaggingResource,
)
from capo_controltower._services._aws_config import aaws_config
from capo_controltower._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.baseline_arn
    import capo_controltower.types.baseline_summary
    import capo_controltower.types.baseline_version
    import capo_controltower.types.control_identifier
    import capo_controltower.types.control_operation_filter
    import capo_controltower.types.control_operation_summary
    import capo_controltower.types.create_landing_zone_input
    import capo_controltower.types.create_landing_zone_output
    import capo_controltower.types.delete_landing_zone_input
    import capo_controltower.types.delete_landing_zone_output
    import capo_controltower.types.disable_baseline_input
    import capo_controltower.types.disable_baseline_output
    import capo_controltower.types.disable_control_input
    import capo_controltower.types.disable_control_output
    import capo_controltower.types.enable_baseline_input
    import capo_controltower.types.enable_baseline_output
    import capo_controltower.types.enable_control_input
    import capo_controltower.types.enable_control_output
    import capo_controltower.types.enabled_baseline_filter
    import capo_controltower.types.enabled_baseline_parameters
    import capo_controltower.types.enabled_baseline_summary
    import capo_controltower.types.enabled_control_filter
    import capo_controltower.types.enabled_control_parameters
    import capo_controltower.types.enabled_control_summary
    import capo_controltower.types.get_baseline_input
    import capo_controltower.types.get_baseline_operation_input
    import capo_controltower.types.get_baseline_operation_output
    import capo_controltower.types.get_baseline_output
    import capo_controltower.types.get_control_operation_input
    import capo_controltower.types.get_control_operation_output
    import capo_controltower.types.get_enabled_baseline_input
    import capo_controltower.types.get_enabled_baseline_output
    import capo_controltower.types.get_enabled_control_input
    import capo_controltower.types.get_enabled_control_output
    import capo_controltower.types.get_landing_zone_input
    import capo_controltower.types.get_landing_zone_operation_input
    import capo_controltower.types.get_landing_zone_operation_output
    import capo_controltower.types.get_landing_zone_output
    import capo_controltower.types.landing_zone_operation_filter
    import capo_controltower.types.landing_zone_operation_summary
    import capo_controltower.types.landing_zone_summary
    import capo_controltower.types.landing_zone_version
    import capo_controltower.types.list_baselines_input
    import capo_controltower.types.list_baselines_max_results
    import capo_controltower.types.list_baselines_output
    import capo_controltower.types.list_control_operations_input
    import capo_controltower.types.list_control_operations_max_results
    import capo_controltower.types.list_control_operations_next_token
    import capo_controltower.types.list_control_operations_output
    import capo_controltower.types.list_enabled_baselines_input
    import capo_controltower.types.list_enabled_baselines_max_results
    import capo_controltower.types.list_enabled_baselines_next_token
    import capo_controltower.types.list_enabled_baselines_output
    import capo_controltower.types.list_enabled_controls_input
    import capo_controltower.types.list_enabled_controls_output
    import capo_controltower.types.list_landing_zone_operations_input
    import capo_controltower.types.list_landing_zone_operations_max_results
    import capo_controltower.types.list_landing_zone_operations_output
    import capo_controltower.types.list_landing_zones_input
    import capo_controltower.types.list_landing_zones_max_results
    import capo_controltower.types.list_landing_zones_output
    import capo_controltower.types.list_tags_for_resource_input
    import capo_controltower.types.list_tags_for_resource_output
    import capo_controltower.types.manifest
    import capo_controltower.types.max_results
    import capo_controltower.types.operation_identifier
    import capo_controltower.types.remediation_types
    import capo_controltower.types.reset_enabled_baseline_input
    import capo_controltower.types.reset_enabled_baseline_output
    import capo_controltower.types.reset_enabled_control_input
    import capo_controltower.types.reset_enabled_control_output
    import capo_controltower.types.reset_landing_zone_input
    import capo_controltower.types.reset_landing_zone_output
    import capo_controltower.types.tag_keys
    import capo_controltower.types.tag_map
    import capo_controltower.types.tag_resource_input
    import capo_controltower.types.tag_resource_output
    import capo_controltower.types.target_identifier
    import capo_controltower.types.untag_resource_input
    import capo_controltower.types.untag_resource_output
    import capo_controltower.types.update_enabled_baseline_input
    import capo_controltower.types.update_enabled_baseline_output
    import capo_controltower.types.update_enabled_control_input
    import capo_controltower.types.update_enabled_control_output
    import capo_controltower.types.update_landing_zone_input
    import capo_controltower.types.update_landing_zone_output


class AsyncControlTowerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncControlTowerClient:
    """A client for the ``ControlTower`` service.

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
        self._config = AsyncControlTowerClientConfig(
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
        self.baseline_operation_resource = AsyncBaselineOperationResource(self)
        self.baseline_resource = AsyncBaselineResource(self)
        self.control_operation_resource = AsyncControlOperationResource(self)
        self.enabled_baseline_resource = AsyncEnabledBaselineResource(self)
        self.enabled_control_resource = AsyncEnabledControlResource(self)
        self.landing_zone_operation_resource = AsyncLandingZoneOperationResource(self)
        self.landing_zone_resource = AsyncLandingZoneResource(self)
        self.tagging_resource = AsyncTaggingResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncControlTowerClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncControlTowerClientConfig = config_overrides or {}
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

    async def disable_control(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        control_identifier: Optional[
            "capo_controltower.types.control_identifier.ControlIdentifier"
        ] = None,
        target_identifier: Optional[
            "capo_controltower.types.target_identifier.TargetIdentifier"
        ] = None,
        enabled_control_identifier: Optional["capo_controltower.types.arn.Arn"] = None,
    ) -> "capo_controltower.types.disable_control_output.DisableControlOutput":
        r"""<p>This API call turns off a control. It starts an asynchronous operation that deletes Amazon Web Services resources on the specified organizational unit and the accounts it contains. The resources will vary according to the control that you specify. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            control_identifier: <p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            enabled_control_identifier: <p>The ARN of the enabled control to be disabled, which uniquely identifies the control instance on the target organizational unit.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html\">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.disable_control_input.DisableControlInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.disable_control_output.DisableControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.disable_control

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.disable_control.async_disable_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.disable_control_input.DisableControlInput = {}
        if control_identifier is not None:
            input_["control_identifier"] = control_identifier
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier
        if enabled_control_identifier is not None:
            input_["enabled_control_identifier"] = enabled_control_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_baseline_operation(
        self,
        operation_identifier: "capo_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_baseline_operation_output.GetBaselineOperationOutput":
        r"""<p>Returns the details of an asynchronous baseline operation, as initiated by any of these APIs: <code>EnableBaseline</code>, <code>DisableBaseline</code>, <code>UpdateEnabledBaseline</code>, <code>ResetEnabledBaseline</code>. A status message is displayed in case of operation failure. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            operation_identifier: <p>The operation ID returned from mutating asynchronous APIs (Enable, Disable, Update, Reset).</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_baseline_operation_input.GetBaselineOperationInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_baseline_operation_output.GetBaselineOperationOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_baseline_operation

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_baseline_operation.async_get_baseline_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.get_baseline_operation_input.GetBaselineOperationInput = {
            "operation_identifier": operation_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_baseline(
        self,
        baseline_identifier: "capo_controltower.types.baseline_arn.BaselineArn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_baseline_output.GetBaselineOutput":
        r"""<p>Retrieve details about an existing <code>Baseline</code> resource by specifying its identifier. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_identifier: <p>The ARN of the <code>Baseline</code> resource to be retrieved.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_baseline_input.GetBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_baseline_output.GetBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_baseline.async_get_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.get_baseline_input.GetBaselineInput = {
            "baseline_identifier": baseline_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_baselines(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_baselines_max_results.ListBaselinesMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_baselines_output.ListBaselinesOutput":
        r"""<p>Returns a summary list of all available baselines. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_baselines_input.ListBaselinesInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_baselines_output.ListBaselinesOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_baselines

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_baselines.async_list_baselines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.list_baselines_input.ListBaselinesInput = {}
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

    async def iter_list_baselines(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_baselines_max_results.ListBaselinesMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_controltower.types.baseline_summary.BaselineSummary]":
        _token = next_token
        while True:
            _response = await self.list_baselines(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("baselines",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_control_operation(
        self,
        operation_identifier: "capo_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> (
        "capo_controltower.types.get_control_operation_output.GetControlOperationOutput"
    ):
        r"""<p>Returns the status of a particular <code>EnableControl</code> or <code>DisableControl</code> operation. Displays a message in case of error. Details for an operation are available for 90 days. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            operation_identifier: <p>The ID of the asynchronous operation, which is used to track status. The operation is available for 90 days.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_control_operation_input.GetControlOperationInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_control_operation_output.GetControlOperationOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_control_operation

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_control_operation.async_get_control_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.get_control_operation_input.GetControlOperationInput = {
            "operation_identifier": operation_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_control_operations(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        filter: Optional[
            "capo_controltower.types.control_operation_filter.ControlOperationFilter"
        ] = None,
        next_token: Optional[
            "capo_controltower.types.list_control_operations_next_token.ListControlOperationsNextToken"
        ] = None,
        max_results: Optional[
            "capo_controltower.types.list_control_operations_max_results.ListControlOperationsMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_control_operations_output.ListControlOperationsOutput":
        r"""<p>Provides a list of operations in progress or queued. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html#list-control-operations-api-examples\">ListControlOperation examples</a>.</p>

        Args:
            filter: <p>An input filter for the <code>ListControlOperations</code> API that lets you select the types of control operations to view.</p>
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_control_operations_input.ListControlOperationsInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_control_operations_output.ListControlOperationsOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_control_operations

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_control_operations.async_list_control_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.list_control_operations_input.ListControlOperationsInput = {}
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_list_control_operations(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        filter: Optional[
            "capo_controltower.types.control_operation_filter.ControlOperationFilter"
        ] = None,
        next_token: Optional[
            "capo_controltower.types.list_control_operations_next_token.ListControlOperationsNextToken"
        ] = None,
        max_results: Optional[
            "capo_controltower.types.list_control_operations_max_results.ListControlOperationsMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_controltower.types.control_operation_summary.ControlOperationSummary]":
        _token = next_token
        while True:
            _response = await self.list_control_operations(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("control_operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def enable_baseline(
        self,
        baseline_version: "capo_controltower.types.baseline_version.BaselineVersion",
        baseline_identifier: "capo_controltower.types.arn.Arn",
        target_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        parameters: Optional[
            "capo_controltower.types.enabled_baseline_parameters.EnabledBaselineParameters"
        ] = None,
        tags: Optional["capo_controltower.types.tag_map.TagMap"] = None,
    ) -> "capo_controltower.types.enable_baseline_output.EnableBaselineOutput":
        r"""<p>Enable (apply) a <code>Baseline</code> to a Target. This API starts an asynchronous operation to deploy resources specified by the <code>Baseline</code> to the specified Target. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_version: <p>The specific version to be enabled of the specified baseline.</p>
            parameters: <p>A list of <code>key-value</code> objects that specify enablement parameters, where <code>key</code> is a string and <code>value</code> is a document of any type.</p>
            baseline_identifier: <p>The ARN of the baseline to be enabled.</p>
            target_identifier: <p>The ARN of the target on which the baseline will be enabled. Only OUs are supported as targets.</p>
            tags: <p>Tags associated with input to <code>EnableBaseline</code>.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html\">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.enable_baseline_input.EnableBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.enable_baseline_output.EnableBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.enable_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.enable_baseline.async_enable_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.enable_baseline_input.EnableBaselineInput = {
            "baseline_version": baseline_version,
            "baseline_identifier": baseline_identifier,
            "target_identifier": target_identifier,
        }
        if parameters is not None:
            input_["parameters"] = parameters
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_enabled_baseline(
        self,
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_enabled_baseline_output.GetEnabledBaselineOutput":
        """<p>Retrieve details of an <code>EnabledBaseline</code> resource by specifying its identifier.</p>

        Args:
            enabled_baseline_identifier: <p>Identifier of the <code>EnabledBaseline</code> resource to be retrieved, in ARN format.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_enabled_baseline_input.GetEnabledBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_enabled_baseline_output.GetEnabledBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_enabled_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_enabled_baseline.async_get_enabled_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.get_enabled_baseline_input.GetEnabledBaselineInput = {
            "enabled_baseline_identifier": enabled_baseline_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_enabled_baseline(
        self,
        baseline_version: "capo_controltower.types.baseline_version.BaselineVersion",
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        parameters: Optional[
            "capo_controltower.types.enabled_baseline_parameters.EnabledBaselineParameters"
        ] = None,
    ) -> "capo_controltower.types.update_enabled_baseline_output.UpdateEnabledBaselineOutput":
        r"""<p>Updates an <code>EnabledBaseline</code> resource's applied parameters or version. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            baseline_version: <p>Specifies the new <code>Baseline</code> version, to which the <code>EnabledBaseline</code> should be updated.</p>
            parameters: <p>Parameters to apply when making an update.</p>
            enabled_baseline_identifier: <p>Specifies the <code>EnabledBaseline</code> resource to be updated.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html\">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.update_enabled_baseline_input.UpdateEnabledBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.update_enabled_baseline_output.UpdateEnabledBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.update_enabled_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.update_enabled_baseline.async_update_enabled_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.update_enabled_baseline_input.UpdateEnabledBaselineInput = {
            "baseline_version": baseline_version,
            "enabled_baseline_identifier": enabled_baseline_identifier,
        }
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_baseline(
        self,
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.disable_baseline_output.DisableBaselineOutput":
        r"""<p>Disable an <code>EnabledBaseline</code> resource on the specified Target. This API starts an asynchronous operation to remove all resources deployed as part of the baseline enablement. The resource will vary depending on the enabled baseline. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            enabled_baseline_identifier: <p>Identifier of the <code>EnabledBaseline</code> resource to be deactivated, in ARN format.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html\">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.disable_baseline_input.DisableBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.disable_baseline_output.DisableBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.disable_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.disable_baseline.async_disable_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.disable_baseline_input.DisableBaselineInput = {
            "enabled_baseline_identifier": enabled_baseline_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_enabled_baselines(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        filter: Optional[
            "capo_controltower.types.enabled_baseline_filter.EnabledBaselineFilter"
        ] = None,
        next_token: Optional[
            "capo_controltower.types.list_enabled_baselines_next_token.ListEnabledBaselinesNextToken"
        ] = None,
        max_results: Optional[
            "capo_controltower.types.list_enabled_baselines_max_results.ListEnabledBaselinesMaxResults"
        ] = None,
        include_children: Optional[bool] = None,
    ) -> "capo_controltower.types.list_enabled_baselines_output.ListEnabledBaselinesOutput":
        r"""<p>Returns a list of summaries describing <code>EnabledBaseline</code> resources. You can filter the list by the corresponding <code>Baseline</code> or <code>Target</code> of the <code>EnabledBaseline</code> resources. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            filter: <p>A filter applied on the <code>ListEnabledBaseline</code> operation. Allowed filters are <code>baselineIdentifiers</code> and <code>targetIdentifiers</code>. The filter can be applied for either, or both.</p>
            next_token: <p>A pagination token.</p>
            max_results: <p>The maximum number of results to be shown.</p>
            include_children: <p>A value that can be set to include the child enabled baselines in responses. The default value is false.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_enabled_baselines_input.ListEnabledBaselinesInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_enabled_baselines_output.ListEnabledBaselinesOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_enabled_baselines

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_enabled_baselines.async_list_enabled_baselines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.list_enabled_baselines_input.ListEnabledBaselinesInput = {}
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if include_children is not None:
            input_["include_children"] = include_children

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_enabled_baselines(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        filter: Optional[
            "capo_controltower.types.enabled_baseline_filter.EnabledBaselineFilter"
        ] = None,
        next_token: Optional[
            "capo_controltower.types.list_enabled_baselines_next_token.ListEnabledBaselinesNextToken"
        ] = None,
        max_results: Optional[
            "capo_controltower.types.list_enabled_baselines_max_results.ListEnabledBaselinesMaxResults"
        ] = None,
        include_children: Optional[bool] = None,
    ) -> "AsyncIterator[capo_controltower.types.enabled_baseline_summary.EnabledBaselineSummary]":
        _token = next_token
        while True:
            _response = await self.list_enabled_baselines(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
                include_children=include_children,
            )
            _page = _resolve_path(_response, ("enabled_baselines",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reset_enabled_baseline(
        self,
        enabled_baseline_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.reset_enabled_baseline_output.ResetEnabledBaselineOutput":
        r"""<p>Re-enables an <code>EnabledBaseline</code> resource. For example, this API can re-apply the existing <code>Baseline</code> after a new member account is moved to the target OU. For usage examples, see <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html\"> <i>the Amazon Web Services Control Tower User Guide</i> </a>.</p>

        Args:
            enabled_baseline_identifier: <p>Specifies the ID of the <code>EnabledBaseline</code> resource to be re-enabled, in ARN format.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html\">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.reset_enabled_baseline_input.ResetEnabledBaselineInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.reset_enabled_baseline_output.ResetEnabledBaselineOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.reset_enabled_baseline

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.reset_enabled_baseline.async_reset_enabled_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.reset_enabled_baseline_input.ResetEnabledBaselineInput = {
            "enabled_baseline_identifier": enabled_baseline_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_control(
        self,
        control_identifier: "capo_controltower.types.control_identifier.ControlIdentifier",
        target_identifier: "capo_controltower.types.target_identifier.TargetIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        tags: Optional["capo_controltower.types.tag_map.TagMap"] = None,
        parameters: Optional[
            "capo_controltower.types.enabled_control_parameters.EnabledControlParameters"
        ] = None,
    ) -> "capo_controltower.types.enable_control_output.EnableControlOutput":
        r"""<p>This API call activates a control. It starts an asynchronous operation that creates Amazon Web Services resources on the specified organizational unit and the accounts it contains. The resources created will vary according to the control that you specify. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            control_identifier: <p>The ARN of the control. Only <b>Strongly recommended</b> and <b>Elective</b> controls are permitted, with the exception of the <b>Region deny</b> control. For information on how to find the <code>controlIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            tags: <p>Tags to be applied to the <code>EnabledControl</code> resource.</p>
            parameters: <p>A list of input parameter values, which are specified to configure the control when you enable it.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html\">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.enable_control_input.EnableControlInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.enable_control_output.EnableControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.enable_control

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.enable_control.async_enable_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.enable_control_input.EnableControlInput = {
            "control_identifier": control_identifier,
            "target_identifier": target_identifier,
        }
        if tags is not None:
            input_["tags"] = tags
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_enabled_control(
        self,
        enabled_control_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_enabled_control_output.GetEnabledControlOutput":
        r"""<p>Retrieves details about an enabled control. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            enabled_control_identifier: <p>The <code>controlIdentifier</code> of the enabled control.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_enabled_control_input.GetEnabledControlInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_enabled_control_output.GetEnabledControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_enabled_control

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_enabled_control.async_get_enabled_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.get_enabled_control_input.GetEnabledControlInput = {
            "enabled_control_identifier": enabled_control_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_enabled_control(
        self,
        parameters: "capo_controltower.types.enabled_control_parameters.EnabledControlParameters",
        enabled_control_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.update_enabled_control_output.UpdateEnabledControlOutput":
        r"""<p> Updates the configuration of an already enabled control.</p> <p>If the enabled control shows an <code>EnablementStatus</code> of SUCCEEDED, supply parameters that are different from the currently configured parameters. Otherwise, Amazon Web Services Control Tower will not accept the request.</p> <p>If the enabled control shows an <code>EnablementStatus</code> of FAILED, Amazon Web Services Control Tower updates the control to match any valid parameters that you supply.</p> <p>If the <code>DriftSummary</code> status for the control shows as <code>DRIFTED</code>, you cannot call this API. Instead, you can update the control by calling the <code>ResetEnabledControl</code> API. Alternatively, you can call <code>DisableControl</code> and then call <code>EnableControl</code> again. Also, you can run an extending governance operation to repair drift. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>. </p>

        Args:
            parameters: <p>A key/value pair, where <code>Key</code> is of type <code>String</code> and <code>Value</code> is of type <code>Document</code>.</p>
            enabled_control_identifier: <p> The ARN of the enabled control that will be updated. </p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html\">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.update_enabled_control_input.UpdateEnabledControlInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.update_enabled_control_output.UpdateEnabledControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.update_enabled_control

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.update_enabled_control.async_update_enabled_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.update_enabled_control_input.UpdateEnabledControlInput = {
            "parameters": parameters,
            "enabled_control_identifier": enabled_control_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_enabled_controls(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        target_identifier: Optional[
            "capo_controltower.types.target_identifier.TargetIdentifier"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional["capo_controltower.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_controltower.types.enabled_control_filter.EnabledControlFilter"
        ] = None,
        include_children: Optional[bool] = None,
    ) -> (
        "capo_controltower.types.list_enabled_controls_output.ListEnabledControlsOutput"
    ):
        r"""<p>Lists the controls enabled by Amazon Web Services Control Tower on the specified organizational unit and the accounts it contains. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            target_identifier: <p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href=\"https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html\">the overview page</a>.</p>
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>How many results to return per API call.</p>
            filter: <p>An input filter for the <code>ListEnabledControls</code> API that lets you select the types of control operations to view.</p>
            include_children: <p>A boolean value that determines whether to include enabled controls from child organizational units in the response.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_enabled_controls_input.ListEnabledControlsInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_enabled_controls_output.ListEnabledControlsOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_enabled_controls

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_enabled_controls.async_list_enabled_controls(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.list_enabled_controls_input.ListEnabledControlsInput = {}
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if include_children is not None:
            input_["include_children"] = include_children

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_enabled_controls(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        target_identifier: Optional[
            "capo_controltower.types.target_identifier.TargetIdentifier"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional["capo_controltower.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_controltower.types.enabled_control_filter.EnabledControlFilter"
        ] = None,
        include_children: Optional[bool] = None,
    ) -> "AsyncIterator[capo_controltower.types.enabled_control_summary.EnabledControlSummary]":
        _token = next_token
        while True:
            _response = await self.list_enabled_controls(
                config_overrides=config_overrides,
                target_identifier=target_identifier,
                next_token=_token,
                max_results=max_results,
                filter=filter,
                include_children=include_children,
            )
            _page = _resolve_path(_response, ("enabled_controls",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reset_enabled_control(
        self,
        enabled_control_identifier: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> (
        "capo_controltower.types.reset_enabled_control_output.ResetEnabledControlOutput"
    ):
        """<p>Resets an enabled control. Does not work for controls implemented with SCPs.</p>

        Args:
            enabled_control_identifier: <p>The ARN of the enabled control to be reset.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. See <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/request-an-increase.html\">Service quotas</a>.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.reset_enabled_control_input.ResetEnabledControlInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.reset_enabled_control_output.ResetEnabledControlOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.reset_enabled_control

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.reset_enabled_control.async_reset_enabled_control(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.reset_enabled_control_input.ResetEnabledControlInput = {
            "enabled_control_identifier": enabled_control_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_landing_zone_operation(
        self,
        operation_identifier: "capo_controltower.types.operation_identifier.OperationIdentifier",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_landing_zone_operation_output.GetLandingZoneOperationOutput":
        """<p>Returns the status of the specified landing zone operation. Details for an operation are available for 90 days.</p>

        Args:
            operation_identifier: <p>A unique identifier assigned to a landing zone operation.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_landing_zone_operation_input.GetLandingZoneOperationInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_landing_zone_operation_output.GetLandingZoneOperationOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_landing_zone_operation

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_landing_zone_operation.async_get_landing_zone_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.get_landing_zone_operation_input.GetLandingZoneOperationInput = {
            "operation_identifier": operation_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_landing_zone_operations(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        filter: Optional[
            "capo_controltower.types.landing_zone_operation_filter.LandingZoneOperationFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_landing_zone_operations_max_results.ListLandingZoneOperationsMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_landing_zone_operations_output.ListLandingZoneOperationsOutput":
        """<p>Lists all landing zone operations from the past 90 days. Results are sorted by time, with the most recent operation first.</p>

        Args:
            filter: <p>An input filter for the <code>ListLandingZoneOperations</code> API that lets you select the types of landing zone operations to view.</p>
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>How many results to return per API call.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_landing_zone_operations_input.ListLandingZoneOperationsInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_landing_zone_operations_output.ListLandingZoneOperationsOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_landing_zone_operations

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_landing_zone_operations.async_list_landing_zone_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.list_landing_zone_operations_input.ListLandingZoneOperationsInput = {}
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_list_landing_zone_operations(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        filter: Optional[
            "capo_controltower.types.landing_zone_operation_filter.LandingZoneOperationFilter"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_landing_zone_operations_max_results.ListLandingZoneOperationsMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_controltower.types.landing_zone_operation_summary.LandingZoneOperationSummary]":
        _token = next_token
        while True:
            _response = await self.list_landing_zone_operations(
                config_overrides=config_overrides,
                filter=filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("landing_zone_operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_landing_zone(
        self,
        version: "capo_controltower.types.landing_zone_version.LandingZoneVersion",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        remediation_types: Optional[
            "capo_controltower.types.remediation_types.RemediationTypes"
        ] = None,
        tags: Optional["capo_controltower.types.tag_map.TagMap"] = None,
        manifest: Optional["capo_controltower.types.manifest.Manifest"] = None,
    ) -> "capo_controltower.types.create_landing_zone_output.CreateLandingZoneOutput":
        r"""<p>Creates a new landing zone. This API call starts an asynchronous operation that creates and configures a landing zone, based on the parameters specified in the manifest JSON file.</p>

        Args:
            version: <p>The landing zone version, for example, 3.0.</p>
            remediation_types: <p>Specifies the types of remediation actions to apply when creating the landing zone, such as automatic drift correction or compliance enforcement.</p>
            tags: <p>Tags to be applied to the landing zone. </p>
            manifest: <p>The manifest JSON file is a text file that describes your Amazon Web Services resources. For examples, review <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch\">Launch your landing zone</a>. </p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.create_landing_zone_input.CreateLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.create_landing_zone_output.CreateLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.create_landing_zone

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.create_landing_zone.async_create_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.create_landing_zone_input.CreateLandingZoneInput = {
            "version": version
        }
        if remediation_types is not None:
            input_["remediation_types"] = remediation_types
        if tags is not None:
            input_["tags"] = tags
        if manifest is not None:
            input_["manifest"] = manifest

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_landing_zone(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.get_landing_zone_output.GetLandingZoneOutput":
        """<p>Returns details about the landing zone. Displays a message in case of error.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.get_landing_zone_input.GetLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.get_landing_zone_output.GetLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.get_landing_zone

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.get_landing_zone.async_get_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.get_landing_zone_input.GetLandingZoneInput = {
            "landing_zone_identifier": landing_zone_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_landing_zone(
        self,
        version: "capo_controltower.types.landing_zone_version.LandingZoneVersion",
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        remediation_types: Optional[
            "capo_controltower.types.remediation_types.RemediationTypes"
        ] = None,
        manifest: Optional["capo_controltower.types.manifest.Manifest"] = None,
    ) -> "capo_controltower.types.update_landing_zone_output.UpdateLandingZoneOutput":
        r"""<p>This API call updates the landing zone. It starts an asynchronous operation that updates the landing zone based on the new landing zone version, or on the changed parameters specified in the updated manifest file. </p>

        Args:
            version: <p>The landing zone version, for example, 3.2.</p>
            remediation_types: <p>Specifies the types of remediation actions to apply when updating the landing zone configuration.</p>
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>
            manifest: <p>The manifest file (JSON) is a text file that describes your Amazon Web Services resources. For an example, review <a href=\"https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch\">Launch your landing zone</a>. The example manifest file contains each of the available parameters. The schema for the landing zone's JSON manifest file is not published, by design.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.update_landing_zone_input.UpdateLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.update_landing_zone_output.UpdateLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.update_landing_zone

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.update_landing_zone.async_update_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.update_landing_zone_input.UpdateLandingZoneInput = {
            "version": version,
            "landing_zone_identifier": landing_zone_identifier,
        }
        if remediation_types is not None:
            input_["remediation_types"] = remediation_types
        if manifest is not None:
            input_["manifest"] = manifest

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_landing_zone(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.delete_landing_zone_output.DeleteLandingZoneOutput":
        """<p>Decommissions a landing zone. This API call starts an asynchronous operation that deletes Amazon Web Services Control Tower resources deployed in accounts managed by Amazon Web Services Control Tower.</p> <p>Decommissioning a landing zone is a process with significant consequences, and it cannot be undone. We strongly recommend that you perform this decommissioning process only if you intend to stop using your landing zone.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.delete_landing_zone_input.DeleteLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.delete_landing_zone_output.DeleteLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.delete_landing_zone

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.delete_landing_zone.async_delete_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.delete_landing_zone_input.DeleteLandingZoneInput = {
            "landing_zone_identifier": landing_zone_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_landing_zones(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_landing_zones_max_results.ListLandingZonesMaxResults"
        ] = None,
    ) -> "capo_controltower.types.list_landing_zones_output.ListLandingZonesOutput":
        """<p>Returns the landing zone ARN for the landing zone deployed in your managed account. This API also creates an ARN for existing accounts that do not yet have a landing zone ARN. </p> <p>Returns one landing zone ARN.</p>

        Args:
            next_token: <p>The token to continue the list from a previous API call with the same parameters.</p>
            max_results: <p>The maximum number of returned landing zone ARNs, which is one.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_landing_zones_input.ListLandingZonesInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_landing_zones_output.ListLandingZonesOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_landing_zones

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_landing_zones.async_list_landing_zones(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.list_landing_zones_input.ListLandingZonesInput = {}
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

    async def iter_list_landing_zones(
        self,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_controltower.types.list_landing_zones_max_results.ListLandingZonesMaxResults"
        ] = None,
    ) -> (
        "AsyncIterator[capo_controltower.types.landing_zone_summary.LandingZoneSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_landing_zones(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("landing_zones",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reset_landing_zone(
        self,
        landing_zone_identifier: str,
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.reset_landing_zone_output.ResetLandingZoneOutput":
        """<p>This API call resets a landing zone. It starts an asynchronous operation that resets the landing zone to the parameters specified in the original configuration, which you specified in the manifest file. Nothing in the manifest file's original landing zone configuration is changed during the reset process, by default. This API is not the same as a rollback of a landing zone version, which is not a supported operation.</p>

        Args:
            landing_zone_identifier: <p>The unique identifier of the landing zone.</p>

        Raises:
            capo_controltower.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_controltower.errors.conflict_exception.ConflictException: <p>Updating or deleting the resource can cause an inconsistent state.</p>
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.reset_landing_zone_input.ResetLandingZoneInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.reset_landing_zone_output.ResetLandingZoneOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.reset_landing_zone

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.reset_landing_zone.async_reset_landing_zone(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.reset_landing_zone_input.ResetLandingZoneInput = {
            "landing_zone_identifier": landing_zone_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_controltower.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        r"""<p>Returns a list of tags associated with the resource. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p> The ARN of the resource.</p>

        Raises:
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_controltower.types.arn.Arn",
        tags: "capo_controltower.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.tag_resource_output.TagResourceOutput":
        r"""<p>Applies tags to a resource. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be tagged.</p>
            tags: <p>Tags to be applied to the resource.</p>

        Raises:
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.tag_resource

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_controltower.types.arn.Arn",
        tag_keys: "capo_controltower.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncControlTowerClientConfig] = None,
    ) -> "capo_controltower.types.untag_resource_output.UntagResourceOutput":
        r"""<p>Removes tags from a resource. For usage examples, see the <a href=\"https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html\"> <i>Controls Reference Guide</i> </a>.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>Tag keys to be removed from the resource.</p>

        Raises:
            capo_controltower.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred during processing of a request.</p>
            capo_controltower.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_controltower.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_controltower.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_controltower.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_controltower.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_controltower._operations.aws_control_tower_apis.untag_resource

            (
                output,
                http_response,
            ) = await capo_controltower._operations.aws_control_tower_apis.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_controltower.types.untag_resource_input.UntagResourceInput = {
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
