"""Generated from Smithy shape ``com.amazonaws.cloud9#AWSCloud9WorkspaceManagementService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_cloud9._auth._signers
import capo_cloud9._auth._sigv4
from capo_cloud9._auth._identity import Credentials
from capo_cloud9._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloud9._auth._zapros_handler import AuthMiddleware
from capo_cloud9._pagination import resolve_path as _resolve_path
from capo_cloud9._services._aws_config import aws_config
from capo_cloud9._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_cloud9.types.automatic_stop_time_minutes
    import capo_cloud9.types.bounded_environment_id_list
    import capo_cloud9.types.client_request_token
    import capo_cloud9.types.connection_type
    import capo_cloud9.types.create_environment_ec2_request
    import capo_cloud9.types.create_environment_ec2_result
    import capo_cloud9.types.create_environment_membership_request
    import capo_cloud9.types.create_environment_membership_result
    import capo_cloud9.types.delete_environment_membership_request
    import capo_cloud9.types.delete_environment_membership_result
    import capo_cloud9.types.delete_environment_request
    import capo_cloud9.types.delete_environment_result
    import capo_cloud9.types.describe_environment_memberships_request
    import capo_cloud9.types.describe_environment_memberships_result
    import capo_cloud9.types.describe_environment_status_request
    import capo_cloud9.types.describe_environment_status_result
    import capo_cloud9.types.describe_environments_request
    import capo_cloud9.types.describe_environments_result
    import capo_cloud9.types.environment_arn
    import capo_cloud9.types.environment_description
    import capo_cloud9.types.environment_id
    import capo_cloud9.types.environment_name
    import capo_cloud9.types.image_id
    import capo_cloud9.types.instance_type
    import capo_cloud9.types.list_environments_request
    import capo_cloud9.types.list_environments_result
    import capo_cloud9.types.list_tags_for_resource_request
    import capo_cloud9.types.list_tags_for_resource_response
    import capo_cloud9.types.managed_credentials_action
    import capo_cloud9.types.max_results
    import capo_cloud9.types.member_permissions
    import capo_cloud9.types.nullable_boolean
    import capo_cloud9.types.permissions_list
    import capo_cloud9.types.string
    import capo_cloud9.types.subnet_id
    import capo_cloud9.types.tag_key_list
    import capo_cloud9.types.tag_list
    import capo_cloud9.types.tag_resource_request
    import capo_cloud9.types.tag_resource_response
    import capo_cloud9.types.untag_resource_request
    import capo_cloud9.types.untag_resource_response
    import capo_cloud9.types.update_environment_membership_request
    import capo_cloud9.types.update_environment_membership_result
    import capo_cloud9.types.update_environment_request
    import capo_cloud9.types.update_environment_result
    import capo_cloud9.types.user_arn


class Cloud9ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class Cloud9Client:
    """A client for the ``Cloud9`` service.

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
        self._config = Cloud9ClientConfig(
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
        self, config_overrides: Optional[Cloud9ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: Cloud9ClientConfig = config_overrides or {}
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

    def create_environment_ec2(
        self,
        name: "capo_cloud9.types.environment_name.EnvironmentName",
        instance_type: "capo_cloud9.types.instance_type.InstanceType",
        image_id: "capo_cloud9.types.image_id.ImageId",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
        description: Optional[
            "capo_cloud9.types.environment_description.EnvironmentDescription"
        ] = None,
        client_request_token: Optional[
            "capo_cloud9.types.client_request_token.ClientRequestToken"
        ] = None,
        subnet_id: Optional["capo_cloud9.types.subnet_id.SubnetId"] = None,
        automatic_stop_time_minutes: Optional[
            "capo_cloud9.types.automatic_stop_time_minutes.AutomaticStopTimeMinutes"
        ] = None,
        owner_arn: Optional["capo_cloud9.types.user_arn.UserArn"] = None,
        tags: Optional["capo_cloud9.types.tag_list.TagList"] = None,
        connection_type: Optional[
            "capo_cloud9.types.connection_type.ConnectionType"
        ] = None,
        dry_run: Optional["capo_cloud9.types.nullable_boolean.NullableBoolean"] = None,
    ) -> "capo_cloud9.types.create_environment_ec2_result.CreateEnvironmentEC2Result":
        """<p>Creates an Cloud9 development environment, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            name: <p>The name of the environment to create.</p> <p>This name is visible to other IAM users in the same Amazon Web Services account.</p>
            description: <p>The description of the environment to create.</p>
            client_request_token: <p>A unique, case-sensitive string that helps Cloud9 to ensure this operation completes no more than one time.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Client Tokens</a> in the <i>Amazon EC2 API Reference</i>.</p>
            instance_type: <p>The type of instance to connect to the environment (for example, <code>t2.micro</code>).</p>
            subnet_id: <p>The ID of the subnet in Amazon VPC that Cloud9 will use to communicate with the Amazon EC2 instance.</p>
            image_id: <p>The identifier for the Amazon Machine Image (AMI) that's used to create the EC2 instance. To choose an AMI for the instance, you must specify a valid AMI alias or a valid Amazon EC2 Systems Manager (SSM) path.</p> <p></p> <p>We recommend using Amazon Linux 2023 as the AMI to create your environment as it is fully supported.</p> <p>From December 16, 2024, Ubuntu 18.04 will be removed from the list of available <code>imageIds</code> for Cloud9. This change is necessary as Ubuntu 18.04 has ended standard support on May 31, 2023. This change will only affect direct API consumers, and not Cloud9 console users.</p> <p>Since Ubuntu 18.04 has ended standard support as of May 31, 2023, we recommend you choose Ubuntu 22.04.</p> <p> <b>AMI aliases </b> </p> <ul> <li> <p>Amazon Linux 2023 (recommended): <code>amazonlinux-2023-x86_64</code> </p> </li> <li> <p>Ubuntu 22.04: <code>ubuntu-22.04-x86_64</code> </p> </li> </ul> <p> <b>SSM paths</b> </p> <ul> <li> <p>Amazon Linux 2023 (recommended): <code>resolve:ssm:/aws/service/cloud9/amis/amazonlinux-2023-x86_64</code> </p> </li> <li> <p>Ubuntu 22.04: <code>resolve:ssm:/aws/service/cloud9/amis/ubuntu-22.04-x86_64</code> </p> </li> </ul>
            automatic_stop_time_minutes: <p>The number of minutes until the running instance is shut down after the environment has last been used.</p>
            owner_arn: <p>The Amazon Resource Name (ARN) of the environment owner. This ARN can be the ARN of any IAM principal. If this value is not specified, the ARN defaults to this environment's creator.</p>
            tags: <p>An array of key-value pairs that will be associated with the new Cloud9 development environment.</p>
            connection_type: <p>The connection type used for connecting to an Amazon EC2 environment. Valid values are <code>CONNECT_SSH</code> (default) and <code>CONNECT_SSM</code> (connected through Amazon EC2 Systems Manager).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html">Accessing no-ingress EC2 instances with Amazon EC2 Systems Manager</a> in the <i>Cloud9 User Guide</i>.</p>
            dry_run: <p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_cloud9.errors.forbidden_exception.ForbiddenException: <p>An access permissions issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit was exceeded.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many service requests were made over the given time period.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateEnvironmentEC2

            >>> client.create_environment_ec2(name='my-demo-environment', description='This is my demonstration environment.', instance_type='t2.micro', image_id='amazonlinux-2023-x86_64', subnet_id='subnet-6300cd1b', automatic_stop_time_minutes=60, owner_arn='arn:aws:iam::123456789012:user/MyDemoUser')
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.create_environment_ec2_request.CreateEnvironmentEC2Request]",
        ) -> OperationResponse[
            "capo_cloud9.types.create_environment_ec2_result.CreateEnvironmentEC2Result"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.create_environment_ec2

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.create_environment_ec2.create_environment_ec2(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.create_environment_ec2_request.CreateEnvironmentEC2Request = {
            "name": name,
            "instance_type": instance_type,
            "image_id": image_id,
        }
        if description is not None:
            input_["description"] = description
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if subnet_id is not None:
            input_["subnet_id"] = subnet_id
        if automatic_stop_time_minutes is not None:
            input_["automatic_stop_time_minutes"] = automatic_stop_time_minutes
        if owner_arn is not None:
            input_["owner_arn"] = owner_arn
        if tags is not None:
            input_["tags"] = tags
        if connection_type is not None:
            input_["connection_type"] = connection_type
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_environment_membership(
        self,
        environment_id: "capo_cloud9.types.environment_id.EnvironmentId",
        user_arn: "capo_cloud9.types.user_arn.UserArn",
        permissions: "capo_cloud9.types.member_permissions.MemberPermissions",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
    ) -> "capo_cloud9.types.create_environment_membership_result.CreateEnvironmentMembershipResult":
        """<p>Adds an environment member to an Cloud9 development environment.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            environment_id: <p>The ID of the environment that contains the environment member you want to add.</p>
            user_arn: <p>The Amazon Resource Name (ARN) of the environment member you want to add.</p>
            permissions: <p>The type of environment member permissions you want to associate with this environment member. Available values include:</p> <ul> <li> <p> <code>read-only</code>: Has read-only access to the environment.</p> </li> <li> <p> <code>read-write</code>: Has read-write access to the environment.</p> </li> </ul>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_cloud9.errors.forbidden_exception.ForbiddenException: <p>An access permissions issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit was exceeded.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many service requests were made over the given time period.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateEnvironmentMembership

            >>> client.create_environment_membership(environment_id='8d9967e2f0624182b74e7690ad69ebEX', user_arn='arn:aws:iam::123456789012:user/AnotherDemoUser', permissions='read-write')
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.create_environment_membership_request.CreateEnvironmentMembershipRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.create_environment_membership_result.CreateEnvironmentMembershipResult"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.create_environment_membership

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.create_environment_membership.create_environment_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.create_environment_membership_request.CreateEnvironmentMembershipRequest = {
            "environment_id": environment_id,
            "user_arn": user_arn,
            "permissions": permissions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_environment(
        self,
        environment_id: "capo_cloud9.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
    ) -> "capo_cloud9.types.delete_environment_result.DeleteEnvironmentResult":
        """<p>Deletes an Cloud9 development environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            environment_id: <p>The ID of the environment to delete.</p>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_cloud9.errors.forbidden_exception.ForbiddenException: <p>An access permissions issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit was exceeded.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many service requests were made over the given time period.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteEnvironment

            >>> client.delete_environment(environment_id='8d9967e2f0624182b74e7690ad69ebEX')
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.delete_environment_result.DeleteEnvironmentResult"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.delete_environment

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.delete_environment_request.DeleteEnvironmentRequest = {
            "environment_id": environment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_environment_membership(
        self,
        environment_id: "capo_cloud9.types.environment_id.EnvironmentId",
        user_arn: "capo_cloud9.types.user_arn.UserArn",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
    ) -> "capo_cloud9.types.delete_environment_membership_result.DeleteEnvironmentMembershipResult":
        """<p>Deletes an environment member from a development environment.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            environment_id: <p>The ID of the environment to delete the environment member from.</p>
            user_arn: <p>The Amazon Resource Name (ARN) of the environment member to delete from the environment.</p>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_cloud9.errors.forbidden_exception.ForbiddenException: <p>An access permissions issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit was exceeded.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many service requests were made over the given time period.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DeleteEnvironmentMembership

            >>> client.delete_environment_membership(environment_id='8d9967e2f0624182b74e7690ad69ebEX', user_arn='arn:aws:iam::123456789012:user/AnotherDemoUser')
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.delete_environment_membership_request.DeleteEnvironmentMembershipRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.delete_environment_membership_result.DeleteEnvironmentMembershipResult"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.delete_environment_membership

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.delete_environment_membership.delete_environment_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.delete_environment_membership_request.DeleteEnvironmentMembershipRequest = {
            "environment_id": environment_id,
            "user_arn": user_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_environment_memberships(
        self,
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
        user_arn: Optional["capo_cloud9.types.user_arn.UserArn"] = None,
        environment_id: Optional[
            "capo_cloud9.types.environment_id.EnvironmentId"
        ] = None,
        permissions: Optional[
            "capo_cloud9.types.permissions_list.PermissionsList"
        ] = None,
        next_token: Optional["capo_cloud9.types.string.String"] = None,
        max_results: Optional["capo_cloud9.types.max_results.MaxResults"] = None,
    ) -> "capo_cloud9.types.describe_environment_memberships_result.DescribeEnvironmentMembershipsResult":
        """<p>Gets information about environment members for an Cloud9 development environment.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            user_arn: <p>The Amazon Resource Name (ARN) of an individual environment member to get information about. If no value is specified, information about all environment members are returned.</p>
            environment_id: <p>The ID of the environment to get environment member information about.</p>
            permissions: <p>The type of environment member permissions to get information about. Available values include:</p> <ul> <li> <p> <code>owner</code>: Owns the environment.</p> </li> <li> <p> <code>read-only</code>: Has read-only access to the environment.</p> </li> <li> <p> <code>read-write</code>: Has read-write access to the environment.</p> </li> </ul> <p>If no value is specified, information about all environment members are returned.</p>
            next_token: <p>During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a <i>next token</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>
            max_results: <p>The maximum number of environment members to get information about.</p>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_cloud9.errors.forbidden_exception.ForbiddenException: <p>An access permissions issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit was exceeded.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many service requests were made over the given time period.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeEnvironmentMemberships2
            The following example gets information about the owner of the specified development environment.

            >>> client.describe_environment_memberships(permissions=['owner'], environment_id='8d9967e2f0624182b74e7690ad69ebEX')
            DescribeEnvironmentMemberships3
            The following example gets development environment membership information for the specified user.

            >>> client.describe_environment_memberships(user_arn='arn:aws:iam::123456789012:user/MyDemoUser')
            DescribeEnvironmentMemberships1
            The following example gets information about all of the environment members for the specified development environment.

            >>> client.describe_environment_memberships(environment_id='8d9967e2f0624182b74e7690ad69ebEX')
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.describe_environment_memberships_request.DescribeEnvironmentMembershipsRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.describe_environment_memberships_result.DescribeEnvironmentMembershipsResult"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.describe_environment_memberships

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.describe_environment_memberships.describe_environment_memberships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.describe_environment_memberships_request.DescribeEnvironmentMembershipsRequest = {}
        if user_arn is not None:
            input_["user_arn"] = user_arn
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if permissions is not None:
            input_["permissions"] = permissions
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

    def iter_describe_environment_memberships(
        self,
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
        user_arn: Optional["capo_cloud9.types.user_arn.UserArn"] = None,
        environment_id: Optional[
            "capo_cloud9.types.environment_id.EnvironmentId"
        ] = None,
        permissions: Optional[
            "capo_cloud9.types.permissions_list.PermissionsList"
        ] = None,
        next_token: Optional["capo_cloud9.types.string.String"] = None,
        max_results: Optional["capo_cloud9.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_cloud9.types.describe_environment_memberships_result.DescribeEnvironmentMembershipsResult]":
        _token = next_token
        while True:
            _response = self.describe_environment_memberships(
                config_overrides=config_overrides,
                user_arn=user_arn,
                environment_id=environment_id,
                permissions=permissions,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_environments(
        self,
        environment_ids: "capo_cloud9.types.bounded_environment_id_list.BoundedEnvironmentIdList",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
    ) -> "capo_cloud9.types.describe_environments_result.DescribeEnvironmentsResult":
        """<p>Gets information about Cloud9 development environments.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            environment_ids: <p>The IDs of individual environments to get information about.</p>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_cloud9.errors.forbidden_exception.ForbiddenException: <p>An access permissions issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit was exceeded.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many service requests were made over the given time period.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeEnvironments

            >>> client.describe_environments(environment_ids=['8d9967e2f0624182b74e7690ad69ebEX', '349c86d4579e4e7298d500ff57a6b2EX'])
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.describe_environments_request.DescribeEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.describe_environments_result.DescribeEnvironmentsResult"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.describe_environments

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.describe_environments.describe_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.describe_environments_request.DescribeEnvironmentsRequest = {
            "environment_ids": environment_ids
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_environment_status(
        self,
        environment_id: "capo_cloud9.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
    ) -> "capo_cloud9.types.describe_environment_status_result.DescribeEnvironmentStatusResult":
        """<p>Gets status information for an Cloud9 development environment.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            environment_id: <p>The ID of the environment to get status information about.</p>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_cloud9.errors.forbidden_exception.ForbiddenException: <p>An access permissions issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit was exceeded.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many service requests were made over the given time period.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            DescribeEnvironmentStatus

            >>> client.describe_environment_status(environment_id='8d9967e2f0624182b74e7690ad69ebEX')
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.describe_environment_status_request.DescribeEnvironmentStatusRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.describe_environment_status_result.DescribeEnvironmentStatusResult"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.describe_environment_status

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.describe_environment_status.describe_environment_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.describe_environment_status_request.DescribeEnvironmentStatusRequest = {
            "environment_id": environment_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_environments(
        self,
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
        next_token: Optional["capo_cloud9.types.string.String"] = None,
        max_results: Optional["capo_cloud9.types.max_results.MaxResults"] = None,
    ) -> "capo_cloud9.types.list_environments_result.ListEnvironmentsResult":
        """<p>Gets a list of Cloud9 development environment identifiers.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            next_token: <p>During a previous call, if there are more than 25 items in the list, only the first 25 items are returned, along with a unique string called a <i>next token</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.</p>
            max_results: <p>The maximum number of environments to get identifiers for.</p>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_cloud9.errors.forbidden_exception.ForbiddenException: <p>An access permissions issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit was exceeded.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many service requests were made over the given time period.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListEnvironments

            >>> client.list_environments()
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.list_environments_result.ListEnvironmentsResult"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.list_environments

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.list_environments_request.ListEnvironmentsRequest = {}
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

    def iter_list_environments(
        self,
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
        next_token: Optional["capo_cloud9.types.string.String"] = None,
        max_results: Optional["capo_cloud9.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_cloud9.types.list_environments_result.ListEnvironmentsResult]":
        _token = next_token
        while True:
            _response = self.list_environments(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_cloud9.types.environment_arn.EnvironmentArn",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
    ) -> (
        "capo_cloud9.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>Gets a list of the tags associated with an Cloud9 development environment.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Cloud9 development environment to get the tags for.</p>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.list_tags_for_resource

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_cloud9.types.environment_arn.EnvironmentArn",
        tags: "capo_cloud9.types.tag_list.TagList",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
    ) -> "capo_cloud9.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to an Cloud9 development environment.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important> <important> <p>Tags that you add to an Cloud9 environment by using this method will NOT be automatically propagated to underlying resources.</p> </important>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Cloud9 development environment to add tags to.</p>
            tags: <p>The list of tags to add to the given Cloud9 development environment.</p>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.concurrent_access_exception.ConcurrentAccessException: <p>A concurrent access issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.tag_resource

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_cloud9.types.environment_arn.EnvironmentArn",
        tag_keys: "capo_cloud9.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
    ) -> "capo_cloud9.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from an Cloud9 development environment.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Cloud9 development environment to remove tags from.</p>
            tag_keys: <p>The tag names of the tags to remove from the given Cloud9 development environment.</p>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.concurrent_access_exception.ConcurrentAccessException: <p>A concurrent access issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.untag_resource

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.untag_resource_request.UntagResourceRequest = {
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

    def update_environment(
        self,
        environment_id: "capo_cloud9.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
        name: Optional["capo_cloud9.types.environment_name.EnvironmentName"] = None,
        description: Optional[
            "capo_cloud9.types.environment_description.EnvironmentDescription"
        ] = None,
        managed_credentials_action: Optional[
            "capo_cloud9.types.managed_credentials_action.ManagedCredentialsAction"
        ] = None,
    ) -> "capo_cloud9.types.update_environment_result.UpdateEnvironmentResult":
        """<p>Changes the settings of an existing Cloud9 development environment.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            environment_id: <p>The ID of the environment to change settings.</p>
            name: <p>A replacement name for the environment.</p>
            description: <p>Any new or replacement description for the environment.</p>
            managed_credentials_action: <p>Allows the environment owner to turn on or turn off the Amazon Web Services managed temporary credentials for an Cloud9 environment by using one of the following values:</p> <ul> <li> <p> <code>ENABLE</code> </p> </li> <li> <p> <code>DISABLE</code> </p> </li> </ul> <note> <p>Only the environment owner can change the status of managed temporary credentials. An <code>AccessDeniedException</code> is thrown if an attempt to turn on or turn off managed temporary credentials is made by an account that's not the environment owner.</p> </note>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_cloud9.errors.forbidden_exception.ForbiddenException: <p>An access permissions issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit was exceeded.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many service requests were made over the given time period.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateEnvironment

            >>> client.update_environment(environment_id='8d9967e2f0624182b74e7690ad69ebEX', name='my-changed-demo-environment', description='This is my changed demonstration environment.')
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.update_environment_request.UpdateEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.update_environment_result.UpdateEnvironmentResult"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.update_environment

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.update_environment.update_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.update_environment_request.UpdateEnvironmentRequest = {
            "environment_id": environment_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if managed_credentials_action is not None:
            input_["managed_credentials_action"] = managed_credentials_action

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_environment_membership(
        self,
        environment_id: "capo_cloud9.types.environment_id.EnvironmentId",
        user_arn: "capo_cloud9.types.user_arn.UserArn",
        permissions: "capo_cloud9.types.member_permissions.MemberPermissions",
        *,
        config_overrides: Optional[Cloud9ClientConfig] = None,
    ) -> "capo_cloud9.types.update_environment_membership_result.UpdateEnvironmentMembershipResult":
        """<p>Changes the settings of an existing environment member for an Cloud9 development environment.</p> <important> <p>Cloud9 is no longer available to new customers. Existing customers of Cloud9 can continue to use the service as normal. <a href="http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/">Learn more"</a> </p> </important>

        Args:
            environment_id: <p>The ID of the environment for the environment member whose settings you want to change.</p>
            user_arn: <p>The Amazon Resource Name (ARN) of the environment member whose settings you want to change.</p>
            permissions: <p>The replacement type of environment member permissions you want to associate with this environment member. Available values include:</p> <ul> <li> <p> <code>read-only</code>: Has read-only access to the environment.</p> </li> <li> <p> <code>read-write</code>: Has read-write access to the environment.</p> </li> </ul>

        Raises:
            capo_cloud9.errors.bad_request_exception.BadRequestException: <p>The target request is invalid.</p>
            capo_cloud9.errors.conflict_exception.ConflictException: <p>A conflict occurred.</p>
            capo_cloud9.errors.forbidden_exception.ForbiddenException: <p>An access permissions issue occurred.</p>
            capo_cloud9.errors.internal_server_error_exception.InternalServerErrorException: <p>An internal server error occurred.</p>
            capo_cloud9.errors.limit_exceeded_exception.LimitExceededException: <p>A service limit was exceeded.</p>
            capo_cloud9.errors.not_found_exception.NotFoundException: <p>The target resource cannot be found.</p>
            capo_cloud9.errors.too_many_requests_exception.TooManyRequestsException: <p>Too many service requests were made over the given time period.</p>
            capo_cloud9.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateEnvironmentMembership

            >>> client.update_environment_membership(environment_id='8d9967e2f0624182b74e7690ad69ebEX', user_arn='arn:aws:iam::123456789012:user/AnotherDemoUser', permissions='read-only')
        """

        def _handler(
            req: "OperationRequest[capo_cloud9.types.update_environment_membership_request.UpdateEnvironmentMembershipRequest]",
        ) -> OperationResponse[
            "capo_cloud9.types.update_environment_membership_result.UpdateEnvironmentMembershipResult"
        ]:
            import capo_cloud9._operations.aws_cloud9_workspace_management_service.update_environment_membership

            output, http_response = (
                capo_cloud9._operations.aws_cloud9_workspace_management_service.update_environment_membership.update_environment_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloud9.types.update_environment_membership_request.UpdateEnvironmentMembershipRequest = {
            "environment_id": environment_id,
            "user_arn": user_arn,
            "permissions": permissions,
        }

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
