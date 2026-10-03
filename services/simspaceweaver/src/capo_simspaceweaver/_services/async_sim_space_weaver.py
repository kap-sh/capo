"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimSpaceWeaver``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_simspaceweaver._auth._signers
import capo_simspaceweaver._auth._sigv4
from capo_simspaceweaver._auth._identity import Credentials
from capo_simspaceweaver._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_simspaceweaver._auth._zapros_handler import AuthMiddleware
from capo_simspaceweaver._pagination import resolve_path as _resolve_path
from capo_simspaceweaver._resources.sim_space_weaver.simulation import AsyncSimulation
from capo_simspaceweaver._services._aws_config import aaws_config
from capo_simspaceweaver._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_simspaceweaver.types.client_token
    import capo_simspaceweaver.types.create_snapshot_input
    import capo_simspaceweaver.types.create_snapshot_output
    import capo_simspaceweaver.types.delete_app_input
    import capo_simspaceweaver.types.delete_app_output
    import capo_simspaceweaver.types.delete_simulation_input
    import capo_simspaceweaver.types.delete_simulation_output
    import capo_simspaceweaver.types.describe_app_input
    import capo_simspaceweaver.types.describe_app_output
    import capo_simspaceweaver.types.describe_simulation_input
    import capo_simspaceweaver.types.describe_simulation_output
    import capo_simspaceweaver.types.description
    import capo_simspaceweaver.types.launch_overrides
    import capo_simspaceweaver.types.list_apps_input
    import capo_simspaceweaver.types.list_apps_output
    import capo_simspaceweaver.types.list_simulations_input
    import capo_simspaceweaver.types.list_simulations_output
    import capo_simspaceweaver.types.list_tags_for_resource_input
    import capo_simspaceweaver.types.list_tags_for_resource_output
    import capo_simspaceweaver.types.optional_string
    import capo_simspaceweaver.types.positive_integer
    import capo_simspaceweaver.types.role_arn
    import capo_simspaceweaver.types.s3_destination
    import capo_simspaceweaver.types.s3_location
    import capo_simspaceweaver.types.sim_space_weaver_arn
    import capo_simspaceweaver.types.sim_space_weaver_long_resource_name
    import capo_simspaceweaver.types.sim_space_weaver_resource_name
    import capo_simspaceweaver.types.start_app_input
    import capo_simspaceweaver.types.start_app_output
    import capo_simspaceweaver.types.start_clock_input
    import capo_simspaceweaver.types.start_clock_output
    import capo_simspaceweaver.types.start_simulation_input
    import capo_simspaceweaver.types.start_simulation_output
    import capo_simspaceweaver.types.stop_app_input
    import capo_simspaceweaver.types.stop_app_output
    import capo_simspaceweaver.types.stop_clock_input
    import capo_simspaceweaver.types.stop_clock_output
    import capo_simspaceweaver.types.stop_simulation_input
    import capo_simspaceweaver.types.stop_simulation_output
    import capo_simspaceweaver.types.tag_key_list
    import capo_simspaceweaver.types.tag_map
    import capo_simspaceweaver.types.tag_resource_input
    import capo_simspaceweaver.types.tag_resource_output
    import capo_simspaceweaver.types.time_to_live_string
    import capo_simspaceweaver.types.untag_resource_input
    import capo_simspaceweaver.types.untag_resource_output


class AsyncSimSpaceWeaverClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncSimSpaceWeaverClient:
    """A client for the ``SimSpaceWeaver`` service.

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
        self._config = AsyncSimSpaceWeaverClientConfig(
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
        self.simulation = AsyncSimulation(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSimSpaceWeaverClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists all tags on a SimSpace Weaver resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.list_tags_for_resource_input.ListTagsForResourceInput = {
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
        resource_arn: "capo_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn",
        tags: "capo_simspaceweaver.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.tag_resource_output.TagResourceOutput":
        """<p>Adds tags to a SimSpace Weaver resource. For more information about tags, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to add tags to. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tags: <p>A list of tags to apply to the resource.</p>

        Raises:
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.too_many_tags_exception.TooManyTagsException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.tag_resource

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn",
        tag_keys: "capo_simspaceweaver.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.untag_resource_output.UntagResourceOutput":
        """<p>Removes tags from a SimSpace Weaver resource. For more information about tags, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tag_keys: <p>A list of tag keys to remove from the resource.</p>

        Raises:
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.untag_resource

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.untag_resource_input.UntagResourceInput = {
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

    async def start_simulation(
        self,
        name: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        role_arn: "capo_simspaceweaver.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
        client_token: Optional[
            "capo_simspaceweaver.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_simspaceweaver.types.description.Description"
        ] = None,
        schema_s3_location: Optional[
            "capo_simspaceweaver.types.s3_location.S3Location"
        ] = None,
        maximum_duration: Optional[
            "capo_simspaceweaver.types.time_to_live_string.TimeToLiveString"
        ] = None,
        tags: Optional["capo_simspaceweaver.types.tag_map.TagMap"] = None,
        snapshot_s3_location: Optional[
            "capo_simspaceweaver.types.s3_location.S3Location"
        ] = None,
    ) -> "capo_simspaceweaver.types.start_simulation_output.StartSimulationOutput":
        """<p>Starts a simulation with the given name. You must choose to start your simulation from a schema or from a snapshot. For more information about the schema, see the <a href="https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference.html">schema reference</a> in the <i>SimSpace Weaver User Guide</i>. For more information about snapshots, see <a href="https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots.html">Snapshots</a> in the <i>SimSpace Weaver User Guide</i>.</p>

        Args:
            client_token: <p>A value that you provide to ensure that repeated calls to this API operation using the same parameters complete only once. A <code>ClientToken</code> is also known as an <i>idempotency token</i>. A <code>ClientToken</code> expires after 24 hours.</p>
            name: <p>The name of the simulation.</p>
            description: <p>The description of the simulation.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the simulation assumes to perform actions. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>. For more information about IAM roles, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM roles</a> in the <i>Identity and Access Management User Guide</i>.</p>
            schema_s3_location: <p>The location of the simulation schema in Amazon Simple Storage Service (Amazon S3). For more information about Amazon S3, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html"> <i>Amazon Simple Storage Service User Guide</i> </a>.</p> <p>Provide a <code>SchemaS3Location</code> to start your simulation from a schema.</p> <p>If you provide a <code>SchemaS3Location</code> then you can't provide a <code>SnapshotS3Location</code>.</p>
            maximum_duration: <p>The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is <code>14D</code>, or its equivalent in the other units. The default value is <code>14D</code>. A value equivalent to <code>0</code> makes the simulation immediately transition to <code>Stopping</code> as soon as it reaches <code>Started</code>.</p>
            tags: <p>A list of tags for the simulation. For more information about tags, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p>
            snapshot_s3_location: <p>The location of the snapshot .zip file in Amazon Simple Storage Service (Amazon S3). For more information about Amazon S3, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html"> <i>Amazon Simple Storage Service User Guide</i> </a>.</p> <p>Provide a <code>SnapshotS3Location</code> to start your simulation from a snapshot.</p> <p>The Amazon S3 bucket must be in the same Amazon Web Services Region as the simulation.</p> <p>If you provide a <code>SnapshotS3Location</code> then you can't provide a <code>SchemaS3Location</code>.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.conflict_exception.ConflictException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.start_simulation_input.StartSimulationInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.start_simulation_output.StartSimulationOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.start_simulation

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.start_simulation.async_start_simulation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.start_simulation_input.StartSimulationInput = {
            "name": name,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if schema_s3_location is not None:
            input_["schema_s3_location"] = schema_s3_location
        if maximum_duration is not None:
            input_["maximum_duration"] = maximum_duration
        if tags is not None:
            input_["tags"] = tags
        if snapshot_s3_location is not None:
            input_["snapshot_s3_location"] = snapshot_s3_location

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_simulation(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> (
        "capo_simspaceweaver.types.describe_simulation_output.DescribeSimulationOutput"
    ):
        """<p>Returns the current state of the given simulation.</p>

        Args:
            simulation: <p>The name of the simulation.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.describe_simulation_input.DescribeSimulationInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.describe_simulation_output.DescribeSimulationOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.describe_simulation

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.describe_simulation.async_describe_simulation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.describe_simulation_input.DescribeSimulationInput = {
            "simulation": simulation
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_simulation(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.stop_simulation_output.StopSimulationOutput":
        """<p>Stops the given simulation.</p> <important> <p>You can't restart a simulation after you stop it. If you want to restart a simulation, then you must stop it, delete it, and start a new instance of it.</p> </important>

        Args:
            simulation: <p>The name of the simulation.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.conflict_exception.ConflictException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.stop_simulation_input.StopSimulationInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.stop_simulation_output.StopSimulationOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.stop_simulation

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.stop_simulation.async_stop_simulation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.stop_simulation_input.StopSimulationInput = {
            "simulation": simulation
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_simulation(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.delete_simulation_output.DeleteSimulationOutput":
        """<p>Deletes all SimSpace Weaver resources assigned to the given simulation.</p> <note> <p>Your simulation uses resources in other Amazon Web Services. This API operation doesn't delete resources in other Amazon Web Services.</p> </note>

        Args:
            simulation: <p>The name of the simulation.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.conflict_exception.ConflictException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.delete_simulation_input.DeleteSimulationInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.delete_simulation_output.DeleteSimulationOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.delete_simulation

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.delete_simulation.async_delete_simulation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.delete_simulation_input.DeleteSimulationInput = {
            "simulation": simulation
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_simulations(
        self,
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
        max_results: Optional[
            "capo_simspaceweaver.types.positive_integer.PositiveInteger"
        ] = None,
        next_token: Optional[
            "capo_simspaceweaver.types.optional_string.OptionalString"
        ] = None,
    ) -> "capo_simspaceweaver.types.list_simulations_output.ListSimulationsOutput":
        """<p>Lists the SimSpace Weaver simulations in the Amazon Web Services account used to make the API call.</p>

        Args:
            max_results: <p>The maximum number of simulations to list.</p>
            next_token: <p>If SimSpace Weaver returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an <i>HTTP 400 ValidationException</i> error.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.list_simulations_input.ListSimulationsInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.list_simulations_output.ListSimulationsOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.list_simulations

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.list_simulations.async_list_simulations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.list_simulations_input.ListSimulationsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_simulations(
        self,
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
        max_results: Optional[
            "capo_simspaceweaver.types.positive_integer.PositiveInteger"
        ] = None,
        next_token: Optional[
            "capo_simspaceweaver.types.optional_string.OptionalString"
        ] = None,
    ) -> "AsyncIterator[capo_simspaceweaver.types.list_simulations_output.ListSimulationsOutput]":
        _token = next_token
        while True:
            _response = await self.list_simulations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_snapshot(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        destination: "capo_simspaceweaver.types.s3_destination.S3Destination",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.create_snapshot_output.CreateSnapshotOutput":
        """<p>Creates a snapshot of the specified simulation. A snapshot is a file that contains simulation state data at a specific time. The state data saved in a snapshot includes entity data from the State Fabric, the simulation configuration specified in the schema, and the clock tick number. You can use the snapshot to initialize a new simulation. For more information about snapshots, see <a href="https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots.html">Snapshots</a> in the <i>SimSpace Weaver User Guide</i>. </p> <p>You specify a <code>Destination</code> when you create a snapshot. The <code>Destination</code> is the name of an Amazon S3 bucket and an optional <code>ObjectKeyPrefix</code>. The <code>ObjectKeyPrefix</code> is usually the name of a folder in the bucket. SimSpace Weaver creates a <code>snapshot</code> folder inside the <code>Destination</code> and places the snapshot file there.</p> <p>The snapshot file is an Amazon S3 object. It has an object key with the form: <code> <i>object-key-prefix</i>/snapshot/<i>simulation-name</i>-<i>YYMMdd</i>-<i>HHmm</i>-<i>ss</i>.zip</code>, where: </p> <ul> <li> <p> <code> <i>YY</i> </code> is the 2-digit year</p> </li> <li> <p> <code> <i>MM</i> </code> is the 2-digit month</p> </li> <li> <p> <code> <i>dd</i> </code> is the 2-digit day of the month</p> </li> <li> <p> <code> <i>HH</i> </code> is the 2-digit hour (24-hour clock)</p> </li> <li> <p> <code> <i>mm</i> </code> is the 2-digit minutes</p> </li> <li> <p> <code> <i>ss</i> </code> is the 2-digit seconds</p> </li> </ul>

        Args:
            simulation: <p>The name of the simulation.</p>
            destination: <p>The Amazon S3 bucket and optional folder (object key prefix) where SimSpace Weaver creates the snapshot file.</p> <p>The Amazon S3 bucket must be in the same Amazon Web Services Region as the simulation.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.conflict_exception.ConflictException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.create_snapshot_input.CreateSnapshotInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.create_snapshot_output.CreateSnapshotOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.create_snapshot

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.create_snapshot.async_create_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.create_snapshot_input.CreateSnapshotInput = {
            "simulation": simulation,
            "destination": destination,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_app(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        domain: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        app: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.delete_app_output.DeleteAppOutput":
        """<p>Deletes the instance of the given custom app.</p>

        Args:
            simulation: <p>The name of the simulation of the app.</p>
            domain: <p>The name of the domain of the app.</p>
            app: <p>The name of the app.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.conflict_exception.ConflictException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.delete_app_input.DeleteAppInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.delete_app_output.DeleteAppOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.delete_app

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.delete_app.async_delete_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.delete_app_input.DeleteAppInput = {
            "simulation": simulation,
            "domain": domain,
            "app": app,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_app(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        domain: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        app: "capo_simspaceweaver.types.sim_space_weaver_long_resource_name.SimSpaceWeaverLongResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.describe_app_output.DescribeAppOutput":
        """<p>Returns the state of the given custom app.</p>

        Args:
            simulation: <p>The name of the simulation of the app.</p>
            domain: <p>The name of the domain of the app.</p>
            app: <p>The name of the app.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.describe_app_input.DescribeAppInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.describe_app_output.DescribeAppOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.describe_app

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.describe_app.async_describe_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.describe_app_input.DescribeAppInput = {
            "simulation": simulation,
            "domain": domain,
            "app": app,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_apps(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
        domain: Optional[
            "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
        ] = None,
        max_results: Optional[
            "capo_simspaceweaver.types.positive_integer.PositiveInteger"
        ] = None,
        next_token: Optional[
            "capo_simspaceweaver.types.optional_string.OptionalString"
        ] = None,
    ) -> "capo_simspaceweaver.types.list_apps_output.ListAppsOutput":
        """<p>Lists all custom apps or service apps for the given simulation and domain.</p>

        Args:
            simulation: <p>The name of the simulation that you want to list apps for.</p>
            domain: <p>The name of the domain that you want to list apps for.</p>
            max_results: <p>The maximum number of apps to list.</p>
            next_token: <p>If SimSpace Weaver returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an <i>HTTP 400 ValidationException</i> error.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.list_apps_input.ListAppsInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.list_apps_output.ListAppsOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.list_apps

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.list_apps.async_list_apps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.list_apps_input.ListAppsInput = {
            "simulation": simulation
        }
        if domain is not None:
            input_["domain"] = domain
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_apps(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
        domain: Optional[
            "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
        ] = None,
        max_results: Optional[
            "capo_simspaceweaver.types.positive_integer.PositiveInteger"
        ] = None,
        next_token: Optional[
            "capo_simspaceweaver.types.optional_string.OptionalString"
        ] = None,
    ) -> "AsyncIterator[capo_simspaceweaver.types.list_apps_output.ListAppsOutput]":
        _token = next_token
        while True:
            _response = await self.list_apps(
                simulation,
                config_overrides=config_overrides,
                domain=domain,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_app(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        domain: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        name: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
        client_token: Optional[
            "capo_simspaceweaver.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_simspaceweaver.types.description.Description"
        ] = None,
        launch_overrides: Optional[
            "capo_simspaceweaver.types.launch_overrides.LaunchOverrides"
        ] = None,
    ) -> "capo_simspaceweaver.types.start_app_output.StartAppOutput":
        """<p>Starts a custom app with the configuration specified in the simulation schema.</p>

        Args:
            client_token: <p>A value that you provide to ensure that repeated calls to this API operation using the same parameters complete only once. A <code>ClientToken</code> is also known as an <i>idempotency token</i>. A <code>ClientToken</code> expires after 24 hours.</p>
            simulation: <p>The name of the simulation of the app.</p>
            domain: <p>The name of the domain of the app.</p>
            name: <p>The name of the app.</p>
            description: <p>The description of the app.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.conflict_exception.ConflictException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.start_app_input.StartAppInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.start_app_output.StartAppOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.start_app

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.start_app.async_start_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.start_app_input.StartAppInput = {
            "simulation": simulation,
            "domain": domain,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if launch_overrides is not None:
            input_["launch_overrides"] = launch_overrides

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_clock(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.start_clock_output.StartClockOutput":
        """<p>Starts the simulation clock.</p>

        Args:
            simulation: <p>The name of the simulation.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.conflict_exception.ConflictException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.start_clock_input.StartClockInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.start_clock_output.StartClockOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.start_clock

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.start_clock.async_start_clock(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.start_clock_input.StartClockInput = {
            "simulation": simulation
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_app(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        domain: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        app: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.stop_app_output.StopAppOutput":
        """<p>Stops the given custom app and shuts down all of its allocated compute resources.</p>

        Args:
            simulation: <p>The name of the simulation of the app.</p>
            domain: <p>The name of the domain of the app.</p>
            app: <p>The name of the app.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.conflict_exception.ConflictException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.stop_app_input.StopAppInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.stop_app_output.StopAppOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.stop_app

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.stop_app.async_stop_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.stop_app_input.StopAppInput = {
            "simulation": simulation,
            "domain": domain,
            "app": app,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_clock(
        self,
        simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName",
        *,
        config_overrides: Optional[AsyncSimSpaceWeaverClientConfig] = None,
    ) -> "capo_simspaceweaver.types.stop_clock_output.StopClockOutput":
        """<p>Stops the simulation clock.</p>

        Args:
            simulation: <p>The name of the simulation.</p>

        Raises:
            capo_simspaceweaver.errors.access_denied_exception.AccessDeniedException: <p/>
            capo_simspaceweaver.errors.conflict_exception.ConflictException: <p/>
            capo_simspaceweaver.errors.internal_server_exception.InternalServerException: <p/>
            capo_simspaceweaver.errors.resource_not_found_exception.ResourceNotFoundException: <p/>
            capo_simspaceweaver.errors.validation_exception.ValidationException: <p/>
            capo_simspaceweaver.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_simspaceweaver.types.stop_clock_input.StopClockInput]",
        ) -> AsyncOperationResponse[
            "capo_simspaceweaver.types.stop_clock_output.StopClockOutput"
        ]:
            import capo_simspaceweaver._operations.sim_space_weaver.stop_clock

            (
                output,
                http_response,
            ) = await capo_simspaceweaver._operations.sim_space_weaver.stop_clock.async_stop_clock(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_simspaceweaver.types.stop_clock_input.StopClockInput = {
            "simulation": simulation
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
