"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ServerlessApplicationRepository``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_serverlessapplicationrepository._auth._signers
import capo_serverlessapplicationrepository._auth._sigv4
from capo_serverlessapplicationrepository._auth._identity import Credentials
from capo_serverlessapplicationrepository._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_serverlessapplicationrepository._auth._zapros_handler import AuthMiddleware
from capo_serverlessapplicationrepository._pagination import (
    resolve_path as _resolve_path,
)
from capo_serverlessapplicationrepository._services._aws_config import aaws_config
from capo_serverlessapplicationrepository._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__list_of__string
    import capo_serverlessapplicationrepository.types.__list_of_application_policy_statement
    import capo_serverlessapplicationrepository.types.__list_of_parameter_value
    import capo_serverlessapplicationrepository.types.__list_of_tag
    import capo_serverlessapplicationrepository.types.__string
    import capo_serverlessapplicationrepository.types.create_application_request
    import capo_serverlessapplicationrepository.types.create_application_response
    import capo_serverlessapplicationrepository.types.create_application_version_request
    import capo_serverlessapplicationrepository.types.create_application_version_response
    import capo_serverlessapplicationrepository.types.create_cloud_formation_change_set_request
    import capo_serverlessapplicationrepository.types.create_cloud_formation_change_set_response
    import capo_serverlessapplicationrepository.types.create_cloud_formation_template_request
    import capo_serverlessapplicationrepository.types.create_cloud_formation_template_response
    import capo_serverlessapplicationrepository.types.delete_application_request
    import capo_serverlessapplicationrepository.types.get_application_policy_request
    import capo_serverlessapplicationrepository.types.get_application_policy_response
    import capo_serverlessapplicationrepository.types.get_application_request
    import capo_serverlessapplicationrepository.types.get_application_response
    import capo_serverlessapplicationrepository.types.get_cloud_formation_template_request
    import capo_serverlessapplicationrepository.types.get_cloud_formation_template_response
    import capo_serverlessapplicationrepository.types.list_application_dependencies_request
    import capo_serverlessapplicationrepository.types.list_application_dependencies_response
    import capo_serverlessapplicationrepository.types.list_application_versions_request
    import capo_serverlessapplicationrepository.types.list_application_versions_response
    import capo_serverlessapplicationrepository.types.list_applications_request
    import capo_serverlessapplicationrepository.types.list_applications_response
    import capo_serverlessapplicationrepository.types.max_items
    import capo_serverlessapplicationrepository.types.put_application_policy_request
    import capo_serverlessapplicationrepository.types.put_application_policy_response
    import capo_serverlessapplicationrepository.types.rollback_configuration
    import capo_serverlessapplicationrepository.types.unshare_application_request
    import capo_serverlessapplicationrepository.types.update_application_request
    import capo_serverlessapplicationrepository.types.update_application_response


class AsyncServerlessApplicationRepositoryClientConfig(
    TypedDict, total=False, closed=True
):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncServerlessApplicationRepositoryClient:
    """A client for the ``ServerlessApplicationRepository`` service.

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
        self._config = AsyncServerlessApplicationRepositoryClientConfig(
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
        self,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncServerlessApplicationRepositoryClientConfig = (
            config_overrides or {}
        )
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

    async def create_application(
        self,
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        author: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        description: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        home_page_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        labels: Optional[
            "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
        ] = None,
        license_body: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        license_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        name: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        readme_body: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        readme_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        semantic_version: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        source_code_archive_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        source_code_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        spdx_license_id: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        template_body: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        template_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.create_application_response.CreateApplicationResponse":
        r"""<p>Creates an application, optionally including an AWS SAM file to create the first application version in the same call.</p>

        Args:
            author: <p>The name of the author publishing the app.</p><p>Minimum length=1. Maximum length=127.</p><p>Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";</p>
            description: <p>The description of the application.</p><p>Minimum length=1. Maximum length=256</p>
            home_page_url: <p>A URL with more information about the application, for example the location of your GitHub repository for the application.</p>
            labels: <p>Labels to improve discovery of apps in search results.</p><p>Minimum length=1. Maximum length=127. Maximum number of labels: 10</p><p>Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";</p>
            license_body: <p>A local text file that contains the license of the app that matches the spdxLicenseID value of your application. The file has the format file://&lt;path>/&lt;filename>.</p><p>Maximum size 5 MB</p><p>You can specify only one of licenseBody and licenseUrl; otherwise, an error results.</p>
            license_url: <p>A link to the S3 object that contains the license of the app that matches the spdxLicenseID value of your application.</p><p>Maximum size 5 MB</p><p>You can specify only one of licenseBody and licenseUrl; otherwise, an error results.</p>
            name: <p>The name of the application that you want to publish.</p><p>Minimum length=1. Maximum length=140</p><p>Pattern: "[a-zA-Z0-9\\-]+";</p>
            readme_body: <p>A local text readme file in Markdown language that contains a more detailed description of the application and how it works. The file has the format file://&lt;path>/&lt;filename>.</p><p>Maximum size 5 MB</p><p>You can specify only one of readmeBody and readmeUrl; otherwise, an error results.</p>
            readme_url: <p>A link to the S3 object in Markdown language that contains a more detailed description of the application and how it works.</p><p>Maximum size 5 MB</p><p>You can specify only one of readmeBody and readmeUrl; otherwise, an error results.</p>
            semantic_version: <p>The semantic version of the application:</p><p> <a href="https://semver.org/">https://semver.org/</a> </p>
            source_code_archive_url: <p>A link to the S3 object that contains the ZIP archive of the source code for this version of your application.</p><p>Maximum size 50 MB</p>
            source_code_url: <p>A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.</p>
            spdx_license_id: <p>A valid identifier from <a href="https://spdx.org/licenses/">https://spdx.org/licenses/</a>.</p>
            template_body: <p>The local raw packaged AWS SAM template file of your application. The file has the format file://&lt;path>/&lt;filename>.</p><p>You can specify only one of templateBody and templateUrl; otherwise an error results.</p>
            template_url: <p>A link to the S3 object containing the packaged AWS SAM template of your application.</p><p>You can specify only one of templateBody and templateUrl; otherwise an error results.</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.conflict_exception.ConflictException: <p>The resource already exists.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.create_application

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.create_application_request.CreateApplicationRequest = {}
        if author is not None:
            input_["author"] = author
        if description is not None:
            input_["description"] = description
        if home_page_url is not None:
            input_["home_page_url"] = home_page_url
        if labels is not None:
            input_["labels"] = labels
        if license_body is not None:
            input_["license_body"] = license_body
        if license_url is not None:
            input_["license_url"] = license_url
        if name is not None:
            input_["name"] = name
        if readme_body is not None:
            input_["readme_body"] = readme_body
        if readme_url is not None:
            input_["readme_url"] = readme_url
        if semantic_version is not None:
            input_["semantic_version"] = semantic_version
        if source_code_archive_url is not None:
            input_["source_code_archive_url"] = source_code_archive_url
        if source_code_url is not None:
            input_["source_code_url"] = source_code_url
        if spdx_license_id is not None:
            input_["spdx_license_id"] = spdx_license_id
        if template_body is not None:
            input_["template_body"] = template_body
        if template_url is not None:
            input_["template_url"] = template_url

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_application_version(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        semantic_version: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        source_code_archive_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        source_code_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        template_body: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        template_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.create_application_version_response.CreateApplicationVersionResponse":
        """<p>Creates an application version.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>
            semantic_version: <p>The semantic version of the new version.</p>
            source_code_archive_url: <p>A link to the S3 object that contains the ZIP archive of the source code for this version of your application.</p><p>Maximum size 50 MB</p>
            source_code_url: <p>A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.</p>
            template_body: <p>The raw packaged AWS SAM template of your application.</p>
            template_url: <p>A link to the packaged AWS SAM template of your application.</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.conflict_exception.ConflictException: <p>The resource already exists.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.create_application_version_request.CreateApplicationVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.create_application_version_response.CreateApplicationVersionResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.create_application_version

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.create_application_version.async_create_application_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.create_application_version_request.CreateApplicationVersionRequest = {
            "application_id": application_id,
            "semantic_version": semantic_version,
        }
        if source_code_archive_url is not None:
            input_["source_code_archive_url"] = source_code_archive_url
        if source_code_url is not None:
            input_["source_code_url"] = source_code_url
        if template_body is not None:
            input_["template_body"] = template_body
        if template_url is not None:
            input_["template_url"] = template_url

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cloud_formation_change_set(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        capabilities: Optional[
            "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
        ] = None,
        change_set_name: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        client_token: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        description: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        notification_arns: Optional[
            "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
        ] = None,
        parameter_overrides: Optional[
            "capo_serverlessapplicationrepository.types.__list_of_parameter_value.__listOfParameterValue"
        ] = None,
        resource_types: Optional[
            "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
        ] = None,
        rollback_configuration: Optional[
            "capo_serverlessapplicationrepository.types.rollback_configuration.RollbackConfiguration"
        ] = None,
        semantic_version: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        stack_name: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        tags: Optional[
            "capo_serverlessapplicationrepository.types.__list_of_tag.__listOfTag"
        ] = None,
        template_id: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.create_cloud_formation_change_set_response.CreateCloudFormationChangeSetResponse":
        r"""<p>Creates an AWS CloudFormation change set for the given application.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>
            capabilities: <p>A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.</p><p>The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.</p><p>The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html">AWS::IAM::Group</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html">AWS::IAM::Policy</a>, and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html">AWS::IAM::Role</a>. If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.</p><p>The following resources require you to specify CAPABILITY_RESOURCE_POLICY: <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html">AWS::Lambda::Permission</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html">AWS::IAM:Policy</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html">AWS::ApplicationAutoScaling::ScalingPolicy</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html">AWS::S3::BucketPolicy</a>, <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html">AWS::SQS::QueuePolicy</a>, and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html">AWS::SNS:TopicPolicy</a>.</p><p>Applications that contain one or more nested applications require you to specify CAPABILITY_AUTO_EXPAND.</p><p>If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you don't specify this parameter for an application that requires capabilities, the call will fail.</p>
            change_set_name: <p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>
            client_token: <p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>
            description: <p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>
            notification_arns: <p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>
            parameter_overrides: <p>A list of parameter values for the parameters of the application.</p>
            resource_types: <p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>
            rollback_configuration: <p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>
            semantic_version: <p>The semantic version of the application:</p><p> <a href="https://semver.org/">https://semver.org/</a> </p>
            stack_name: <p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>
            tags: <p>This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a> </i> API.</p>
            template_id: <p>The UUID returned by CreateCloudFormationTemplate.</p><p>Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.create_cloud_formation_change_set_request.CreateCloudFormationChangeSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.create_cloud_formation_change_set_response.CreateCloudFormationChangeSetResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.create_cloud_formation_change_set

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.create_cloud_formation_change_set.async_create_cloud_formation_change_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.create_cloud_formation_change_set_request.CreateCloudFormationChangeSetRequest = {
            "application_id": application_id
        }
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if change_set_name is not None:
            input_["change_set_name"] = change_set_name
        if client_token is not None:
            input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if notification_arns is not None:
            input_["notification_arns"] = notification_arns
        if parameter_overrides is not None:
            input_["parameter_overrides"] = parameter_overrides
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if rollback_configuration is not None:
            input_["rollback_configuration"] = rollback_configuration
        if semantic_version is not None:
            input_["semantic_version"] = semantic_version
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if tags is not None:
            input_["tags"] = tags
        if template_id is not None:
            input_["template_id"] = template_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cloud_formation_template(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        semantic_version: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.create_cloud_formation_template_response.CreateCloudFormationTemplateResponse":
        """<p>Creates an AWS CloudFormation template.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>
            semantic_version: <p>The semantic version of the application:</p><p> <a href="https://semver.org/">https://semver.org/</a> </p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.create_cloud_formation_template_request.CreateCloudFormationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.create_cloud_formation_template_response.CreateCloudFormationTemplateResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.create_cloud_formation_template

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.create_cloud_formation_template.async_create_cloud_formation_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.create_cloud_formation_template_request.CreateCloudFormationTemplateRequest = {
            "application_id": application_id
        }
        if semantic_version is not None:
            input_["semantic_version"] = semantic_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_application(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
    ) -> None:
        """<p>Deletes the specified application.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.conflict_exception.ConflictException: <p>The resource already exists.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.delete_application

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_application(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        semantic_version: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.get_application_response.GetApplicationResponse":
        """<p>Gets the specified application.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>
            semantic_version: <p>The semantic version of the application to get.</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.get_application

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
        }
        if semantic_version is not None:
            input_["semantic_version"] = semantic_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_application_policy(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.get_application_policy_response.GetApplicationPolicyResponse":
        """<p>Retrieves the policy for the application.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.get_application_policy_request.GetApplicationPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.get_application_policy_response.GetApplicationPolicyResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.get_application_policy

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.get_application_policy.async_get_application_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.get_application_policy_request.GetApplicationPolicyRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cloud_formation_template(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        template_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.get_cloud_formation_template_response.GetCloudFormationTemplateResponse":
        r"""<p>Gets the specified AWS CloudFormation template.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>
            template_id: <p>The UUID returned by CreateCloudFormationTemplate.</p><p>Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.get_cloud_formation_template_request.GetCloudFormationTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.get_cloud_formation_template_response.GetCloudFormationTemplateResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.get_cloud_formation_template

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.get_cloud_formation_template.async_get_cloud_formation_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.get_cloud_formation_template_request.GetCloudFormationTemplateRequest = {
            "application_id": application_id,
            "template_id": template_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_application_dependencies(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        max_items: Optional[
            "capo_serverlessapplicationrepository.types.max_items.MaxItems"
        ] = None,
        next_token: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        semantic_version: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.list_application_dependencies_response.ListApplicationDependenciesResponse":
        """<p>Retrieves the list of applications nested in the containing application.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>
            max_items: <p>The total number of items to return.</p>
            next_token: <p>A token to specify where to start paginating.</p>
            semantic_version: <p>The semantic version of the application to get.</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.list_application_dependencies_request.ListApplicationDependenciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.list_application_dependencies_response.ListApplicationDependenciesResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.list_application_dependencies

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.list_application_dependencies.async_list_application_dependencies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.list_application_dependencies_request.ListApplicationDependenciesRequest = {
            "application_id": application_id
        }
        if max_items is not None:
            input_["max_items"] = max_items
        if next_token is not None:
            input_["next_token"] = next_token
        if semantic_version is not None:
            input_["semantic_version"] = semantic_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_application_dependencies(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        max_items: Optional[
            "capo_serverlessapplicationrepository.types.max_items.MaxItems"
        ] = None,
        next_token: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        semantic_version: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[capo_serverlessapplicationrepository.types.list_application_dependencies_response.ListApplicationDependenciesResponse]":
        _token = next_token
        while True:
            _response = await self.list_application_dependencies(
                application_id,
                config_overrides=config_overrides,
                max_items=max_items,
                next_token=_token,
                semantic_version=semantic_version,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_applications(
        self,
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        max_items: Optional[
            "capo_serverlessapplicationrepository.types.max_items.MaxItems"
        ] = None,
        next_token: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists applications owned by the requester.</p>

        Args:
            max_items: <p>The total number of items to return.</p>
            next_token: <p>A token to specify where to start paginating.</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.list_applications

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.list_applications_request.ListApplicationsRequest = {}
        if max_items is not None:
            input_["max_items"] = max_items
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_applications(
        self,
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        max_items: Optional[
            "capo_serverlessapplicationrepository.types.max_items.MaxItems"
        ] = None,
        next_token: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[capo_serverlessapplicationrepository.types.list_applications_response.ListApplicationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_applications(
                config_overrides=config_overrides,
                max_items=max_items,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_application_versions(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        max_items: Optional[
            "capo_serverlessapplicationrepository.types.max_items.MaxItems"
        ] = None,
        next_token: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.list_application_versions_response.ListApplicationVersionsResponse":
        """<p>Lists versions for the specified application.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>
            max_items: <p>The total number of items to return.</p>
            next_token: <p>A token to specify where to start paginating.</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.list_application_versions_request.ListApplicationVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.list_application_versions_response.ListApplicationVersionsResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.list_application_versions

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.list_application_versions.async_list_application_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.list_application_versions_request.ListApplicationVersionsRequest = {
            "application_id": application_id
        }
        if max_items is not None:
            input_["max_items"] = max_items
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_application_versions(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        max_items: Optional[
            "capo_serverlessapplicationrepository.types.max_items.MaxItems"
        ] = None,
        next_token: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "AsyncIterator[capo_serverlessapplicationrepository.types.list_application_versions_response.ListApplicationVersionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_application_versions(
                application_id,
                config_overrides=config_overrides,
                max_items=max_items,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_application_policy(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        statements: Optional[
            "capo_serverlessapplicationrepository.types.__list_of_application_policy_statement.__listOfApplicationPolicyStatement"
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.put_application_policy_response.PutApplicationPolicyResponse":
        """<p>Sets the permission policy for an application. For the list of actions supported for this operation, see <a href="https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions">Application Permissions</a> .</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>
            statements: <p>An array of policy statements applied to the application.</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.put_application_policy_request.PutApplicationPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.put_application_policy_response.PutApplicationPolicyResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.put_application_policy

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.put_application_policy.async_put_application_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.put_application_policy_request.PutApplicationPolicyRequest = {
            "application_id": application_id
        }
        if statements is not None:
            input_["statements"] = statements

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def unshare_application(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        organization_id: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> None:
        """<p>Unshares an application from an AWS Organization.</p><p>This operation can be called only from the organization's master account.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>
            organization_id: <p>The AWS Organization ID to unshare the application from.</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.unshare_application_request.UnshareApplicationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.unshare_application

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.unshare_application.async_unshare_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.unshare_application_request.UnshareApplicationRequest = {
            "application_id": application_id
        }
        if organization_id is not None:
            input_["organization_id"] = organization_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_application(
        self,
        application_id: "capo_serverlessapplicationrepository.types.__string.__string",
        *,
        config_overrides: Optional[
            AsyncServerlessApplicationRepositoryClientConfig
        ] = None,
        author: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        description: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        home_page_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        labels: Optional[
            "capo_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
        ] = None,
        readme_body: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
        readme_url: Optional[
            "capo_serverlessapplicationrepository.types.__string.__string"
        ] = None,
    ) -> "capo_serverlessapplicationrepository.types.update_application_response.UpdateApplicationResponse":
        r"""<p>Updates the specified application.</p>

        Args:
            application_id: <p>The Amazon Resource Name (ARN) of the application.</p>
            author: <p>The name of the author publishing the app.</p><p>Minimum length=1. Maximum length=127.</p><p>Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";</p>
            description: <p>The description of the application.</p><p>Minimum length=1. Maximum length=256</p>
            home_page_url: <p>A URL with more information about the application, for example the location of your GitHub repository for the application.</p>
            labels: <p>Labels to improve discovery of apps in search results.</p><p>Minimum length=1. Maximum length=127. Maximum number of labels: 10</p><p>Pattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";</p>
            readme_body: <p>A text readme file in Markdown language that contains a more detailed description of the application and how it works.</p><p>Maximum size 5 MB</p>
            readme_url: <p>A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.</p><p>Maximum size 5 MB</p>

        Raises:
            capo_serverlessapplicationrepository.errors.bad_request_exception.BadRequestException: <p>One of the parameters in the request is invalid.</p>
            capo_serverlessapplicationrepository.errors.conflict_exception.ConflictException: <p>The resource already exists.</p>
            capo_serverlessapplicationrepository.errors.forbidden_exception.ForbiddenException: <p>The client is not authenticated.</p>
            capo_serverlessapplicationrepository.errors.internal_server_error_exception.InternalServerErrorException: <p>The AWS Serverless Application Repository service encountered an internal error.</p>
            capo_serverlessapplicationrepository.errors.not_found_exception.NotFoundException: <p>The resource (for example, an access policy statement) specified in the request doesn't exist.</p>
            capo_serverlessapplicationrepository.errors.too_many_requests_exception.TooManyRequestsException: <p>The client is sending more than the allowed number of requests per unit of time.</p>
            capo_serverlessapplicationrepository.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_serverlessapplicationrepository.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_serverlessapplicationrepository.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_serverlessapplicationrepository._operations.serverless_application_repository.update_application

            (
                output,
                http_response,
            ) = await capo_serverlessapplicationrepository._operations.serverless_application_repository.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_serverlessapplicationrepository.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if author is not None:
            input_["author"] = author
        if description is not None:
            input_["description"] = description
        if home_page_url is not None:
            input_["home_page_url"] = home_page_url
        if labels is not None:
            input_["labels"] = labels
        if readme_body is not None:
            input_["readme_body"] = readme_body
        if readme_url is not None:
            input_["readme_url"] = readme_url

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
